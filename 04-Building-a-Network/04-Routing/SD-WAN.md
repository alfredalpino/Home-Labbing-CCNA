---
tags: [routing, networking, ccna, sd-wan, wan]
aliases: [SD-WAN, Software-Defined WAN, Software Defined WAN]
layer: Overlay / WAN architecture
---

# SD-WAN

## Learning objectives

- Define SD-WAN as policy-driven, controller-orchestrated WAN overlays
- Contrast traditional hub-spoke MPLS/VPN WANs with SD-WAN application-aware paths
- Name underlay vs overlay, controllers, and edge roles at CCNA awareness depth
- Relate SD-WAN to [[VPN]], [[MPLS]], and Internet DIA circuits

## One-sentence definition

> **SD-WAN** (Software-Defined WAN) centralizes WAN **policy and control**, building encrypted overlays across whatever underlays you have (Internet, [[MPLS]], LTE) so traffic can prefer paths by application, SLA, and cost — not just destination prefix.

## Analogy

> Classic WAN is a **fixed railroad**: trains (packets) follow the tracks the railroad company laid ([[MPLS]] circuits). SD-WAN is a **fleet dispatcher with GPS**: vans can take highways, side streets, or toll roads (Internet / MPLS / LTE). The dispatcher (controller) picks the route from live road conditions and cargo type (voice vs backup), while each van still drives on real asphalt (underlay).

## Why it matters

Enterprises replace or augment expensive MPLS with broadband + IPsec overlays. CCNA/enterprise paths expect you to know *what problem SD-WAN solves* (agility, multi-transport, app-aware steering) without memorizing one vendor’s CLI.

## Deep dive

### Mental model

```text
          ┌──────── Controller / orchestrator ────────┐
          │  policy, templates, keys, telemetry         │
          └───────────────┬───────────────────────────┘
                          │ control
   Branch edge ←── overlay tunnels (IPsec-ish) ──→ Hub / cloud edge
        │                        │
   Underlays: Internet DIA · MPLS · 4G/5G
```

### Mechanism — pieces

| Piece | Role |
|-------|------|
| Underlay | Physical/IP reachability (BGP to ISP, static, etc.) |
| Overlay | Encrypted tunnels between edges; carries customer traffic |
| Controller | Pushes policy, certs/keys, topology intent |
| Edge / vEdge / cEdge | Enforces policy, measures loss/latency/jitter |
| Orchestration | ZTP, templates, compliance |

**App-aware routing:** classify (DSCP, NBAR, ports) → pick tunnel meeting SLA → fail over when brownout detected (not only hard down).

### SD-WAN vs “just IPsec”

| | DIY IPsec mesh | SD-WAN |
|-|----------------|--------|
| Scale | Painful N² tunnels | Controller / hierarchy |
| Policy | Per-box ACL/route-maps | Central intent |
| Transport | Often one | Active-active multi-path |
| Visibility | DIY | Built-in path quality |

### On the wire

Expect DTLS/IPsec/ESP between edges; management to controllers (vendor-specific ports). Data plane looks like [[VPN]] encapsulated packets over public or private underlay IPs.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Overlay | Typically L3 VPN tunnels | Customer IP inside |
| Underlay | L3 [[WAN]] / Internet | Carries outer headers |
| Control | Management / orchestration | Out-of-band or in-band to controller |

## Lab exercises

### Lab 1 — Emulate the idea without a full SD-WAN stack

In GNS3: two “branches” each with dual exits (simulate ISP-A and ISP-B with different delay). Build two IPsec or GRE+IPsec paths to HQ. Prefer path A with floating static / IP SLA tracking; fail to B when A loss exceeds threshold. Document how this is a **manual** SD-WAN.

### Lab 2 — Brownout thought experiment

Add latency on path A with a traffic-shaping/delay node. Show that “link up” ≠ “good for VoIP.” List what an SD-WAN would measure (loss, latency, jitter) vs a simple interface `up/down`.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Overlay down, underlay up | IKE/certs/firewall | UDP 500/4500, time sync, ACL |
| App slow, tunnel up | Bad path choice / DIA congestion | Path metrics, DIA vs MPLS preference |
| One site offline | Controller reachability / ZTP | Edge to controller, DNS, DHCP option |
| Split brain policy | Template mismatch | Version, feature flags, site ID |

## Common traps / interview gotchas

- SD-WAN is **not** “no more routing” — underlay and overlay still need IP reachability.
- Replacing MPLS with Internet DIA changes **SLA and security** assumptions — encryption becomes mandatory.
- Vendor marketing “AI WAN” still rests on tunnels + policy + measurement.
- SD-WAN ≠ [[SDN]] campus fabric; related idea (central control), different domain.

## Mastery checklist

- [ ] Draw underlay vs overlay with a controller
- [ ] Contrast SD-WAN with classic hub-spoke IPsec
- [ ] Explain brownout vs hard failure
- [ ] Relate to [[MPLS]] and [[VPN]] as underlay/overlay options

## Related notes

- [[VPN]] · [[MPLS]] · [[MPLS-VPN]] · [[IPSec-vs-SSL-VPN]] · [[Static-vs-Dynamic-Routing]] · [[WAN]] · [[Bandwidth]] · [[Latency]]
- ← [[04-Routing/Index|Routing]] · [[04-Building-a-Network/Index|Building a Network]]
