---
tags: [nat, networking, ccna, ip-addressing]
aliases: [NAT vs PAT, NAT and PAT Comparison]
layer: Network (Layer 3) — edge translation
---

# NAT vs PAT

## Learning objectives

- Define NAT as rewriting IP addresses at a boundary
- Contrast one‑to‑one NAT styles with PAT (NAT overload) many‑to‑one using ports
- Know when static, dynamic, and overload apply
- Link to [[Public-vs-Private-Addresses]] and deeper notes [[Static-vs-Dynamic-NAT]], [[PAT-NAT-Overload]], [[NAT64]]

## One-sentence definition

> **NAT** changes IP addresses in packets as they cross a device; **PAT** (NAT overload) is the common many‑to‑one form that also rewrites **L4 ports** so many private hosts share one public IP.

## Analogy

> NAT is the office **receptionist rewriting visitor badges**. Classic one‑to‑one NAT issues a unique lobby badge per employee (1:1). **PAT** is one shared lobby badge number with a **different sticker** (port) per conversation so replies still find the right desk.

## Why it matters

Home Wi‑Fi, most enterprise Internet edges, and countless CCNA labs depend on PAT. Confusing “NAT” (umbrella) with “PAT” (specific method) causes wrong designs and wrong interview answers. IPv4 scarcity made translation normal; understanding *what* is rewritten keeps troubleshooting sane.

## Deep dive

### Mental model

```text
Inside (private)          Edge NAT/PAT           Outside (public)
10.1.1.10:52344  ──►  rewrite src IP[/port] ──►  203.0.113.5:40001
                 ◄──  reverse on replies   ◄──
```

### Comparison table

| Trait | NAT (broad / 1:1 styles) | PAT / overload |
|-------|--------------------------|----------------|
| Addresses | Map IP → IP | Many IPs → one (or few) IP |
| Ports | Often unchanged | Source ports remapped |
| Typical use | Servers, 1:1 DMZ | Consumer & enterprise egress |
| State table | Address mappings | Address + port + protocol |
| Scalability | Needs public IP per inside | Thousands of flows per public IP |

### Flavors under the NAT umbrella

| Flavor | Note |
|--------|------|
| Static NAT | Fixed 1:1 — [[Static-vs-Dynamic-NAT]] |
| Dynamic NAT | Pool of publics, still ~1:1 while in use — [[Static-vs-Dynamic-NAT]] |
| PAT / overload | Many:1 with ports — [[PAT-NAT-Overload]] |
| NAT64 | Family translation v6↔v4 — [[NAT64]] |

### Mechanism

1. Interesting traffic matches an ACL / rule (“inside” → “outside”).
2. Device allocates a mapping (static or from pool / overload table).
3. Rewrites source (SNAT) or destination (DNAT / port‑forward) as configured.
4. Reverse rewrite on return path using the state table.

### On the wire / fields

Changed fields commonly: IP source and/or destination; for PAT also TCP/UDP source port (sometimes destination for port forwards). IP header checksum and L4 checksums are recalculated. End hosts usually **don’t know** translation happened — only the edge and captures on both sides reveal it.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI / TCP-IP | L3 | IP rewrite |
| OSI / TCP-IP | L4 | Port rewrite for PAT |
| Architecture | Edge | Boundary between [[Public-vs-Private-Addresses]] |

## Lab exercises

### Lab 1 — Prove PAT on a home gateway

```bash
# Inside IP
ip -4 addr   # or ifconfig

# Outside IP
curl -4 ifconfig.me
```

Start a few HTTPS flows; on a lab router use `show ip nat translations` (IOS) and note unique ports sharing one public IP.

### Lab 2 — IOS conceptual config contrast

```text
! Static 1:1 idea
ip nat inside source static 10.1.1.10 203.0.113.10

! PAT overload idea
ip nat inside source list 1 interface GigabitEthernet0/0 overload
```

Sketch packets before/after for each.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Outbound OK, inbound fail | No static/DNAT / CGNAT | mappings; WAN IP type |
| Some apps fail (VoIP/FTP) | ALG / port expectations | fix ALG or use tunnels |
| Translations exhaust | PAT port space / idle timers | `show ip nat statistics` |
| Wrong inside/outside | Interface nat direction | `ip nat inside/outside` |

## Common traps / interview gotchas

- “NAT” in casual speech often means **PAT**.
- NAT is not a firewall — it’s translation; pair with ACL/stateful filter.
- Breaking end‑to‑end IP transparency complicates IPSec and logging — design consciously.
- Dynamic NAT without overload still consumes one public per inside host — doesn’t solve scarcity like PAT.
- Hairpin/NAT loopback needed when LAN clients use the public VIP.

## Mastery checklist

- [ ] Define NAT vs PAT in one sentence each
- [ ] Draw SNAT for a private client browsing the web
- [ ] Know which notes cover static, dynamic, overload, NAT64
- [ ] Read a NAT translation table entry (inside global / local)
- [ ] Explain why ports appear in PAT entries

## Related notes

- [[Static-vs-Dynamic-NAT]] · [[PAT-NAT-Overload]] · [[NAT64]] · [[Public-vs-Private-Addresses]] · [[IP Address]] · [[Routers]] · [[TCP]] · [[UDP]]
- ← [[01-NAT/Index|NAT]] · [[02-IP-Addressing/Index|IP Addressing]]
