# AI Agents

A collection of local AI agent projects built with open-source models and modern tooling.

---

## Projects

### `local_chatgpt/`

A fully local ChatGPT-style chatbot powered by [Google DeepMind's Gemma 3](https://deepmind.google/technologies/gemma/) running via [Ollama](https://ollama.com), with a chat UI built on [Chainlit](https://docs.chainlit.io).

**Features:**
- 100% local inference — no OpenAI API key or cloud dependency
- Streaming token-by-token responses
- Multi-modal support: send images alongside text messages
- Conversation history maintained per session
- Docker Compose setup for easy one-command deployment

**Tech Stack:**
| Component | Tool |
|-----------|------|
| LLM | Gemma 3 4B via Ollama |
| UI | Chainlit |
| Containerization | Docker Compose |

---

## Getting Started

### Option 1 — Docker (Recommended)

```bash
cd local_chatgpt
docker compose up
```

This will:
1. Start an Ollama server and pull the `gemma3:4b` model
2. Install dependencies and launch the Chainlit app

Open your browser at [http://localhost:8000](http://localhost:8000).

> **GPU support:** To enable NVIDIA GPU acceleration, uncomment the `deploy` block in `docker_compose.yml`.

### Option 2 — Run Locally

**Prerequisites:** [Ollama](https://ollama.com) installed and running.

```bash
ollama pull gemma3:4b
cd local_chatgpt
pip install pydantic==2.10.1 chainlit ollama
chainlit run app.py -w
```

---

## Requirements

- Docker & Docker Compose (for containerised setup)
- Python 3.11+ (for local setup)
- 8 GB+ RAM recommended for running Gemma 3 4B
