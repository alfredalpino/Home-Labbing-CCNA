---
tags: [network-security, firewalls, networking, ccna, proxy]
aliases: [Proxy Firewall, Application Proxy, Proxy Gateway]
layer: Application (often)
---

# Proxy Firewall

## Learning objectives

- Define proxy firewalls as traffic intermediaries that terminate sessions
- Contrast forward vs reverse proxies
- Compare to packet/stateful filters and [[Web Application Firewall]]
- Understand visibility and breakage tradeoffs

## One-sentence definition

> A **proxy firewall** (application proxy) stands in the middle: clients connect to the proxy, the proxy opens a **separate** connection to the server — inspecting or controlling application exchanges rather than merely forwarding packets blindly.

## Analogy

> A proxy is a **concierge**. You never speak directly to the restaurant kitchen; you tell the concierge what you want; they place the order and bring food back. The kitchen only knows the concierge. That lets the hotel enforce dress codes and keep the kitchen address private — but a confused concierge can break exotic orders (weird apps).

## Why it matters

Explicit proxies, reverse proxies, and secure web gateways still appear in enterprises. They enable inspection, caching, authentication, and hiding internal topology — and cause classic “works without proxy” tickets.

## Deep dive

### Mental model

```text
Client ══ session A ══ Proxy ══ session B ══ Server
          (two sockets; proxy can read/modify within policy)
```

### Forward vs reverse

| Kind | Client thinks… | Common use |
|------|----------------|------------|
| Forward proxy | Proxy is how I reach Internet | User web egress |
| Reverse proxy | Server VIP *is* the app | Publish apps, load balance, WAF front |

### Strengths / weaknesses

| Strengths | Weaknesses |
|-----------|------------|
| Deep app control | App compatibility pain |
| Hide internals / central auth | Extra latency/hops |
| Strong logging | Scaling & HA complexity |

### On the wire

You’ll see client → proxy IP/port, then proxy → origin. With TLS, intercepting proxies need trust; CONNECT method tunnels HTTPS unless decrypted.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Often | Application | HTTP/SOCKS/etc. |
| Related | [[Circuit-Level Gateway]] | Lower-than-full-app cousin |

## Lab exercises

### Lab 1 — Explicit proxy env vars

```bash
export https_proxy=http://127.0.0.1:8080
curl -vI https://example.com/ || true
# Observe failure mode when proxy missing — teaches path dependence
unset https_proxy
```

### Lab 2 — Reverse proxy mental model

Draw browser → reverse proxy → app servers; mark where TLS terminates.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Browser OK, CLI fails | Proxy settings only in GUI | env vars, PAC |
| TLS errors | Intercept CA untrusted | cert chain |
| One app fails | Non-proxy-aware protocol | exception / transparent proxy |

## Common traps / interview gotchas

- Proxy firewall ≠ packet filter with “proxy” in the product name.
- Transparent proxies still break some apps.
- Reverse proxy is often where WAF lives.

## Mastery checklist

- [ ] Concierge analogy
- [ ] Draw two sessions through a proxy
- [ ] Forward vs reverse in one sentence each
- [ ] Name a TLS intercept failure mode

## Related notes

- [[Circuit-Level Gateway]] · [[Web Application Firewall]] · [[HTTP-HTTPS]] · [[SSL-TLS]] · [[Next-Generation Firewall]]
- ← [[01-Firewalls/Index|Firewalls]] · [[04-Network-Security/Index|Network Security]]
