---
tags: [network-types, networking, ccna, san]
aliases: [Storage Area Network, SAN]
layer: Scope / data-center fabric
---

# SAN

## Learning objectives

- Define SAN as a network purpose-built for block storage traffic
- Contrast SAN vs NAS vs ordinary [[LAN]] file shares
- Recognize FC / iSCSI / NVMe-oF at awareness level
- Know why mixing heavy storage and user LAN is painful

## One-sentence definition

> A **SAN** (Storage Area Network) is a specialized high-speed network that connects servers to shared **block storage**, so disks appear local to the OS while living on centralized arrays.

## Analogy

> A normal [[LAN]] is the office hallway where people chat and carry papers (files). A SAN is the **bank vault pneumatic-tube system**: only storage blocks move, on dedicated pipes, with strict performance and access rules. NAS is more like a **shared filing cabinet in the hallway** (files over Ethernet/IP).

## Why it matters

Virtualization clusters, databases, and boot-from-SAN designs depend on clean storage fabrics. Confusing SAN with “big NAS share” leads to wrong troubleshooting (looking at SMB while the outage is multipathing/zoning).

## Deep dive

### Mental model

```text
Server HBA/iSCSI ══ SAN fabric ══ Storage array LUNs
   (block I/O looks like local disks)
```

### SAN vs NAS vs LAN

| | SAN | NAS | LAN file share |
|--|-----|-----|----------------|
| What you mount | Blocks/LUNs | Filesystems | Files (SMB/NFS) |
| Classic media | Fibre Channel; also iSCSI/NVMe-oF on Ethernet | Ethernet/IP | Ethernet/IP |
| Consumer feel | Invisible “local disk” | `\\fileserver\share` | same family as NAS |

### On the wire

May be Fibre Channel frames (not IP) or IP-based (iSCSI). Either way: low latency, lossless behavior (often PFC on Ethernet storage), multipathing.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Purpose-built fabric | L1–L4 depending on tech | FC vs iSCSI differ |
| Ops view | Data-center network | Separate from user campus LAN ideally |

## Lab exercises

### Lab 1 — Vocabulary drill

Explain to a rubber duck: LUN, zoning, multipath, latency sensitivity.

### Lab 2 — Spot it in architecture diagrams

Find a diagram with “FC switches” or “iSCSI VLAN” — label it SAN, not generic LAN.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| VM datastore latency | Fabric congestion / path loss | array stats, HBA paths |
| Server can’t see LUN | Zoning/masking | fabric config, WWNs/IQNs |
| iSCSI flaps | Ethernet pause/MTU/NIC | jumbo frames end-to-end |

## Common traps / interview gotchas

- SAN ≠ “Storage Available on Network” marketing fluff for NAS.
- Putting iSCSI on the same congested user VLAN is a classic footgun.
- Fibre Channel SAN may have **no IP** — ping won’t help.

## Mastery checklist

- [ ] Define SAN as block storage network
- [ ] Contrast SAN vs NAS with the vault vs cabinet analogy
- [ ] Name FC and iSCSI as transports
- [ ] Explain why storage traffic wants isolation

## Related notes

- [[LAN]] · [[Switches]] · [[Latency]] · [[Throughput]] · [[Cloud]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
