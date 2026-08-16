---
tags: [high-availability, networking, ccna, hsrp, fhrp, cisco]
aliases: [HSRP, Hot Standby Router Protocol]
layer: Gateway redundancy (FHRP)
---

# HSRP

## Learning objectives

- Define HSRP as Cisco’s FHRP presenting one virtual gateway IP/MAC
- Explain Active/Standby roles and hello-based failover
- Contrast HSRP with [[VRRP]] and [[GLBP]]
- Tune awareness of timers vs [[Failover]] and spanning events

## One-sentence definition

> **HSRP** (Hot Standby Router Protocol) lets two or more Cisco routers share a **virtual IP and MAC** as the LAN default gateway — one **Active** forwards, others **Standby** ready to take over if the Active fails.

## Analogy

> HSRP is a **restaurant with one hostess podium (virtual IP)** and two managers’ name tags. Only the **Active** manager greets guests (forwards packets). The **Standby** watches the radio check-ins (hellos). If the Active disappears, the Standby steps to the podium wearing the *same* hostess smile (virtual MAC) so diners ([[Host]]s) don’t rewrite their GPS (default gateway).

## Why it matters

First-hop failure takes down “the Internet” for a VLAN even when WAN links are fine. CCNA expects HSRP roles, virtual IP, and basic priority/preempt ideas.

## Deep dive

### Mental model

```text
Hosts → VIP/vMAC (gateway)
          ├─ Router A Active  ── upstream
          └─ Router B Standby ── upstream
Hellos between A/B on LAN; failover promotes Standby
```

### Mechanism

1. Group configured with virtual IP on a subnet.
2. Priority elects Active (preempt optional).
3. Active sends hellos; Standby monitors.
4. Active loss → Standby becomes Active, owns VIP/vMAC.
5. Hosts keep ARP’d virtual MAC — session blip depends on timers.

### On the wire

Multicast hellos (Cisco HSRP addresses historically well-known). Data plane uses virtual MAC as destination from hosts. [[Packet-Analysis]] during failover shows brief loss then recovery — not a new gateway IP.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network (gateway) | First-hop IP redundancy |
| OSI | 3 (+ L2 vMAC) | Virtual IP/MAC pair |

## Lab exercises

### Lab 1 — Role sketch

Draw two routers, VIP `.1`, hosts using `.1`. Label Active/Standby and what ARP shows for `.1`.

### Lab 2 — Failover thought timer

If hello/hold timers are long, predict user symptom during Active pull. Relate to [[Failover]] SLAs and voice apps.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Two Actives | Layer-2 partition | trunks, VLANs, hellos |
| Never fails over | Tracking/priority | interface track, preempt |
| Hosts wrong gateway | VIP not configured on hosts | DHCP gateway option |
| Flapping Active | Unstable tracked link | dampen, track correctly |

## Common traps / interview gotchas

- HSRP is Cisco-proprietary; [[VRRP]] is standards-based cousin.
- Virtual IP must be unused by a physical interface as primary (design carefully).
- HSRP doesn’t load-share per flow by itself (see [[GLBP]] / multiple groups).
- Faster timers ≠ always better on busy/lossy links.

## Mastery checklist

- [ ] Define Active/Standby/VIP
- [ ] Explain why hosts don’t change gateway IP
- [ ] Contrast with [[VRRP]] / [[GLBP]]
- [ ] Name a split-brain cause (L2 break)

## Related notes

- [[VRRP]] · [[GLBP]] · [[Failover]] · [[Routers]] · [[ARP]] · [[Load-Balancer]] · [[Packet-Analysis]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
