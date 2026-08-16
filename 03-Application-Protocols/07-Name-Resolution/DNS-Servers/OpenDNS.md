---
tags: [dns-servers, networking, dns, resolvers, opendns]
aliases: [OpenDNS, Cisco Umbrella DNS, 208.67.222.222]
provider: OpenDNS / Cisco
---

# OpenDNS

## Learning objectives

- Configure OpenDNS resolver IPs and verify with dig
- Understand its historical role in filtering / dashboards
- Relate OpenDNS to Cisco Umbrella at a high level
- Decide when filtering resolvers help vs hurt troubleshooting

## One-sentence definition

> **OpenDNS** is a public recursive DNS service (now part of Cisco’s security portfolio) known for optional **content filtering**, phishing protection, and management dashboards — commonly reached at `208.67.222.222`.

## Why engineers care

Home labs and small orgs use it for category blocking without a full firewall UTM. Enterprises often graduate to **Cisco Umbrella** (related lineage) for policy-based DNS security. Filtering resolvers can also **mask** real NXDOMAIN vs blocked answers — know the difference when debugging.

## Resolver addresses

| Role | IPv4 | IPv6 |
|------|------|------|
| Primary | `208.67.222.222` | `2620:119:35::35` |
| Secondary | `208.67.220.220` | `2620:119:53::53` |

(Confirm current IPv6 in vendor docs if deploying critically — OpenDNS/Umbrella SKUs vary.)

## Features

| Topic | Notes |
|-------|-------|
| Filtering | Category blocks, custom allow/deny (account features) |
| Phishing/malware | Reputation-informed responses |
| Management | Web dashboard historically a major draw |
| Umbrella | Broader enterprise DNS security platform |

## How it works in your path

Stub → OpenDNS recursive (policy applied) → upstream resolution / block page logic. Blocked names may return sinkhole IPs or NXDOMAIN-like behavior depending on product settings — always verify with dig and documentation for your SKU.

## Lab: test and compare

```bash
dig @208.67.222.222 example.com A +stats
dig @208.67.220.220 example.com A +stats

# Compare unfiltered public resolvers
dig @1.1.1.1 example.com A
dig @9.9.9.9 example.com A
```

```bash
networksetup -setdnsservers Wi-Fi 208.67.222.222 208.67.220.220
```

## When to choose this resolver

- Need DNS-layer category filtering with simple client config
- Aligning with Cisco security tooling / Umbrella direction
- Home network with kids/guest filtering requirements

For pure troubleshooting of “is the name real on the Internet?”, also test an unfiltered resolver ([[Cloudflare]], [[Google DNS]]) in parallel.

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Site “down” only on OpenDNS | Category block / policy — dig and check block page |
| Dashboard stats empty | Wrong network registration / IP not affiliated |
| Bypass | Clients hardcode 8.8.8.8 — enforce at firewall |

## Common traps

- Filtering can look like application failure.
- Users bypass by setting other DNS — control egress UDP/TCP 53 or use DoH policies.
- Free vs paid features differ — don’t assume enterprise controls on free tiers.

## Mastery checklist

- [ ] Recite 208.67.222.222 / 208.67.220.220
- [ ] dig against OpenDNS successfully
- [ ] Explain filtering vs outage
- [ ] Relate OpenDNS ↔ Umbrella at cocktail-party depth

## Related notes

- [[DNS]] · [[Cloudflare]] · [[Google DNS]] · [[Quad9]] · [[DNS-Servers/Index|DNS Servers]]
- ← [[DNS-Servers/Index|DNS Servers]] · [[07-Name-Resolution/Index|Name Resolution]]
