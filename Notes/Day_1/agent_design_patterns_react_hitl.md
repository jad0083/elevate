# Agent Design Patterns: ReAct & Human-in-the-Loop

![Agent Design Patterns: ReAct & Human-in-the-Loop](assets/agent_design_patterns_react_hitl.png)

## Overview

Core architectural patterns govern how autonomous agents process goals, invoke external tools, and incorporate oversight. Two foundational patterns are **ReAct** and **Human-in-the-Loop (HITL)**.

---

## 1. ReAct (Reason + Act)

Combines dynamic chain-of-thought reasoning with tool execution in an iterative feedback loop until the termination condition or goal is reached.

### Execution Loop

```mermaid
graph TD
    T["1. Think (Reason)"] --> A["2. Act (Tool Call)"]
    A --> O["3. Observe (Tool Output)"]
    O --> R{"Goal Reached?"}
    R -- No --> T
    R -- Yes --> F["Final Answer"]
```

* **Formula**: `Think → Act → Observe → Repeat`
* **Best For**:
  * Multi-step research and exploratory troubleshooting.
  * Workflows where the next tool call depends on the output of previous tools.
* **Key Benefit**: Enables dynamic error recovery and self-correction during execution.

---

## 2. Human-in-the-Loop (HITL)

Introduces explicit human verification and authorization checkpoints before executing sensitive, destructive, or costly actions.

### Execution Flow

```mermaid
graph LR
    A["Agent Prepares Action"] --> H["Human Review & Intercept"]
    H --> App{"Approved?"}
    App -- Yes --> E["Execute Action"]
    App -- No --> F["Feedback / Abort"]
    F --> A
```

* **Formula**: `Agent → Human Review → Approval → Execution`
* **Best For**:
  * High-stakes operations (financial transactions, deleting resources, deploying to production).
  * High-ambiguity decisions requiring human alignment before proceeding.
* **Key Benefit**: Combines agentic automation speed with human safety guarantees and compliance governance.

---

## Comparative Pattern Summary

| Pattern | Control Model | Latency Profile | Primary Risk / Cost | Ideal Use Case |
| :--- | :--- | :--- | :--- | :--- |
| **ReAct** | Fully autonomous loop | Variable (multi-turn tool calls) | Runaway loops / token consumption | Complex research, investigations, automated debugging |
| **Human-in-the-Loop (HITL)** | Semi-autonomous with gates | Blocked on human review | User friction / delayed execution | Destructive mutations, production deployments, financial operations |
