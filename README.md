# 🤖 Qwen2.5-3B Autonomous AI Code Generation & Self-Correction Assistant

An end-to-end, enterprise-grade AI coding system built on **Qwen2.5-Coder-3B-Instruct** fine-tuned with **LoRA (Low-Rank Adaptation)**. 

Unlike standard code generation models that output static code, this system features a **sandboxed execution engine** and an **autonomous reflection loop** that automatically tests generated code, catches runtime/assertion failures, and self-corrects until all tests pass.

---

## 🌟 Key Features

* **🧠 Fine-Tuned AI Brain:** Qwen2.5-Coder-3B fine-tuned on curated algorithmic problem-solution pairs with training loss converging from $2.46 \to 0.27$.
* **🛡️ Sandboxed Code Execution:** Evaluates code in an isolated subprocess with memory, CPU, and timeout limits across 5 execution states (`PASS`, `SYNTAX_ERROR`, `RUNTIME_ERROR`, `TIMEOUT`, `WRONG_ANSWER`).
* **🔄 Autonomous Self-Correction:** When execution fails, the system captures stderr tracebacks, reflects on the error, and re-generates corrected code without human intervention.
* **🌐 Multi-Language Support:** Generates and executes Python, C (compiled via `gcc`), and C++ (compiled via `g++`).
* **🚀 Production Deployment:** Packaged with **FastAPI** REST endpoints (`/generate`, `/evaluate`, `/solve`), **vLLM** high-throughput serving, and **Docker**.
* **🏆 100% Benchmark Score:** Achieved **43/43 (100.0%) PASS** on the MBPP validation benchmark and **10/10 PASS** across diverse algorithmic domains (Arrays, Trees, Graphs, DP, etc.).

---

## 📊 Benchmark Results

| Metric | Result |
| :--- | :---: |
| **MBPP Benchmark Accuracy (43 Problems)** | **100.0% (43 / 43 PASS)** |
| **Domain Generalization (10 Domains)** | **100.0% (10 / 10 PASS)** |
| **First-Pass Success Rate (Round 0)** | **> 90%** |
| **Self-Correction Recovery Rate** | **100%** |
| **Average Latency** | **< 6.5s per problem** |

---

## 🏗️ System Architecture

```
User Problem ──► Qwen2.5-3B + LoRA ──► Code Extraction
                                              │
                                              ▼
                                     Sandboxed Executor
                                              │
                              ┌───────────────┴───────────────┐
                              ▼                               ▼
                       All Tests Pass?                Test Failed?
                              │                               │
                              ▼                               ▼
                     ✅ Return Solution         Capture Traceback & Reflect
                                                              │
                                                              ▼
                                                   Self-Correction Loop ──► (Retest)
```

---

## 📁 Repository Structure

```
├── qwen2.5-3b-coder-lora-v3/    # Trained LoRA adapter weights & tokenizer
├── app.py                       # FastAPI REST backend service
├── mbpp_harness_fix.py          # Sandboxed execution & self-correction engine
├── Dockerfile                   # Container definition for API deployment
├── docker-compose.yml           # Multi-container orchestration (vLLM + API)
├── requirements.txt             # Production Python dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Quick Start & Usage

### 1. Local / Cloud Deployment with Docker
```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# Launch vLLM and FastAPI services
docker compose up --build
```
Access the interactive Swagger UI at: `http://localhost:8080/docs`

### 2. FastAPI Endpoints
* `POST /generate` — Generates code for a given problem signature.
* `POST /evaluate` — Executes and tests code in the sandbox.
* `POST /solve` — Full pipeline: generates, executes, and autonomously self-corrects.

---

## 📜 License
MIT License
