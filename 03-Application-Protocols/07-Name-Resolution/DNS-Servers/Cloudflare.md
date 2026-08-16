---
tags: [dns-servers, networking, dns, resolvers, cloudflare]
aliases: [Cloudflare, 1.1.1.1, Cloudflare DNS]
provider: Cloudflare
---

# Cloudflare DNS

## Learning objectives

- Configure and test Cloudflare’s public recursive resolver
- Know primary IPv4/IPv6 addresses and security variants
- Evaluate privacy claims with an engineer’s skepticism
- Compare latency/behavior against other public resolvers

## One-sentence definition

> **Cloudflare DNS** (`1.1.1.1`) is Cloudflare’s public **recursive DNS resolver**, marketed for speed and privacy, used by stub resolvers on clients and routers worldwide.

## Why engineers care

It’s a clean lab default, often low-latency via anycast, and a common “change your DNS” fix when ISP resolvers misbehave. You still must understand it does **not** replace enterprise split-horizon DNS.

## Resolver addresses

| Role | IPv4 | IPv6 |
|------|------|------|
| Primary | `1.1.1.1` | `2606:4700:4700::1111` |
| Secondary | `1.0.0.1` | `2606:4700:4700::1001` |

**Variants (high level):**

- `1.1.1.2` / `1.0.0.2` — malware blocking flavor
- `1.1.1.3` / `1.0.0.3` — malware + adult content blocking flavor

Also offers DNS over HTTPS / TLS endpoints for encrypted client→resolver transport (DoH/DoT).

## Features

| Topic | Notes |
|-------|-------|
| Privacy | Strong marketing; still a recursive that **sees query names** from your IP (or DoH endpoint). Read current privacy policy for retention claims. |
| Filtering | Optional blocked variants above |
| Performance | Anycast; often excellent RTT |
| Security | Resolver hardening; filtering SKUs separate |

## How it works in your path

```text
Your OS stub → 1.1.1.1 (recursive) → root/TLD/auth → answer (+ cache)
```

Same model as other public resolvers. See [[DNS]].

## Lab: test and compare

```bash
dig @1.1.1.1 example.com A +stats
dig @1.0.0.1 example.com A +stats
dig @1.1.1.1 cloudflare.com AAAA

# macOS: view current resolvers
scutil --dns | head -40
```

**Set on macOS (System Settings → Network → DNS)** or temporarily:

```bash
networksetup -setdnsservers Wi-Fi 1.1.1.1 1.0.0.1
# restore DHCP DNS later:
networksetup -setdnsservers Wi-Fi Empty
```

## When to choose this resolver

- Lab / home when ISP DNS is flaky or hijacks NXDOMAIN
- You want a simple anycast recursive with optional block lists
- Prefer not to send queries to Google for policy reasons

Avoid as the **only** resolver for corporate laptops that need internal zones — use internal recursive or split DNS / VPN DNS.

## Troubleshooting

| Symptom | Check |
|---------|-------|
| No resolution | Path to 1.1.1.1 (some networks block), try DoH |
| Internal names fail | Expected — public recursive has no corp zones |
| Inconsistent answers | Cache TTLs / geo; compare `@8.8.8.8` |

## Common traps

- `1.1.1.1` is also used in unrelated products historically — confirm you’re talking about DNS.
- Encrypting DNS to Cloudflare doesn’t hide destinations from your ISP (they still see IPs); it hides *query names* from on-path observers between you and Cloudflare.
- Some captive portals break until you use ISP DNS briefly.

## Mastery checklist

- [ ] Recite 1.1.1.1 / 1.0.0.1 and IPv6 pair
- [ ] `dig @1.1.1.1` successfully and read Query time
- [ ] Explain when not to use public DNS on corp endpoints
- [ ] Name malware/family variants

## Related notes

- [[DNS]] · [[Google DNS]] · [[OpenDNS]] · [[Quad9]] · [[DNS-Servers/Index|DNS Servers]] · [[UDP]]
- ← [[DNS-Servers/Index|DNS Servers]] · [[07-Name-Resolution/Index|Name Resolution]]
