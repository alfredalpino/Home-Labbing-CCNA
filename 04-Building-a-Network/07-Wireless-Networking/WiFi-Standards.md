---
tags: [wireless, networking, ccna, wifi, 802.11]
aliases: [Wi-Fi Standards, 802.11 Standards, IEEE 802.11]
layer: Physical + Data Link (RF / MAC)
---

# Wi‑Fi Standards

## Learning objectives

- Name the major IEEE 802.11 generations (a/b/g/n/ac/ax/be) and their bands
- Relate PHY rate marketing numbers to real shared [[Throughput]]
- Explain why 2.4 / 5 / 6 GHz behave differently for coverage vs capacity
- Map standards awareness to [[WLAN]] design and client capability

## One-sentence definition

> **Wi‑Fi standards** (IEEE **802.11** amendments) define how radios encode, share, and secure wireless [[LAN]] frames — each generation adds bands, MIMO tricks, and efficiency so more clients fit in the same airtime.

## Analogy

> Think of Wi‑Fi generations as **highway lane upgrades**. 802.11b was a single dirt lane; g paved it; n added lanes (MIMO) and better markings; ac built a fast expressway mostly at 5 GHz; ax (Wi‑Fi 6) added smart traffic lights (OFDMA/scheduling) so rush hour doesn’t gridlock; be (Wi‑Fi 7) adds even wider multi‑lane expressways and better merging. The road still has a **shared speed limit of physics** — more cars still wait at the light ([[Access Points]] / CSMA).

## Why it matters

Ticket language is “Wi‑Fi 5 vs Wi‑Fi 6,” but the engineer must translate that into band, channel width, client capability, and AP firmware. CCNA-level awareness stops you buying “gigabit Wi‑Fi” stickers while blaming the [[WAN]] for RF pain.

## Deep dive

### Mental model

```text
Client radio  ←→  AP radio(s)
   |                   |
 802.11 PHY/MAC    wired Ethernet to switch
   |
 bands: 2.4 GHz | 5 GHz | 6 GHz (ax/be)
 generations: a/b/g/n/ac/ax/be
```

### Generation cheat sheet

| Marketing | IEEE | Primary band(s) | Headline idea |
|-----------|------|-----------------|---------------|
| — | 802.11a | 5 GHz | Early OFDM, short range |
| — | 802.11b | 2.4 GHz | DSSS, crowded ISM |
| — | 802.11g | 2.4 GHz | OFDM on 2.4, faster than b |
| Wi‑Fi 4 | 802.11n | 2.4 + 5 | MIMO, channel bonding |
| Wi‑Fi 5 | 802.11ac | 5 GHz | Wider channels, MU‑MIMO (later) |
| Wi‑Fi 6/6E | 802.11ax | 2.4/5 (+6E) | OFDMA, denser clients |
| Wi‑Fi 7 | 802.11be | 2.4/5/6 | Ultra-wide channels, MLO |

### Mechanism

1. **PHY** chooses modulation/coding and spatial streams → advertised link rate.
2. **MAC** shares the medium (CSMA/CA historically; ax adds scheduled OFDMA).
3. Client and [[Access Points|AP]] negotiate the highest mutually supported mode.
4. Traffic is bridged to Ethernet on the wired side of the [[WLAN]].

### On the wire / air

On the air you see 802.11 management/data frames (beacons, probes, data). On the switch you see Ethernet [[Frame]]s — PHY rate and RF retries are invisible there. A 1200 Mbps PHY might deliver a few hundred Mbps TCP if the cell is busy.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | 802.11 as LAN technology under IP |
| OSI | 1–2 | RF PHY + 802.11 MAC |

## Lab exercises

### Lab 1 — Inventory client capabilities

On a laptop/phone, open Wi‑Fi details and note supported bands (2.4/5/6) and standard (n/ac/ax). Compare to your AP’s advertised mode.

### Lab 2 — Band vs throughput feel

```bash
# Same gateway, compare bands if your OS lets you force 2.4 vs 5
ping -c 30 $(route -n get default | awk '/gateway:/ {print $2}')
# Note min/avg/max RTT and loss — not a full speed test, but RF health signal
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| “Fast AP,” slow phone | Client stuck on legacy / 2.4 | client capabilities, band steering |
| Great signal, bad Zoom | Retries / airtime / width mismatch | channel util, interference, MCS |
| New Wi‑Fi 6E SSID invisible | No 6 GHz client / regulatory | client chipset, country code |
| Mixed b/g clients slow cell | Protection / low rates | disable legacy rates carefully |

## Common traps / interview gotchas

- Marketing Mbps ≠ application [[Throughput]]; airtime is shared and half‑duplex-ish in practice.
- 802.11ac is primarily 5 GHz; “ac on 2.4” usually means concurrent n/g radios.
- Wider channels (80/160 MHz) need clean spectrum — bonding into interference hurts more than it helps.
- Wi‑Fi 6 helps **dense** cells; one lonely laptop may not feel magical.

## Mastery checklist

- [ ] Map Wi‑Fi 4/5/6/7 to 802.11n/ac/ax/be
- [ ] Explain 2.4 vs 5 vs 6 GHz tradeoffs
- [ ] Separate PHY rate from TCP goodput
- [ ] Relate standards to [[WLAN]] / [[Access Points]] design choices

## Related notes

- [[WLAN]] · [[Access Points]] · [[Access-Points-Controllers]] · [[Channel-Planning]] · [[Throughput]] · [[Latency]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
