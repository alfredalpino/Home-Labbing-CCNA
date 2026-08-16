---
tags: [switching, networking, ccna, vlan]
aliases: [VLAN, Virtual LAN, VLANs]
layer: Data Link (Layer 2)
---

# VLANs

## Learning objectives

- Define a VLAN as a logical broadcast domain on shared switch hardware
- Configure access ports, trunks (802.1Q), and SVIs for inter-VLAN routing
- Explain native VLAN, allowed VLAN lists, and DTP risks
- Troubleshoot “same switch, can’t ping” VLAN mismatches

## One-sentence definition

> A **VLAN** (Virtual LAN) carves one physical switch fabric into **multiple isolated Layer-2 broadcast domains**, each with its own flooding/ARP scope — like multiple logical [[LAN]]s on shared gear.

## Analogy

> A switch without VLANs is one **open-plan office**: everyone hears every shout ([[ARP]], broadcasts). VLANs are **colored badge zones** painted on the same floor: red badges only hear red; blue only blue. Trunks are **multicolor elevators** between floors carrying badge colors in a tag. To talk across colors you need a **translator at the stairs** (router / L3 SVI) — that’s inter-VLAN routing.

## Why it matters

Security segmentation, smaller broadcast domains, and almost every campus design start with VLANs. Mis-tagged trunks and native VLAN mismatches are classic outages and interview traps.

## Deep dive

### Mental model

```text
Access port: one VLAN untagged (PC ↔ switch)
Trunk port:  many VLANs tagged 802.1Q (switch ↔ switch / AP / firewall)

[PC VLAN10]──[SW]══trunk══[SW]──[PC VLAN10]   same L2 domain
[PC VLAN20]──[SW]── SVI/router ──[PC VLAN10]  needs L3
```

### Mechanism

| Topic | Detail |
|-------|--------|
| VLAN ID | 1–4094 (normal 1–1005 on older; extended common now) |
| Access | Untagged; `switchport mode access` + `access vlan N` |
| Trunk | 802.1Q tags; `switchport mode trunk` |
| Native VLAN | Untagged on trunk; **must match both ends** |
| SVI | `interface vlan N` — L3 gateway for that VLAN |
| Router-on-a-stick | Subinterfaces `.10`, `.20` with `encapsulation dot1Q` |

**DTP:** Dynamic Trunking Protocol can negotiate trunks — often disabled for security (`nonegotiate` + static mode).

### On the wire

802.1Q inserts a **4-byte tag** (TPID `0x8100` + PCP/DEI + VLAN ID) between SA MAC and EtherType. Untagged native VLAN frames look like plain Ethernet.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | Data Link (L2) | Broadcast domain boundary |
| L3 | Inter-VLAN routing | SVIs / ROAS / firewall |
| Contrast | [[VRFs]] | L3 table separation vs L2 VLAN |

## Lab exercises

### Lab 1 — Two VLANs + trunk (GNS3 / CML / Packet Tracer)

Two switches, PCs in VLAN 10 and 20. Access ports + trunk between switches. Confirm same-VLAN ping works; cross-VLAN fails until L3.

```ios
vlan 10
vlan 20
interface Gi0/1
 switchport mode access
 switchport access vlan 10
interface Gi0/24
 switchport mode trunk
 switchport nonegotiate
```

### Lab 2 — Inter-VLAN via SVI

On L3 switch: `ip routing`, create `interface vlan 10` / `vlan 20` with gateways; set PC default gateways. Ping across VLANs; capture to see no tag on access, tags on trunk.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| No ping same VLAN | Access VLAN mismatch / down | `show vlan brief`, port mode |
| Trunk brings one VLAN only | Allowed list / pruning | `show interfaces trunk` |
| Odd native behavior | Native VLAN mismatch | Both ends native ID |
| Cross-VLAN fail | No SVI/router / ACL | `ip routing`, SVI up, GW |

## Common traps / interview gotchas

- VLAN ≠ subnet by law — but best practice is **1:1 VLAN↔subnet**.
- VLAN 1 default is often left unused for user data (security hygiene).
- Native VLAN mismatch can cause leaks/CDP weirdness — match and avoid VLAN 1 as native in hardened designs.
- Wireless SSIDs usually map to VLANs on the wired side.

## Mastery checklist

- [ ] Configure access + trunk and verify with `show interfaces trunk`
- [ ] Explain 802.1Q tag and native VLAN
- [ ] Build inter-VLAN routing (SVI or ROAS)
- [ ] Contrast VLAN (L2) with VRF (L3)

## Related notes

- [[Switches]] · [[MAC-Address-Tables]] · [[STP]] · [[Link-Aggregation]] · [[VXLAN]] · [[Default-Gateway]] · [[LAN]] · [[Frame]]
- ← [[05-Switching/Index|Switching]] · [[04-Building-a-Network/Index|Building a Network]]
