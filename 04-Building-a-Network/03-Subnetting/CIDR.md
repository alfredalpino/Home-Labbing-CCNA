---
tags: [subnetting, networking, ccna, cidr]
aliases: [CIDR, Classless Inter-Domain Routing, Slash Notation]
layer: Network (Layer 3) — addressing & routing
---

# CIDR

## Learning objectives

- Explain CIDR as classless prefix‑length addressing (vs old class A/B/C)
- Read and write slash notation (`192.0.2.0/24`)
- Relate CIDR to [[Subnet-Masks]] and route aggregation ([[Supernetting]])
- Use CIDR blocks correctly in ACLs and cloud security groups

## One-sentence definition

> **CIDR** (Classless Inter‑Domain Routing) identifies networks by an **address + prefix length** (e.g. `/24`), replacing rigid classful boundaries so subnets and aggregates can be any valid length.

## Analogy

> Old classful IP was a school that only sold **fixed meal sizes** (Class A/B/C trays). CIDR is **à la carte**: you order exactly how many bits of “network” you need — a `/30` nibble or a `/12` banquet — and the kitchen ([[Routers]]) understands the slash on the ticket.

## Why it matters

Every modern route, VPN, firewall rule, and CCNA question uses CIDR. Classful thinking wastes space and breaks summarization. If you still say “Class C network” as a habit, retrain to **prefix length**.

## Deep dive

### Mental model

```text
Classful (legacy):  first octet → fixed mask (/8, /16, /24)
CIDR (modern):      you choose prefix length; classes irrelevant

192.0.2.0/24   → 256 addresses (254 usable typical LAN)
192.0.2.0/25   → left half of that block
192.0.2.0/23   → aggregate of two /24s (see [[Supernetting]])
```

### Mechanism — prefix length

Prefix length = number of **1** bits in the mask.

| Slash | Mask | Block size (addresses) |
|-------|------|-------------------------|
| `/32` | host | 1 |
| `/24` | `255.255.255.0` | 256 |
| `/16` | `255.255.0.0` | 65,536 |
| `/0` | default | entire IPv4 space |

**Longest prefix match:** routers prefer more specific routes (`/28` wins over `/16`) when forwarding.

### CIDR in ACLs and labs

```text
! IOS wildcard is inverse of mask — not the same as CIDR slash
access-list 10 permit 192.0.2.0 0.0.0.255    ! matches /24
```

Cloud: `10.0.0.0/8` in a security group means the whole RFC1918 `/8` — know your intent.

### On the wire / fields

CIDR isn’t a packet header field; it’s how humans and control planes **describe** sets of addresses. BGP advertises prefixes with lengths; data packets still carry full 32‑bit IPs.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Prefixes define routes & subnets |
| Routing | Control plane | CIDR aggregates shrink tables |

## Lab exercises

### Lab 1 — Slash ↔ mask drills

Convert both ways: `/19`, `/22`, `/26`, `/29` ↔ dotted masks. Check with:

```bash
python3 - <<'PY'
import ipaddress
for p in ["192.0.2.0/24","192.0.2.0/26","10.0.0.0/12"]:
    n=ipaddress.ip_network(p, strict=False)
    print(n, n.netmask, n.num_addresses)
PY
```

### Lab 2 — Longest prefix match story

Given routes `10.1.0.0/16` and `10.1.1.0/24`, where does `10.1.1.50` go? Where does `10.1.2.50` go? Write the answer, then verify on a lab router with `show ip route`.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| ACL too broad/narrow | Slash vs wildcard confusion | convert carefully |
| Overlapping VPCs/VPNs | Same CIDR reused | [[Public-vs-Private-Addresses]] planning |
| Route not used | Less specific / wrong AD | `show ip route` specificity |
| “Class C” mis‑size | Classful habit | redesign with needed prefix |

## Common traps / interview gotchas

- Classful A/B/C is historical — **CIDR is the rule**.
- `/24` is not “Class C”; Class C *was* `/24` by default, but `/24` can come from any parent.
- Wildcard mask `0.0.0.255` ≈ match `/24` — don’t paste CIDR into IOS ACL blindly.
- IPv6 is CIDR‑native (`2001:db8::/32`) — no dotted masks.
- Overlapping CIDRs in lab diagrams = guaranteed routing pain.

## Mastery checklist

- [ ] Explain CIDR vs classful in one minute
- [ ] Convert slash ↔ mask for common prefixes
- [ ] Apply longest prefix match to a mini routing table
- [ ] Write a /24 and /25 correctly in ACL/cloud syntax
- [ ] Link CIDR aggregates to [[Supernetting]]

## Related notes

- [[Subnet-Masks]] · [[VLSM]] · [[Supernetting]] · [[IP Address]] · [[IPv4-vs-IPv6]] · [[Routers]]
- ← [[03-Subnetting/Index|Subnetting]]
