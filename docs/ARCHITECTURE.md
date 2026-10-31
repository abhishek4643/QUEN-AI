# 🏛️ System Architecture
### Qwen2.5-Coder — Autonomous AI Code Generation & Self-Correction Engine

> This document describes the overall system architecture, technology stack, directory structure, data flow, and key design decisions for the **Qwen2.5-Coder** software engineering system.

---

### 1. High-Level Architecture
*Qwen2.5-Coder follows a hardened, decoupled micro-service architecture separating high-throughput generative inference from isolated subprocess execution:*

<table>
  <tr align="center">
    <td width="22%" style="background-color: #1e3a8a; border: 1px solid #3b82f6; border-radius: 10px; padding: 14px 10px;">
      <div style="font-size: 22px;">👤</div>
      <b style="color: #bfdbfe; font-size: 13px;">User / Client</b><br>
      <span style="color: #93c5fd; font-size: 11px;">Prompt + Test Cases</span>
    </td>
    <td width="4%" style="color: #94a3b8; font-size: 18px;">
      <b>⟷</b><br><span style="font-size: 9px;">HTTPS</span>
    </td>
    <td width="22%" style="background-color: #064e3b; border: 1px solid #10b981; border-radius: 10px; padding: 14px 10px;">
      <div style="font-size: 22px;">⚡</div>
      <b style="color: #a7f3d0; font-size: 13px;">FastAPI Gateway</b><br>
      <span style="color: #6ee7b7; font-size: 11px;">Endpoints / Logic</span>
    </td>
    <td width="4%" style="color: #94a3b8; font-size: 18px;">
      <b>⟷</b><br><span style="font-size: 9px;">IPC / v1</span>
    </td>
    <td width="22%" style="background-color: #78350f; border: 1px solid #f59e0b; border-radius: 10px; padding: 14px 10px;">
      <div style="font-size: 22px;">🧠</div>
      <b style="color: #fef3c7; font-size: 13px;">vLLM + Qwen2.5</b><br>
      <span style="color: #fde68a; font-size: 11px;">LoRA Serving Engine</span>
    </td>
    <td width="4%" style="color: #94a3b8; font-size: 18px;">
      <b>⟷</b><br><span style="font-size: 9px;">Sandbox</span>
    </td>
    <td width="22%" style="background-color: #4c1d95; border: 1px solid #8b5cf6; border-radius: 10px; padding: 14px 10px;">
      <div style="font-size: 22px;">🛡️</div>
      <b style="color: #ddd6fe; font-size: 13px;">Isolated Sandbox</b><br>
      <span style="color: #c4b5fd; font-size: 11px;">POSIX setrlimit (5s/256M)</span>
    </td>
  </tr>
</table>

---

### 2. Technology Stack
*Technologies used in the project and their purpose:*

| Layer | Technology | Purpose |
| :-- | :-- | :-- |
| **Foundation Model** | Qwen2.5-Coder-3B-Instruct | High-efficiency 3B parameter model specialized in programming logic |
| **Fine-Tuning Framework** | PyTorch + Hugging Face PEFT (LoRA) | Parameter-efficient training with low-rank adapters (loss converged: 2.46 $\rightarrow$ 0.27) |
| **Inference Serving** | vLLM Engine | PagedAttention GPU serving with continuous batching and dynamic LoRA loading |
| **API Gateway** | FastAPI (Python 3.11) | High-performance asynchronous REST endpoints for code synthesis and test evaluation |
| **Sandbox Isolation** | Linux `resource` (`setrlimit`) + `subprocess` | Hardware resource throttling (RAM, CPU, PIDs, FDs) preventing malicious code escape |
| **HTTP Transport** | HTTPX (Async Client) | Resilient connection-pooled client communicating with the vLLM backend |
| **Containerization** | Docker & Docker Compose | Multi-container orchestration binding FastAPI gateway and vLLM server |
| **Evaluation Suite** | MBPP (Mostly Basic Python Problems) | 43-problem validation benchmark verifying 100% pass rates |
| **Version Control** | Git + GitHub | Source repository and artifact versioning (`abhishek4643/QUEN-AI`) |

---

### 3. Folder Structure
*The project follows a clean, modular structure separating model adapters, runtime harnesses, and API services:*

```text
Qwen/
├── docs/                               # Architecture, design & development guidelines
│   ├── PRD.md                          # Product requirements & MVP features
│   ├── ARCHITECTURE.md                 # System topology, data flow & tech stack
│   ├── RULES.md                        # Coding standards & AI pair-programming guidelines
│   ├── DESIGN.md                       # Design system, UI tokens & terminal themes
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

### 4. Data Flow & Reflection Loop Pipeline

```
[ POST /solve Request ] ──> [ FastAPI Gateway ] ──> [ vLLM + Qwen2.5-3B ]
                                                           │
                                                           ▼ (Raw Code Output)
                                                  [ AST Extractor ]
                                                           │
                                                           ▼ (Executable Code)
                                            [ Hardened Sandbox Executor ]
                                                           │
                                  ┌────────────────────────┴────────────────────────┐
                                  ▼                                                 ▼
                         [ Status: PASS ]                               [ Status: RUNTIME_ERROR ]
                                  │                                                 │
                                  ▼                                                 ▼
                       [ Return 200 OK ]                             [ Intercept Traceback & Stderr ]
                                                                                    │
                                                                                    ▼
                                                                     [ Self-Correction Engine ]
                                                                       (Retry with Patch Prompt)
```

---

### 5. Key Architectural Decisions (ADRs)

* **ADR-001: LoRA Fine-Tuning over Full Parameter Retraining**  
  *Rationale*: Retraining 3B parameters requires massive GPU VRAM and produces cumbersome checkpoints. LoRA targeting `q_proj`, `k_proj`, `v_proj`, and `o_proj` achieved loss convergence to 0.27 with an adapter size under 80 MB.
* **ADR-002: In-Process `setrlimit` Throttling vs Secondary MicroVMs**  
  *Rationale*: Spinning up Docker-in-Docker or microVMs incurs >500ms latency per problem. POSIX `setrlimit` inside isolated sub-processes brings test execution latency under 25ms while enforcing absolute resource ceilings.
* **ADR-003: Deterministic AST Name Normalization (`ensure_expected_name`)**  
  *Rationale*: Models frequently synthesize functionally perfect algorithms but name functions generically (`solution` instead of the expected `find_max`). AST inspection dynamically aliases function symbols to eliminate false-negative test failures.
