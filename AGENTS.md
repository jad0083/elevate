# AGENTS.md — Operational Invariants for the Elevate Repository

> *"The model is not the variable you control. The context is."*
> — [Day 2: The First Law of Agent Engineering](Notes/Day_2/the_model_is_not_the_variable_you_control.md)

This file defines the persistent operational rules, structural invariants, and verification commands for autonomous coding and research agents working in the `elevate` repository.

---

## 1. Repository Architecture & Four-File Contract

This repository follows the [Four Files, Four Audiences](Notes/Day_2/four_files_four_audiences.md) specification pattern:

- [`README.md`](README.md) — **Human-Centric Project Hub**: Executive overview, 5-day curriculum architecture, topic index, and navigation entry point.
- [`AGENTS.md`](AGENTS.md) — **Machine-Centric Repository Physics**: Persistent rules, directory invariants, note authoring conventions, and verification gates.
- [`.gemini/skills/elevate-curriculum/SKILL.md`](.gemini/skills/elevate-curriculum/SKILL.md) — **Workspace Capability Skill**: Progressive-disclosure instructions for searching, synthesizing, and extending the Elevate knowledge base.
- [`docs/`](docs/) — **Cross-Curriculum Playbooks & Reference Guides**:
    - [`docs/MASTER_SYNTHESIS.md`](docs/MASTER_SYNTHESIS.md): End-to-end 5-day technical synthesis with links to underlying notes.
    - [`docs/CE_PLAYBOOK.md`](docs/CE_PLAYBOOK.md): Actionable decision matrices and architectural guidance for Google Cloud Customer Engineers (CE / DBCE).
    - [`docs/CLI_AND_SDK_CHEATSHEET.md`](docs/CLI_AND_SDK_CHEATSHEET.md): Consolidated command-line (`adk`, `agents-cli`, `agy`, `cm`, `gcloud`) and Python SDK (`google.adk`, `google.genai`) recipes.
- [`Notes/`](Notes/README.md) — **Primary 5-Day Curriculum Corpus**:
    - [`Notes/Day_1/`](Notes/Day_1/README.md): Foundations, Grounding/RAG, OKF, Google ADK 4 Pillars, Multi-Agent Research, ADK Eval, Cloud Deployment (`106` topic notes, `105` slide assets).
    - [`Notes/Day_2/`](Notes/Day_2/README.md): Antigravity 2.0 Surfaces, Skills Architecture, Context Engineering (`C = P + M`), Spec-Driven Development, Enterprise Modernization (Mainframe, .NET, Databases), Governed MCP, WIF/STS, Wiz AI-APP (`87` topic notes, `87` slide assets).
    - [`Notes/Day_3/`](Notes/Day_3/README.md): Machine-Speed Security, Adversarial AI, Shift-Left Co-Pilots & Shift-Right Runtime Defense, Wiz 5-Phase AI DAST Funnel, CodeMender (`24` topic notes, `24` slide assets).
    - [`Notes/Day_4/`](Notes/Day_4/README.md): Google ADK 2.0 `StateGraph`, 6 Lifecycle Callbacks, Vertex AI Memory Bank, A2A Protocol vs. MCP, SPIFFE Dual-Gate Identity, 7 Evaluation Dimensions & 8 Methodologies, Harness Engineering, MCP Toolbox for Databases, Vector DB Topologies (`31` topic notes, `34` slide assets).
    - [`Notes/Day_5/`](Notes/Day_5/README.md): Enterprise Model Serving & Cost Economics (5 Vertex AI Consumption Tiers, Implicit vs. Explicit Context Caching, 3-Stage Cascading Semantic Router) & Capstone (`5` topic notes, `5` slide assets; active).
- [`scripts/verify_repo.py`](scripts/verify_repo.py) — **Deterministic Verification Gate**: Validates markdown links, image embeds, index completeness, PNG headers, and code fence balance.

---

## 2. Invariants & Authoring Rules

1. **Preserve `Notes/Day_N/` Paths**:
    - Never rename or move existing files under `Notes/Day_1/` through `Notes/Day_5/` without updating all incoming references and preserving compatibility with laptop `rsync` workflows.
2. **Read Before Edit**:
    - Always read the target `.md` file and its corresponding `Notes/Day_N/README.md` section before making edits.
3. **Standard Topic Note Structure**:
    - Every curriculum topic note in `Notes/Day_N/<slug>.md` must include:
        1. H1 title (`# ...`)
        2. Embedded slide asset (`![...](assets/<slug>.png)`) on line 3
        3. `## Overview` section
        4. At least one Mermaid architecture diagram (` ```mermaid `) or code block
        5. Detailed technical breakdown and a summary comparison table
    - Every new topic note must be indexed in its parent `Notes/Day_N/README.md`.
4. **Zero Broken Links or Orphaned Assets**:
    - Every relative link `[...](...)` and image reference `![...](...)` outside code blocks must resolve to an existing file on disk.
    - Every `.png` in `Notes/Day_N/assets/` must be referenced by at least one `.md` note in `Notes/Day_N/`.
5. **Security & Credential Hygiene**:
    - Never commit real API keys, OAuth tokens, service account JSONs, or internal-only URLs/code prohibited by `go/ce-customer-code-sharing`.
    - `git secrets` pre-commit hooks are enforced on this repository.

---

## 3. Mandatory Verification Protocol

Before claiming any task is complete or creating a commit, run the repository verification suite and confirm a zero-error exit code:

```bash
python3 scripts/verify_repo.py
```
