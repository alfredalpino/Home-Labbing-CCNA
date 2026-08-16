---
tags: [basic-terminology, networking, ccna, bandwidth]
aliases: [Link Capacity, Capacity]
layer: Physical / Link capacity concept
---

# Bandwidth

## Learning objectives

- Define bandwidth as **capacity**, not “speed you feel”
- Use correct units (b/s vs B/s) and SI/binary prefixes carefully
- Relate bandwidth to serialization delay and bandwidth-delay product
- Separate marketing “speed” from engineering capacity

## One-sentence definition

> **Bandwidth** is the maximum rate at which bits can be transferred over a link or channel, usually expressed in bits per second (kb/s, Mb/s, Gb/s).

## Analogy

> Bandwidth is the **width of the pipe**, not how fast water feels at the faucet. A firehose (1 Gb/s) can still trickle for you if it’s shared, kinked (loss), or the valve opens slowly (protocol/window).

## Why it matters

You size circuits, interfaces, QoS policies, and backups around bandwidth. Confusing bandwidth with [[Throughput]] or [[Latency]] causes wrong upgrades (“we bought 1 Gb/s and Zoom still stutters” — often latency/loss/Wi-Fi, not raw capacity).

## Deep dive

### Mental model

Bandwidth is the **width of the pipe**.  
Throughput is how much water you actually push.  
Latency is how long until the first drop arrives.

```text
|← —— bandwidth (bits per second capacity) —— →|
```

### Mechanism

- On digital links, interface speed (100M/1G/10G) caps how fast bits are serialized onto the wire.
- **Serialization delay** ≈ packet_bits / link_bandwidth.
  - 1500-byte packet on 1 Gb/s ≈ 12 µs
  - Same packet on 1 Mb/s ≈ 12 ms
- Shared media / Wi-Fi: nominal bandwidth ≠ per-user capacity (contention, overhead, half-duplex airtime).
- Protocols eat overhead (headers, ACKs, retransmits) so app goodput < link bandwidth.

### Bandwidth-delay product (BDP)

```text
BDP (bits) ≈ bandwidth × RTT
```

TCP needs enough window to “fill the pipe.” High bandwidth + high latency (long fat networks) needs large windows / window scaling — otherwise [[Throughput]] caps below bandwidth.

### Units traps

| People say | Often mean |
|------------|------------|
| 100 Mbps | 100 × 10^6 bits/s |
| 100 MBps | 100 × 10^6 **bytes**/s (≈ 800 Mb/s) |
| 1 GiB download on 100 Mb/s | ≈ 80+ seconds ideal (plus overhead) |

ISPs advertise bandwidth; applications experience throughput.

### On the wire / fields

Bandwidth isn’t a packet field. You infer capacity from interface config/negotiation:

```bash
ifconfig en0 | grep media   # macOS media/speed hints
# Linux: ethtool eth0
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | Physical/link bit rate |
| OSI | 1 (also constrained by L2 design) | Signaling rate / channel capacity |

## Lab exercises

### Lab 1 — Compute serialization delay

For 12,000-bit frame on 10 Mb/s and 1 Gb/s, calculate serialization time. Compare to typical LAN RTT.

### Lab 2 — Measure vs rated

```bash
# Rough feel (use a known speed test server or iperf3 if available)
ping -c 10 1.1.1.1
# Note: ping measures latency/loss, NOT bandwidth.
# Install/use iperf3 between two lab hosts to measure throughput ≈ usable bandwidth.
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Slow transfers, low latency | Congestion / small TCP window / disk | interface counters, QoS, TCP window, iperf |
| Speed test << interface rate | Wi-Fi / ISP / CPU / single-flow limits | medium, duplex, offload, parallel flows |
| Duplex mismatch | Hard-coded vs autoneg fail | interface errors (CRC/runts), negotiate settings |

## Common traps / interview gotchas

- Bandwidth ↑ does not guarantee latency ↓.
- Asymmetric uplink/downlink (DOCSIS/PON) — uploads starve.
- Aggregate switch backplane vs per-port bandwidth.
- “Unlimited bandwidth” marketing ≠ infinite capacity at busy hour.

## Mastery checklist

- [ ] Define bandwidth in bits/s with an example
- [ ] Calculate serialization delay for a 1500 B packet at 100 Mb/s
- [ ] Explain BDP and why WAN TCP may underperform
- [ ] Contrast bandwidth vs throughput vs latency in one paragraph

## Related notes

- [[Throughput]] · [[Latency]] · [[Packet]] · [[Frame]] · [[TCP]] · [[Transmission Media Types]]
- ← [[03-Performance/Index|Performance]] · [[01-Basic-Terminology/Index|Basic Terminology]]
