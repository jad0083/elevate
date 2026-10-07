# Elevate CLI & Python SDK Quick-Reference Cheat Sheet

Consolidated command-line workflows and production Python code patterns across Days 1–5.

---

## 1. Google Agents CLI (`agents-cli`) & ADK CLI (`adk`)

Sources: [google_agents_cli_commands.md](../Notes/Day_1/google_agents_cli_commands.md), [adk_run_evaluation.md](../Notes/Day_1/adk_run_evaluation.md), [one_command_per_target.md](../Notes/Day_1/one_command_per_target.md), [agents_cli_core_commands_reference.md](../Notes/Day_4/agents_cli_core_commands_reference.md)

```bash
# 1. Bootstrap CLI, GCP ADC, and inject the 7 bundled skills into Antigravity
agents-cli setup --ide antigravity --inject-skills

# 2. Scaffold a new production agent project (templates: adk | adk_a2a | agentic_rag | chat | workflow | rag)
agents-cli scaffold my-agent --template workflow --target agent-runtime

# 3. Run fast local interactive inner-loop testing with tool call inspection
agents-cli run "Check inventory for SKU-992" --interactive --verbose-tools

# 4. Run Golden Dataset trajectory + response evaluations (ADK CLI & Agents CLI)
uv run adk eval customer_service_agent \
    customer_service_agent/eval.test.json \
    --config_file_path=customer_service_agent/test_config.json \
    --print_detailed_results

agents-cli eval run --dataset eval/golden_dataset.json --judge-model gemini-2.5-pro

# 5. Run CI/CD evaluation gate via Pytest
uv run pytest tests/test_eval.py

# 6. Provision single-project Terraform IaC (Cloud Run, Firestore, Artifact Registry, Secret Manager, IAM)
agents-cli infra single-project --project-id $PROJECT_ID --region us-central1

# 7. Deploy same agent code to Agent Runtime, Cloud Run (with externalized state), or GKE
adk deploy agent_engine --project=$PROJECT_ID --region=us-central1 app
adk deploy cloud_run --project=$PROJECT_ID --region=us-central1 --agent_engine_id=$ENGINE_ID app
agents-cli deploy --target gke --service-account agent-runner@$PROJECT_ID.iam.gserviceaccount.com

# 8. Publish A2A Agent Card (/.well-known/agent.json) to Gemini Enterprise Catalog
agents-cli publish gemini-enterprise --display-name "Finance Assistant" --category finance
```

---

## 2. MCP Security, IAM Deny (CEL) & Model Armor CLI (`gcloud`)

Sources: [mcp_iam_deny_fine_grained_controls.md](../Notes/Day_2/mcp_iam_deny_fine_grained_controls.md), [google_mcp_server_model_armor.md](../Notes/Day_2/google_mcp_server_model_armor.md)

```bash
# Enforce org/project-wide Read-Only MCP guardrails via Cloud IAM Deny + CEL
# policy.json denyRule condition: api.getAttribute('mcp.googleapis.com/tool.isReadOnly', false) == false
gcloud iam policies create deny-read-write-tool-access-policy \
    --attachment-point=cloudresourcemanager.googleapis.com/projects/$PROJECT_ID \
    --kind=denypolicies \
    --policy-file=policy.json

# Configure Google Model Armor global floor settings for MCP & prompt injection defense
gcloud model-armor floorsettings update \
    --full-uri="projects/$PROJECT_ID/locations/global/floorSetting" \
    --mcp-sanitization=ENABLED \
    --malicious-uri-filter-settings-enforcement=ENABLED \
    --pi-and-jailbreak-filter-settings-enforcement=ENABLED \
    --pi-and-jailbreak-filter-settings-confidence-level=MEDIUM_AND_ABOVE
```

---

## 3. CodeMender Autonomous Vulnerability Remediation (`cm`)

Sources: [codemender_wiz_integration_architecture.md](../Notes/Day_3/codemender_wiz_integration_architecture.md), [codemender_ingest_from_third_party_scanners.md](../Notes/Day_3/codemender_ingest_from_third_party_scanners.md)

```bash
# 1. Ingest findings from Wiz Code, Snyk, Veracode, Checkmarx, or SARIF and verify PoC in sandbox
cm import --file findings_wiz.json

# 2. Synthesize differential AST fix, run unit test suite in sandbox, and open PR
cm fix --id CVE-2026-4011 --create-pr
```

---

## 4. Google ADK 2.0 & Gemini SDK Python Patterns

### A. Declarative ADK Agent with `PreloadMemoryTool` & Lifecycle Callbacks
Sources: [adk_framework_code_example_preload_memory_tools.md](../Notes/Day_4/adk_framework_code_example_preload_memory_tools.md), [adk_concepts_callbacks_lifecycle_hooks.md](../Notes/Day_4/adk_concepts_callbacks_lifecycle_hooks.md), [scenario_3_enterprise_guardrails_pii_redaction_auditing.md](../Notes/Day_4/scenario_3_enterprise_guardrails_pii_redaction_auditing.md)

```python
from google.adk import Agent
from google.adk.tools import PreloadMemoryTool, google_search
from google.adk.context import InvocationContext, ToolContext

def scrub_pii_before_model(context: InvocationContext, contents: list):
    """Scrub SSNs and credit card numbers before sending prompts to Gemini."""
    # Invoke Cloud DLP or regex redaction on contents
    return contents

def enforce_dual_gate_rbac(context: ToolContext, tool_name: str, tool_args: dict):
    """Block destructive database tools unless delegated caller holds admin role."""
    if tool_name == "execute_sql_delete" and "roles/database.admin" not in context.user_roles:
        raise PermissionError("Caller lacks roles/database.admin for destructive SQL execution.")

root_agent = Agent(
    name="enterprise_support_agent",
    model="gemini-2.5-pro",
    instruction="You are an enterprise support specialist. Ground all answers in verified tools.",
    tools=[PreloadMemoryTool(), google_search],
    before_model_callback=scrub_pii_before_model,
    before_tool_callback=enforce_dual_gate_rbac,
)
```

### B. Explicit Context Caching (`google.genai` SDK — 90% Token Discount)
Source: [gemini_context_caching_implicit_vs_explicit.md](../Notes/Day_5/gemini_context_caching_implicit_vs_explicit.md)

```python
from google import genai
from google.genai import types

client = genai.Client()

# Upload large shared reference corpus once with a 60-minute guaranteed TTL
cache = client.cached_contents.create(
    model="gemini-2.5-pro",
    config=types.CreateCachedContentConfig(
        contents=[large_repo_context, architecture_manual],
        system_instruction="You are a principal cloud architect.",
        ttl="3600s",
    ),
)

# Subsequent requests pass only the lightweight cache pointer
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="Audit the payment service retry topology against section 4 of the manual.",
    config=types.GenerateContentConfig(cached_content=cache.name),
)
```
