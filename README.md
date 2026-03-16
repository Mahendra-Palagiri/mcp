# MCP Learning Journal

A hands-on guide to learning the Model Context Protocol (MCP) from scratch.

---

<details>
<summary><strong>What is MCP?</strong></summary>

MCP (Model Context Protocol) is an open standard by Anthropic that defines how AI models connect to external tools, data sources, and services — a universal interface so any client can talk to any server.

**Three primitives a server can expose:**

| Primitive | Controlled by | Description |
|-----------|--------------|-------------|
| Tools | Model | Functions the AI can call |
| Resources | App / User | Data the AI can read |
| Prompts | User | Reusable prompt templates |

</details>

---

<details>
<summary><strong>Setup</strong></summary>

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</details>

---

<details>
<summary><strong>Running a Server</strong></summary>

```bash
# Run directly
.venv/bin/python3 01_MCP_Primitives/01.server.py

# Run with MCP Inspector (recommended for testing)
npx @modelcontextprotocol/inspector .venv/bin/python3 01_MCP_Primitives/01.server.py
```

</details>

---

<details>
<summary><strong>Tools Used</strong></summary>

- **Python MCP SDK** — `mcp` package (`FastMCP`)
- **MCP Inspector** — `npx @modelcontextprotocol/inspector` — browser UI for testing servers locally

</details>

---

<details open>
<summary><strong>Roadmap</strong></summary>

## Completed

| Day | Phase | Topic | File | Notes |
|-----|-------|-------|------|-------|
| 01 | 01_MCP_Primitives | Hello World — minimal server, one tool, string param | [01.server.py](01_MCP_Primitives/01.server.py) | [notes](docs/01_MCP_Primitives/01.server.md) |
| 02 | 01_MCP_Primitives | Multiple Tools + Parameters — int, bool, optional params | [02.tools.py](01_MCP_Primitives/02.tools.py) | [notes](docs/01_MCP_Primitives/02.tools.md) |

## Upcoming

| Day | Phase | Topic |
|-----|-------|-------|
| 03 | 01_MCP_Primitives | MCP Resources — expose read-only data via `@mcp.resource()` |
| 04 | 01_MCP_Primitives | MCP Prompts — reusable prompt templates via `@mcp.prompt()` |
| 05 | 02_Real_World_Usage | Real-World Tool — connect to an external API (e.g. weather, GitHub) |
| 06 | 02_Real_World_Usage | Transport Modes — `stdio` vs SSE/HTTP |
| 07 | 02_Real_World_Usage | Claude Desktop Integration — wire server into Claude.app config |
| 08 | 03_Production_Readiness | Context, Logging & Progress — MCP `Context` object |
| 09 | 03_Production_Readiness | Error Handling — `McpError`, graceful failures |
| 10 | 04_Capstone | Capstone Project — combine all concepts into one real server |

</details>
