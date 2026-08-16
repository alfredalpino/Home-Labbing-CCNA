---
tags: [application-protocols, networking, ccna, dns]
aliases: [Domain Name System, Name Resolution]
layer: Application
---

# DNS

## Learning objectives

- Explain DNS as a distributed database mapping names ↔ data (not only IPs)
- Trace recursive resolution from stub resolver → recursive → authoritative
- Know critical record types and UDP/53 vs TCP/53
- Troubleshoot with `dig` like a professional; compare public resolvers

## One-sentence definition

> **DNS** (Domain Name System) is the hierarchical, distributed naming system that resolves human-friendly names into records — most commonly **A/AAAA** addresses — using recursive and authoritative servers.

## Analogy

> DNS is the **Internet’s contact directory**. Humans remember names; networks dial numbers (IPs). Your phone’s contacts app (stub) asks a librarian (recursive resolver), who walks the library floors (root → TLD → authoritative) unless the answer is already sticky-noted (cache).

## Why it matters

When DNS breaks, *everything* looks broken: browsing, APIs, email (MX), VPN portals, updates. Senior engineers always ask: “Is it DNS?” — and then **prove** it with `dig`.

## Deep dive

### Mental model

```text
App → Stub resolver (OS)
        → Recursive resolver (ISP / 1.1.1.1 / internal)
             → Root → TLD → Authoritative nameservers
                  ← answers cached per TTL
```

| Role | Job |
|------|-----|
| Stub | Asks a recursive; little logic |
| Recursive | Walks the tree; caches |
| Authoritative | Holds the zone truth |

### Critical record types

| Type | Purpose |
|------|---------|
| A | IPv4 address |
| AAAA | IPv6 address |
| CNAME | Alias to another name |
| MX | Mail exchangers ([[SMTP-IMAP]]) |
| NS | Nameservers for a zone |
| SOA | Zone authority metadata |
| TXT | SPF/DKIM/verification strings |
| PTR | Reverse name (in-addr.arpa) |

### UDP vs TCP

- Most queries: [[UDP]]/53
- Truncated answers (TC flag), zone transfers, some large responses: [[TCP]]/53

### On the wire / labs tooling

```bash
dig example.com A +norecurse
dig @1.1.1.1 example.com
dig example.com NS
dig -x 1.1.1.1
scutil --dns   # macOS: see search domains & resolvers
```

Public resolvers deep-dive: [[Cloudflare]] · [[Google DNS]] · [[OpenDNS]] · [[Quad9]]

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Naming service |
| Transport | UDP/TCP 53 | |

## Lab exercises

### Lab 1 — Full story for one name

```bash
dig example.com A +trace
```

### Lab 2 — Compare resolvers

```bash
dig @1.1.1.1 cloudflare.com A
dig @8.8.8.8 cloudflare.com A
dig @9.9.9.9 cloudflare.com A
```

### Lab 3 — Split-horizon thought

Internal name resolves differently inside corp vs public — predict failure when laptop leaves VPN.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Browser fails, ping IP works | DNS | dig, stub config, DHCP option 6 |
| NXDOMAIN | True miss / wrong zone | authoritative answer, typos |
| ServFail | Upstream/DNSSEC/broken NS | dig +nssearch, parent NS |
| Stale answer | Cache TTL | dig +nocmd +noall +answer +ttlid; flush cache |
| Intermittent wrong VIP | GeoDNS / ECS | compare resolvers, see [[Google DNS]] |

## Common traps / interview gotchas

- Flushing browser cache ≠ flushing OS DNS cache.
- CNAME at zone apex is problematic; use A/ALIAS/ANAME patterns carefully.
- DNSSEC failures look like random ServFail.
- “Use 8.8.8.8” can break internal names if it bypasses corp recursive.

## Mastery checklist

- [ ] Draw stub → recursive → authoritative
- [ ] Use dig to show Answer vs Authority vs Additional
- [ ] Explain UDP vs TCP 53
- [ ] Compare two public resolvers with evidence

## Related notes

- [[UDP]] · [[TCP]] · [[DHCP]] · [[IP Address]] · [[HTTP-HTTPS]] · [[SMTP-IMAP]]
- [[Cloudflare]] · [[Google DNS]] · [[OpenDNS]] · [[Quad9]]
- ← [[07-Name-Resolution/Index|Name Resolution]] · [[03-Application-Protocols/Index|Application Protocols]]
