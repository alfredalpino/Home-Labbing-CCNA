---
tags: [network-devices, networking, ccna, switch]
aliases: [Switch, Ethernet Switch, Network Switch]
layer: Data Link (Layer 2)
---

# Switches

## Learning objectives

- Define a switch as an L2 forwarder using MAC learning
- Explain flood / forward / filter behavior
- Relate switches to VLANs, trunks, and [[LAN]] design
- Contrast with [[Hub]] and [[Routers]]

## One-sentence definition

> An Ethernet **switch** forwards [[Frame]]s within a LAN based on destination [[MAC Address]]es, learning source MACs into a CAM/MAC table to reduce flooding.

## Analogy

> A switch is a **smart post office inside one town**. It learns which house (MAC) sits on which street (port). Mail for a known house goes only down that street. Unknown addresses get “Did anyone see this person?” shouted through the town (flood). A [[Hub]] is a town crier who repeats every message to every street, always.

## Why it matters

Access and distribution layers are switch-heavy. STP loops, VLAN mis-tags, duplex errors, and CAM overflows are classic outages. Master switches before fancy routing.

## Deep dive

### Mental model

```text
Frame in → learn src MAC→port → lookup dst MAC
  ├ known unicast → out one port
  ├ unknown/bcast/mcast → flood in VLAN
  └ filter if dst is on same incoming port
```

### Key topics you’ll grow into

| Topic | Idea |
|-------|------|
| VLAN | Logical LANs on one switch fabric |
| Trunk | Carry many VLANs between switches |
| STP | Loop prevention |
| EtherChannel | Bundle links |

### On the wire

Switches generally don’t decrement IP TTL (pure L2). They care about FCS errors, VLAN tags, MAC tables.

```bash
# Host view into switched LAN
arp -a
sudo tcpdump -ni en0 -e -c 10
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | LAN switching |
| OSI | 2 | Data-link forwarder |

## Lab exercises

### Lab 1 — Same VLAN ping

Two PCs on one switch/VLAN; verify ARP then unicast.

### Lab 2 — Compare to hub behavior (thought)

Explain collision domains: each switch port is its own collision domain (full duplex).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| MAC flapping | Loop / dual NIC | STP, cabling |
| Devices on “wrong network” | VLAN membership | access VLAN, trunk allow list |
| CRC errors | Cable/duplex | replace patch, autoneg |

## Common traps / interview gotchas

- Unmanaged home “switch” still switches — just no config.
- L3 switches route *and* switch — know which feature you’re using.
- Switching ≠ routing; wrong gateway still breaks off-subnet even if switch is perfect.

## Mastery checklist

- [ ] Tell the post-office analogy
- [ ] Describe flood vs forward
- [ ] Contrast switch vs hub vs router in one table
- [ ] Name VLAN/trunk/STP as next skills

## Related notes

- [[Hub]] · [[Routers]] · [[Frame]] · [[MAC Address]] · [[ARP]] · [[LAN]] · [[Access Points]]
- ← [[02-Network-Devices/Index|Network Devices]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
