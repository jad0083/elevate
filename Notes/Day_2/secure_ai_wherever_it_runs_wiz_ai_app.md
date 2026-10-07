# Secure AI Wherever It Runs: Multi-Environment Protection with Wiz AI-APP

![Secure AI Wherever It Runs with Wiz AI APP](assets/secure_ai_wherever_it_runs_wiz_ai_app.png)

## Overview

Modern enterprise AI deployments do not reside in a single siloed environment. AI workloads execute across local developer laptops, third-party SaaS ecosystems, hyperscaler cloud platforms, and custom in-house agent frameworks.

**Wiz AI-APP** delivers ubiquitous, environment-agnostic security by aggregating, analyzing, and correlating signals from all four operational tiers into the centralized **Wiz Security Graph**.

---

## Architecture: The 4 Ingestion Environments & The Security Graph

```mermaid
graph TD
    subgraph Env1["💻 1. Workstations"]
        W1["Windows / macOS / Linux"]
        W2["Local IDE Extensions &amp; CLIs"]
        W3["Local MCP stdio Subprocesses"]
    end

    subgraph Env2["☁️ 2. SaaS AI"]
        S1["Microsoft Copilot Studio"]
        S2["Salesforce Agentforce"]
        S3["OpenAI / Anthropic APIs"]
    end

    subgraph Env3["🚀 3. Cloud PaaS"]
        P1["Google Cloud (Vertex AI, GKE)"]
        P2["AWS (Bedrock, SageMaker)"]
        P3["Azure AI"]
    end

    subgraph Env4["🛠️ 4. Custom Apps"]
        C1["LangChain / LlamaIndex"]
        C2["Hugging Face Models"]
        C3["PyTorch / TensorFlow Pipelines"]
    end

    subgraph Graph["🌐 Centralized Wiz Security Graph"]
        Core["<b>Wiz Security Graph</b><br/><i>Correlates Identity, Code, Cloud, &amp; Runtime</i>"]
    end

    subgraph Outcomes["🎯 3 Core Security Outcomes"]
        O1["👁️ <b>Visibility:</b> MCPs, Models, Agents, &amp; Skills"]
        O2["⚠️ <b>Risk:</b> Toxic Combinations &amp; Attack Paths"]
        O3["🛡️ <b>Runtime:</b> Continuous Threat Detection &amp; Response"]
    end

    W1 ==> Core
    S1 ==> Core
    P1 ==> Core
    C1 ==> Core

    Core ==> O1
    Core ==> O2
    Core ==> O3
```

---

## The 4 Monitored AI Environments

### 1. Workstations (Developer & Local Endpoints)
* **Scope**: Developer endpoints across Windows, macOS, and Linux running local IDE extensions (Antigravity 2.0, VS Code), terminal CLIs (`agy`), and local MCP `stdio` servers.
* **Security Focus**: Hardcoded API secrets in `.env` files, unverified local MCP server binaries, and unconstrained local shell access granted to autonomous agents.

---

### 2. SaaS AI Ecosystems
* **Scope**: Third-party enterprise AI products including **Microsoft Copilot Studio**, **Salesforce Agentforce**, **OpenAI**, and **Anthropic**.
* **Security Focus**: Shadow AI SaaS discovery, excessive data sharing permissions, unmonitored API token consumption, and third-party data retention compliance.

---

### 3. Hyperscaler Cloud PaaS
* **Scope**: Managed cloud AI infrastructure across **Google Cloud (Vertex AI, Cloud Run, GKE)**, **AWS (Bedrock, SageMaker)**, and **Azure AI**.
* **Security Focus**: Public model endpoint exposure, overly permissive Cloud IAM service account bindings, missing VPC Service Controls (VPC-SC), and unencrypted vector databases.

---

### 4. Homegrown Custom AI Applications
* **Scope**: In-house agent frameworks, model training scripts, and custom inference microservices built with **LangChain**, **Hugging Face**, **PyTorch**, and Google ADK.
* **Security Focus**: Insecure model weight deserialization (pickle vulnerabilities), prompt injection vulnerabilities in custom tools, and open supply chain dependencies.

---

## The 3 Core Security Outcomes

```mermaid
graph LR
    subgraph Outcomes["🌟 The 3 Pillars of Wiz AI-APP Protection"]
        direction TB
        
        V["👁️ <b>1. FULL-STACK VISIBILITY</b><br/>• Complete inventory of all MCP servers, models, agents, and skills<br/>• Comprehensive AI Bill of Materials (AI BOM)"]
        
        R["⚠️ <b>2. CONTEXTUAL RISK &amp; ATTACK PATHS</b><br/>• Eliminates alert noise by mapping 'toxic combinations'<br/>• Simulates reachable attack paths to sensitive training data"]
        
        T["🛡️ <b>3. ACTIVE RUNTIME DEFENSE</b><br/>• Real-time detection of rogue agent drift and abnormal tool calls<br/>• Dynamic inline prompt injection blocking"]
    end
```

---

## Multi-Environment Protection Matrix

| Environment Tier | Typical Workloads | Key Security Capabilities | Mitigated Risks |
| :--- | :--- | :--- | :--- |
| **Workstations** | Antigravity CLI, IDE extensions, local MCP | Endpoint secret scanning, binary vetting | Local privilege escalation, leaked API tokens |
| **SaaS AI** | Copilot, Salesforce, ChatGPT Enterprise | SaaS posture management, OAuth auditing | Shadow AI adoption, sensitive data leakage |
| **Cloud PaaS** | Vertex AI, GKE, BigQuery, AWS Bedrock | Toxic combination analysis, IAM posture | Public endpoint exposure, confused deputy attacks |
| **Custom Apps** | LangChain, PyTorch, Hugging Face | Supply chain scanning, model weight audits | Deserialization exploits, poisoned model weights |
