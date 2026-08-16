---
tags: [basic-terminology, networking, ccna, frame]
aliases: [Ethernet Frame, Data Link PDU, L2 Frame]
layer: Data Link (Layer 2)
---

# Frame

## Learning objectives

- Define frame as the Layer-2 PDU
- Read Ethernet header fields: MACs, EtherType, FCS
- Explain switching vs routing using frames vs packets
- Understand broadcast domains, flooding, and MAC learning at a conceptual mastery level

## One-sentence definition

> A **frame** is a data-link-layer protocol data unit that packages a network [[Packet]] (or other payload) for delivery across a single physical or logical link using link-layer addressing (e.g. Ethernet [[MAC Address]]es).

## Analogy

> A frame is the **local delivery envelope** used only on this block. The outer sticker says which house on this street (MAC). When the mailman hands the package to a highway driver, they put it in a **new envelope** for the next road.

## Why it matters

Wi-Fi association issues, duplex mismatches, VLAN tags, CAM table overflows, and ARP all live in the world of frames. If the frame never delivers the packet to the right next hop, no amount of perfect OSPF will save you.

## Deep dive

### Mental model

```text
Same L2 broadcast domain (VLAN / LAN segment):
  Host A ──frame──► Switch ──frame──► Host B
           (MACs matter; IP may be same subnet)

Across routers:
  Host A ──frame──► R1 ──frame──► R2 ──frame──► Host B
  Packet IPs stay (modulo NAT); frame MACs rewrite each hop
```

### Ethernet frame (simplified)

```text
[Dest MAC 6][Src MAC 6][802.1Q optional 4][EtherType 2][Payload 46–1500][FCS 4]
```

| Field | Purpose |
|-------|---------|
| Dest MAC | Who should accept on this LAN |
| Src MAC | Sender on this LAN; used for learning |
| 802.1Q tag | VLAN ID + PCP (QoS) when trunking |
| EtherType | What’s inside: `0x0800` IPv4, `0x86DD` IPv6, `0x0806` ARP |
| Payload | Usually the IP packet (or ARP) |
| FCS | CRC integrity check |

**Minimum payload padding** exists so collisions/timing rules of classic Ethernet still hold; modern full-duplex switched Ethernet still keeps minimum frame size rules.

### Mechanism — what a switch does

1. Accept frame on a port (if FCS OK)
2. Learn Src MAC → port mapping (MAC/CAM table)
3. Lookup Dest MAC:
   - **known unicast** → forward out one port
   - **unknown unicast** → flood in VLAN
   - **broadcast** (`ff:ff:ff:ff:ff:ff`) → flood
   - **multicast** → flood or constrain (IGMP snooping)
4. Never “route” by IP unless it’s an L3 interface / SVI

### On the wire

```bash
sudo tcpdump -ni en0 -e -vv arp or icmp
# -e prints Ethernet headers
```

Wireshark: `eth`, `vlan`, `eth.dst == ff:ff:ff:ff:ff:ff`

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access / Link | Frame delivery on local network |
| OSI | 2 | Data link PDU; LLC/MAC sublayers historically |

## Lab exercises

### Lab 1 — See MACs on local traffic

```bash
arp -a
sudo tcpdump -ni en0 -c 20 -e not port 443
```

Identify your NIC MAC vs gateway MAC.

### Lab 2 — Broadcast frames (ARP)

```bash
ping -c 1 192.168.1.1   # use your gateway
sudo tcpdump -ni en0 -e arp
```

ARP request is Ethernet broadcast; reply is unicast.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Local IP works, remote fails | L3/routing — frames OK | gateway, routes |
| Same VLAN can’t ping | L2 issue / ACL / private VLAN | MAC table, VLAN membership, cable |
| Intermittent MAC flaps | Loop or duplicate | STP, cabling, dual-homed misconfig |
| Oversized frames dropped | MTU / jumbo mismatch | interface MTU both sides |

## Common traps / interview gotchas

- Wi-Fi also uses frames (802.11), but format ≠ Ethernet; AP bridges to Ethernet.
- Trunks carry many VLANs via tagged frames; access ports usually untagged.
- FCS errors → physical/duplex problems, not “DNS.”
- Hubs (obsolete) flood everything; switches reduce unicast flooding via learning.

## Mastery checklist

- [ ] Sketch Ethernet header and explain EtherType
- [ ] Explain when a switch floods vs forwards
- [ ] Describe why MACs rewrite each routed hop
- [ ] Capture ARP and point to broadcast dest MAC

## Related notes

- [[Packet]] · [[MAC Address]] · [[ARP]] · [[IP Address]] · [[Transmission Media Types]]
- [[Bandwidth]] · [[Latency]] · [[Throughput]]
- ← [[02-Data-Units/Index|Data Units]] · [[01-Basic-Terminology/Index|Basic Terminology]]
