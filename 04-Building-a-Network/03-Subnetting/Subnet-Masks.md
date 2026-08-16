---
tags: [subnetting, networking, ccna, ipv4]
aliases: [Subnet Mask, Netmask, Subnet Masks]
layer: Network (Layer 3) — addressing math
---

# Subnet Masks

## Learning objectives

- Explain what a subnet mask does to an [[IP Address]] (network vs host portion)
- Convert between dotted‑decimal masks and prefix lengths ([[CIDR]])
- Compute network, broadcast, and usable host ranges
- Spot mask mismatches as a top outage cause

## One-sentence definition

> A **subnet mask** is a 32‑bit pattern (IPv4) paired with an address that marks which bits identify the **network/subnet** and which bits identify the **host**.

## Analogy

> An IP address is a **full serial number** on a warehouse bin. The subnet mask is a **stencil** laid over that serial: the part showing through the stencil is the **aisle code** (subnet); the covered part is the **bin number** (host). Same stencil on two labels → same aisle → same subnet.

## Why it matters

Every interface, ACL, route, and DHCP pool depends on correct masks. A host with `192.168.1.10/24` and a gateway thought to be in `/16` will ARP forever for remote hosts. Subnetting exams are mask fluency in disguise.

## Deep dive

### Mental model

```text
IP      11000000.10101000.00000001.00001010   192.168.1.10
Mask    11111111.11111111.11111111.00000000   255.255.255.0
        \__________ network __________/\host/

Network = IP AND Mask  → 192.168.1.0
Broadcast = network | ~mask → 192.168.1.255
Usable hosts = 192.168.1.1 … 192.168.1.254  (in ordinary /24)
```

### Common masks

| Prefix | Dotted mask | Usable hosts* |
|--------|-------------|---------------|
| `/8` | `255.0.0.0` | 16,777,214 |
| `/16` | `255.255.0.0` | 65,534 |
| `/24` | `255.255.255.0` | 254 |
| `/25` | `255.255.255.128` | 126 |
| `/26` | `255.255.255.192` | 62 |
| `/27` | `255.255.255.224` | 30 |
| `/28` | `255.255.255.240` | 14 |
| `/30` | `255.255.255.252` | 2 (point‑to‑point) |
| `/32` | `255.255.255.255` | host route |

\*Classic IPv4 Ethernet math; `/31` exists for p2p (RFC3021).

### Mechanism — finding network & broadcast

1. Convert IP + mask to binary (or use known octet boundaries).
2. Network address = bitwise AND.
3. Broadcast = set all host bits to 1.
4. First usable = network + 1; last usable = broadcast − 1 (typical LAN).

Magic octet shortcuts: for mask `255.255.255.X`, block size = `256 − X`.

### On the wire / fields

The mask is **not** a field in every data packet. Hosts and routers use configured masks/prefixes to decide: *local subnet?* → ARP ([[IP-vs-MAC-vs-ARP]]); *else?* → send to gateway. Wrong mask = wrong decision = wrong ARP target.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Defines subnet boundaries for L3 |
| OSI | Network | Same — local vs remote delivery |

## Lab exercises

### Lab 1 — Compute by hand

For `172.16.5.77` mask `255.255.255.224` (`/27`):

- Network?
- Broadcast?
- Usable range?
- Is `172.16.5.64` usable?

### Lab 2 — See your OS mask

```bash
# Linux
ip -4 addr
# macOS
ifconfig | grep 'inet '

# Check local vs remote decision
ip route get 8.8.8.8
ip route get 192.168.1.50   # adjust to your LAN
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Same VLAN can’t ping | Mask mismatch | both hosts’ masks/gateways |
| ARP for remote IPs | Mask too short (too many host bits) | host thinks remote is local |
| DHCP clients odd | Pool/mask mismatch | scope prefix vs interface |
| “/24 vs 255.255.0.0” | Human conversion error | verify prefix ↔ dotted |

## Common traps / interview gotchas

- Mask `255.255.255.256` is invalid — octets max 255.
- Non‑contiguous masks (e.g. `255.0.255.0`) are illegal in modern IP.
- Gateway must be **inside** the host’s subnet as defined by *that host’s* mask.
- `/30` has 2 usable — perfect for serial/p2p; don’t put a LAN of 10 hosts there.
- IPv6 uses prefix lengths, not dotted masks — see [[CIDR]] / [[IPv4-vs-IPv6]].

## Mastery checklist

- [ ] Convert `/20`–`/30` to dotted masks from memory
- [ ] Compute network/broadcast for a random /27
- [ ] Explain how mask errors cause ARP weirdness
- [ ] Relate mask to [[CIDR]] prefix notation
- [ ] Design a /24 split into two /25s on paper

## Related notes

- [[CIDR]] · [[VLSM]] · [[Supernetting]] · [[IP Address]] · [[IP-vs-MAC-vs-ARP]] · [[Public-vs-Private-Addresses]] · [[DHCP]]
- ← [[03-Subnetting/Index|Subnetting]]
