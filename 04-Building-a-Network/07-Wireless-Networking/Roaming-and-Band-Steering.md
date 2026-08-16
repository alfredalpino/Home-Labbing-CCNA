---
tags: [wireless, networking, ccna, wifi, roaming]
aliases: [Wi-Fi Roaming, Band Steering, Sticky Client]
layer: Client mobility / RF policy
---

# Roaming & Band Steering

## Learning objectives

- Define roaming as changing [[Access Points]] (or BSSID) while keeping network session intent
- Explain sticky clients and why “strong signal” can still be the wrong AP
- Describe band steering as nudging dual‑band clients toward 5/6 GHz
- Separate L2 roam success from app drops (DHCP, auth, [[VPN]])

## One-sentence definition

> **Roaming** is a client moving its association from one AP/BSSID to another as it walks; **band steering** is the network’s polite shove that prefers higher‑capacity bands (usually 5/6 GHz) when the client can use them.

## Analogy

> Roaming is **changing subway cars without leaving the train line** — you want the doors to open at the next car before the old one leaves the station. Sticky clients are passengers who **won’t leave an almost-empty car** even though the crowded express car (5 GHz AP next door) is better. Band steering is the conductor saying, “Sir, the express is boarding — please move.”

## Why it matters

Voice/video tickets scream “Wi‑Fi drops when I walk.” Root cause is often roam timing, missing overlap ([[AP-Placement-and-Coverage]]), or 802.1X/OKC/FT gaps — not the Internet [[VPN]] concentrator.

## Deep dive

### Mental model

```text
Walk → RSSI(AP1) falls, RSSI(AP2) rises
Client decides (or is steered) → reassociate AP2
Fast roam: key caching / 802.11r / OKC reduces full reauth time
Slow roam: full 802.1X again → gaps → Zoom dies
```

### Mechanism — roaming

1. Client scans (active/passive) for candidate BSSIDs on the same SSID.
2. Decision algorithm (vendor/OS secret sauce) picks a target.
3. Auth/assoc (and maybe 802.1X) complete on the new AP.
4. Ideally same IP/VLAN; DHCP renew should not be required mid-walk.

### Mechanism — band steering

1. AP/controller sees dual‑band client probe/assoc on 2.4 GHz.
2. Policy delays/ignores 2.4 or responds preferentially on 5/6.
3. Client lands on cleaner band → better capacity for the [[WLAN]] cell.

### On the wire / air

Roams show as 802.11 auth/assoc/reassoc and maybe EAP. Wired captures may only show a brief pause or a new AP MAC as the client’s upstream. [[VPN]] tunnels hate multi‑second gaps.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access (+ auth) | Association change under IP |
| OSI | 2 (+ security) | 802.11 roam; 802.1X may involve higher layers |

## Lab exercises

### Lab 1 — Sticky client walk

Connect on 2.4 if possible, walk away slowly while watching which BSSID you stay on (analyzer app). Note when you finally jump.

### Lab 2 — Band check after connect

Connect to a dual‑band SSID; confirm whether you landed on 2.4 or 5/6. Toggle band steering if your lab gear exposes it; reconnect and compare.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Drop every doorway | Coverage hole / late roam | overlap, power, roam thresholds |
| Sticky to far AP | Client algorithm / high power | lower far AP power, min RSSI |
| Auth delay on roam | Full 802.1X each time | FT/OKC, RADIUS latency |
| Steering fails | Legacy client / blacklists | client capabilities, SSID design |

## Common traps / interview gotchas

- Same SSID ≠ seamless roam; security mode and key caching matter.
- Band steering is a *hint*, not a law — stubborn clients exist.
- Layer‑3 roam (different subnet) breaks sessions unless mobility/anchoring exists.
- “Roaming issue” can be DHCP/VLAN mismatch between APs — IP layer, not RF.

## Mastery checklist

- [ ] Define roam vs sticky client
- [ ] Explain why overlap enables roaming
- [ ] Describe band steering goal (capacity)
- [ ] Name one fast-roam idea (FT/OKC) at awareness level

## Related notes

- [[WLAN]] · [[Access Points]] · [[Access-Points-Controllers]] · [[AP-Placement-and-Coverage]] · [[Wireless-Security]] · [[VPN]] · [[DHCP]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
