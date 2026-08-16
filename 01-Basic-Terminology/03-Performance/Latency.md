---
tags: [basic-terminology, networking, ccna, latency]
aliases: [Delay, RTT, Round Trip Time]
layer: Cross-layer performance metric
---

# Latency

## Learning objectives

- Break latency into propagation, serialization, queuing, processing
- Distinguish one-way delay vs RTT
- Explain why latency destroys interactive apps and TCP ramp-up
- Measure latency correctly and interpret ping limitations

## One-sentence definition

> **Latency** is the time it takes for data to travel from source to destination (one-way) or there and back (**RTT**), usually measured in milliseconds.

## Analogy

> Latency is **how long until the first drop arrives**, not how wide the pipe is. A garden hose to your neighbor (LAN) vs a hose to another continent (WAN): same hose width possible, totally different wait for the first splash.

## Why it matters

Voice/video, gaming, SSH typing feel, stock trading, and chatty APIs are latency-bound. A 1 Gb/s link with 200 ms RTT can feel worse than a 10 Mb/s link with 10 ms RTT for interactive work. CDN and anycast exist largely to buy lower latency.

## Deep dive

### Mental model — delay budget

```text
Total one-way ≈ Propagation + Serialization + Queuing + Processing (+ retransmission effects)
```

| Component | Driven by | Notes |
|-----------|-----------|-------|
| Propagation | Distance × speed of signal | Fiber ≈ 5 µs/km order-of-magnitude; geography dominates WAN |
| Serialization | Packet size / [[Bandwidth]] | Big on slow links |
| Queuing | Congestion | Explodes under load; bufferbloat |
| Processing | Devices/firewalls/DPI | Can be significant on security appliances |

### RTT vs one-way

- `ping` reports **RTT** (ICMP echo).
- Asymmetric paths → one-way delays differ; RTT still sums both.
- TCP RTT estimation drives retransmission timeout (RTO).

### Latency vs bandwidth

Independent knobs. Satellite: high bandwidth possible, **huge** latency. Metro dark fiber: low latency, bandwidth whatever you light.

### On the wire

Latency isn’t a header field, but timestamps and TCP TS options help estimators. Traceroute shows per-hop RTT to the responding interface (caveats galore).

```bash
ping -c 10 1.1.1.1
traceroute 1.1.1.1
# macOS: traceroute; Linux often traceroute or tracepath
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| All | Cross-cutting | Every layer can add delay |
| Physical | Distance/media | Propagation |
| Network/Transport | Congestion, reordering | Queuing, retransmission |

## Lab exercises

### Lab 1 — Baseline RTT distribution

```bash
ping -c 50 1.1.1.1
# Note min/avg/max/stddev if available — jitter matters for real-time
```

### Lab 2 — Local vs remote

```bash
ping -c 20 $(route -n get default | awk '/gateway:/ {print $2}')  # macOS default GW
ping -c 20 8.8.8.8
```

Compare LAN RTT vs Internet RTT.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| High RTT, low loss | Distance, satellite, suboptimal route | traceroute, geo path |
| Spiky RTT | Congestion, Wi-Fi, bufferbloat | interface util, AQM, wireless |
| App slow, ping fine | App chatty RTT × requests | HTTP waterfall, DB round trips |
| Sudden latency jump | Reroute / brownout | path change, ISP status |

## Common traps / interview gotchas

- Ping blocked ≠ high latency; it means ICMP filtered.
- Traceroute * shows timeouts on hop responses, not necessarily packet loss to destination.
- VPN adds processing + often longer path → latency tax.
- DNS latency happens *before* TCP; users blame “the network” for slow resolve.

## Mastery checklist

- [ ] Name four delay components
- [ ] Explain why BDP couples latency with TCP throughput
- [ ] Interpret ping min/avg/max thoughtfully
- [ ] Give one app that is bandwidth-bound vs latency-bound

## Related notes

- [[Bandwidth]] · [[Throughput]] · [[TCP]] · [[ICMP]] · [[DNS]] · [[Packet]]
- ← [[03-Performance/Index|Performance]] · [[01-Basic-Terminology/Index|Basic Terminology]]
