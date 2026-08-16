---
tags: [subnetting, networking, ccna, vlsm]
aliases: [VLSM, Variable Length Subnet Masking]
layer: Network (Layer 3) — efficient addressing
---

# VLSM

## Learning objectives

- Define VLSM as using **different prefix lengths** inside one addressing plan
- Carve a parent block into unequal subnets sized to host counts
- Avoid overlaps and wasted space from fixed‑length (FLSM) habits
- Practice exam‑style allocation tables

## One-sentence definition

> **VLSM** (Variable Length Subnet Masking) assigns subnets of **different sizes** (different [[CIDR]] lengths) from a single address pool so each segment gets “just enough” addresses.

## Analogy

> You’re catering a party from one **sheet cake** (parent prefix). FLSM cuts every piece the same size — wasteful for a table of two. VLSM cuts a **big slab** for the LAN of 100 hosts, a **thin slice** for a /30 WAN link, and medium pieces for medium VLANs — same cake, smarter knife ([[Subnet-Masks]]).

## Why it matters

Real networks rarely need identical subnet sizes. Point‑to‑point links want `/30` or `/31`; user VLANs want `/24` or `/23`; management might want `/28`. VLSM is how you respect [[CIDR]] and conserve IPv4 (still scarce internally when overlapping orgs merge).

## Deep dive

### Mental model

```text
Parent: 192.168.10.0/24

Need:
  VLAN A 100 hosts → /25 (128 addrs) → 192.168.10.0/25
  VLAN B  50 hosts → /26 (64)        → 192.168.10.128/26
  VLAN C  25 hosts → /27 (32)        → 192.168.10.192/27
  P2P link 2 hosts → /30             → 192.168.10.224/30
  ... remaining space for growth
```

### Mechanism — allocation algorithm (exam friendly)

1. List segments by **required hosts** (descending).
2. Pick smallest prefix that fits (`hosts ≤ 2^(32-p) − 2` for classic LAN).
3. Allocate next aligned block; never overlap.
4. Document network, mask, first/last host, broadcast.
5. Leave free space for growth if possible.

**Alignment rule:** a `/26` must start on a multiple of 64 in the last octet, `/27` on 32, etc.

### FLSM vs VLSM

| Approach | Idea | Waste |
|----------|------|-------|
| FLSM | All subnets same size | High if needs differ |
| VLSM | Size per need | Lower; more planning |

### On the wire / fields

VLSM is a **planning** concept. Packets don’t carry “VLSM”; each interface simply has its own prefix. Mis‑documented plans cause overlaps — two interfaces with colliding ranges = routing chaos.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Efficient subnet design |
| Ops | Addressing plan | Feeds DHCP, ACLs, routes |

## Lab exercises

### Lab 1 — Carve `10.20.0.0/22`

Requirements:

- 1× ~500 hosts
- 2× ~100 hosts
- 3× point‑to‑point `/30`

Produce a table: name, CIDR, mask, range. Verify no overlaps with `python3` `ipaddress` or paper.

### Lab 2 — Implement two sizes in a lab

On a router, put `192.168.1.0/25` on G0/0 and `192.168.1.128/26` on G0/1. Confirm hosts in each VLAN only ARP locally; traceroute between them goes through the router L3 interface.

```text
interface GigabitEthernet0/0
 ip address 192.168.1.1 255.255.255.128
interface GigabitEthernet0/1
 ip address 192.168.1.129 255.255.255.192
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Overlap / duplicate routes | Bad VLSM carve | spreadsheet alignment |
| Hosts “out of range” | Undersized subnet | host count vs prefix |
| DHCP exhausted early | Plan ignored growth | expand or re‑carve |
| P2P using /24 | FLSM habit | redesign with /30 |

## Common traps / interview gotchas

- Always allocate **largest first** to reduce fragmentation mistakes.
- Usable hosts = `2^h − 2` (usually) — don’t forget network/broadcast.
- `/30` waste of 2 addresses is OK; putting a /24 on a serial link is not.
- VLSM requires classless routing protocols (anything modern — OSPF, EIGRP, BGP).
- Overlapping VLSM + summarization ([[Supernetting]]) needs clean boundaries.

## Mastery checklist

- [ ] Explain VLSM vs FLSM with the cake analogy
- [ ] Carve a /24 into mixed /25,/26,/30 without overlap
- [ ] State alignment rules for /25–/30
- [ ] Build an allocation table an examiner can grade
- [ ] Implement two different masks on router interfaces

## Related notes

- [[Subnet-Masks]] · [[CIDR]] · [[Supernetting]] · [[IP Address]] · [[DHCP]] · [[Routers]]
- ← [[03-Subnetting/Index|Subnetting]]
