---
tags: [wireless, networking, ccna, wifi, channels, rf]
aliases: [Wi-Fi Channels, Channel Plan, RF Channel Planning]
layer: RF spectrum / L1 design
---

# Channel Planning

## Learning objectives

- Explain why Wi‑Fi channels must be planned like scarce parking spots
- Use non‑overlapping 2.4 GHz channels (1/6/11 in many regions) correctly
- Contrast 20/40/80/160 MHz widths and interference risk on 5/6 GHz
- Relate channel reuse to [[AP-Placement-and-Coverage]] and [[WLAN]] capacity

## One-sentence definition

> **Channel planning** assigns RF channels (and widths) to [[Access Points]] so neighboring cells don’t constantly talk over each other — turning shared spectrum into usable airtime.

## Analogy

> Channels are **radio talk groups / walkie-talkie frequencies**. If every AP and microwave yells on channel 6, nobody hears anything useful — it’s a cafeteria of overlapping conversations. A good plan is a **seating chart**: alternate talk groups so adjacent tables aren’t on the same frequency, and don’t give one table a megaphone that occupies four seats (ultra-wide channels) unless the room is empty.

## Why it matters

Auto-channel can be fine at home and catastrophic in dense offices. CCNA troubleshooting expects “check channel utilization / overlap” before blaming [[TCP]] or the firewall.

## Deep dive

### Mental model

```text
2.4 GHz (conceptual):
 Ch1          Ch6          Ch11
[====]       [====]       [====]   ← prefer these non-overlapping
  Ch3 overlaps 1+6 → avoid dense reuse

5/6 GHz:
 More channels → reuse with distance; wider = fewer unique channels
```

### Mechanism

1. Inventory APs, walls, and external interferers (neighbors, BLE, radar).
2. Pick band strategy: put capacity on 5/6; treat 2.4 as IoT/legacy coverage.
3. Assign channels to minimize co‑channel and adjacent interference.
4. Set width conservatively (20/40 first); widen only where spectrum is clean.
5. Revisit after RRM / site survey validation.

### Width tradeoffs

| Width | Upside | Downside |
|-------|--------|----------|
| 20 MHz | More unique channels, robust | Lower peak PHY |
| 40 MHz | More throughput | Fewer clean assignments |
| 80/160 | Fast on paper | Collision with DFS/neighbors |

### On the wire / air

Spectrum analyzers show energy; Wi‑Fi tools show duty cycle / retries. Wired [[Packet]] captures won’t show channel fights — only symptoms (loss, latency).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | RF under [[WLAN]] |
| OSI | 1 | Frequency, channelization |

## Lab exercises

### Lab 1 — Neighbor channel map

Use a Wi‑Fi analyzer; list strong SSIDs on 2.4 and their channels. Mark if your AP shares 1/6/11 with a neighbor.

### Lab 2 — Width experiment (lab only)

On lab gear, set 80 MHz then 20 MHz on 5 GHz. Compare perceived speed *and* stability with a neighbor AP nearby. Document the tradeoff.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| High util, few clients | Co‑channel interference | neighbor map, channel reuse |
| Random disconnects 5 GHz | DFS radar hit | channel event logs |
| 2.4 always miserable | Overlap / non‑Wi‑Fi noise | 1/6/11 plan, microwaves |
| One AP “slow” | Wrong width / bad channel | RRM history, manual pin |

## Common traps / interview gotchas

- In many regions, **1, 6, 11** are the non‑overlapping 2.4 set — using 3+8 is a classic mistake.
- Bonding channels without clean spectrum lowers everyone’s goodput.
- “Auto” isn’t magic; it needs time and can flap.
- Regulatory domains differ — don’t copy a US channel plan blindly worldwide.

## Mastery checklist

- [ ] Draw 2.4 non‑overlapping channels for your region
- [ ] Explain why wider ≠ always better
- [ ] Tie channel plan to AP density
- [ ] Name DFS as a 5 GHz gotcha

## Related notes

- [[WLAN]] · [[Access Points]] · [[WiFi-Standards]] · [[AP-Placement-and-Coverage]] · [[Wireless-Site-Surveys]] · [[Throughput]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
