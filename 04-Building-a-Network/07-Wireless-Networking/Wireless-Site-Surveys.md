---
tags: [wireless, networking, ccna, wifi, site-survey]
aliases: [Wi-Fi Site Survey, RF Survey, Wireless Survey]
layer: Design / validation process
---

# Wireless Site Surveys

## Learning objectives

- Define predictive, passive, and active (AP-on-a-stick) surveys
- Explain what data a survey collects (RSSI, SNR, interference, roaming)
- Connect surveys to [[AP-Placement-and-Coverage]] and [[Channel-Planning]]
- Know when a “walkaround with a phone” is enough vs when tools are required

## One-sentence definition

> A **wireless site survey** measures or predicts RF behavior in a real building so you place [[Access Points]], set power/channels, and validate that the [[WLAN]] meets coverage and capacity goals *before* (or after) users complain.

## Analogy

> A survey is an **acoustic check of a concert hall** before opening night. Predictive design is the architect’s simulation; a passive survey is walking the empty hall with a sound meter listening to existing noise; an active survey is putting a test speaker ([[Access Points|AP]] on a stick) on stage and measuring every seat. You don’t guess where the dead spots are from the lobby brochure.

## Why it matters

Guessing AP count from square footage fails in warehouses, hospitals, and concrete campuses. Surveys turn RF from folklore into evidence — the same mindset as [[Packet-Analysis]] for wired faults.

## Deep dive

### Mental model

```text
Requirements → predictive model → install/pilot → validate survey → tune → accept
     ^                                              |
     └──────── capacity/voice SLAs ←────────────────┘
```

### Survey types

| Type | What you do | Best for |
|------|-------------|----------|
| Predictive | Floor plans + materials in software | Early BOM / rough AP count |
| Passive | Listen to existing RF / SSIDs | Interference, neighbor audit |
| Active | Associate / iPerf / roam tests | Prove throughput & roam |
| AP-on-a-stick | Temporary AP, measure cell | Validate placement before cable pulls |

### Mechanism

1. Capture requirements: density, voice, scanners, IoT bands.
2. Model or measure attenuation (walls, racks, elevators).
3. Propose AP locations and channel plan.
4. Validate with heatmaps + real client tests (not just colored blobs).
5. Document as-built for future changes ([[VPN]] rooms, new walls, etc.).

### On the wire / air

Survey tools care about RF metrics and sometimes active traffic. Ethernet only proves the AP has power and uplink — necessary but not sufficient.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access design | Ensures RF under IP works |
| OSI | 1 primarily | Propagation validation |

## Lab exercises

### Lab 1 — Mini passive survey

Walk three rooms with a Wi‑Fi analyzer. Record strongest RSSI, channel, and visible AP count. Circle one problem zone and hypothesize cause.

### Lab 2 — Active smoke test

```bash
# From a client in the problem zone — replace TARGET with a LAN iperf server if you have one
ping -c 50 <gateway-or-server>
# Note loss/jitter; compare to a known-good room
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Predictive looked fine, real bad | Wrong wall attenuation | validate survey, materials |
| Heatmap green, apps fail | Capacity / retries ignored | airtime, active tests |
| New dead zone after remodel | Environment change | re-survey affected wing |
| Voice roam fails | Overlap not validated | roam path walk test |

## Common traps / interview gotchas

- Colored heatmap ≠ user experience; always spot-check with real clients.
- Surveying only empty buildings misses body attenuation and Monday density.
- One survey for data may fail voice/RTLS requirements.
- Post-install validation is part of the job — not optional paperwork.

## Mastery checklist

- [ ] Name three survey types and when to use each
- [ ] List metrics beyond RSSI (SNR, util, roam)
- [ ] Tie survey outputs to placement and channels
- [ ] Explain predictive vs validate-in-field

## Related notes

- [[WLAN]] · [[Access Points]] · [[AP-Placement-and-Coverage]] · [[Channel-Planning]] · [[WiFi-Standards]] · [[Packet-Analysis]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
