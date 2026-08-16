---
tags: [network-security, zero-trust, networking, ccna, architecture]
aliases: [Zero Trust, ZTA, Zero Trust Architecture]
layer: Security architecture
---

# Zero Trust Architecture

## Learning objectives

- Define Zero Trust as “never trust, always verify” — not a single product
- Contrast perimeter-only trust with identity/device/app-centric controls
- Map ZT ideas to VPN, ZTNA, microsegmentation, and continuous auth
- Avoid buzzword misuse in designs and interviews

## One-sentence definition

> **Zero Trust Architecture (ZTA)** is a security design approach that assumes **no implicit trust** based on network location — every access request is authenticated, authorized, and continuously evaluated against policy for that user/device/app/data.

## Analogy

> Old castle model: once you’re **inside the walls** ([[Firewalls]] perimeter), you’re mostly trusted. Zero Trust is an **airport + hotel keycard culture**: even after entering the building, every door re-checks who you are, whether your badge is still valid, which room you’re allowed into, and whether your behavior looks weird — *every time*, not once at the moat.

## Why it matters

Remote work, cloud, and lateral-movement ransomware broke “flat inside network = safe.” Network engineers increasingly build **segmentation**, identity-aware proxies, and least-privilege paths instead of big flat VLANs + fat VPN.

## Deep dive

### Mental model

```text
Request access → authenticate identity → check device posture → authorize least privilege
→ grant narrow path (often per-app) → log/monitor → re-evaluate continuously
```

### Pillars you’ll hear

| Pillar | Network-flavored meaning |
|--------|---------------------------|
| Identity | Who (user/workload) |
| Device trust | Posture, managed status |
| Least privilege | Microsegmentation, per-app access |
| Assume breach | Monitor east-west, limit blast radius |
| Continuous verification | Sessions aren’t forever trusted |

### Related technologies (not synonyms)

| Tech | Relationship to ZT |
|------|--------------------|
| [[VPN]] | Often still used; classic full-tunnel VPN alone ≠ ZT |
| ZTNA / SSE | App-level access brokers |
| Microsegmentation | Limit east-west in DC/cloud |
| [[Next-Generation Firewall]] | Enforcement point, not the whole architecture |
| MFA + IdP | Identity backbone |

### On the wire

May look like many small authenticated tunnels to brokers, not one flat “inside” subnet. East-west ACLs/SG tighten.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Architecture | Cross-layer + identity | Policy plane above packets |
| Enforcement | L3–L7 devices | Firewalls, brokers, agents |

## Lab exercises

### Lab 1 — Castle vs airport rewrite

Take your home lab diagram; list what becomes “verified per request” in a ZT mindset (admin SSH, app access, guest Wi‑Fi).

### Lab 2 — Blast radius

If one PC is malware-infected on a flat LAN, what can it reach? Design one segmentation improvement.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| User “on VPN” but app denied | ZT policy/posture | IdP, device compliance, app assignment |
| Lateral unexpected success | Flat segment remains | east-west ACL/SG |
| Too many breaks | Over-tight policy | phased rollout, logging |

## Common traps / interview gotchas

- Zero Trust is a **strategy**, not a SKU.
- Replacing VPN with marketing “ZT” that still yields flat access isn’t Zero Trust.
- Still need solid baselines: patching, [[Encryption Basics]], monitoring ([[IDS IPS]]).

## Mastery checklist

- [ ] Airport/keycard vs castle analogy
- [ ] Define never-trust-always-verify
- [ ] Contrast full-tunnel VPN vs ZTNA idea
- [ ] Give one microsegmentation example

## Related notes

- [[Firewalls]] · [[VPN]] · [[ACLs]] · [[Encryption Basics]] · [[IDS IPS]] · [[Cloud]]
- ← [[04-Network-Security/Index|Network Security]]
