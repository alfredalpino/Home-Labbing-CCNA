---
tags: [network-devices, networking, ccna, access-point, wifi]
aliases: [Access Point, Wireless AP, AP, WAP]
layer: Data Link + RF
---

# Access Points

## Learning objectives

- Define an AP as the bridge between wireless clients and wired LAN
- Contrast autonomous AP vs controller-based designs
- Relate APs to [[WLAN]], SSIDs, VLANs, and PoE switches
- Troubleshoot association vs IP problems separately

## One-sentence definition

> An **access point (AP)** is a device that allows wireless clients to join a [[WLAN]] and bridges their traffic onto a wired Ethernet [[LAN]] (usually toward a [[Switches|switch]]).

## Analogy

> An AP is a **radio taxi stand beside a highway on‑ramp**. Phones arrive over the air (radio taxis), hop onto the paved road (Ethernet), and join city traffic ([[Switches]] / [[Routers]]). The stand doesn’t replace the highway interchange (router); it only gets wireless riders onto the streets.

## Why it matters

Coverage, capacity, roaming, and SSID-to-VLAN mapping live at the AP edge. Most “Wi‑Fi is broken” tickets start with: associated? authenticated? DHCP? gateway?

## Deep dive

### Mental model

```text
Client ))) AP === switch === router === WAN
        RF     PoE Ethernet
```

### Modes & designs

| Design | Idea |
|--------|------|
| Autonomous AP | Each AP configured locally |
| Controller / lightweight | Central brains; APs as radios |
| Mesh | APs wireless backhaul to root |
| SOHO gateway AP | Built into home router box |

### SSID → VLAN

Corporate APs often map Corporate SSID → VLAN 10, Guest → VLAN 20, with trunk to upstream switch.

### On the wire

Wired side: Ethernet frames, often 802.1Q tagged. Air side: 802.11. Bridging hides most RF pain from tcpdump on Ethernet.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Air interface | L1–L2 | 802.11 |
| Toward LAN | L2 bridge | Into Ethernet switching |

## Lab exercises

### Lab 1 — Find your AP path

On phone Wi‑Fi details, note BSSID (AP radio MAC) vs SSID (network name).

### Lab 2 — Isolation test

On guest Wi‑Fi, try to reach another guest device — many APs isolate clients (expected).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Can’t see SSID | AP down / WLAN disabled / band | AP power, radio status |
| Associated, no IP | VLAN/DHCP | SSID VLAN, helper, scope |
| Roam voice drops | Coverage / sticky client | site survey, power, channels |
| Slow with good bars | Airtime / interference / duplex backhaul | channel util, switch errors |

## Common traps / interview gotchas

- Extender/repeater ≠ full AP design — often halves airtime.
- Signal bars ≠ capacity.
- AP is not a router unless it also routes (many home gateways do both).

## Mastery checklist

- [ ] Taxi-stand analogy
- [ ] Draw client → AP → switch → router
- [ ] Separate association vs DHCP failures
- [ ] Explain SSID-to-VLAN mapping

## Related notes

- [[WLAN]] · [[Switches]] · [[Routers]] · [[LAN]] · [[MAC Address]] · [[DHCP]] · [[Transmission Media Types]]
- ← [[02-Network-Devices/Index|Network Devices]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
