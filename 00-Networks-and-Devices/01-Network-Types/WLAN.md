---
tags: [network-types, networking, ccna, wlan, wifi]
aliases: [Wireless LAN, Wi-Fi, WLAN]
layer: Scope / access technology
---

# WLAN

## Learning objectives

- Define WLAN as a LAN using wireless media
- Relate SSIDs, APs, controllers, and wired upstream switches
- Explain why wireless feels “slower/less reliable” than copper
- Troubleshoot at RF vs IP layers deliberately

## One-sentence definition

> A **WLAN** (Wireless Local Area Network) is a [[LAN]] that uses radio (typically Wi‑Fi / IEEE 802.11) instead of — or in addition to — cables to connect clients, usually via [[Access Points]].

## Analogy

> Wired LAN is a **private driveway into your garage**. WLAN is a **shared parking lot with a radio attendant ([[Access Points]])**. Everyone’s cars (frames) share the lot’s airtime; if the lot is crowded or noisy (interference), everyone waits — even if the highway beyond ([[WAN]]) is empty.

## Why it matters

Most user devices are wireless-first. CCNA wireless topics and real tickets blend RF (signal, channel, retries) with normal IP ([[DHCP]], [[DNS]], gateway). Mis-blaming “the firewall” for Wi‑Fi congestion wastes hours.

## Deep dive

### Mental model

```text
Phone  )))  Access Point  ── Ethernet ── Switch ── Router ── Internet
         RF                    wired LAN fabric
```

### Key ideas

| Concept | Meaning |
|---------|---------|
| SSID | Network name clients join |
| AP | Radio bridge to wired LAN ([[Access Points]]) |
| Association | Client ↔ AP relationship |
| Shared medium | Half-duplex airtime contention |
| Roaming | Move between APs hoping session survives |

WLAN still ends up as Ethernet frames on the wire after the AP. Security (WPA3/enterprise) is critical because RF leaks past walls.

### On the wire / air

802.11 frames ≠ Ethernet frames on the air; APs bridge/translate into Ethernet toward the switch. Captures on the wired side won’t show RF retries.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access | Wireless LAN technology |
| OSI | 1–2 | RF + MAC |

## Lab exercises

### Lab 1 — Separate Wi‑Fi vs path

```bash
ping -c 20 $(route -n get default | awk '/gateway:/ {print $2}')
# Compare on Wi‑Fi vs Ethernet if available
```

### Lab 2 — SSID inventory

List SSIDs around you; note 2.4 vs 5/6 GHz tradeoffs (range vs capacity).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| High latency local only on Wi‑Fi | RF / airtime | RSSI, channel util, interference |
| Connected, no IP | DHCP | VLAN on AP/SSID, helper |
| Roaming drops | Sticky client / coverage holes | AP placement, power, band steering |

## Common traps / interview gotchas

- Wi‑Fi bandwidth is shared and optimistic (PHY rate ≠ TCP [[Throughput]]).
- “Weak Wi‑Fi” can still pass ping while destroying Zoom (jitter/loss).
- Guest Wi‑Fi often uses client isolation — looks like “LAN broken.”

## Mastery checklist

- [ ] Define WLAN as wireless LAN, not “the Internet”
- [ ] Draw phone → AP → switch → router
- [ ] Explain shared airtime analogy
- [ ] Name two RF vs two IP failure checks

## Related notes

- [[LAN]] · [[Access Points]] · [[Switches]] · [[Transmission Media Types]] · [[Latency]] · [[Throughput]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
