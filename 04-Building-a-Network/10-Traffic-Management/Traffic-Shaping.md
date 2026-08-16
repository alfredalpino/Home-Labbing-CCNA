---
tags: [traffic-management, networking, ccna, qos, shaping]
aliases: [Traffic Shaping, Shaping, Traffic Shaper]
layer: Rate control (buffer / delay)
---

# Traffic Shaping

## Learning objectives

- Define shaping as delaying packets to enforce an average rate
- Contrast shaping (buffer) vs policing (drop/remark)
- Explain token bucket / Tc / Be awareness at CCNA level
- Place shaping at WAN edges and [[VPN]] overlays before congestion explodes downstream

## One-sentence definition

> **Traffic shaping** meters egress traffic to a target rate by **queuing and delaying** packets (instead of immediately dropping), smoothing bursts so downstream links and contracts aren’t overrun.

## Analogy

> Policing is a **bouncer who rejects anyone over the guest count** (drops). Shaping is a **velvet rope line**: when the club ([[Throughput]] contract) is full, people wait in an orderly queue and enter at a controlled drip. Waiting adds [[Latency]]; rejection adds loss. Both enforce the rate — different pain.

## Why it matters

ISP contracts, MPLS, and SD-WAN overlays often need you to *shape to the purchased rate* so your router — not the provider’s unmarked drop — decides which packets wait. Pairs with [[QoS]] marking/queuing.

## Deep dive

### Mental model

```text
App bursts → Shaper queue → drip at CIR/avg rate → wire
                 ↑
         excess delayed (shaped) rather than hard-dropped (policed)
```

### Mechanism

1. Measure bytes over time (token bucket metaphor).
2. If tokens available, send; else hold in shaping queue.
3. Scheduler still applies [[Packet-Prioritization]] inside the shaper.
4. If queue overflows, *then* drops happen — size matters.

### Shape vs police

| | Shaping | Policing |
|--|---------|----------|
| Excess | Delay/buffer | Drop or remark |
| Latency | Can increase | Usually not (just loss) |
| Typical place | Outbound to WAN | Inbound enforcement, peering |

### On the wire

Shaped traffic looks smoother in graphs; bursts flatten. PCAPs show increased gap times under load — use [[Packet-Analysis]] plus interface counters.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Link egress behavior | Rate control before transmit |
| OSI | 2–3 device queues | Interface policy |

## Lab exercises

### Lab 1 — Draw the rope line

Sketch bulk + voice entering a shaper at 10 Mbps toward a 10 Mbps WAN. Show voice in LLQ inside the shaper.

### Lab 2 — Predict TCP behavior

Explain why shaping (delay) can be friendlier to [[TCP]] than hard policing (loss) for the same average rate — three bullets.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| High latency under load | Shaper queue buildup | rate vs offered load, queue depth |
| Still getting ISP drops | Shaped above contract | match true CIR, account overhead |
| Voice hurt inside shaper | No LLQ/priority | [[Packet-Prioritization]] config |
| Spiky graphs remain | Shape not applied | wrong interface/direction |

## Common traps / interview gotchas

- Shape on the **correct direction** (usually out toward the constrained link).
- Tunnel/[[VPN]] overhead means shape *below* line rate or still get drops.
- Huge shaper buffers = bufferbloat; tune with care.
- Shaping ≠ guaranteeing speed — only capping/smoothing.

## Mastery checklist

- [ ] Define shaping as delay-to-rate
- [ ] Contrast with policing drops
- [ ] Place shaping at WAN edge mentally
- [ ] Tie to parent [[QoS]] policy

## Related notes

- [[QoS]] · [[Packet-Prioritization]] · [[Throughput]] · [[Latency]] · [[VPN]] · [[TCP]] · [[Packet-Analysis]]
- ← [[10-Traffic-Management/Index|Traffic Management]] · [[04-Building-a-Network/Index|Building a Network]]
