---
tags: [basic-terminology, networking, ccna, throughput]
aliases: [Goodput, Transfer Rate, Effective Rate]
layer: Cross-layer performance metric
---

# Throughput

## Learning objectives

- Define throughput vs [[Bandwidth]] vs goodput
- Explain factors that reduce throughput (loss, RTT, window, overhead, CPU)
- Measure throughput with the right tools (not ping)
- Reason about single-flow vs aggregate throughput

## One-sentence definition

> **Throughput** is the actual rate of successful data transfer over a path for a given flow or aggregate, measured in bits/s or bytes/s over a time interval.

## Analogy

> Throughput is **how much water you actually collected in a bucket per second**. Bandwidth is the pipe rating on the box; throughput is your measured fill rate after leaks, sharing, and waiting for acknowledgments.

## Why it matters

SLAs, backups, and user “network is slow” complaints are about throughput (and completion time). You upgrade bandwidth only after proving the bottleneck is capacity — not loss, latency, Wi-Fi airtime, disk, or server CPU.

## Deep dive

### Mental model

```text
Bandwidth  ≥  Throughput  ≥  Goodput
   (cap)        (on wire success)   (app payload after headers/retransmits)
```

### Mechanism — what limits TCP throughput (intuition)

Rough ceiling for a single TCP flow (order-of-magnitude teaching model):

```text
Throughput ≲ Window / RTT
```

Also roughly sensitive to loss: higher loss → more recovery → lower rate. That’s why a “little” packet loss destroys WAN transfers.

Other limiters:

- Receiver disk/CPU
- Server app concurrency
- Crypto ([[SSL-TLS]]) CPU
- Wi-Fi contention
- Middlebox policing / shaping
- Small IO sizes / chatty protocols (many RTTs)

### UDP throughput

No built-in congestion control (unless app/QUIC provides it). You can blast UDP and lose most of it — high *send* rate ≠ high *useful* throughput.

### On the wire

Measure with:

```bash
# iperf3 (lab standard)
iperf3 -s                 # server
iperf3 -c SERVER_IP -t 30 # client

# Rough HTTPS download timing
curl -o /dev/null -w 'time=%{time_total}s size=%{size_download}\n' https://example.com/...
```

Counters: interface `bytes/sec`, SNMP ifHCInOctets, NetFlow/IPFIX.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Cross-layer | End-to-end | Emergent property of path + protocols + endpoints |
| Transport | TCP | Window, congestion control dominate many flows |

## Lab exercises

### Lab 1 — Bandwidth vs measured throughput

On two lab hosts connected at 1 Gb/s, run `iperf3`. If you get ~940 Mb/s, explain where ~6% went (headers, framing, protocol overhead).

### Lab 2 — Latency’s effect (thought + optional WAN emulator)

Compare `iperf3` on LAN vs through a high-latency VPN. Watch single-flow throughput drop even if “bandwidth” is high.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Speed test low on Wi-Fi | Signal/airtime/interference | RSSI, channel, retry rate |
| One flow slow, aggregate OK | Per-flow shaper / TCP issues | parallel iperf streams `-P` |
| Throughput collapses periodically | Microbursts, bufferbloat, wifi scan | latency under load, AQM |
| Asymmetric results | Asymmetric link / reverse path | test both directions |

## Common traps / interview gotchas

- Ping does **not** measure throughput.
- Browser download ≠ link capacity (CDN, disk, single connection limits).
- “99% bandwidth utilization” can still mean bad application latency (bufferbloat).
- Goodput matters for backups; line-rate with tiny payload efficiency still wastes capacity.

## Mastery checklist

- [ ] Define throughput vs bandwidth in one sentence each
- [ ] Explain Window/RTT intuition
- [ ] Run and interpret an iperf3 test
- [ ] List five non-bandwidth reasons transfers are slow

## Related notes

- [[Bandwidth]] · [[Latency]] · [[TCP]] · [[UDP]] · [[Packet]] · [[SSL-TLS]]
- ← [[03-Performance/Index|Performance]] · [[01-Basic-Terminology/Index|Basic Terminology]]
