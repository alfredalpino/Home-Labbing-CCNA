---
tags: [high-availability, networking, ccna, load-balancing, least-connections]
aliases: [Least Connections, Least-Conn]
layer: Scheduling algorithm
---

# Least Connections

## Learning objectives

- Define least-connections as sending new work to the member with the fewest active connections
- Explain why it helps when session durations differ
- Contrast with [[Round-Robin]] and note weighted variants
- Spot when connection count is a bad proxy for load (UDP, short APIs, elephant flows)

## One-sentence definition

> **Least-connections** load balancing assigns each new session to the healthy pool member currently holding the **fewest open connections**, aiming to even out concurrency rather than mere turn-taking.

## Analogy

> If [[Round-Robin]] is a **card dealer**, least-connections is a **restaurant host** who always seats the next party at the table with the fewest diners still eating. A table stuck with a three-hour feast (long download) stops getting new guests until it clears — smarter than blindly rotating seats.

## Why it matters

Real pools mix chatty APIs and fat streams. Least-conn is the default “smarter than RR” answer on many [[Load-Balancer]]s — know its blind spots for interviews and tuning.

## Deep dive

### Mental model

```text
Server A: 120 conns
Server B:  40 conns  ← next new client goes here
Server C:  41 conns
```

### Mechanism

1. Track active connection count per member (L4) or outstanding requests (L7).
2. On new schedulable unit, pick minimum count (tie-break: RR or hash).
3. Increment/decrement as sessions open/close.
4. Weighted least-conn scales the metric by capacity factor.

### When it shines / fails

| Situation | Likely fit |
|-----------|------------|
| Varied session length | Strong |
| Uniform short APIs | Similar to RR |
| Huge single elephant flow | Still one conn — CPU may skew |
| UDP without clear “conn” | Need careful definition |

### On the wire

Again, no special protocol — observe VIP choice via server logs or LB stats. [[Packet-Analysis]] alone won’t name the algorithm without correlation.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Mostly L4 session awareness | Conn tracking |
| OSI | 4–7 | Counts may be HTTP requests |

## Lab exercises

### Lab 1 — Predict seating

A=5, B=5, C=1 connections. Where do the next three clients go if none close? Write the running counts.

### Lab 2 — Elephant critique

One [[TCP]] flow saturates a 10G NIC but counts as “1 connection.” Explain why least-conn may still overload that server and what you’d try next (weight, least-bandwidth, L7 queue).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Still unbalanced CPU | Elephant flows | bandwidth-aware algo, QoS |
| Flapping assignments | Conn churn / bad timers | persistence, slow-start |
| New node overload | Empty counts magnet | slow ramp / warm-up |
| UDP mess | Fake conn tracking | idle timeouts |

## Common traps / interview gotchas

- Least-conn ≠ least CPU or least latency.
- A just-added empty server can get slammed (“thundering herd”) — warm-up matters.
- Persistence can freeze an imbalance.
- Pair with health checks; never balance to a dead member with “0 conns.”

## Mastery checklist

- [ ] Define least-conn vs [[Round-Robin]]
- [ ] Give one case where least-conn wins
- [ ] Give one case where counts mislead
- [ ] Tie back to [[Load-Balancer]] pools

## Related notes

- [[Load-Balancer]] · [[Round-Robin]] · [[Failover]] · [[TCP]] · [[QoS]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
