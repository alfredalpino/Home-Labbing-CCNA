---
tags: [application-protocols, networking, ccna, ntp]
aliases: [Network Time Protocol]
layer: Application
---

# NTP

## Learning objectives

- Explain why accurate time is a network service dependency
- Understand strata, modes, and UDP/123
- Configure/verify NTP at a conceptual + CLI lab level
- Relate time failure to TLS, logs, Kerberos, and correlating incidents

## One-sentence definition

> **NTP** (Network Time Protocol) synchronizes clocks between systems over the network, typically using **UDP port 123**, so timestamps and time-sensitive security protocols remain coherent.

## Analogy

> NTP is the **town clock radio signal**. Every shop sets its wall clock from trusted stratum towers so “meet at 3pm,” certificates (“valid from/to”), and log timelines agree. If your clock is years off, the security guard (TLS) thinks your badge is expired.

## Why it matters

Bad time → [[SSL-TLS]] certs look expired, log correlation fails, Kerberos tickets break, scheduled jobs fire wrong, certificate OCSP weirdness. Time is infrastructure.

## Deep dive

### Mental model

```text
Reference clocks (stratum 0 hardware)
  → stratum 1 NTP servers
  → stratum 2... enterprise servers
  → clients (workstations, routers, VMs)
```

Lower stratum number = closer to reference (stratum 1 is best commonly reachable).

### Mechanism

- Client polls servers, measures offset/delay/jitter
- Steers clock gradually (slew) or steps when far off
- Modes: client/server, symmetric peers, broadcast/multicast (less common in modern hardened nets)
- Authentication possible (symmetric keys / Autokey legacy / NTS modern)

### On the wire

UDP/123. Often bidirectional from client ephemeral → 123.

```bash
# macOS
sntp -sS time.apple.com
date
# Linux often: chronyc tracking / timedatectl / ntpq -p
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Time sync service |
| Transport | UDP/123 | |

## Lab exercises

### Lab 1 — Query a public time source

```bash
sntp time.cloudflare.com
# or: ntpdate -q pool.ntp.org   (if available)
```

### Lab 2 — Dependency story

Set a lab VM clock wrong by years; attempt HTTPS; observe certificate date errors. Fix via NTP.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Large offset | NTP blocked / wrong server | UDP/123 ACL, reachability |
| Flapping offset | VM pause / bad hypervisor time | VMtools, chrony config |
| Auth failures | Kerberos/TLS | system time first |

## Common traps / interview gotchas

- [[SNTP]] is simplified client algorithm — fine for many devices, weaker statistics than full NTP.
- Using random public NTP without policy may be OK for labs; enterprises use internal hierarchy + authenticated sources.
- Firewalls must allow responses; stateful UDP helps.

## Mastery checklist

- [ ] Explain strata
- [ ] Name UDP/123
- [ ] Connect clock skew to TLS failures
- [ ] Contrast NTP vs SNTP

## Related notes

- [[SNTP]] · [[UDP]] · [[SSL-TLS]] · [[DNS]] · [[DHCP]] (option 42 sometimes)
- ← [[03-Time/Index|Time]] · [[03-Application-Protocols/Index|Application Protocols]]
