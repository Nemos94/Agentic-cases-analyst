# Agent Comparison — Custom Agent vs n8n Agent

## Context
This project implements the same **Case Analyst Agent** in two ways:
1. A custom Python implementation with explicit loop and state
2. A framework-based implementation using the n8n AI Agent (LangChain)

The goal is not to choose a “winner”, but to understand trade-offs.

---

## Agent Loop

**Custom Agent**
- Explicit `while` loop
- Clear max iterations
- Full control over stop conditions

**n8n Agent**
- Loop is implicit
- Iterations simulated via workflow routing
- Requires explicit guardrails to avoid infinite loops

**Insight:**  
Frameworks simplify execution but hide loop mechanics.

---

## State & Memory

**Custom Agent**
- Explicit `CaseState` object
- Clear separation between facts, confidence, and reasoning
- Easy to audit and test

**n8n Agent**
- State lives in the JSON flowing between nodes
- Memory is implicit and must be manually preserved
- Easier to lose context if not careful

**Insight:**  
n8n requires discipline to maintain state explicitly.

---

## Decision Making

**Custom Agent**
- LLM used only for decision selection
- Output constrained to strict JSON
- Fallback to escalation on error

**n8n Agent**
- LLM handles decision + tool selection
- Prompt placement is critical (System vs User Message)
- Easier to misconfigure without clear design

**Insight:**  
Custom agents offer stronger guarantees; frameworks offer speed.

---

## Tool Usage

**Custom Agent**
- Tools are explicit functions
- State updated manually after each call

**n8n Agent**
- Tools are nodes
- Easier visual integration
- Less explicit control over how results affect state

---

## Observability

**Custom Agent**
- Explicit reasoning trace
- Easier to explain and debug

**n8n Agent**
- Visual execution logs
- Reasoning spread across nodes and outputs

---

## When to Use Each Approach

**Use Custom Agent when:**
- You need strict governance and auditability
- The agent has complex decision boundaries
- You want full control over behavior

**Use n8n Agent when:**
- Speed of delivery matters
- Integration with external systems is the priority
- The agent logic is relatively simple

---

## Final Takeaway
Frameworks are powerful, but understanding agent fundamentals is essential.
Building the agent from scratch first made the framework implementation safer,
more predictable, and easier to debug.