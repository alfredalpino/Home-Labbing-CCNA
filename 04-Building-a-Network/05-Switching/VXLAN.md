---
tags: [switching, networking, ccna, vxlan, overlay]
aliases: [VXLAN, Virtual Extensible LAN]
layer: Overlay / data center L2 over L3
---

# VXLAN

## Learning objectives

- Define VXLAN as an L2 overlay that stretches Ethernet segments over an IP underlay
- Explain VNI, VTEP, and why VXLAN exists (VLAN ID scale + L3 underlay)
- Contrast VXLAN with classic [[VLANs]] and relate to [[MPLS]]/EVPN awareness
- Sketch a two-VTEP lab mental model even if hardware is limited

## One-sentence definition

> **VXLAN** (Virtual Extensible LAN) encapsulates Ethernet [[Frame]]s in UDP/IP so Layer-2 networks (identified by a **VNI**) can span a Layer-3 underlay between **VTEPs** — scaling far beyond 4094 VLANs.

## Analogy

> Classic [[VLANs]] are **colored rooms in one building** (limited paint colors: ~4094). VXLAN is **shipping whole rooms in sealed containers** across the city’s highway system (IP underlay). Each container has a big barcode (**VNI**, ~16 million). Loading docks (**VTEPs**) pack/unpack containers; trucks don’t open the furniture (inner MACs) — they just haul IP.

## Why it matters

Data centers and campus fabrics use VXLAN (+ often BGP EVPN) to stretch L2 for VM mobility and multi-tenancy without giant L2 underlays. CCNA-level: understand *overlay vs underlay* and why flooding/ARP need special care (multicast or control plane).

## Deep dive

### Mental model

```text
Host A ── Ethernet ── VTEP1 ── VXLAN (UDP/IP) ── underlay ── VTEP2 ── Ethernet ── Host B
                         │                              │
                      encap VNI                      decap VNI
```

### Mechanism

| Piece | Role |
|-------|------|
| VNI | 24-bit segment ID (like “super VLAN”) |
| VTEP | VXLAN Tunnel Endpoint — encap/decap |
| Underlay | IP routed network (OSPF/BGP/ECMP) between VTEPs |
| Outer header | IP + UDP (port **4789**) + VXLAN header |
| Control plane | Flood-and-learn (multicast) or **EVPN** (BGP) — modern preferred |

**BUM traffic** (Broadcast, Unknown unicast, Multicast) must be replicated across VTEPs — multicast groups or head-end replication / EVPN.

### On the wire

Outer: underlay src/dst VTEP IPs. UDP dst 4789. VXLAN header includes VNI. Inner: original Ethernet frame (and usually inner IP). MTU: underlay must allow ~50 extra bytes — jumbo or careful sizing.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Overlay | L2 service | Ethernet in VNI |
| Underlay | L3 | IP between VTEPs |
| Encap | UDP/IP | Transport of VXLAN |

## Lab exercises

### Lab 1 — Whiteboard / Packet Tracer conceptual

Draw two racks, VTEP loopbacks, underlay spine, VNI 10010 mapping to VLAN 10 on each access. Trace a frame from Host A to B: inner MAC → encap → underlay hop-by-hop → decap.

### Lab 2 — Linux VXLAN (if you have two VMs)

```bash
# Example sketch — adjust iface/IPs
ip link add vxlan100 type vxlan id 100 local 10.0.0.1 dstport 4789
ip link set vxlan100 up
# Bridge vxlan100 with a tap/veth to a VM — document ARP across underlay
```

Capture UDP/4789 and identify VNI in Wireshark.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Local OK, remote fail | Underlay to VTEP down | ping VTEP loopbacks, routing |
| MTU black hole | Underlay MTU too small | ping -M do -s, jumbo config |
| BUM not reaching | Multicast/EVPN issue | underlay mcast, nve peers |
| Wrong segment | VNI/VLAN map mismatch | VNI mapping both sides |

## Common traps / interview gotchas

- VXLAN does **not** replace the need for underlay routing — it depends on it.
- VLAN ID still may exist locally; VNI is the fabric-wide identifier.
- “L2 stretch” can revive large failure domains — design carefully.
- EVPN is control plane; VXLAN is often the data plane — don’t conflate names.

## Mastery checklist

- [ ] Define VTEP, VNI, underlay vs overlay
- [ ] Explain why VXLAN scales past 4094
- [ ] Name UDP 4789 and MTU impact
- [ ] Contrast flood-and-learn vs EVPN at awareness level

## Related notes

- [[VLANs]] · [[Switches]] · [[OSPF]] · [[BGP]] · [[MPLS]] · [[Frame]] · [[UDP]] · [[MAC-Address-Tables]]
- ← [[05-Switching/Index|Switching]] · [[04-Building-a-Network/Index|Building a Network]]
