---
tags: [network-types, networking, ccna, wan]
aliases: [Wide Area Network, WAN]
layer: Scope / architecture
---

# WAN

## Learning objectives

- Define WAN as long-haul connectivity between sites
- Contrast WAN vs [[LAN]] in speed, cost, latency, and ownership
- Recognize modern WAN flavors (MPLS, Internet VPN, SD-WAN)
- Reason about why WAN troubleshooting differs from LAN

## One-sentence definition

> A **WAN** (Wide Area Network) spans large geographic distances to interconnect LANs/sites — often using service-provider circuits — with higher [[Latency]] and different cost/SLAs than local Ethernet.

## Analogy

> If a [[LAN]] is neighborhood streets, a WAN is the **interstate highway system** (and airlines). You don’t own most of the asphalt — you pay carriers for lanes. Trips take longer (latency), tolls matter (cost per bandwidth), and accidents far away still delay *your* traffic.

## Why it matters

Branch offices, data centers, and cloud regions meet over WANs. CCNA routing (static, OSPF intro, etc.) exists largely to stitch LANs across WANs. Most “app is slow” tickets that survive LAN checks become WAN/path/DNS problems.

## Deep dive

### Mental model

```text
Site A LAN ── Router ──[ WAN cloud / ISP ]── Router ── Site B LAN
```

You control customer edge routers; the middle may be opaque (Internet) or partially visible (MPLS).

### Typical properties

| Trait | WAN vs LAN |
|-------|------------|
| Distance | Cities/countries |
| Bandwidth | Often lower / expensive |
| Latency | Higher, sometimes asymmetric |
| Ownership | Provider + customer shared responsibility |
| Failure domain | Circuits, BGP, last-mile |

### Modern WAN patterns

- **Internet + [[VPN]]**: cheap, encrypted overlay
- **MPLS / private IP**: provider-routed private WAN
- **SD-WAN**: policy-based use of multiple underlays
- **Direct cloud connect**: “WAN” into [[Cloud]] on-ramps

### On the wire

Still IP [[Packet]]s end-to-end; underlay may be Ethernet, optical, cellular, etc. You often only see your CE interfaces + tunnel overlays.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Scope | Cross-layer | Geographic interconnect |
| Tech | Often L3 edge | Routing between LANs |

## Lab exercises

### Lab 1 — Measure WAN-ish RTT

```bash
ping -c 20 1.1.1.1
traceroute -n 1.1.1.1
```

Compare to LAN gateway RTT.

### Lab 2 — Mental SD-WAN

List two underlays a branch might have (fiber broadband + LTE) and what “fail over” means for users.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| High RTT/loss only off-site | WAN congestion/circuit | provider stats, both CE interfaces |
| One cloud app slow | Path / region | traceroute, DNS steering |
| VPN up, app fails | Overlay routing/DNS | tunnel selectors, split tunnel |

## Common traps / interview gotchas

- The Internet *is* a WAN of WANs — but “WAN link” in enterprise docs often means a *paid private* circuit.
- Buying more WAN bandwidth won’t fix chatty apps with huge RTT × round-trips ([[Latency]]).
- Asymmetric routing across WAN edges breaks stateful firewalls.

## Mastery checklist

- [ ] Define WAN vs LAN in one breath each
- [ ] Name three WAN underlay/overlay patterns
- [ ] Explain why latency dominates WAN feel
- [ ] Point to the WAN boundary on a branch diagram

## Related notes

- [[LAN]] · [[MAN]] · [[VPN]] · [[Cloud]] · [[Routers]] · [[Latency]] · [[Bandwidth]] · [[Throughput]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
