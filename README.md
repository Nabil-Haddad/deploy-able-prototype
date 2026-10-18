# SheetPilot

**Talk to your spreadsheets. No formulas required.**

SheetPilot is a production grade web application that lets anyone, regardless of technical background, inspect, modify, and extract insights from spreadsheet data through natural conversation. It combines a Retrieval Augmented Generation pipeline with the Model Context Protocol so an AI assistant can reason over real operational data and act on it safely, instead of forcing users to learn SQL, pivot tables, or Python.

<p align="center">
  <a href="https://github.com/Nabil-Haddad/deploy-able-prototype/actions/workflows/ci-cd.yml"><img src="https://github.com/Nabil-Haddad/deploy-able-prototype/actions/workflows/ci-cd.yml/badge.svg" alt="CI/CD"></a>
  <img src="https://img.shields.io/badge/python-3.13-3776AB?logo=python&logoColor=white" alt="Python 3.13">
  <img src="https://img.shields.io/badge/FastAPI-0.141-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Docker-ready-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/package%20manager-uv-DE3332?logo=python&logoColor=white" alt="uv">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License"></a>
</p>

<p align="center">
  <strong>Live demo:</strong> coming soon &nbsp;|&nbsp; <strong>Demo video:</strong> coming soon
</p>

## Why this exists

Every production floor, finance team, and ops department runs on spreadsheets that only two or three people in the building actually know how to query. Everyone else either waits for a report or learns to be dangerous in Excel. SheetPilot closes that gap: upload a sheet, ask a question in plain English, and get a grounded, cited answer, or a safe, validated write back into the data, without a single formula.

## What it does today

The backend that powers SheetPilot is already a real, tested, containerized service, not a notebook experiment.

| Area | What's built |
|---|---|
| API | A FastAPI service with a layered architecture (routers, schemas, models, repositories) so each concern can be tested and changed independently |
| Data layer | PostgreSQL via SQLAlchemy, with Pydantic enforcing validation rules before anything reaches the database |
| Testing | A pytest suite covering schema validation, repository logic, and full HTTP integration, running against an isolated in memory database so tests never touch production |
| Packaging | A multi stage aware Dockerfile built on `uv`, producing a reproducible image that boots the same way locally and in CI |
| Delivery | A GitHub Actions pipeline that runs the full test suite on every change and publishes a versioned image to GitHub Container Registry on every merge to `main` |

## Where it's going

This is the part that matters most. The sections below are not vague ideas, they are commitments with a deadline attached to this repository's next milestones.

| Milestone | Outcome | Status |
|---|---|---|
| RAG ingestion pipeline | Spreadsheets are chunked, embedded, and indexed so questions are answered from real row level data, with the source rows cited back to the user | planned |
| MCP server | The assistant connects to spreadsheet operations (read, filter, aggregate, write) as typed, permissioned tools, so "modify" requests are explicit, auditable actions, not free text SQL | planned |
| Conversational frontend | A chat first interface for people who have never opened a terminal, built so a factory supervisor is just as comfortable as a data analyst | planned |
| Authentication and multi tenant data isolation | Every sheet belongs to a workspace, every query is scoped to it | planned |
| Public live deployment | A link in this README that anyone, including the recruiter reading this, can open and try in under a minute | planned |
| Recorded walkthrough | A short demo video embedded above, showing the upload to insight loop end to end | planned |

Each of these ships as its own reviewed pull request against this repository, with its own tests, the same way the backend above was built.

## Architecture

```
src/Backend/
├── main.py            entry point, FastAPI app, lifespan managed startup
├── api/                HTTP layer only: routing, request and response shapes
├── schemas/             Pydantic contracts for everything crossing the API boundary
├── models/             SQLAlchemy ORM definitions for the relational store
├── db/                 engine, session, and dependency wiring
├── repositories/       the only layer allowed to touch the database directly
└── services/           business logic that will host the RAG and MCP orchestration
```

The `services/` layer is deliberately already in place and empty. It is where the retrieval pipeline and the MCP tool handlers will live, sitting behind the same repository abstraction the rest of the app already uses, so adding intelligence to this app never means rewriting its foundations.

## Getting started

Clone the repository and install dependencies with `uv`, which resolves and locks everything in seconds.

```bash
git clone https://github.com/Nabil-Haddad/deploy-able-prototype.git
cd deploy-able-prototype
uv sync
```

Create a `.env` file at the project root with your database connection details.

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=production_db
DB_USER=postgres
DB_PASSWORD=your-password
```

Run the API.

```bash
uv run uvicorn main:app --reload --app-dir src/Backend
```

Or run it in Docker, with the same `.env` mounted at runtime so no secret ever lives inside the image.

```bash
docker build -t sheetpilot .
docker run -d -p 8000:8000 -v "$(pwd)/.env:/app/.env:ro" sheetpilot
```

Interactive API documentation is then available at `http://127.0.0.1:8000/docs`.

## Testing

```bash
uv run pytest -v
```

Every test runs against an in memory SQLite database created fresh per test, so the suite is fast, deterministic, and never depends on a live PostgreSQL instance being reachable.

## Tech stack

Python 3.13, FastAPI, Pydantic, SQLAlchemy, PostgreSQL, pytest, Docker, GitHub Actions, and `uv` as the dependency and environment manager. Retrieval Augmented Generation and Model Context Protocol integrations are the next layer, built on top of this same foundation rather than bolted on beside it.

## Author

Built by Nabil Haddad as a demonstration of taking a backend from a single endpoint to a tested, containerized, continuously deployed service, with a clear and public roadmap toward a genuinely useful AI product.
