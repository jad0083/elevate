# Elevate 5-Day Agent Engineering Exam Study Guide & Master Cram Sheet

> **Rapid-Fire Exam Preparation**: Quantitative metrics, mathematical formulas, SLAs, high-probability distractor traps, and day-by-day architecture comparison matrices across all 253 curriculum notes (`Day 1` – `Day 5`).

**Quick Navigation**:
- 📝 **[55-Question Practice Knowledge Check](PRACTICE_EXAM_50Q.md)** *(Self-Test Exam + Quick Scoring Grid + Detailed Rationales)*
- 🏛️ **[Master 5-Day Technical Synthesis](MASTER_SYNTHESIS.md)** *(End-to-End Architectural Narrative)*
- 🧭 **[Google Cloud CE & DBCE Decision Playbook](CE_PLAYBOOK.md)** *(Customer Scenario Decision Matrices)*
- 💻 **[CLI & Python SDK Cheat Sheet](CLI_AND_SDK_CHEATSHEET.md)** *(Copy-Paste Commands & Code Recipes)*
- 📚 **[Repository Root](../README.md)** · **[Master Curriculum Index](../Notes/README.md)**

---

## Part 1: Master Quantitative Metrics, Thresholds, Formulas & SLAs Table

Every testable number, equation, latency target, percentage, and SLA from Days 1–5 in one scannable reference table.

| Day & Domain | Metric / Formula / Threshold | Exact Value / Equation | Architectural Meaning & Exam Context | Primary Source |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1 · Foundations** | Deterministic Rule / ML Latency Boundary | **`< 10ms`** | Sub-10ms SLAs or strict regulatory determinism require Traditional ML / Rules—not LLMs or agents. | [you_dont_always_need_agents.md](../Notes/Day_1/you_dont_always_need_agents.md) |
| **Day 1 · Multi-Agent** | Google Empirical Research Scale | **`180` configurations** | Controlled study evaluating single-agent vs. multi-agent topologies across enterprise workloads. | [more_agents_not_automatically_better.md](../Notes/Day_1/more_agents_not_automatically_better.md) |
| **Day 1 · Multi-Agent** | Agent Count Plateau | **`2–3` agents** | Marginal accuracy gains plateau beyond 2–3 agents while latency and token spend grow linearly/exponentially. | [more_agents_not_automatically_better.md](../Notes/Day_1/more_agents_not_automatically_better.md) |
| **Day 1 · Multi-Agent** | Serial Reliability Decay Formula | $\text{Accuracy}_{\text{total}} = \prod_{i=1}^N \text{Accuracy}_i$ | Four `90%`-accurate agents chained in series yield $0.9^4 = \mathbf{65.6\%}$ end-to-end reliability. | [more_agents_not_automatically_better.md](../Notes/Day_1/more_agents_not_automatically_better.md) |
| **Day 1 · Multi-Agent** | Alignment Principle Gain | **`+81%` improvement** | Decomposable, parallelizable subtasks under centralized coordination beat a single model by `+81%`. | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md) |
| **Day 1 · Multi-Agent** | Sequential Reasoning Penalty | **`-39%` to `-70%` degradation** | Splitting strict step-by-step sequential reasoning across agents degrades accuracy by `39%–70%` due to lossy handoffs fragmenting latent CoT. | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md) |
| **Day 1 · Multi-Agent** | Tool-Use Bottleneck Threshold | **`16+` tools** | At `16+` tools, multi-agent routing tax explodes; **1–2 agents with progressive-disclosure Skills/MCP** win. | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md) |
| **Day 1 · Multi-Agent** | Error Amplification (Unchecked vs. Centralized) | **`17.2×` vs. `4.4×` (`~75%` reduction)** | Independent peer meshes amplify hallucinations by `17.2×`; a centralized orchestrator enforcing **Pydantic Schema (`output_schema`)**, **Grounding Citation**, and **Policy (`after_subagent_callback`)** gates drops it to `4.4×`. | [architecture_is_a_safety_feature.md](../Notes/Day_1/architecture_is_a_safety_feature.md) |
| **Day 1 · Multi-Agent** | Max Hierarchy Depth | **`<= 3` tiers** | Keep Hierarchical Task Decomposition (Executive $\to$ Domain Lead $\to$ Worker) to $\le 3$ levels. | [hierarchical_task_decomposition_pattern.md](../Notes/Day_1/hierarchical_task_decomposition_pattern.md) |
| **Day 1 · Grounding / RAG** | Stage 1 Recall (Candidate Generation) | **`k = 100–1000` in `< 10ms`** | Hybrid BM25 + ANN (`text-embedding-004`, `768–3072` dims) on Vertex AI Vector Search (`ScaNN`). | [rag_vertex_ai_architecture_example.md](../Notes/Day_1/rag_vertex_ai_architecture_example.md) |
| **Day 1 · Grounding / RAG** | Stage 2 Precision Re-Ranking | **`k = 3–7` chunks** | Cross-encoder re-ranker narrows candidates; raw text hydrated from **Vertex AI Feature Store / Bigtable**. | [classic_information_retrieval.md](../Notes/Day_1/classic_information_retrieval.md) |
| **Day 1 · Grounding / RAG** | Optimal Chunk Size & Overlap | **`200–500` tokens (`10–20%` overlap)** | Balances semantic completeness against context dilution during RAG ingestion. | [rag_workflow_qa_system.md](../Notes/Day_1/rag_workflow_qa_system.md) |
| **Day 1 · OKF** | OKF Two Halves Attention Budget | **`~20–60` tokens** (Frontmatter) vs. **`300–3,000+` tokens** (Body) | YAML frontmatter is always scanned for fast discovery; Markdown body is lazy-loaded only on match. | [okf_file_structure_two_halves.md](../Notes/Day_1/okf_file_structure_two_halves.md) |
| **Day 1 · OKF** | Runtime Provenance Filter | `verified == true AND status == 'stable' AND current_date < stale_after` | Prevents agents from using unverified, deprecated, or expired business metric definitions (e.g., WAU). | [agent_concept_accountability.md](../Notes/Day_1/agent_concept_accountability.md) |
| **Day 1 · ADK Eval** | Rubric Anchored Scale & Golden Split | **`1–3–5` scale**; **`30% / 40% / 30%`** test mix | `1-3-5` rubric (Accuracy, Completeness, Conciseness, Empathy); Golden cases: `~30%` Single-Tool, `~40%` Context-Extraction, `~30%` Action/Trajectory. | [better_evaluation_rubric_support_chatbot.md](../Notes/Day_1/better_evaluation_rubric_support_chatbot.md), [three_kinds_of_test_cases.md](../Notes/Day_1/three_kinds_of_test_cases.md) |
| **Day 1 · ADK Eval** | Default `adk eval` CI/CD Thresholds | **`0.8` trajectory** / **`0.5` response** | `"tool_trajectory_avg_score": 0.8` catches **Lucky Hallucinations**; `"response_match_score": 0.5` avoids brittle exact-string failures. | [setting_the_bar.md](../Notes/Day_1/setting_the_bar.md) |
| **Day 1 · Deployment** | Cold Start & Billing by Target | **Agent Runtime `< 800ms`** · **Cloud Run `1.5s–4.0s` (`$0` idle)** · **GKE `0ms` pod** | Agent Runtime includes `VertexAiSessionService`; Cloud Run defaults to ephemeral RAM (`InMemorySessionService`) and **must externalize state**. | [the_other_two_axes_cold_start_and_billing.md](../Notes/Day_1/the_other_two_axes_cold_start_and_billing.md), [a_restart_must_not_erase_memory.md](../Notes/Day_1/a_restart_must_not_erase_memory.md) |
| **Day 2 · Market Share** | JetBrains AI Pulse Survey (Jan 2026) | **Copilot `29%`** · **Cursor `18%`** · **Claude Code `18%`** · **Junie `11%`** · **Antigravity `6%`** | Survey of `10,000+` devs: Copilot flatlined (59-min timeout), Claude Code surged `6×` in 8 mos, Antigravity hit `6%` in **2 months** (fastest debut). | [developer_work_adoption_ai_tools.md](../Notes/Day_2/developer_work_adoption_ai_tools.md) |
| **Day 2 · Trust Gap** | Developer Adoption vs. Trust Paradox | **`84%–90%` adoption** vs. **`29%` trust** (down from `40%`) | **`66%`** cite *"almost right, but not quite"* tax; **`81%`** security/privacy concern; **`45%`** say debugging AI code takes longer than manual coding. | [ai_adoption_universal_trust_is_not.md](../Notes/Day_2/ai_adoption_universal_trust_is_not.md), [governance_and_trust_enterprise_blocker.md](../Notes/Day_2/governance_and_trust_enterprise_blocker.md) |
| **Day 2 · Trust Gap** | High-Resistance SDLC Boundaries | **`76%` refuse Deployment/Monitoring** · **`69%` refuse Project Planning** | Enterprises require deterministic guardrails and human-in-the-loop gates to cross Stages 3 and 4 of adoption. | [how_customers_adopt_ai_tools_maturity_stages.md](../Notes/Day_2/how_customers_adopt_ai_tools_maturity_stages.md) |
| **Day 2 · Context Eng.** | The Context Equation | $\mathbf{C = P + M}$ | $C$ = Total Context, $P$ = Prompt-Visible Working Set (RAM), $M$ = External Context Universe (`PLAN.md`, OKF, Memory Bank, DBs). | [prompt_is_not_context_formula.md](../Notes/Day_2/prompt_is_not_context_formula.md) |
| **Day 2 · Context Eng.** | 4 Context Window Partitions | **System `5–10%`** · **Tools/RAG `20–30%`** · **History `20–40%`** · **Headroom `30–50%`** | Even on Gemini 3.1 (`1M–2M+` tokens), reserve **`30–50%` free headroom** to prevent reasoning degradation and Context Rot. | [what_is_context_engineering.md](../Notes/Day_2/what_is_context_engineering.md), [context_window_evolution_gemini.md](../Notes/Day_2/context_window_evolution_gemini.md) |
| **Day 2 · Skills** | 3-Level Progressive Disclosure Tokens | **L1 `~20–50`** · **L2 `~500–2,000`** · **L3 `0` baseline tokens** | L1 (`WHEN`: YAML frontmatter) $\to$ L2 (`HOW`: `SKILL.md` body) $\to$ L3 (`WHAT`: `scripts/`, `references/`, `assets/`). Keep global skills to **`5–15`**. | [progressive_disclosure_when_how_what.md](../Notes/Day_2/progressive_disclosure_when_how_what.md), [skills_reusable_just_in_time_context.md](../Notes/Day_2/skills_reusable_just_in_time_context.md) |
| **Day 2 · Context Eng.** | Observation Flooding CLI Cap | **`-max_results=50`** | Enforce driver-level pagination and quiet flags so raw shell/DB dumps never flood working memory $P$. | [context_collapse_and_observation_flooding.md](../Notes/Day_2/context_collapse_and_observation_flooding.md) |
| **Day 2 · MCP** | Virtual MCP Toolsets Token Reduction | **`1k–4k` tokens/turn** vs. **`30k–80k+` tokens/turn** | Partitioning a 100-tool MCP server into domain-scoped virtual endpoints (`.../toolsets/bigquery_sql_readonly`) slashes per-turn schema overhead by `~95%`. | [toolsets_protect_the_context_window.md](../Notes/Day_2/toolsets_protect_the_context_window.md) |
| **Day 2 · MCP** | Connector Complexity Formula | $O(N \times M) \longrightarrow O(N + M)$ (**`88%` reduction** at $10 \times 50$) | $10$ agent surfaces $\times 50$ tools drops from `500` bespoke point-to-point connectors to `60` standardized JSON-RPC 2.0 integrations. | [nxm_problem_custom_connectors.md](../Notes/Day_2/nxm_problem_custom_connectors.md) |
| **Day 2 · MCP Catalog** | Managed Google MCP Tool Counts | **BigQuery (`5`)** · **Maps Grounding Lite (`3`)** · **GKE (`8`)** | BigQuery (`list_dataset_ids`, `list_table_ids`, `get_dataset_info`, `get_table_info`, `execute_sql`); Maps (`search_places`, `compute_routes`, `lookup_weather`). | [example_mcp_for_bigquery.md](../Notes/Day_2/example_mcp_for_bigquery.md), [mcp_servers_gce_gke_maps_catalog.md](../Notes/Day_2/mcp_servers_gce_gke_maps_catalog.md) |
| **Day 2 · Modernization** | AlloyDB vs. Cloud SQL Performance & SLA | **AlloyDB: `4×` OLTP, `100×` Analytical, `99.99%` SLA** vs. **Cloud SQL: `99.95%` SLA** | AlloyDB SLA includes maintenance; pair with Serverless DMS CDC + Gemini AI `PL/SQL` & `T-SQL` $\to$ `PL/pgSQL` conversion. | [database_modernization_dms_alloydb_cloudsql.md](../Notes/Day_2/database_modernization_dms_alloydb_cloudsql.md) |
| **Day 2 · Modernization** | .NET & App Modernization Accelerators | **`< 2 Month` .NET Acceleration** · **`3–7 Week` Accelerator** · **`7-Tab` CodMod Report** | Phase 1: `3-week` assessment (`3–10` apps); Phase 2: `2–4 week` pilot co-engineering (`3` prerequisites), funded by **RaMP** & **PSF**. | [accelerate_dotnet_modernization_google_cloud_ai.md](../Notes/Day_2/accelerate_dotnet_modernization_google_cloud_ai.md), [application_modernization_accelerator_program.md](../Notes/Day_2/application_modernization_accelerator_program.md) |
| **Day 2 · Identity** | Pure WIF Constraints in Gemini Enterprise | **`6` hard limitations** (resolved by **`WIF + SCIM`**) | Pure WIF lacks sharing autocomplete, NotebookLM sharing, group licensing, Workspace sources, GCS links, and **cannot migrate to Cloud Identity**. | [wif_for_gemini_enterprise.md](../Notes/Day_2/wif_for_gemini_enterprise.md) |
| **Day 3 · Threat Intel** | Offensive AI Multipliers | **`10×` faster recon** · **`85%` CVE PoC coverage** · **`~0` human oversight** | Recon shrinks from weeks to hours; LLMs auto-synthesize working PoC exploits from CVE diffs for `85%` of known vulnerabilities. | [how_ai_scales_attacks_by_the_numbers.md](../Notes/Day_3/how_ai_scales_attacks_by_the_numbers.md) |
| **Day 3 · Secure SDLC** | 4 Continuous SDLC Security Signals | **`< 1s` IDE** · **`< 2m` CI/CD** · **`< 5s` Runtime** · **`< 5m` Patch PR** | IDE AST autocomplete (`<1s`), Cloud Build/Critique gate (`<2m`), Wiz Defend/Model Armor (`<5s`), Eventarc + CodeMender PR (`<5m`). | [machinespeed_defense_in_practice.md](../Notes/Day_3/machinespeed_defense_in_practice.md) |
| **Day 3 · Shift-Right** | HITL Configurable Autonomy Tiers | **Tier 1 `>= 95%`** · **Tier 2 `80%–94%`** · **Tier 3 `< 80%`** | Tier 1: autonomous kill/revoke/block; Tier 2: CodeMender PR + **1-click human approval**; Tier 3: context enrichment + human analyst triage. | [shift_right_realities_runtime_defense.md](../Notes/Day_3/shift_right_realities_runtime_defense.md) |
| **Day 3 · Wiz AI DAST** | 5-Phase Attack Surface Funnel | **`24,402` $\to$ `1,147` (`-95.3%`) $\to$ `452` (`-60.6%`) $\to$ `233` (`-48.5%`) $\to$ `123` Paths** | **`99.5%` total noise reduction**: `425` portal screenshots, `827` tech stacks, `92` AI Red Agent DAST simulations, **`87` Critical** paths (**`89` Red Agent verified**). | [wiz_attack_surface_assessment_stages_console.md](../Notes/Day_3/wiz_attack_surface_assessment_stages_console.md) |
| **Day 3 · CodeMender** | Sandbox PoC False-Positive Elimination | **`100%` false-positive elimination** (`14` CVEs avoided in WizOS image example) | Executes a tailored exploit PoC against AST coordinates in an isolated sandbox container before opening a unit-test-verified PR. | [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md), [ai_threat_defense_agentic_security_operating_model.md](../Notes/Day_3/ai_threat_defense_agentic_security_operating_model.md) |
| **Day 4 · Harness Eng.** | Fundamental Harness Equation | $\mathbf{\text{Agent} = \text{Model} + \text{Harness}}$ | Coined by Mitchell Hashimoto (Feb 2026) / formalized by Vivek Trivedy (Mar 2026) for multi-hour/multi-day autonomous execution. | [what_is_a_harness_agent_equals_model_plus_harness.md](../Notes/Day_4/what_is_a_harness_agent_equals_model_plus_harness.md) |
| **Day 4 · ADK 2.0** | 6 Lifecycle Callbacks Latency Budgets | **Agent `<1–2ms`** · **Model `5–15ms` / `<1ms`** · **Tool `<2–5ms`** | `before_model_callback` (`5–15ms`) runs Cloud DLP SSN/CC scrubbing & Model Armor; `before_tool_callback` (`<2ms`) enforces Dual-Gate RBAC. | [adk_concepts_callbacks_lifecycle_hooks.md](../Notes/Day_4/adk_concepts_callbacks_lifecycle_hooks.md) |
| **Day 4 · Memory Bank** | Session & Memory Bank Latencies | **`< 10ms` session** (`<1 KB` payload) · **`< 5ms` `CreateSessions`** · **`15–30ms` `PreloadMemoryTool`** | `FirestoreSessionService` keeps last `10` turns verbatim (`>10` summarized); `StateGraph` nodes isolate context to **`< 1K` tokens** (vs. `40K+` stacking). | [scenario_1_multiturn_conversation_continuity_state_persistence.md](../Notes/Day_4/scenario_1_multiturn_conversation_continuity_state_persistence.md), [adk_framework_code_example_preload_memory_tools.md](../Notes/Day_4/adk_framework_code_example_preload_memory_tools.md) |
| **Day 4 · Identity** | SPIFFE Dual-Gate Permission Formula | $\text{Effective Permission} = \min(\text{User Permissions}, \text{Agent Permissions})$ | Combines Human OAuth/OIDC token + workload X.509 SPIFFE SVID (`spiffe://...`, sub-hour rotation) to eliminate Confused Deputy attacks. | [agent_platform_runtime_master_architecture.md](../Notes/Day_4/agent_platform_runtime_master_architecture.md) |
| **Day 4 · Evaluation** | Dimension 1 (Intent Satisfaction) Weights | **`35%` Explicit** ($\ge 95\%$) · **`30%` Latent Spec** ($\ge 85\%$) · **`20%` Pivots** ($\ge 90\%$) · **`15%` Convergence** ($\le 5$ turns) | Scored by `gemini-2.5-pro` LLM-as-a-Judge using session-prefix rubric generation, calibrated by **`5%–10%` Human Review**. | [eval_dimension_1_intent_satisfaction.md](../Notes/Day_4/eval_dimension_1_intent_satisfaction.md) |
| **Day 4 · Evaluation** | Dimension 7 Test-File Immutability Gate | **`0.0` automatic score** on any test diff (`<= 2` repair turns target) | Prevents reward hacking (deleting `assert`s or modifying `tests/`). Any mutation to test files immediately fails the evaluation with `0.0`. | [eval_dimension_7_self_repair_behaviour.md](../Notes/Day_4/eval_dimension_7_self_repair_behaviour.md) |
| **Day 4 · Evaluation** | Method 8 Biased Online Sampling | **`>= 4` user corrections**, **high-cost**, and **abandoned sessions** | Production online eval uses **biased sampling** over failure indicators rather than flat `1%` uniform random sampling. | [eval_methods_deep_dive_tooling_playbook.md](../Notes/Day_4/eval_methods_deep_dive_tooling_playbook.md) |
| **Day 4 · DB & Vector** | Vector Database p99 Latencies & Scale | **Vertex AI `ScaNN` `< 5ms`** (Billions) · **AlloyDB/Cloud SQL/Spanner `5–25ms`** (Millions, ACID) · **BigQuery `IVF`/`TreeAH` `200ms–3s`** (PBs) | Pair with **Google MCP Toolbox for Databases (`go/mcp-toolbox`)** requiring **`< 10` lines** of ADK Python code (`McpToolboxClient`). | [vector_database_design_options_tradeoffs.md](../Notes/Day_4/vector_database_design_options_tradeoffs.md), [mcp_toolbox_for_databases_overview.md](../Notes/Day_4/mcp_toolbox_for_databases_overview.md) |
| **Day 5 · Model Serving** | Provisioned Throughput (PT) & Discounts | **PT `80%–85%` target utilization** · **Flex PayGo `~50%` off** · **Batch `>= 50%` off** | Size PT to `80–85%` on minute-level telemetry with burst spillover to Standard/Priority PayGo; route non-interactive jobs to Flex or Batch. | [foundation_model_consumption_options.md](../Notes/Day_5/foundation_model_consumption_options.md), [choosing_the_right_consumption_option.md](../Notes/Day_5/choosing_the_right_consumption_option.md) |
| **Day 5 · Caching** | Implicit vs. Explicit Context Caching | **`90%` discount** (`75%` Gemini 2.0 Explicit) · **`>= 32k` min tokens** · **`60-min` (`3600s`) TTL** | Implicit caching is enabled by default (requires **Static-First Prompt Ordering**); Explicit `CachedContent` guarantees a 60-min TTL SLA. | [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md) |
| **Day 5 · Routing** | 3-Stage Cascading Router & TTFT | **Stage 1 Rule `< 1ms` (`$0`)** $\to$ **Stage 2 Vector `~5ms` (`cosine >= 0.82`)** $\to$ **Stage 3 LLM `500ms+`** | Dispatches across **Flash-Lite (`100–200ms`, `$`)**, **Flash (`200–400ms`, `$$`)**, and **Pro (`800ms–1.5s`, `$$$$`)** with Pro self-repair fallback. | [routing_patterns_rule_llm_semantic.md](../Notes/Day_5/routing_patterns_rule_llm_semantic.md), [model_routing_semantic_router_tiers.md](../Notes/Day_5/model_routing_semantic_router_tiers.md) |

---

## Part 2: Top 25 High-Probability "Exam Trap" Distractors vs. Ground Truth

Watch out for these 25 realistic multiple-choice distractors designed to test whether you mastered the engineering principles vs. surface intuition.

| # | Common Exam Trap / Plausible Distractor ❌ | Verified Curriculum Ground Truth ✅ | Source Note |
| :---: | :--- | :--- | :--- |
| **1** | *"Adding more specialized subagents to a sequential chain improves accuracy by letting each agent focus on one reasoning step."* | **False.** Splitting strict sequential reasoning across multiple agents degrades accuracy by **39%–70%** (Sequential Penalty) because lossy text handoffs fragment latent Chain-of-Thought. Keep tightly coupled sequential reasoning in **one frontier model**. | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md) |
| **2** | *"When an agent requires 25+ tools, split them across a 6-agent peer-to-peer mesh to reduce per-agent complexity."* | **False.** At **16+ tools**, multi-agent routing overhead explodes (Tool-Use Bottleneck), and unchecked peer meshes amplify errors by **17.2×**. Use **1–2 agents** with **Progressive Disclosure Skills** and **Virtual MCP Toolsets** (`1k–4k` tokens) under a centralized orchestrator (`4.4×`). | [multi_agent_wins_and_loses.md](../Notes/Day_1/multi_agent_wins_and_loses.md), [architecture_is_a_safety_feature.md](../Notes/Day_1/architecture_is_a_safety_feature.md) |
| **3** | *"Full fine-tuning on enterprise documents is the best way to prevent hallucinations on private company facts."* | **False.** Fine-tuning teaches **form/style, not dynamic factual recall**—it is static, expensive, lacks ACL enforcement, and still hallucinates. Use **2-Stage RAG** + **Open Knowledge Format (OKF)** with closed-book prompt templates. | [naive_grounding_solutions.md](../Notes/Day_1/naive_grounding_solutions.md) |
| **4** | *"Giving an SQL agent full DDL schemas and `INFORMATION_SCHEMA` access is sufficient to answer business metric questions like WAU."* | **False.** Schemas lack institutional semantics (e.g., excluding `is_internal_account = TRUE`, bots, and `'page_view'` noise). Pair database tools with a git-native **OKF bundle** filtered by `verified == true AND status == 'stable' AND current_date < stale_after`. | [agent_does_not_know_your_business.md](../Notes/Day_1/agent_does_not_know_your_business.md), [okf_bundle_example_wau.md](../Notes/Day_1/okf_bundle_example_wau.md) |
| **5** | *"If an agent's final response matches the Golden Dataset answer (`response_match_score >= 0.9`), the evaluation should pass."* | **False.** Grading only final output misses **Lucky Hallucinations** (guessing the right text without invoking `check_inventory` or `process_refund`). Always gate CI/CD on **both** `tool_trajectory_avg_score >= 0.8` and `response_match_score >= 0.5`. | [trajectory_vs_response.md](../Notes/Day_1/trajectory_vs_response.md), [setting_the_bar.md](../Notes/Day_1/setting_the_bar.md) |
| **6** | *"Deploying an ADK agent to Cloud Run with default settings automatically persists multi-turn user conversations across days."* | **False.** Default `InMemorySessionService` stores state in container RAM; when Cloud Run scales to zero, **all memory is erased**. Pass `--agent_engine_id` (`VertexAiSessionService`) or configure `FirestoreSessionService` / Cloud SQL / AlloyDB. | [a_restart_must_not_erase_memory.md](../Notes/Day_1/a_restart_must_not_erase_memory.md), [where_state_lives.md](../Notes/Day_1/where_state_lives.md) |
| **7** | *"Google Cloud CEs can screen-share JetSki on Cloudtop during customer demos or instruct customers to download the standalone Antigravity IDE."* | **Double Hard Violation.** (1) **JetSki** is strictly internal (`google3`/dogfood models)—never screen-share with customers. (2) Standalone **Antigravity IDE** is a consumer app lacking GCP ToS/HIPAA/SOC2 and blocks `@google.com`/Workspace logins. Use **Antigravity IDE Extensions**, **`agy` CLI**, or **Antigravity 2.0 Hub** on **Argolis**. | [antigravity_vs_jetski_ce_guidelines.md](../Notes/Day_1/antigravity_vs_jetski_ce_guidelines.md), [dont_use_antigravity_ide.md](../Notes/Day_2/dont_use_antigravity_ide.md) |
| **8** | *"With Gemini 3.1's 2M-token context window, you should preload all 200 corporate skills and 100 MCP tools into the global system prompt."* | **False.** Every skill frontmatter costs `~20–50` tokens and every MCP tool schema costs `300–800` tokens (`30k–80k` for 100 tools), causing attention dilution and lost headroom (`30–50%`). Keep global skills to **5–15**, use project-scoped skills, and partition MCP servers into **Virtual MCP Toolsets** (`1k–4k` tokens). | [context_window_evolution_gemini.md](../Notes/Day_2/context_window_evolution_gemini.md), [toolsets_protect_the_context_window.md](../Notes/Day_2/toolsets_protect_the_context_window.md) |
| **9** | *"To prevent Observation Flooding when a chat transcript grows long, summarize the entire conversation into a single paragraph every 5 turns."* | **False.** Aggressive lossy summarization causes **Context Collapse**—erasing exact UUIDs, file paths, and error codes (*"the agent had it before summarizing, and fails after"*). Instead, **WRITE** structured state to `PLAN.md`, cap CLI outputs (`-max_results=50`), and **ISOLATE** noisy exploration in **Subagents**. | [context_collapse_and_observation_flooding.md](../Notes/Day_2/context_collapse_and_observation_flooding.md), [subagents_context_isolation.md](../Notes/Day_2/subagents_context_isolation.md) |
| **10** | *"A high-fidelity `SPEC.md` should include exact Python for-loops and helper function implementations so the agent doesn't make mistakes."* | **False.** Writing pseudocode/implementation details in `SPEC.md` is the **Over-Prescriptive Micromanagement** anti-pattern. Target the **Declarative Goldilocks Zone** across the 6 pillars: Measurable Outcomes, Scope Boundaries, Invariants, Prior Decisions, Data Contracts, and Verification Criteria. | [anatomy_of_high_fidelity_specs.md](../Notes/Day_2/anatomy_of_high_fidelity_specs.md), [critical_anti_patterns_prescriptive_vs_ambiguity.md](../Notes/Day_2/critical_anti_patterns_prescriptive_vs_ambiguity.md) |
| **11** | *"The fastest way to modernize a COBOL mainframe is automated line-by-line transpilation of COBOL into Java classes."* | **False.** Line-by-line transpilation produces unmaintainable **"JOBOL"**. Use the 4-stage AI lifecycle: **MAT** extracts natural-language business rules $\to$ **Mainframe Agents + Gemini 3.1** author `SPEC.md` & idiomatic Java 21/Go microservices $\to$ **Google Dual Run** certifies byte-for-byte parity via live traffic shadowing. | [end_to_end_ai_powered_mainframe_modernization.md](../Notes/Day_2/end_to_end_ai_powered_mainframe_modernization.md), [mainframe_agentic_rewrite_loop.md](../Notes/Day_2/mainframe_agentic_rewrite_loop.md) |
| **12** | *"Customers using Okta or Microsoft Entra ID for SSO must deploy Workforce Identity Federation (WIF) to use Gemini Enterprise."* | **False.** **Google Cloud Identity** natively supports 3rd-party SAML 2.0 / OIDC SSO with Okta, Entra ID, and Ping while preserving **100% Day-1 Gemini Enterprise feature parity**. Only use WIF when regulations forbid directory sync—and always deploy **WIF + SCIM** (never pure WIF). | [third_party_idp_sso_with_cloud_identity.md](../Notes/Day_2/third_party_idp_sso_with_cloud_identity.md), [wif_for_gemini_enterprise.md](../Notes/Day_2/wif_for_gemini_enterprise.md) |
| **13** | *"To connect Gemini Enterprise to multiple Google Workspace domains after an M&A, switch the Google Auth Platform OAuth app type from Internal to External."* | **False.** Switching to `External` triggers mandatory CASA security audits and scary unverified-app consent screens. Keep the OAuth app set to **`Internal`** and submit a **Backend Engineering Cross-Domain Allowlist Request** mapping the subsidiary Workspace domains. | [cloud_identity_multiple_google_workspace.md](../Notes/Day_2/cloud_identity_multiple_google_workspace.md) |
| **14** | *"Granting an IAM Allow role with a condition is the most reliable way to block an agent from invoking mutating MCP tools across a GCP project."* | **False.** IAM Allow bindings are additive—another broad role (`roles/editor`) will bypass the condition. Use a **Cloud IAM Deny Policy** with the CEL condition `api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false`, which overrides all Allow grants. | [mcp_iam_deny_fine_grained_controls.md](../Notes/Day_2/mcp_iam_deny_fine_grained_controls.md) |
| **15** | *"Shift-Left security gates should block every developer commit to run a full 20-minute SAST audit report."* | **False.** Blocking audits cause alert fatigue and dev-sec friction. Shift-Left must feel like **"autocomplete, not an audit"** (`< 1 sec` inline IDE AST fixes via 1-click `Tab`/`Enter`), paired with `< 2 min` CI/CD gating and `< 5 sec` Shift-Right runtime defense. | [shift_left_developer_experience_autocomplete_not_audit.md](../Notes/Day_3/shift_left_developer_experience_autocomplete_not_audit.md), [machinespeed_defense_in_practice.md](../Notes/Day_3/machinespeed_defense_in_practice.md) |
| **16** | *"When a runtime sensor detects a potential anomaly with 85% confidence, the autonomous defense system should immediately merge a source code patch to production."* | **False.** At **80%–94% confidence (Tier 2)**, **CodeMender** autonomously generates the AST patch and runs sandbox unit tests, but gates merge on **1-click human approval**. Only **Tier 1 ($\ge 95\%$ confidence)** executes immediate autonomous containment (process kill, token revocation, IP block). | [shift_right_realities_runtime_defense.md](../Notes/Day_3/shift_right_realities_runtime_defense.md) |
| **17** | *"Adopting CodeMender requires replacing existing Snyk, Veracode, or Checkmarx scanners with Wiz Code."* | **False.** CodeMender follows **"Augment, Don't Rip-and-Replace"**—ingesting SARIF/JSON/XML from Wiz, Snyk, Veracode, Checkmarx, and SonarQube (`cm import --file ...`) and running an isolated **sandbox PoC exploit** to eliminate **100% of false positives** before opening a PR. | [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md) |
| **18** | *"In ADK 2.0, scrubbing SSNs and credit card numbers from user prompts should be implemented inside `before_agent_callback` or `before_tool_callback`."* | **False.** `before_agent_callback` runs once at turn start for JWT/entitlement checks, and `before_tool_callback` guards downstream tool execution. PII redaction (Cloud DLP) and Model Armor prompt sanitization belong in **`before_model_callback`** (`5–15ms`), intercepting the exact payload right before every Gemini API call. | [adk_concepts_callbacks_lifecycle_hooks.md](../Notes/Day_4/adk_concepts_callbacks_lifecycle_hooks.md), [scenario_3_enterprise_guardrails_pii_redaction_auditing.md](../Notes/Day_4/scenario_3_enterprise_guardrails_pii_redaction_auditing.md) |
| **19** | *"A2A (Agent-to-Agent Protocol) is Google's replacement for Anthropic's Model Context Protocol (MCP)."* | **False.** A2A and MCP are **complementary**: **MCP is the vertical downward bus** connecting an agent to deterministic tools/resources (`/tools`, `go/mcp-toolbox`), while **A2A is the horizontal outward bus** federating stateful tasks across opaque black-box peer agents (`/.well-known/agent.json`, `/v1/a2a/tasks`). | [a2a_vs_mcp_coexistence_architecture.md](../Notes/Day_4/a2a_vs_mcp_coexistence_architecture.md) |
| **20** | *"If an agent's SPIFFE identity has `roles/bigquery.admin`, any authenticated user chatting with the agent can run administrative BigQuery queries."* | **False.** That is a **Confused Deputy** vulnerability. The Agent Platform Runtime enforces **Dual-Gate Authorization**: $\text{Effective Permission} = \min(\text{User Permissions}, \text{Agent Permissions})$. Both the user's OAuth token and the agent's SPIFFE SVID must independently hold permission. | [agent_platform_runtime_master_architecture.md](../Notes/Day_4/agent_platform_runtime_master_architecture.md) |
| **21** | *"During self-repair evaluation (Dimension 7), if an agent updates an outdated unit assertion in `tests/test_api.py` so the test suite passes, it receives partial credit."* | **False.** The **Test-File Immutability Gate** treats `tests/`, `*.spec.ts`, and `test_*.py` as cryptographically read-only. Any modification, deletion, or relaxation of a test file triggers an **automatic `0.0` score**. | [eval_dimension_7_self_repair_behaviour.md](../Notes/Day_4/eval_dimension_7_self_repair_behaviour.md) |
| **22** | *"For production online evaluation (Method 8), sample a uniform random 1% of all live agent sessions to get an unbiased quality metric."* | **False.** Since `~95%` of routine production turns succeed, uniform 1% sampling wastes LLM-judge compute on trivial turns. Use a **Biased Sampling Strategy** over-indexing on **high-cost sessions**, **`>= 4` user corrections**, and **abandoned sessions**. | [eval_methods_deep_dive_tooling_playbook.md](../Notes/Day_4/eval_methods_deep_dive_tooling_playbook.md) |
| **23** | *"BigQuery Vector Search (`VECTOR_SEARCH()` with IVF/TreeAH) is the recommended choice for a customer-facing voice agent requiring `< 10ms` p99 vector retrieval."* | **False.** BigQuery Vector Search has a **`200ms–3s` p99 latency** designed for analytical batch RAG and petabyte SQL joins. Use **Vertex AI Vector Search (`ScaNN`)** for **`< 5ms` p99** at billion-vector scale, or **AlloyDB `ScaNN` / Cloud SQL `pgvector` / Spanner** for **`5ms–25ms` p99** with transactional ACID filtering. | [vector_database_design_options_tradeoffs.md](../Notes/Day_4/vector_database_design_options_tradeoffs.md) |
| **24** | *"To avoid paying for idle capacity, provision Vertex AI Provisioned Throughput (PT) to cover 100% of your highest possible annual traffic spike."* | **False.** Sizing PT for rare peaks leaves expensive reserved PTUs idle most of the year. Right-size PT to **`80%–85%` baseline utilization** using minute-by-minute telemetry, and configure automatic burst spillover to **Standard PayGo** or **Priority PayGo**. | [choosing_the_right_consumption_option.md](../Notes/Day_5/choosing_the_right_consumption_option.md) |
| **25** | *"Placing the current timestamp and user ID at the very top of your system prompt has no impact on Gemini Implicit Context Caching."* | **False.** Implicit Context Caching (`90%` discount on prefixes $\ge 32\text{k}$ tokens) relies on an exact **left-to-right prefix matcher**. Dynamic variables at line 1 invalidate the entire downstream KV-cache every turn. Enforce **Static-First Prompt Ordering**: `[System Instructions + Tool Schemas + Reference Docs]` $\to$ `[Dynamic Turn Context]`. | [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md) |

---

## Part 3: Day-by-Day Exam Cram & Architecture Comparison Matrices (Days 1–5)

### 📅 Day 1 Cram: Foundations, Grounding/RAG, OKF, ADK 4 Pillars, Multi-Agent & Cloud Deployment
Full Index: [Notes/Day_1/README.md](../Notes/Day_1/README.md) (`106` Topic Notes)

#### 1. The 5-Stage Evolution & Architecture Selection Matrix
Sources: [ai_agents_an_evolution.md](../Notes/Day_1/ai_agents_an_evolution.md), [you_dont_always_need_agents.md](../Notes/Day_1/you_dont_always_need_agents.md), [sdk_vs_adk.md](../Notes/Day_1/sdk_vs_adk.md)

| Stage / Option | Execution Pattern | When to Choose | When NOT to Choose |
| :--- | :--- | :--- | :--- |
| **0. Traditional ML / Rules** | Deterministic math / decision trees | `< 10ms` latency SLAs, credit/fraud scoring, strict regulatory repeatability | Open-ended natural language or dynamic multi-step planning |
| **1. Raw LLM (`google-genai` SDK)** | `Prompt -> Text` (parametric weights) | Single-turn translation, summarization, classification, tone rewrite | Facts after training cutoff or external system mutations |
| **2. LLM + 2-Stage RAG** | `Query -> ScaNN Recall (k=100–1000) -> Cross-Encoder Re-Rank (k=3–7) -> Closed-Book Prompt` | Read-only Q&A over private enterprise docs with citation grounding | Multi-step workflows requiring dynamic API calls or state mutation |
| **3. LLM + RAG + Tools** | Single-step function call | Fixed one-shot lookups (e.g., check weather or single DB status) | Ambiguous goals requiring iterative self-correction |
| **4. Autonomous Agent (`google.adk`)** | Closed-loop **ReAct** (`Think -> Act -> Observe -> Iterate`) | Multi-step reasoning where the path depends on runtime tool observations | Simple deterministic pipelines (use `SequentialAgent` or code) |
| **5. Multi-Agent System** | Coordinator / Parallel / Loop / `StateGraph` | Parallelizable subtasks (`+81%` gain) or strict security/context boundaries | Tightly coupled sequential reasoning (`-39% to -70%` penalty) or `16+` tools in a flat mesh |

#### 2. Multi-Agent Workflow vs. Dynamic Topologies (`google.adk`)
Sources: [multi_agent_design_patterns.md](../Notes/Day_1/multi_agent_design_patterns.md), [adk_workflow_patterns_sequential_parallel_hierarchical.md](../Notes/Day_1/adk_workflow_patterns_sequential_parallel_hierarchical.md), [adk_multi_agent_systems.md](../Notes/Day_1/adk_multi_agent_systems.md)

- **Deterministic Workflow Agents (0 LLM routing overhead)**:
    - `SequentialAgent(sub_agents=[a, b, c])`: Fixed pipeline; passes structured values via `output_key` in `session.state`.
    - `ParallelAgent(sub_agents=[a, b, c])`: Concurrent fan-out (`asyncio.gather`) writing to distinct keys in `session.state` (+81% alignment sweet spot).
    - `LoopAgent(sub_agents=[...], max_iterations=N)`: Iterative cycle with mandatory `max_iterations` circuit breaker; powers **Review & Critique** (Generator + Critic) and **Iterative Refinement** (Generator $\to$ Quality Evaluator $\to$ Prompt Enhancer).
- **Dynamic AI-Routed Topologies**:
    - **Coordinator (`LlmAgent`)**: Hub-and-spoke router matching user intent against child agent `description` fields; acts as the **Centralized Validation Bottleneck (`4.4×` vs `17.2×`)** enforcing Pydantic `output_schema`, Grounding, and `after_subagent_callback`.
    - **Hierarchical Task Decomposition**: Executive Coordinator $\to$ Domain Leads $\to$ Leaf Workers (keep depth $\le 3$).
    - **Swarm**: Peer-to-peer handoff mesh via `transfer_to_<agent>` tools, guarded by `max_handoffs`.

#### 3. Rules vs. Workflows vs. Skills & JetSki vs. Antigravity Compliance
Sources: [when_to_use_which_rules_workflows_skills.md](../Notes/Day_1/when_to_use_which_rules_workflows_skills.md), [antigravity_config_context_primitives.md](../Notes/Day_1/antigravity_config_context_primitives.md), [antigravity_vs_jetski_ce_guidelines.md](../Notes/Day_1/antigravity_vs_jetski_ce_guidelines.md), [jetski_to_antigravity_naming_map.md](../Notes/Day_1/jetski_to_antigravity_naming_map.md)

| Primitive / Surface | Trigger Mechanism | Scope & Purpose | Customer Demo / Compliance Rule |
| :--- | :--- | :--- | :--- |
| **Rules** (`.gemini/rules/`, `AGENTS.md`) | **Always-On** (injected every session) | Global/repo coding standards, architecture invariants, read-before-edit | Safe when scoped to customer/Argolis repo |
| **Workflows** (`/slash` commands) | **User-Triggered** | Repeatable multi-step macros (`/goal`, `/plan`, `/grill-me`, `/learn`) | Safe on Antigravity 2.0 / `agy` |
| **Skills** (`SKILL.md` + `scripts/`) | **Agent-Triggered** (3-tier progressive disclosure) | On-demand domain expertise (L1 `~20–50` $\to$ L2 `~500–2k` $\to$ L3 `0` tokens) | Share external skills via **GTM GitHub** (`go/ce-customer-code-sharing`) |
| **Runtime Hooks** (`pre-tool-call`, `post-edit`) | **Deterministic System Event** (outside LLM control) | Hard shell gates (linters, secret scanners, test runners) | Cannot be bypassed by prompt injection |
| **Antigravity 2.0 / `agy` CLI / Extensions** | External Enterprise Product (`Jetski Hub`/`CLI` equivalent) | Customer-facing agentic IDE extensions, CLI, Hub, and SDK | ✅ **APPROVED FOR CUSTOMER DEMOS** (use clean **Argolis** profile) |
| **JetSki (Cloudtop) / Cider** | Internal Google3 Dogfood Environment | Connected to Piper/CitC, `google3`, Critique, Buganizer, Moma | ❌ **STRICTLY INTERNAL — NEVER SCREEN-SHARE WITH CUSTOMERS** |

---

### 📅 Day 2 Cram: Antigravity 2.0, Context Engineering ($C=P+M$), SDD, Modernization & Governed MCP
Full Index: [Notes/Day_2/README.md](../Notes/Day_2/README.md) (`87` Topic Notes)

#### 1. The 5 Functional Skill Archetypes & SDD 4-File Matrix
Sources: [skill_patterns_5_archetypes.md](../Notes/Day_2/skill_patterns_5_archetypes.md), [four_files_four_audiences.md](../Notes/Day_2/four_files_four_audiences.md), [agent_is_computer_system_analogy.md](../Notes/Day_2/agent_is_computer_system_analogy.md)

- **5 Skill Archetypes**:
    1. **Informational**: Passive domain/repo conventions (`g3doc_documentation`).
    2. **Tool Wrapper**: Binary paths, flags, and `-max_results=50` output capping (`analog`, `blaze`, `buganizer_cli`).
    3. **Generator**: Boilerplate templates, negative constraints, and validator scripts (`scripts/validate_hcl.py`), built via **"Experience Before Theory"** (`skill_creator`, `autoprovisioner`).
    4. **Reviewer**: Rubrics (`EVAL.txtpb`) and severity tags (`[BLOCKER]`, `[SUGGESTION]`, `[NIT]`) (`skill_readability`).
    5. **Workflow**: Multi-step sequential runbooks with fail-fast prerequisite checks (`aclcheck`) and checkpoints (`whitefly`).
- **Four Files, Four Audiences (SDD Matrix)**:
    - `README.md` $\to$ Audience: **Humans** | Scope: **The Project** | Lifetime: **Permanent**
    - `AGENTS.md` $\to$ Audience: **Agents** | Scope: **The Repo** | Lifetime: **Persistent across all tasks**
    - `SPEC.md` $\to$ Audience: **Human & Agent** | Scope: **One Change** | Lifetime: **Feature-scoped (ephemeral)**
    - `SKILL.md` $\to$ Audience: **Agents** | Scope: **One Capability** | Lifetime: **Reusable across repos**
- **Von Neumann Computer Analogy**: LLM $\leftrightarrow$ **CPU** · Context Window ($P$) $\leftrightarrow$ **RAM/Cache** · External Memory ($M$) $\leftrightarrow$ **Disk/Storage** · Tools $\leftrightarrow$ **I/O Peripherals** · MCP Schemas $\leftrightarrow$ **Syscalls/Drivers** · Tests (`verify.py`) $\leftrightarrow$ **Hardware Interrupts**.

#### 2. Enterprise Application & Database Modernization Matrix
Sources: [end_to_end_ai_powered_mainframe_modernization.md](../Notes/Day_2/end_to_end_ai_powered_mainframe_modernization.md), [windows_modernization_how_it_works.md](../Notes/Day_2/windows_modernization_how_it_works.md), [database_modernization_dms_alloydb_cloudsql.md](../Notes/Day_2/database_modernization_dms_alloydb_cloudsql.md)

| Modernization Track | Discovery & Assessment Tool | AI Transformation Engine | Testing, Parity & Target Runtime |
| :--- | :--- | :--- | :--- |
| **Mainframe (COBOL / PL/I / JCL / CICS)** | **Mainframe Assessment Tool (MAT)** (extracts call graphs + natural-language business rules) | **Mainframe Agents + Gemini 3.1** (`Business Rules -> SPEC.md -> Idiomatic Java 21 / Go`; zero "JOBOL") | **Google Dual Run** (`Dualize -> Execute -> Compare -> Certify` byte-for-byte live traffic shadowing) + **Mainframe Connector / DMS** (EBCDIC/VSAM $\to$ BQ/Spanner/AlloyDB) |
| **Windows / .NET Framework** | **CodMod Advisor** in **Modernize Hub** (**7-Tab Report** from `.sln`/`.csproj`/`Web.config`) | **Gemini CLI + .NET Skills**: WCF/SOAP $\to$ gRPC/Minimal API; WebForms $\to$ .NET 8 API + Blazor/SPA; EF6 $\to$ EF Core 8; Registry $\to$ Secret Manager | **.NET 8 on Linux Containers** (Cloud Run / GKE) via **`< 2 Month` Acceleration** or **`3–7 Week` Accelerator** (RaMP / PSF funded) |
| **Legacy DBs (Oracle / SQL Server)** | **Database Migration Assessment (DMA)** | **Serverless DMS Continuous CDC** (Oracle LogMiner / MSSQL CDC) + **Gemini AI `PL/SQL` & `T-SQL` $\to$ `PL/pgSQL`** | **AlloyDB for PostgreSQL** (`4×` OLTP, `100×` Analytical Columnar, `99.99%` SLA) or **Cloud SQL for PostgreSQL** (`99.95%` SLA) |

#### 3. Governed MCP, Enterprise Identity & Wiz AI-APP
Sources: [what_an_mcp_server_exposes.md](../Notes/Day_2/what_an_mcp_server_exposes.md), [mcp_authorization_controls_iam.md](../Notes/Day_2/mcp_authorization_controls_iam.md), [mcp_iam_deny_fine_grained_controls.md](../Notes/Day_2/mcp_iam_deny_fine_grained_controls.md), [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md), [wif_for_gemini_enterprise.md](../Notes/Day_2/wif_for_gemini_enterprise.md), [wiz_red_agent_ai_pentesting_exploit_chain.md](../Notes/Day_2/wiz_red_agent_ai_pentesting_exploit_chain.md)

- **3 MCP Primitives**: (1) **Tools** (`tools/list`, `tools/call` — model-controlled actions), (2) **Prompts** (`prompts/list`, `prompts/get` — user/server templates), (3) **Resources** (`resources/list`, `resources/read` — app-controlled read-only URI context streams).
- **4-Layer MCP Security Stack**:
    1. **Dual-Layer Cloud IAM**: Gate 1 checks `roles/mcp.toolUser` at the MCP Gateway; Gate 2 checks downstream service IAM (`roles/bigquery.dataViewer`) using delegated caller identity.
    2. **Cloud IAM Deny + CEL**: `api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false` (`--kind=denypolicies`) overrides all Allow grants to enforce read-only mode.
    3. **Google Model Armor Floor Settings**: `gcloud model-armor floorsettings update --mcp-sanitization=ENABLED --malicious-uri-filter-settings-enforcement=ENABLED --pi-and-jailbreak-filter-settings-enforcement=ENABLED --pi-and-jailbreak-filter-settings-confidence-level=MEDIUM_AND_ABOVE`.
    4. **Wiz AI-APP & Red Agent**: Unites **Wiz Code** (repo/MCP scan), **Wiz Cloud** (AI-BOM, toxic combinations), and **Wiz Defend** (runtime sensors) across **4 console stages** (*Visibility $\to$ Posture $\to$ Risk $\to$ Threat Detection*). Counteracts the **5-step Wiz Red Agent Exploit Chain** (`401` probe $\to$ dummy `Bearer` token bypass $\to$ `post_chat_message` Confused Deputy injection $\to$ over-privileged SA DB query $\to$ PII/Stripe key exfiltration).

---

### 📅 Day 3 Cram: Machine-Speed Threat Defense, Wiz 5-Phase Funnel & CodeMender
Full Index: [Notes/Day_3/README.md](../Notes/Day_3/README.md) (`24` Topic Notes)

#### 1. Threat Actors, 4 Attack Pillars & The 4-Stage Google + Wiz Readiness Lifecycle
Sources: [autonomous_threat_actors_machine_scale.md](../Notes/Day_3/autonomous_threat_actors_machine_scale.md), [ai_mechanisms_in_vulnerability_discovery.md](../Notes/Day_3/ai_mechanisms_in_vulnerability_discovery.md), [case_studies_ai_in_adversarial_use.md](../Notes/Day_3/case_studies_ai_in_adversarial_use.md), [ai_threat_defense_google_and_wiz_lifecycle.md](../Notes/Day_3/ai_threat_defense_google_and_wiz_lifecycle.md), [ai_threat_defense_agentic_security_operating_model.md](../Notes/Day_3/ai_threat_defense_agentic_security_operating_model.md)

- **Documented State-Sponsored Tradecraft**:
    - **Chinese State Actors (Claude Code)**: Multi-file binary/source taint analysis across massive context windows to synthesize zero-day exploits in minutes (countered by **CodeMender** AST patching).
    - **Russian Threat Groups (Gemini CLI)**: Automated network/API/DNS recon, hyper-personalized spear-phishing, and dynamic in-flight shellcode re-encoding (countered by **Model Armor** + **Wiz Defend**).
- **4 Attack Pillars of AI Vulnerability Discovery**: (1) *Continuous Untiring Scanning* (24/7 BGP/DNS/Cert logs), (2) *Semantic Code Understanding* (cross-file AST taint analysis), (3) *Zero-Day Discovery at Scale* (protocol-aware gRPC/Protobuf/JSON-RPC fuzzing), (4) *Adaptive Evasion Loops*.
- **4-Stage Google & Wiz Readiness Lifecycle (Living Architecture Graph + Mandiant Threat Intel)**:
    1. **01. Prepare — Autonomous Red Agent**: Continuous AI DAST penetration testing across On-Prem, Multi-Cloud, and SaaS/Repos.
    2. **02. Remediate — CodeMender & Wiz Code Green Agent**: Traces runtime exposure to exact AST line and `git blame` owner, opening sandbox-verified PRs.
    3. **03. Prevent — Wiz Atlas & Pre-Commit Guardrails**: Inline IDE base-image swaps (e.g., `Dockerfile` swap to WizOS avoiding 14 CVEs), Model Armor, Binary Authorization.
    4. **04. Monitor — Autonomous Defender / SOC Agent**: 4-Layer cross-stack investigation (*Application $\to$ Data & Access $\to$ Model & Guardrails $\to$ Infrastructure*) feeding Google SecOps / Chronicle.

#### 2. Wiz 5-Phase AI DAST Funnel & CodeMender (`cm`) Workflow
Sources: [wiz_attack_surface_assessment_stages_console.md](../Notes/Day_3/wiz_attack_surface_assessment_stages_console.md), [codemender_wiz_integration_architecture.md](../Notes/Day_3/codemender_wiz_integration_architecture.md), [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md)

```text
[Stage 1: Discovery]             24,402 Scan Candidates (22,627 cloud workloads, 902 OSINT, 355 APIs, 12 repos)
       │ (-95.3% filtered)
       ▼
[Stage 2: Ingress Validation]     1,147 Routable Internet-Facing Endpoints (425 live portal screenshots)
       │ (-60.6% filtered)
       ▼
[Stage 3: Fingerprinting]           452 Fingerprinted Endpoints across 827 Tech Stacks (153 VPN/SSH/RDP, 80 WAFs)
       │ (-48.5% filtered)
       ▼
[Stage 4: External Risk Scan]       233 Externally Validated Findings (92 AI Red Agent DAST + 2 Secrets Blast Radius)
       │ (Graph Toxic-Combo Scoring -> 99.5% total noise reduction)
       ▼
[Stage 5: Prioritized Paths]        123 Validated Attack Paths (87 Critical · 25 High · 11 Medium | 89 Red Agent Verified)
```

- **CodeMender (`cm`) 2-Step CLI & Universal Scanner Ingestion**:
    - Ingests **Wiz Code**, **Snyk**, **Veracode**, **Checkmarx**, **SonarQube**, and **SARIF**: `cm import --file findings_wiz.json` (provisions isolated sandbox container and executes exploit PoC $\to$ **100% false-positive elimination**).
    - Synthesizes differential AST patch, runs unit test suite in sandbox, and opens PR: `cm fix --id CVE-2026-4011 --create-pr`.

---

### 📅 Day 4 Cram: ADK 2.0 `StateGraph`, 6 Callbacks, Memory Bank, A2A, SPIFFE & 7×8 Evaluation
Full Index: [Notes/Day_4/README.md](../Notes/Day_4/README.md) (`31` Topic Notes)

#### 1. ADK 2.0 Runtime, 4-Tier Scoped State & 6 Lifecycle Callbacks
Sources: [adk_2_paradigm_shift_graph_execution_engine.md](../Notes/Day_4/adk_2_paradigm_shift_graph_execution_engine.md), [google_adk_architecture_runner_session_state_context.md](../Notes/Day_4/google_adk_architecture_runner_session_state_context.md), [adk_concepts_callbacks_lifecycle_hooks.md](../Notes/Day_4/adk_concepts_callbacks_lifecycle_hooks.md), [scenario_3_enterprise_guardrails_pii_redaction_auditing.md](../Notes/Day_4/scenario_3_enterprise_guardrails_pii_redaction_auditing.md)

- **4-Tier Scoped State (`Session.state`)**:
    1. `session` (default, no prefix): Current conversation thread; discarded on close (`state["cart_items"]`).
    2. `user:`: Persistent across all sessions for a specific `user_id` (`state["user:preferred_language"]`).
    3. `app:`: Global cluster-wide state shared across all users/sessions (`state["app:maintenance_mode"]`).
    4. `temp:`: Ephemeral single-turn scratchpad purged immediately at turn end (`state["temp:raw_sql_draft"]`).
- **The 6 Lifecycle Callbacks Across 3 Execution Boundaries**:

| Boundary | Before Hook (Pre-Execution Gate) | After Hook (Post-Execution Audit/Transform) |
| :--- | :--- | :--- |
| **1. Agent Boundary** (`InvocationContext`) | `before_agent_callback` (`<1ms`): JWT validation, tenant entitlement check, early cache hit return | `after_agent_callback` (`<2ms`): Compliance disclaimers, tamper-proof **Cloud Audit Logs**, OTEL span close |
| **2. Model Boundary** (`InvocationContext`, `contents`) | `before_model_callback` (`5–15ms`): **Cloud DLP** SSN/credit-card redaction & **Model Armor** prompt injection check *before* Gemini API | `after_model_callback` (`<1ms`): Token billing metering, Pydantic schema check, retry trigger |
| **3. Tool Boundary** (`ToolContext`, `tool_name`, `tool_args`) | `before_tool_callback` (`<2ms`): **Dual-Gate IAM RBAC** (e.g., block `execute_sql_delete` without `roles/database.admin`), SQLi sanitization, HITL modal | `after_tool_callback` (`<5ms`): Truncate 50 MB DB payloads, scrub internal secrets from tool output |

#### 2. Cognitive Memory Hierarchy, A2A vs. MCP & ADK 2.0 vs. LangGraph
Sources: [agent_memory_hierarchy_episodic_semantic_procedural.md](../Notes/Day_4/agent_memory_hierarchy_episodic_semantic_procedural.md), [a2a_vs_mcp_coexistence_architecture.md](../Notes/Day_4/a2a_vs_mcp_coexistence_architecture.md), [a2a_component_breakdown_client_server_cards_messages_artifacts.md](../Notes/Day_4/a2a_component_breakdown_client_server_cards_messages_artifacts.md), [adk_2_vs_langgraph_competitive_architecture_matrix.md](../Notes/Day_4/adk_2_vs_langgraph_competitive_architecture_matrix.md)

- **Cognitive Memory Hierarchy**:
    - **Short-Term Working Memory**: In-context window, `temp:*` state, `InvocationContext` (RAM / Memorystore).
    - **Long-Term Memory (3 Subsystems)**: (1) **Episodic** (past interactions/trajectories $\to$ **Vertex AI MemoryBank / Firestore**), (2) **Semantic** (domain facts/concepts $\to$ **Vertex AI Vector Search / AlloyDB `pgvector` / Spanner Graph / OKF**), (3) **Procedural** (how-to skills/workflows $\to$ **`SKILL.md` / `StateGraph` / Git**).
    - **Vertex AI Memory Bank Dual Channels**: *Channel A* runs async background Gemini LROs to extract/merge facts over time (with UUID `delete_memory` for GDPR); *Channel B* exposes synchronous `memory_service.as_tool()` (`20–40ms`), while `PreloadMemoryTool()` hydrates preferences at turn start (`15–30ms`).
- **A2A (Horizontal) vs. MCP (Vertical) & The 5 A2A Primitives**:
    - **MCP (Vertical Downward Bus)**: Stateless JSON-RPC calls from an agent downward to deterministic `/tools` and `/resources` (one-sided reasoning).
    - **A2A (Horizontal Lateral Bus)**: Stateful task delegation outward to opaque **Black-Box Peer Agents** (dual-sided reasoning).
    - **5 Core A2A Primitives**: (1) `A2A Client`, (2) `A2A Server` (`PENDING`, `RUNNING`, `INTERRUPTED`, `COMPLETED`, `A2A_INTERRUPT_REQUIRED`), (3) `Agent Card` at `https://DOMAIN/.well-known/agent.json` (with `supports_authenticated_extended_card=True`), (4) `A2A Message` (`POST /v1/a2a/tasks/{id}/turns` + SSE), (5) `A2A Artifacts` (`GET /v1/a2a/tasks/{id}/artifacts`).
- **Google ADK 2.0 vs. LangGraph (5 Competitive Pillars)**: (1) Unified end-to-end lifecycle (`agents-cli` build/eval/deploy/monitor) vs. stitching LangChain + paid LangSmith + LangServe; (2) 1-click deploy to Agent Runtime/Cloud Run/GKE with WIF & VPC-SC; (3) First-class Coordinator/Swarm/Hierarchy + `StateGraph`; (4) Built-in `agents-cli eval`; (5) Native BigQuery Agent Analytics, SPIFFE Identity, and MCP Toolbox.

#### 3. The 7 Evaluation Dimensions, 8 Methodologies & `agents-cli` 7 Commands / 7 Skills
Sources: [agent_eval_seven_dimensions_framework.md](../Notes/Day_4/agent_eval_seven_dimensions_framework.md), [how_to_evaluate_eight_methods.md](../Notes/Day_4/how_to_evaluate_eight_methods.md), [agents_cli_core_commands_reference.md](../Notes/Day_4/agents_cli_core_commands_reference.md), [agents_cli_7_bundled_skills_suite.md](../Notes/Day_4/agents_cli_7_bundled_skills_suite.md)

- **3 Unique Challenges of Evaluating Vibe Coding**: (1) **Underspecification Gap** (must reconstruct latent spec), (2) **Validation Asymmetry** (UI looks right while hiding SQLi/bugs), (3) **Iterative Sessions as State** (Turn 1 debt compounds by Turn 7).
- **7 Evaluation Dimensions**:
    - *Outside-In (User-Facing 1–4)*: **1. Intent Satisfaction** (`35%` Explicit Ask, `30%` Latent Spec, `20%` Dynamic Pivots, `15%` Convergence), **2. Functional Correctness** (sandboxed tests), **3. Visual & Behavioural Fidelity** (Playwright + Gemini 2.5 Pro Vision), **4. Cost & Efficiency** (tokens, latency, turns).
    - *Inside-Out (Internal 5–7)*: **5. Code Quality & Conventions** (Ruff/ESLint + LLM style judge), **6. Trajectory Quality** (OTEL trace replay preventing **Fragile Success**), **7. Self-Repair Behaviour** (**Test-File Immutability Gate** = `0.0` score on any test edit; $\le 2$ repair turns).
    - *Transversal*: **Safety & Responsible AI** (OWASP/CWE vulnerabilities, zero leaked secrets, IP/license compliance, jailbreak refusal).
- **8 Evaluation Methodologies**: (1) Standardised Benchmarks (`SWE-bench Verified`, `Vibe Code Bench`, `LiveCodeBench`), (2) Automated Functional Testing (`pytest`/`jest`), (3) Security & Safety (`Snyk`, `Semgrep`, `git-secrets`, `Model Armor`), (4) LLM/Agent-as-a-Judge (`gemini-2.5-pro`), (5) Browser Testing (`Playwright`), (6) Trajectory Inspection (`OTEL` replay), (7) Human Review (`5–10%` calibration sample), (8) Online Production Eval (**Biased Sampling**: high-cost, $\ge 4$ corrections, abandoned sessions).
- **`agents-cli` 7 Core Commands & 7 Bundled Skills**:
    - *7 Commands*: `setup` (`--ide antigravity --inject-skills`) $\to$ `scaffold` (`--template chat|workflow|rag|adk|adk_a2a|agentic_rag`) $\to$ `run` (`--interactive --verbose-tools`) $\to$ `eval run` (`--dataset ... --judge-model gemini-2.5-pro`) $\to$ `infra single-project` (Terraform IaC) $\to$ `deploy` (`--target agent-runtime|cloud-run|gke`) $\to$ `publish gemini-enterprise`.
    - *7 Bundled Skills (`google-agents-cli-*`)*: `workflow`, `adk-code`, `scaffold`, `eval`, `deploy`, `publish`, `observability`.

---

### 📅 Day 5 Cram: 5 Vertex AI Consumption Tiers, Context Caching & 3-Stage Semantic Router
Full Index: [Notes/Day_5/README.md](../Notes/Day_5/README.md) (`5` Topic Notes)

#### 1. The 5 Vertex AI Consumption Tiers & Hybrid Spillover Architecture
Sources: [foundation_model_consumption_options.md](../Notes/Day_5/foundation_model_consumption_options.md), [choosing_the_right_consumption_option.md](../Notes/Day_5/choosing_the_right_consumption_option.md)

| Consumption Tier | Billing & Discount | SLA & Latency Profile | Ideal Workload & Sizing Rule |
| :--- | :--- | :--- | :--- |
| **1. Provisioned Throughput (PT)** | Fixed commitment (reserved PTUs) | **Deterministic sub-second SLA**; zero peak throttling | Steady-state interactive production agents; right-size to **`80%–85%` baseline utilization** on minute-level telemetry |
| **2. Standard PayGo** *(Default)* | Standard per-token | Fast interactive; Shared Region SLA | Everyday dev/staging, spiky traffic, and **automatic burst spillover** above PT baseline |
| **3. Priority PayGo** | Premium per-token | Preferential cluster queue; elevated burst RPM/TPM | VIP/executive workflows, flash sales, and high-priority PT burst spillover without fixed commitment |
| **4. Flex PayGo** | **`~50%` discount** per-token | Best-effort / queued on spare TPU capacity | Latency-tolerant near-real-time internal agents: PR reviewers, lint bots, overnight refactors, vector re-indexing |
| **5. Batch Inference** | **`>= 50%` discount** per-token | Async (hours, Job Completion SLA); no HTTP timeouts | Massive offline backlogs via direct **GCS / BigQuery** JSONL I/O and synthetic evaluation flywheels |

#### 2. Implicit vs. Explicit Gemini Context Caching (`90%` Savings)
Source: [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md)

| Dimension | Implicit Context Caching | Explicit Context Caching (`CachedContent` API) |
| :--- | :--- | :--- |
| **Activation** | **Zero setup (Enabled by default)** | Programmatic via `client.cached_contents.create(...)` |
| **Token Discount** | **`90%` discount** on matching prefixes | **`90%` discount on Gemini 2.5+** (`75%` on Gemini 2.0) |
| **Minimum Size & TTL** | Typically **`>= 32k` tokens**; best-effort rolling window | Typically **`>= 32k` tokens**; **`60-minute` (`ttl="3600s"`) guaranteed SLA** (updatable) |
| **Wire Payload** | Sends full prompt; reuses server KV-cache on prefix hit | Uploads corpus once; subsequent calls pass only `cached_content=cache.name` |
| **Mandatory Rule** | Enforce **Static-First Prompt Ordering** (`[System + Tools + Docs]` $\to$ `[Dynamic Turn]`) + temporal clustering | Ideal for multi-user portals querying shared large repositories or manuals across independent sessions |

#### 3. The 3-Stage Cascading Hybrid Model Router
Sources: [model_routing_semantic_router_tiers.md](../Notes/Day_5/model_routing_semantic_router_tiers.md), [routing_patterns_rule_llm_semantic.md](../Notes/Day_5/routing_patterns_rule_llm_semantic.md)

```text
Incoming Query ──► [Stage 1: Rule Filter (<1ms, $0)] ──(Match: /plan, /eval, flag)──► Direct Tier Dispatch
                         │ (No Rule Match)
                         ▼
                   [Stage 2: Semantic Vector Router (~5ms, ~$0)]
                         ├──► Cosine Similarity >= 0.82 ──► Dispatch to Matched Tier:
                         │      • Tier 1: Gemini Flash-Lite (~100–200ms TTFT, $)    [Classification, JSON extraction, PII tagging]
                         │      • Tier 2: Gemini Flash      (~200–400ms TTFT, $$)   [Multi-turn chat, RAG synthesis, fast tool loops]
                         │      • Tier 3: Gemini Pro        (~800ms–1.5s TTFT, $$$$)[Complex reasoning, multi-file code, architecture]
                         │
                         └──► Cosine Similarity < 0.82 (Ambiguous)
                                │
                                ▼
                   [Stage 3: LLM Disambiguation Fallback (500ms–1.2s, $$)]
                         └──► Gemini Flash-Lite Classifier routes query
                                │
                                ▼
                   [Post-Dispatch Validation Gate] ──(Schema Failure / Low Confidence)──► Escalate to Gemini Pro
```
