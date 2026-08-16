---
tags: [routing-protocols, networking, ccna, mpls, underlay]
aliases: [Multiprotocol Label Switching, MPLS, Label Switching]
layer: Data plane / provider underlay (L2.5 concept)
---

# MPLS

## Learning objectives

- Explain MPLS as label-based forwarding between PE/P routers
- Separate MPLS **underlay** (this note) from [[MPLS-VPN]] customer overlays
- Describe label push / swap / pop and PHP at a conceptual level
- Relate MPLS to IGP + LDP (or segment routing) for label distribution

## One-sentence definition

> **MPLS** (Multiprotocol Label Switching) forwards packets based on short **labels** rather than full IP lookups at every hop — building a high-speed **underlay** used by providers (and for services like L3VPN).

## Analogy

> IP routing is reading the **full street address** at every intersection. MPLS is a **baggage tag at the airport**: check-in sticks on a destination tag (push); each conveyor only reads the tag and shoves the bag (swap); at the last belt the tag is removed (pop) and local sorting uses the real address again. The airport halls underneath are the **underlay**; passenger tickets for different airlines sharing halls are services like [[MPLS-VPN]].

## Why it matters

Carriers and many enterprises run MPLS cores for traffic engineering and VPNs. CCNA asks for the *idea*: labels, LSR roles, why it’s fast/flexible — not full TE math. Don’t confuse MPLS transport with “MPLS means VPN.”

## Deep dive

### Mental model

```text
CE -- IP --> PE (PUSH label) --> P (SWAP) --> P (SWAP) --> PE (POP/PHP) -- IP --> CE

Control plane: IGP builds reachability to loopbacks; LDP/RSVP/SR binds labels to FECs
Data plane:   label lookup table (LFIB), not recursive IP at every P
```

### Mechanism — roles & operations

| Role | Who | Job |
|------|-----|-----|
| CE | Customer edge | IP only (usually) |
| PE | Provider edge | Push/pop; service awareness (VPN VRFs) |
| P | Provider core | Label swap only — “P doesn’t need customer routes” |

| Op | Meaning |
|----|---------|
| Push | Impose label(s) |
| Swap | Replace top label |
| Pop | Remove label |
| PHP | Penultimate hop pops so egress PE sees IP (or inner label) |

**FEC** (Forwarding Equivalence Class): packets treated the same (e.g. to a PE loopback).

### Label stack (awareness)

Multiple labels: e.g. **transport** label (how to reach egress PE) + **VPN** label (which VRF/CE) — details in [[MPLS-VPN]].

### On the wire

EtherType `0x8847` (unicast MPLS) / `0x8848` (multicast). Label stack entry: 20-bit label, TC/EXP, S-bit, TTL. Often sits between L2 and IP (“layer 2.5” nickname).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Nickname | “L2.5” | Between Ethernet and IP |
| Control | IGP + LDP/SR/BGP-LU | Distributes labels |
| Data | Label switching | Underlay forwarding |

## Lab exercises

### Lab 1 — Conceptual GNS3 MPLS core (if IOS image supports)

Four routers: CE1–PE1–P–PE2–CE2. Enable MPLS on PE/P links, IGP for loopbacks, LDP. Confirm `show mpls forwarding-table` and traceroute showing labels (MPLS-aware traceroute if available).

### Lab 2 — Underlay vs service table

On a PE (even as a whiteboard lab): list **global/IGP** routes to other PE loopbacks vs **VRF** customer routes. State clearly: P routers need PE loopbacks, **not** customer prefixes — that’s the scalability win.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| No label | LDP/session / MPLS not on iface | `show mpls ldp neighbor`, `mpls ip` |
| Break at P | MTU / label mismatch | iface MTU, LFIB |
| CE ping fail, core OK | VPN/VRF issue not underlay | move to [[MPLS-VPN]] checks |
| PHP confusion | Expect label on last hop | penultimate hop behavior |

## Common traps / interview gotchas

- MPLS ≠ encryption. Privacy for customers comes from separation + optional crypto elsewhere.
- MPLS ≠ [[MPLS-VPN]] — VPN is a *service* on an MPLS (or other) underlay.
- P routers typically **don’t** carry full Internet/customer tables.
- SD-WAN often *competes with* or *overlays* MPLS circuits — see [[SD-WAN]].

## Mastery checklist

- [ ] Explain push/swap/pop with airport-tag analogy
- [ ] Define CE / PE / P roles
- [ ] Separate underlay labels from VPN service
- [ ] Name IGP + LDP as classic label distribution

## Related notes

- [[MPLS-VPN]] · [[BGP]] · [[OSPF]] · [[VRFs]] · [[SD-WAN]] · [[WAN]] · [[Packet]]
- ← [[01-Routing-Protocols/Index|Routing Protocols]] · [[04-Routing/Index|Routing]]
