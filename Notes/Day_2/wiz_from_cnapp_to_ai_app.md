# Wiz: From CNAPP to AI-APP — Google's Flagship AI Security Platform

![Introducing the Wiz: From CNAPP to AI-APP](assets/wiz_from_cnapp_to_ai_app.png)

## Overview

**Wiz** represents Google Cloud's landmark cybersecurity platform integration, fundamentally expanding Google Cloud's enterprise security portfolio by bridging traditional **Cloud-Native Application Protection Platforms (CNAPP)** into modern **AI Application Protection Platforms (AI-APP)**.

As enterprise customers deploy autonomous agents, Model Context Protocol (MCP) servers, Vertex AI models, and Gemini Enterprise pipelines across multi-cloud environments, Wiz provides the end-to-end security fabric. Centered on the **Wiz Graph**, it correlates risk from source code and CI/CD pipelines to cloud infrastructure and live agent runtime execution.

---

## The AI Operating Model & Mika

Wiz introduces a dedicated **AI Operating Model** that secures both human developer workflows and autonomous agent swarms:
* **Mika (Wiz AI Companion)**: An embedded AI security partner that contextualizes complex graph findings, generates automated remediation code, and triages multi-cloud risks.
* **Autonomous AI Agents & Swarms**: Real-time inspection and guardrail enforcement for developer agents (Antigravity, JetSki, ADK agents) and operational systems.
* **Bidirectional Correlation**:
  * **Runtime to Code**: Automatically traces exploitable runtime anomalies back to the exact source repository and line of code, opening pull requests / fix CLs automatically.
  * **Code to Runtime**: Proactively simulates reachable attack paths in the cloud before vulnerable code or tool schemas are deployed to production.

---

## The AI-APP End-to-End Operating Model

```mermaid
graph TD
    subgraph Lifecycle["🔄 Full AI Lifecycle Security (Runtime to Code & Code to Runtime)"]
        direction LR
        Code["💻 <b>Code</b><br/>(Repos, Specs, Prompts)"]
        Pipe["⚙️ <b>Pipeline</b><br/>(CI/CD, Eval, Models)"]
        Graph["🌐 <b>Security Graph</b><br/><i>(Contextual Correlation Engine)</i>"]
        Cloud["☁️ <b>Cloud</b><br/>(IAM, Vertex AI, BigQuery)"]
        Runtime["⚡ <b>Runtime</b><br/>(Live Agents, MCP Servers)"]

        Code ==> Pipe ==> Graph ==> Cloud ==> Runtime
        Runtime -. "<b>Runtime to Code:</b> Auto-fix exploitable risk at source" .-> Code
        Code -. "<b>Code to Runtime:</b> Proactively test reachable paths" .-> Runtime
    end
```

---

## The 3 Pillars of AI-APP Security

```mermaid
graph TD
    subgraph Pillars["🛡️ The 3 Product Pillars"]
        direction TB
        
        P1["⚡ <b>WIZ Code</b><br/><i>Secure AI development at the source</i><br/>• Scans agent code, prompts, and MCP tool schemas<br/>• Detects hardcoded API keys &amp; insecure endpoints<br/>• Automated runtime-to-code PR remediation"]
        
        P2["☁️ <b>WIZ Cloud</b><br/><i>Contextualize &amp; prioritize AI risk across cloud</i><br/>• Full AI Inventory &amp; AI Bill of Materials (AI BOM)<br/>• Maps toxic combinations &amp; AI attack paths<br/>• Audits Agent &amp; MCP permissions in Cloud IAM"]
        
        P3["🛡️ <b>WIZ Defend</b><br/><i>Detect &amp; contain malicious AI runtime behavior</i><br/>• Real-time Prompt Injection defense<br/>• Rogue Agent anomaly detection &amp; sensor isolation<br/>• Blocks abnormal tool execution &amp; data exfiltration"]
    end
```

---

## The 3 Horizontal AI Security Layers

### 1. Visibility (Know What You Run)
* **AI Inventory (Code & Cloud)**: Discovers all models (proprietary, fine-tuned, third-party APIs), agent harnesses, MCP servers, and vector databases across multi-cloud environments.
* **AI Bill of Materials (AI BOM)**: Tracks model provenance, base weights, training datasets, licenses, dependencies, and attached toolsets.
* **AI Service Catalog**: Centralizes discovery of verified, internal enterprise AI endpoints.

---

### 2. Risk & Posture (AI-SPM)
* **AI Misconfigurations**: Identifies publicly exposed Vertex AI endpoints, unauthenticated MCP servers, overly permissive Cloud Storage buckets, and missing VPC Service Controls.
* **AI Posture & Attack Paths**: Correlates vulnerabilities, excessive IAM privileges, and reachable network paths to identify true exploitable attack chains targeting AI systems.
* **Agent & MCP Risk**: Detects overly permissive tool definitions (e.g. mutating tools granted read-only scopes) and unmonitored tool endpoints.

---

### 3. Runtime Protection (Defend Live Agents)
* **Rogue Agent Defense & Sensors**: Monitors autonomous agents for abnormal behavior (e.g., unexpected token spikes, out-of-bounds file system scans, anomalous SQL queries) and halts execution in real time.
* **Prompt Injection Defense**: In-line threat inspection mitigating Direct Prompt Injections (jailbreaks) and Indirect Prompt Injections (IPI) hidden inside web content or retrieved documents.

---

## Comprehensive AI-APP Capability Matrix

| Lifecycle Stage | Security Layer | Core Capabilities | Mitigated Threats |
| :--- | :--- | :--- | :--- |
| **Code & Build** | **Wiz Code** | Static code analysis, prompt scanning, hardcoded secret detection, automated PR fixes | Leaked API credentials, vulnerable base model dependencies |
| **Cloud & Posture** | **Wiz Cloud** | AI BOM generation, toxic combination graph, IAM privilege analysis for agents | Publicly exposed models, unauthenticated MCP servers, data poisoning |
| **Runtime & Ops** | **Wiz Defend** | Rogue agent behavioral sensors, prompt injection filters, dynamic tool execution guardrails | Indirect prompt injection, rogue agent data exfiltration, tool abuse |
