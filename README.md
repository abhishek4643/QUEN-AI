# Qwen2.5-3B Autonomous AI Code Generation and Self-Correction Assistant

An end-to-end, production-ready AI coding system based on Qwen2.5-Coder-3B-Instruct fine-tuned with Low-Rank Adaptation (LoRA). 

The system couples generative code intelligence with an automated execution sandbox and a self-correction reflection loop. Generated code is evaluated against deterministic test cases in real time. If a failure occurs, the engine intercepts the execution traceback, reflects on the error, and autonomously repairs the solution until all test assertions pass.

---

## Key Capabilities

* **Fine-Tuned Architecture:** Qwen2.5-Coder-3B fine-tuned on curated algorithmic datasets with training loss converging from 2.46 to 0.27.
* **Sandboxed Code Execution:** Isolated subprocess executor with strict memory, CPU, and execution timeout constraints across 5 execution states (PASS, SYNTAX_ERROR, RUNTIME_ERROR, TIMEOUT, WRONG_ANSWER).
* **Autonomous Self-Correction:** Closed reflection loop that feeds runtime tracebacks back to the model for iterative bug fixing without human intervention.
* **Multi-Language Execution:** Dynamic compilation and execution for Python, C (compiled via gcc), and C++ (compiled via g++).
* **Production Deployment Stack:** Packaged with FastAPI REST endpoints (/generate, /evaluate, /solve), high-throughput vLLM serving, and Docker containerization.
* **Verified Benchmark Score:** Achieved 100.0% (43 / 43 PASS) on the MBPP validation benchmark and 100.0% (10 / 10 PASS) across diverse algorithmic domains.

---

## Benchmark Results

| Metric | Result |
| :--- | :--- |
| MBPP Benchmark Pass Rate (43 Problems) | 100.0% (43 / 43 PASS) |
| Algorithmic Domain Generalization (10 Types) | 100.0% (10 / 10 PASS) |
| First-Pass Success Rate (Round 0) | > 90% |
| Self-Correction Recovery Rate | 100.0% |
| Average Generation Latency | < 6.5s per problem |

---

## System Architecture

```
User Problem ---> Qwen2.5-3B + LoRA ---> Code Extraction
                                               |
                                               v
                                      Sandboxed Executor
                                               |
                               +---------------+---------------+
                               |                               |
                               v                               v
                        All Tests Pass?                  Test Failed?
                               |                               |
                               v                               v
                       Return Verified Code             Capture Traceback
                                                               |
                                                               v
                                                    Self-Correction Loop ---> (Retest)
```

---

## Repository Structure

```
├── qwen2.5-3b-coder-lora-v3/    # Trained LoRA adapter weights and tokenizer
├── quen-ai.ipynb                # Clean end-to-end training and evaluation notebook
├── app.py                       # FastAPI REST backend service
├── mbpp_harness_fix.py          # Sandboxed execution and self-correction engine
├── Dockerfile                   # Container definition for service deployment
├── docker-compose.yml           # Multi-container orchestration (vLLM + API)
├── requirements.txt             # Production dependencies
└── README.md                    # Project documentation
```

---

## Quick Start

### 1. Interactive Notebook Execution
Open `quen-ai.ipynb` in any Jupyter or Kaggle environment with GPU support. Run the interactive cell at the bottom to generate and test code for any programming prompt.

### 2. Containerized Deployment (vLLM + FastAPI)
```bash
# Clone the repository
git clone https://github.com/abhishek4643/QUEN-AI.git
cd QUEN-AI

# Build and run with Docker Compose
docker compose up --build
```
Interactive API documentation will be accessible at: `http://localhost:8080/docs`

---

## API Endpoints

* `POST /generate`: Generates code for a given problem signature.
* `POST /evaluate`: Executes code against assertions in the isolated sandbox.
* `POST /solve`: Complete end-to-end pipeline: generation, execution, and automatic self-correction.

---

## License

MIT License
