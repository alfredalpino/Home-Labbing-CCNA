---
tags: [wireless, networking, ccna, wifi, rf-design]
aliases: [AP Placement, Wi-Fi Coverage, Cell Planning]
layer: RF design / physical
---

# AP Placement & Coverage

## Learning objectives

- Separate **coverage** (can hear) from **capacity** (enough airtime)
- Place [[Access Points]] for overlap suitable for roaming, not just “max walls”
- Explain how walls, floors, and power settings reshape cells
- Tie placement mistakes to sticky clients and dead zones in a [[WLAN]]

## One-sentence definition

> **AP placement** is the physical and RF design of where [[Access Points]] sit, how loud they transmit, and how their cells overlap so users get continuous, usable [[WLAN]] service — not just a green bars icon.

## Analogy

> Coverage is **streetlights on a dark road**. One giant floodlight in the middle leaves blinding glare near the pole and dark patches between trees (walls). Good design uses **many medium lamps with intentional overlap** so you can walk (roam) without stepping into blackness — and without lighting the neighbor’s bedroom (bleed / co‑channel interference).

## Why it matters

Most “buy a stronger AP” failures are placement problems: APs in closets, wrong power, one AP trying to cover three floors. CCNA labs and real floors both punish RF ignorance.

## Deep dive

### Mental model

```text
Floor plan
  [AP]······overlap······[AP]······overlap······[AP]
     \      /                \      /
      wall attenuates         stairwell hole
Clients need: primary AP + neighbor audible for roam
```

### Mechanism

1. **Site needs**: density (users/m²), apps (voice/video), building materials.
2. **Mount**: ceiling preferred; avoid metal cabinets and elevator shafts as “homes.”
3. **Power / antennas**: lower power often *helps* by shrinking cells and reducing interference.
4. **Overlap**: enough for roaming (~15–20% conceptual target — vendor tools refine this).
5. **Wired**: PoE budget, switch uplink, VLAN trunking to each AP.

### Coverage vs capacity

| Goal | Design lever |
|------|----------------|
| Coverage | More APs or better placement / antennas |
| Capacity | More cells, 5/6 GHz, right channel plan |
| Both | Don’t crank TX power to “fix” holes |

### On the wire / air

Placement lives in RF: RSSI, SNR, retry rates. Wired side only shows whether the AP has link/PoE. A perfect Ethernet [[Frame]] path cannot fix a concrete wall.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | Physical RF under the [[WLAN]] |
| OSI | 1 (mostly) | Propagation, antennas, power |

## Lab exercises

### Lab 1 — Heatmap by foot

Walk your home/office with a phone Wi‑Fi analyzer. Mark rooms with strong / usable / dead. Guess wall materials that match the map.

### Lab 2 — One AP power thought experiment

If you lower AP TX power, predict: cell size, co‑channel neighbors, roaming behavior. Write three bullets before changing anything in a lab.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| One room always bad | Hole / attenuation | AP location, wall type, secondary AP |
| Connected everywhere, slow | Capacity / interference | channel util, client count per AP |
| Calls drop mid-hallway | Insufficient overlap | roam thresholds, neighbor AP hearing |
| Strong RSSI, high retries | Noise / multipath | SNR, not just bars |

## Common traps / interview gotchas

- High RSSI ≠ good SNR; noise floor matters.
- Max power is not “best”; it creates giant cells and sticky clients.
- Mounting an AP next to a metal rack turns it into a weird directional antenna.
- Mesh/wireless backhaul placement is a *second* RF problem on top of client RF.

## Mastery checklist

- [ ] Distinguish coverage vs capacity in one sentence
- [ ] Explain intentional overlap for roaming
- [ ] Argue why lowering power can improve a campus
- [ ] Relate placement to [[Access Points]] and [[Roaming-and-Band-Steering]]

## Related notes

- [[Access Points]] · [[WLAN]] · [[Channel-Planning]] · [[Wireless-Site-Surveys]] · [[Roaming-and-Band-Steering]] · [[WiFi-Standards]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
