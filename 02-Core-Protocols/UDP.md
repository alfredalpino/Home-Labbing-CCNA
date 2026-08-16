---
tags: [core-protocols, networking, ccna, udp]
aliases: [User Datagram Protocol]
layer: Transport (Layer 4)
---

# UDP

## Learning objectives

- Define UDP as connectionless, unreliable datagram transport
- Know the tiny header and checksum behavior
- Choose UDP vs [[TCP]] for the right jobs
- Troubleshoot silent drops, firewalls, and DNS truncation

## One-sentence definition

> **UDP** (User Datagram Protocol) delivers independent **datagrams** with optional integrity checking, **without** connections, retransmissions, ordering guarantees, or congestion control.

## Analogy

> UDP is a **postcard**: you write it, toss it in the box, hope it arrives. No delivery receipt built in. Great for “what’s the time?” / “what’s this name?” style questions where retrying the whole question is cheaper than a formal courier contract.

## Why it matters

[[DNS]], [[DHCP]], [[NTP]], [[SNTP]], VoIP, gaming, and QUIC (HTTP/3) depend on UDP. Firewalls historically treated UDP poorly (no handshake to latch state). If you only understand TCP, half of infrastructure traffic looks like “mystery UDP.”

## Deep dive

### Mental model

```text
App message → UDP datagram → IP packet → (hope) → UDP → App message
Best effort. Duplicates/reorder/loss possible. Boundaries preserved.
```

### Mechanism

- No handshake: send first packet anytime.
- Demux by destination [[Port]].
- Checksum covers header + data (+ IP pseudo-header); in IPv4 can be zero (disabled) — rare/bad idea; IPv6 requires checksum.
- Reliability, if needed, is **application-built** (DNS retries, RTP+RTCP, QUIC).

### On the wire / header

```text
| Src Port | Dst Port | Length | Checksum | Data... |
```

Only 8 bytes. Beautiful and brutal.

```bash
sudo tcpdump -ni en0 udp port 53
dig example.com
nc -u 127.0.0.1 9999
```

### Where UDP shines

| Use | Why UDP |
|-----|---------|
| DNS queries | Tiny, retry-cheap, latency-sensitive |
| DHCP | Broadcast/discovery before IP config |
| NTP | Small time samples |
| Real-time media | Prefer fresh packet over late retransmission |
| QUIC | Build modern reliability atop UDP to bypass TCP ossification |

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Transport | Unreliable datagrams |
| OSI | 4 | Transport |

## Lab exercises

### Lab 1 — DNS over UDP

```bash
sudo tcpdump -ni en0 udp port 53 &
dig +notcp example.com A
```

### Lab 2 — Truncation → TCP fallback

```bash
dig +ignore +bufsize=512 large-record-domain.example
# Or query ANY/DNSSEC-heavy names; observe TC flag then TCP/53
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| App timeouts, no errors | UDP drop / ACL | captures both ends, firewall UDP policy |
| DNS works intermittently | Loss / rate limit / broken TC fallback | dig +tcp, fragmentation |
| VoIP choppy | Loss/jitter not repaired | QoS, Wi-Fi, not “add TCP” |
| State timeouts | Idle UDP conntrack short | firewall udp idle timers |

## Common traps / interview gotchas

- UDP “connection” in firewalls is synthetic state from seeing traffic.
- Broadcast/multicast often UDP — L2 domain design matters.
- Fragmented UDP DNS can break on middleboxes — why DNS prefers EDNS0 carefully + TCP fallback.
- Higher UDP send rate can melt Wi-Fi without helping goodput.

## Mastery checklist

- [ ] Recite UDP header fields
- [ ] Explain when you’d pick UDP over TCP
- [ ] Capture DNS and identify ports
- [ ] Describe DNS TC bit → TCP/53 behavior

## Related notes

- [[TCP]] · [[ICMP]] · [[Port]] · [[Socket]] · [[DNS]] · [[DHCP]] · [[NTP]] · [[SNTP]]
- ← [[02-Core-Protocols/Index|Core Protocols]]
