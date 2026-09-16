from __future__ import annotations
import ast
import re
import subprocess
import sys

SAFE_PRELUDE = """\
import re, math, cmath, itertools, functools, string, sys
from collections import Counter, defaultdict, OrderedDict, deque
from itertools import combinations, permutations, product
from heapq import heappush, heappop, heapify
"""

_DEF_PAT = re.compile(r"^\s*def\s+\w+\s*\(")
_IMPORT_PAT = re.compile(r"^\s*(?:import|from)\s+\S")

SYSTEM_PROMPT = (
    "You are an expert Python programmer who writes correct, efficient, "
    "self-contained solutions."
)

def parse_signature_from_tests(test_list: list[str]) -> dict | None:
    for test in test_list:
        try:
            tree = ast.parse(test.strip())
        except SyntaxError:
            continue
        if not tree.body or not isinstance(tree.body[0], ast.Assert):
            continue
        test_expr = tree.body[0].test
        call_node = None
        if isinstance(test_expr, ast.Compare) and isinstance(test_expr.left, ast.Call):
            call_node = test_expr.left
        elif isinstance(test_expr, ast.Call):
            call_node = test_expr
        if call_node is not None and isinstance(call_node.func, ast.Name):
            return {
                "name": call_node.func.id,
                "n_args": len(call_node.args),
                "example_call": test.strip(),
            }
    return None

def build_generation_prompt(problem_text: str, sig: dict) -> str:
    return (
        f"Solve this problem:\n{problem_text}\n\n"
        f"Your function MUST be named exactly `{sig['name']}` and MUST work "
        f"with this exact call (it is one of the real tests that will run "
        f"against your code):\n"
        f"    {sig['example_call']}\n\n"
        f"Put any `import` statements you need at the top of the code. "
        f"Return ONLY one fenced ```python code block — no explanation "
        f"before or after it."
    )

def build_correction_prompt(problem_text: str, sig: dict, failed_code: str | None, result: dict) -> str:
    return (
        f"Your previous solution for this problem failed.\n\n"
        f"Problem:\n{problem_text}\n\n"
        f"Required call (must keep working):\n    {sig['example_call']}\n\n"
        f"Your code:\n```python\n{failed_code or '(no valid code was produced)'}\n```\n\n"
        f"Failure ({result['status']}):\n{(result.get('detail') or '')[-600:]}\n\n"
        f"Fix the bug. Keep the function name `{sig['name']}` and its "
        f"{sig['n_args']}-argument signature exactly as shown. Include every "
        f"`import` you use. Return ONLY one fenced ```python code block."
    )

def extract_code(generated_text: str) -> str | None:
    fence = re.search(r"```(?:python)?\s*\n?(.*?)```", generated_text, re.DOTALL)
    code = fence.group(1) if fence else generated_text
    lines = code.splitlines()

    if not any(_DEF_PAT.match(l) for l in lines):
        return None

    if fence:
        return code.strip()

    start = next((i for i, l in enumerate(lines) if _DEF_PAT.match(l) or _IMPORT_PAT.match(l)), None)
    if start is None:
        return None
    end = start
    for i in range(start, len(lines)):
        l = lines[i]
        if l.strip() == "" or l.startswith((" ", "\t")) or _DEF_PAT.match(l) or _IMPORT_PAT.match(l):
            end = i
        else:
            break
    return "\n".join(lines[start:end + 1]).strip()

def ensure_expected_name(code: str, expected_name: str) -> str:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return code
    top_level = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
    if expected_name in top_level or len(top_level) != 1:
        return code
    return code + f"\n\n{expected_name} = {top_level[0]}\n"

def build_runnable(code: str) -> str:
    return SAFE_PRELUDE + "\n" + code

def execute_code(code: str, test_list: list[str], timeout: int = 5, preexec_fn=None) -> dict:
    script = build_runnable(code) + "\n\n" + "\n".join(test_list) + "\nprint('__ALL_TESTS_PASSED__')\n"
    try:
        kwargs = {}
        if preexec_fn is not None and sys.platform != "win32":
            kwargs["preexec_fn"] = preexec_fn
        proc = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, timeout=timeout, **kwargs)
    except subprocess.TimeoutExpired:
        return {"status": "TIMEOUT", "detail": f"exceeded {timeout}s"}

    if proc.returncode == 0 and "__ALL_TESTS_PASSED__" in proc.stdout:
        return {"status": "PASS", "detail": None}

    stderr = proc.stderr.strip()
    if "SyntaxError" in stderr:
        return {"status": "SYNTAX_ERROR", "detail": stderr[-500:]}
    if "AssertionError" in stderr:
        return {"status": "WRONG_ANSWER", "detail": stderr[-500:]}
    return {"status": "RUNTIME_ERROR", "detail": stderr[-500:] or proc.stdout[-500:] or "unknown failure"}

def solve_problem(problem_text: str, test_list: list[str], generate_fn, max_corrections: int = 2, execute_fn=None) -> dict:
    if execute_fn is None:
        execute_fn = execute_code

    sig = parse_signature_from_tests(test_list)
    if sig is None:
        return {"status": "SKIPPED", "detail": "couldn't parse a call signature from test_list", "attempts": []}

    raw = generate_fn(build_generation_prompt(problem_text, sig))
    code = extract_code(raw)
    attempts = []

    for round_idx in range(max_corrections + 1):
        if code is None:
            result = {"status": "EXTRACTION_FAILED", "detail": "no `def` found in model output"}
        else:
            code = ensure_expected_name(code, sig["name"])
            result = execute_fn(code, test_list)
        attempts.append({"round": round_idx, "code": code, "result": result})

        if result["status"] == "PASS":
            return {"status": "PASS", "round": round_idx, "code": code, "attempts": attempts}
        if round_idx == max_corrections:
            break

        raw = generate_fn(build_correction_prompt(problem_text, sig, code, result))
        code = extract_code(raw)

    return {"status": "FAIL", "attempts": attempts}
