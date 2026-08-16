---
tags: [wireless, networking, ccna, bluetooth, nfc, pan]
aliases: [Bluetooth, NFC, Bluetooth and NFC]
layer: PAN / short-range radio
---

# Bluetooth & NFC

## Learning objectives

- Place Bluetooth and NFC as **personal-area** radios, not campus [[WLAN]] replacements
- Contrast range, pairing, and typical network-engineer touchpoints
- Know when BT/NFC show up in tickets (audio, printers, payment, provisioning)
- Link to [[PAN]] and contrast with [[WLAN]] / [[Access Points]]

## One-sentence definition

> **Bluetooth** is a short‑range wireless PAN technology for peripherals and audio; **NFC** (Near Field Communication) is an ultra‑short‑range radio for tap‑to‑pair, payments, and tags — both live near the human body, not the building RF plan.

## Analogy

> [[WLAN]] is the **office PA system** — one tower ([[Access Points]]) covers a floor. Bluetooth is **walkie-talkies between you and your headset** across a desk. NFC is **whispering while bumping shoulders** — intentional, inches apart, hard to eavesdrop from the hallway. Different conversations; don’t tune the PA to fix a headset.

## Why it matters

Network engineers get dragged into “wireless” tickets that are BT interference on 2.4 GHz, rogue BT bridges, or NFC badge quirks. Knowing the lane prevents mis-blaming the WLC.

## Deep dive

### Mental model

```text
Phone ─BT── Headphones / keyboard / IoT
Phone ─NFC─ Tag / payment terminal / tap-to-pair Wi‑Fi (some vendors)
Phone ─Wi‑Fi─ AP ─ LAN/Internet     ← separate radio path
```

### Comparison

| Trait | Bluetooth | NFC |
|-------|-----------|-----|
| Range | ~meters (class-dependent) | ~cm |
| Typical use | Audio, HID, beacons | Pay, tap pair, access cards |
| Topology | Piconet / LE connections | Initiator–target |
| Overlap with Wi‑Fi | 2.4 GHz coexistence | Usually not a capacity peer |

### Mechanism

- **Bluetooth Classic/LE**: discover, pair/bond, encrypt link, stream profiles (A2DP, HID, etc.).
- **NFC**: inductive coupling; read tag NDEF or run card-emulation; often *triggers* another channel (BT/Wi‑Fi) rather than carrying bulk data.

### On the wire / air

You rarely “tcpdump NFC.” BT may appear as interference energy on 2.4 GHz Wi‑Fi. Some enterprise tools inventory BT beacons separately from [[WLAN]] clients.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Often non-IP or alternate stack | Profiles above RF |
| OSI | 1–2 (+ app profiles) | PAN radios |

## Lab exercises

### Lab 1 — Inventory PAN devices

List paired Bluetooth devices on your phone/laptop. Note which would break if 2.4 GHz Wi‑Fi were saturated.

### Lab 2 — NFC intent check

Find one NFC tag or payment tap use-case around you. Write whether data stayed on NFC or handed off to Wi‑Fi/BT/Internet.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Wi‑Fi 2.4 miserable near desks | BT dense + Wi‑Fi | band steer clients to 5/6 |
| Headset drops | BT range/interference | distance, USB3 noise, dongle |
| Tap fails | NFC position/power | alignment, wallet stacks |
| “Wireless printer” mystery | BT vs Wi‑Fi path | which radio is in use |

## Common traps / interview gotchas

- Bluetooth ≠ Wi‑Fi; different standards and security models.
- NFC range myth: “secure because short” helps but isn’t a full threat model.
- BLE beacons don’t replace [[Access Points]] for data networking.
- 2.4 GHz coexistence is real — capacity planning still starts with [[Channel-Planning]].

## Mastery checklist

- [ ] Place BT/NFC under [[PAN]], not campus WLAN
- [ ] Contrast range and purpose
- [ ] Name one Wi‑Fi interaction (2.4 coexistence)
- [ ] Explain NFC often *triggers* another link

## Related notes

- [[PAN]] · [[WLAN]] · [[Access Points]] · [[Hotspot-and-Tethering]] · [[Zigbee-Z-Wave]] · [[WiFi-Standards]]
- ← [[01-Wireless-Technologies/Index|Wireless Technologies]] · [[07-Wireless-Networking/Index|Wireless Networking]]
