# Product Requirements Document (PRD)

**Qwen2.5-Coder Autonomous AI Code Generation & Self-Correction Engine**  
*Production-Grade Generative Code Assistant with Real-Time Sandboxed Execution & Autonomous Reflection*

---

| Metadata | Specification |
| :--- | :--- |
| **Version** | 1.0 |
| **Date** | October 2026 |
| **Author** | Abhishek Perumalla |
| **Status** | Production / Benchmark Verified |
| **Target Launch** | MVP (v1.0) |

---

## 1. Product Overview

The **Qwen2.5-Coder Autonomous AI Code Generation Engine** is an end-to-end, self-correcting software development agent powered by `Qwen2.5-Coder-3B-Instruct` fine-tuned via Low-Rank Adaptation (LoRA). 

Unlike standard LLM code generation tools that output code without runtime validation, this engine establishes a closed-loop execution and reflection environment. Generated solutions are dynamically compiled and executed against rigorous assertions within a hardened OS-level sandbox. If execution yields an error (syntax, runtime, timeout, or logic failure), the system intercepts the execution traceback, constructs a reflective repair prompt, and autonomously corrects the code until 100% of test assertions pass.

---

## 2. Problem Statement

Modern software engineers and automated workflows suffer from the reliability gap in AI code generation:
1. **Hallucinated Syntax & Signatures**: Foundation models frequently hallucinate deprecated APIs, incorrect function signatures, or misaligned parameter types.
2. **Zero Runtime Feedback**: Conventional code assistants emit code into the IDE without deterministic verification against target test cases.
3. **Manual Human Debugging Loop**: When AI-generated code fails, developers spend significant time manually reading tracebacks and re-prompting the model.
4. **Execution Security Risks**: Running untrusted AI-generated code on developer workstations exposes systems to fork-bombs, memory exhaustion, and unauthorized file access.

---

## 3. Goals & Success Metrics

* **100% Test Pass Rate**: Achieve full autonomous resolution across standard algorithmic benchmarks (MBPP).
* **Zero Human Intervention**: Automatically intercept errors and heal failing code through reflection loops without developer prompts.
* **Hardened Sandbox Isolation**: Restrict CPU time (5s), virtual memory (256 MB), processes (1), and open file descriptors (64) per test execution.
* **Low-Latency Serving**: Serve inferences in under 6.5s per round via vLLM and FastAPI.
* **Multi-Language Adaptability**: Support dynamic sandboxed execution for Python, C, and C++.

---

## 4. Target Users

* **Software Engineers & Developers**: Requiring verified algorithmic implementations and bug-free boilerplate generation.
* **Automated CI/CD Pipelines**: Automated bot repairing broken unit tests in pull requests autonomously.
* **Competitive Programmers & Students**: Real-time feedback and explanation of runtime bugs and algorithmic optimizations.
* **Autonomous Agent Platforms**: Backend code execution and verification layer for multi-agent workflows.

---

## 5. Core Features (MVP)

### 5.1 Fine-Tuned Model Weights (LoRA)
* Fine-tuned on curated algorithmic datasets using PyTorch and Hugging Face PEFT.
* Training loss converged from `2.46` to `0.27`, specializing the model in concise, production-ready code outputs.

### 5.2 Deterministic Code Extractor & Normalizer
* Extracts raw executable source code from Markdown code fences (```python).
* AST inspection to ensure generated function signatures strictly conform to target test assertion names.

### 5.3 Hardened Subprocess Sandbox
* Isolated subprocess execution with OS-level `setrlimit` boundaries:
  * `RLIMIT_CPU`: 5 seconds hard cap.
  * `RLIMIT_AS`: 256 MB address space.
  * `RLIMIT_NPROC`: Maximum 1 child process (prevents fork-bombs).
  * `RLIMIT_NOFILE`: Maximum 64 file descriptors.
* Five execution status classifications: `PASS`, `SYNTAX_ERROR`, `RUNTIME_ERROR`, `TIMEOUT`, `WRONG_ANSWER`.

### 5.4 Autonomous Self-Correction Reflection Loop
* Intercepts `stderr`, exception type, failing inputs, and traceback lines upon execution failure.
* Formulates a specialized reflection prompt injecting the original prompt, failed implementation, and exact runtime error.
* Iteratively feeds corrections back into the model up to `max_corrections=2` rounds.

### 5.5 High-Throughput FastAPI REST Service
* Production REST API containerized with Docker and Docker Compose:
  * `POST /generate`: Fast zero-shot code synthesis.
  * `POST /evaluate`: Hardened sandboxed test runner.
  * `POST /solve`: End-to-end generation, verification, and autonomous reflection loop.

---

## 6. Non-Functional Requirements

* **Reliability**: 99.9% uptime for the API gateway; graceful timeout recovery if a sub-process crashes.
* **Security**: Total isolation of code execution prevents host file system mutation and network access.
* **Scalability**: Decoupled vLLM model engine allowing horizontal scaling of sandboxed worker containers.
* **Portability**: Standardized OCI container images deployable on Kubernetes, AWS ECS, or bare-metal Linux.

---

## 7. Future Enhancements

* Multi-turn chat interface with live syntax-highlighted IDE diff viewer.
* Support for external package installation inside ephemeral microVMs (Firecracker / gVisor).
* Reinforcement Learning from Compiler Feedback (RLCF) for continuous online adapter optimization.

