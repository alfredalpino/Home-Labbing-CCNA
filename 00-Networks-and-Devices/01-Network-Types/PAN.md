---
tags: [network-types, networking, ccna, pan]
aliases: [Personal Area Network, PAN]
layer: Scope
---

# PAN

## Learning objectives

- Define PAN as person-centric, very short-range networking
- Give examples (Bluetooth, USB tethering, Wearables)
- Contrast PAN vs [[LAN]] / [[WLAN]]
- Know when PAN traffic still hits enterprise security policy

## One-sentence definition

> A **PAN** (Personal Area Network) links devices around a single person — typically within a few meters — such as phone↔earbuds, watch↔phone, or laptop↔phone tethering.

## Analogy

> A PAN is the **stuff clipped to your backpack and pockets** talking to each other: watch, earbuds, phone hotspot. It’s not the office building’s street grid ([[LAN]]); it’s your personal bubble’s whispering network.

## Why it matters

PANs seem “too small for CCNA,” but they create real paths: phone hotspots become [[WAN]] uplinks; Bluetooth keyboards appear in asset inventories; USB tethering bypasses corporate Wi‑Fi controls. Engineers must recognize the *path*, not dismiss the acronym.

## Deep dive

### Mental model

```text
Watch ──BT── Phone ──LTE/Wi‑Fi── Internet
               └──USB tether── Laptop
```

### Examples

| Tech | PAN role |
|------|----------|
| Bluetooth / BLE | Audio, peripherals, sensors |
| USB tethering | Phone shares WAN to laptop |
| Wi‑Fi Direct / hotspot | Phone as AP (often overlaps [[WLAN]] ideas) |
| NFC | Ultra-short, usually not a full “network stack” conversation |

### Security angle

Personal hotspots and rogue PANs can bridge untrusted Internet into a managed laptop — treat as an alternate underlay.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Scope | Cross-layer | Very local personal fabric |
| Often | L1–L2 + profiles | Bluetooth stacks differ from Ethernet |

## Lab exercises

### Lab 1 — Trace a tether path

Enable phone hotspot; connect laptop; run `traceroute 1.1.1.1`. Note hop0 is phone/NAT.

### Lab 2 — Inventory PAN devices

List paired Bluetooth devices on your phone/laptop; which ones carry IP vs audio profiles only?

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Hotspot works, corp VPN fails | Policy / MTU / DNS | VPN logs, split tunnel |
| BT audio drops | RF congestion | 2.4 GHz Wi‑Fi overlap |
| Tether no Internet | Carrier/APN / phone data | phone WAN status |

## Common traps / interview gotchas

- PAN ≠ always IP. Many Bluetooth links never assign 192.168 addresses.
- Don’t call office Wi‑Fi a PAN — wrong scope.
- Exam answers often cite Bluetooth as classic PAN.

## Mastery checklist

- [ ] Define PAN with distance + person-centric idea
- [ ] Give three examples
- [ ] Contrast PAN vs WLAN
- [ ] Explain one security bypass risk (hotspot/tether)

## Related notes

- [[LAN]] · [[WLAN]] · [[WAN]] · [[Access Points]] · [[Modems]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
