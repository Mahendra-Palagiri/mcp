# MCP Learning Journal

A hands-on guide to learning the Model Context Protocol (MCP) from scratch.

---

## What is MCP?

MCP (Model Context Protocol) is an open standard by Anthropic that defines how AI models connect to external tools, data sources, and services — a universal interface so any client can talk to any server.

**Three primitives a server can expose:**

| Primitive | Controlled by | Description |
|-----------|--------------|-------------|
| Tools | Model | Functions the AI can call |
| Resources | App / User | Data the AI can read |
| Prompts | User | Reusable prompt templates |

---

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Lessons

### Basics

| Lesson | File | Docs | Notes |
|--------|------|------|-------|
| 01 — Hello World | [basics/1.server.py](basics/1.server.py) | [docs](basics/docs/server.md) | Minimal server with one tool, tested via MCP Inspector |
| 02 — Multiple Tools + Parameters | [basics/2.tools.py](basics/2.tools.py) | [docs](basics/docs/tools.md) | Multiple tools, type hints, optional params, validation |

---

## Tools Used

- **Python MCP SDK** — `mcp` package (`FastMCP`)
- **MCP Inspector** — `npx @modelcontextprotocol/inspector` — browser UI for testing servers locally

---

## Running a Server

```bash
# Run directly
.venv/bin/python3 basics/1.server.py

# Run with MCP Inspector (recommended for testing)
npx @modelcontextprotocol/inspector .venv/bin/python3 basics/1.server.py
```
