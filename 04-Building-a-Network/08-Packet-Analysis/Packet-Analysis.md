---
tags: [packet-analysis, networking, ccna, wireshark, tcpdump]
aliases: [Packet Analysis, Wireshark, tcpdump Methodology]
layer: Troubleshooting methodology / visibility
---

# Packet Analysis

## Learning objectives

- Follow a disciplined loop: **capture → filter → prove fault**
- Know when to use Wireshark vs `tcpdump` vs device ACLs/SPAN
- Read [[Frame]] / [[Packet]] / segment relationships for [[TCP]], [[UDP]], [[ICMP]]
- Avoid “looking at packets” without a hypothesis

## One-sentence definition

> **Packet analysis** is capturing traffic on a path and inspecting [[Frame]]s/[[Packet]]s to **prove** where a fault lives — not to admire hex — by filtering to the conversation that matters.

## Analogy

> The network is a **highway**. Device logs are **witness interviews** (“I think I saw a red car”). Packet analysis is **CCTV at a chosen overpass**: you place the camera (capture point), zoom to plate/time (display filter), and show the jury the exact crash (retransmits, RSTs, missing SYN-ACKs). Wrong overpass = wrong movie. No filter = watching every car in the city.

## Why it matters

CCNA and real ops live or die by evidence. “DNS is broken” becomes: see query, see no response, see response from wrong server. Same skill debugs [[WLAN]] wired side, [[VPN]] underlay, and HA failover blips.

## Deep dive

### Mental model

```text
Hypothesis → pick capture point → capture → filter conversation
     → interpret (who sent what?) → prove / revise hypothesis
```

### Methodology

1. **Hypothesis**: “SYN leaves PC, no SYN-ACK from server.”
2. **Capture point**: client SPAN, server NIC, mid-path tap — *both ends* if possible.
3. **Capture**: Wireshark GUI or `tcpdump -w file.pcap`.
4. **Filter**: `ip.addr==x && tcp.port==443` (Wireshark) / `host x and port 443` (bpf).
5. **Prove**: missing packets, checksum issues, TCP retrans, ICMP unreachable, TLS alerts.

### Tool roles

| Tool | Strength |
|------|----------|
| Wireshark | Decode, Follow Stream, graphs |
| tcpdump | Remote/CLI, ring buffers, scripts |
| SPAN/ERSPAN | Get packets off switches |
| Device `debug`/`pcap` | On-box when allowed |

### On the wire / fields

- L2 [[Frame]]: MACs, EtherType, VLAN tag
- L3 [[Packet]]: IPs, TTL, proto
- L4: [[TCP]] seq/ack/flags; [[UDP]] ports/len; [[ICMP]] type/code
- App: DNS/HTTP only after you prove transport is healthy

### Wireshark filter cheats (awareness)

| Intent | Example |
|--------|---------|
| Host pair | `ip.addr == 10.1.1.10` |
| TCP trouble | `tcp.analysis.retransmission` |
| ICMP | `icmp` |
| DNS | `dns` |

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | All (visibility) | See each layer’s headers |
| OSI | 1–7 as decoded | Camera doesn’t replace layer thinking |

## Lab exercises

### Lab 1 — Capture a ping

```bash
# Terminal 1
sudo tcpdump -ni any -w /tmp/ping.pcap icmp
# Terminal 2
ping -c 4 1.1.1.1
# Stop capture; open in Wireshark — find echo request/reply
```

### Lab 2 — Prove a TCP handshake

Browse an HTTP site (or `curl`); filter `tcp.flags.syn==1`. Confirm SYN → SYN/ACK → ACK. Then Follow TCP Stream.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Capture empty | Wrong interface/SPAN | direction, VLAN, promiscuous |
| One-way traffic | Asymmetric path | capture both ends |
| “TCP window full” | Receiver slow | app/host, not WAN myth |
| Good PCAP, still confused | No hypothesis | write expected packets first |

## Common traps / interview gotchas

- Capturing on Wi‑Fi *client* shows 802.11 differently than wired SPAN after an AP.
- Encrypted payloads ([[VPN]], TLS) still show outer headers — useful!
- tcpdump without `-s 0` / snaplen may truncate.
- Packet analysis without timestamps/NTP sync confuses correlated events.

## Mastery checklist

- [ ] State capture → filter → prove
- [ ] Pick a capture point for a given fault story
- [ ] Read [[TCP]] handshake and [[ICMP]] echo in a PCAP
- [ ] Write one Wireshark and one bpf filter from memory

## Related notes

- [[Frame]] · [[Packet]] · [[TCP]] · [[UDP]] · [[ICMP]] · [[VPN]] · [[WLAN]] · [[Latency]]
- ← [[08-Packet-Analysis/Index|Packet Analysis]] · [[04-Building-a-Network/Index|Building a Network]]
