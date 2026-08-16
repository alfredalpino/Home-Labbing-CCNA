---
tags: [routing, networking, ccna, vrf, segmentation]
aliases: [VRF, Virtual Routing and Forwarding, VRFs]
layer: Network (Layer 3) / virtualization
---

# VRFs

## Learning objectives

- Define VRF as a virtual routing table instance on one device
- Contrast VRF with [[VLANs]] (L2) and explain VRF-lite vs MPLS VPN VRFs
- Configure simple VRF-lite with separate interfaces/SVIs on Cisco IOS
- Spot route-leak and “same IP, different VRF” designs

## One-sentence definition

> A **VRF** (Virtual Routing and Forwarding) instance is a **separate IP routing table** (and associated FIB / interfaces) on the same router/switch — multiple virtual routers in one box.

## Analogy

> One physical shopping mall ([[Routers|router]]) can host **several separate stores’ back offices**. Each store has its own address book of shipping partners (routing table). Two stores can both have a customer named “10.0.0.5” and never collide — unless someone deliberately opens a door between offices (route leaking / shared services).

## Why it matters

Multi-tenant edges, guest vs corp, OT vs IT, and [[MPLS-VPN]] all use VRFs. Without VRFs you’d need separate physical routers or messy overlapping-NAT hacks. CCNA-level VRF-lite shows up on multilayer switches and firewalls too.

## Deep dive

### Mental model

```text
Physical router
├─ VRF CUST-A  → table A → interfaces in A only see A routes
├─ VRF CUST-B  → table B
└─ global (default) table → classic single RIB
```

Packet ingress on an interface **bound to a VRF** is looked up only in that VRF’s table (unless leaking configured).

### Mechanism — VRF-lite vs MPLS VPN

| Mode | How separation extends |
|------|------------------------|
| **VRF-lite** | VRFs local to a device/domain; no MPLS labels required; separate L3 links/SVIs |
| **MPLS VPN (L3VPN)** | VRFs + MP-BGP + labels across provider core — see [[MPLS-VPN]] / [[MPLS]] |

### Key config ideas (Cisco IOS VRF-lite)

```ios
ip vrf GUEST
 rd 65000:10
! modern IOS-XE often uses: vrf definition GUEST / address-family ipv4
interface GigabitEthernet0/1
 ip vrf forwarding GUEST
 ip address 192.168.10.1 255.255.255.0
```

**Caveat:** adding `ip vrf forwarding` wipes the interface IP — re-add addressing after.

### Route targets & RD (awareness)

In MPLS L3VPN, **Route Distinguisher (RD)** makes prefixes unique in BGP; **Route Targets (RT)** control which VRFs import/export which routes. VRF-lite labs may still show `rd` depending on IOS — focus on **table separation** first.

### On the wire

VRF itself adds no header. Separation is **control/data plane context** on the device. Across an MPLS core, labels + VPNv4 BGP carry the context — that’s [[MPLS-VPN]], not bare VRF-lite.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI / TCP-IP | Network (L3) | Multiple virtual L3 contexts |
| Contrast | [[VLANs]] = L2 broadcast domains | VRF = L3 routing domains |

## Lab exercises

### Lab 1 — Two VRFs, overlapping IPs (GNS3)

On one L3 switch/router:

1. Create VRF `RED` and `BLUE`.
2. Put two interfaces (or SVIs) in RED with `10.0.0.0/24`; two in BLUE with the **same** `10.0.0.0/24`.
3. Hosts in RED ping each other; BLUE ping each other; **cross-VRF ping fails**.
4. `show ip route vrf RED` vs `show ip route vrf BLUE`.

### Lab 2 — Shared services leak (careful)

Export a single route (e.g. DNS `10.9.9.9`) from a SERVICES VRF into RED/BLUE with statics or BGP import — document the security implication (shared path = shared risk).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Ping fails, IP looks right | Host in wrong VRF / interface not in VRF | `show vrf`, iface VRF binding |
| Route missing in VRF | Learned in global only | `show ip route vrf X` |
| Config wiped IP | VRF apply order | Re-address after `vrf forwarding` |
| Unexpected reachability | Route leak / shared RT | Import maps, static leaks |

## Common traps / interview gotchas

- VLAN ≠ VRF: VLAN separates broadcast domains; VRF separates **routing tables**.
- Same subnet in two VRFs is OK; connecting them without intent is a security bug.
- Management often lives in global or a MGMT VRF — don’t lock yourself out.
- “VRF” on firewalls/cloud is the same idea: routing isolation.

## Mastery checklist

- [ ] Define VRF in one sentence with the mall-store analogy
- [ ] Configure VRF-lite and prove overlapping IPs are isolated
- [ ] Contrast VRF-lite vs MPLS L3VPN
- [ ] Explain RD/RT at awareness level

## Related notes

- [[VLANs]] · [[MPLS]] · [[MPLS-VPN]] · [[BGP]] · [[Static-vs-Dynamic-Routing]] · [[Routers]] · [[IP Address]]
- ← [[04-Routing/Index|Routing]] · [[04-Building-a-Network/Index|Building a Network]]
