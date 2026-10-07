# Google Cloud CE & DBCE Architecture Decision Playbook

Actionable decision matrices, architectural trade-offs, and field rules distilled from the 5-Day Elevate Agent Engineering Curriculum.

---

## 1. Customer Field Scenarios & Decision Rules

| Customer Scenario / Question | Recommended Google Cloud Architecture & Decision Rule | Primary Curriculum Reference |
| :--- | :--- | :--- |
| **"Should we build a multi-agent mesh for our workflow?"** | Start with **1 frontier model + modular Skills + MCP**. Only add multiple agents when subtasks are **parallelizable (`+81%` gain)** or require isolated permissions/context. Always use a **Centralized Orchestrator (`4.4×` vs `17.2×` error amplification)** with Pydantic schema gates—never split strict sequential reasoning across agents (`39%–70%` degradation). | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md), [architecture_is_a_safety_feature.md](../Notes/Day_1/architecture_is_a_safety_feature.md) |
| **"Our Text-to-SQL agent writes valid SQL that returns wrong business numbers (e.g., WAU, ARR)."** | Pair **Google MCP Toolbox for Databases (`go/mcp-toolbox`)** with a git-native **Open Knowledge Format (OKF)** bundle (`tables/`, `metrics/`, `policies/`) enforcing frontmatter provenance (`verified: true`, `status: stable`). | [open_knowledge_format_okf.md](../Notes/Day_1/open_knowledge_format_okf.md), [mcp_toolbox_for_databases_overview.md](../Notes/Day_4/mcp_toolbox_for_databases_overview.md) |
| **"Should we deploy our ADK agent on Agent Runtime, Cloud Run, or GKE?"** | Use **Agent Runtime (Vertex AI Agent Engine)** for turnkey managed state (`VertexAiSessionService`) and $<800\text{ms}$ cold starts. Use **Cloud Run** for custom Docker/scale-to-zero APIs, **but never leave default `InMemorySessionService` enabled**—pass `--agent_engine_id` or wire Firestore/Cloud SQL/AlloyDB. Use **GKE** for $0\text{ms}$ pre-warmed pods, custom GPUs/TPUs, or strict VPC-SC. | [three_targets_one_decision.md](../Notes/Day_1/three_targets_one_decision.md), [a_restart_must_not_erase_memory.md](../Notes/Day_1/a_restart_must_not_erase_memory.md) |
| **"Can our developers download the standalone Antigravity IDE?"** | **No (Hard Blocker).** The standalone consumer `Antigravity IDE` lacks Google Cloud ToS, HIPAA/SOC2, IP indemnification, and Workspace/`@google.com` login. Deploy **Antigravity IDE Extensions** (VS Code, IntelliJ, Visual Studio, Xcode), **`agy` CLI**, or **Antigravity 2.0 Hub**. | [dont_use_antigravity_ide.md](../Notes/Day_2/dont_use_antigravity_ide.md), [antigravity_vs_jetski_ce_guidelines.md](../Notes/Day_1/antigravity_vs_jetski_ce_guidelines.md) |
| **"How do we stop 'Vibe Coding' and 'Almost Right' (66%) AI code?"** | Enforce **Specification-Driven Development (SDD)** using the 4-file contract (`README.md`, `AGENTS.md`, `SPEC.md`, `SKILL.md`), require read-before-edit and deterministic test gates (`verify.py` / `pytest`) in `AGENTS.md`, and enforce a **Test-File Immutability Gate** in CI. | [four_files_four_audiences.md](../Notes/Day_2/four_files_four_audiences.md), [eval_dimension_7_self_repair_behaviour.md](../Notes/Day_4/eval_dimension_7_self_repair_behaviour.md) |
| **"Our agents are slow, expensive, and hallucinate tool parameters."** | Apply **Context Economics**: (1) Keep global skills lean (5–15), (2) Partition monolithic MCP servers into **Virtual MCP Toolsets** ($1\text{k–}4\text{k}$ vs $30\text{k–}80\text{k}$ tokens), (3) Cap CLI outputs (`-max_results=50`), (4) Isolate exploration in **Subagents** + **Git Worktrees**, and (5) Use **Static-First Prompt Ordering** for 90% Implicit Context Caching. | [toolsets_protect_the_context_window.md](../Notes/Day_2/toolsets_protect_the_context_window.md), [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md) |
| **"Why choose Google ADK 2.0 over LangGraph?"** | **LangGraph** is an orchestration-only library requiring separate paid LangSmith SaaS and custom Docker/LangServe plumbing. **Google ADK 2.0** is a unified enterprise platform combining `StateGraph` + `agents-cli eval` + 1-click Agent Runtime/Cloud Run deploy + SPIFFE Dual-Gate IAM + BigQuery Agent Analytics. | [adk_2_vs_langgraph_competitive_architecture_matrix.md](../Notes/Day_4/adk_2_vs_langgraph_competitive_architecture_matrix.md) |
| **"When do we use MCP vs. A2A?"** | They are **complementary**: **MCP** is the *vertical downward bus* connecting an agent to deterministic tools and databases (`go/mcp-toolbox`); **A2A** is the *horizontal outward bus* federating tasks across opaque black-box agents (SAP, Salesforce Agentforce) via `/.well-known/agent.json`. | [a2a_vs_mcp_coexistence_architecture.md](../Notes/Day_4/a2a_vs_mcp_coexistence_architecture.md) |
| **"Should we use Okta/Entra ID with Cloud Identity SSO or WIF for Gemini Enterprise?"** | Default to **Google Cloud Identity + 3rd-Party SAML/OIDC SSO** for 100% Day-1 feature parity. Use **WIF** only if regulations strictly forbid directory sync—and always deploy **WIF + SCIM** (pure WIF breaks sharing autocomplete and cannot migrate to Cloud Identity later). | [third_party_idp_sso_with_cloud_identity.md](../Notes/Day_2/third_party_idp_sso_with_cloud_identity.md), [wif_for_gemini_enterprise.md](../Notes/Day_2/wif_for_gemini_enterprise.md) |
| **"How do we secure MCP tools and agents against Confused Deputy & Prompt Injection?"** | Enforce the **4-Layer Defense**: (1) **SPIFFE / Cloud IAM Dual-Gate** ($\min(\text{User}, \text{Agent})$ + `roles/mcp.toolUser`), (2) **IAM Deny + CEL** (`tool.isReadOnly == false`), (3) **Model Armor Floor Settings** (`--mcp-sanitization=ENABLED`) + `before_model_callback` DLP scrubbing, and (4) **Wiz AI-APP + CodeMender**. | [mcp_authorization_controls_iam.md](../Notes/Day_2/mcp_authorization_controls_iam.md), [agent_platform_runtime_master_architecture.md](../Notes/Day_4/agent_platform_runtime_master_architecture.md) |

---

## 2. Database & Vector Architecture Matrices (DBCE Reference)

### A. Vector Database Selection Matrix
Source: [vector_database_design_options_tradeoffs.md](../Notes/Day_4/vector_database_design_options_tradeoffs.md)

| Dimension | 1. Managed Dedicated (**Vertex AI Vector Search**) | 2. Integrated Analytical (**BigQuery Vector Search**) | 3. Integrated Transactional (**AlloyDB ScaNN / Cloud SQL `pgvector` / Spanner**) |
| :--- | :--- | :--- | :--- |
| **Core Engine** | Dedicated auto-scaling **ScaNN** index nodes | `VECTOR_SEARCH()` with **IVF / TreeAH** indexes | Co-located `pgvector` (+ AlloyDB ScaNN) / Spanner vector functions |
| **p99 Latency** | **Sub-5ms** | $200\text{ms} \text{ – } 3\text{s}$ | **$5\text{ms} \text{ – } 25\text{ms}$** |
| **Max Scale** | Billions of vectors (high QPS) | Multi-billion vectors (Petabytes) | Millions to tens of millions |
| **Data Sync** | Requires ETL / CDC pipeline | Zero-ETL in-place warehouse queries | **Zero-ETL (Single ACID store, zero sync skew)** |
| **Filtering** | Restricted metadata attributes | Full GoogleSQL joins & expressions | **Full ACID SQL `WHERE` clauses** |
| **Sweet Spot** | Ultra-low-latency conversational agents at billion-vector scale | Enterprise BI, batch RAG, data lake joins | Operational/transactional apps requiring strict ACID consistency |

### B. Legacy Database & Application Modernization Tracks
Sources: [database_modernization_dms_alloydb_cloudsql.md](../Notes/Day_2/database_modernization_dms_alloydb_cloudsql.md), [end_to_end_ai_powered_mainframe_modernization.md](../Notes/Day_2/end_to_end_ai_powered_mainframe_modernization.md), [accelerate_dotnet_modernization_google_cloud_ai.md](../Notes/Day_2/accelerate_dotnet_modernization_google_cloud_ai.md)

- **Oracle / SQL Server $\rightarrow$ AlloyDB vs. Cloud SQL**:
    - Pipeline: **Database Migration Assessment (DMA)** $\rightarrow$ **Serverless DMS Continuous CDC** $\rightarrow$ **Gemini AI PL/SQL & T-SQL Conversion** to `PL/pgSQL`.
    - Choose **AlloyDB for PostgreSQL** for heavy enterprise OLTP, Oracle RAC replacements, and HTAP (**4× faster** OLTP, **100× faster** analytical Columnar Engine, **99.99% SLA inclusive of maintenance**, built-in AlloyDB AI).
    - Choose **Cloud SQL for PostgreSQL** for standard web apps and departmental workloads (**99.95% HA SLA**).
- **COBOL Mainframe $\rightarrow$ Cloud Run / GKE + Spanner / AlloyDB / BigQuery**:
    - Pipeline: **MAT** (extracts natural-language business rules) $\rightarrow$ **Mainframe Agents + Gemini 3.1** (`SPEC.md` $\rightarrow$ Java 21 / Go microservices) $\rightarrow$ **Google Dual Run** (live traffic shadowing & byte-for-byte parity certification) $\rightarrow$ **Mainframe Connector / DMS**.
- **Windows / .NET Framework $\rightarrow$ .NET 8 on Linux**:
    - Pipeline: **CodMod Advisor** in **Modernize Hub** (7-tab assessment) + **Gemini CLI + .NET Skills** via the **$<2\text{ Month}$ .NET Acceleration** or **3–7 Week Accelerator Program** (funded by **RaMP** and **PSF**).

---

## 3. Production Model Serving & FinOps Playbook

Sources: [foundation_model_consumption_options.md](../Notes/Day_5/foundation_model_consumption_options.md), [choosing_the_right_consumption_option.md](../Notes/Day_5/choosing_the_right_consumption_option.md), [routing_patterns_rule_llm_semantic.md](../Notes/Day_5/routing_patterns_rule_llm_semantic.md), [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md)

1. **Right-Size Provisioned Throughput (PT) + PayGo Spillover**:
    - Reserve PTUs for predictable interactive agent baseline traffic, targeting **$80\text{–}85\%$ utilization** on minute-by-minute telemetry, and configure automatic burst spillover to **Standard PayGo** or **Priority PayGo**.
2. **Offload Non-Interactive Workloads ($\ge 50\%$ Savings)**:
    - Route near-real-time internal bots (PR reviews, lint checks, vector re-indexing) to **Flex PayGo** (`~50%` discount) and large offline datasets/eval flywheels to **Batch Inference** ($\ge 50\%$ discount, direct GCS/BigQuery I/O).
3. **Deploy the 3-Stage Cascading Router**:
    - **Stage 1 (`< 1ms`)**: Rule check for slash commands/flags.
    - **Stage 2 (`~5ms`)**: Semantic Vector Router (`cosine >= 0.82`) dispatching to **Flash-Lite** (`$`), **Flash** (`$$`), or **Pro** (`$$$$`).
    - **Stage 3 (`500ms+`)**: Flash-Lite LLM disambiguation fallback + automatic self-repair escalation to **Gemini Pro** on schema/validation failure.
4. **Enforce 90% Context Caching**:
    - Structure all prompts **Static-First** (`[System Prompt + Tool Schemas + Reference Docs]` $\rightarrow$ `[Dynamic Turn]`) to get automatic **90% Implicit Caching** ($\ge 32\text{k}$ tokens), and use **Explicit `CachedContent` (`ttl="3600s"`)** for multi-user shared repositories/manuals.
