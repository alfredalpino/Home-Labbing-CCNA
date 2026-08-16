---
tags: [switching, networking, ccna, etherchannel, lacp, link-aggregation]
aliases: [EtherChannel, LACP, Link Aggregation, Port-Channel, LAG]
layer: Data Link (Layer 2) / optional L3
---

# Link-Aggregation

## Learning objectives

- Define link aggregation as bundling multiple physical links into one logical link
- Configure Cisco EtherChannel with LACP and verify the port-channel
- Explain load-balancing hash (not per-packet round-robin by default)
- Avoid common mismatches that keep bundles from forming

## One-sentence definition

> **Link aggregation** (EtherChannel / LAG) combines multiple physical Ethernet links into one **logical** port-channel for higher bandwidth and redundancy — appearing as a single link to [[STP]] and to the MAC table.

## Analogy

> Instead of one **highway lane** between cities, you open **four lanes that count as one road** on the map. Spanning Tree sees one road (won’t block three as “redundant loops”). Cars (flows) are assigned lanes by a **hash of the license plate** (MACs/IPs/ports) — one conversation usually sticks to one lane, so a single fat elephant flow won’t stripe across all four.

## Why it matters

Uplinks between access and distribution rarely stay single-homed. Bundles multiply capacity and survive a single cable failure without waiting for STP reconvergence the same way. Misconfigured EtherChannel = flapping and loops.

## Deep dive

### Mental model

```text
SW1 Gi1/0/1 ──┐
SW1 Gi1/0/2 ──┼── Po1  ←→  Po1 ──┼── SW2 Gi1/0/1
SW1 Gi1/0/3 ──┘                  └── SW2 Gi1/0/2

STP / MAC table see Po1 as one interface
```

### Mechanism

| Mode | Protocol | Notes |
|------|----------|-------|
| LACP active/passive | 802.1AX (LACP) | Preferred standards-based |
| PAgP auto/desirable | Cisco proprietary | Legacy labs |
| On / static | No negotiation | Dangerous if other side disagrees |

**Must match across members:** speed/duplex, VLAN mode (access/trunk), allowed VLANs, native VLAN, MTU, etc.

**Load balance:** hash of src/dst MAC, IP, or L4 ports — **per-flow**, not perfect packet spray. Elephant flows can fill one member.

### On the wire

LACP uses Slow Protocol multicast `01:80:C2:00:00:02` (LACPDUs). Data frames still normal Ethernet on each member; logical membership is control-plane.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| L2 EtherChannel | Data Link | One logical L2 uplink |
| L3 EtherChannel | Network | Routed port-channel (no switchport) |
| With STP | L2 topology | Bundle = single edge in the tree |

## Lab exercises

### Lab 1 — LACP bundle (GNS3 / real switches)

```ios
interface range Gi0/1 - 2
 channel-protocol lacp
 channel-group 1 mode active
 switchport mode trunk
interface Port-channel1
 switchport mode trunk
```

Mirror with `mode active` or `passive` on peer. Verify: `show etherchannel summary`, `show lacp neighbor`.

### Lab 2 — Fail a member

Generate traffic; shut one physical member; confirm port-channel stays up and flows continue. Check `show etherchannel port-channel` load numbers.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Bundle not forming | Mode mismatch / VLAN mismatch | `show etherchannel summary`, trunks |
| Err-disable / flaps | One side `on`, other LACP | standardize on LACP |
| Uneven use | Hash + elephant flow | change load-balance algorithm |
| STP blocking members | Channel failed → individual links | fix Po first |

## Common traps / interview gotchas

- EtherChannel does **not** guarantee N× speed for one TCP flow.
- Mixing `mode on` with LACP is a classic loop recipe.
- Always configure the **Port-channel** interface settings consistently (some IOS inherit from members — know your platform).
- Cross-stack / vPC / MLAG variants exist — idea is multi-chassis aggregation (awareness).

## Mastery checklist

- [ ] Build LACP EtherChannel and verify summary
- [ ] List parameters that must match
- [ ] Explain per-flow hashing vs total bandwidth
- [ ] Describe how STP sees a port-channel

## Related notes

- [[STP]] · [[VLANs]] · [[Switches]] · [[MAC-Address-Tables]] · [[Bandwidth]] · [[LAN]]
- ← [[05-Switching/Index|Switching]] · [[04-Building-a-Network/Index|Building a Network]]
