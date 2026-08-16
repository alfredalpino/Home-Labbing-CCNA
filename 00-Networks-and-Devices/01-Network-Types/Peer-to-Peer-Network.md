---
tags: [network-types, networking, ccna, p2p, peer-to-peer]
aliases: [Peer-to-Peer, P2P Network, Peer to Peer]
layer: Architecture model
---

# Peer-to-Peer Network

## Learning objectives

- Define P2P as symmetric role sharing among peers
- Contrast with [[Client-Server Network]]
- Know classic examples and enterprise implications
- Understand hybrid models (P2P overlay with trackers/bootstrap)

## One-sentence definition

> A **peer-to-peer (P2P) network** lets participants act as both consumers and providers of resources — peers share files, media, or workload without requiring a single central [[Server]] for every exchange.

## Analogy

> P2P is a **potluck dinner**: every guest brings food and may serve others. There’s no single restaurant kitchen ([[Client-Server Network]]). Someone may still send invitations (bootstrap/tracker), but the meal circulates guest-to-guest.

## Why it matters

File sharing, some update distribution, blockchain gossip, and WebRTC calls use P2P patterns. Firewalls hate inbound peer connections; NAT traversal becomes a sport. Architecturally, you must know when traffic will *not* hairpin through a friendly server VIP.

## Deep dive

### Mental model

```text
Peer A ◄──► Peer B
  ▲           ▲
  └────► Peer C
Roles blur: each node may upload + download
```

### Properties

| Trait | P2P |
|-------|-----|
| Roles | Symmetric / fluid |
| Scaling | Can scale with participants |
| Admin | Often decentralized; harder enterprise control |
| NAT | Inbound connectivity is hard |

### Hybrids

Many “P2P” systems still use directories, trackers, or signaling servers (still client–server for *control*), then P2P for *data*.

### On the wire

Expect many flows between ephemeral ports; may use [[UDP]] for NAT-friendly transports. Harder to ACL with simple “allow VIP:443.”

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Architecture | Application overlay | Independent of LAN/WAN type |
| Transport | TCP and/or UDP | App-dependent |

## Lab exercises

### Lab 1 — Compare flows

Mentally contrast: one HTTPS download from a CDN (client–server) vs BitTorrent-style multi-peer (P2P).

### Lab 2 — NAT thought experiment

Two peers behind home routers want to connect — list why STUN/TURN or relays appear.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Works on-site, fails at home | NAT/firewall inbound | UPnP, relays, ports |
| Partial connectivity | Some peers reachable | path diversity |
| Corp block | Policy against P2P | proxy/firewall categories |

## Common traps / interview gotchas

- P2P ≠ “no servers ever exist.”
- Not inherently more secure — often the opposite for enterprise visibility.
- Small office “just share folders between PCs” is P2P-ish workgroup behavior.

## Mastery checklist

- [ ] Use potluck vs restaurant analogy correctly
- [ ] Define peer role symmetry
- [ ] Give one hybrid example (signaling + P2P media)
- [ ] Explain NAT pain for peers

## Related notes

- [[Client-Server Network]] · [[Client]] · [[Server]] · [[UDP]] · [[TCP]] · [[VPN]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
