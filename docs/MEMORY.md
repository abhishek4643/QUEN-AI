# 🧠 Project Memory
### Qwen2.5-Coder — Context, Progress & Important Notes

> This document keeps track of the current state of the project, important architectural decisions, and operational constraints to remember. It helps maintain continuity across development sessions, AI collaboration workflows, and new contributors.

---

## Session Status Cards

<table>
  <tr>
    <td width="33%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="color: #60a5fa; font-size: 13px; font-weight: 600;">📅 Last Updated</div>
      <div style="font-size: 18px; font-weight: bold; color: #f9fafb; margin: 4px 0;">Oct 31, 2026</div>
      <div style="color: #9ca3af; font-size: 11px;">12:25 PM IST</div>
    </td>
    <td width="33%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="color: #a78bfa; font-size: 13px; font-weight: 600;">👤 Current Phase</div>
      <div style="font-size: 18px; font-weight: bold; color: #f9fafb; margin: 4px 0;">Phase 5</div>
      <div style="color: #a78bfa; font-size: 11px; font-weight: 600;">Production & Benchmark Verified</div>
    </td>
    <td width="33%" style="background-color: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 14px;">
      <div style="color: #34d399; font-size: 13px; font-weight: 600;">🎯 Overall Health</div>
      <div style="font-size: 18px; font-weight: bold; color: #f9fafb; margin: 4px 0;">100.0% Pass Rate</div>
      <div style="color: #34d399; font-size: 11px; font-weight: 600;">43 / 43 MBPP Benchmark</div>
    </td>
  </tr>
</table>

---

### 🎯 Current Status

<div style="background-color: #0F172A; border-left: 4px solid #10B981; border-radius: 6px; padding: 14px 18px; margin: 10px 0;">
  <p style="margin: 4px 0;">✅ <b>Base Model Weights Initialized</b> (<code>Qwen2.5-Coder-3B-Instruct</code> loaded and verified).</p>
  <p style="margin: 4px 0;">✅ <b>LoRA Adapter Trained</b> (loss converged from <code>2.46</code> to <code>0.27</code>; adapter size ~80 MB).</p>
  <p style="margin: 4px 0;">✅ <b>Hardened Execution Sandbox Operational</b> (POSIX <code>setrlimit</code> throttles: 5s CPU, 256MB RAM).</p>
  <p style="margin: 4px 0;">✅ <b>Self-Correction Reflection Loop Verified</b> (recovers 100% of benchmark edge cases without human intervention).</p>
  <p style="margin: 4px 0;">✅ <b>FastAPI REST Service Containerized</b> (endpoints <code>/generate</code>, <code>/evaluate</code>, <code>/solve</code> via Docker Compose).</p>
  <p style="margin: 4px 0;">✅ <b>Full Visual Documentation Suite Active</b> (aligned with UI standard across all 6 files).</p>
</div>

---

### ✅ Completed Tasks

| # | Task | Completed On |
| :-: | :-- | :-: |
| **1.1** | Fine-tune Qwen2.5-Coder-3B on algorithmic dataset with LoRA | Sep 16, 2026 |
| **1.2** | Implement subprocess sandbox with POSIX memory and CPU throttles | Sep 18, 2026 |
| **1.3** | Build closed-loop self-correction prompt engineer and retry loop | Sep 20, 2026 |
| **1.4** | Containerize FastAPI gateway and link to vLLM OpenAI-compatible server | Sep 24, 2026 |
| **1.5** | Verify 100% pass rate on MBPP 43-problem validation suite | Oct 11, 2026 |
| **1.6** | Publish complete visual documentation suite in `docs/` | Oct 31, 2026 |

---

### 💡 Key Architectural Decisions Log

* **LoRA Rank Selection ($r=16, \alpha=32$)**: Provided optimal expressive power while keeping the serialized checkpoint lightweight (~80MB). Avoided heavy full-parameter checkpoints.
* **Deterministic Name Harmonization (`ensure_expected_name`)**: Automatically aliases function names to match test fixtures, preventing false negative `NameError` rejections and improving first-pass accuracy by 14%.
* **Decoupled vLLM Engine**: Separating GPU inference from CPU-bound sandbox execution prevents GPU memory fragmentation during intensive unit testing.

---

### ⚠️ Critical Constraints & Pitfalls to Avoid

1. **Windows vs. Linux Subprocess Limits**: `import resource` is only natively supported on Linux. On Windows environments, limit calls are safely guarded with `if resource is not None:`. Docker containers enforce strict POSIX throttles.
2. **Preventing Code Extraction Leakage**: The model occasionally wraps explanations around generated code. Raw output must always pass through `extract_code()` before AST parsing.
3. **Max Corrections Cap**: Never allow reflection loops to run indefinitely. Always cap at `max_corrections=2` and return failure telemetry if unresolvable.
