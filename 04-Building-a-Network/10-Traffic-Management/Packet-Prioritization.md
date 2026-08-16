---
tags: [traffic-management, networking, ccna, qos, prioritization]
aliases: [Packet Prioritization, Priority Queuing, LLQ]
layer: Scheduling / congestion management
---

# Packet Prioritization

## Learning objectives

- Define prioritization as scheduling some [[Packet]]s ahead of others under congestion
- Relate DSCP/CoS marks to queue assignment
- Explain LLQ / priority queue awareness for voice
- Warn about starvation and why prioritization needs companions ([[Traffic-Shaping]], bandwidth limits)

## One-sentence definition

> **Packet prioritization** is the scheduler’s choice to dequeue high-importance packets first (or with preferential treatment) when multiple queues compete for the same outbound wire — the sharp end of [[QoS]].

## Analogy

> Prioritization is the **express lane / ambulance cut-in** at the bridge from the [[QoS]] analogy. Stickers on cars (DSCP) decide who may enter the express lane. If you hand *everyone* an ambulance sticker, the express lane becomes the regular lane again. If ambulances never yield capacity planning to trucks, trucks starve in the ditch (queue starvation) — so cops still meter the on-ramp ([[Traffic-Shaping]]).

## Why it matters

Jitter kills VoIP. Prioritization is how engineers keep interactive traffic responsive without buying infinite bandwidth. Interviewers want LLQ awareness and the starvation caveat.

## Deep dive

### Mental model

```text
Marked packets → class queues
                  ├─ Priority/LLQ (voice) ──┐
                  ├─ AF / business ─────────┼→ scheduler → tx ring → wire
                  └─ BE / scavenger ────────┘
```

### Mechanism

1. Classify/mark (or trust marks).
2. Assign to queues (priority vs bandwidth classes).
3. Under congestion, priority queue serviced preferentially (often policed to a cap).
4. Remaining bandwidth shared by CBWFQ weights among other classes.
5. Without congestion, prioritization barely matters — everyone goes.

### Marks → intent (examples)

| Traffic | Typical intent |
|---------|----------------|
| Voice bearer | EF / LLQ |
| Video | AF classes |
| Bulk backup | BE or lower |

### On the wire

Prioritization is local to each hop’s scheduler. Marks are the *signal*; if a hop ignores them, priority dies. Confirm with delay tests + occasional [[Packet-Analysis]] of DSCP.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Forwarding device queues | Per-hop behavior |
| OSI | 2–3 | CoS/DSCP-informed scheduling |

## Lab exercises

### Lab 1 — Congestion A/B

With a lab shaper creating artificial congestion, send bulk + latency-sensitive traffic. Compare RTT with and without a priority class.

### Lab 2 — Starvation sketch

Write what happens if priority traffic is uncapped at 95% of a link while bulk shares the rest. Propose a fix (priority police / bandwidth limit).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Voice still jittery | Not marked or not honored | DSCP end-to-end, LLQ |
| Bulk never moves | Starvation | priority police, weights |
| Priority on wrong apps | Bad classify | ACLs/NBAR accuracy |
| Fine until WAN | Edge missing policy | shape+queue on WAN int |

## Common traps / interview gotchas

- Priority without a rate limit can starve everything else.
- Prioritization only helps when the link is a bottleneck you control.
- Rewriting DSCP at the trust boundary can undo campus intent.
- Wi‑Fi airtime is another scheduler — wired LLQ doesn’t fix RF contention alone ([[WLAN]]).

## Mastery checklist

- [ ] Define prioritization as dequeue preference
- [ ] Tie marks to queues
- [ ] Explain LLQ + police-to-cap idea
- [ ] Name starvation as the classic foot-gun

## Related notes

- [[QoS]] · [[Traffic-Shaping]] · [[Latency]] · [[Packet]] · [[WLAN]] · [[Packet-Analysis]] · [[Throughput]]
- ← [[10-Traffic-Management/Index|Traffic Management]] · [[04-Building-a-Network/Index|Building a Network]]
