# Multi-Agent Architectures: Choosing the Right Pattern

![Choosing the Right Pattern](assets/choosing_the_right_pattern.png)

## Overview

Selecting the optimal multi-agent design pattern is an engineering decision governed by three core constraints: **Task Shape**, **Latency Tolerance**, and **Cost Budget**.

> **"Predefined, repeatable steps belong in workflow patterns. Open-ended, ambiguous goals belong in dynamic patterns."**

---

## The 3 Critical Selection Questions

```mermaid
graph TD
    Start["🏗️ Multi-Agent Pattern Selection"]
    
    Q1["1️⃣ What's the task shape?<br/><i>Deterministic vs. Open-ended</i>"]
    Q2["2️⃣ How much latency can you tolerate?<br/><i>Interactive (<2s) vs. Deep Async (>10s)</i>"]
    Q3["3️⃣ What's your cost budget?<br/><i>Inference call count & token economics</i>"]
    
    Start --> Q1 --> Q2 --> Q3
```

### 1. What's the task shape?
* **Predefined, repeatable steps $\rightarrow$ Workflow Patterns**: When the business logic, transformation steps, or validation checkpoints are known at design time, encode them as deterministic code workflows.
* **Open-ended, ambiguous goals $\rightarrow$ Dynamic Patterns**: When the path to resolution depends entirely on the unstructured input query, empower the AI model to triage, decompose, and route at runtime.

### 2. How much latency can you tolerate?
* **Fast, interactive user-facing responses**: Minimize model hops ($1 \text{ or } 2 \text{ calls max}$). Use **Parallel** fan-outs or single-stage **Coordinators** powered by lightweight models (e.g. Gemini 2.5 Flash).
* **Asynchronous deep-thinking / batch workloads**: High latency tolerance permits multi-stage **Hierarchical Decomposition**, **Iterative Refinement** loops, and multi-round **Swarms**.

### 3. What's your cost budget?
* **Every dynamic routing decision is another model invocation**: A 3-tier hierarchical swarm can easily consume 10–25 LLM calls per user prompt.
* **Cost Optimization Strategy**: Use deterministic workflow gates where possible, and use asymmetric model sizing (Flash for routing/workers, Pro for complex synthesis).

---

## Workload Characteristic to Pattern Mapping

| Workload Characteristic | Pattern Family | Recommended Pattern | Architectural Rationale |
| :--- | :--- | :--- | :--- |
| **Fixed order, repeatable** | 🟢 Workflow | **Sequential** | Strict linear dependency chain ($A \rightarrow B \rightarrow C$) with deterministic transitions. |
| **Independent, concurrent** | 🟢 Workflow | **Parallel** | Concurrent worker fan-out bounded by the slowest task ($\max_i(T_i)$). |
| **Improve over cycles** | 🟢 Workflow | **Iterative Refinement** | 3-agent closed loop (Generator $\rightarrow$ Evaluator $\rightarrow$ Prompt Enhancer) for quality convergence. |
| **Needs a validation step** | 🟢 Workflow | **Review & Critique** | Decoupled 2-agent actor-critic evaluation against explicit objective rubrics. |
| **Adaptive routing, varied input** | 🔵 Dynamic | **Coordinator** | Central supervisor model dynamically classifies intent and delegates to specialized subagents. |
| **Ambiguous, multi-level planning** | 🔵 Dynamic | **Hierarchical** | Multi-tier executive lead $\rightarrow$ domain lead $\rightarrow$ leaf worker recursive decomposition. |
| **Debate toward synthesis** | 🔵 Dynamic | **Swarm** | Decentralized peer-to-peer handoffs and lateral negotiation without a coordinator bottleneck. |

---

## Architectural Decision Tree

```mermaid
graph TD
    Root["❓ What is your primary workload requirement?"]

    Root --> D1{"Are steps known at design time?"}
    
    D1 -- "Yes (Deterministic)" --> W_Branch["🟢 Workflow Patterns"]
    W_Branch --> W1{"What is the step relationship?"}
    W1 -- "Linear dependencies" --> Seq["Sequential Pipeline"]
    W1 -- "Independent subtasks" --> Par["Parallel Fan-Out"]
    W1 -- "Needs quality rubric check" --> Rev["Review & Critique"]
    W1 -- "Automated prompt tuning" --> Iter["Iterative Refinement"]

    D1 -- "No (Ambiguous / Dynamic)" --> D_Branch["🔵 Dynamic Patterns"]
    D_Branch --> D2{"What is the coordination style?"}
    D2 -- "Central triage & tool isolation" --> Coord["Coordinator / Router"]
    D2 -- "Multi-level enterprise planning" --> Hier["Hierarchical Decomposition"]
    D2 -- "Peer handoffs & debate" --> Swarm["Autonomous Swarm"]
```

---

## Production Hybrid Architectures

In enterprise software engineering, real-world systems combine workflow and dynamic patterns into powerful **hybrid compositions**:

```mermaid
graph TD
    User["👤 User Request"] --> Gateway["👑 Dynamic Coordinator (Triage)"]
    
    subgraph Route A: Deterministic Pipeline
        Gateway -.->|Intent: Report Generation| S1["Extract"] --> S2["Transform"] --> S3["Review & Critique Gate"]
    end

    subgraph Route B: Parallel Fan-Out
        Gateway -.->|Intent: Compliance Audit| P1["Security"] & P2["Legal"] & P3["Cost"]
        P1 & P2 & P3 --> PAgg["Synthesizer"]
    end

    subgraph Route C: Multi-Tier Hierarchy
        Gateway -.->|Intent: Full App Migration| Lead["Hierarchical Migration Lead"]
        Lead --> W1["Infra Worker"] & W2["Database Worker"]
    end
```

### Hybrid Engineering Principles:
1. **Dynamic at Ingress, Deterministic in Core**: Use a dynamic **Coordinator** at the front door to interpret user intent, then route into deterministic **Sequential** or **Parallel** workflows.
2. **Deterministic Quality Gates in Dynamic Swarms**: Embed deterministic validation checks (unit tests, schema linters) at each handoff boundary within dynamic swarms.
3. **Budget & Timeout Envelopes**: Always wrap dynamic multi-agent loops in global deadline timers and token ceiling circuit breakers.
