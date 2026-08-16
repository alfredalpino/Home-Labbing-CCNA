---
tags: [wireless, networking, ccna, lorawan, satellite, iot, wan]
aliases: [LoRaWAN, Satellite Networking, LoRa]
layer: LPWAN / space underlay
---

# LoRaWAN & Satellite

## Learning objectives

- Define LoRaWAN as LPWAN for tiny, infrequent IoT messages
- Place satellite links as high‑latency [[WAN]] underlays (GEO vs LEO awareness)
- Contrast both with campus [[WLAN]] and cellular broadband
- Know engineering implications: duty cycle, latency, MTU, [[VPN]] pain

## One-sentence definition

> **LoRaWAN** is a long‑range, low‑power wide‑area network for small sensor uplinks to gateways/network servers; **satellite networking** uses space segment relays so sites or IoT devices reach Earth networks when terrestrial fiber/cellular isn’t practical — both trade bitrate and latency for reach.

## Analogy

> Campus Wi‑Fi is **passing notes in class** (fast, short distance via [[Access Points]]). Cellular is **courier bike across the city**. LoRaWAN is **carrier pigeon with a postcard** — miles of range, tiny message, hours/days of battery. Satellite is **airmail overseas**: incredible reach, postage and delay (especially GEO) remind you physics still bills interest. Don’t put a Zoom call on a pigeon.

## Why it matters

Industrial IoT, agriculture, maritime, and backup WANs show up in modern designs. Network engineers must set expectations: LoRaWAN isn’t “long Wi‑Fi,” and satellite [[VPN]]s need MSS clamping and patience.

## Deep dive

### Mental model

```text
LoRaWAN:
 Sensor ))) Gateway ── IP ── Network Server ── App Server

Satellite:
 Site router ── dish ── satellite ── ground station ── Internet / MPLS
 Optional overlay: [[VPN]] / SD-WAN
```

### Comparison

| Trait | LoRaWAN | Satellite broadband |
|-------|---------|---------------------|
| Payload | Bytes–small | Can be general Internet |
| Power | Ultra-low sensors | Powered terminals |
| Latency | Seconds–duty cycle | GEO high; LEO lower |
| Role | Telemetry | WAN underlay / remote Internet |

### Mechanism — LoRaWAN

1. End device uses LoRa PHY chirps on regional ISM bands.
2. Gateways hear and forward to a network server (often Ethernet/cellular backhaul).
3. Join/OTAA keys; adaptive data rate; strict duty cycles in many regions.

### Mechanism — satellite

1. Terminal acquires bird; modem presents Ethernet/IP to router.
2. Traffic traverses space segment + teleport.
3. Enterprise overlays ([[VPN]], SD-WAN) ride on top — tune timers for RTT.

### On the wire

LoRaWAN air frames ≠ Ethernet; you debug IP north of the gateway. Satellite handoff looks like a WAN NIC with unusual latency/loss — `ping` and MSS matter more than RF tools from [[WLAN]] kits.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | WAN / IoT backhaul | IP often starts at gateway/terminal |
| OSI | 1–2 specialty + L3 uplink | Diverse PHYs |

## Lab exercises

### Lab 1 — Latency expectation sheet

Write expected RTT orders of magnitude: LAN, [[WLAN]], cellular, LEO sat, GEO sat. Keep it as a pocket reference.

### Lab 2 — VPN on high RTT (thought lab)

List three [[VPN]]/TCP settings you’d revisit on GEO satellite (keepalive, MSS, maybe UDP transport). Explain why.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Sensors silent | Duty cycle / join keys | logs, gateway backhaul |
| Gateway up, no data | Network server path | IP/[[DNS]], firewall |
| Sat link up, apps stall | Latency/MSS | ping size, TCP window |
| VPN flaps | Dead peer timers | adjust for RTT |

## Common traps / interview gotchas

- LoRaWAN ≠ LoRa (PHY) alone; LoRaWAN is the MAC/network architecture.
- “Long range Wi‑Fi” marketing is usually wrong — different tech.
- GEO satellite RTT breaks naive chatty protocols and some HA hellos — see [[Failover]] timers.
- Starlink-class LEO improves latency vs GEO but still isn’t a data center LAN.

## Mastery checklist

- [ ] Define LoRaWAN use-case in one sentence
- [ ] Contrast GEO vs LEO latency qualitatively
- [ ] Explain gateway/terminal as the IP edge
- [ ] Name one [[VPN]] tuning concern on sat

## Related notes

- [[Mobile-Networks]] · [[WAN]] · [[VPN]] · [[WLAN]] · [[Zigbee-Z-Wave]] · [[Latency]] · [[Throughput]]
- ← [[01-Wireless-Technologies/Index|Wireless Technologies]] · [[07-Wireless-Networking/Index|Wireless Networking]]
