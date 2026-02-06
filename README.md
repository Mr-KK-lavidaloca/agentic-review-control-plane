# Agentic Review Control Plane

Production-grade agentic system for performing structured architecture
reviews using schema-bound agents and a bounded LLM execution layer.

The system demonstrates how LLM-based agents can be orchestrated,
validated, and isolated in production-oriented application architectures.

---

## Why this exists

Many agentic AI projects combine reasoning, orchestration, and model
execution into a single layer, making them hard to test and reason
about under failure.

This project deliberately separates:

- **Agents** — domain-specific reasoning units
- **Executor** — the sole boundary for LLM invocation
- **Execution controls** — retries, timeouts, and validation
- **Orchestration** — LangGraph used only as a routing layer

---

## System Architecture

- Independent domain agents:
  - Backend
  - ML
  - Security
  - Infrastructure
- A lead agent synthesizes all domain reviews into a final assessment
- All agent outputs are enforced via strict JSON schemas
- Agents cannot directly invoke the LLM or bypass execution limits


---


Client → FastAPI → Executor

↓

Backend / ML / Security / Infra Agents

↓

Lead Agent


---


---

## Key Engineering Guarantees

| Property | How it's enforced |
|--------|-------------------|
| Deterministic outputs | Schema validation |
| Bounded execution | Timeouts and retry caps |
| Failure isolation | Per-agent execution |
| Cost control | Centralized executor |
| Testability | Fully mocked LLM calls |

---

## Testing Strategy

- Executor unit tests without FastAPI
- Endpoint tests using ASGI transport
- All LLM calls mocked to ensure deterministic and cost-free tests
- No external API keys required to run tests locally


## How to Run

### Prerequisites
- Python 3.10+
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Mr-KK-lavidaloca/agentic-review-control-plane.git

   cd agentic-review-control-plane
   ```
2. Create and activate a virtual environment:

   Windows

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   macOS / Linux

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Run Tests

All tests mock LLM calls. No API keys are required.

```bash
pytest
```

Run the API Server
```bash
uvicorn app.main:app --reload
```
The API will be available at:
```bash
http://127.0.0.1:8000/docs
```
