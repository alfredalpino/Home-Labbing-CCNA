# Roadmap & Curriculum

## Canonical spine

**Spine = [roadmap.sh Network Engineer](https://roadmap.sh/network-engineer).**

Everything else is either a **graft** (allowed, network-scoped) or a **drop** (forbidden in Month 1).

Daily rhythm: **~6h lab / 2h docs / 1h applications**.

Proof bias: **labs + GitHub > more certs**. Portfolio: update Candidate → certified; ship public lab monorepo; **do not redesign UI**.

---

## Keep / Graft / Drop

### KEEP (spine)

| Track | Rule |
|-------|------|
| roadmap.sh **Network Engineer** | Primary curriculum. Week plans map to this spine. |

### GRAFT (Month 1 — only as network-relevant slices)

| Graft | How to use |
|-------|------------|
| Linux networking | Interfaces, routes, ss/tcpdump, iptables/nft basics — support labs |
| Bash | Lab automation, verify scripts, ticket-style runbooks |
| Cyber (network slice) | ACL, hardening, threat-aware edge — not full security career |
| Terraform networking | Azure VNet/peering/NSG as code for LAB-05 |
| Docker basics | Lab tooling / lightweight service deps — not platform engineering |
| Cloudflare DNS / Tunnel / WAF edge | DNS + edge exposure patterns — graft into docs/labs, not a Cloudflare-only career |

### DROP (Month 1 — binding)

Do **not** spend Month-1 time on:

| Drop | Why |
|------|-----|
| Design System | Not network-ops proof |
| Software Architect | Wrong north star |
| DSA deep / LeetCode grind | Not NOC hiring signal for this plan |
| CS full (generic CS degree track) | Degree may be incomplete; lead with certs+labs |
| PostgreSQL DBA | Off-spine |
| Technical Writer (as career) | Docs for labs yes; writer career no |
| Prompt Engineering (as career) | AI is a tool, not the path |
| AI Red Team | Off-spine |
| Code Review (as career track) | Off-spine |
| API Security career | Security graft only via network ACLs/edge |
| Full Kubernetes | Graft Docker basics only |
| Full DevOps | Automation for network labs only |
| AWS deep | Azure networking graft only (AZ-104 already in pack) |

If a suggestion conflicts with DROP, refuse it and redirect to the spine + current week lab.

---

## Month 1 — week by week

| Week | Focus | Labs | Notes |
|------|-------|------|-------|
| **W1** | Deep L2/L3 | LAB-01, LAB-02 | VLANs, trunks, inter-VLAN; OSPF single-area |
| **W2** | Security + edge ops | LAB-03, LAB-04 | ISP edge playbook; ACL/security hardening |
| **W3** | Azure hybrid + IaC | LAB-05 | Hybrid networking concepts + Terraform networking |
| **W4** | Automation + applications | LAB-06 | Bash/Python ops automation; push apps hard |

Each week still includes **docs** (2h/day) and **applications** (1h/day). W4 intensifies applications but does not pause lab quality.

---

## Labs LAB-01 … LAB-06

Status values: `Queued` | `In progress` | `Done (public)`.

### LAB-01 — VLAN Segmentation

| Field | Detail |
|-------|--------|
| Status | In progress (ship to public) |
| Stack | Packet Tracer (multi-switch) |
| Goals | Access vs trunk; VLAN design; inter-VLAN routing; intentional failure cases; recovery notes |
| Proof | Topology diagram, configs, verify commands, failure/recovery write-up in monorepo |

### LAB-02 — OSPF Single-Area

| Field | Detail |
|-------|--------|
| Status | In progress (ship to public) |
| Stack | Packet Tracer / lab routers |
| Goals | Adjacency formation; LSDB verification; path selection in a small routed domain |
| Proof | Show/verify outputs, adjacency troubleshooting notes, config set |

### LAB-03 — ISP Edge Playbook

| Field | Detail |
|-------|--------|
| Status | Queued |
| Stack | Packet Tracer + runbook markdown |
| Goals | L1/L2 isolation → CPE checks → upstream escalation loop (**Tikona-style triage**) |
| Proof | Decision tree / playbook; example ticket notes; escalation hygiene checklist |

### LAB-04 — ACL & Network Security Hardening

| Field | Detail |
|-------|--------|
| Status | Queued |
| Stack | Packet Tracer + Security+ concepts applied |
| Goals | Standard/extended ACLs; place correctly; verify permit/deny; document blast radius |
| Proof | Before/after traffic tests; ACL rationale; common misconfig traps |

### LAB-05 — Azure Hybrid Networking + Terraform

| Field | Detail |
|-------|--------|
| Status | Queued |
| Stack | Azure networking + Terraform |
| Goals | VNet patterns / hybrid connectivity concepts; NSG mindset; Terraform for networking resources |
| Proof | `.tf` + apply notes + architecture diagram; no fake production claims |

### LAB-06 — Network Ops Automation

| Field | Detail |
|-------|--------|
| Status | Queued |
| Stack | Bash + Python |
| Goals | Automate verification / parsing / repetitive ops checks from earlier labs |
| Proof | Scripts + README + sample output; idempotent where sensible |

---

## Lab definition of done (all labs)

A lab is **not done** until all are true:

1. Public in the GitHub monorepo
2. README: objective, topology, steps, verify, failure cases, recovery
3. Configs or code committed (no “screenshots only”)
4. One “ticket story” paragraph (how this maps to a real incident)
5. Linked from portfolio **without** a UI redesign

---

## Mapping spine → Month 1

| Spine theme (Network Engineer) | Month-1 home |
|--------------------------------|--------------|
| Switching / VLANs / STP foundations | W1 / LAB-01 |
| IP, subnetting, static, OSPF | W1 / LAB-02 |
| ACLs / security basics | W2 / LAB-04 |
| Ops / troubleshooting / ISP edge | W2 / LAB-03 |
| Cloud networking (Azure) | W3 / LAB-05 |
| Automation | W4 / LAB-06 |
| Linux / Bash / Docker / Cloudflare / Terraform | Grafts across W1–W4 — never replace spine |

---

## After Month 1 (pointer only)

Stay on the Network Engineer spine. Deepen labs, polish interview stories, continue GCC applications. Do not unlock DROP list just because Month 1 ended — re-evaluate grafts deliberately in `02` 90-day review.
