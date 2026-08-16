---
tags: [application-protocols, networking, ccna, sntp]
aliases: [Simple Network Time Protocol]
layer: Application
---

# SNTP

## Learning objectives

- Define SNTP as a simplified subset of [[NTP]] client behavior
- Know when embedded devices use SNTP
- Understand accuracy/robustness tradeoffs
- Test time sync on systems that expose SNTP tooling

## One-sentence definition

> **SNTP** (Simple Network Time Protocol) is a lightweight version of NTP client logic that synchronizes time with reduced complexity and generally lower robustness than a full NTP implementation — still commonly on **UDP/123**.

## Analogy

> SNTP is a **cheap wristwatch that syncs to the radio once in a while** — same station as NTP, simpler guts. Fine for a camera or IoT gadget; not the precision chronometer you want as the city’s master clock.

## Why it matters

Cameras, controllers, cheap IoT, and some OS utilities speak SNTP. You’ll see it in vendor docs. Don’t assume “NTP configured” means full chrony/ntpd features.

## Deep dive

### Mental model

```text
Full NTP: filter many samples, peer selection, complex state
SNTP:    simpler query/adjust — “good enough” clock for many devices
```

### Mechanism

- Same on-wire NTP packet format family in many cases
- Client sends request, applies offset from reply with simpler algorithms
- May lack sophisticated falseticker detection / complex polling adaptation

### Accuracy tradeoffs

| | NTP (full) | SNTP |
|-|------------|------|
| Typical use | Servers, infra | IoT, appliances, simple clients |
| Robustness | Higher | Lower |
| Port | 123/UDP | 123/UDP |

### On the wire

Indistinguishable from NTP at a glance in many captures — context is the implementation.

```bash
sntp -sS pool.ntp.org
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Simplified time client |
| Transport | UDP/123 | |

## Lab exercises

### Lab 1 — Use sntp client on macOS

```bash
sntp pool.ntp.org
date
```

### Lab 2 — Compare docs

On a home router/AP UI, find “SNTP server” field — point it at an internal or public server and verify device logs timestamps.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Device time wrong | SNTP server unreachable | UDP/123, DNS name of server |
| Jittery time | Unstable path / poor client | try closer server, wired path |

## Common traps / interview gotchas

- SNTP ≠ “insecure NTP”; security depends on deployment (auth rare on SNTP devices).
- Same port as NTP — ACL language often says “allow NTP” covering both.
- Not a substitute for enterprise authenticated time distribution.

## Mastery checklist

- [ ] Define SNTP vs NTP in one sentence
- [ ] Know shared port 123/UDP
- [ ] Give two device classes that use SNTP
- [ ] Fix a device with wrong time via SNTP settings

## Related notes

- [[NTP]] · [[UDP]] · [[SSL-TLS]] · [[DHCP]]
- ← [[03-Time/Index|Time]] · [[03-Application-Protocols/Index|Application Protocols]]
