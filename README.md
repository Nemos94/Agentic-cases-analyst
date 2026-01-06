# Agentic Case Analyst  
**Designing and implementing the same AI agent _with and without frameworks_**

---

## 🚀 Project Overview

This repository is a **case study on agentic AI design**.

Instead of starting with a framework, this project starts with **first principles**:
- What is the agent supposed to do?
- What is its state?
- How does it decide?
- Where are the boundaries?

The **same agent** is then implemented twice:

1. **Custom Agent (from scratch, Python)**  
2. **Framework-based Agent (n8n AI Agent / LangChain)**  

The goal is **not** to compare code styles, but to compare **design, control, and trade-offs**.

---

## 🧠 The Agent: Case Analyst

The agent acts as a **Case Analyst** for inbound customer requests (e.g. emails).

### Responsibilities
- Analyze a customer request
- Decide the *next action*, not the final resolution
- Prepare information for a human to act

### The agent can choose one action:
- `CONCLUDE` – Enough information for a human to act
- `REQUEST_CONTEXT` – Missing critical information
- `CONSULT_HISTORY` – Historical data may help
- `ESCALATE` – Risk, ambiguity, or manual review required

⚠️ The agent **never** replies directly to the customer.

---

## 🧩 Why This Project Exists

Many AI agent examples:
- hide state
- mix reasoning with execution
- rely heavily on framework magic

This project intentionally:
- designs the agent **before** choosing tools
- keeps state explicit
- separates *decision-making* from *orchestration*
- enforces strict JSON contracts

---

## 🏗️ Repository Structure

```text
agentic-case-analyst/
│
├── README.md                 # You are here
│
├── docs/
│   ├── decisions.md          # Technical decisions & learnings
│   ├── agent-comparison.md   # Custom agent vs n8n agent
│   └── architecture.png      # High-level architecture diagram
│
├── custom-agent/             # Agent without frameworks
│   ├── agent/
│   │   ├── agent.py          # Agent loop and decision logic
        ├── main.py           # Run the agent
│   │   └── state.py          # Explicit agent state
│   │    
│   └── README.md
│
├── n8n-agent/                # Agent implemented with framework
│   ├── Agentic (n8n).json    # n8n workflow export
│   ├── README.md
│   └── screenshot n8n
```

---

## 🧪 Implementation 1: Custom Agent (No Framework)

### Characteristics
- Explicit agent loop (`while`)
- Explicit state object (`CaseState`)
- LLM used **only** for decision-making
- Deterministic control flow
- Easy to test and reason about

### What this shows
- How agents actually work under the hood
- Why boundaries matter
- Why frameworks abstract complexity

📁 See: `custom-agent/`

---

## ⚙️ Implementation 2: Framework Agent (n8n)

### Characteristics
- Visual orchestration
- Stateless AI Agent node
- State carried explicitly through workflow JSON
- Loop simulated via routing
- LLM configured via prompt + guardrails

### What this shows
- Faster integration with real systems
- More hidden assumptions
- Need for discipline in state handling

📁 See: `n8n-agent/`

---

## 🔍 Key Learnings

Some of the most important takeaways from this project:

- Agents are **not** prompts
- State must be explicit
- LLMs should decide, not orchestrate
- Frameworks are powerful
- Designing first makes frameworks safer

These learnings are documented in detail in:
📄 `docs/decisions.md`

---

## 🆚 Custom vs Framework

A full comparison is available in:
📄 `docs/agent-comparison.md`

It covers:
- Loop control
- State & memory
- Observability
- Governance
- When to choose each approach

---

## 🎯 Who This Is For

- Engineers learning agentic AI
- Architects evaluating AI frameworks
- Developers using n8n, LangChain, or similar tools
- Anyone who wants to understand **how agents really work**

---

## 🏁 Final Note

This project is intentionally **not a product**.

It is a **learning artifact** and **design reference** that demonstrates:
- agent thinking
- system boundaries
- framework trade-offs

If you understand this repository, you can build agents **with or without** any tool.

---

Feel free to explore, fork, and adapt.
