---
tags: [basic-terminology, networking, ccna, media]
aliases: [Transmission Media, Cable Types, Fiber Copper Wireless]
layer: Physical (Layer 1)
---

# Transmission Media Types

## Learning objectives

- Compare copper, fiber, and wireless as physical media
- Choose media based on distance, EMI, bandwidth, cost, and security
- Know common connector/cable categories used in enterprise LANs
- Tie media faults to symptoms (CRC, light levels, Wi-Fi retries)

## One-sentence definition

> **Transmission media** are the physical (or radiative) paths that carry signals representing bits — primarily copper cabling, optical fiber, and wireless RF — forming Layer-1 of the network.

## Analogy

> Media is the **road surface**: copper streets, fiber express tunnels, and wireless open air. Protocols are traffic laws; media is what your tires actually touch. Potholes (CRC/light levels) beat fancy GPS (routing) every time.

## Why it matters

Fancy protocols die on bad Layer-1. Most “random” drops are cables, dirty fiber, failing SFPs, or RF interference. Before redesigning OSPF, prove the media.

## Deep dive

### Mental model

```text
Bits ↔ analog/digital signal ↔ MEDIA ↔ receiver recovers bits ↔ frames
```

Constraints: **bandwidth**, **distance**, **attenuation**, **noise/EMI**, **cost**, **security** (easier to tap copper/wireless than fiber — still not “unhackable”).

### Copper (twisted pair)

| Category | Typical use | Notes |
|----------|-------------|-------|
| Cat5e | 1 Gb/s to 100m | Still common |
| Cat6 | 1 Gb/s; 10 Gb/s shorter runs | Better NEXT |
| Cat6A | 10 Gb/s to 100m | Data center / future-proof offices |
| Cat7/8 | Higher-rate / short DC | Less common in campus horizontal |

**Connectors:** RJ-45 for Ethernet copper.  
**Failure modes:** bad crimps, split pairs, EMI near power, exceeding 100m horizontal, water in outdoor cable.

**Coax** still appears in DOCSIS/cable plants and some video — not modern office Ethernet horizontal.

### Fiber optics

| Type | Core | Distance/Bandwidth |
|------|------|--------------------|
| MMF (OM3/OM4) | Larger core | Shorter; cheap optics for campus/DC |
| SMF (OS2) | Small core | Long haul / campus backbone / ISP |

**Connectors:** LC (common SFP), SC, MPO/MTP (parallel optics).  
**Transceivers:** SFP/SFP+/QSFP — match fiber type, wavelength, distance rating.

**Failure modes:** dirty endfaces (clean before you complain), macrobends, wrong polarity, TX/RX swap, mismatched SR vs LR optics.

### Wireless

- **Wi-Fi (802.11):** shared medium, contention, SNR-limited rates, roaming.
- **Cellular / microwave / satellite:** WAN flavors with different latency profiles ([[Latency]]).

Wireless “bandwidth” is shared airtime; walls and interference dominate.

### On the wire / fields

Media doesn’t add a header — it carries the signal for [[Frame]] bits. Optics have digital diagnostics (DOM): TX/RX power, temperature.

```bash
# Interface errors often scream Layer-1
netstat -I en0 -w 1   # macOS packet/error counters style
# On Cisco: show interfaces  → CRC, input errors, output errors
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access / Physical | Bit transmission |
| OSI | 1 | Physical media & signaling |

## Lab exercises

### Lab 1 — Inventory your links

List every path from laptop → AP/switch → router → ISP. Label each segment copper / fiber / wireless.

### Lab 2 — Symptom correlation

Intentionally use a damaged cable in a lab (or flap link). Watch link lights, speed/duplex renegotiation, and CRC counters.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| CRC/input errors | Cable/duplex/EMI | replace patch, hardcode/autoneg, path away from power |
| Link down | Cable cut / SFP / shut | lights, DOM power, `show int` |
| Slow Wi-Fi, good Ethernet | RF / contention | channel, RSSI, interference |
| Optics up/down | Dirty fiber / wrong optic | clean, verify LR vs SR, SMF vs MMF |

## Common traps / interview gotchas

- Autonegotiation failures → duplex mismatch → high errors + “weird slowness.”
- Fiber distance ratings assume clean plant and correct optics — not magic.
- PoE copper budgets matter for AP/camera density.
- “Airplane mode” is a host RF kill switch — not a routing issue.

## Mastery checklist

- [ ] Pick copper vs fiber for 80m office run vs 10 km campus
- [ ] Name Cat6 vs Cat6A use cases
- [ ] Explain why dirty fiber causes intermittent errors
- [ ] Map CRC errors to Layer-1 first actions

## Related notes

- [[Bandwidth]] · [[Latency]] · [[Throughput]] · [[Frame]] · [[Packet]]
- ← [[05-Physical/Index|Physical]] · [[01-Basic-Terminology/Index|Basic Terminology]]
