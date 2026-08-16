---
tags: [wireless, networking, ccna, wifi, security, wpa, wps]
aliases: [WPA vs WPS, WPS, WPA Comparison]
layer: Security mechanisms
---

# WPA vs WPS

## Learning objectives

- Separate **WPA/WPA2/WPA3** (security protocols) from **WPS** (setup convenience feature)
- Explain why WPS PIN mode is widely considered unsafe
- Know when WPA3-Personal/Enterprise changes the story vs WPA2
- Give clear advice: use WPA2/WPA3; disable WPS on production APs

## One-sentence definition

> **WPA** (Wi‑Fi Protected Access) is the family of standards that authenticate and encrypt a [[WLAN]]; **WPS** (Wi‑Fi Protected Setup) is a push‑button/PIN convenience feature to join that WLAN — and the PIN method historically cracked the door open.

## Analogy

> **WPA** is the **deadbolt and alarm system** on the house ([[Wireless-Security]]). **WPS** is the **“press here for the pizza guy” gate remote** — handy, but the PIN version was like a lock with only 10,000 combinations that told you when you got half right. You can have a great deadbolt (WPA2/WPA3) and still lose if you leave the pizza remote enabled.

## Why it matters

Users confuse “WPS button” with “WPA security.” Interviewers and home-lab hardening both love this distinction. Link it to [[Access Points]] defaults that ship insecure.

## Deep dive

### Mental model

```text
WPA2/WPA3  → how you prove identity + encrypt air traffic
WPS        → shortcut to provision PSK credentials onto a client
             (PBC = button; PIN = numeric — avoid PIN)
```

### WPA family (awareness)

| Version | Era | Notes |
|---------|-----|-------|
| WPA | Post-WEP stopgap | TKIP — legacy |
| WPA2 | Long baseline | AES-CCMP; PSK or Enterprise |
| WPA3 | Modern | SAE (personal), stronger enterprise; PMF |

### WPS mechanisms

| Method | Idea | Risk |
|--------|------|------|
| PBC | Push button on AP + client | Physical access window |
| PIN | 8-digit PIN | Offline/online attacks; disable |
| NFC/USB | Rare in enterprise | Physical provisioning |

### On the wire / air

WPS exchanges happen during enrollment; afterward the client uses normal WPA keys. Attacks historically targeted the WPS registrar PIN space — not the full WPA PSK brute force directly.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | Join/encryption of [[WLAN]] |
| OSI | 2 (+ management) | 802.11 security / provisioning |

## Lab exercises

### Lab 1 — Find WPS on your AP

Log into a home lab AP/router. Locate WPS settings. Note if enabled by default. Disable WPS for hardening practice.

### Lab 2 — Security mode label check

Confirm the SSID uses WPA2-Personal, WPA3-Personal, or mixed. Prefer WPA3 or WPA2/WPA3 transition deliberately — document client compatibility.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Client can’t use WPS join | WPS disabled (good!) | use passphrase / 802.1X |
| “Secure” home Wi‑Fi owned | WPS PIN left on | disable WPS, rotate PSK |
| Mixed WPA2/WPA3 weirdness | Transition mode bugs | client drivers, force mode in lab |
| Enterprise join ≠ WPS | Wrong mental model | 802.1X, not push-button |

## Common traps / interview gotchas

- WPS ≠ WPA; one is setup, one is the security protocol family.
- Disabling WPS does not weaken WPA; it removes a provisioning attack surface.
- WPA3-Personal (SAE) resists offline PSK dictionary attacks better than WPA2-PSK — still use a strong passphrase.
- Corporate networks should use Enterprise ([[Wireless-Security]]), not WPS.

## Mastery checklist

- [ ] Define WPA vs WPS without mixing them
- [ ] Recommend disabling WPS PIN
- [ ] Place WPA2/WPA3 as the real lock
- [ ] Point to [[Wireless-Security]] for 802.1X depth

## Related notes

- [[Wireless-Security]] · [[WLAN]] · [[Access Points]] · [[VPN]] · [[WiFi-Standards]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
