---
tags: [nat, networking, ccna, ip-addressing]
aliases: [Static NAT, Dynamic NAT, Static vs Dynamic NAT]
layer: Network (Layer 3) — edge translation
---

# Static vs Dynamic NAT

## Learning objectives

- Configure the mental model for **static** 1:1 vs **dynamic** pool NAT
- Know Cisco IOS “inside local / inside global” terminology
- Choose static for published servers and dynamic for temporary 1:1 needs
- Contrast both with [[PAT-NAT-Overload]] when public IPs are scarce

## One-sentence definition

> **Static NAT** permanently maps one inside address to one outside address; **dynamic NAT** hands out outside addresses from a pool for the duration of traffic, still roughly one‑to‑one while the mapping exists.

## Analogy

> Static NAT is a **reserved parking spot** with your name on it — always the same space (public IP) for that car (private IP). Dynamic NAT is a **visitor lot**: first come, first served from a pool of spaces; when you leave, someone else can take that spot. Neither is the crowded **valet ticket system** of [[PAT-NAT-Overload]] (many cars, one curb address).

## Why it matters

CCNA exams test the vocabulary (inside local/global) and the pool vs static choice. In production, static NAT (or 1:1 cloud EIPs) publishes servers; dynamic 1:1 is rarer today because PAT stole the mainstream, but the concepts underpin every translation discussion.

## Deep dive

### Mental model — Cisco address terms

```text
Inside network                         Outside network
[Inside local]  ←── NAT device ──►  [Inside global]
  10.1.1.10                           203.0.113.10

Outside host sees inside global.
Inside host often uses inside local as its real IP.
```

| Term | Meaning |
|------|---------|
| Inside local | Real IP of inside host (often RFC1918) |
| Inside global | Public (or outside) IP that represents that host |
| Outside local / global | Rare in simple labs — how inside sees outside hosts |

### Static NAT

- Permanent mapping in config.
- Inbound and outbound can use the same 1:1 binding (with ACLs).
- Typical: DMZ web server `10.50.1.10` ↔ `203.0.113.10`.

```text
ip nat inside source static 10.50.1.10 203.0.113.10
```

### Dynamic NAT

- Define ACL matching inside hosts + pool of public IPs.
- First packet grabs a free global from the pool; idle timeout returns it.
- Still **not** many‑to‑one — if the pool is empty, new connections fail.

```text
access-list 1 permit 10.1.1.0 0.0.0.255
ip nat pool PUB 203.0.113.10 203.0.113.20 netmask 255.255.255.0
ip nat inside source list 1 pool PUB
```

### Mechanism

1. Classify traffic (inside → outside).
2. Static: always same rewrite. Dynamic: allocate from pool if needed.
3. Install translation; reverse for return packets.
4. Dynamic entry ages out → address returns to pool.

### On the wire / fields

Source (or destination) IP changes at the NAT boundary. Ports usually unchanged in pure static/dynamic NAT (unlike PAT). Captures inside vs outside show different IPs, same L4 ports for a given flow.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Rewrites L3 addresses |
| Design | Edge / DMZ | Publish or temporarily map hosts |

## Lab exercises

### Lab 1 — Packet Tracer / CML static NAT

1. Inside host `10.1.1.10`, outside “ISP” loopback `203.0.113.1`.
2. Configure static NAT to `203.0.113.10`.
3. Ping from outside to inside global; verify `show ip nat translations`.

### Lab 2 — Dynamic pool exhaustion thought‑lab

Give a pool of **two** publics and **three** inside hosts generating traffic. Predict the third host’s failure mode, then confirm with `show ip nat translations` and `show ip nat statistics`. Contrast with adding `overload` ([[PAT-NAT-Overload]]).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Static not reachable inbound | ACL / missing outside | `show ip nat translations`; routes back |
| Dynamic fails under load | Pool exhausted | enlarge pool or use overload |
| Wrong host mapped | Overlapping static/ACL | translation table; ACL order |
| One‑way traffic | Routing asymmetry | return path to inside global |

## Common traps / interview gotchas

- Dynamic NAT ≠ PAT — without `overload` you still need many publics.
- Inside/outside interface markers wrong → silent failure.
- Static NAT still needs **routing** and **security policy** to the global IP.
- “Inside local” is not always private — terminology is about topology side, not RFC1918.
- Clearing translations (`clear ip nat translation *`) drops flows — lab only.

## Mastery checklist

- [ ] Define inside local vs inside global
- [ ] Write a static NAT one‑liner in IOS style
- [ ] Explain dynamic pool exhaustion
- [ ] Choose static vs dynamic vs PAT for a web server and for 500 clients
- [ ] Read `show ip nat translations` correctly

## Related notes

- [[NAT-vs-PAT]] · [[PAT-NAT-Overload]] · [[NAT64]] · [[Public-vs-Private-Addresses]] · [[IP Address]] · [[Routers]]
- ← [[01-NAT/Index|NAT]]
