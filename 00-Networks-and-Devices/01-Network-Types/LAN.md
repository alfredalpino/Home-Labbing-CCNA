---
tags: [network-types, networking, ccna, lan]
aliases: [Local Area Network, LAN]
layer: Scope / architecture
---

# LAN

## Learning objectives

- Define a LAN by scope, ownership, and typical speeds
- Contrast LAN vs [[WAN]] / [[MAN]] / [[WLAN]]
- Map LAN components to [[Switches]], [[Routers]], and cabling
- Spot LAN boundaries in real home/office designs

## One-sentence definition

> A **LAN** (Local Area Network) connects devices in a limited geographic area — typically a home, floor, building, or campus — under one administrative domain, usually at high speed and low [[Latency]].

## Analogy

> A LAN is your **neighborhood street grid**. Houses ([[Host]]s) connect to local intersections ([[Switches]]). To leave the neighborhood for another city, you need the on‑ramp ([[Routers]] / default gateway) onto bigger roads ([[WAN]]).

## Why it matters

Almost every CCNA lab *is* a LAN (or a few LANs connected by routers). VLANs, STP, EtherChannel, and most switching topics assume a LAN context. When someone says “the network is down,” they often mean *this LAN segment*.

## Deep dive

### Mental model

```text
[PC]──[Switch]──[Switch]──[Router]──► WAN / Internet
         ▲
     same broadcast domain(s) / VLANs = LAN fabric
```

### Characteristics

| Trait | Typical LAN |
|-------|-------------|
| Distance | Meters to a few km (campus) |
| Speed | 1G / 10G common; Wi‑Fi varies ([[WLAN]]) |
| Ownership | One org controls addressing & policy |
| Media | Copper, fiber, Wi‑Fi |
| Cost model | CapEx gear + power; not per-bit WAN circuits |

### LAN vs VLAN

A **physical LAN** is the real wires/APs. A **VLAN** is a *logical* LAN sliced inside switches — multiple broadcast domains on shared hardware. Same “neighborhood” metaphor, different street names painted on the same asphalt.

### On the wire

LAN traffic is mostly Ethernet [[Frame]]s; IP [[Packet]]s ride inside. Broadcasts ([[ARP]], DHCP Discover) stay inside the LAN/VLAN unless relayed.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Scope concept | Cross-layer | Describes *where* devices live |
| LAN tech | L1–L2 primarily | Ethernet/Wi‑Fi switching |

## Lab exercises

### Lab 1 — Draw your home LAN

Sketch modem/ONT → router → switch/AP → devices. Label the LAN side vs WAN side of the router.

### Lab 2 — See LAN neighbors

```bash
arp -a
ping -c 2 $(route -n get default | awk '/gateway:/ {print $2}')
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Local shares fail, Internet OK | LAN/VLAN isolation | switch VLAN, AP SSID isolation |
| Everything local fails | Switch/PoE/cable | link lights, another port/cable |
| Slow only on one floor | LAN congestion / duplex | interface errors, Wi‑Fi band |

## Common traps / interview gotchas

- “LAN cable” usually means Ethernet copper — not the whole LAN definition.
- Two offices connected by dark fiber can still be *one* extended LAN — design carefully (broadcast domain size).
- Cloud resources are not “on your LAN” unless you build private connectivity.

## Mastery checklist

- [ ] Define LAN without only saying “local”
- [ ] Draw LAN vs WAN boundary on a home router
- [ ] Explain VLAN as a logical LAN
- [ ] Contrast LAN broadcast behavior vs routed networks

## Related notes

- [[WAN]] · [[MAN]] · [[WLAN]] · [[Switches]] · [[Routers]] · [[Frame]] · [[ARP]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
