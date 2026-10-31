# Development Rules

**Qwen2.5-Coder Autonomous AI Code Generation Engine**  
*Project Guidelines for AI Assistants & Human Collaboration*

---

This document defines the development rules, coding standards, security guardrails, and best practices to be followed when contributing to the Qwen2.5-Coder repository. These rules ensure system consistency, maintainability, execution safety, and high-quality software engineering. Both AI assistants (Cursor, Antigravity) and human contributors must strictly observe these directives.

---

## 1. General Principles

* **Adhere to Project Documentation**: Always consult `PRD.md` and `ARCHITECTURE.md` before implementing architectural alterations.
* **Keep Code Clean, Readable & Well-Structured**: Code is read far more often than it is written.
* **Prioritize Simplicity & Maintainability**: Avoid premature over-engineering. Write straightforward, verifiable logic.
* **Do Not Duplicate Logic**: Always reuse existing utility functions in `mbpp_harness_fix.py` and `app.py`.
* **Make Small, Focused Changes**: Keep commits atomic and isolated to a single concern.
* **Do Not Modify Unrelated Files**: Never touch training notebooks or LoRA weights when refactoring API logic.
* **Write Self-Explanatory Code**: Code should be expressive, augmented by type hints and concise docstrings.

---

## 2. Technology & Coding Standards

| Standard | Rule / Requirement |
| :--- | :--- |
| **Language** | Python 3.11+ strictly typed with `typing` annotations (`list[str]`, `dict[str, Any]`, `str \| None`). |
| **Framework** | FastAPI using Pydantic v2 schemas for all request/response models. |
| **HTTP Client** | Asynchronous / Pooled `httpx.Client` with strict timeouts (`timeout=60.0`). |
| **Linting & Style** | PEP 8 compliance, formatted via Black / Ruff. Maximum line length: 100 characters. |
| **Dependencies** | Strict pinning in `requirements.txt`. Do not introduce unvetted heavy dependencies. |
| **File Naming** | Snake_case for Python modules (`mbpp_harness_fix.py`), kebab-case for config files (`docker-compose.yml`). |

---

## 3. Project Structure & Boundary Rules

1. **`docs/`**: Sole home for architectural guidelines, design tokens, tasks, and memory state. No code files.
2. **`qwen2.5-3b-coder-lora-v3/`**: Read-only directory containing serialized LoRA safetensors and tokenizer configs. Do not overwrite or reformat manually.
3. **`app.py`**: Handles network I/O, API routing, serialization, and high-level orchestration. Must remain lightweight.
4. **`mbpp_harness_fix.py`**: Houses core algorithmic parsing, AST inspection, sandbox isolation, and self-correction loops.

---

## 4. Sandbox Isolation & Security Guidelines

* **Never Execute Code on the Root Host**: All dynamically synthesized code must pass through `execute_hardened()`.
* **Resource Limits Are Mandatory**: Never disable or bypass `setrlimit` constraints (`RLIMIT_CPU`, `RLIMIT_AS`, `RLIMIT_NPROC`).
* **Process Termination**: Any subprocess exceeding `timeout` (default: 5.0 seconds) must be sent `SIGKILL` immediately.
* **Environment Scrubbing**: Subprocesses must never inherit sensitive host environment variables (API keys, credentials).

---

## 5. Testing & Verification Requirements

* **Zero Regressions**: Any modification to `mbpp_harness_fix.py` must maintain a 100% pass rate across the 43-problem benchmark.
* **Mock vLLM in Unit Tests**: API gateway test suites must mock vLLM HTTP responses to run hermetically without requiring GPU hardware.
* **Validate Edge Cases**: Verify that syntax errors, division by zero, infinite recursion, and memory leaks are cleanly caught and classified.

---

## 6. Git & Version Control

* **Commit Message Format**: Follow Conventional Commits:
  * `feat: add AST function aliasing for multi-argument test fixtures`
  * `fix: prevent zombie processes when timeout triggered in sandbox`
  * `docs: update ARCHITECTURE.md with vLLM PagedAttention specs`
* **Clean Working Tree**: Never commit temporary files (`.pytest_cache`, `__pycache__`, `.ipynb_checkpoints`).

---

## 7. AI Collaboration Guidelines (Cursor / Antigravity Rules)

1. **Check `MEMORY.md` First**: Read the current state, active phase, and known constraints before executing changes.
2. **Never Hallucinate External Tools**: Use only installed libraries specified in `requirements.txt`.
3. **No Breaking Interface Changes**: Preserve public API endpoints (`/generate`, `/evaluate`, `/solve`) and their schema models.
4. **Update `TASKS.md` & `MEMORY.md`**: When completing tasks or resolving edge cases, update documentation status in the same session.

---

## 8. What NOT to Do

* ❌ **DO NOT** remove POSIX resource limits to "speed up execution".
* ❌ **DO NOT** execute user code via `eval()` or `exec()` in the main thread.
* ❌ **DO NOT** hardcode host paths (`/home/user/...`). Use relative paths and environment variables.
* ❌ **DO NOT** modify the LoRA weights directory without versioned checkpointing.
* ❌ **DO NOT** permit unescaped user code to manipulate file system state or open outward network sockets.

---

## 9. Definition of Done (DoD)

A task or pull request is strictly considered complete when:
1. All Python code passes type checks and is properly documented.
2. The endpoint responds within the defined latency SLA (< 6.5s).
3. The sandbox reliably handles error states without leaking memory or zombie processes.
4. The change is verified against the test harness.
5. `MEMORY.md` and `TASKS.md` are updated to reflect the new state.

