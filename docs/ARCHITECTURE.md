# System Architecture

**Qwen2.5-Coder Autonomous AI Code Generation & Self-Correction Engine**  
*System Architecture, Component Topology, Security Sandbox Boundaries, and Data Flow Specifications*

---

This document outlines the end-to-end system architecture, technology stack, directory layout, execution pipeline, and key design decisions powering the autonomous code generation and reflection engine.

---

## 1. High-Level Architecture

The system decouples high-throughput generative inference from secure code execution via a multi-tiered architecture:

```
[ User / Client Application ]
             |
             | (HTTP / REST JSON)
             v
+---------------------------------------------------------------------------------+
|                              FastAPI Gateway Service                            |
|                               (Port 8080 - app.py)                              |
|   +---------------------+   +---------------------+   +---------------------+   |
|   |   POST /generate    |   |    POST /evaluate   |   |     POST /solve     |   |
|   +---------------------+   +---------------------+   +---------------------+   |
+---------------------------------------------------------------------------------+
             |                                                  |
             | (OpenAI-compatible v1 API)                       | (Spawns Hardened Process)
             v                                                  v
+-----------------------------+               +-----------------------------------+
|      vLLM Serving Engine    |               |    Sandboxed Execution Runtime    |
|   (Qwen2.5-Coder-3B + LoRA) |               |      (mbpp_harness_fix.py)        |
| - Continuous Batching       |               | - setrlimit (CPU: 5s, RAM: 256MB) |
| - PagedAttention Kernel     |               | - Child Process Jail (NPROC: 1)   |
| - Low-Rank Adapter v3       |               | - File Cap (NOFILE: 64)           |
+-----------------------------+               +-----------------------------------+
             ^                                                  |
             |                                                  v
             |                                      +-----------------------+
             |                                      | Evaluation Result:    |
             |                                      | - PASS                |
             |                                      | - RUNTIME_ERROR       |
             |                                      | - SYNTAX_ERROR        |
             |                                      | - TIMEOUT             |
             |                                      | - WRONG_ANSWER        |
             |                                      +-----------------------+
             |                                                  |
             +----------- Self-Correction Reflection Loop <----+ (If Failed)
                          (Injects Traceback + Failing Inputs)
```

---

## 2. Technology Stack

Technologies used across the project and their functional roles:

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Foundation Model** | Qwen2.5-Coder-3B-Instruct | High-efficiency 3B parameter model optimized for code syntax and logic |
| **Fine-Tuning Framework** | PyTorch + Hugging Face PEFT (LoRA) | Parameter-efficient training with low-rank adapters converging loss to 0.27 |
| **Inference Serving** | vLLM Engine | PagedAttention GPU serving with continuous batching and dynamic LoRA loading |
| **API Gateway** | FastAPI (Python 3.11) | High-performance asynchronous REST endpoints for code generation and eval |
| **Sandbox Isolation** | Linux `resource` (`setrlimit`) + `subprocess` | Hardware resource throttling (RAM, CPU, PIDs, FDs) preventing malicious code |
| **HTTP Transport** | HTTPX (Async Client) | Resilient connection-pooled client communicating with the vLLM backend |
| **Containerization** | Docker & Docker Compose | Multi-container orchestration binding FastAPI gateway and vLLM server |
| **Benchmarking Suite** | MBPP (Mostly Basic Python Problems) | 43-problem rigorous evaluation harness verifying 100% pass rates |
| **Version Control** | Git + GitHub | Source repository and artifact versioning (`abhishek4643/QUEN-AI`) |

---

## 3. Folder Structure

The project follows a modular, feature-oriented structure separating training notebooks, serving runtimes, and documentation:

```text
Qwen/
├── docs/                               # Engineering & architecture governance
│   ├── PRD.md                          # Product requirements & MVP features
│   ├── ARCHITECTURE.md                 # System topology, data flow & tech stack
│   ├── RULES.md                        # Coding standards & AI pair-programming guidelines
│   ├── DESIGN.md                       # Design system, API contracts & tokens
│   ├── TASKS.md                        # Phased task dashboard & execution tracker
│   └── MEMORY.md                       # Session memory, active phase & decision logs
├── qwen2.5-3b-coder-lora-v3/           # Trained Low-Rank Adapter weights
│   ├── adapter_config.json             # LoRA rank, alpha, and target modules config
│   ├── adapter_model.safetensors       # Quantized/fp16 fine-tuned weights
│   ├── tokenizer.json                  # Byte-level BPE tokenizer
│   └── tokenizer_config.json           # Special tokens and chat template
├── app.py                              # FastAPI production REST gateway service
├── mbpp_harness_fix.py                 # Sandboxed execution runner & reflection harness
├── quen-ai.ipynb                       # End-to-end training, loss analysis & eval notebook
├── Dockerfile                          # Container specification for production deployment
├── docker-compose.yml                  # Multi-service stack (vLLM + FastAPI API)
├── requirements.txt                    # Locked production Python dependencies
└── README.md                           # Quickstart guide, benchmark results & setup
```

---

## 4. Data Flow & Execution Pipeline

The life cycle of a request submitted to `POST /solve`:

```mermaid
sequenceDiagram
    autonumber
    actor Client
    participant API as FastAPI Gateway
    participant LLM as vLLM / Qwen2.5-3B
    participant Box as Hardened Sandbox

    Client->>API: POST /solve (problem_text, test_list)
    API->>LLM: build_generation_prompt(problem_text)
    LLM-->>API: Generated Markdown / Code
    API->>API: extract_code() & ensure_expected_name()
    
    API->>Box: execute_hardened(code, test_list)
    alt Execution Passes (All Assertions Valid)
        Box-->>API: status: PASS
        API-->>Client: 200 OK (code, status: PASS, attempts: 1)
    else Execution Fails (Runtime / Syntax / Logic Error)
        Box-->>API: status: RUNTIME_ERROR (traceback, failing test)
        loop Self-Correction Reflection (up to max_corrections)
            API->>LLM: build_correction_prompt(code, traceback, test)
            LLM-->>API: Corrected Patch Code
            API->>Box: execute_hardened(patched_code, test_list)
            Box-->>API: Updated Execution Status
        end
        API-->>Client: 200 OK (final_code, status, attempts)
    end
```

---

## 5. Key Architectural Decisions (ADRs)

* **ADR-001: LoRA Fine-Tuning over Full Model Fine-Tuning**  
  *Context*: Full parameter fine-tuning of 3B parameters requires massive GPU VRAM and makes adapter deployment bulky.  
  *Decision*: Selected Low-Rank Adaptation (LoRA) targeting `q_proj`, `k_proj`, `v_proj`, and `o_proj`.  
  *Outcome*: Reduced memory footprint to under 80 MB for the adapter while converging loss from 2.46 to 0.27.

* **ADR-002: Subprocess Execution with `setrlimit` over Docker-in-Docker**  
  *Context*: Running untrusted user code inside secondary Docker containers incurs ~500ms spin-up overhead per test.  
  *Decision*: Utilize POSIX `resource.setrlimit` inside isolated Python sub-processes with capped memory and CPU counters.  
  *Outcome*: Execution latency drops below 25ms per test run while strictly containing compute abuse.

* **ADR-003: Deterministic AST Name Normalization**  
  *Context*: Foundation models frequently output valid algorithmic solutions but name functions generically (`solution` instead of the expected `find_max`).  
  *Decision*: Built `ensure_expected_name()` to parse test assertions and verify/alias function names before running tests.  
  *Outcome*: Eliminated false negative `NameError` failures on benchmark runs.

