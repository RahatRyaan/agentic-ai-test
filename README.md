# Agentic AI Integration Test Project

This repository serves as an end-to-end integration and verification environment for local Agentic AI workflows on the Ubuntu workstation `AKANDA`.

---

## Architecture & Capabilities

* **Local LLM Engine:** Ollama local inference service (running on `http://127.0.0.1:11434`)
* **AI Agent CLI:** Anthropic Claude Code CLI (`claude`) & Google Antigravity SDK tooling
* **Containerization:** Docker Engine & Docker Compose for isolated microservice tests
* **Language Support:** Python 3.14 (`uv`), Go 1.26, Rust 1.98, Node.js 22 (`pnpm`)

---

## Project Structure

```text
~/Projects/agentic-ai-test/
├── README.md           # Project architecture and usage guide
├── AGENT.md            # Agent operational constraints and permissions
├── .gitignore          # Environment and build artifact ignores
├── app/
│   ├── main.py         # Microservice implementation
│   └── test_main.py    # Automated test suite
└── Dockerfile          # Containerized build and run manifest
```

---

## Local Verification Commands

1. **Run Unit Tests:**
   ```bash
   python3 -m unittest discover -s app -p "test_*.py"
   ```
2. **Build Docker Image:**
   ```bash
   docker build -t agentic-test:local .
   ```
3. **Execute Container:**
   ```bash
   docker run --rm agentic-test:local
   ```
