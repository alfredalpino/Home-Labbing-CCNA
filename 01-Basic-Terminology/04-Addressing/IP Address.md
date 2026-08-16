---
tags: [basic-terminology, networking, ccna, ip]
aliases: [IPv4 Address, IPv6 Address, IP Addr]
layer: Network (Layer 3)
---

# IP Address

## Learning objectives

- Explain IPv4 structure, masks, and CIDR prefix lengths
- Identify private, loopback, link-local, multicast, and other special ranges
- Contrast historical classful addressing with modern CIDR
- Relate IP identity to routing, ARP, and DNS

## One-sentence definition

> An **IP address** is a Layer-3 numerical identifier assigned to an interface (or set of interfaces) so packets can be routed across networks — 32-bit for IPv4, 128-bit for IPv6.

## Analogy

> An IP address is your **postal forwarding code** for the whole country of networks. MAC is your **apartment buzzer code** that only works inside this building’s LAN.

## Why it matters

Every ACL, route, NAT rule, and reachability test keys off IP addresses. DNS names are human convenience; **packets carry IPs**. Mis-set masks and wrong gateways cause more outages than exotic protocol bugs.

## Deep dive

### Mental model

```text
IP address  = where (logical network identity)
MAC address = how on this LAN ([[MAC Address]])
Hostname/DNS= human label ([[DNS]])
```

An address has two views under a mask:

```text
Network portion | Host portion
```

Example: `192.168.10.44/24` → network `192.168.10.0`, host `.44`.

### IPv4 essentials

**CIDR notation:** `address/prefixlen` (e.g. `/24` = mask `255.255.255.0`).

**Historical classes (exam folklore, don’t design with them):**

| Class | Leading bits | Default mask (old) |
|-------|--------------|--------------------|
| A | 0… | /8 |
| B | 10… | /16 |
| C | 110… | /24 |

Modern networks use **CIDR** + VLSM exclusively.

### Special IPv4 ranges you must recognize

| Range | Meaning |
|-------|---------|
| `0.0.0.0/8` | “This network” / unspecified (context-dependent) |
| `127.0.0.0/8` | Loopback |
| `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16` | Private (RFC 1918) |
| `169.254.0.0/16` | Link-local (APIPA) — DHCP failure smell |
| `224.0.0.0/4` | Multicast |
| `255.255.255.255` | Limited broadcast |

### IPv6 contrast (must-know)

- Hex groups, `::` compression
- `fe80::/10` link-local (always), Neighbor Discovery replaces [[ARP]]
- Global unicast typically `2000::/3`
- One interface → many addresses simultaneously is normal

### On the wire / fields

Source/Destination addresses in the IP header of every [[Packet]].

```bash
ifconfig
ip addr                 # Linux
ipconfig getifaddr en0  # macOS helper
route -n get default    # macOS default gateway
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Primary locator/identifier for packets |
| OSI | 3 | Network addressing |

## Lab exercises

### Lab 1 — Decode your LAN addressing

```bash
ifconfig en0
# Identify: IP, mask/prefix, broadcast
# Compute network address and usable host range
```

### Lab 2 — Private vs public

```bash
curl -4 ifconfig.me
# Compare to RFC1918 LAN address — NAT boundary explained
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| 169.254.x.x address | DHCP failed | DHCP server/relay, cable/VLAN |
| Duplicate IP | Conflict | ARP claims, switch logs |
| Same subnet can’t ping | Mask wrong / VLAN | masks both sides, L2 |
| Has IP, no Internet | Gateway/DNS | default route, ping GW, DNS |

## Common traps / interview gotchas

- Hosts need **matching mask** and correct gateway for off-subnet traffic.
- Secondary IPs, anycast, and VIP mobility break naive “one IP = one box” mental models.
- PTR records in DNS are optional; missing reverse DNS ≠ missing IP connectivity.
- `/31` point-to-point and `/32` loopbacks are normal in modern designs.

## Mastery checklist

- [ ] Convert between prefix length and dotted mask fluently
- [ ] List RFC1918 ranges from memory
- [ ] Explain why 169.254 appears
- [ ] Contrast IPv4 ARP vs IPv6 ND in one paragraph

## Related notes

- [[MAC Address]] · [[ARP]] · [[Packet]] · [[Host]] · [[DHCP]] · [[DNS]] · [[ICMP]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
