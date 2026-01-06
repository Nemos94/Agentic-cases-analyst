# n8n Agent (Framework-based)

This folder contains the **framework-based implementation** of the Agentic Case Analyst
using **n8n AI Agent (LangChain)**.

The purpose of this version is to show how the **same agent design**
can be implemented using a low-code automation framework.

---

## 🎯 Purpose

This implementation focuses on:
- Speed of integration
- Visual orchestration
- Practical constraints of agent frameworks

The agent behavior is the same as the custom Python version,
but execution is handled by n8n.

---

## 🧠 Agent Role

The agent acts as a **Case Analyst** and decides the next step for a customer case.

Possible actions:
- `CONCLUDE`
- `REQUEST_CONTEXT`
- `CONSULT_HISTORY`
- `ESCALATE`

⚠️ The agent does **not** respond directly to customers.

---

## 🏗️ How It Works

Key characteristics of the n8n implementation:

- The **AI Agent node is stateless**
- All agent state is carried explicitly in the workflow JSON
- Agent output is parsed and merged back into the state
- The agent loop is simulated using workflow routing
- Iterations are controlled using an explicit counter

---

## 📁 Files

```text
n8n-agent/
│
├── workflow.json      # Exported n8n workflow
├── README.md          # This file
└── screenshots/       # Optional workflow screenshots
```

---

## 🔁 Agent Loop (High Level)

1. Workflow initializes state
2. AI Agent decides next action
3. Workflow routes based on action
4. State is updated (history, iteration)
5. Loop continues or stops based on conditions

---

## 🧩 Key Learning

Frameworks accelerate delivery, but:
- they hide state
- they hide loop mechanics
- they require discipline to avoid bugs

This implementation highlights the importance of **explicit state management**
when using agent frameworks.

---

## ✅ Takeaway

This folder demonstrates:
- how agent frameworks actually behave
- where control is gained and lost
- why agent design must come before tools

It should be read alongside the custom agent implementation
to fully understand the trade-offs.
