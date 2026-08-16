---
tags: [wireless, networking, ccna, wifi, security]
aliases: [Wi-Fi Security, WLAN Security, 802.11 Security]
layer: Security / access control
---

# Wireless Security

## Learning objectives

- Explain why open Wi‑Fi is a shared-medium confidentiality risk
- Contrast personal (PSK) vs enterprise (802.1X/EAP) authentication
- Place WPA2/WPA3 in the modern baseline; treat WEP as historical poison
- Relate wireless security to [[VPN]], segmentation, and guest isolation

## One-sentence definition

> **Wireless security** authenticates stations and encrypts 802.11 traffic so a [[WLAN]] isn’t a free microphone into your [[LAN]] — because RF ignores cubicle walls and parking lots.

## Analogy

> An open AP is a **party in a glass house** — anyone walking by can watch the dancing ([[Frame]]s) and sometimes join. PSK WPA is a **shared house key** under the mat (convenient, painful to rotate, one leak affects all). Enterprise 802.1X is a **bouncer with a guest list** (RADIUS): each person proves identity, gets their own coat-check ticket (keys), and can be kicked individually. A [[VPN]] on top is a **locked briefcase** you still carry through the party.

## Why it matters

Wireless is the easiest remote edge to attack or misconfigure. CCNA and real ops expect WPA2/WPA3 literacy, guest design, and “evil twin” awareness — not crypto math.

## Deep dive

### Mental model

```text
Client → (auth) → AP/controller → (optional RADIUS) → policy/VLAN
         └───── 802.11 encryption (CCMP/GCMP) on air ─────┘
Guest SSID → isolated VLAN → Internet only
Corp SSID  → corp VLAN → maybe require [[VPN]] for sensitive apps
```

### Mechanism

1. **Authentication**: open, PSK, or 802.1X/EAP (PEAP, EAP-TLS, etc.).
2. **Key hierarchy**: session keys derived so air traffic is encrypted.
3. **Authorization**: VLAN/ACL/role from RADIUS or local policy.
4. **Ongoing**: rogue AP detection, PMF (management frame protection) on modern WPA3.

### Baseline choices

| Mode | Use when | Watch-outs |
|------|----------|------------|
| Open / OWE | Captive portals, some guest | OWE encrypts without auth; still untrusted users |
| WPA2/WPA3-Personal | Home/SMB | PSK rotation, sharing |
| WPA2/WPA3-Enterprise | Corp | RADIUS, certs, roam design |
| WEP / WPA-TKIP | Never for new | Broken / deprecated |

### On the wire / air

Encrypted data frames hide payloads from casual sniffers; management frames historically were weaker (deauth attacks). Captures on the wired side see decrypted/bridged Ethernet after the AP. Evil twins mimic SSIDs — users need validation beyond the name.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access (+ AAA) | Protect LAN entry |
| OSI | 2 (+ 4/7 for EAP/RADIUS) | 802.11 crypto; RADIUS often UDP |

## Lab exercises

### Lab 1 — Inventory SSIDs & security

List nearby SSIDs and security types (Open/WPA2/WPA3). Note any still advertising weak modes.

### Lab 2 — Guest vs corp thought model

Design two SSIDs: Guest (Internet only, client isolation) and Corp (802.1X, internal VLANs). Write which traffic should never mix — include when you’d still force [[VPN]].

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Auth loop / can’t join | PSK mismatch / EAP fail | passphrase, RADIUS, clock ([[NTP]]) |
| Joins, no resources | VLAN/ACL | SSID→VLAN map, isolation |
| OK at desk, fails roaming | Fast roam / reauth | FT/OKC, RADIUS latency |
| “Secure” but phishing SSID | Evil twin | validate portal/cert, user training |

## Common traps / interview gotchas

- Hiding SSID ≠ security; it only slows honest devices.
- MAC filtering is theater at scale.
- WPA3-Personal improves PSK offline-attack resistance — still rotate secrets.
- Corporate [[VPN]] does not fix an open guest SSID bridging into corp VLANs.

## Mastery checklist

- [ ] Contrast PSK vs 802.1X in the bouncer analogy
- [ ] State WEP is obsolete; WPA2/WPA3 baseline
- [ ] Explain guest isolation purpose
- [ ] Relate air encryption to [[VPN]] defense-in-depth

## Related notes

- [[WLAN]] · [[Access Points]] · [[WPA-vs-WPS]] · [[VPN]] · [[SSL-TLS]] · [[Roaming-and-Band-Steering]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
