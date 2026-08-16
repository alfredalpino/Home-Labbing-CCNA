---
tags: [wireless, networking, ccna, cellular, 4g, 5g, mobile]
aliases: [Mobile Networks, Cellular, 4G LTE, 5G]
layer: WAN access / service provider
---

# Mobile Networks

## Learning objectives

- Explain cellular (4G/5G) as a **service-provider radio WAN**, not a campus [[WLAN]]
- Map UE → RAN → core → Internet at a network-engineer awareness level
- Contrast licensed spectrum, handoff, and SIM identity vs Wi‑Fi SSID/PSK
- Know when cellular matters: SD-WAN underlay, out-of-band, hotspots, IoT

## One-sentence definition

> **Mobile networks** (4G LTE / 5G) are carrier-operated radio systems that authenticate subscriber devices (SIM/eSIM) and backhaul IP traffic through a provider core to the Internet or private APNs — a [[WAN]] access method you rent, not an [[Access Points|AP]] you cable in the closet.

## Analogy

> Campus Wi‑Fi is a **private parking garage** you own ([[WLAN]] / [[Access Points]]). Cellular is **city taxi + metro system**: you flash a transit pass (SIM), hop cells (base stations) as you move, and the city’s operations center (packet core) decides how you reach destinations. You can take a taxi to the office ([[VPN]] from phone) but you don’t redesign the metro when your garage AP dies.

## Why it matters

Branches use LTE/5G as SD-WAN underlay; engineers use phone hotspots in outages; private 5G appears in factories. CCNA-level fluency is topology and failure domains — not OFDM math.

## Deep dive

### Mental model

```text
Phone/UE ))) Radio cell (eNB/gNB) ── backhaul ── Carrier core (EPC/5GC)
                                              ├─ Internet
                                              └─ Private APN / NaaS
Optional: UE ── [[VPN]] ── Corp
```

### 4G vs 5G (engineer view)

| Topic | 4G LTE | 5G |
|-------|--------|-----|
| Marketing | Mature broadband WAN | Higher peaks, slicing vision |
| Air | OFDMA family | New NR + often LTE anchor (NSA) |
| Core | EPC | 5GC (SA) or hybrid |
| Campus replace? | No | Private 5G sometimes — still not Wi‑Fi |

### Mechanism

1. UE attaches; SIM authenticates to HSS/UDM.
2. Sessions get IP via PGW/UPF; APN selects route/policy.
3. Mobility: handoff between cells keeps session where designed.
4. Enterprise: breakout, private APN, or overlay [[VPN]]/SASE.

### On the wire / air

On the device you see a cellular interface (rmnet/wwan). On the enterprise edge, a cellular modem looks like a WAN DHCP/PPP client. You won’t see 3GPP air frames on Wireshark of the LAN.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | WAN underlay for IP | Carrier provides L3 reachability |
| OSI | 1–3 in RAN/core | Radio + tunneling inside provider |

## Lab exercises

### Lab 1 — Compare paths

From a phone, note public IP on cellular vs on [[WLAN]]. Traceroute a known host on each path; observe hop count/latency differences.

### Lab 2 — Outage design sketch

Draw branch router with dual underlay: broadband + LTE. Mark which overlay ([[VPN]]/SD-WAN) survives if fiber dies.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Modem up, no apps | APN/auth | APN, SIM, carrier provision |
| High latency VPN | Radio + overlay | underlay RTT, MTU |
| Works on Wi‑Fi only | Policy / DNS | split tunnel, firewall |
| Flaps at site edge | Coverage / band | antenna, signal bars ≠ SNR |

## Common traps / interview gotchas

- Cellular bandwidth is shared and radio-conditioned — marketing Gbps ≠ steady TCP.
- Private 5G ≠ “just enterprise Wi‑Fi with a new sticker.”
- Phone [[Hotspot-and-Tethering]] uses cellular WAN + local Wi‑Fi/USB LAN roles mixed.
- CGNAT is common — inbound connections and some [[VPN]] modes need care.

## Mastery checklist

- [ ] Draw UE → RAN → core → Internet
- [ ] Contrast SIM identity vs Wi‑Fi PSK
- [ ] Place cellular as WAN underlay option
- [ ] Explain when to add [[VPN]] on top

## Related notes

- [[WAN]] · [[VPN]] · [[Hotspot-and-Tethering]] · [[WLAN]] · [[LoRaWAN-Satellite]] · [[Latency]] · [[Throughput]]
- ← [[01-Wireless-Technologies/Index|Wireless Technologies]] · [[07-Wireless-Networking/Index|Wireless Networking]]
