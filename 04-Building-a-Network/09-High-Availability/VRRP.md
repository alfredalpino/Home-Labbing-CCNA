---
tags: [high-availability, networking, ccna, vrrp, fhrp]
aliases: [VRRP, Virtual Router Redundancy Protocol]
layer: Gateway redundancy (FHRP)
---

# VRRP

## Learning objectives

- Define VRRP as the open FHRP analog to [[HSRP]]
- Explain Master/Backup roles and virtual router ID
- Note that the virtual IP may be owned by a real interface (address owner)
- Compare multi-vendor use vs Cisco-only HSRP

## One-sentence definition

> **VRRP** (Virtual Router Redundancy Protocol) is an open standard that elects a **Master** router to own a virtual gateway IP for a LAN, with **Backup** routers ready to assume forwarding when the Master fails.

## Analogy

> If [[HSRP]] is a **branded restaurant chain** hostess system, VRRP is the **industry-standard podium protocol** any restaurant brand can implement. Guests still see one podium number (VIP). The Master chef runs the pass; Backups keep their knives sharp and listen for the heartbeat. When Master walks out, Backup puts on the same podium face so diners don’t renumber their map apps.

## Why it matters

Multi-vendor campuses and many firewalls/routers speak VRRP. CCNA compares it to HSRP so you don’t memorize one vendor’s nouns only.

## Deep dive

### Mental model

```text
Hosts → Virtual Router (VRID + VIP)
          ├─ Master  (forwards)
          └─ Backup(s)
```

### Mechanism

1. Configure VRID and VIP on participating routers.
2. Priority elects Master (100 default typical; address owner = 255 concept).
3. Advertisements notify backups; timeouts trigger takeover.
4. Hosts ARP for VIP; Master answers with virtual MAC derived from VRID.

### HSRP vs VRRP (awareness)

| Topic | HSRP | VRRP |
|-------|------|------|
| Standard | Cisco | IETF |
| Roles | Active/Standby | Master/Backup |
| VIP as real IP | Avoid generally | Allowed as “address owner” |

### On the wire

Multicast advertisements to the VRRP group address. Failover visible as short silence then continued traffic to same VIP — confirm with [[Packet-Analysis]] / `show` commands on gear.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network gateway | First-hop redundancy |
| OSI | 3 (+ L2 vMAC) | Virtual router |

## Lab exercises

### Lab 1 — Noun translation

Make a two-column cheat: HSRP Active≡VRRP Master, Standby≡Backup. Add VIP/VRID notes.

### Lab 2 — Owner IP caution

Explain why making the VIP a physical interface IP (owner) changes failure behavior — write three bullets.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Dual Master | L2 broken / ACL | hellos allowed, VLAN continuity |
| Wrong Master | Priority/preempt | config consistency |
| Hosts blackhole | VIP mismatch | DHCP gateway, VRID |
| Slow cutover | Timers | advert interval vs app SLA |

## Common traps / interview gotchas

- VRRP ≠ load balancer; it’s gateway HA (pair with [[Load-Balancer]] for servers).
- VRID must match on members; VIP subnet must match the LAN.
- Preemption behavior differs by config — don’t assume.
- [[GLBP]] is the Cisco load-sharing FHRP cousin; VRRP needs multiple groups for simple L3 load share.

## Mastery checklist

- [ ] Define Master/Backup/VIP/VRID
- [ ] Say “open standard” vs [[HSRP]]
- [ ] Explain host ARP still points at VIP
- [ ] Tie timer choice to [[Failover]]

## Related notes

- [[HSRP]] · [[GLBP]] · [[Failover]] · [[Routers]] · [[ARP]] · [[Load-Balancer]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
