from __future__ import annotations
import os
try:
    import resource
except ImportError:
    resource = None

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mbpp_harness_fix import (
    SYSTEM_PROMPT, build_generation_prompt, build_correction_prompt,
    parse_signature_from_tests, extract_code, ensure_expected_name,
    execute_code, solve_problem,
)

VLLM_BASE_URL = os.environ.get("VLLM_BASE_URL", "http://vllm:8000/v1")
LORA_ADAPTER_NAME = os.environ.get("LORA_ADAPTER_NAME", "mbpp-lora")

app = FastAPI(title="MBPP Code Assistant")
_http = httpx.Client(base_url=VLLM_BASE_URL, timeout=60.0)

def generate_via_vllm(prompt_text: str, temperature: float = 0.0, max_tokens: int = 384) -> str:
    try:
        resp = _http.post(
            "/chat/completions",
            json={
                "model": LORA_ADAPTER_NAME,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt_text},
                ],
                "temperature": temperature,
                "max_tokens": max_tokens,
            },
        )
        resp.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"vLLM backend error: {e}")
    return resp.json()["choices"][0]["message"]["content"]

def _limit_resources():
    if resource is not None:
        resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
        resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024,) * 2)
        resource.setrlimit(resource.RLIMIT_NPROC, (1, 1))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))

def execute_hardened(code: str, test_list: list[str], timeout: int = 5) -> dict:
    return execute_code(code, test_list, timeout=timeout, preexec_fn=_limit_resources)

class ProblemRequest(BaseModel):
    problem_text: str
    test_list: list[str]
    max_corrections: int = 2

class GenerateResponse(BaseModel):
    code: str | None
    function_name: str | None = None

class EvaluateRequest(BaseModel):
    code: str
    test_list: list[str]

class SolveResponse(BaseModel):
    status: str
    round: int | None = None
    code: str | None = None
    attempts: list

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate", response_model=GenerateResponse)
def generate(req: ProblemRequest):
    sig = parse_signature_from_tests(req.test_list)
    if sig is None:
        raise HTTPException(status_code=422, detail="couldn't parse a call signature from test_list")
    raw = generate_via_vllm(build_generation_prompt(req.problem_text, sig))
    code = extract_code(raw)
    if code is not None:
        code = ensure_expected_name(code, sig["name"])
    return GenerateResponse(code=code, function_name=sig["name"])

@app.post("/evaluate")
def evaluate_endpoint(req: EvaluateRequest):
    return execute_hardened(req.code, req.test_list)

@app.post("/solve", response_model=SolveResponse)
def solve(req: ProblemRequest):
    result = solve_problem(
        req.problem_text, req.test_list, generate_via_vllm,
        max_corrections=req.max_corrections, execute_fn=execute_hardened,
    )
    if result["status"] == "SKIPPED":
        raise HTTPException(status_code=422, detail=result["detail"])
    return SolveResponse(
        status=result["status"],
        round=result.get("round"),
        code=result.get("code"),
        attempts=result.get("attempts", []),
    )
