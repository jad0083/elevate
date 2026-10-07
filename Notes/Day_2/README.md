# Elevate — Day 2: Google Antigravity & Developer Surfaces

## Overview

Day 2 focuses on **Google Antigravity**, its unified agent harness co-optimized with Gemini, its developer surfaces across CLI, IDE extensions, visual hubs, and custom SDK applications within the broader **Gemini Enterprise** ecosystem, and **Enterprise Application Modernization** across Mainframe, Windows/.NET, Java, and Databases.

---

## Day 2 Session Notes

### 1. Antigravity Architecture & Surfaces
* [Google Antigravity: One Agent Harness, Many Surfaces](antigravity_one_harness_many_surfaces.md): Overview of Antigravity 2.0, CLI, IDE Extensions, and SDK unified on the Gemini-optimized harness and Gemini Enterprise platform.
* [Google Antigravity Surfaces: Antigravity 2.0, IDE Extensions & CLI](antigravity_surfaces_deepdive_2_0_ide_cli.md): Deep dive into Antigravity 2.0 visual hub, IDE companion extensions (VS Code, IntelliJ, Xcode, Visual Studio), and terminal CLI (`agy`).
* [Policy & Compliance: Don't Use Antigravity IDE](dont_use_antigravity_ide.md): Incompatibility of standalone consumer IDE with Google Cloud ToS and why IDE Extensions must be used instead.
* [Developer Work Adoption: Market Share & The Rise of Agentic Coding](developer_work_adoption_ai_tools.md): JetBrains Jan 2026 empirical benchmark (Copilot 29% flatlined, Cursor 18%, Claude Code 18%, JetBrains 11%, Antigravity 6% in 2 months).
* [The AI Coding Market in Three Lanes: Commercial, Open-Source & Antigravity](ai_coding_market_in_three_lanes.md): Taxonomic breakdown of Lane 1 Commercial Agents (Copilot, Cursor, Claude Code), Lane 2 Open-Source Terminal (Aider, Cline, Neovim), and Lane 3 Google Antigravity Agent Platform.
* [Commercial AI Coding Players: Capabilities & Competitive Dynamics](commercial_ai_coding_players_capabilities.md): Comparative analysis of GitHub Copilot (Incumbent), Cursor (Fast Mover), Claude Code (Terminal Agent), and OpenAI Codex (Multi-Surface Agent) vs. Google Antigravity.
* [Specialized AI Coding Players on the Radar: Windsurf, Junie & Cody](ai_coding_also_on_the_radar.md): Analysis of Windsurf (FedRAMP High/Cascade), JetBrains Junie (IDE debugger/AST), and Sourcegraph Cody (Monorepo code search context) alongside Google Antigravity positioning.
* [Open-Source & Terminal Workflows: The Invisible AI Adoption Layer](opensource_and_terminal_workflows.md): Open-source agent runtimes (Aider, Cline, Goose, OpenHands) and terminal/Vim compositions (Neovim, CodeCompanion.nvim, ripgrep, fzf, tmux) bridged by Antigravity CLI.

### 2. Skills Architecture & Progressive Disclosure
* [Skill Architecture: The Canonical Definition & Progressive Disclosure](skill_definition_progressive_disclosure.md): The foundational breakdown of instructions, metadata, resources, and tier-by-tier context optimization.
* [Skill Specification: The `SKILL.md` File Structure & Anatomy](skill_md_structure.md): YAML frontmatter metadata rules, trigger formula conventions, and Markdown instruction formatting.
* [Skill Architecture: Directory Structure & File Roles](what_are_skills_directory_structure.md): Mandatory `SKILL.md` root manifest vs. optional on-disk executables (`scripts/`), references (`references/`), and templates (`assets/`).
* [Context Economics: The 3 Levels of Progressive Disclosure (When, How, What)](progressive_disclosure_when_how_what.md): Level 1 When (YAML frontmatter), Level 2 How (`SKILL.md` body), and Level 3 What (`references/`, `assets/`, `scripts/`).
* [Skill Design Patterns: The 5 Functional Archetypes](skill_patterns_5_archetypes.md): Writing use-case tailored skills across Informational, Tool Wrapper, Generator, Reviewer, and Workflow patterns.
* [Skill Pattern Deep Dive: Informational Skills](informational_skills_pattern.md): Providing agents with background context, repository conventions, and environment grounding (e.g. `g3doc_documentation`).
* [Skill Pattern Deep Dive: Tool Wrapper Skills](tool_wrapper_skills_pattern.md): Instructing agents on CLI executables, binary paths, output filtering, and task recipes (e.g. `analog`, `blaze`, `buganizer_cli`).
* [Skill Pattern Deep Dive: Generator Skills](generator_skills_pattern.md): Guiding structured artifact creation, "Experience Before Theory", templates, and validation scripts (e.g. `skill_creator`, `autoprovisioner`).
* [Skill Pattern Deep Dive: Reviewer Skills](reviewer_skills_pattern.md): Equipping agents with assessment rubrics, procedural inspection steps, and severity tagging (e.g. `skill_readability`, `cc_readability`).
* [Skill Pattern Deep Dive: Workflow Skills](workflow_skills_pattern.md): Guiding agents through multi-step procedures, ACL prerequisite checks, and conditional branching (e.g. `whitefly`).
* [Skills: A System for Reusable "Just in Time" Context](skills_reusable_just_in_time_context.md): Bridging model capability gaps, JIT hydration, "Accumulate with caution" governance, and standard Google skills (`python-readability`, `create-cl`, `colab`, `skill-creator`, `evaluating-skills`).

### 3. Authoring & Deploying Antigravity Skills
* [Authoring Antigravity Skills: Complete 4-Step Integration Guide](authoring_antigravity_skills.md): Global scope (`~/.gemini/config/skills/`) vs. project workspace scope (`.gemini/skills/`), cloning templates, packaging, and verifying active status.
* [Discovering Skills: The Agent Marketplace & Governance Ecosystem](discover_skills_agent_marketplace.md): Centralized registry, live & offline eval scores (`SCORE 97`), seamless toggling, and verified team ownership.
* [Customer Engineering Agent Ecosystem: CE Tech Skills & Marketplace Integration](ce_tech_skills_marketplace.md): Official CE skills suite (`/skill ce-tech`, `/skill ce-tech-concord-conversational-agent`, `/skill ce-tech-sales-agent`) published by Cloud Customer Engineering.
* [Authoring & Deploying Experimental Skills in Google3](experimental_skills_google3.md): Creating personal sandbox skills under `google3/experimental/users/<ldap>/skills/`, Agent Market discovery, and Jetski/Antigravity execution.

### 4. Software Engineering Rigor & Anti-Patterns
* [The AI Trust Gap: Universal Adoption vs. Low Output Confidence](ai_adoption_universal_trust_is_not.md): Benchmark data (84% dev adoption vs 29% trust, 66% "almost right" tax) and the market opening for strong engineering governance.
* [The 4 Stages of AI Tool Adoption: From Search to Autonomous Automation](how_customers_adopt_ai_tools_maturity_stages.md): The enterprise maturity curve (Stage 1 Search/Learn, Stage 2 Write/Fix, Stage 3 Orchestrate, Stage 4 Automate) and overcoming deployment/planning resistance.
* [Governance & Trust: The Enterprise Blocker & The 9-Point Checklist](governance_and_trust_enterprise_blocker.md): Developer concerns (81% security, 45% debug tax, 29% accuracy) and the 9-point enterprise governance framework mapping to Google Cloud & Antigravity.
* [Beyond "Vibe Coding": The 3 Fatal Pathologies of Unstructured Agentic Coding](beyond_vibe_coding.md): The collapse of conversational vibe coding and how engineering rigor prevents Context Rot (`history_edu`), PR Slop (`code_off`), and Architectural Drift (`account_tree`).
* [The Power of Rules & Directives: Same Model, Same Task (`AGENTS.md`)](same_model_same_task_agents_md.md): Empirical comparison of raw vibe prompting (hallucinated fail) vs. `AGENTS.md` guided execution (read-before-edit, local verification, clean pass).
* [The First Law of Agent Engineering: The Model Is Not the Variable You Control — The Context Is](the_model_is_not_the_variable_you_control.md): The foundational paradigm shift from passenger model-tweaking to disciplined context engineering (Invariants, Progressive Disclosure, OKF, MCP).
* [Context Engineering: Dynamic Information Assembly & Token Budgeting](what_is_context_engineering.md): Canonical definition, the 4 context window partitions (System Prompt, Tools/Context, History, Headroom), and dynamic assembly vs. monolithic stuffing.
* [The Context Window Revolution: From Capacity Limits to Value-Density Curation](context_window_evolution_gemini.md): Gemini 3.1 1M–2M+ token horizons, why capacity is no longer the constraint, and why curation governs reasoning fidelity.
* [Architectural Evolution: Legacy Prompt Engineering vs. Modern Context Engineering](prompt_engineering_vs_context_engineering.md): Paradigm comparison across focus, retrieval methods, input streams (BigQuery/multimodal), and Google Cloud scalability.
* [Working Memory Taxonomy: The Three Levels of Context](three_levels_of_context.md): Persistent (System instructions / AI physics), Semi-Persistent (Memory Bank / episodic state), and Transient (Dynamic data / Agent Search).
* [The 4 Core Principles of Context Engineering: Write, Select, Compress, Isolate](four_principles_of_context_engineering.md): Externalizing state to disk (`PLAN.md`), JIT retrieval, history compaction, and subagent boundary isolation.
* [The Context Equation: Prompt Is Not Context ($C = P + M$)](prompt_is_not_context_formula.md): Mathematical breakdown of total context ($C$), prompt working set ($P$), and external universe ($M$).
* [Systems Architecture: An Agent Is a Computer System](agent_is_computer_system_analogy.md): The Von Neumann analog mapping LLM $\leftrightarrow$ CPU, Context $\leftrightarrow$ RAM, Memory $\leftrightarrow$ Storage, Tools $\leftrightarrow$ Peripherals, Schemas $\leftrightarrow$ Syscalls, and Tests $\leftrightarrow$ Interrupts.
* [Dual Hazards of Context Management: Context Collapse vs. Observation Flooding](context_collapse_and_observation_flooding.md): The perils of lossy over-summarization vs. unconstrained shell outputs and stack trace flooding.
* [Affordance RAG: Tool & Skill Descriptions Are Context Too](tool_descriptions_are_context_too.md): Managing tool definitions as token-consuming working memory, affordance indexing, and remembering capabilities without holding full manuals.
* [Subagent Architecture: Context Isolation & Clean Delegation](subagents_context_isolation.md): The shock absorber pattern absorbing messy exploration (file dumps, stack traces, dead ends) to keep parent reasoning pristine.
* [Specification-Driven Development: The Spec Is the Primary Artifact of Software Engineering](specification_is_the_primary_artifact.md): The paradigm shift where declarative specifications (`SPEC.md` / `PLAN.md`) outlive code, and agents act as compilers.
* [SDLC Transformation: The Document-as-Context Evolution](document_as_context_evolution.md): Mapping the 6 SDLC phases to version-controlled Markdown instruction files and native Antigravity support features.
* [Specification Matrix: Four Files, Four Audiences](four_files_four_audiences.md): Breakdown of `README.md` (Human/Project), `AGENTS.md` (Agent/Repo), `SPEC.md` (Human+Agent/Change), and `SKILL.md` (Agents/Capability).
* [Specification Engineering: The Anatomy of High-Fidelity Specs](anatomy_of_high_fidelity_specs.md): The 6 core pillars (Measurable Outcomes, Scope Boundaries, Invariants, Prior Decisions, Data Contracts, Verification Criteria).
* [Specification Anti-Patterns: Prescriptive Detail vs. Ambiguity](critical_anti_patterns_prescriptive_vs_ambiguity.md): Avoiding micromanagement (`error_outline`) and hand-waving ambiguity (`help_outline`) by targeting the Declarative Goldilocks Zone.

### 5. Enterprise Strategy & Modernization
* [Enterprise Strategy: Why an Agentic AI Future Requires Modernization Now](why_agentic_ai_requires_modernization_now.md): The convergent strategy linking AI, cloud migration, and legacy modernization to unlock enterprise data context.
* [Enterprise Workload Tracks: Agentic Enterprise Application Modernization](agentic_enterprise_application_modernization.md): De-risking modernization across 5 technical tracks (Infrastructure, Mainframe, Windows/.NET, Java, Databases) and 4 horizontal stages (Assessments, Transformation, Data, Testing).
* [Google Cloud as the Best Hyperscaler for "Full-Stack AI" Modernization](best_hyperscaler_full_stack_ai.md): Google's 5-layer vertical AI stack (Silicon, Research, Models, Products, Partners) and dedicated modernization suites (Mainframe, .NET/Java, Databases).
* [Google Cloud Modernize Hub: Unified Application Transformation Console](google_cloud_modernize_hub_preview.md): Console-native hub for tooling discovery, automated portfolio assessments, and guided transformation companions (.NET, Mainframe, Java).
* [Enterprise Mainframe Modernization: End-to-End AI-Powered Architecture](end_to_end_ai_powered_mainframe_modernization.md): The 4-stage lifecycle (Assessment via MAT, Modernize via Gemini CLI/Agents, Test via Dual Run, Data Migration via Connector/DMS).
* [Mainframe Modernization: The Agentic Rewrite & Convergence Loop](mainframe_agentic_rewrite_loop.md): Bidirectional rewrite lifecycle from COBOL source $\rightarrow$ Natural Language Business Rules $\rightarrow$ PRD/Specs $\rightarrow$ Java/Go Code $\rightarrow$ Dual Run Parity Convergence.
* [Google Dual Run: Production Traffic Shadowing & Zero-Risk Migration Certification](de_risk_with_dual_run.md): Patented zero-risk technology that dualizes live production mainframe traffic, compares outputs byte-for-byte, and certifies modernized applications.
* [Enterprise Windows Modernization: .NET Modernization with Gemini](dotnet_modernization_gemini_solutions.md): Ingesting legacy .NET/WCF/ASPX code with CodMod and autonomously refactoring to .NET 8 on Linux containers using Gemini CLI and Agent Skills.
* [Google Cloud App Modernization CLI: Windows, .NET & MSSQL Code Assessment](windows_dotnet_mssql_modernization_cli.md): Ingesting raw source code and context to produce interactive assessment reports mapping code evidence to Google Cloud solutions.
* [Database Modernization: Google Cloud DMS, AlloyDB & Cloud SQL with Gemini](database_modernization_dms_alloydb_cloudsql.md): Heterogeneous database migration from Oracle and MSSQL to AlloyDB and Cloud SQL using serverless DMS CDC replication and Gemini AI stored procedure conversion.
* [Agentic Modernization: Google Antigravity as the Unified Enterprise Orchestrator](agentic_modernization_with_google_ai.md): Uniting application refactoring (Assessment, Conversion, Retrospective) and database modernization (DMA & DMS) via Antigravity.
* [Customer Acceleration: .NET Modernization Engagement Model & Funding Programs](accelerate_dotnet_modernization_google_cloud_ai.md): The <2 month engagement model combining estate assessment, pilot app refactoring, Modernize Hub, and Google funding (RaMP, PSF).
* [Customer Execution: Application Modernization Accelerator Program](application_modernization_accelerator_program.md): The 3-phase engagement framework (3-Week Assessment, 2-4 Week Pilot Co-Engineering & Pre-Prod Deploy, Ongoing Estate Scale).
* [Google Cloud CodMod: Windows Application Modernization Advisor](windows_modernization_codmod_advisor.md): Ingesting Windows source code (.sln, .csproj) and user context to generate structured assessment reports and task backlogs.
* [Windows Modernization: Technical Architecture & Migration Mechanisms](windows_modernization_how_it_works.md): Detailed mechanics for converting SOAP/WCF, ASP.NET MVC, WebForms (ASPX), EF6, and Registry keys into .NET 8 on Linux.

### 6. AI Agent Core Architecture & Runtime Systems
* [AI Agents: The Next Frontier of Software & The Four Key Components](ai_agents_next_frontier_four_components.md): Decomposing agent architecture into Models, Tools, Orchestration (Agent Brain), and Runtime execution substrates.
* [The $N \times M$ Integration Problem: Tool Fragmentation vs. Standardized Protocols (MCP)](nxm_problem_custom_connectors.md): Why point-to-point custom connectors create an $O(N \times M)$ maintenance collapse and how MCP standardizes integrations to $O(N + M)$.
* [Model Context Protocol (MCP): Client-Server Architecture & Standardized Tool Execution](model_context_protocol_client_server_architecture.md): Decoupling agents (`MCPClient`) from tool servers (`MCPServer`) with declarative JSON discovery and standardized execution.
* [Model Context Protocol (MCP) Topology: Three Components, One Protocol](mcp_three_components_one_protocol.md): The canonical 3-tier topology mapping the MCP Host (Antigravity/CLI), MCP Clients (1:1 sessions), and MCP Servers (BigQuery, GitHub, Local files) over JSON-RPC.
* [The 3 Core Primitives of MCP: Tools, Prompts, and Resources](what_an_mcp_server_exposes.md): Detailed mechanics of `tools/list` (active actions), `prompts/list` (server templates), and `resources/list` (passive context streams).
* [Model Context Protocol: Local vs. Remote Servers](mcp_local_vs_remote_servers.md): Architectural trade-offs between local on-device `stdio` subprocesses (rapid prototyping, privacy) and remote cloud-hosted `SSE` services (centralized IAM, audit logging, fleet scaling).
* [Google Managed MCP Servers: Enterprise Cloud Ecosystem & Apigee Integration](google_managed_mcp_servers.md): Managed MCP infrastructure for Google 1P / Google Cloud ecosystems and Apigee-powered automated API transformation.
* [Google MCP Servers: The Unified, Fully Managed Platform for Google Cloud](google_mcp_servers_unified_platform.md): The 3-tier runtime connecting Agents, Apps, and IDEs backed by Discoverability, Authentication, Admin Governance, Content Security, and Observability.
* [Google MCP Servers: Value Propositions across Agent Builders, Security Admins & Service Owners](google_mcp_servers_value_propositions.md): Tailored enterprise benefits for developers (JIT discovery, tracing), SecOps (IAM RBAC, audit logs, DLP), and service teams (zero-code MCP tool exposure).
* [Key Capabilities & Security Architecture for Google MCP Servers](key_capabilities_google_mcp_servers.md): The 6-pillar framework covering Managed MCP, Endpoints Directory, OAuth 2.1, VPC-SC Governance, Google Model Armor, and OTel Distributed Tracing.
* [MCP Authorization Controls: The Dual-Layer Security Model via Cloud IAM](mcp_authorization_controls_iam.md): Eliminating confused deputy hazards via Gate 1 MCP Gate (`roles/mcp.toolUser`) and Gate 2 Service Gate (target resource IAM roles).
* [Fine-Grained MCP Authorization: IAM Deny Policies for Tool Modification Guardrails](mcp_iam_deny_fine_grained_controls.md): Declarative guardrails using CEL attribute conditions (`tool.isReadOnly == false`) to enforce read-only agent boundaries across Cloud Run, BigQuery, and AlloyDB.
* [Google MCP Server Integration with Model Armor](google_mcp_server_model_armor.md): Inline AI threat defense, prompt injection mitigation, jailbreak prevention, and floor settings configuration (`gcloud model-armor floorsettings update`).
* [MCP Toolsets: Protecting the Context Window via Virtual MCP Server Subsets](toolsets_protect_the_context_window.md): Grouping granular tools into domain-specific virtual endpoints to prevent affordance saturation, token bloat, and model confusion.
* [Example: MCP for BigQuery — Intelligence at Scale & Zero-Copy Analytics](example_mcp_for_bigquery.md): Powering agents with petabyte-scale zero-copy analytics, BigQuery ML/AI SQL functions, and CLI inspection (`execute_sql`, `get_table_info`).
* [Google MCP Server Catalog: GKE, GCE, Maps & Enterprise Cloud Services](mcp_servers_gce_gke_maps_catalog.md): Directory of available and upcoming Google MCP servers across GKE (cluster/pod triage), Maps Grounding (`search_places`, `compute_routes`), SecOps, and Vertex AI.
* [Gemini Cloud Assist MCP Server: Architecture, Operations & Cross-Surface Integration](gemini_cloud_assist_mcp_server.md): Connecting the 4 cloud ops pillars (Design, Investigate, Manage, Optimise) across Gemini CLI, Antigravity, JetSki, and custom autonomous agents.
* [Making the Call: Native Function Calling vs. Model Context Protocol (MCP)](making_the_call_function_calling_vs_mcp.md): Canonical decision framework comparing single-client script prototyping (function calling) vs multi-client audited production shipping (MCP).
* [Syncless Identity Federation: Workforce Identity Federation for Gemini Enterprise & Google Cloud](syncless_identity_federation.md): Eliminating shadow directory replication via OIDC/SAML token exchange through Secure Token Service (STS) for Gemini Enterprise and Cloud Console access.
* [Workforce Identity Federation (WIF) for Gemini Enterprise](wif_for_gemini_enterprise.md): Capabilities, constraints, and why the WIF+SCIM hybrid pattern restores agent autocompletion, NotebookLM sharing, and collaborative features.
* [Cloud Identity with Microsoft Federated Connectors](cloud_identity_microsoft_federated_connectors.md): Recommended hybrid enterprise architecture for Microsoft 365 (Outlook, SharePoint, OneDrive) integration using OAuth 2.0 delegated permissions.
* [Cloud Identity with Multiple Google Workspace Tenants](cloud_identity_multiple_google_workspace.md): Resolving M&A multi-domain OAuth conflicts with Google Auth Platform Internal application type and backend engineering cross-domain allowlisting.
* [3rd-Party IdP SSO with Google Cloud Identity](third_party_idp_sso_with_cloud_identity.md): Enabling Okta, Ping Identity, and Microsoft Entra ID SAML 2.0 / OIDC SSO within Cloud Identity without requiring Workforce Identity Federation.
* [Wiz: From CNAPP to AI-APP — Google's Flagship AI Security Platform](wiz_from_cnapp_to_ai_app.md): Google's cybersecurity acquisition uniting Cloud-Native Application Protection (CNAPP) with AI Application Protection (AI-APP) across Wiz Code, Wiz Cloud, and Wiz Defend.
* [Secure AI Wherever It Runs: Multi-Environment Protection with Wiz AI-APP](secure_ai_wherever_it_runs_wiz_ai_app.md): Ingesting signals across Workstations (IDEs/CLIs), SaaS AI (Copilot/Salesforce), Cloud PaaS (Vertex AI/GKE), and custom apps into the centralized Wiz Security Graph.
* [Wiz AI Visibility: Multi-Cloud AI Inventory & AI-BOM](wiz_ai_inventory_and_ai_bom.md): Centralizing Multi-Cloud AI Inventory (AWS Bedrock, OpenAI, GCP Vertex/Dialogflow) and generating developer supply chain AI-BOMs across IDEs and CI/CD pipelines.
* [Wiz AI Security Console: 4-Stage Operating Pipeline & Agentic Governance](wiz_ai_security_dashboard_console.md): The 4 operational stages (Visibility, Posture, Risk, Threat Detection) with OWASP Top 10 for Agentic Applications compliance and agentic identity governance.
* [Wiz Red Agent: Autonomous AI Penetration Testing & Exploit Chains](wiz_red_agent_ai_pentesting_exploit_chain.md): Autonomous DAST attack simulation revealing multi-step MCP auth bypass, confused deputy tool abuse, and database PII/credential exfiltration.

---

## Daily Navigation
* [Master Elevate Curriculum](../README.md)
* [Day 1 Notes](../Day_1/README.md)
* [Day 3 Notes](../Day_3/README.md)
