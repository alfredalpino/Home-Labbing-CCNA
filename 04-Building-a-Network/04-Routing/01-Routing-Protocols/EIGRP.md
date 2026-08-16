---
tags: [routing-protocols, networking, ccna, eigrp]
aliases: [Enhanced Interior Gateway Routing Protocol, EIGRP]
layer: Network (Layer 3) / control plane
---

# EIGRP

## Learning objectives

- Explain EIGRP as Cisco’s advanced distance-vector protocol using DUAL
- Configure EIGRP classic or named mode basics and verify successors
- Understand composite metric (bandwidth + delay by default) and feasible successor
- Contrast EIGRP with [[OSPF]] for CCNA design conversations

## One-sentence definition

> **EIGRP** (Enhanced Interior Gateway Routing Protocol) is a Cisco **advanced distance-vector** IGP: neighbors exchange reachability, DUAL picks a loop-free successor (and optional feasible successors) for fast local repair.

## Analogy

> EIGRP is a **taxi radio network** that shares “best known times to destinations,” not full city blueprints. Each dispatcher keeps a **primary route** (successor) and often a **ready backup** that already proved it isn’t a U-turn into you (feasible successor). When the main road closes, the backup engages *without* waiting for a city-wide remapping — that’s DUAL’s speed.

## Why it matters

Still common on Cisco campuses and in CCNA/enterprise labs. Feasible successor and unequal-cost load balancing (`variance`) are classic interview topics. Know it well enough to configure, verify, and contrast with OSPF.

## Deep dive

### Mental model

```text
Hello (multicast) → neighbor up
Update (partial, bounded) → topology table
DUAL → successor in routing table (+ feasible successors)
Link fail → if FS exists: instant switch; else query domain
```

### Mechanism — metrics & DUAL

**Classic composite metric (simplified):** uses **bandwidth** (slowest along path) and **delay** (sum) by default; reliability/load optional (K-values). Matching K-values required for adjacency.

| Term | Meaning |
|------|---------|
| FD (Feasible Distance) | Best metric to dest via successor |
| RD / AD reported | Neighbor’s metric to dest |
| Feasibility condition | Neighbor’s reported distance **<** my FD → loop-free backup |
| Successor | Best path installed |
| Feasible successor | Backup meeting FC |

**AS number** must match. Auto-summary historically dangerous — disable (`no auto-summary` in classic).

### On the wire

- Protocol 88 (IP), multicast `224.0.0.10`
- RTP (Reliable Transport Protocol) for updates — not TCP
- Hellos maintain neighbors; updates are incremental

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Control plane | L3 IGP | Installs routes (AD 90 internal) |
| Data plane | L3 | Forwards using successors |
| Vs OSPF | Distance-vector + DUAL | OSPF = link-state + SPF |

## Lab exercises

### Lab 1 — Three-router EIGRP (GNS3 / IOSv)

```ios
router eigrp 100
 network 10.0.0.0 0.0.255.255
 no auto-summary
```

Verify: `show ip eigrp neighbors`, `show ip eigrp topology`, `show ip route eigrp`.

### Lab 2 — Feasible successor demo

Build dual paths R1→R2→R3 and R1→R4→R3 with different bandwidth/delay so both exist but one is successor. Confirm FS in topology table; shut successor link; watch near-instant failover without active querying (ideal case).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| No neighbor | AS / K-values / subnet / ACL | `show ip eigrp neighbors`, iface |
| Route missing | Filter / auto-summary / stub | topology table vs RIB |
| Unexpected path | Delay/bw mis-set | `show interface` delay/bw |
| SIA (stuck in active) | Query boundary / link issues | stub routers, timers, unstable WAN |

## Common traps / interview gotchas

- EIGRP is **not** link-state — don’t say it floods an LSDB like OSPF.
- Feasible successor ≠ any second-best path — must pass feasibility condition.
- AD 90 (internal) beats OSPF 110 — dual-running labs surprise people.
- Named mode vs classic: same ideas, different CLI — labs may use either.
- “Advanced distance vector” / “hybrid” marketing — be precise: DUAL DV.

## Mastery checklist

- [ ] Configure EIGRP and verify neighbors + routes
- [ ] Explain successor vs feasible successor + FC
- [ ] Contrast EIGRP vs OSPF in one clear paragraph
- [ ] Predict AD behavior vs OSPF/static

## Related notes

- [[OSPF]] · [[RIP]] · [[BGP]] · [[Static-vs-Dynamic-Routing]] · [[Routers]] · [[Bandwidth]] · [[Latency]]
- ← [[01-Routing-Protocols/Index|Routing Protocols]] · [[04-Routing/Index|Routing]]
