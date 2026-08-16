---
tags: [core-protocols, networking, ccna, icmp]
aliases: [Internet Control Message Protocol, Ping Protocol]
layer: Network (companion to IP)
---

# ICMP

## Learning objectives

- Position ICMP as IP’s control/error companion (not a transport for apps)
- Memorize the types/codes that matter in production
- Explain ping and traceroute mechanics precisely
- Avoid the “block all ICMP” footgun (PMTUD)

## One-sentence definition

> **ICMP** carries diagnostics and error messages for IP — destination unreachable, time exceeded, echo request/reply, and more — enabling tools like **ping** and **traceroute** and critical behaviors like **Path MTU Discovery**.

## Analogy

> ICMP is the **network’s sticky notes and error tickets**: “host unreachable,” “TTL expired,” “please fragment.” Ping is politely asking “are you there?” with an echo sticky note — useful, but not the same as testing the actual application door.

## Why it matters

Without ICMP, you lose visibility and sometimes *data-plane correctness* (MTU black holes). Blindly filtering all ICMP “for security” breaks networks in subtle ways.

## Deep dive

### Mental model

```text
IP delivery problem or probe
  → ICMP message back toward source (often)
  → Source stack/app adjusts or reports error
```

ICMP rides inside IP (proto 1 for IPv4). It is **not** TCP/UDP and has **no ports**.

### Types / codes that matter (IPv4)

| Type | Name | Ops relevance |
|------|------|----------------|
| 0 / 8 | Echo Reply / Request | ping |
| 3 | Destination Unreachable | admin prohibited, port unreachable, **frag needed (code 4)** |
| 5 | Redirect | usually ignored/suspicious on modern hosts |
| 11 | Time Exceeded | TTL expired → traceroute hops |

Embedded in many Type 3/11 messages: quote of the offending packet header — gold for debugging.

### Ping

Sender transmits Echo Request; target replies Echo Reply. Measures RTT + loss for *ICMP*, which may be rate-limited differently from TCP.

### Traceroute

```text
Send probes with TTL=1,2,3,...
Hop that decrements to 0 sends Time Exceeded
Destination eventually responds (UDP port unreachable / TCP RST / ICMP echo) depending on method
```

macOS `traceroute` traditionally UDP; `traceroute -I` uses ICMP; `traceroute -T` TCP.

### ICMPv6

Neighbor Discovery (replace [[ARP]]), Router Advertisements, Echo still exist. Don’t disable ICMPv6 wholesale on IPv6 networks.

### On the wire

```bash
ping -c 4 1.1.1.1
traceroute 1.1.1.1
sudo tcpdump -ni en0 icmp
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Control messages for IP |
| OSI | 3 | Network-layer signaling |

## Lab exercises

### Lab 1 — Ping + capture

```bash
sudo tcpdump -ni en0 icmp &
ping -c 3 8.8.8.8
```

### Lab 2 — Traceroute interpretation

```bash
traceroute -n 1.1.1.1
# Note: * * * means this hop didn’t reply — not always packet loss to dest
```

### Lab 3 — Frag needed awareness

Document why blocking ICMP type 3 code 4 breaks PMTUD for [[TCP]] large transfers.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Ping fails, TCP works | ICMP filtered | don’t conclude host down |
| Large transfers hang | PMTUD black hole | MSS clamp, allow frag-needed, test sizes |
| Traceroute incomplete | Rate limit / ACL on ICMP time exceeded | try TCP traceroute |
| Destination unreachable code 13 | ACL administratively prohibited | firewall policy |

## Common traps / interview gotchas

- ICMP is not “below IP”; it’s carried *in* IP.
- Security: rate-limit / selectively filter — don’t blanket drop all ICMP on routers.
- Ping success ≠ application success (different path/policy possible but uncommon; still different proto).
- Asymmetric routing: ICMP errors may take odd paths.

## Mastery checklist

- [ ] List ICMP types 0/8/3/11 use cases
- [ ] Explain traceroute TTL trick
- [ ] Describe PMTUD dependency on ICMP
- [ ] Contrast ICMPv6 ND vs ARP

## Related notes

- [[TCP]] · [[UDP]] · [[IP Address]] · [[Packet]] · [[ARP]] · [[Latency]] · [[Bandwidth]]
- ← [[02-Core-Protocols/Index|Core Protocols]]
