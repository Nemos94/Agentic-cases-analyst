# Technical Decisions & Learnings

This document captures the key technical decisions made during the
implementation of the **Agentic Case Analyst**, and the reasoning behind them.

The goal is to make design trade-offs explicit and auditable.

---

## 1. Agent-First Design (Before Frameworks)

**Decision:**  
Design the agent behavior, state, and loop *before* implementing it in any framework.

**Why:**  
Frameworks abstract critical concepts such as state, memory, and control flow.
Designing the agent from scratch first ensured:
- Clear responsibility boundaries
- Predictable behavior
- Easier debugging once implemented in n8n

**Learning:**  
Frameworks accelerate delivery, but only if the agent logic is already well-defined.

---

## 2. Explicit Agent State (No Hidden Memory)

**Decision:**  
Treat agent state as explicit data passed between steps, not as implicit memory.

**State fields include:**
- `email_text`
- `historical_context`
- `iteration`
- `agent_decision`

**Why:**  
All memory must be managed by the workflow itself.

**Learning:**  
In low-code tools, state management is the developer’s responsibility.

---

## 3. Agent Decides, Workflow Acts

**Decision:**  
Separate **decision-making** from **execution**.

- The AI Agent decides *what* to do next.
- The workflow decides *how* to do it.

**Why:**  
This avoids overloading the LLM with orchestration logic and keeps actions deterministic.

**Learning:**  
Agents should reason, not orchestrate infrastructure.

---

## 4. Conservative Case Analysis Strategy

**Decision:**  
Allow the agent to request additional context even after consulting historical data.

**Why:**  
Historical resolution does not guarantee that:
- The same solution was attempted again
- The issue has the same root cause
- The current impact or urgency is known

**Outcome:**  
The agent may still return `REQUEST_CONTEXT` after `CONSULT_HISTORY`.

**Learning:**  
A conservative agent is preferable to an overconfident one in customer support scenarios.

---

## 5. Loop Control and Safety

**Decision:**  
Limit agent iterations using an explicit `iteration` counter.

**Why:**  
To prevent infinite loops and ensure predictable execution.

**Learning:**  
LLMs should never control loop termination implicitly.

---

## 6. JSON Contracts Everywhere

**Decision:**  
All agent outputs must conform to a strict JSON schema:
```json
{
  "action": "<ONE_ACTION>",
  "reason": "<short explanation>"
}
```

**Why:**  
- Enables deterministic routing
- Simplifies debugging
- Prevents prompt drift

**Learning:**  
Strong contracts are essential for reliable agent systems.

---

## 7. No Hidden Framework Magic

**Decision:**  
Avoid referencing other nodes directly inside prompts (e.g. `$('NodeName')`).

**Why:**  
- Breaks encapsulation
- Creates fragile dependencies
- Makes reasoning about state harder

**Learning:**  
Agents should consume state, not query the workflow graph.

---

## Final Takeaway

This project demonstrates that:
- Agent reliability comes from design, not tools
- Low-code platforms require explicit state discipline
- LLMs are powerful decision engines, but poor system orchestrators

Designing the agent first made the framework implementation predictable,
auditable, and production-aligned.
