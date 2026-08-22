---
tags: [network-security, ids, ips, networking, ccna]
aliases: [IDS, IPS, Intrusion Detection, Intrusion Prevention, IDS/IPS, IDS IPS, IDS-IPS]
layer: Detection / prevention
---

# IDS / IPS

## Learning objectives

- Define IDS vs IPS and inline vs out-of-band
- Know signature vs anomaly detection at a high level
- Place IDS/IPS relative to firewalls and NGFW
- Handle false positives without blinding yourself

## One-sentence definition

> An **IDS** (*Intrusion Detection System*) monitors traffic or hosts for suspicious patterns and **alerts**; an **IPS** (*Intrusion Prevention System*) sits **inline** and can **block** matching traffic automatically.

## Analogy

> IDS is a **security camera + guard watching monitors**: sees a break-in pattern, raises an alarm, doesn’t physically stop the thief by itself. IPS is a **lock that slams shut mid-hallway** when the camera AI recognizes a banned behavior — powerful, but if the AI is wrong it traps employees too (false positives).

## Why it matters

NGFWs often bundle IPS. Network engineers get paged when IPS signatures break business apps after an update — tuning is a shared sport with security teams.

## Deep dive

### Mental model

```text
IDS (tap/SPAN/copy) → detect → alert → human/SOAR response
IPS (inline path)   → detect → drop/reset/quarantine (+ alert)
```

### Detection styles

| Style | Idea | Risk |
|-------|------|------|
| Signature | Match known bad patterns | Miss novel attacks |
| Anomaly / behavior | Deviate from baseline | False positives |
| Reputation | Known-bad IPs/domains | Stale/wrong intel |

### Placement

| Placement | Notes |
|-----------|-------|
| On NGFW | Common enterprise pattern |
| Dedicated inline appliance | Fail-open vs fail-closed matters |
| Host IDS/IPS | Endpoint agent view |
| Cloud | Security group + IDS offerings |

### On the wire

Inline IPS becomes another hop (latency, failure domain). TAP/SPAN IDS shouldn’t change packets — if it does, it’s mis-plumbed.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Cross-layer | L3–L7 patterns | Depends on signatures |
| Ops | Monitoring + control | Alert vs block |

## Lab exercises

### Lab 1 — SPAN thought

Draw switch SPAN to IDS. Why can’t this IDS *block* by itself?

### Lab 2 — False positive policy

Write rules: who can disable a signature, for how long, with what ticket proof.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| App fails through IPS path | Signature hit | IPS logs, rule ID |
| Detection gap | Encrypted payload | decrypt policy, endpoint telemetry |
| Outage on IPS failure | Fail-closed design | HA, bypass procedure |

## Common traps / interview gotchas

- IDS ≠ IPS (detect vs prevent).
- More signatures ≠ better — noise buries real incidents.
- Encrypted traffic limits payload signatures without decrypt or endpoint controls.

## Mastery checklist

- [ ] Camera vs slamming-lock analogy
- [ ] Define inline vs passive
- [ ] Name signature vs anomaly tradeoff
- [ ] Describe a false-positive handling loop

## Related notes

- [[Next-Generation Firewall]] · [[DoS DDoS]] · [[Encryption Basics]] · [[ACLs]] · [[Zero Trust Architecture]]
- ← [[04-Network-Security/Index|Network Security]]
