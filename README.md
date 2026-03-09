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

| Lesson | File | Notes |
|--------|------|-------|
| 01 — Hello World | [basics/server.py](basics/server.py) | Minimal server with one tool, tested via MCP Inspector |

> Detailed walkthrough: [basics/server.md](basics/server.md)

---

## Tools Used

- **Python MCP SDK** — `mcp` package (`FastMCP`)
- **MCP Inspector** — `npx @modelcontextprotocol/inspector` — browser UI for testing servers locally

---

## Running a Server

```bash
# Run directly
.venv/bin/python3 basics/server.py

# Run with MCP Inspector (recommended for testing)
npx @modelcontextprotocol/inspector .venv/bin/python3 basics/server.py
```
