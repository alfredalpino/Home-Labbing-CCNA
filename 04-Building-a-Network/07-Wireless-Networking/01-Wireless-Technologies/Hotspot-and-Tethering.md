---
tags: [wireless, networking, ccna, hotspot, tethering]
aliases: [Mobile Hotspot, Tethering, Personal Hotspot]
layer: NAT / edge sharing
---

# Hotspot & Tethering

## Learning objectives

- Define hotspot/tethering as sharing one uplink (often cellular) to other devices
- Map roles: phone as router/[[Access Points|AP]]/NAT boundary
- Contrast USB/Bluetooth tethering vs Wi‑Fi hotspot
- Spot security and policy issues (corp data over personal hotspot)

## One-sentence definition

> **Tethering / hotspot** turns a device (usually a phone on [[Mobile-Networks]]) into a temporary gateway — sharing its WAN uplink with laptops via Wi‑Fi, USB, or Bluetooth, typically with NAT like a tiny travel router.

## Analogy

> Your phone’s cellular link is a **single garden hose from the city** ([[WAN]]). Hotspot mode attaches a **sprinkler splitter and a mini Wi‑Fi sprinkler head**: nearby devices drink from your hose. USB tethering is a **direct drip line** to one plant; Bluetooth tethering is a **slow eyedropper**. None of that rebuilds the municipal water plant — and your corp [[VPN]] still rides inside the spray.

## Why it matters

Outage workarounds, travel labs, and shadow IT all use hotspots. Engineers must know the NAT boundary, battery/thermal limits, and that “online via hotspot” still needs DNS/VPN troubleshooting.

## Deep dive

### Mental model

```text
Laptop ─Wi‑Fi─ Phone AP/NAT ─Cellular─ Carrier ─ Internet
Laptop ─USB── Phone NAT ─────Cellular─ ...
Laptop ─BT──── Phone NAT ─────Cellular─ ...
Optional: Laptop ── [[VPN]] ── Corp (overlay on hotspot underlay)
```

### Modes

| Mode | Medium | Notes |
|------|--------|-------|
| Wi‑Fi hotspot | 802.11 | Phone acts like SOHO AP |
| USB tethering | USB Ethernet | Stable, often faster, one host |
| Bluetooth PAN | BT | Low throughput fallback |

### Mechanism

1. Phone retains cellular (or sometimes Wi‑Fi) uplink.
2. Local interface hands out RFC1918 addresses ([[DHCP]]-like).
3. NAT/PAT translates to carrier IP (often CGNAT).
4. Clients treat phone as default gateway.

### On the wire

From the laptop, traffic looks like any [[WLAN]] or USB Ethernet LAN. Outer path is carrier IP; captures won’t show LTE air interface. Double NAT appears if you nest hotspot behind another router.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Edge NAT + access | Phone = gateway |
| OSI | 2–3 (+ radio WAN) | Local L2 + IP NAT |

## Lab exercises

### Lab 1 — Trace the hop

Enable phone hotspot; on laptop run `traceroute`/`tracert` to 1.1.1.1. Identify phone hop vs carrier hops.

### Lab 2 — VPN over hotspot

Connect corp or personal [[VPN]] while on hotspot. Note new tunnel adapter and whether split tunneling still reaches local phone services.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Associated, no Internet | Cellular data / APN | bars, airplane, carrier |
| VPN fails | CGNAT / UDP blocked | transport, ports, IKE |
| Slow only on BT tether | BT bandwidth | switch USB/Wi‑Fi |
| Corp policy block | MDM forbids hotspot | compliance, not RF |

## Common traps / interview gotchas

- Hotspot Wi‑Fi security still matters — use WPA2/WPA3; see [[WPA-vs-WPS]].
- You’re sharing *your* quota and exposing devices to a less-controlled LAN.
- Phone hotspot ≠ enterprise [[Access Points]] design (no controller, weak roaming story).
- Some carriers disable tethering or bill it separately.

## Mastery checklist

- [ ] Draw laptop → phone NAT → cellular → Internet
- [ ] Contrast Wi‑Fi / USB / BT tethering
- [ ] Explain CGNAT impact on inbound/VPN
- [ ] Relate to [[Mobile-Networks]] and [[VPN]]

## Related notes

- [[Mobile-Networks]] · [[WLAN]] · [[Access Points]] · [[VPN]] · [[PAN]] · [[Bluetooth-NFC]] · [[DHCP]]
- ← [[01-Wireless-Technologies/Index|Wireless Technologies]] · [[07-Wireless-Networking/Index|Wireless Networking]]
