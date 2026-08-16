---
tags: [high-availability, networking, ccna, failover, ha]
aliases: [Failover, HA Failover, Fail-over]
layer: Resilience pattern
---

# Failover

## Learning objectives

- Define failover as shifting service from a failed primary path/device to a standby
- Contrast active/passive vs active/active
- Relate detection (hellos, health checks) to cutover time and user impact
- Connect examples: [[HSRP]]/[[VRRP]], [[Load-Balancer]] pairs, WAN / [[VPN]] underlays

## One-sentence definition

> **Failover** is the controlled (or automatic) handoff of forwarding or service responsibility from a failed or degraded component to a redundant partner so users keep reaching the destination — ideally with a blip, not an outage.

## Analogy

> Failover is a **understudy taking the stage** when the lead actor loses their voice. Detection is the stage manager’s stopwatch (hello timers / health checks). Too slow, and the audience boos (app timeouts). Too twitchy, and actors swap mid-aria every time someone coughs (flapping). Active/active is **two leads sharing scenes**; active/passive is one waiting in the wings ([[HSRP]] standby).

## Why it matters

HA designs are only as good as detection + state + DNS/VIP behavior. CCNA labs with FHRP and real SD-WAN both teach: redundancy without tested failover is cosplay.

## Deep dive

### Mental model

```text
Primary healthy ──hellos/probes──► Standby ready
Primary fails → detect → promote standby → optional failback later
```

### Mechanism

1. **Redundancy**: second box, link, or pool member exists.
2. **Detection**: BFD, FHRP hellos, LB probes, routing neighbors.
3. **Decision**: threshold crossed → role change.
4. **Data plane**: VIP/vMAC moves, route withdraws, pool removes member.
5. **Failback**: preempt/return-to-primary policies (careful).

### Patterns

| Pattern | Idea |
|---------|------|
| Active/passive | One forwards; one waits |
| Active/active | Both carry work; still need failure plan |
| Path failover | Routing/SD-WAN shifts underlay |
| Service failover | LB/DNS moves VIP or name |

### On the wire

Expect hello silence, gratuitous ARP, route updates, or [[TCP]] resets depending on design. [[Packet-Analysis]] during a controlled fail proves detection time.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Cross-layer pattern | L2 vMAC, L3 routes, L4 pools |
| OSI | Many | Detection often L3/L4; impact hits apps |

## Lab exercises

### Lab 1 — Time the blip

In a lab with [[HSRP]] or dual WAN, start `ping -c 100` to a far target; fail primary; count lost replies ≈ detection window.

### Lab 2 — Write an RFO template

After a failover event, draft: detection method, time-to-detect, time-to-recover, data-plane symptom, prevent flapping next time.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| No failover | Detection blocked | ACL on hellos, tracks |
| Flapping | Unstable link / aggressive timers | dampening, thresholds |
| Failover but apps die | State/ASNAT/DNS TTL | sticky sessions, conn table |
| Split brain | Dual primaries | fencing, L2 continuity |

## Common traps / interview gotchas

- Redundant gear ≠ tested failover — rehearse it.
- Stateful devices need session sync or accept resets.
- DNS TTLs can outlast your clever VIP move.
- Faster timers on lossy [[WLAN]]/satellite links cause false failovers — see [[LoRaWAN-Satellite]] latency.

## Mastery checklist

- [ ] Define detect → promote → recover
- [ ] Contrast active/passive vs active/active
- [ ] Give FHRP and LB examples
- [ ] Explain flap risk from aggressive timers

## Related notes

- [[HSRP]] · [[VRRP]] · [[GLBP]] · [[Load-Balancer]] · [[VPN]] · [[Packet-Analysis]] · [[QoS]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
