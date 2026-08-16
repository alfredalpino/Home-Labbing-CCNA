---
tags: [nat, networking, ccna, ipv6, nat64]
aliases: [NAT64, IPv6 to IPv4 Translation, DNS64]
layer: Network (Layer 3) — family translation
---

# NAT64

## Learning objectives

- Explain the problem NAT64 solves: IPv6‑only clients reaching IPv4‑only servers
- Relate NAT64 to DNS64 synthesized AAAA records
- Contrast NAT64 with dual stack and with IPv4 [[PAT-NAT-Overload]]
- Know well‑known prefix `64:ff9b::/96` at awareness level

## One-sentence definition

> **NAT64** is a translation mechanism that lets **IPv6** hosts communicate with **IPv4** servers by rewriting packets between families — often paired with **DNS64** so names resolve to a reachable IPv6 representation of an IPv4 address.

## Analogy

> Imagine a new city that only speaks **Metric** ([[IPv4-vs-IPv6|IPv6]]) calling an old warehouse that only understands **Imperial** (IPv4). NAT64 is the **bilingual shipping dock** that restamps crates both ways. DNS64 is the **directory service** that prints the warehouse’s Imperial street number *in Metric digits* so Metric couriers know where to drive.

## Why it matters

Mobile carriers and some lab/cloud designs push IPv6‑mostly or IPv6‑only access. The Internet still has vast IPv4‑only content. Dual stack is ideal; when you can’t, NAT64/DNS64 (and cousins like 464XLAT) keep the web usable. CCNA‑level awareness: *what problem*, *where it sits*, *not a replacement for learning IPv4*.

## Deep dive

### Mental model

```text
IPv6-only client                 NAT64 gateway              IPv4-only server
2001:db8::10  ──IPv6 packets──►  translate  ──IPv4 packets──►  192.0.2.80
              ◄────────────────  translate  ◄────────────────
                     DNS64 may return AAAA embedding 192.0.2.80
                     e.g. under 64:ff9b::/96
```

### Mechanism

1. Client does DNS lookup for `server.example`.
2. If only an **A** record exists, **DNS64** synthesizes a **AAAA** embedding that IPv4 address (commonly using Well‑Known Prefix `64:ff9b::/96`).
3. Client sends IPv6 packets toward that AAAA.
4. **NAT64** device maps IPv6 ↔ IPv4, maintaining state similar in spirit to PAT (ports matter for multiplexing).
5. Replies translate back.

### Compared to other approaches

| Approach | Idea | Tradeoff |
|----------|------|----------|
| Dual stack | Client has v4+v6 | Best fidelity; more to manage |
| NAT64/DNS64 | v6 client → v4 server | Breaks some literals / discovery |
| 464XLAT | CLAT on handset + NAT64 | Helps apps that need private v4 |
| SIIT | Stateless IP/ICMP translation | Different deployment model |

### On the wire / fields

Entire IP header family changes: version 6 ↔ 4, addresses rewritten, ICMPv6 ↔ ICMPv4 carefully mapped. TCP/UDP payloads usually untouched except checksum fixups. Captures on the v6 side never show the real v4 address unless you decode the embedded form.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Cross‑family L3 translation |
| DNS | Application helper | DNS64 feeds destinations to NAT64 |
| Ops | Transition | Bridge islands during IPv6 adoption |

## Lab exercises

### Lab 1 — Detect DNS64 synthesis (if your network uses it)

```bash
dig AAAA ipv4only.arpa +short
# On DNS64 networks may return AAAA under 64:ff9b::/96
dig A example.com +short
dig AAAA example.com +short
```

Compare whether AAAA is “real” dual‑stack or synthesized.

### Lab 2 — Dual stack vs translation thought experiment

For a v6‑only laptop and an IPv4‑only API:

1. Dual stack laptop → direct IPv4 path.
2. v6‑only + NAT64 → translated path.
Predict what breaks if the app hard‑codes `192.0.2.80` without DNS.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Names fail, literals work oddly | DNS64 missing / app uses v4 literal | DNS path; CLAT need |
| Some sites broken on mobile | NAT64 ALG / MTU | PMTUD; vendor known issues |
| Works on Wi‑Fi not LTE | Different transition tech | compare dual stack vs NAT64 |
| Confusion with NAT44 | Wrong mental model | family change vs [[PAT-NAT-Overload]] |

## Common traps / interview gotchas

- NAT64 is **not** “IPv6 NAT overload for RFC1918” — it’s **family** translation.
- Without DNS64 (or provisioning), clients won’t know how to address IPv4‑only targets.
- Hard‑coded IPv4 literals break IPv6‑only + DNS64 designs.
- Still need IPv4 expertise — the other side of the dock is v4.
- Security controls must exist on **both** families / at the translator.

## Mastery checklist

- [ ] State the problem NAT64 solves in one sentence
- [ ] Explain how DNS64 and NAT64 cooperate
- [ ] Contrast dual stack vs NAT64
- [ ] Recognize `64:ff9b::/96` as well‑known prefix
- [ ] Tie back to [[IPv4-vs-IPv6]] and [[NAT-vs-PAT]]

## Related notes

- [[IPv4-vs-IPv6]] · [[NAT-vs-PAT]] · [[PAT-NAT-Overload]] · [[DNS]] · [[IP Address]] · [[Public-vs-Private-Addresses]]
- ← [[01-NAT/Index|NAT]]
