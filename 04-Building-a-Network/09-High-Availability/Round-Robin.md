---
tags: [high-availability, networking, ccna, load-balancing, round-robin]
aliases: [Round Robin, Round-Robin Load Balancing]
layer: Scheduling algorithm
---

# Round Robin

## Learning objectives

- Define round-robin as rotating new work evenly across members
- Explain weighted round-robin as capacity-aware rotation
- Know strengths/weaknesses vs [[Least-Connections]]
- Apply the idea at DNS, [[Load-Balancer]], and even [[GLBP]] assignment

## One-sentence definition

> **Round-robin** distributes each new connection (or request) to the next pool member in turn — like dealing cards — optionally with **weights** so bigger servers get more turns.

## Analogy

> Round-robin is a **dealer at a card table** handing one card (new session) to seat 1, then 2, then 3, then back to 1. Weighted round-robin gives the whale at seat 1 **two cards per cycle**. It doesn’t look at who is still eating a huge meal ([[Least-Connections]]) — it only tracks whose turn it is.

## Why it matters

Simplest algorithm interviewers expect. Works well when flows are similar; fails when one “turn” is a monster download and another is a tiny API call — then least-connections often wins.

## Deep dive

### Mental model

```text
New flow 1 → Server A
New flow 2 → Server B
New flow 3 → Server C
New flow 4 → Server A
...
Weighted 2:1 → A, A, B, A, A, B, ...
```

### Mechanism

1. Maintain ordered member list (healthy only).
2. On each new schedulable unit, pick next pointer.
3. Skip down members (health).
4. Optional: weight counters for uneven hardware.

### Where it shows up

| Place | Unit rotated |
|-------|----------------|
| [[Load-Balancer]] | Connections/requests |
| DNS | Answer order / RRset |
| [[GLBP]] | vMAC assignment (conceptually) |

### On the wire

No special “round-robin protocol” — you infer it from VIP distribution in logs or [[Packet-Analysis]] of many client connections landing on alternating backends.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Service distribution | Above routing |
| OSI | 4–7 decision | Scheduler policy |

## Lab exercises

### Lab 1 — Deal 12 connections

Three equal servers; write the sequence of assignments for 12 new connections under plain round-robin.

### Lab 2 — Weight math

Servers A:B = 3:1. Write one full cycle of assignments. Predict unfairness if A’s connections are huge file transfers.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| One server CPU hot | Uneven flow sizes | switch to [[Least-Connections]] |
| Uneven counts | Weights / persistence | sticky, weight config |
| New node idle | Not in pool / unhealthy | health, enabled flag |
| DNS “RR” ignored | Client caching | resolver behavior |

## Common traps / interview gotchas

- Round-robin ≠ equal *bytes* — equal *turns*.
- Persistence/sticky can defeat RR fairness.
- DNS round-robin is a weak LB (caching, no health).
- Don’t confuse with packet spraying on a single flow (that breaks [[TCP]]).

## Mastery checklist

- [ ] Define RR in one sentence
- [ ] Explain weighted RR
- [ ] Contrast with [[Least-Connections]]
- [ ] Place RR under [[Load-Balancer]] context

## Related notes

- [[Load-Balancer]] · [[Least-Connections]] · [[GLBP]] · [[Failover]] · [[DNS]] · [[TCP]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
