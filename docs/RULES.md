# Development Rules
### Qwen2.5-Coder — Engineering Standards and Collaboration Guidelines

This document defines the development rules, coding standards, and best practices to be followed while building and maintaining the **Qwen2.5-Coder** software engineering platform. These rules ensure architectural consistency, maintainability, execution safety, and high code quality. Both AI assistants (Cursor, Antigravity) and human contributors must strictly observe these directives.

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">1</span> General Principles
*These rules apply to the entire project.*

<div style="background-color: #0F172A; border-left: 4px solid #2563EB; border-radius: 6px; padding: 16px 20px; margin: 12px 0;">
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Follow the project documentation</b> (<code>PRD.md</code>, <code>ARCHITECTURE.md</code>, <code>DESIGN.md</code>) before implementing changes.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Keep code clean, readable, and well-structured.</b> Prioritize simplicity over abstraction.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Do not duplicate logic.</b> Reuse existing components, sandbox runners, or helper utilities.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Make small, focused changes</b> instead of large, high-risk diffs.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Do not modify unrelated files.</b> Never touch model weights when refactoring API logic.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; <b>Write self-explanatory code</b> with meaningful variable, argument, and function names.</p>
</div>

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">2</span> Technology & Coding Standards
*Rules related to the core tech stack and coding style:*

| Category | Standard & Directive |
| :-- | :-- |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Language</span> | Use **Python 3.11+** with strict typing annotations (`list[str]`, `dict[str, Any]`, `str \| None`). |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Framework</span> | Follow **FastAPI** best practices; use Pydantic v2 schemas for all request/response models. |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Async I/O</span> | Use connection-pooled **HTTPX** (`httpx.Client`) with strict timeouts (`timeout=60.0`). |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Linting</span> | Follow **PEP 8** style guidelines; clean all syntax warnings before staging commits. |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Formatting</span> | Use **Black** or **Ruff** for consistent formatting (100 character maximum line length). |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">Dependencies</span> | Use locked packages in `requirements.txt`. Avoid introducing unvetted external libraries. |
| <span style="background-color: #1E293B; color: #94A3B8; border: 1px solid #334155; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">File Naming</span> | Use clean snake_case for Python modules (`mbpp_harness_fix.py`, `app.py`). |

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">3</span> Project Structure
*Follow the defined directory boundaries in <code>ARCHITECTURE.md</code>:*

<div style="background-color: #0F172A; border-left: 4px solid #2563EB; border-radius: 6px; padding: 16px 20px; margin: 12px 0;">
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; Architecture specifications and design governance strictly reside inside <code>/docs</code>.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; Model checkpoints and safetensors live inside <code>/qwen2.5-3b-coder-lora-v3</code> (read-only).</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; Gateway routing and endpoint serialization must stay inside <code>app.py</code>.</p>
  <p style="margin: 6px 0; color: #F8FAFC;">&bull; Sandboxing, execution isolation, and prompt reflection logic reside in <code>mbpp_harness_fix.py</code>.</p>
</div>

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">4</span> Sandbox Isolation & Security Guidelines

* **Enforce Resource Throttles**: Never bypass POSIX `setrlimit` boundaries (`RLIMIT_CPU: 5s`, `RLIMIT_AS: 256MB`, `RLIMIT_NPROC: 1`, `RLIMIT_NOFILE: 64`).
* **Process Termination**: Terminate unresponsive or runaway execution threads with `SIGKILL` upon timeout.
* **Hermetic Execution**: Subprocesses must never inherit host secrets, credentials, or network sockets.

---

### <span style="background-color: #2563EB; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">5</span> AI Collaboration Guidelines (Cursor & Agent Rules)

* **Read `MEMORY.md` First**: Always verify active phase, constraints, and decisions before generating code.
* **No Speculative Breaking Changes**: Preserve existing REST API contracts (`POST /solve`, `POST /evaluate`).
* **Maintain Documentation Sync**: Whenever completing tasks or resolving edge cases, update `TASKS.md` and `MEMORY.md`.

---

### <span style="background-color: #DC2626; color: white; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; margin-right: 6px;">6</span> Prohibited Patterns

* **Do not** execute untrusted user code via `eval()` or `exec()` in the main thread.
* **Do not** remove CPU or memory bounds to artificially accelerate execution.
* **Do not** hardcode local machine paths (`C:\Users\...`). Always use environment variables and relative paths.
* **Do not** modify fine-tuned adapter safetensors without versioned checkpoints.
