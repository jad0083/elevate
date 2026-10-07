# Elevate Mock Assessment Review — Questions 12–30 (Grounded Answer Key)

> **Companion Resources**:
> - [55-Question Practice Knowledge Check](PRACTICE_EXAM_50Q.md)
> - [Elevate Exam Study Guide & Cram Sheet](STUDY_GUIDE.md)
> - [Master Technical Synthesis](MASTER_SYNTHESIS.md)
> - [CLI & Python SDK Quick-Reference Cheat Sheet](CLI_AND_SDK_CHEATSHEET.md)
> - [Master Curriculum Index](../Notes/README.md)

---

## About This Review

This document captures **19 questions (Q12–Q30)** from a mock run of the Elevate knowledge-check assessment. Questions 1–11 were not captured. Every answer was **re-verified against official, current documentation on 2026-10-07** (Google Cloud docs, `adk.dev`, the A2A specification, and the Gemini API docs), with a verbatim supporting quote and source URL recorded for each.

| Result | Count |
| :--- | :---: |
| Answers confirmed by official documentation | **19 / 19** |
| Answers corrected after grounding | **0** |
| Questions on topics missing or incomplete in `Notes/` | **12** (see [Section 4](#section-4-curriculum-gaps--corrections-triggered-by-this-review)) |

> **Documentation rebrands to know before you click a source link**:
> - Vertex AI docs now live under **Gemini Enterprise Agent Platform** (`docs.cloud.google.com/gemini-enterprise-agent-platform/...`); old `cloud.google.com/vertex-ai/...` links redirect there.
> - ADK docs moved from `google.github.io/adk-docs` to **`adk.dev`**.
> - The MCP Toolbox for Databases repository was renamed from `googleapis/genai-toolbox` to **`googleapis/mcp-toolbox`**.

## How to Use This Review

1. **Section 1 (Self-Test Mode)**: Answer all 19 questions without looking ahead. They are regrouped by theme, so the question numbers are not in sequence.
2. **Section 2 (Quick Scoring Grid)**: Grade yourself, and note which topics are thinly covered in the curriculum notes.
3. **Section 3 (Grounded Answer Key)**: For each question: why the answer wins, why each distractor fails (including distractors that are *partially* true), the official source with a verbatim quote, and the matching curriculum note.
4. **Section 4 (Gaps & Corrections)**: The curriculum topics this assessment exposed as missing, plus the outdated repository facts corrected as a result.

---

## Section 1: Mock Assessment Questions (Self-Test Mode — Q12 to Q30)

### Part A: Model Armor & Governed MCP (Questions 12–15, 25)

#### Question 12: Model Armor Document Screening — Supported File Types
A customer wants Model Armor to screen uploaded Microsoft Office files for sensitive and malicious content, in addition to PDFs and plain text. Which of the following file types does Model Armor's document screening actually cover?

- **A)** Only PDFs; no other file format is supported for document screening.
- **B)** Only plain text files; binary Office formats are explicitly unsupported.
- **C)** Image files exclusively, since document screening is really an alias for image screening.
- **D)** PDFs, CSV, TXT, and Microsoft Word, PowerPoint, and Excel formats (including template variants like DOTX and POTX).
- **E)** Any file format whatsoever, with no restriction on type or extension.

#### Question 13: Guaranteed Minimum Model Armor Protection Across Teams
An organization wants a guaranteed minimum level of Model Armor protection that individual application teams cannot drop below when they configure templates for their own apps. Which capability provides that?

- **A)** Enforcement types, which determine whether a violation is logged for monitoring or actively stops the content from proceeding.
- **B)** Floor settings, which define minimum requirements applying to all templates created at a given point in the resource hierarchy.
- **C)** Confidence thresholds, which determine how certain a filter must be about a violation before it reports a match.
- **D)** Template versioning, which pins each application to the most recent configuration an administrator reviewed and approved.
- **E)** Sensitive Data Protection templates, which centralize detection rules so that every team inherits an identical set of them.

#### Question 14: The Always-On Responsible AI Filter
Within Model Armor's Responsible AI filter categories, which specific filter is applied by default and cannot be turned off under any template configuration (as of August 2026)?

- **A)** Hate speech
- **B)** Harassment
- **C)** Sexually suggestive content
- **D)** CSAM (child sexual abuse material)
- **E)** Violence

#### Question 15: Is Model Armor Google-Cloud-Only?
A customer asks whether Model Armor is limited to protecting AI applications deployed on Google Cloud only. Is that true?

- **A)** Model Armor requires full migration to Agent Platform before any protection becomes available.
- **B)** Model Armor is available only as an on-premises appliance with no cloud-hosted option.
- **C)** Model Armor only protects applications deployed on Google Cloud infrastructure.
- **D)** Model Armor provides protection across environments, including AI applications deployed on Google Cloud or other cloud providers.
- **E)** Model Armor functions exclusively within Gemini Enterprise with no standalone API access.

#### Question 25: Managed Google Cloud MCP Servers — Enterprise Capabilities
What enterprise capabilities does the managed Google Cloud MCP servers platform provide alongside basic protocol support?

- **A)** Only raw JSON-RPC message passing, with no additional enterprise controls, discovery, governance, or content-security layer built on top of it.
- **B)** Only billing consolidation, with no security or discovery features.
- **C)** Only local, stdio-based transport with no remote HTTP option.
- **D)** MCP discovery, IAM/VPC Service Controls governance, MCP-spec-compliant authentication, Model Armor content scanning, and Cloud Trace/audit-log observability.
- **E)** Only support for a single hard-coded model provider.

### Part B: CodeMender, Agent Gateway & Agent Registry (Questions 16–20)

#### Question 16: Overriding CodeMender's Model
Can the model used by CodeMender be overridden?

- **A)** Model selection is only configurable by contacting Google Cloud support directly; there is no CLI flag.
- **B)** The model is fixed and cannot be changed under any configuration.
- **C)** The model can be overridden by passing a `--model` flag with a different supported model identifier.
- **D)** CodeMender does not use a Gemini model at all; it relies exclusively on a third-party frontier model.
- **E)** The model changes randomly on every invocation for load-balancing purposes.

#### Question 17: Agent Gateway's Role
What is Agent Gateway's function with respect to agent traffic, and what does it integrate with for content inspection?

- **A)** Only handles usage billing and cost tracking; it plays no role in traffic inspection, policy enforcement, content scanning, or Model Armor integration.
- **B)** Available only for agents built with the LangChain framework, not for ADK-based agents at all.
- **C)** Only governs outbound egress traffic; inbound ingress traffic to the agent is entirely unmanaged.
- **D)** Fully managed component that governs agent traffic, enforcing access policies and supporting Model Armor inspection of tool calls.
- **E)** Replaces Agent Identity, making per-agent cryptographic identity unnecessary going forward.

#### Question 18: Automated Patching Without Regressions
An engineering manager's main objection to automated patching is regressions: a fix that closes the vulnerability but quietly breaks working behaviour. What addresses that, and who decides whether the change lands?

- **A)** The patch is applied to the repository automatically and reverted only if production error rates climb measurably after the deployment goes out.
- **B)** A second scan is run against the patched file, and the change is merged automatically whenever that follow-up scan comes back clean.
- **C)** Patches are constrained to single-line edits, which keeps the blast radius small enough that a human review step is not required at all.
- **D)** A rules engine checks the diff against the project's style guide, after which a security reviewer merges it on the development team's behalf.
- **E)** The fix is validated with an LLM-as-a-judge check that existing functionality still works, then delivered as a diff inside developer tools where engineers review and approve it before anything is committed.

#### Question 19: CodeMender — Where Reasoning vs. Execution Happens
What is CodeMender's architecture with respect to where reasoning happens versus where code execution happens?

- **A)** Both reasoning and code execution happen entirely on Google-managed infrastructure, with no local component.
- **B)** The hosted reasoning engine (agentic reasoning, threat modeling, orchestration logic) runs on Gemini Enterprise Agent Platform, while the local `cm` CLI executes file reads, local build checks, and proof-of-concept exploit verification in the user's local sandbox, sending only surgical code snippets and tool execution results to the cloud backend.
- **C)** All code execution happens on Google's infrastructure via full repository upload; only the final report is returned to the customer.
- **D)** CodeMender has no cloud component whatsoever; it runs entirely offline with no connection to Gemini Enterprise Agent Platform.
- **E)** Reasoning happens locally on the customer's machine, while raw source code is uploaded to Google for storage only.

#### Question 20: Agent Registry — Agent Identifier vs. Agent Principal
In the context of the Agent Registry, what is the difference between an Agent Identifier and an Agent Principal?

- **A)** An Agent Identifier is a globally unique, immutable URN used as a stable reference, whereas an Agent Principal is an IAM identifier used for permissions and auditing.
- **B)** An Agent Identifier represents the human user accessing the application, whereas an Agent Principal represents the agent's autonomous execution environment.
- **C)** An Agent Identifier is a temporary session token used for API access, whereas an Agent Principal is a permanent, globally unique URN.
- **D)** An Agent Identifier is used to manage network bindings to MCP servers, whereas an Agent Principal defines the agent's specific executable skills.
- **E)** An Agent Identifier is an IAM service account used for auditing, whereas an Agent Principal is an OAuth token used for delegated access.

### Part C: ADK Runtime, A2A, Toolbox & Evaluation (Questions 21–23, 26, 29–30)

#### Question 21: ADK 2.0 Core Architectural Change
What is the core architectural change introduced in ADK 2.0 compared to ADK 1.x?

- **A)** A move from open-source to closed-source licensing.
- **B)** A move away from Python entirely to a JVM-only runtime.
- **C)** The elimination of all workflow agent types in favor of a single monolithic LLM call.
- **D)** The complete removal of tool-calling support in favor of pure text generation.
- **E)** A move from a hierarchical agent executor with prompt-based orchestration to a graph-based workflow engine, enabling deterministic, code-defined execution flows combined with AI reasoning.

#### Question 22: ADK `SessionService`
What does the `SessionService` do in ADK, and what are two of its implementations?

- **A)** It is responsible solely for model selection at each turn.
- **B)** It exists only in the Java SDK, not in Python, Go, or TypeScript.
- **C)** It loads and saves `Session` objects — the state and event history of one conversation — and applies state deltas from events.
- **D)** It generates embeddings for RAG pipelines; implementations include `TextEmbeddingService` and `MultimodalEmbeddingService`.
- **E)** It manages billing and quota enforcement across projects.

#### Question 23: A2A Protocol Core Technologies
Which set of technologies make up the A2A protocol's core design, chosen specifically to reuse existing, well-understood standards?

- **A)** FTP for transfer, SOAP for messaging, and long polling for streams.
- **B)** WebSockets for transport, GraphQL for queries, and WebRTC for data streaming.
- **C)** Raw TCP sockets, Protocol Buffers for RPC, and MQTT for streaming.
- **D)** HTTP, JSON-RPC 2.0, and Server-Sent Events (SSE) — reusing existing web standards rather than inventing a new protocol layer.
- **E)** MQTT exclusively for all agent-to-agent messaging.

#### Question 26: ADK Support for MCP Toolbox for Databases
What is the nature of ADK's support for MCP Toolbox for Databases?

- **A)** No; ADK has no relationship to MCP Toolbox for Databases and requires entirely custom integration code.
- **B)** ADK only supports MCP Toolbox through a paid, closed-source connector unavailable to open-source users.
- **C)** Yes — ADK ships a built-in integration that lets an agent use a running Toolbox server as a source of tools, without needing custom protocol glue.
- **D)** MCP Toolbox can only be used with LangChain, never with ADK.
- **E)** ADK requires MCP Toolbox to be rewritten in Java before it can be used, regardless of the agent's implementation language, deployment target, or hosting environment.

#### Question 29: Streaming Tokens, Tool Progress & Confirmation Cards to a UI
A team needs their UI to render tokens as they are produced, show when a specific tool such as SQL Search starts and finishes, and deliver structured cards that ask the user to confirm an action. Which ADK mechanism carries all three?

- **A)** The `SessionService`, by polling the persisted session record after each turn and diffing it against the previously retrieved snapshot.
- **B)** The `ArtifactService`, which pushes binary and structured payloads to the browser over a dedicated server-side channel.
- **C)** A streaming callback registered on the Runner, which is the only component in the framework permitted to emit incremental output.
- **D)** The event stream yielded by `runner.run_async()`, where incremental chunks are flagged as partial, tool calls and their results ride on their own events, and `EventActions` signals state changes and control flow.
- **E)** A direct subscription from the front end to the model endpoint, bypassing the Runner so that no server-side buffering is introduced.

#### Question 30: Right Answer, Wrong Trajectory (ADK Eval)
An agent is asked to process a refund. It returns the correct refund amount and a well-worded confirmation, but the trace shows it never called `lookup_order` — it produced the number from context. The eval case defines both an expected tool trajectory and an expected final response. What happens, and why?

- **A)** The case passes, because both built-in criteria evaluate the final response text.
- **B)** The case fails on `response_match_score`, because ROUGE-1 penalizes any tool call that is missing.
- **C)** The case fails on `tool_trajectory_avg_score`, because that criterion compares the agent's actual tool calls against the expected trajectory and defaults to requiring an exact match.
- **D)** The case is skipped, because ADK Eval cannot score a run in which no tools were called.

### Part D: Model Serving, Caching & Routing (Questions 24, 27–28)

#### Question 24: Provisioned Throughput — Documented Limitation
Which of the following is a documented limitation of Provisioned Throughput?

- **A)** Supports batch prediction calls at the same guaranteed rate as real-time calls.
- **B)** Has no interaction with fine-tuned model endpoints; tuned models are billed completely independently and never count toward any shared quota, even in the same project.
- **C)** Guarantees capacity for every Google Cloud product unconditionally, with no exceptions.
- **D)** Cannot be purchased in any increment smaller than a full year commitment.
- **E)** Doesn't support batch prediction calls, and doesn't guarantee capacity for calls made by other Agent Platform products (e.g., Agent Search) using the same model.

#### Question 27: Context Caching Minimum Input Tokens
Does the Gemini API require a minimum input token count to use context caching, and does that minimum change from model to model?

- **A)** There is no minimum; caching applies to prompts of any length, including a single token.
- **B)** Yes — for example, Gemini 2.5 Flash requires at least 2,048 tokens while Gemini 3.7 Flash requires at least 4,096 tokens before implicit caching kicks in.
- **C)** The minimum is a flat 1,000,000 tokens for every model with no exceptions.
- **D)** Minimum token requirements apply only to explicit caching, never to implicit caching.
- **E)** Minimum token requirements were removed entirely as of Gemini 3.

#### Question 28: The Cost Argument for Semantic Routing
Given a meaningful per-token cost gap between Gemini's Pro and Flash-Lite tiers, what's the practical cost argument for routing queries through a semantic router instead of sending every query to a single model?

- **A)** There is no cost argument; routing decisions have zero effect on total spend regardless of model tier distribution.
- **B)** Directing simple queries to the cheaper tier and complex queries to the more capable tier reduces total spend compared to sending every query to the most capable (and most expensive) tier, without sacrificing quality on tasks that genuinely need the stronger model.
- **C)** Routing exclusively increases cost because the router itself always requires a full, expensive LLM call regardless of implementation.
- **D)** The cost argument only applies to batch workloads, never to real-time traffic.
- **E)** Model tier cost differentials are identical across all providers and therefore irrelevant to a routing decision.

---

## Section 2: Quick Scoring Grid (Q12–Q30)

| Q# | Correct | Topic | Grounding | Covered in `Notes/`? |
| :---: | :---: | :--- | :---: | :---: |
| **Q12** | **D** | Model Armor document screening file types (PDF, CSV, TXT, Word/PowerPoint/Excel incl. templates) | Confirmed | Gap |
| **Q13** | **B** | Model Armor floor settings (minimum bar across the resource hierarchy) | Confirmed | Yes |
| **Q14** | **D** | CSAM filter is always on and cannot be disabled | Confirmed | Gap |
| **Q15** | **D** | Model Armor protects apps on Google Cloud *and* other clouds | Confirmed | Gap |
| **Q16** | **C** | CodeMender `--model` override | Confirmed | Gap |
| **Q17** | **D** | Agent Gateway: ingress + egress policy enforcement with Model Armor inspection | Confirmed | Gap |
| **Q18** | **E** | CodeMender: LLM-as-a-judge regression check, then human review and approval | Confirmed | Partial |
| **Q19** | **B** | CodeMender: hosted reasoning, local `cm` execution, snippets only | Confirmed | Partial |
| **Q20** | **A** | Agent Registry: Agent Identifier (URN) vs. Agent Principal (IAM) | Confirmed | Partial |
| **Q21** | **E** | ADK 2.0: hierarchical executor → graph-based workflow engine | Confirmed | Yes |
| **Q22** | **C** | `SessionService`: load/save sessions, apply state deltas | Confirmed | Partial |
| **Q23** | **D** | A2A core: HTTP + JSON-RPC 2.0 + SSE | Confirmed | Yes |
| **Q24** | **E** | Provisioned Throughput: no batch, no coverage of other products' calls | Confirmed | Partial |
| **Q25** | **D** | Managed MCP servers: discovery, IAM/VPC-SC, MCP auth, Model Armor, Trace/audit logs | Confirmed | Yes |
| **Q26** | **C** | ADK built-in `ToolboxToolset` for MCP Toolbox for Databases | Confirmed | Yes |
| **Q27** | **B** | Context-caching minimum input tokens are model-specific | Confirmed | Gap (was outdated) |
| **Q28** | **B** | Semantic routing cost argument (cheap tier for simple, Pro for complex) | Confirmed | Yes |
| **Q29** | **D** | `runner.run_async()` event stream (`partial`, tool events, `EventActions`) | Confirmed | Gap |
| **Q30** | **C** | ADK Eval fails on `tool_trajectory_avg_score` (default `1.0`, `EXACT`) | Confirmed | Yes (defaults clarified) |

---

## Section 3: Grounded Answer Key, Rationales & Sources

### Part A Answer Key: Model Armor & Governed MCP

#### Q12 — Model Armor Document Screening — Supported File Types
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - Document screening extracts and screens text from: **PDF, CSV, TXT**; **Word** (`DOCX`, `DOCM`, `DOTX`, `DOTM`); **PowerPoint** (`PPTX`, `PPTM`, `POTX`, `POTM`, `POT`); and **Excel** (`XLSX`, `XLSM`, `XLTX`, `XLTM`). Files are capped at **4 MB**.
  - *Distractors A and B* name real supported types but wrongly say "only". *Distractor C* is wrong, although image screening does exist as a **separate** capability for prompts and responses; it is not an alias for document screening. *Distractor E* is wrong because only the listed types are supported.
- **Official Source**: [Model Armor overview](https://docs.cloud.google.com/model-armor/overview) — *"Microsoft Word documents: DOCX, DOCM, DOTX, DOTM, Microsoft PowerPoint slides: PPTX, PPTM, POTX, POTM, POT, Microsoft Excel sheets: XLSX, XLSM, XLTX, XLTM"*
- **Curriculum Source Links**: [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md) *(Model Armor context only; file types not covered)*

#### Q13 — Guaranteed Minimum Model Armor Protection Across Teams
- **Correct Answer**: **B**
- **Why It Is Correct & Why Distractors Fail**:
  - **Floor settings** set the minimum filters and confidence levels for every template beneath an organization, folder, or project. Model Armor rejects any template create or update that is less strict than the floor. Organization and folder floors are configured through the API.
  - *Distractors A, C, and E* are real features (inspect-only vs. inspect-and-block enforcement, confidence thresholds, Sensitive Data Protection templates), but none of them prevents a team from going below a minimum. *Distractor D* is not a feature: Model Armor versions its *filters* (v1–v4), not templates.
- **Official Source**: [Configure floor settings](https://docs.cloud.google.com/model-armor/configure-floor-settings) — *"You can set floor settings at the organization, folder, and project levels… You cannot create or update a template that's less strict than the floor settings."*
- **Curriculum Source Links**: [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md)

#### Q14 — The Always-On Responsible AI Filter
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - Model Armor has four configurable Responsible AI categories (**Hate speech, Harassment, Sexually explicit, Dangerous content**), each with its own confidence level. **CSAM** is a separate filter that is always on. The July 2026 (v3) and September 2026 (v4) filter updates did not change this.
  - *Distractors A and B* are real categories, but they can be turned off. *Distractor C* uses the wrong name (the category is "Sexually explicit") and can also be turned off. *Distractor E* does not exist as a category; the closest is "Dangerous content".
- **Official Source**: [Model Armor overview](https://docs.cloud.google.com/model-armor/overview) — *"Contains references to child sexual abuse material (CSAM). This filter is applied by default and cannot be turned off."*
- **Curriculum Source Links**: [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md) *(CSAM not covered)*

#### Q15 — Is Model Armor Google-Cloud-Only?
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - Model Armor works with any model and any cloud. Applications anywhere can call its standalone REST API, and it also integrates natively with Gemini Enterprise Agent Platform, Agent Gateway, and Google-managed MCP servers.
  - *Distractor E* is partly true: the Gemini Enterprise integration is real, but a standalone API also exists, so "exclusively" is false. *Distractors A, B, and C* are false.
- **Official Source**: [Model Armor overview](https://docs.cloud.google.com/model-armor/overview) — *"Whether you are deploying AI in Google Cloud or other cloud providers, Model Armor can help you prevent malicious input, verify content safety, protect sensitive data…"*
- **Curriculum Source Links**: [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md) *(multi-cloud reach not covered)*

#### Q25 — Managed Google Cloud MCP Servers — Enterprise Capabilities
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - All five capabilities are documented:
    1. **Discovery** through Agent Registry.
    2. **IAM policies** and **VPC Service Controls perimeters**.
    3. Compliance with the **MCP authorization specification**.
    4. **Model Armor** scanning of MCP calls and responses (floor settings also apply to Google-managed MCP servers since December 2025).
    5. **Cloud Trace** and **Cloud Audit Logs**.
  - *Distractor C* is the opposite of the truth: these are **remote** servers exposed over streamable HTTP. *Distractors A, B, and E* are unsupported.
- **Official Source**: [Google Cloud MCP servers overview](https://docs.cloud.google.com/mcp/overview) — *"Google and Google Cloud remote MCP servers are compliant with the MCP authorization specification."*
- **Curriculum Source Links**: [google_mcp_servers_unified_platform.md](../Notes/Day_2/google_mcp_servers_unified_platform.md), [key_capabilities_google_mcp_servers.md](../Notes/Day_2/key_capabilities_google_mcp_servers.md), [mcp_authorization_controls_iam.md](../Notes/Day_2/mcp_authorization_controls_iam.md), [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md)

### Part B Answer Key: CodeMender, Agent Gateway & Agent Registry

#### Q16 — Overriding CodeMender's Model
- **Correct Answer**: **C**
- **Why It Is Correct & Why Distractors Fail**:
  - `cm find`, `cm verify`, and `cm fix` accept `--model MODEL_NAME`, and `config.yaml` accepts a persistent `model:` key. The current default is **Gemini 3.8 Flash**. The alternatives are `gemini-3.7-flash`, `gemini-3.6-flash`, `gemini-3.5-flash`, and `gemini-3.1-pro-preview`.
  - *Distractors A, B, D, and E* are false: CodeMender runs on Gemini, and the model is configurable from the CLI.
  - **Watch out**: The July 2026 launch blog named Gemini 3.5 Flash as the default; the live docs now say 3.8 Flash. Expect quiz items that cite a default model to go stale.
- **Official Source**: [CodeMender overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender) · [Set up your environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/set-up-environment) — *"By default, CodeMender uses Gemini 3.8 Flash. To override the default model, pass the --model flag with the corresponding model identifier"*
- **Curriculum Source Links**: [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md), [CLI_AND_SDK_CHEATSHEET.md](CLI_AND_SDK_CHEATSHEET.md) *(`--model` not covered)*

#### Q17 — Agent Gateway's Role
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - Agent Gateway enforces policy on traffic in both directions: **client-to-agent (ingress)** and **agent-to-anywhere (egress)**. It denies connections by default unless an IAM policy allows them. Model Armor inspects prompts coming in and tool payloads going out.
  - *Distractor C* is false because ingress is governed too. *Distractor B* inverts a real nuance: inline Model Armor on *ingress* is supported **only for ADK-built agents**, and egress inspection covers MCP, OpenAI-format, and A2A traffic. *Distractor E* is false: the Gateway **uses** Agent Identity (SPIFFE IDs) rather than replacing it. *Distractor A* is false.
- **Official Source**: [Agent Gateway overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) · [Model Armor + Agent Gateway](https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration) — *"It acts as the network entry and exit point for all agentic interactions."*
- **Curriculum Source Links**: [agent_platform_runtime_end_to_end_architecture.md](../Notes/Day_4/agent_platform_runtime_end_to_end_architecture.md) *(Agent Gateway not covered)*

#### Q18 — Automated Patching Without Regressions
- **Correct Answer**: **E**
- **Why It Is Correct & Why Distractors Fail**:
  - `cm fix` runs the project's build and unit tests in a local sandbox, then re-runs the proof-of-concept exploit against the patch. An **LLM-as-a-judge** confirms that existing functionality is preserved. Write confirmation is on by default, and engineers inspect changes with `cm vcs diff` before anything is committed.
  - *Distractor B* is partly true: auto-approve exists (`-y` / `confirm_writes: false`), but the docs place responsibility on the customer when human confirmation is disabled, so it is not the designed workflow. *Distractor D* is partly true: you can supply style conventions, but nothing has a security reviewer merging on the team's behalf. *Distractors A and C* are false.
- **Official Source**: [Find and fix vulnerabilities with CodeMender (Google Cloud blog)](https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender) · [Fix and patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/agents/codemender/fix-and-patch) — *"CodeMender further strengthens the fix by using LLM-as-a-judge to ensure it doesn't disrupt existing application functionality… Developers remain in full control, manually reviewing and approving CodeMender's patches before any code is committed"*
- **Curriculum Source Links**: [codemender_wiz_integration_architecture.md](../Notes/Day_3/codemender_wiz_integration_architecture.md), [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md)

#### Q19 — CodeMender — Where Reasoning vs. Execution Happens
- **Correct Answer**: **B**
- **Why It Is Correct & Why Distractors Fail**:
  - This is the documented **local-first execution model**. Reasoning, threat modeling, and orchestration run on the hosted backend. The local `cm` CLI reads files, runs builds, and verifies proof-of-concept exploits in a local sandbox, and only small code snippets and tool results go to the cloud. Full repositories are never uploaded.
  - *Distractor C* is directly contradicted by the docs. *Distractor D* ignores the hosted agent. *Distractor E* has a grain of truth (session snippets are retained for up to 7 days so a scan can be resumed), but reasoning is not local and raw source is not uploaded. *Distractor A* ignores the local CLI.
- **Official Source**: [Set up your environment](https://docs.cloud.google.com/gemini-enterprise-agent-platform/codemender/set-up-environment) — *"Local cm CLI tool executes file reads, local build checks, and proof-of-concept (PoC) exploit verifications in your local sandbox, sending only surgical code snippets and tool execution results to the cloud backend"*
- **Curriculum Source Links**: [codemender_wiz_integration_architecture.md](../Notes/Day_3/codemender_wiz_integration_architecture.md), [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md)

#### Q20 — Agent Registry — Agent Identifier vs. Agent Principal
- **Correct Answer**: **A**
- **Why It Is Correct & Why Distractors Fail**:
  - **Agent Identifier**: a permanent logical URN used for inventory and lookup, for example `urn:agent:projects-PROJECT_NUMBER:projects:PROJECT_NUMBER:locations:REGION:reasoningEngines:AGENT_ID`.
  - **Agent Principal**: the IAM identity that holds permissions and appears in audit logs, for example `principal://agents.global.org-ORGANIZATION_ID.system.id.goog/resources/aiplatform/projects/PROJECT_NUMBER/locations/REGION/reasoningEngines/REASONING_ENGINE_ID`. It may be a service account or a managed workload identity such as a SPIFFE ID.
  - *Distractor E* is partly true: the principal can be a service account, but E attaches it to the wrong term and calls the principal an OAuth token. *Distractors B, C, and D* are false.
- **Official Source**: [Agent Registry concepts](https://docs.cloud.google.com/agent-registry/concepts) — *"The unique Identity and Access Management (IAM) identifier assigned to an agent, letting it hold permissions and be audited."*
- **Curriculum Source Links**: [agent_platform_runtime_master_architecture.md](../Notes/Day_4/agent_platform_runtime_master_architecture.md), [agent_platform_runtime_end_to_end_architecture.md](../Notes/Day_4/agent_platform_runtime_end_to_end_architecture.md)

### Part C Answer Key: ADK Runtime, A2A, Toolbox & Evaluation

#### Q21 — ADK 2.0 Core Architectural Change
- **Correct Answer**: **E**
- **Why It Is Correct & Why Distractors Fail**:
  - ADK 2.0 introduces a **Workflow Runtime**: a graph-based engine in which agents, tools, and functions run as nodes. ADK is still Apache-2.0 licensed and Python-first, and LLM agents and tool calling remain.
  - **Nuance**: ADK 1.x already offered deterministic workflow agents (`SequentialAgent`, `ParallelAgent`, `LoopAgent`), so "prompt-based orchestration" slightly overstates the 1.x model. The core claim of E still holds.
  - *Distractors A–D* are false.
- **Official Source**: [ADK 2.0](https://adk.dev/2.0/) — *"transitioning ADK from a hierarchical agent executor to a graph-based execution engine"*
- **Curriculum Source Links**: [adk_2_paradigm_shift_graph_execution_engine.md](../Notes/Day_4/adk_2_paradigm_shift_graph_execution_engine.md), [adk_advanced_graph_workflows.md](../Notes/Day_1/adk_advanced_graph_workflows.md)

#### Q22 — ADK `SessionService`
- **Correct Answer**: **C**
- **Why It Is Correct & Why Distractors Fail**:
  - `SessionService` creates, gets, lists, and deletes sessions and appends events. Appending an event applies its `state_delta`. The three implementations:

    | Implementation | Persistence | Typical Use |
    | :--- | :--- | :--- |
    | `InMemorySessionService` | None (lost on restart) | Local development and tests |
    | `DatabaseSessionService` | PostgreSQL / MySQL / SQLite | Self-hosted persistence |
    | `VertexAiSessionService` | Managed by Gemini Enterprise Agent Platform | Production on Google Cloud |

  - *Distractor D* uses invented class names. *Distractors A, B, and E* are false.
- **Official Source**: [ADK Sessions](https://adk.dev/sessions/session/) — *"Retrieving a specific `Session` (using its ID) so the agent can continue where it left off"*
- **Curriculum Source Links**: [google_adk_architecture_runner_session_state_context.md](../Notes/Day_4/google_adk_architecture_runner_session_state_context.md), [adk_state.md](../Notes/Day_1/adk_state.md), [a_restart_must_not_erase_memory.md](../Notes/Day_1/a_restart_must_not_erase_memory.md)

#### Q23 — A2A Protocol Core Technologies
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - A2A's design principle is to reuse **HTTP, JSON-RPC 2.0, and Server-Sent Events**. Agents publish an Agent Card at `/.well-known/agent.json` for discovery.
  - *Distractor C* is partly true: A2A v1.0 defines three bindings (JSON-RPC, **gRPC**, and HTTP+JSON/REST), so Protocol Buffers RPC now has a real counterpart. Raw TCP and MQTT are not part of the spec, so C is still wrong. *Distractors A, B, and E* are false.
- **Official Source**: [A2A Protocol Specification](https://a2a-protocol.org/latest/specification/) — *"Simple: Reuse existing, well-understood standards (HTTP, JSON-RPC 2.0, Server-Sent Events)."*
- **Curriculum Source Links**: [a2a_open_protocol_agent_to_agent_interoperability.md](../Notes/Day_4/a2a_open_protocol_agent_to_agent_interoperability.md), [a2a_agent_card_well_known_discovery_schema.md](../Notes/Day_4/a2a_agent_card_well_known_discovery_schema.md), [a2a_vs_mcp_coexistence_architecture.md](../Notes/Day_4/a2a_vs_mcp_coexistence_architecture.md)

#### Q26 — ADK Support for MCP Toolbox for Databases
- **Correct Answer**: **C**
- **Why It Is Correct & Why Distractors Fail**:
  - ADK ships `ToolboxToolset` (`google.adk.tools.toolbox_toolset`). Install it with `pip install google-adk[toolbox]`, which pulls in `toolbox-adk`:

    ```python
    from google.adk.agents import Agent
    from google.adk.tools.toolbox_toolset import ToolboxToolset

    toolbox = ToolboxToolset("http://127.0.0.1:5000")
    agent = Agent(model="gemini-3.8-flash", name="db_agent", tools=[toolbox])
    ```

  - Toolbox is open source and also ships LangChain and LlamaIndex SDKs, which rules out *Distractors B and D*. *Distractors A and E* are false.
- **Official Source**: [ADK — MCP Toolbox for Databases](https://adk.dev/integrations/mcp-toolbox-for-databases/) — *"Google's Agent Development Kit (ADK) has built in support for MCP Toolbox."*
- **Curriculum Source Links**: [mcp_toolbox_for_databases_overview.md](../Notes/Day_4/mcp_toolbox_for_databases_overview.md), [data_as_a_tool_mcp_design_options_tradeoffs.md](../Notes/Day_4/data_as_a_tool_mcp_design_options_tradeoffs.md)

#### Q29 — Streaming Tokens, Tool Progress & Confirmation Cards to a UI
- **Correct Answer**: **D**
- **Why It Is Correct & Why Distractors Fail**:
  - One event stream carries all three UI needs:

    | UI Need | How It Surfaces in the `run_async()` Event Stream |
    | :--- | :--- |
    | Render tokens as produced | Streaming chunks arrive with `event.partial=True`, followed by a final aggregated event |
    | Show tool start and finish | `event.get_function_calls()` / `event.get_function_responses()` |
    | Ask the user to confirm an action | A function-call event named `adk_request_confirmation`, triggered by `require_confirmation=True` or `tool_context.request_confirmation()`; the client replies with a `FunctionResponse` carrying `confirmed` |
    | State and control flow | `EventActions`: `state_delta`, `artifact_delta`, `transfer_to_agent`, `escalate`, `requested_tool_confirmations` |

  - *Distractor C* is partly true: the Runner produces the stream, but by yielding events, not through a special streaming callback, and it is not the "only component allowed" to emit output. *Distractor A* only reads persisted state after the fact. *Distractor B* misdescribes `ArtifactService`, which stores files and does not push to browsers. *Distractor E* loses tool calls, state, and confirmations.
- **Official Source**: [ADK Events](https://adk.dev/events/) · [Tool confirmation](https://adk.dev/tools-custom/confirmation/) — *"[run_async] yields (Python) or returns/emits (Java) the processed event outwards to the calling application."*
- **Curriculum Source Links**: [google_adk_architecture_runner_session_state_context.md](../Notes/Day_4/google_adk_architecture_runner_session_state_context.md), [human_in_the_loop_pattern_deepdive.md](../Notes/Day_1/human_in_the_loop_pattern_deepdive.md)

#### Q30 — Right Answer, Wrong Trajectory (ADK Eval)
- **Correct Answer**: **C**
- **Why It Is Correct & Why Distractors Fail**:
  - When no criteria are configured, ADK Eval applies **`tool_trajectory_avg_score: 1.0`** with trajectory match type **`EXACT`** (the alternatives are `IN_ORDER` and `ANY_ORDER`), and **`response_match_score: 0.8`** (ROUGE-1 on the final text). The missing `lookup_order` call drives the trajectory score below `1.0`, so the case **fails** even though the response would probably pass.
  - This is the **Lucky Hallucination** pattern from Day 1. Note that the curriculum's [setting_the_bar.md](../Notes/Day_1/setting_the_bar.md) recommends a *relaxed, explicitly configured* `0.8` / `0.5` bar in `test_config.json`. Those are **not** the framework defaults.
  - *Distractor B* is partly true: `response_match_score` does use ROUGE-1, but it never looks at tool calls. *Distractors A and D* are false.
- **Official Source**: [ADK Evaluate](https://adk.dev/evaluate/) · [`eval_config.py`](https://raw.githubusercontent.com/google/adk-python/main/src/google/adk/evaluation/eval_config.py) — *"tool_trajectory_avg_score: Defaults to 1.0, requiring a 100% match in the tool usage trajectory."*
- **Curriculum Source Links**: [trajectory_vs_response.md](../Notes/Day_1/trajectory_vs_response.md), [anatomy_of_an_eval_case.md](../Notes/Day_1/anatomy_of_an_eval_case.md), [what_is_adk_eval.md](../Notes/Day_1/what_is_adk_eval.md), [setting_the_bar.md](../Notes/Day_1/setting_the_bar.md)

### Part D Answer Key: Model Serving, Caching & Routing

#### Q24 — Provisioned Throughput — Documented Limitation
- **Correct Answer**: **E**
- **Why It Is Correct & Why Distractors Fail**:
  - Provisioned Throughput (PT) does **not** cover batch prediction, and it does **not** guarantee capacity for calls that other platform products (for example Agent Search) make to the same model.
  - *Distractor D* is false: terms are **1 week, 1 month, 3 months, and 1 year**. *Distractor B* is false: supervised fine-tuned endpoints and their base model **share** the same PT quota, and from Gemini 3 onward tuned-model inference uses capacity faster. *Distractors A and C* are false.
- **Official Source**: [Provisioned Throughput — supported models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/supported-models) · [Purchase Provisioned Throughput](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/provisioned-throughput/purchase-provisioned-throughput) — *"your Provisioned Throughput order for Gemini 3.5 Flash won't guarantee the calls made by Agent Search. Provisioned Throughput doesn't support batch prediction calls."*
- **Curriculum Source Links**: [foundation_model_consumption_options.md](../Notes/Day_5/foundation_model_consumption_options.md), [choosing_the_right_consumption_option.md](../Notes/Day_5/choosing_the_right_consumption_option.md)

#### Q27 — Context Caching Minimum Input Tokens
- **Correct Answer**: **B**
- **Why It Is Correct & Why Distractors Fail**:
  - The minimum is **model-specific**, and option B's numbers match the Gemini API table exactly:

    | Platform | Model(s) | Minimum Input Tokens |
    | :--- | :--- | :---: |
    | Gemini API | Gemini 2.5 Flash, 2.5 Pro | **2,048** |
    | Gemini API | Gemini 3.5 / 3.6 / 3.7 / 3.8 Flash, 3.1 Pro Preview | **4,096** |
    | Gemini Enterprise Agent Platform | Gemini 2 family | **2,048** |
    | Gemini Enterprise Agent Platform | Gemini 3 family | **4,096** |
    | Gemini Enterprise Agent Platform | 3.0 Flash Preview, 3.1 Pro Preview, 3.7 Flash, 3.8 Flash (**implicit only**) | **6,144** |

  - *Distractor D* is false: both platforms apply minimums to implicit caching. *Distractor C* (1,000,000 tokens) is roughly the size of a whole context window, not a threshold. *Distractors A and E* are false.
  - **Exam trap**: The same model can have different minimums on the Gemini API and on Agent Platform. Read which API the question names.
- **Official Source**: [Gemini API — Context caching](https://ai.google.dev/gemini-api/docs/caching) · [Agent Platform — Context cache overview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview) — *"The minimum input token count for context caching is listed in the following table for each model: … Gemini 3.7 Flash 4,096 … Gemini 2.5 Flash 2,048"*
- **Curriculum Source Links**: [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md)

#### Q28 — The Cost Argument for Semantic Routing
- **Correct Answer**: **B**
- **Why It Is Correct & Why Distractors Fail**:
  - Google's Architecture Center recommends routing simple requests to a small model and reserving the expensive model for complex reasoning. The price gap is large:

    | Comparison (Gemini API, per 1M tokens, input / output) | Pro | Flash-Lite | Gap |
    | :--- | :---: | :---: | :---: |
    | Gemini 3.1 Pro Preview vs. 3.1 Flash-Lite | $2.00 / $12.00 | $0.25 / $1.50 | ~8× |
    | Gemini 2.5 Pro vs. 2.5 Flash-Lite | $1.25 / $10.00 | $0.10 / $0.40 | 12.5× / 25× |

  - *Distractor C* is partly true: a router adds *some* overhead, but a semantic router uses embeddings (about 5 ms) or a small model, not "a full, expensive LLM call". *Distractors A, D, and E* are false.
- **Official Source**: [Choose agentic AI architecture components](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components) · [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) — *"route simple requests to a small language model (SLM) … and reserve a more powerful and expensive model for complex reasoning … create a cost-effective system that maintains high performance."*
- **Curriculum Source Links**: [model_routing_semantic_router_tiers.md](../Notes/Day_5/model_routing_semantic_router_tiers.md), [routing_patterns_rule_llm_semantic.md](../Notes/Day_5/routing_patterns_rule_llm_semantic.md)

---

## Section 4: Curriculum Gaps & Corrections Triggered by This Review

### 4.1 Topics Missing or Incomplete in `Notes/`

| Topic | Question | Status | Where It Should Live |
| :--- | :---: | :---: | :--- |
| Model Armor document screening file types | Q12 | Missing | `Notes/Day_2` (Model Armor) |
| CSAM filter always on; the 4 configurable RAI categories | Q14 | Missing | `Notes/Day_2` (Model Armor) |
| Model Armor protects apps on any cloud | Q15 | Missing | `Notes/Day_2` (Model Armor) |
| CodeMender `--model` flag and default model | Q16 | Missing | `Notes/Day_3` + `docs/CLI_AND_SDK_CHEATSHEET.md` |
| Agent Gateway (ingress + egress, Model Armor inline) | Q17 | Missing | `Notes/Day_4` (Agent Platform runtime) |
| CodeMender LLM-as-a-judge + human approval gate | Q18 | Partial | `Notes/Day_3` (CodeMender) |
| CodeMender hosted reasoning vs. local execution split | Q19 | Partial | `Notes/Day_3` (CodeMender) |
| Agent Identifier (URN) vs. Agent Principal (IAM) | Q20 | Partial | `Notes/Day_4` (Agent Registry / Identity) |
| `DatabaseSessionService` and the full implementation list | Q22 | Partial | `Notes/Day_1` / `Notes/Day_4` (Sessions) |
| PT limitations (no batch; other products not covered; terms) | Q24 | Partial | `Notes/Day_5` (Consumption tiers) |
| Per-model context-caching minimums | Q27 | Was outdated | `Notes/Day_5` (Caching), corrected below |
| `run_async()` events: `partial`, tool events, `EventActions`, confirmations | Q29 | Missing | `Notes/Day_4` (Runner / Events) |

### 4.2 Outdated Repository Facts Corrected

| Claim Previously in the Repository | Grounded Fact (2026-10-07) | Files Corrected |
| :--- | :--- | :--- |
| Context caching minimum is "typically `>= 32k` tokens" | Model-specific: `2,048` (Gemini 2.5) / `4,096` (Gemini 3.x) on the Gemini API; up to `6,144` for some 3.x Flash models on Agent Platform | [STUDY_GUIDE.md](STUDY_GUIDE.md), [PRACTICE_EXAM_50Q.md](PRACTICE_EXAM_50Q.md) (Q51, Q52), [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md) |
| `0.8` / `0.5` described as the "default" / "standard" `adk eval` thresholds, and `1.0` described as "impossible" | ADK built-in defaults are `tool_trajectory_avg_score: 1.0` (`EXACT`) and `response_match_score: 0.8`; `0.8` / `0.5` is the curriculum's recommended, explicitly configured bar | [STUDY_GUIDE.md](STUDY_GUIDE.md), [PRACTICE_EXAM_50Q.md](PRACTICE_EXAM_50Q.md) (Q9) |

---

## Navigation & Next Steps

- [55-Question Practice Knowledge Check](PRACTICE_EXAM_50Q.md)
- [Elevate Exam Study Guide & Cram Sheet](STUDY_GUIDE.md)
- [Master Technical Synthesis](MASTER_SYNTHESIS.md)
- [CE & DBCE Architecture Decision Playbook](CE_PLAYBOOK.md)
- [CLI & Python SDK Quick-Reference Cheat Sheet](CLI_AND_SDK_CHEATSHEET.md)
- [Master Curriculum Index](../Notes/README.md)
- [Repository Root Hub](../README.md)
