---
tags: [network-devices, networking, ccna, router]
aliases: [Router, Routing Device]
layer: Network (Layer 3)
---

# Routers

## Learning objectives

- Define a router as an L3 forwarder between networks
- Explain routing table + longest-prefix match at intuition level
- Contrast routers vs [[Switches]] / L3 switches
- Identify WAN edge roles (default gateway, NAT, [[VPN]])

## One-sentence definition

> A **router** forwards [[Packet]]s between different IP networks by consulting a routing table — choosing the best next hop for each destination prefix.

## Analogy

> A router is a **highway interchange with a GPS database**. Cars ([[Packet]]s) arrive from local streets ([[LAN]]). The interchange reads the destination city ([[IP Address]]) and sends each car onto the correct highway ramp (next hop / exit interface). A switch is still inside one city reading street addresses ([[MAC Address]]).

## Why it matters

Without routers, broadcast domains and IP subnets can’t interconnect. Your home “Wi‑Fi router” is usually router + switch + AP + modem functions in one box — exams and jobs require separating those roles mentally.

## Deep dive

### Mental model

```text
LAN A (192.168.1.0/24) ── Router ── LAN B (10.0.0.0/8) or WAN
Routing table: destination prefix → next-hop / exit iface
```

### Core behaviors

| Behavior | Meaning |
|----------|---------|
| Strip/rewrite L2 | New [[Frame]] each hop |
| Decrement TTL | Loop safety ([[ICMP]] time exceeded) |
| Longest prefix match | More specific routes win |
| Gateway of last resort | Default route `0.0.0.0/0` |

### SOHO “router” bundle

Home gateway often includes: modem (or ONT handoff), router, NAT, firewall, Ethernet switch, Wi‑Fi AP. Lab truth: **draw the functions**, not the plastic box.

### On the wire

Hop-by-hop: MACs change, IPs usually stay (except NAT). Capture at two interfaces of a router to see rewrite.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Primary L3 device |
| OSI | 3 | Network layer forwarder |

## Lab exercises

### Lab 1 — Find your default router

```bash
route -n get default
ping -c 2 $(route -n get default | awk '/gateway:/ {print $2}')
```

### Lab 2 — GNS3 two-router lab

Connect two LANs with routers; show that hosts need correct gateway; traceroute across.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Local OK, Internet fail | Default route/NAT/WAN | routing table, WAN IP, NAT |
| Asymmetric paths | Policy routing / dual homing | both directions, firewall state |
| TTL exceeded | Loop | routing loop, recursive routes |

## Common traps / interview gotchas

- L3 switch can route too — “router” is a *role*, not only a chassis shape.
- Switches don’t care about IP when acting pure L2.
- NAT is common on edge routers but is **not** required for routing itself.

## Mastery checklist

- [ ] Explain interchange/GPS analogy
- [ ] State what changes each hop (MAC vs IP)
- [ ] Find and ping default gateway on macOS
- [ ] Separate SOHO box functions on a sketch

## Related notes

- [[Switches]] · [[Packet]] · [[IP Address]] · [[ICMP]] · [[WAN]] · [[LAN]] · [[VPN]] · [[Modems]]
- ← [[02-Network-Devices/Index|Network Devices]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
