# Product Requirements Document (PRD)
### Qwen2.5-Coder — Autonomous AI Code Generation & Reflection Assistant

This document outlines the product requirements, target user personas, core features, and architectural goals for the **Qwen2.5-Coder** software engineering system.

---

## Document Metadata

<div style="background-color: #0F172A; border: 1px solid #1E293B; border-radius: 8px; padding: 18px 20px; margin: 14px 0;">
  <table width="100%" cellpadding="0" cellspacing="6" border="0">
    <tr>
      <td width="20%"><span style="color: #64748B; font-size: 12px; font-weight: 600;">Version:</span></td>
      <td><code style="color: #F8FAFC; font-size: 12px;">1.0</code></td>
    </tr>
    <tr>
      <td><span style="color: #64748B; font-size: 12px; font-weight: 600;">Date:</span></td>
      <td><span style="color: #F8FAFC; font-size: 12px;">October 31, 2026</span></td>
    </tr>
    <tr>
      <td><span style="color: #64748B; font-size: 12px; font-weight: 600;">Author:</span></td>
      <td><span style="color: #F8FAFC; font-size: 12px; font-weight: 600;">Abhishek Perumalla</span></td>
    </tr>
    <tr>
      <td><span style="color: #64748B; font-size: 12px; font-weight: 600;">Status:</span></td>
      <td><span style="background-color: #065F46; color: #A7F3D0; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: 600; letter-spacing: 0.03em;">PRODUCTION RELEASE</span></td>
    </tr>
    <tr>
      <td><span style="color: #64748B; font-size: 12px; font-weight: 600;">Target Launch:</span></td>
      <td><code style="color: #F8FAFC; font-size: 12px;">MVP (v1.0)</code></td>
    </tr>
  </table>
</div>

---

### 1. Product Overview

**Qwen2.5-Coder** is an end-to-end, self-correcting software development agent powered by `Qwen2.5-Coder-3B-Instruct` fine-tuned via Low-Rank Adaptation (LoRA). It couples generative code synthesis with a real-time, POSIX-hardened execution sandbox. If generated code yields any runtime, syntax, or assertion failure, the system automatically intercepts the execution traceback, constructs a reflective repair prompt, and autonomously repairs the solution until 100% of test assertions pass.

---

### 2. Problem Statement

Software engineers frequently encounter frustrating friction when using standard generative AI assistants:
* **Hallucinated Logic & Syntax**: Conventional foundation models emit plausible-looking code that fails during compilation or edge-case execution.
* **Absence of Runtime Feedback**: LLMs cannot execute the code they synthesize, leading to broken unit tests and subtle regressions.
* **Manual Debugging Overhead**: Developers must manually copy runtime tracebacks and repeatedly re-prompt the assistant to get a fix.
* **Host Execution Vulnerabilities**: Running AI-generated code directly on local machines risks CPU denial-of-service, memory leaks, and unauthorized file system access.

---

### 3. Goals

* **100% Deterministic Pass Rate**: Achieve full autonomous resolution across standard algorithmic benchmarks (MBPP).
* **Zero-Touch Self-Correction**: Automatically intercept errors and heal failing code through reflection loops without developer prompts.
* **Hardened Sandbox Isolation**: Restrict CPU time (5s), virtual memory (256 MB), processes (1), and open file descriptors (64) per test execution.
* **Low-Latency Serving**: Serve inferences in under 6.5s per round via vLLM and FastAPI.
* **Production Containerization**: Provide a one-command multi-container Docker Compose deployment stack.

---

### 4. Target Users

* **Software Engineers & Developers**: Requiring verified algorithmic implementations and bug-free boilerplate code.
* **Automated CI/CD Bot Agents**: Autonomous bots resolving failing unit tests in pull requests prior to human review.
* **Competitive Programmers & Students**: Real-time feedback, traceback explanation, and algorithmic optimizations.
* **Multi-Agent Systems**: High-reliability code execution and verification layer for developer tooling agents.

---

### 5. Core Features (MVP)

1. **Fine-Tuned LoRA Adapter**: Specialized Qwen2.5-3B weights with training loss converged from `2.46` to `0.27`.
2. **Deterministic Code Extractor & Normalizer**: Markdown code fence parser and AST function aliaser (`ensure_expected_name`).
3. **Hardened POSIX Sandbox**: Subprocess execution isolation enforcing `RLIMIT_CPU`, `RLIMIT_AS`, `RLIMIT_NPROC`, and `RLIMIT_NOFILE`.
4. **Autonomous Self-Correction Reflection Loop**: Closed-loop prompt repair mechanism handling runtime tracebacks and unit test failures.
5. **High-Throughput FastAPI REST Service**:
   * `POST /generate`: Fast zero-shot code synthesis.
   * `POST /evaluate`: Hardened sandboxed test runner.
   * `POST /solve`: End-to-end generation, verification, and autonomous reflection loop.
6. **Production Docker Deployment**: Fully orchestrated multi-container deployment linking vLLM serving and FastAPI API.

---

### 6. Non-Functional Requirements

* **Performance**: Generation latency $< 6.5$ seconds under vLLM PagedAttention continuous batching.
* **Security**: Zero file system mutation outside ephemeral execution boundaries; zero socket leaks.
* **Availability**: 99.9% uptime for the FastAPI REST gateway service.
