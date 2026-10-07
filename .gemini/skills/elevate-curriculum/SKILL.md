---
name: elevate-curriculum
description: >-
  Navigates, synthesizes, audits, and extends the 5-Day Elevate Agent
  Engineering Curriculum knowledge base (Google ADK 1.x/2.0, Antigravity 2.0,
  Context Engineering, Open Knowledge Format, Enterprise Modernization, Governed
  MCP, SPIFFE Dual-Gate IAM, Wiz AI-APP, CodeMender, A2A Protocol, Agent
  Evaluation, and Vertex AI Serving/FinOps). Use when answering architecture
  questions, preparing customer guidance, adding new session notes or slide
  captures, or verifying repository link and asset integrity.
---

# Elevate Curriculum Workspace Skill

## 1. Progressive Disclosure Routing Map

Follow the [3-Level Progressive Disclosure](../../../Notes/Day_2/progressive_disclosure_when_how_what.md) pattern to minimize token usage:

1. **Cross-Curriculum Syntheses & Playbooks (`docs/`)**:
   - [`docs/MASTER_SYNTHESIS.md`](../../../docs/MASTER_SYNTHESIS.md): Complete 5-day technical synthesis with direct links to all topic notes.
   - [`docs/CE_PLAYBOOK.md`](../../../docs/CE_PLAYBOOK.md): Customer Engineering & DBCE decision matrices (Multi-Agent sizing, OKF + MCP Toolbox for Databases, Vector DB selection, Mainframe/.NET/DB modernization, WIF+SCIM vs. Cloud Identity, 4-Layer MCP Security, and Vertex AI FinOps).
   - [`docs/CLI_AND_SDK_CHEATSHEET.md`](../../../docs/CLI_AND_SDK_CHEATSHEET.md): CLI commands (`agents-cli`, `adk`, `gcloud`, `cm`) and Python SDK snippets (`google.adk`, `google.genai`).
2. **Daily Master Indexes (`Notes/Day_N/README.md`)**:
   - [`Notes/Day_1/README.md`](../../../Notes/Day_1/README.md): Foundations, 2-Stage RAG, OKF, ADK 4 Pillars, 180-Config Multi-Agent Study, Golden Dataset Eval, Cloud Run / Agent Runtime (`106` topic notes).
   - [`Notes/Day_2/README.md`](../../../Notes/Day_2/README.md): Antigravity 2.0 Surfaces, Skills Architecture, Context Engineering (`C = P + M`), Spec-Driven Development, Enterprise Modernization (Mainframe, .NET, DBs), Governed MCP, WIF/STS, Wiz AI-APP (`87` topic notes).
   - [`Notes/Day_3/README.md`](../../../Notes/Day_3/README.md): Machine-Speed AppSec, Adversarial AI Case Studies, Shift-Left Co-Pilots & Shift-Right Runtime Sensors, Wiz 5-Phase AI DAST Funnel, CodeMender (`24` topic notes).
   - [`Notes/Day_4/README.md`](../../../Notes/Day_4/README.md): ADK 2.0 `StateGraph`, 6 Lifecycle Callbacks, Vertex AI Memory Bank, A2A vs. MCP, SPIFFE Dual-Gate Identity, 7 Evaluation Dimensions & 8 Methodologies, Harness Engineering, MCP Toolbox for Databases, Vector DB Topologies (`31` topic notes).
   - [`Notes/Day_5/README.md`](../../../Notes/Day_5/README.md): Vertex AI Consumption Tiers (PT + PayGo Spillover vs. Flex/Batch), Implicit vs. Explicit Context Caching, 3-Stage Semantic Router, and Production Capstone (`5` topic notes).

## 2. Adding or Updating Session Notes

1. Place the slide screenshot in `Notes/Day_N/assets/<slug>.png`.
2. Create `Notes/Day_N/<slug>.md` with:
   - `# <Title>`
   - `![<Alt Text>](assets/<slug>.png)` on line 3
   - `## Overview`
   - Architecture diagram (` ```mermaid `) and technical breakdown sections
   - Summary reference table
3. Add the note entry to the appropriate section in `Notes/Day_N/README.md` (and update note counts in `README.md` and `Notes/README.md` if applicable).
4. Run the deterministic verification suite before committing:
   ```bash
   python3 scripts/verify_repo.py
   ```
