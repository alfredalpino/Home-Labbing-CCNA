---
tags: [core-protocols, networking, ccna, tcp]
aliases: [Transmission Control Protocol, TCP/IP Transport]
layer: Transport (Layer 4)
---

# TCP

## Learning objectives

- Explain TCP as a reliable, ordered, byte-stream transport over IP
- Master handshake, teardown, flags, seq/ack, and windowing
- Separate flow control from congestion control
- Diagnose real failures: resets, stalls, TIME_WAIT, MTU black holes

## One-sentence definition

> **TCP** (Transmission Control Protocol) provides **connection-oriented**, **reliable**, **ordered** delivery of a **byte stream** between applications, using ports, sequence numbers, acknowledgments, retransmissions, and congestion control over best-effort IP.

## Analogy

> TCP is a **certified tracked courier** with receipts: numbered pages, acknowledgments, resends if a page is missing, and “slow down, dock is full” flow control. Reliable, ordered delivery — with more paperwork than a postcard ([[UDP]]).

## Why it matters

HTTP(S), SSH, SMTP, FTP control, and most business apps ride TCP. When “the app hangs,” you’re often looking at TCP: packet loss, window exhaustion, middlebox RSTs, or TLS failing after TCP already connected.

## Deep dive

### Mental model

```text
App writes bytes → TCP segments → IP packets → ... → TCP reassembles bytes → App reads
Guarantees: ordered byte stream (or error/abort). Not message boundaries.
```

UDP preserves message boundaries; TCP does **not** — your app protocol must frame messages.

### Mechanism — connection lifecycle

**Three-way handshake**

```text
Client                Server
  SYN seq=c ─────────►
  ◄──────── SYN-ACK seq=s ack=c+1
  ACK ack=s+1 ────────►
     (ESTABLISHED)
```

**Data transfer:** each segment consumes sequence space (bytes). ACK number = next expected byte.

**Teardown:** FIN/ACK exchange (graceful) or RST (abort).

### Header fields / flags (must know)

| Item | Role |
|------|------|
| Src/Dst Port | App demux ([[Port]], [[Socket]]) |
| Seq / Ack | Reliability + ordering |
| Window | Receiver flow control advertise |
| Data Offset | Header length |
| Flags | SYN, ACK, FIN, RST, PSH, URG, ECE, CWR |
| Checksum | Integrity |
| Urgent pointer | Rarely used modernly |
| Options | MSS, Window Scale, SACK, Timestamps |

**MSS vs MTU:** MSS ≈ MTU − IP header − TCP header (e.g. 1460 on typical Ethernet IPv4).

### Flow control vs congestion control

| | Flow control | Congestion control |
|-|--------------|-------------------|
| Protects | Receiver buffer | Network |
| Signal | Window field | Loss/ECN/delay algorithms |
| Failure mode | Window = 0 stall | Collapse / unfairness |

Algorithms (conceptual mastery): slow start, congestion avoidance, fast retransmit/recovery; modern stacks use CUBIC/BBR variants — know *ideas*, not every RFC.

### States worth memorizing

`LISTEN`, `SYN_SENT`, `SYN_RCVD`, `ESTABLISHED`, `FIN_WAIT_1/2`, `CLOSE_WAIT`, `CLOSING`, `LAST_ACK`, `TIME_WAIT`, `CLOSED`.

**TIME_WAIT:** normal after active close; absorbs delayed duplicates. Don’t panic at modest counts.

### On the wire

```bash
sudo tcpdump -ni en0 'tcp port 443'
sudo tcpdump -ni en0 'tcp[tcpflags] & (tcp-syn|tcp-fin|tcp-rst) != 0'
ss -tan
```

Wireshark: follow TCP stream; Expert Infos for retransmissions.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Transport | Reliable byte stream |
| OSI | 4 | Transport |

## Lab exercises

### Lab 1 — Capture handshake

```bash
sudo tcpdump -ni en0 -w /tmp/tcp.pcap host example.com and tcp port 443
curl -s https://example.com -o /dev/null
# Open pcap in Wireshark: filter tcp.flags.syn==1
```

### Lab 2 — Socket states

```bash
ss -tan | head
netstat -an | grep ESTABLISHED | head
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| SYN no SYN-ACK | Filter / no listener / asymmetric path | ACL, listener, capture both ends |
| Handshake OK, then stall | Window 0 / app / loss | seq graph, retransmits |
| Sudden RST | App abort / WAF / idle timeout | who sent RST, middleboxes |
| Large payloads fail | MTU / PMTUD black hole | ping size + DF, ICMP frag-needed |
| Slow ramp WAN | Loss / small window / buffering | RTT, loss, window scale |

## Common traps / interview gotchas

- TCP is reliable **if the connection stays up** — it cannot invent connectivity.
- ACKs are cumulative (SACK adds selective info).
- Middleboxes that “help” TCP often hurt (bufferbloat, broken SEQ rewrite).
- HTTP/2 and SSH multiplex many logical streams over one TCP connection — head-of-line blocking at TCP layer.

## Mastery checklist

- [ ] Draw 3-way handshake with seq/ack
- [ ] Explain MSS/MTU and a black hole
- [ ] Differentiate flow vs congestion control
- [ ] Read retransmissions in Wireshark confidently

## Related notes

- [[UDP]] · [[ICMP]] · [[Port]] · [[Socket]] · [[Packet]] · [[Latency]] · [[Throughput]]
- [[HTTP-HTTPS]] · [[SSH]] · [[SSL-TLS]]
- ← [[02-Core-Protocols/Index|Core Protocols]]
