# Google ADK: File-Based Skill Deep Dive & Demo Implementation

![Common Skill Patterns](assets/common_skill_patterns.png)

## Overview

A **File-Based Skill** is the canonical production pattern for packaging capabilities in Google ADK. It lives on disk as a folder containing a standardized `SKILL.md` specification alongside optional helper scripts, templates, and reference manuals—version-controlled in Git directly alongside your agent codebase.

---

## Directory Anatomy of a File-Based Skill

```text
my-agent-project/
├── main.py
├── agent.py
└── skills/
    └── bigquery_optimizer/
        ├── SKILL.md                 # 📄 L1 Metadata + L2 Operational Instructions
        ├── scripts/                 # ⚙️ L3 Deterministic Helper Scripts
        │   └── estimate_cost.py     # Fast dry-run SQL cost calculator
        ├── references/              # 📚 L3 Deep Domain Documentation
        │   └── partition_rules.md   # Organizational partition/cluster policies
        └── resources/               # 📊 L3 Query Templates & Schemas
            └── golden_queries.sql   # Few-shot optimized query examples
```

---

## 1. The Specification: `SKILL.md`

```markdown
---
name: bigquery_optimizer
description: Analyzes SQL queries for BigQuery best practices, estimates scan costs, and suggests partitioning/clustering keys.
version: 1.0.0
tools:
  - execute_dry_run_cost_estimation
---

# BigQuery Optimizer Skill

## When to Use
Activate this skill whenever the user asks to write, optimize, debug, or evaluate a Google Cloud BigQuery SQL query.

## Operating Procedures
1. **Analyze Schema**: Inspect table definitions using `references/partition_rules.md`.
2. **Dry Run Validation**: Before executing any expensive query, run `scripts/estimate_cost.py` to calculate projected byte scan volume.
3. **Partition & Cluster Enforcement**:
   - Always filter on `_PARTITIONTIME` or date partitioning columns in `WHERE` clauses.
   - Avoid `SELECT *`; explicitly name required columns.
4. **Output Format**: Provide the optimized query along with estimated savings in scan cost.
```

---

## 2. The Deterministic Script: `scripts/estimate_cost.py`

```python
import sys
from google.cloud import bigquery

def estimate_query_cost(sql_query: str) -> dict:
    client = bigquery.Client()
    job_config = bigquery.QueryJobConfig(dry_run=True, use_query_cache=False)
    
    query_job = client.query(sql_query, job_config=job_config)
    bytes_scanned = query_job.total_bytes_processed
    cost_usd = (bytes_scanned / (1024 ** 4)) * 6.25  # $6.25 per TB on-demand
    
    return {
        "bytes_scanned": bytes_scanned,
        "gigabytes_scanned": round(bytes_scanned / (1024 ** 3), 2),
        "estimated_cost_usd": round(cost_usd, 4),
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(estimate_query_cost(sys.argv[1]))
```

---

## 3. Loading the Skill in Google ADK Python

```python
from google.adk.agents import Agent
from google.adk.skills import FileBasedSkillLoader

# 1. Initialize the Skill Loader pointing to the local skills directory
skill_loader = FileBasedSkillLoader(skills_dir="./skills")

# 2. Instantiate the Base Agent with dynamic skill discovery
agent = Agent(
    name="data_engineer_copilot",
    model="gemini-2.0-flash",
    instruction="You are an expert Data Engineer assistant. Use your available skills to optimize customer queries.",
    skills=skill_loader.discover_skills(), # Loads L1 metadata menus
)

# 3. Execution: When a user query arrives, ADK dynamically loads L2 instructions & L3 resources
response = agent.run("Please optimize this query: SELECT * FROM `analytics.events` WHERE date > '2026-01-01'")
print(response.content)
```

---

## Why the File-Based Pattern Excels

1. **GitOps Versioning**: Every prompt change, script fix, and rule update is tracked via standard Git commits and pull requests.
2. **Local IDE Ergonomics**: Engineers can edit markdown files, run unit tests against `scripts/`, and format files with standard developer tools.
3. **Decoupled Architecture**: Adding a new skill requires zero changes to `main.py`—simply create a new directory inside `skills/`.
