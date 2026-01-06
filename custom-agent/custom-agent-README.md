# Custom Agent (No Framework)

This folder contains the **from-scratch implementation** of the Agentic Case Analyst,
built without any agent framework.

The goal of this implementation is **clarity and control**, not speed.

---

## 🎯 Purpose

This version demonstrates:
- How an AI agent actually works under the hood
- Explicit state management
- A fully controlled agent loop
- LLM usage limited to decision-making only

No orchestration, memory, or control flow is hidden.

---

## 🧠 Agent Responsibilities

The agent acts as a **Case Analyst** and decides the next step for a customer case.

Possible actions:
- `CONCLUDE` – Enough information for a human to act
- `REQUEST_CONTEXT` – Missing critical information
- `CONSULT_HISTORY` – Historical data may help
- `ESCALATE` – Risk or ambiguity requires human review

⚠️ The agent never responds directly to the customer.

---

## 🏗️ Key Components

```text
custom-agent/
│
├── agent/
│   ├── agent.py     # Agent loop and decision logic
│   └── state.py     # Explicit agent state (CaseState)
│ 
│
└── README.md
```

---

## 🔁 Agent Loop (Conceptual)

1. Initialize agent state
2. Analyze the case
3. Ask the LLM to decide the next action
4. Update state
5. Repeat until:
   - case is concluded
   - case is escalated
   - max iterations reached

All loop boundaries are enforced in code.

---

## 🧩 Why No Framework?

Frameworks are powerful, but they:
- hide state
- hide loops
- mix decision-making with execution

This implementation exists to make those concepts **explicit and testable**.

---

## 🚀 How to Run (Optional)

```bash
python main.py
```

(Adjust entry point as needed.)

---

## ✅ Takeaway

If you understand this folder, you understand:
- what agent frameworks abstract
- where their limits are
- when you might want to avoid them

This implementation is the **reference design** for the framework-based version.
