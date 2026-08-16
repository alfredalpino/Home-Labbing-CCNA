---
tags: [routing-protocols, networking, ccna, bgp]
aliases: [Border Gateway Protocol, BGP4, BGP]
layer: Network (Layer 3) / exterior routing
---

# BGP

## Learning objectives

- Explain BGP as the Internet’s path-vector protocol between ASes
- Contrast iBGP vs eBGP and why BGP is policy-driven, not “shortest bandwidth”
- Read the core best-path idea (Local Pref, AS_PATH, MED — awareness order)
- Bring up a simple eBGP session in a lab and verify prefixes

## One-sentence definition

> **BGP** (Border Gateway Protocol) is the **path-vector** routing protocol that exchanges reachability **between autonomous systems**, choosing paths primarily by **policy attributes**, not by simple IGP cost.

## Analogy

> IGPs are **city street GPS** (fastest local roads). BGP is **international diplomacy and airline alliances**. Countries (ASNs) announce which destinations they can reach and via which alliance path (AS_PATH). You pick partners for politics, contracts, and “don’t transit my enemy,” not because the runway is 3 meters shorter. The route is a **passport stamp trail**, not an OSPF blueprint.

## Why it matters

The Internet runs on BGP. Enterprises use it at dual-ISP edges, data centers, and [[MPLS-VPN]] (MP-BGP). CCNA expects solid *concepts*; deep attribute mastery grows into CCNP. Misconfigured BGP can blackhole or leak routes — treat labs carefully.

## Deep dive

### Mental model

```text
TCP session :179 between peers
  UPDATE: NLRI prefixes + path attributes
  → BGP table → best path → (maybe) RIB/FIB

AS 65001 ──eBGP── AS 65002
   │ iBGP
  RR / full mesh among iBGP speakers
```

### Mechanism — must-know pieces

| Topic | Idea |
|-------|------|
| ASN | Autonomous System Number (public or private) |
| eBGP | Between different ASNs; usually TTL 1; AD 20 |
| iBGP | Same ASN; AD 200; needs full mesh or Route Reflector / confederation |
| NLRI | Prefixes advertised |
| AS_PATH | Sequence of ASNs — loop detection + prefer shorter (default) |
| Next-hop | Who to send to (eBGP changes; iBGP often leaves eBGP next-hop) |
| LocPrp / Local Pref | Prefer exit within AS (higher better) |
| MED | Hint to external AS (lower better) — weak signal |

**Best path (simplified mental order):** prefer highest Weight (Cisco) → Local Pref → local originated → shortest AS_PATH → … → lowest IGP to next-hop → … (full list is longer — know that **policy beats bandwidth**).

### On the wire

- TCP port **179**
- OPEN / KEEPALIVE / UPDATE / NOTIFICATION messages
- Can carry IPv4, IPv6, VPNv4 (MP-BGP AFI/SAFI) — see [[MPLS-VPN]]

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Application/control | BGP over TCP | Inter-AS (and overlay VPN) control plane |
| Forwarding | L3 | Uses selected next hops |
| Vs IGP | Policy path-vector | IGP = topology/cost inside AS |

## Lab exercises

### Lab 1 — Two-AS eBGP (GNS3)

R1 in AS 65001, R2 in AS 65002, link `10.0.0.0/30`.

```ios
router bgp 65001
 bgp router-id 1.1.1.1
 neighbor 10.0.0.2 remote-as 65002
 network 192.168.1.0 mask 255.255.255.0
```

Mirror on R2. Verify: `show ip bgp summary` (Established), `show ip bgp`, ping between LANs.

### Lab 2 — AS_PATH visibility

Add AS 65003 behind R2; advertise a prefix. On R1 read `show ip bgp` and explain the AS_PATH stamps. Optionally prefer a longer path with route-map (awareness).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Idle / Active | TCP 179 blocked, wrong IP/AS | `show ip bgp summary`, ACL, iface |
| Established, no routes | Network not in RIB / next-hop unreachable | `show ip bgp`, `next-hop-self`, IGP |
| Prefers “worse” ISP | Local Pref / weight / AS_PATH policy | attributes in `show ip bgp` |
| iBGP learned but not used | Sync / next-hop / AD | IGP to next-hop, route-maps |

## Common traps / interview gotchas

- BGP does **not** minimize latency by default — policy first.
- iBGP AD 200 loses to OSPF — design redistribution carefully.
- `network` command advertises only if an exact match exists in the routing table (classic IOS behavior).
- Route leaks (announcing too much) can disrupt the Internet — lab with private ASNs.
- BGP ≠ VPN by itself; MPLS VPN *uses* MP-BGP as signaling.

## Mastery checklist

- [ ] Explain AS, eBGP vs iBGP, TCP/179
- [ ] Establish eBGP and verify a prefix
- [ ] Read AS_PATH on a BGP table entry
- [ ] Contrast BGP policy vs OSPF cost

## Related notes

- [[OSPF]] · [[MPLS]] · [[MPLS-VPN]] · [[VRFs]] · [[Static-vs-Dynamic-Routing]] · [[WAN]] · [[TCP]]
- ← [[01-Routing-Protocols/Index|Routing Protocols]] · [[04-Routing/Index|Routing]]
