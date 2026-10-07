# Elevate — Day 4: Google ADK 2.0 Graph Engine & Enterprise Production Systems

## Overview

Day 4 focuses on **Google ADK 2.0**, exploring the paradigm shift to graph-based execution engines, deterministic state graphs, conditional and parallel branching, native human-in-the-loop (HITL) checkpoints, and enterprise production architectures.

---

## Day 4 Session Notes

### 1. ADK 2.0 Paradigm Shift & Graph Architecture
* [The Paradigm Shift: ADK 1.x to ADK 2.0 Graph Execution Engine](adk_2_paradigm_shift_graph_execution_engine.md): Transitioning from hierarchical prompt-based executors to deterministic graph-based execution engines with DAG nodes, conditional edges, parallel fan-out, and built-in HITL.
* [Google ADK Architecture: Runner, Session, State & Contexts](google_adk_architecture_runner_session_state_context.md): Core runtime abstractions connecting Runner, Session, 4-tier scoped State (`session`, `user:`, `app:`, `temp:`), Event stream, `InvocationContext` $\rightarrow$ `ToolContext`, and pluggable services (`SessionService`, `MemoryService`, `ArtifactService`).
* [ADK Concepts: Callbacks & Lifecycle Interception Hooks](adk_concepts_callbacks_lifecycle_hooks.md): The 6 lifecycle hooks (`before/after_agent`, `before/after_model`, `before/after_tool`) across Agent, Model, and Tool boundaries for guardrails, PII masking, token accounting, and Dual-Gate IAM.
* [Agent Memory Hierarchy: Short-Term vs. Long-Term Subsystems](agent_memory_hierarchy_episodic_semantic_procedural.md): Cognitive memory structure separating Short-Term working context from Long-Term memory (Episodic experiences, Semantic domain knowledge, and Procedural executable skills).
* [How Memory Bank Works: Session Initiation & Lifecycle (Step 1)](how_memory_bank_works_step_1_initiate_session.md): The foundational mechanics of `CreateSessions`, `userID` isolation, automated asynchronous fact extraction/merging, and explicit `memory-as-a-tool` interactions in Vertex AI Agent Engine.
* [Vertex AI Agent Engine: Memory Bank Console & Production Extraction](vertex_ai_agent_engine_memory_bank_console_example.md): Operational deep dive into the Google Cloud Console dashboard, telemetry metrics (LRO latency, token usage), scoped memory schemas (`user_id`, `app_name`), and temporal fact consolidation.
* [ADK Framework Code Reference: Agent Instantiation & PreloadMemoryTool](adk_framework_code_example_preload_memory_tools.md): Code implementation guide for declarative ADK `Agent` instantiation with Gemini 2.5 Pro, `PreloadMemoryTool()`, `google_search` grounding, and custom Python domain APIs.
* [Competitive Analysis: Google ADK 2.0 vs. LangGraph](adk_2_vs_langgraph_competitive_architecture_matrix.md): Head-to-head architectural comparison across 5 dimensions: end-to-end platform scope, Google Cloud-native deployment (Agent Runtime/Cloud Run), multi-agent collaboration, built-in eval, and enterprise ecosystem integration.
* [Google Agents CLI: The 7 Bundled Skills Suite](agents_cli_7_bundled_skills_suite.md): The complete developer tooling suite (Workflow, ADK Code, Scaffold, Eval, Deploy, Publish, Observability) guiding AI assistants through building, testing, and deploying enterprise agents.
* [Google Agents CLI: Core Command Reference & Workflows](agents_cli_core_commands_reference.md): Operational guide covering all seven core CLI commands (`setup`, `scaffold`, `run`, `eval run`, `infra`, `deploy`, `publish`) bridging local inner-loops to production cloud deployment.
* [What Is a Harness? Agent = Model + Harness](what_is_a_harness_agent_equals_model_plus_harness.md): The evolution of AI engineering from Prompt Engineering (2022–2023) to Context Engineering (2024–2025) to Harness Engineering (2026)—wrapping models in deterministic sandboxes, lifecycle hooks, and compounding feedback loops.
* [Evaluating Vibe Coding Agents: The 3 Core Challenges](evaluating_vibe_coding_agents_three_challenges.md): Why evaluating vibe coding is unique—analyzing the Underspecification Gap, Validation Asymmetry (perceived vs. actual correctness), and Iterative Sessions as compounding state.
* [The 7 Dimensions of Agent Evaluation: User-Facing, Internal & Transversal Safety](agent_eval_seven_dimensions_framework.md): The comprehensive evaluation framework spanning User-Facing dimensions (intent, correctness, visual, efficiency), Internal engineering dimensions (code quality, trajectory, self-repair), and the Transversal Safety layer (vulnerabilities, secrets, IP, refusal).
* [Evaluation Dimension 1: Intent Satisfaction](eval_dimension_1_intent_satisfaction.md): Evaluating whether the agent built what the user meant through automated rubric generation, LLM-as-a-judge scoring, human ground-truth calibration, and session convergence tracking.
* [Evaluation Dimensions 2–4: Correctness, Visuals & Efficiency](eval_dimensions_2_to_4_correctness_visual_efficiency.md): Operationalizing Functional Correctness (anti-tampering sandboxes), Visual & Behavioural Fidelity (Playwright DOM tests & multimodal visual judges), and Cost & Efficiency (token spend, latency, and turn convergence).
* [Evaluation Dimensions 5–6: Internal Quality & Trajectory](eval_dimensions_5_and_6_internal_quality_trajectory.md): Auditing code maintainability, project-specific idiom conformity (AST linters, LLM style judge), and trajectory efficiency (OTEL trace spans, avoiding fragile accidental success).
* [Evaluation Dimension 7: Self-Repair Behaviour](eval_dimension_7_self_repair_behaviour.md): Assessing cognitive resilience during build and test failures—contrasting genuine root-cause repair against deceptive test tampering, and implementing automated test immutability evaluation gates.
* [How to Evaluate: The 8 Scientific Methodologies](how_to_evaluate_eight_methods.md): The full evaluation playbook combining standardized benchmarks, automated CI unit testing, security scanning, LLM-as-judge rubrics, Playwright browser workflows, OTEL trajectory inspection, human expert review, and online production sampling.
* [The 8 Agent Evaluation Methods: Deep-Dive Tooling & Implementation Playbook](eval_methods_deep_dive_tooling_playbook.md): Technical implementation details for the 8 evaluation methods—covering benchmarks (SWE-bench, Vibe Code Bench, LiveCodeBench), security scanners (Snyk, Semgrep, `git-secrets`), LLM-as-a-judge rubrics, Playwright browser automation, OTEL trace-replay, and biased online production sampling.

### 2. Deterministic Graph Routing & State Machines
* [Scenario 2: Data Flow & Scoped Variables Across Multi-Agent Pipelines](scenario_2_data_flow_scoped_variables_multiagent_pipelines.md): Decoupling the data plane from the reasoning plane via ADK 2.0 typed Pydantic `StateGraph` schemas, isolating node contexts, and eliminating context bloat in sequential workflows.

### 3. Multi-Agent Orchestration & A2A Interoperability
* [A2A: Open Protocol for Agent-to-Agent Interoperability](a2a_open_protocol_agent_to_agent_interoperability.md): The open protocol standard enabling federated communication between opaque agentic systems, featuring the 3-entity actor model (End-User, Client, Remote Agent) and comparing A2A vs. MCP vs. REST.
* [A2A Agent Card: The `.well-known/agent.json` Discovery Schema](a2a_agent_card_well_known_discovery_schema.md): Declarative capability discovery schema (`https://DOMAIN/.well-known/agent.json`), defining agent metadata, skill input/output schemas, supported modalities, and authentication contracts.
* [A2A vs. MCP: Architectural Coexistence & Interoperability](a2a_vs_mcp_coexistence_architecture.md): The complementary relationship between MCP (vertical data/tool bus) and A2A (horizontal blackbox agent federation bus) within an enterprise agent mesh.
* [A2A Component Breakdown: The 5 Core Primitives](a2a_component_breakdown_client_server_cards_messages_artifacts.md): Deep structural decomposition of A2A Client, Server, Agent Card (`supports_authenticated_extended_card`), Message turns, and Artifacts.
* [Design Patterns & Trade-offs: Data as a Tool (MCP)](data_as_a_tool_mcp_design_options_tradeoffs.md): Exploring Centralized Tool Gateways (Toolbox for Databases) vs. Encapsulating APIs as discrete MCP Tools, detailing technical challenges, governance, and SPOF trade-offs.
* [Google MCP Toolbox for Databases: Open Source Enterprise MCP Gateway](mcp_toolbox_for_databases_overview.md): Deep dive into Google's open-source database gateway (`go/mcp-toolbox`), connecting agents to AlloyDB, BigQuery, Spanner, Cloud SQL, and open-source engines with connection pooling, IAM auth, and OTEL observability.

### 4. Human-in-the-Loop (HITL) & State Checkpointing
* [Native `interrupt()` / `resume()` & `CloudFirestoreCheckpointer` in ADK 2.0](adk_2_paradigm_shift_graph_execution_engine.md): Deterministic graph execution pausing, state persistence across restarts, and human approval resumption.
* [`A2A_INTERRUPT_REQUIRED` & Cross-Agent HITL Escalation](a2a_open_protocol_agent_to_agent_interoperability.md): Propagating human-in-the-loop task interrupts across remote A2A servers and client surfaces.
* [Cross-Device Session Checkpointing (`FirestoreSessionService`)](scenario_1_multiturn_conversation_continuity_state_persistence.md): Sub-10ms session hydration and state continuity across stateless Cloud Run instances.

### 5. Production Enterprise Systems & Cloud Deployment
* [Agent Platform Runtime: Registry, SPIFFE Identity & OTEL Observability](agent_platform_runtime_master_architecture.md): The master enterprise runtime architecture uniting Agent Registry (top control plane), SPIFFE-based Agent Identity with Dual-Gate Auth Manager (center execution plane), and OTEL-native distributed tracing (bottom data plane).
* [Agent Platform Runtime: End-to-End System Architecture](agent_platform_runtime_end_to_end_architecture.md): The complete end-to-end data flow tracing user ingress across multi-channel frontends, Agent Registry discovery, SPIFFE-governed runtime execution, and downstream egress across Agents (A2A), Tools (MCP), Models, and Enterprise APIs.
* [Vector Database Architecture: Dedicated vs. Integrated Analytical vs. Transactional](vector_database_design_options_tradeoffs.md): Decision matrix evaluating Managed Dedicated (Vertex AI Vector Search), Integrated Analytical (BigQuery Vector Search), and Integrated Transactional (AlloyDB/Cloud SQL `pgvector`, Cloud Spanner) based on latency, scale, and ACID needs.
* [Scenario 1: Multi-Turn Conversation Continuity & State Persistence](scenario_1_multiturn_conversation_continuity_state_persistence.md): Solving cross-device continuity (Mobile App $\rightarrow$ Web Portal) on stateless autoscaled Cloud Run instances via ADK `SessionService` (Firestore / Cloud SQL) and eliminating client-side history payloads.
* [Scenario 3: Enterprise Guardrails, PII Redaction & Tool Auditing](scenario_3_enterprise_guardrails_pii_redaction_auditing.md): Enforcing CSO requirements (ingress SSN/credit card scrubbing via `before_model_callback`, destructive SQL delete RBAC via `before_tool_callback`, and tamper-proof Cloud Audit Logs) without polluting business logic.

---

## Daily Navigation
* [Repository Root Hub](../../README.md)
* [Master Elevate Curriculum](../README.md)
* [Day 1 Notes](../Day_1/README.md)
* [Day 2 Notes](../Day_2/README.md)
* [Day 3 Notes](../Day_3/README.md)
* [Day 5 Notes](../Day_5/README.md)
