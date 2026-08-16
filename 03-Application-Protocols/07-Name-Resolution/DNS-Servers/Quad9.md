---
tags: [dns-servers, networking, dns, resolvers, quad9]
aliases: [Quad9, 9.9.9.9]
provider: Quad9
---

# Quad9

## Learning objectives

- Use Quad9 addresses and understand its security-first mission
- Contrast threat-blocking resolvers vs plain recursive resolvers
- Test with dig and interpret blocked vs nonexistent domains
- Choose Quad9 appropriately for lab/home/enterprise edge cases

## One-sentence definition

> **Quad9** (`9.9.9.9`) is a public recursive DNS resolver operated with a **security focus**, blocking access to known malicious domains using threat-intelligence feeds, while offering alternate non-filtering configurations.

## Why engineers care

It’s a strong default when you want recursive DNS plus a free layer of domain blocking without running your own RPZ. Like all filtering DNS, it changes failure modes — blocked ≠ NXDOMAIN necessarily — so validate during incidents.

## Resolver addresses

| Role | IPv4 | IPv6 |
|------|------|------|
| Primary (secured) | `9.9.9.9` | `2620:fe::fe` |
| Secondary | `149.112.112.112` | `2620:fe::9` |

**Alternate services (high level — verify current docs when deploying):**

- Non-filtering / different privacy feature sets exist (e.g. variants around `9.9.9.10` and other service IPs)
- DoT/DoH endpoints available for encrypted transport to the resolver

## Features

| Topic | Notes |
|-------|-------|
| Malware blocking | Core value proposition via threat intel |
| Privacy | Nonprofit/public-benefit oriented messaging; still sees queries |
| ECS | Service variants differ — check which SKU you use |
| DNSSEC | Validation commonly enabled on secure configs |

## How it works in your path

```text
Stub → Quad9 recursive
         ├─ if malicious reputation → block response
         └─ else resolve normally via hierarchy
```

See [[DNS]] for recursive vs authoritative roles.

## Lab: test and compare

```bash
dig @9.9.9.9 example.com A +stats
dig @149.112.112.112 example.com A +stats
dig @9.9.9.9 +dnssec example.com

# Compare with unfiltered
dig @1.1.1.1 example.com A
```

```bash
networksetup -setdnsservers Wi-Fi 9.9.9.9 149.112.112.112
```

## When to choose this resolver

- Want recursive DNS with default-deny for known-bad domains
- Prefer non-Big-Tech operator for policy reasons
- Home lab hardening without full security stack

Still not a substitute for: patching, email auth, HTTP controls, or internal DNS design.

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Domain works on 1.1.1.1 not 9.9.9.9 | Likely block list — investigate reputation false positive |
| Total DNS failure | UDP/53 path, try alternate IP, check DoH |
| Corp names fail | Public resolver limitation — expected |

## Common traps

- Threat lists lag and false-positive; have an escalation path.
- Encrypted DNS to Quad9 doesn’t hide destination IPs from network operators.
- Mixing filtering resolvers inconsistently across devices confuses users (“works on my phone”).

## Mastery checklist

- [ ] Recite 9.9.9.9 / 149.112.112.112 and IPv6
- [ ] dig @9.9.9.9 with +stats
- [ ] Explain security resolver vs plain recursive
- [ ] Know how to confirm a false-positive block

## Related notes

- [[DNS]] · [[Cloudflare]] · [[Google DNS]] · [[OpenDNS]] · [[DNS-Servers/Index|DNS Servers]]
- ← [[DNS-Servers/Index|DNS Servers]] · [[07-Name-Resolution/Index|Name Resolution]]
