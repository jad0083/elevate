# Architecture Policy: External (Antigravity) vs. Internal (JetSki) Code Sharing

![EXTERNAL vs INTERNAL Code Sharing](assets/external_vs_internal_code_sharing_policy.png)

## Overview

To protect Google proprietary intellectual property (IP) and ensure safe customer demonstrations, Google enforces a strict data flow boundary between **External (Antigravity)** and **Internal (JetSki)** development pathways.

---

## The Core Intent Rule

| Path | Primary Engineer Intent | Approved Tooling |
| :--- | :--- | :--- |
| **EXTERNAL** | • *"I want to experience or demo what our customers use."*<br/>• *"I want to share code or artifacts externally."* | **Antigravity** (Desktop & CLI) |
| **INTERNAL** | • *"I want to reduce toilsome Google-internal work."*<br/>• *"I want to contribute to Google3 code."* | **JetSki** (Cloudtop / gLinux) |

---

## Approved vs. Banned Data Flows

```mermaid
graph TD
    subgraph External Domain [EXTERNAL DOMAIN]
        AG["🚀 Antigravity"]
        Argolis["🏢 Argolis Demo Org"]
        GTM["🐙 GTM GitHub"]
        Policy["📜 go/ce-customer-code-sharing"]
        Customer["👥 Customer / External Audience"]
        
        AG ==>|✅ Approved| Argolis
        AG ==>|✅ Approved| GTM
        GTM --> Policy --> Customer
    end

    subgraph Internal Domain [INTERNAL GOOGLE DOMAIN]
        JS["⛵ JetSki (Cloudtop)"]
        G3["📦 Google3 Monorepo"]
        
        JS ==>|✅ Approved| G3
    end

    %% Banned / Risky Cross-Border Flows
    AG -.->|❌ BANNED| G3
    JS -.->|❌ BANNED| Argolis
    JS -.->|❌ BANNED| GTM
    JS -.->|❌ BANNED| Customer

    style AG fill:#e8f0fe,stroke:#4285f4,stroke-width:2px;
    style JS fill:#fce8e6,stroke:#ea4335,stroke-width:2px;
    style G3 fill:#e6f4ea,stroke:#34a853,stroke-width:2px;
```

---

## Strict Policy Guardrails

### 1. External Code Sharing Workflow (Green Path ✅)
When developing customer-facing code, demos, or partner solutions:
1. **Engine**: Use **Antigravity** (Desktop app or CLI).
2. **Environment**: Deploy into **Argolis** demo organizations.
3. **Repository**: Push code exclusively to **GTM GitHub** repositories.
4. **Governance**: Ensure all code shared externally complies with the review rules at [`go/ce-customer-code-sharing`](https://go/ce-customer-code-sharing).

### 2. Internal Engineering Workflow (Green Path ✅)
When developing internal tooling or reducing operational toil:
1. **Engine**: Use **JetSki** hosted remotely on your **Cloudtop** (`gLinux`) workstation.
2. **Repository**: Read and write directly to `google3` via Piper, CitC, and Fig.
3. **Internal Tools**: Integrate with Critique, Buganizer, and Moma.

### 3. Banned & Risky Cross-Border Interactions (Red Path ❌)
* **Never use JetSki to push code to GitHub or send files directly to customers.**
* **Never point JetSki at Argolis demo environments.**
* **Never point Antigravity directly at the internal `google3` codebase.**

---

## Policy Compliance Matrix

| Surface / Flow | Allowed Target | Prohibited Target | Compliance Link |
| :--- | :--- | :--- | :--- |
| **Antigravity** | • Argolis demo tenants<br/>• GTM GitHub<br/>• Local test projects | • `google3`<br/>• Internal Piper workspaces | `go/antigravity` |
| **JetSki (Cloudtop)** | • `google3`<br/>• Internal Piper/CitC<br/>• Buganizer / Critique | • Customers<br/>• Public GitHub<br/>• Argolis | `go/jetski` |
| **Customer Code Sharing** | • GTM GitHub repositories vetted via compliance | • Direct unvetted script transfers from Cloudtop | [`go/ce-customer-code-sharing`](https://go/ce-customer-code-sharing) |
