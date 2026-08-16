---
tags: [network-types, networking, ccna, vpn]
aliases: [Virtual Private Network, VPN]
layer: Overlay / security architecture
---

# VPN

## Learning objectives

- Define VPN as a virtual private overlay across a shared network
- Contrast remote-access vs site-to-site VPNs
- Relate VPN to encryption ([[SSL-TLS]] / IPsec) without drowning in crypto
- Troubleshoot “VPN connected but apps fail”

## One-sentence definition

> A **VPN** (Virtual Private Network) creates a **private, usually encrypted path** for your traffic across a shared or untrusted network (often the Internet), so sites or users behave as if on a private WAN.

## Analogy

> The Internet is a **public subway**. A VPN is a **private sealed capsule** you ride inside that subway: other passengers can’t read your papers ([[Packet]] payloads), and you get dropped near your office building’s private hallways (internal [[LAN]] / routes). The subway still rattles (Internet [[Latency]]/loss) — the capsule doesn’t remove physics.

## Why it matters

Remote work, site interconnect without MPLS, and cloud hybrid all lean on VPNs. CCNA security/network fundamentals expect you to know *what problem VPN solves* and where it sits (overlay on underlay).

## Deep dive

### Mental model

```text
Laptop ──(Internet underlay)── VPN gateway ── Corp LAN
          └── encrypted tunnel (overlay)
```

### Types

| Type | Analogy extension | Typical use |
|------|-------------------|-------------|
| Remote access | Employee capsule from home | User ↔ concentrator |
| Site-to-site | Private tunnel between two buildings | Branch ↔ HQ |
| SSL VPN | Often browser/client over TLS | User access |
| IPsec VPN | Packet-level protected tunnels | Site and client |

### What VPN does / doesn’t

- **Does:** confidentiality, integrity, auth (usually); logical membership in remote network
- **Doesn’t:** magically raise underlay bandwidth; fix bad DNS; replace endpoint security

### On the wire

You may see UDP/4500 (NAT-T), ESP, or TCP/443. Inner packets have internal IPs; outer packets use public underlay IPs.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Overlay | Often L3 (IPsec) or session/app (SSL VPN) | Depends on product |
| Underlay | Internet / [[WAN]] | Carries encapsulated traffic |

## Lab exercises

### Lab 1 — Observe underlay vs overlay

Connect any VPN; compare `ifconfig`/`ip addr` before/after (tunnel adapter). Check routes.

### Lab 2 — Split vs full tunnel thought experiment

List apps that should use corp path vs direct Internet; predict DNS implications.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Won’t establish | Creds/certs/firewall | ports, time ([[NTP]]), cert validity |
| Connected, no apps | Routes/DNS/split tunnel | path to VIP, internal DNS |
| Slow only on VPN | MTU / underlay loss | ping size, fragmentation |

## Common traps / interview gotchas

- VPN ≠ anonymity network (that’s a different threat model).
- “I’m on VPN” doesn’t mean all traffic is tunneled (split tunneling).
- Nested VPNs and TCP-over-TCP meltdown hurt performance.

## Mastery checklist

- [ ] Explain underlay vs overlay with subway capsule analogy
- [ ] Contrast site-to-site vs remote access
- [ ] Diagnose connected-but-broken (routes/DNS)
- [ ] Name common ports/protocols at awareness level

## Related notes

- [[WAN]] · [[LAN]] · [[Cloud]] · [[SSL-TLS]] · [[Routers]] · [[IP Address]] · [[DNS]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
