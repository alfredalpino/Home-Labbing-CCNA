---
tags: [network-devices, networking, ccna, hub]
aliases: [Ethernet Hub, Network Hub, Repeater Hub]
layer: Physical (Layer 1)
---

# Hub

## Learning objectives

- Define a hub as a multiport repeater
- Explain shared collision domain behavior
- Know why hubs are obsolete vs [[Switches]]
- Still answer exam/interview hub questions correctly

## One-sentence definition

> A **hub** is a Layer‑1 multiport repeater that takes bits in one port and electrically repeats them out all other ports — no MAC learning, no frame intelligence.

## Analogy

> A hub is a **town crier with a megaphone in an echo chamber**. Anyone speaks; everyone else is forced to hear it. If two people talk at once, voices collide (collisions). A [[Switches|switch]] is a discreet postal clerk who delivers quietly to one address.

## Why it matters

You may never deploy hubs, but they teach **collision domains**, half-duplex, and why switching won. Exam questions love hub vs switch comparisons.

## Deep dive

### Mental model

```text
Any port RX bits ──► repeat to ALL other ports
One big collision domain (classic Ethernet hub)
```

### Properties

| Trait | Hub |
|-------|-----|
| Layer | 1 (bits) |
| MAC table | None |
| Bandwidth | Shared |
| Duplex | Historically half |
| Security/privacy | Everyone sees frames |
| Modern use | Lab nostalgia / rare specialty |

### Why switches replaced hubs

Per-port collision domains, full duplex, MAC learning, VLANs, higher aggregate [[Throughput]].

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | 1 | Repeater |
| TCP/IP | Network Access physical | Dumb bit copy |

## Lab exercises

### Lab 1 — Comparison table from memory

Write hub vs switch vs router: layer, address used, flood behavior.

### Lab 2 — Wireshark thought

On a hub, promiscuous capture sees neighbors’ unicast; on a switch, usually not (without SPAN/mirroring).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Late collisions / poor performance | Hub + duplex mix | replace with switch |
| Seeing others’ traffic | Hub or mirror port | topology audit |

## Common traps / interview gotchas

- USB “hub” ≠ Ethernet hub (different meaning).
- “Hub” in marketing for SOHO devices often means switch/router.
- Hubs don’t read [[MAC Address]]es — if a device makes forwarding decisions by MAC, it’s not a hub.

## Mastery checklist

- [ ] Define hub as L1 repeater
- [ ] Megaphone analogy
- [ ] Explain one collision domain
- [ ] State why switches superseded hubs

## Related notes

- [[Switches]] · [[Routers]] · [[Frame]] · [[Transmission Media Types]] · [[LAN]]
- ← [[02-Network-Devices/Index|Network Devices]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
