---
tags: [switching, networking, ccna, mac-table, cam]
aliases: [MAC Address Table, CAM Table, MAC Table, Switching Table]
layer: Data Link (Layer 2)
---

# MAC-Address-Tables

## Learning objectives

- Explain how switches learn source MACs and forward on destination MACs
- Distinguish forward / filter / flood behavior
- Use `show mac address-table` and aging timers in labs
- Relate CAM exhaustion and unknown unicast flooding to security/ops

## One-sentence definition

> The **MAC address table** (CAM table) maps **destination MAC → outgoing port/VLAN** so a switch can forward frames selectively instead of behaving like a hub.

## Analogy

> The MAC table is the switch’s **rolodex of who lives on which hallway**. When mail arrives, the clerk looks up the name (dst MAC): known → walk it to that hallway; unknown → shout into every hallway in that badge zone ([[VLANs|VLAN]]); if sender’s name is new, pencil them into the rolodex (source learning). Old pencil marks fade (aging).

## Why it matters

Every L2 forward decision hits this table. Wrong VLAN, sticky MAC, flapping ports, and CAM overflows (“MAC flooding” attacks or bugs) show up as floods, drops, or security alerts. Pair with [[Switches]] fundamentals.

## Deep dive

### Mental model

```text
Frame in on Gi1/0/5, VLAN 10, src=AAAA, dst=BBBB
  1) Learn: AAAA → Gi1/0/5 (VLAN 10)
  2) Lookup BBBB in VLAN 10
       ├ hit → out that port (forward)  [filter if same port]
       └ miss / broadcast → flood all ports in VLAN 10 except ingress
```

### Mechanism

| Topic | Detail |
|-------|--------|
| Learning | Source MAC + ingress port + VLAN |
| Aging | Default often 300s idle — then relearn |
| Static / sticky | Admin or port-security installed entries |
| Flooding | Unknown unicast, broadcast, (some) multicast |
| ASICs | Hardware CAM; control plane sees via IOS |

**Port security** can limit MACs per port and violate (shutdown/restrict/protect) — related operational control of the table.

### On the wire

No “MAC table protocol.” Learning is passive from frames. Control protocols (STP, LACP) have their own MACs but don’t replace unicast learning.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | Data Link | L2 forwarding database |
| vs ARP | ARP = IP↔MAC on hosts/routers | MAC table = MAC↔port on switches |
| vs Routing table | L3 prefix→next hop | Different layer |

## Lab exercises

### Lab 1 — Watch learning (Cisco + Linux)

```ios
show mac address-table
clear mac address-table dynamic
```

From a PC, ping a neighbor; re-check table for both MACs. Unplug PC; wait/age or clear; confirm entry leaves.

```bash
ip link show
# note MAC; compare to switch table
```

### Lab 2 — Unknown unicast flood

With empty table (cleared), send a frame to a nonexistent MAC (crafted packet or ARP for unused IP carefully). Observe flood on a span/monitor port in the same VLAN — contrast after learning.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Flapping MAC | Loop / VM move / duplicate MAC | `show mac address-table` moves, STP |
| Excessive flooding | Empty/overflow CAM / asymmetric path | utilization, port security, SPAN |
| Host unreachable L2 | Wrong VLAN / sticky stale | VLAN, static MAC clear |
| One-way traffic | Unidirectional fiber / learning one side | both directions, cables |

## Common traps / interview gotchas

- Switches learn from **source** MAC, forward by **destination** MAC.
- MAC table is **per VLAN** (same MAC on two VLANs is different context).
- Clearing the table causes temporary flooding — expected.
- CAM exhaustion ≈ switch floods like a hub until recovered — security implication.

## Mastery checklist

- [ ] Narrate learn → lookup → forward/flood
- [ ] Read and clear dynamic MAC table in IOS
- [ ] Contrast MAC table vs ARP table
- [ ] Explain aging and unknown unicast flood

## Related notes

- [[Switches]] · [[MAC Address]] · [[VLANs]] · [[STP]] · [[ARP]] · [[Frame]] · [[LAN]]
- ← [[05-Switching/Index|Switching]] · [[04-Building-a-Network/Index|Building a Network]]
