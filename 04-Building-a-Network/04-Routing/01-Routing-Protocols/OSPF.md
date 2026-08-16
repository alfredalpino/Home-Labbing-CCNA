---
tags: [routing-protocols, networking, ccna, ospf]
aliases: [Open Shortest Path First, OSPF v2, OSPFv2]
layer: Network (Layer 3) / control plane
---

# OSPF

## Learning objectives

- Explain OSPF as a link-state IGP that floods LSAs into an LSDB and runs SPF (Dijkstra)
- Configure single-area and multi-area basics on Cisco IOS
- Master neighbor states, DR/BDR, areas, and cost
- Troubleshoot adjacency and missing routes with classic show commands

## One-sentence definition

> **OSPF** (Open Shortest Path First) is a **link-state** interior gateway protocol: routers flood topology advertisements (LSAs), build a synchronized Link-State Database, and compute loop-free shortest paths by cost.

## Analogy

> OSPF is a **city planning committee with shared blueprints**. Every junction files a building permit describing its roads and neighbors (LSAs). Everyone keeps the **same map binder** (LSDB). Each junction then runs the same shortest-path math on that map (SPF) to decide how to drive. If a bridge falls, a new permit floods, binders update, and routes recalculate.

## Why it matters

OSPF is the CCNA workhorse IGP: vendor-neutral, hierarchical (areas), fast convergence, and everywhere in enterprise labs. If you only deep-master one dynamic protocol first, make it OSPF.

## Deep dive

### Mental model

```text
Hello → neighbors → Exchange DBD/LSR/LSU → synchronized LSDB
                         ↓
                    SPF per router
                         ↓
                    RIB / FIB routes
```

### Mechanism — essentials

| Topic | CCNA must-know |
|-------|----------------|
| Areas | Backbone **Area 0**; others attach to 0 (classic design) |
| Router ID | Highest loopback IP or manual; unique in domain |
| Cost | Cisco default ≈ `ref-bw / iface-bw` (auto); lower better |
| Network types | Broadcast (DR/BDR), point-to-point (no DR), others |
| DR/BDR | On multi-access segments; priority + RID elect |
| LSA types (core) | 1 Router, 2 Network, 3 Summary, 5 External (awareness) |
| Wildcard mask | In `network` command: inverse of subnet mask |
| Adjacency states | Down → Init → 2-Way → ExStart → Exchange → Loading → Full |

**Area types (awareness):** stub / totally stubby / NSSA reduce Type-5 flooding — know *why* (scale, defaults) more than every knob.

### On the wire

- Protocol 89 (IP), multicast `224.0.0.5` (AllSPFRouters), `224.0.0.6` (AllDRouters)
- Hellos keep adjacency; LSAs flood on change (and periodic refresh)
- Authentication optional (cleartext / MD5 / keychain depending on IOS)

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Control plane | L3 protocol | Builds routing table |
| Data plane | L3 forwarding | Uses computed next hops |
| Contrast | Distance-vector ([[RIP]], [[EIGRP]]) | OSPF shares topology, not just vectors |

## Lab exercises

### Lab 1 — Single-area Full adjacency (GNS3)

Three routers in Area 0, point-to-point links + one LAN on R1.

```ios
router ospf 1
 router-id 1.1.1.1
 network 10.0.12.0 0.0.0.255 area 0
 network 192.168.1.0 0.0.0.255 area 0
```

Verify: `show ip ospf neighbor` (FULL), `show ip route ospf`, ping remote LAN.

### Lab 2 — Multi-area + DR election

Add Area 1 behind R2. Put R2–R3 on a multi-access Ethernet segment; set `ip ospf priority` so a chosen DR wins. Confirm `show ip ospf neighbor` roles and Type-2 LSA with `show ip ospf database`.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Stuck in 2-WAY only | Normal for non-DR/BDR on LAN | Or mismatched params if should be Full |
| Stuck ExStart/Exchange | MTU mismatch | `ip ospf mtu-ignore` lab only; fix MTU |
| No neighbor | Area / hello-dead / auth / network type / subnet | `debug ip ospf adj` (lab), iface IP |
| Missing routes | Area filter / stub / redistribute | LSDB vs RIB; ABR summaries |
| Flapping | Unstable link / Duplex | interface errors, timers |

## Common traps / interview gotchas

- **2-WAY** to DROTHER neighbors on broadcast is normal — not always a failure.
- Areas must touch Area 0 (without virtual-links — advanced).
- `network` statement uses **wildcard**, not subnet mask.
- OSPF AD 110 loses to EIGRP 90 if both present — know AD table.
- Passive interfaces stop Hellos but still advertise the network.

## Mastery checklist

- [ ] Explain LSDB + SPF vs distance-vector
- [ ] Bring up Full neighbors and verify routes
- [ ] Describe DR/BDR purpose on multi-access
- [ ] Troubleshoot MTU and area mismatches

## Related notes

- [[Static-vs-Dynamic-Routing]] · [[EIGRP]] · [[RIP]] · [[BGP]] · [[Default-Gateway]] · [[Routers]] · [[IP Address]]
- ← [[01-Routing-Protocols/Index|Routing Protocols]] · [[04-Routing/Index|Routing]]
