---
tags: [network-types, networking, ccna, cloud]
aliases: [Cloud Network, Cloud Computing Network]
layer: Delivery / architecture model
---

# Cloud

## Learning objectives

- Define cloud as on-demand shared infrastructure reached over networks
- Map cloud to your LAN/WAN edge (Internet, Direct Connect, [[VPN]])
- Contrast public / private / hybrid at a networking level
- Avoid “cloud is magic servers in the sky” thinking

## One-sentence definition

> In networking terms, **cloud** means compute, storage, and services hosted in provider data centers that you reach as remote destinations — usually over the Internet or private WAN on-ramps — with elastic, API-driven provisioning.

## Analogy

> Instead of owning a **power generator in your basement** (on‑prem servers), you plug into the **city power grid** (cloud provider). You still need good wiring in your house ([[LAN]]), a meter/connection to the grid ([[WAN]] / interconnect), and breakers (firewalls/security groups). The electricity isn’t “local LAN”; it’s a remote utility you rent.

## Why it matters

Apps you troubleshoot often terminate in AWS/Azure/GCP. Paths include public Internet, [[VPN]], or dedicated circuits. Addressing, DNS, and latency budgets change. CCNA-level engineers must speak cloud *paths* even before specializing in cloud networking.

## Deep dive

### Mental model

```text
User / Office LAN ── Edge router ── Internet or private interconnect ── Cloud VPC/VNet ── App
```

### Networking-relevant cloud ideas

| Idea | Meaning |
|------|---------|
| Region / AZ | Geographic failure domains |
| VPC/VNet | Your private IP space in cloud |
| Security groups / NSG | Stateful filters near NICs |
| Load balancers | Cloud [[Server]] front doors |
| Hybrid | On‑prem + cloud via VPN/Direct Connect |

### Cloud vs “someone else’s server”

Cloud adds **APIs, elasticity, shared responsibility**. From a packet’s view: still IP to a remote [[LAN]] that you don’t physically touch.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Delivery model | Cross-layer | Where workloads live |
| Path | L3 across [[WAN]] | Reachability & policy |

## Lab exercises

### Lab 1 — Trace to a cloud front door

```bash
dig www.google.com +short
traceroute -n $(dig www.google.com +short | head -1)
```

### Lab 2 — Responsibility chart

Pick “patch the OS” vs “power/cooling” vs “IAM” — who owns what in public cloud? (shared responsibility)

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| App down, Internet OK | Cloud region / SG / DNS | provider status, security group, name |
| Hybrid path down | VPN/interconnect | tunnel state, BGP if used |
| Slow only to cloud | Path/peer congestion | RTT, CDN vs origin |

## Common traps / interview gotchas

- Cloud resources still need routes, DNS, and allow-lists — “it’s in the cloud” isn’t a root cause.
- Public IP ≠ secure; private connectivity ≠ automatically compliant.
- Egress costs and NAT gateways are design constraints, not footnotes.

## Mastery checklist

- [ ] Define cloud in network-path language
- [ ] Draw office → Internet/VPN → VPC → app
- [ ] Contrast public vs hybrid connectivity
- [ ] Use the utility-grid analogy cleanly

## Related notes

- [[WAN]] · [[VPN]] · [[LAN]] · [[DNS]] · [[HTTP-HTTPS]] · [[Routers]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
