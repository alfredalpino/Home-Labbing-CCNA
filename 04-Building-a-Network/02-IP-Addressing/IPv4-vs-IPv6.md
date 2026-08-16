---
tags: [ip-addressing, networking, ccna, ipv4, ipv6]
aliases: [IPv4 vs IPv6, Dual Stack, IPv4 and IPv6]
layer: Network (Layer 3)
---

# IPv4 vs IPv6

## Learning objectives

- Contrast IPv4 and IPv6 address formats, size, and notation
- Explain dual‑stack operation and when each family is used
- Compare key header differences that affect MTU, options, and troubleshooting
- Link concepts back to [[IP Address]] and forward to [[NAT64]] / [[Public-vs-Private-Addresses]]

## One-sentence definition

> **IPv4** and **IPv6** are two Internet Protocol generations: 32‑bit dotted‑decimal addresses vs 128‑bit colon‑hex addresses — often run together (**dual stack**) so hosts can reach both worlds.

## Analogy

> IPv4 is the city’s original **5‑digit zip codes** — almost out of unique codes, so buildings share mailrooms ([[NAT-vs-PAT]]). IPv6 is a **planet‑scale postal grid** with room for every doorbell. Dual stack is a building that accepts **both zip styles** until the old city finishes upgrading.

## Why it matters

The public IPv4 pool is exhausted; enterprises still run oceans of IPv4 internally. You will design, ACL, and troubleshoot **both**. CCNA expects you to read IPv6 addresses, know RA/DHCPv6 at a high level, and understand why NAT exists mainly in the IPv4 story.

## Deep dive

### Mental model

```text
                    Dual-stack host
                 ┌──────────────────┐
   App ────────►│  Happy Eyeballs / │
                 │  getaddrinfo()    │
                 └─────┬──────┬─────┘
                       │      │
                   IPv4 path  IPv6 path
                       │      │
                       ▼      ▼
                  203.0.113.10  2001:db8::10
```

### Address formats

| Trait | IPv4 | IPv6 |
|-------|------|------|
| Length | 32 bits | 128 bits |
| Example | `192.0.2.10` | `2001:db8::10` |
| Text length | `/0`–`/32` | `/0`–`/128` |
| Broadcast | Yes (limited) | No — multicast / anycast |
| Common host config | DHCP / static | SLAAC + RA, DHCPv6, static |
| Link‑local | `169.254.0.0/16` | `fe80::/10` (required) |

IPv6 shortening: drop leading zeros; one `::` for longest zero run. Example: `2001:0db8:0000:0000:0000:0000:0000:0010` → `2001:db8::10`.

### Header differences (practical)

| Topic | IPv4 | IPv6 |
|-------|------|------|
| Header size | 20 B + options | Fixed 40 B + extension headers |
| Checksum | Header checksum | No header checksum (L4 does work) |
| Fragmentation | Routers may fragment | End hosts fragment; routers don’t |
| Options | In main header | Extension headers |
| Address scarcity | NAT ubiquitous | NAT rare; plenty of globals |

### When to use which

- **IPv4 only:** legacy lab gear, old IoT, some enterprise islands.
- **IPv6 only:** greenfield mobile/ISP access, some cloud‑native edges (still uncommon end‑to‑end for enterprise apps).
- **Dual stack (most common):** hosts and routers speak both; DNS returns A + AAAA; policy decides preference.
- **Translation:** when v6 clients must reach v4‑only servers → [[NAT64]] (and DNS64).

### On the wire / fields

IPv4 header highlights: Version=4, IHL, Total Length, TTL, Protocol, Source/Dest. IPv6: Version=6, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, 128‑bit addresses. Ethernet ethertype `0x0800` = IPv4, `0x86DD` = IPv6.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Two coexisting L3 protocols |
| OSI | Network (L3) | Addressing + routing per family |
| DNS | App helper | A vs AAAA records steer stack choice |

## Lab exercises

### Lab 1 — See both stacks on your host

```bash
# Linux
ip -4 addr
ip -6 addr
ip -4 route
ip -6 route

# macOS
ifconfig | egrep 'inet |inet6 '
```

Note link‑local `fe80::` on every up interface — normal for IPv6.

### Lab 2 — DNS A vs AAAA

```bash
dig example.com A +short
dig example.com AAAA +short
curl -4 -I https://example.com
curl -6 -I https://example.com   # may fail if no v6 path
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| App slow then works | Happy Eyeballs race / broken v6 | disable v6 test; AAAA reachability |
| ping6 fails, ping4 OK | No v6 route / RA blocked | `ip -6 route`; firewall ICMPv6 |
| “No IPv6” on LAN | RA not allowed on switch/WLAN | MLD/RA guard settings |
| Broken only some sites | One family filtered | compare A vs AAAA paths |

## Common traps / interview gotchas

- IPv6 link‑local is **per interface** — pings often need `%iface` (`ping6 fe80::1%eth0`).
- There is **no broadcast** in IPv6; “broadcast” questions need multicast answers.
- NAT is not “the IPv6 plan” — address space + privacy extensions replace most overload use cases.
- Dual stack doubles ACL/route work — missing v6 ACE = silent hole.
- `localhost` is `127.0.0.1` **and** `::1`.

## Mastery checklist

- [ ] Read and compress/expand an IPv6 address
- [ ] Explain dual stack vs translation ([[NAT64]])
- [ ] Name two header differences that change ops behavior
- [ ] Verify A/AAAA and test `-4`/`-6` reachability
- [ ] Tie back to [[IP Address]] special ranges for both families

## Related notes

- [[IP Address]] · [[Public-vs-Private-Addresses]] · [[IP-vs-MAC-vs-ARP]] · [[NAT64]] · [[CIDR]] · [[Subnet-Masks]] · [[DNS]] · [[ICMP]]
- ← [[02-IP-Addressing/Index|IP Addressing]]
