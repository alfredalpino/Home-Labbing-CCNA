---
tags: [switching, networking, ccna, stp, spanning-tree]
aliases: [Spanning Tree Protocol, STP, RSTP, Rapid STP, MSTP]
layer: Data Link (Layer 2)
---

# STP

## Learning objectives

- Explain why Ethernet loops need Spanning Tree and what a broadcast storm does
- Master root bridge election, port roles/states, and path cost
- Contrast STP vs RSTP vs MSTP at CCNA awareness
- Verify and influence STP with priority and portfast (safely)

## One-sentence definition

> **STP** (Spanning Tree Protocol) builds a **loop-free logical tree** over a redundant L2 topology by blocking some ports — preventing broadcast storms while keeping backup links ready.

## Analogy

> Redundant switch links without STP are a **hall of mirrors**: a shout ([[Frame|broadcast]]) reflects forever and deafens the building (broadcast storm). STP elects a **mayor** (root bridge) and closes some doors (blocking ports) so there’s exactly **one path** between any two rooms. RSTP is the same idea with **faster door actuators**. MSTP paints **multiple trees** for different VLAN groups so load can use different doors.

## Why it matters

Campus switching without loop control is an outage waiting to happen. Interviewers love root election math, PortFast risks, and “why is this port blocking?”

## Deep dive

### Mental model

```text
Elect Root (lowest Bridge ID = priority + MAC)
  → each SW picks Root Port (best path to root)
  → each segment picks Designated Port
  → remaining Alternate/Blocking
Result: loop-free active topology
```

### Mechanism — classic + rapid

| Concept | Detail |
|---------|--------|
| Bridge ID | Priority (default 32768, steps of 4096) + MAC |
| Path cost | Based on link speed (lower better); sum toward root |
| BPDUs | Hellos carrying root info (STP/RSTP formats) |
| Classic states | Blocking → Listening → Learning → Forwarding |
| RSTP roles | Root, Designated, Alternate, Backup; states mostly Discarding/Learning/Forwarding |
| Edge / PortFast | End hosts skip delay — **never** on links to switches |
| MSTP | Maps VLANs → instances; fewer trees than PVST per VLAN |

**Cisco flavors (awareness):** PVST+/RPVST+ run per-VLAN trees; MST regions for scale.

### On the wire

IEEE BPDUs as LLC/SNAP or Ethernet multicast `01:80:C2:00:00:00`. RSTP proposal/agreement handshakes speed convergence on point-to-point links.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | Data Link (L2) | Loop-free Ethernet topology |
| Interaction | [[VLANs]] / trunks | Per-VLAN or MST instances |
| Not | L3 ECMP | That’s routing; STP is L2 |

## Lab exercises

### Lab 1 — Loop then STP (GNS3)

Three switches in a triangle, all trunks. Confirm one port Blocking/Alternate. `show spanning-tree` — note Root ID and roles. Lower priority on chosen root:

```ios
spanning-tree vlan 1 priority 4096
```

### Lab 2 — PortFast + BPDU Guard

On access ports to PCs:

```ios
spanning-tree portfast
spanning-tree bpduguard enable
```

Plug a switch into that port (lab) — watch err-disable; document why BPDU Guard matters.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Broadcast storm / meltdown | STP off / unidirectional link | disable loops, UDLD, storm-control |
| Unexpected root | Priority / MAC | `show spanning-tree`, root priority |
| Slow host connect | No PortFast | edge port config |
| Blocked uplink | Inferior BPDUs / cost | port role, path cost, root guard |

## Common traps / interview gotchas

- Lower priority **wins** root (4096 beats 32768).
- PortFast on an inter-switch link can create temporary loops — use BPDU Guard.
- “STP blocks ports” ≠ link down — backup still there for failover.
- RSTP converges in seconds; classic 802.1D was ~30–50s — know the story.

## Mastery checklist

- [ ] Elect root from priority + MAC examples
- [ ] Read `show spanning-tree` roles
- [ ] Explain RSTP vs STP in one breath
- [ ] State PortFast + BPDU Guard pairing

## Related notes

- [[Switches]] · [[VLANs]] · [[Link-Aggregation]] · [[MAC-Address-Tables]] · [[LAN]] · [[Frame]]
- ← [[05-Switching/Index|Switching]] · [[04-Building-a-Network/Index|Building a Network]]
