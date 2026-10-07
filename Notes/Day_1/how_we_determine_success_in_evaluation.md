# Evaluation Strategy: How We Determine Success in Evaluation

![How we determine success in evaluation](assets/how_we_determine_success_in_evaluation.png)

## Overview

In enterprise AI engineering, evaluation is not an isolated academic exercise. Technical metrics (e.g. cosine similarity, perplexity, or raw token throughput) are meaningless if they are disconnected from business value. Determining success requires an explicit **3-step translation funnel** that bridges organizational objectives to automated technical rubrics and verified deployment decisions.

> **"Step 1: Identify Business KPIs → Step 2: Establish Metrics & Rubrics → Step 3: Execute Evaluation to verify organizational goal attainment."**

---

## The 3-Step Evaluation Success Framework

```mermaid
graph LR
    subgraph Step 1: Business KPIs
        S1["🏢 1. Business KPIs<br/><i>What is the organizational goal?</i>"]
    end

    subgraph Step 2: Metrics & Rubrics
        S2["📐 2. Metrics & Rubrics<br/><i>What do we measure to know AI meets goals?</i>"]
    end

    subgraph Step 3: Execute Evaluation
        S3["🚀 3. Execute Evaluation<br/><i>Will the AI, if deployed, help meet goals?</i>"]
    end

    S1 ==>|Translate & Operationalize| S2
    S2 ==>|Benchmark & Verify| S3
```

---

## Detailed Step-by-Step Breakdown

### Step 1: Identify and Map Business KPIs
* **Core Question**: *What is the organizational goal?*
* **Focus**: Defining the high-level business impact, financial return on investment (ROI), efficiency targets, or customer satisfaction bars.
* **Key Questions for Architects**:
  * What business bottleneck is this agent automating or augmenting?
  * What is the current human baseline for time, cost, and error rate?
  * What is the acceptable risk tolerance and cost of an AI hallucination?
* **Typical Enterprise KPIs**:
  * *Support*: Reduce average handle time (AHT) from 12 mins to 3 mins; deflect 60% of Tier-1 tickets; maintain CSAT $\ge 92\%$.
  * *Engineering*: Accelerate pull request cycle time from 4 hours to 20 minutes; zero regression bugs.
  * *Finance/Legal*: 100% compliance with audit regulations; zero PII leakage.

---

### Step 2: Establish Metrics and Rubrics (The Translation Bridge)
* **Core Question**: *What do we measure to know the AI is meeting organizational goals?*
* **Focus**: Translating qualitative business KPIs into concrete, machine-verifiable evaluation metrics and LLM-as-a-judge rubrics.
* **The KPI-to-Rubric Translation Map**:

```mermaid
graph TD
    KPI1["Business KPI: Reduce Support Handle Time"] --> M1["AI Metric: Turn Count ≤ 3<br/>AI Metric: P95 Latency ≤ 3.5s<br/>AI Metric: Tool Call Precision ≥ 98%"]
    
    KPI2["Business KPI: Zero Regulatory Compliance Risk"] --> M2["AI Rubric: Grounding Score ≥ 4.8 / 5.0<br/>AI Scanner: 100% PII Redaction<br/>AI Metric: 0% Hallucinated Citations"]
    
    KPI3["Business KPI: Accelerate Developer Velocity"] --> M3["AI Metric: Code Syntax Pass Rate = 100%<br/>AI Metric: Unit Test Green Rate ≥ 95%<br/>AI Rubric: Idiomatic Style Score ≥ 4.5 / 5.0"]
```

---

### Step 3: Execute the Evaluation
* **Core Question**: *Will the AI, if deployed, help meet organizational goals?*
* **Focus**: Running the agent against golden test datasets, scoring execution traces with deterministic matchers and calibrated LLM judges, and producing an objective Go / No-Go deployment decision.
* **Evaluation Pipeline**:

```mermaid
graph TD
    TestSet["📁 500 Golden Test Cases"] --> Run["🤖 Run ADK Agent Under Test"]
    Run --> Traces["📝 Collect Trajectories & Responses"]
    Traces --> Judge["⚖️ Evaluate against Step 2 Rubrics"]
    
    Judge --> Gate{"Meets Business KPI Thresholds?"}
    Gate -- "Yes (High Confidence)" --> Deploy["🚀 Approve Production Deployment"]
    Gate -- "No (Regressions Found)" --> Refine["🛠️ Refine Prompts, Tools & Skills"]
```

---

## Enterprise KPI-to-Rubric Translation Matrix

| Business Domain | Organizational KPI (Step 1) | Translated Technical Metrics & Rubrics (Step 2) | Target Threshold (Step 3) |
| :--- | :--- | :--- | :--- |
| **Customer Support Concierge** | Deflect Tier-1 tickets while maintaining $\ge 90\%$ CSAT | • Tool Call Accuracy (correct CRM lookup)<br/>• Tone & Empathy Rubric<br/>• Turn Count to Resolution | • Tool Accuracy $\ge 98\%$<br/>• Tone Score $\ge 4.5/5.0$<br/>• $\le 3$ conversational turns |
| **Enterprise Legal & Compliance** | Zero regulatory fines & strict policy adherence | • Factual Grounding (faithfulness to policy doc)<br/>• Safety Scanner (PII redaction)<br/>• Hallucination Rate | • Grounding $\ge 4.9/5.0$<br/>• $100\%$ PII Redaction<br/>• $0\%$ Uncited Claims |
| **Autonomous DevOps SRE** | Reduce MTTR (Mean Time to Resolution) during SEVs | • Metric Query Precision<br/>• RCA Diagnostic Accuracy<br/>• Step Efficiency (No infinite loops) | • Query Precision $\ge 95\%$<br/>• RCA Match Rate $\ge 90\%$<br/>• Max 6 tool calls |

---

## Architectural Rules for Evaluation Success

1. **Never Ship on Vibe Checks Alone**:
   * An agent that "feels smart" during manual testing can cause severe organizational damage if not verified against objective KPI rubrics.
2. **Every Technical Metric Must Tie to a Business Outcome**:
   * If you are measuring a metric that does not impact cost, latency, safety, or quality, remove it from your eval pipeline.
3. **Automate Step 3 in CI/CD**:
   * Evaluation is not a one-time pre-launch audit; it is a continuous automated quality gate on every prompt, tool, or model change.
