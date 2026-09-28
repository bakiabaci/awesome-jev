# Agent Harness Integration Recipes

Tested and verified integration patterns for embedding Jev and System One decision layers into modern AI coding agents: **Claude Code**, **OpenCode**, **Codex**, **Cursor**, and **Generic MCP Clients**.

---

## 0. Official TypeSafe Skills (Universal)

The official skills package installs recipes, documentation, and prompt helpers directly into your coding environment:

```bash
# Claude Code Plugin
claude plugin marketplace add typesafe-ai/skills
claude plugin install typesafe@typesafe-ai

# OpenCode / Codex / Universal Agents via skills.sh
npx skills add typesafe-ai/skills --skill typesafe-ai -g
```

Once installed, use `/typesafe:typesafe-ai` in chat to inspect recipes and verify connection.

---

## 1. OpenCode Integration via Model Context Protocol (MCP)

OpenCode natively supports MCP servers defined in its configuration file.

### Step 1: Install the MCP server
```bash
npm install -g jev-mcp
```

### Step 2: Configure OpenCode (`opencode.json` or `~/.config/opencode/config.json`)
Add the `jev-mcp` definition to the `mcpServers` block:

```json
{
  "mcpServers": {
    "jev": {
      "command": "npx",
      "args": ["-y", "jev-mcp"],
      "env": {
        "TYPESAFE_API_KEY": "${TYPESAFE_API_KEY}"
      }
    }
  }
}
```

### Step 3: Verified Tools Available to the Agent
Upon restart, the agent receives 11 calibrated decision tools:
* `jev_noul`: Evaluates boolean questions with confidence calibration.
* `jev_classify`: Single-pass categorical classification (`Choice`).
* `jev_rerank`: Re-ranks candidates, files, or passages by relevance score.
* `jev_review`: Evaluates code diffs against architectural rules.
* `jev_screen`: Fast triage of logs, error traces, or test outputs.

---

## 2. Claude Code Integration

### Token Economy & Pruning
Keep your context window focused on actual code rather than verbose Bash and Grep outputs:

```bash
# 1. Install semantic code search (Node 22+)
npm install -g @dzhng/jevgrep

# 2. Add fast compaction hook (replaces lossy LLM compaction with surgical pruning)
claude plugin install tamaratran/fast-jev-compaction
```

### Usage Pattern
```bash
# Search large codebases semantically
jevgrep "where is authentication token refreshed"
```

---

## 3. Cursor & Windsurf (Rules & MCP)

Add the MCP server to `cursor-settings.json`:

```json
{
  "mcpServers": {
    "jev": {
      "command": "npx",
      "args": ["-y", "jev-mcp"],
      "env": {
        "TYPESAFE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

Add to `.cursorrules`:
```markdown
When categorizing files, checking test coverage relevance, or screening diffs, 
prefer calling `jev_noul` or `jev_classify` via MCP before initiating multi-turn LLM reasoning.
```

---

## 4. Python SDK Quickstart (Direct Wire Integration)

```python
from typesafe import TypeSafeClient

client = TypeSafeClient()  # Automatically reads TYPESAFE_API_KEY

# 1. Fast Boolean with Calibrated Confidence (Noul)
verdict = client.decide.noul(
    question="Does this error trace indicate a transient network failure?",
    state=error_trace_string
)
print(f"Is Transient: {verdict.value} (Confidence: {verdict.confidence:.2%})")

# 2. Strict Schema Choice
route = client.decide.choice(
    question="Which service is responsible for handling this incoming webhook?",
    choices=["billing", "auth", "notifications", "ingestion"],
    state=raw_payload
)
print(f"Selected Service: {route.choice}")
```
