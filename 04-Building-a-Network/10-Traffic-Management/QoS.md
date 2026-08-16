---
tags: [traffic-management, networking, ccna, qos]
aliases: [QoS, Quality of Service]
layer: Congestion management / policy
---

# QoS

## Learning objectives

- Define QoS as treating some traffic better (or differently) when the network is congested
- Map the toolkit: classification, marking, queuing, policing, [[Traffic-Shaping]]
- Explain why QoS cannot create bandwidth — only manage scarcity
- Tie markings (DSCP/CoS) to [[Packet-Prioritization]]

## One-sentence definition

> **QoS** (Quality of Service) is the set of mechanisms that **classify, mark, queue, shape, and police** traffic so critical applications keep acceptable [[Latency]], jitter, and loss when links contend for limited capacity.

## Analogy

> A link is a **single-lane bridge at rush hour**. Without QoS, cars ([[Packet]]s) merge randomly — ambulances (voice) sit behind moving trucks (backups). QoS is the **traffic cop + HOV rules**: classify vehicles, paint stickers (DSCP), give ambulances a priority lane ([[Packet-Prioritization]]), meter on-ramps ([[Traffic-Shaping]]), and ticket speeders who blow the rate limit (policing). The bridge doesn’t get wider; the chaos gets managed.

## Why it matters

Voice, video, and trading apps die from jitter/loss long before ping “looks fine.” CCNA expects models (DiffServ awareness), trust boundaries, and the difference between shaping and policing.

## Deep dive

### Mental model

```text
Classify → Mark (DSCP/CoS) → Queue / Schedule → Shape or Police → Transmit
                 ↑
           trust boundary (don’t trust random campus marks blindly)
```

### Mechanism

1. **Classification**: ACL, NBAR, ports, CAPWAP, etc.
2. **Marking**: set DSCP in IP; CoS in L2 [[Frame]] where used.
3. **Congestion management**: CBWFQ, LLQ for voice, etc.
4. **Congestion avoidance**: WRED drops before tail-drop meltdown.
5. **Rate control**: [[Traffic-Shaping]] (buffer/delay) vs police (drop/remark).

### Toolkit snapshot

| Tool | Effect |
|------|--------|
| Queuing / LLQ | Who leaves first under congestion |
| Shaping | Smooth to rate; buffer |
| Policing | Enforce rate; drop/remark |
| Marking | Carry intent across hops |

### On the wire

DSCP in IP TOS/Traffic Class; 802.1p/CoS in VLAN tags. [[Packet-Analysis]] can confirm marks; end-to-end QoS needs every hop to honor policy (or at least not bleach marks).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Mostly Network + link schedulers | DSCP + interface queues |
| OSI | 2–3 (+ app classify) | CoS / DSCP / NBAR |

## Lab exercises

### Lab 1 — Spot DSCP

Capture a voice or video packet if available (or mark in a lab router) and find DSCP in Wireshark IPv4/IPv6 headers.

### Lab 2 — Congestion storyboard

Draw a 10 Mbps WAN with bulk + voice. Write where you’d shape vs police and why voice wants LLQ — link [[Packet-Prioritization]].

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Voice choppy, ping OK | Jitter/queue latency | LLQ, marks, WAN util |
| Marks disappear | Rewrite/bleach | trust boundary, provider |
| Bulk starves | No bandwidth remaining | prioritization without limits |
| Drop spikes | Police too tight | shape instead; burst sizes |

## Common traps / interview gotchas

- QoS ≠ more bandwidth; undersized links stay undersized.
- Prioritizing *everything* prioritizes nothing.
- Scavenger/bulk should be limited or marked lower — not merely “best effort hope.”
- Wireless airtime fairness interacts with QoS — see [[WLAN]] realities.

## Mastery checklist

- [ ] Explain classify → mark → queue → shape/police
- [ ] Contrast shaping vs policing at a high level
- [ ] State QoS manages scarcity
- [ ] Point to DSCP as the common IP mark

## Related notes

- [[Traffic-Shaping]] · [[Packet-Prioritization]] · [[Latency]] · [[Throughput]] · [[Packet]] · [[Frame]] · [[Packet-Analysis]] · [[WLAN]]
- ← [[10-Traffic-Management/Index|Traffic Management]] · [[04-Building-a-Network/Index|Building a Network]]
