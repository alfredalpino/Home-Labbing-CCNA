---
tags: [high-availability, networking, ccna, glbp, fhrp, cisco]
aliases: [GLBP, Gateway Load Balancing Protocol]
layer: Gateway redundancy + load share
---

# GLBP

## Learning objectives

- Define GLBP as Cisco FHRP that can **load-balance** first-hop traffic
- Explain AVG vs AVF roles and per-host virtual MAC assignment
- Contrast with single-forwarder [[HSRP]] / [[VRRP]]
- Know when GLBP helps vs when routing/ECMP or L4 [[Load-Balancer]] is better

## One-sentence definition

> **GLBP** (Gateway Load Balancing Protocol) is a Cisco first-hop redundancy protocol that uses one virtual IP but **multiple virtual MACs** so several routers can forward traffic for that gateway while still providing failover.

## Analogy

> [[HSRP]]/[[VRRP]] put **one chef at one stove** (Active/Master) while others wait. GLBP is a **pizza counter with one phone number (VIP)** but **several ovens (AVFs)**: the greeter (AVG) answers the phone and tells each customer which pickup window (virtual MAC) to use, spreading orders. If an oven dies, customers get redirected — the phone number on the flyer never changes.

## Why it matters

Idle standby bandwidth bothers architects. GLBP is the CCNA answer for “FHRP that load-shares.” Still understand limits: it’s first-hop on a LAN, not global server LB.

## Deep dive

### Mental model

```text
Hosts → same VIP
         AVG assigns vMAC1 / vMAC2 / ...
         AVF1 forwards for vMAC1
         AVF2 forwards for vMAC2
If AVF fails → AVG reassigns hosts
```

### Mechanism

1. Elect **AVG** (Active Virtual Gateway) — answers ARP for VIP.
2. AVG assigns virtual MACs to **AVFs** (Active Virtual Forwarders).
3. Hosts cache different vMACs → traffic spreads across routers.
4. Failure: roles move; hosts may need ARP refresh depending on timing.

### Load-balance awareness

| Method (concept) | Idea |
|------------------|------|
| Round-robin | Rotate vMAC assignment |
| Host-dependent | Sticky per host MAC |
| Weighted | Prefer bigger links/boxes |

### On the wire

ARP replies for the VIP vary by host (different target MAC). Hellos maintain group health. [[Packet-Analysis]] from two PCs may show different gateway MACs for the same VIP — that’s a feature.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network gateway | First-hop LB + HA |
| OSI | 3 (+ L2 vMACs) | Multiple forwarder MACs |

## Lab exercises

### Lab 1 — ARP comparison

On paper: Host A and Host B both use VIP `.1` but learn vMAC_A vs vMAC_B. Draw arrows to Router1 vs Router2.

### Lab 2 — When not to use GLBP

List two designs where ECMP routing or a dedicated [[Load-Balancer]] beats GLBP. Explain why.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| All traffic one router | AVG assign / weights | GLBP weighting, host count |
| Outage on one AVF | Forwarder fail | AVG reassignment, ARP |
| Asymmetric weirdness | Return path | routing symmetry, state devices |
| Confusion with HSRP | Wrong mental model | one VIP ≠ one forwarder here |

## Common traps / interview gotchas

- GLBP still needs solid L2 adjacency for the group.
- Stateful firewalls on asymmetric paths can break “clever” first-hop LB.
- Not a substitute for server [[Load-Balancer]] / [[Least-Connections]].
- Vendor lock: Cisco-oriented; multi-vendor often sticks to [[VRRP]] + routing ECMP.

## Mastery checklist

- [ ] Define AVG vs AVF
- [ ] Explain one VIP, many vMACs
- [ ] Contrast with [[HSRP]] standby waste
- [ ] Name an asymmetry risk

## Related notes

- [[HSRP]] · [[VRRP]] · [[Load-Balancer]] · [[Round-Robin]] · [[Failover]] · [[ARP]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
