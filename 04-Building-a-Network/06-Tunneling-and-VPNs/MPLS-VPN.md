---
tags: [vpn, tunneling, networking, ccna, mpls-vpn, l3vpn]
aliases: [MPLS VPN, MPLS L3VPN, L3VPN, MLPS VPN]
layer: Overlay / provider VPN service
---

# MPLS-VPN

## Learning objectives

- Define MPLS L3VPN as customer VRFs stitched across a provider MPLS underlay
- Separate roles: CE, PE, P and explain why P routers don’t need customer routes
- Relate MP-BGP (VPNv4), route targets, and VPN labels to [[MPLS]] + [[VRFs]]
- Contrast MPLS VPN with Internet IPsec site VPN

## One-sentence definition

> An **MPLS VPN** (typically **L3VPN**) delivers private IP connectivity between customer sites by keeping per-customer [[VRFs]] on PE routers and transporting them across an [[MPLS]] core using **MP-BGP** and an extra **VPN label** — not by encrypting over the Internet (unless separately added).

## Analogy

> The provider runs a **shared airport conveyor** ([[MPLS]] underlay). Each airline (customer) has its own **cargo database** (VRF) at every gate office (PE). Bags get **two tags**: one for which gate office city (transport label) and one for which airline pallet (VPN label). Core conveyors (P routers) only read the city tag — they never open airline manifests (customer routes). That’s how many tenants share one backbone without mixing cargo.

## Why it matters

Enterprises buy “MPLS circuits” as managed site-to-site connectivity with SLAs. Engineers must know CE–PE handoff (BGP/OSPF/static), while provider engineers live in VRFs + MP-BGP. Interview question gold: “Do P routers know customer prefixes?” → **No.**

## Deep dive

### Mental model

```text
CE1 --(PE-CE IGP/BGP)-- PE1 ==(MPLS + MP-BGP)== PE2 -- CE2
         VRF CUST                 transport + VPN labels
                                   P routers: swap transport only
```

### Mechanism

| Piece | Role |
|-------|------|
| VRF on PE | Customer routing table / interfaces |
| RD | Makes prefixes unique in BGP |
| RT import/export | Which VRFs accept which routes |
| MP-BGP | Ships VPNv4/VPNv6 routes PE↔PE |
| VPN label | Tells egress PE which VRF/CE |
| Transport label | Gets packet to egress PE across P core |

**PE-CE options:** eBGP (common), OSPF/EIGRP (with capabilities), static — customer doesn’t run MPLS usually.

### MPLS VPN vs IPsec VPN

| | MPLS L3VPN | Internet IPsec site VPN |
|-|------------|-------------------------|
| Underlay | Provider MPLS | Internet |
| Separation | VRF + labels | Crypto + tunnels |
| Encryption | Not inherent | Core feature |
| SLA | Often provider-backed | DIY / SD-WAN |

### On the wire

CE→PE: normal IP. PE→P→PE: MPLS label stack (transport + VPN). Core never needs inner customer IP for forwarding. See also underlay details in [[MPLS]].

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Customer | L3 VPN service | Appear as private WAN |
| Provider data | MPLS | Label switch |
| Provider control | MP-BGP + IGP | VPN + underlay |

## Lab exercises

### Lab 1 — Role play (whiteboard or GNS3 if MPLS-capable)

Label CE1/PE1/P/PE2/CE2. Write which table each device needs. Advertise `10.1.0.0/24` from CE1 and track: VRF → VPNv4 → labels → VRF → CE2.

### Lab 2 — RT thought experiment

Two customers Accidental-Same-RT — show how wrong RT import merges tenants. Document RT as the “policy glue” between VRFs.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| CE can’t ping remote CE | PE-CE route / VRF / RT | `show ip route vrf`, RT import |
| PE has VPNv4, CE doesn’t | PE-CE protocol | BGP neighbor, redistribute |
| Core drop | LDP/SR / MTU | LFIB, underlay to PE loopback |
| Wrong tenant leak | RT misconfig | export/import maps |

## Common traps / interview gotchas

- Filename/typo **MLPS** → correct **MPLS**.
- MPLS VPN ≠ IPsec; privacy is isolation, not encryption-by-default.
- P routers should **not** carry full customer tables — scalability point.
- L2VPN/VPLS/EVPN exist too — this note focuses on classic **L3VPN**.

## Mastery checklist

- [ ] Explain CE/PE/P with the airport-tag analogy
- [ ] State roles of RD, RT, VPN label, transport label
- [ ] Contrast with Internet IPsec site VPN
- [ ] Link [[MPLS]] underlay + [[VRFs]] + [[BGP]]

## Related notes

- [[MPLS]] · [[VRFs]] · [[BGP]] · [[VPN]] · [[Site-to-Site-vs-Remote-Access]] · [[SD-WAN]] · [[WAN]]
- ← [[06-Tunneling-and-VPNs/Index|Tunneling & VPNs]] · [[04-Building-a-Network/Index|Building a Network]]
