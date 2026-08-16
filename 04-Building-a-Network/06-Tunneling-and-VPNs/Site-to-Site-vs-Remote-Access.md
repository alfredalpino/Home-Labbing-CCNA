---
tags: [vpn, tunneling, networking, ccna, remote-access, site-to-site]
aliases: [Site-to-Site VPN, Remote Access VPN, Site to Site vs Remote Access]
layer: Overlay / architecture
---

# Site-to-Site-vs-Remote-Access

## Learning objectives

- Contrast site-to-site and remote-access [[VPN]] by topology, identity, and scale
- Map each pattern to common tech ([[IPSec-vs-SSL-VPN]], [[GRE-IPSec-Tunnels]], [[SD-WAN]])
- Design a simple hub-spoke site VPN vs user concentrator mental model
- Troubleshoot differently for “branch down” vs “one user down”

## One-sentence definition

> **Site-to-site VPN** permanently (or dynamically) joins **networks**; **remote-access VPN** connects **individual users/devices** to a network — both create private overlays on shared underlays, but the endpoints and operational models differ.

## Analogy

> Site-to-site is a **private tunnel between two warehouses** — forklifts (subnets) drive through all day without each box logging in. Remote access is an **employee badge + sealed capsule from home**: the person authenticates, then walks the corporate halls. Same subway underlay ([[VPN]]); different ticket types.

## Why it matters

Requirements drive technology: branches need routing and always-on crypto; humans need auth (MFA), posture, and easy clients. Mixing them up in designs causes licensing, firewall, and support pain.

## Deep dive

### Mental model

```text
Site-to-site:
  Branch LAN ── VPN GW ════════════ VPN GW ── HQ LAN
                 (IPsec / SD-WAN overlay)

Remote access:
  Laptop ── Internet ── VPN concentrator ── HQ LAN
            (SSL VPN / IPsec client)
```

### Mechanism — comparison

| Dimension | Site-to-site | Remote access |
|-----------|--------------|---------------|
| Endpoints | Gateways / routers / firewalls | User device + concentrator |
| Identity | PSK/certs on boxes; routing | User/device auth + MFA |
| Routing | Advertise LAN prefixes | Often inject client pool + split routes |
| Topology | Hub-spoke, mesh, DMVPN, SD-WAN | Star to concentrator / PoPs |
| Typical tech | IPsec, GRE+IPsec, [[SD-WAN]], [[MPLS-VPN]] | SSL VPN, client IPsec |
| Scale pain | N² tunnels without hub/SD-WAN | Concurrent users / licenses |

### Dynamic site variants (awareness)

- **DMVPN / FlexVPN:** hub-spoke with spoke-spoke shortcuts  
- **SD-WAN:** orchestrated multi-transport site overlays — [[SD-WAN]]  
- **MPLS L3VPN:** provider-powered “site VPN” without Internet IPsec — [[MPLS-VPN]]

### On the wire

Site: steady IKE/ESP between fixed public IPs (or dynamic spoke updates).  
Remote: intermittent sessions; TCP/443 or IKE from changing home NATs; user traffic from assigned tunnel IP pool.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Architecture | Overlay on [[WAN]] / Internet | Both types |
| Data | Usually L3 tunnels | Inner customer IP |
| Auth | Differs | Boxes vs users |

## Lab exercises

### Lab 1 — Site-to-site IPsec sketch (GNS3)

Two routers with “Internet” cloud between. LAN `192.168.1.0/24` and `192.168.2.0/24`. Build IKEv2/IPsec tunnel; verify interesting traffic interesting ACL mirrors; ping across.

### Lab 2 — Remote-access thought + packet path

List: user auth → tunnel IP → corporate DNS → app VIP. Predict failure if split tunnel excludes the VIP or DNS still points public. Optional: connect any SSL VPN and map routes.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Whole branch offline | Site VPN/IKE/routing | peer reachability, SA, LAN routes both ways |
| One user fails | Creds/MFA/client/posture | auth logs, local time, cert |
| Branch OK, one subnet missing | Interesting traffic / BGP/OSPF over tunnel | selectors, advertised routes |
| Users OK, slow SaaS | Full tunnel hairpin | split tunnel policy |

## Common traps / interview gotchas

- Site-to-site still needs **routes both directions** — crypto alone ≠ reachability.
- Remote access “connected” ≠ correct DNS or routes (classic).
- Don’t put user VPN terminators only in a brittle single DC without HA.
- MPLS VPN is site connectivity but **not** the same as Internet IPsec — different trust/underlay.

## Mastery checklist

- [ ] Draw both topologies from memory
- [ ] Pick tech for branch vs hotel laptop
- [ ] Explain routing/auth differences
- [ ] Cross-link to [[VPN]] and [[IPSec-vs-SSL-VPN]]

## Related notes

- [[VPN]] · [[IPSec-vs-SSL-VPN]] · [[GRE-IPSec-Tunnels]] · [[MPLS-VPN]] · [[SD-WAN]] · [[Default-Gateway]] · [[WAN]]
- ← [[06-Tunneling-and-VPNs/Index|Tunneling & VPNs]] · [[04-Building-a-Network/Index|Building a Network]]
