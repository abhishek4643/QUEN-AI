# 📄 Development Rules
### Qwen2.5-Coder — Project Guidelines for AI & Human Collaboration

> This document defines the development rules, coding standards, and best practices to be followed while building the **Qwen2.5-Coder** software engineering platform. These rules ensure consistency, maintainability, security, and high-quality code. Both AI assistants (Cursor, Antigravity) and human contributors must strictly follow these guidelines.

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">1</span> General Principles
*These rules apply to the entire project.*

<div style="background-color: #0F172A; border-left: 4px solid #2563EB; border-radius: 6px; padding: 14px 18px; margin: 10px 0;">
  <p style="margin: 4px 0;">✅ <b>Follow the project documentation</b> (<code>PRD.md</code>, <code>ARCHITECTURE.md</code>, <code>DESIGN.md</code>) before making changes.</p>
  <p style="margin: 4px 0;">✅ <b>Keep the code clean, readable and well-structured.</b></p>
  <p style="margin: 4px 0;">✅ <b>Prioritize simplicity and maintainability.</b> Avoid unnecessary abstractions.</p>
  <p style="margin: 4px 0;">✅ <b>Do not duplicate logic.</b> Reuse existing components, sandbox runners, or helper services.</p>
  <p style="margin: 4px 0;">✅ <b>Make small, focused changes</b> instead of large, risky edits.</p>
  <p style="margin: 4px 0;">✅ <b>Do not modify unrelated files.</b> Never touch training adapters when updating REST endpoints.</p>
  <p style="margin: 4px 0;">✅ <b>Write self-explanatory code</b> with meaningful variable, argument, and function names.</p>
</div>

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">2</span> Technology & Coding Standards
*Rules related to the tech stack and coding style:*

| Category | Standard & Directive |
| :-- | :-- |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Language</span> | Use **Python 3.11+** with strict typing annotations (`list[str]`, `dict[str, Any]`, `str \| None`). |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Framework</span> | Follow **FastAPI** best practices; use Pydantic v2 schemas for all request/response models. |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Async I/O</span> | Use connection-pooled **HTTPX** (`httpx.Client`) with strict timeouts (`timeout=60.0`). |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Linting</span> | Follow **PEP 8** style guidelines; clean all syntax warnings before committing. |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Formatting</span> | Use **Black** or **Ruff** for consistent code formatting (100 character max line length). |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">Dependencies</span> | Use stable, locked packages in `requirements.txt`. Avoid unnecessary heavy dependencies. |
| <span style="background-color: #1E3A8A; color: #93C5FD; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">File Naming</span> | Use clean snake_case for Python modules (`mbpp_harness_fix.py`, `app.py`). |

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">3</span> Project Structure
*Follow the defined directory structure in <code>ARCHITECTURE.md</code> to keep things organized and scalable:*

<div style="background-color: #0F172A; border-left: 4px solid #2563EB; border-radius: 6px; padding: 14px 18px; margin: 10px 0;">
  <p style="margin: 4px 0;">📁 Architecture and system governance must strictly reside inside <code>/docs</code>.</p>
  <p style="margin: 4px 0;">📁 Model checkpoints and safetensors live inside <code>/qwen2.5-3b-coder-lora-v3</code> (read-only).</p>
  <p style="margin: 4px 0;">📁 Gateway routing and endpoint serialization must stay inside <code>app.py</code>.</p>
  <p style="margin: 4px 0;">📁 Sandboxing, execution isolation, and prompt reflection logic reside in <code>mbpp_harness_fix.py</code>.</p>
</div>

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">4</span> Sandbox Isolation & Security Guidelines

* **Enforce Resource Throttles**: Never bypass POSIX `setrlimit` boundaries (`RLIMIT_CPU: 5s`, `RLIMIT_AS: 256MB`, `RLIMIT_NPROC: 1`).
* **Process Killing**: Terminate unresponsive or runaway execution threads with `SIGKILL` upon timeout.
* **Hermetic Execution**: Subprocesses must never inherit sensitive host secrets, tokens, or environment variables.

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">5</span> AI Collaboration Guidelines (Cursor & Agent Rules)

* **Read `MEMORY.md` First**: Always check active phase and constraints before generating or editing code.
* **No Speculative Breaking Changes**: Preserve existing REST API schemas (`POST /solve`, `POST /evaluate`).
* **Keep Docs Synchronized**: Whenever adding features or resolving bugs, update `TASKS.md` and `MEMORY.md`.

---

### <span style="background-color: #DC2626; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; font-size: 13px; margin-right: 6px;">6</span> What NOT to Do

* ❌ **DO NOT** execute untrusted user-generated code via `eval()` or `exec()` in the main thread.
* ❌ **DO NOT** remove CPU or memory bounds to artificially accelerate execution.
* ❌ **DO NOT** hardcode local machine paths (`C:\Users\...`). Always use environment variables and relative paths.
* ❌ **DO NOT** modify fine-tuned adapter safetensors without versioned backup checkpoints.
