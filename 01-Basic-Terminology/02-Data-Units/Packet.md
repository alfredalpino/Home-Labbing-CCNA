---
tags: [basic-terminology, networking, ccna, packet]
aliases: [IP Packet, Datagram, Package]
layer: Network (Layer 3)
---

# Packet

> Note: some roadmaps label this **“Package.”** The correct networking term is **packet** (IP datagram). “Package” is a typo.

## Learning objectives

- Define packet as the Layer-3 PDU and place it in encapsulation
- Read the critical IPv4 header fields used in real troubleshooting
- Explain routing decisions: longest prefix match on destination IP
- Contrast packet vs [[Frame]] vs segment vs bits

## One-sentence definition

> A **packet** is a network-layer protocol data unit — typically an **IPv4/IPv6 datagram** — containing addressing and control fields plus a payload, forwarded hop-by-hop by routers.

## Analogy

> A packet is a **shipping carton with a destination warehouse address (IP)** and contents. Trucks may change license plates each highway ([[Frame]]/MAC), but the carton label (IP) usually stays the same until NAT rewrites it at a border.

## Why it matters

Switches care about frames; **routers care about packets**. When you debug “can’t reach subnet B,” you are reasoning about packets: TTL expiry, fragmentation, ACL matches on IP headers, asymmetric routing, and black holes. If you blur packet and frame, you will misplace blame between L2 and L3.

## Deep dive

### Mental model — encapsulation

```text
Application data
    ↓
Transport segment/datagram   ([[TCP]] / [[UDP]] header + data)
    ↓
Network PACKET               (IP header + transport + data)
    ↓
Data-link FRAME              (Ethernet/Wi-Fi header + packet + FCS)
    ↓
Bits on [[Transmission Media Types|media]]
```

Each hop that routes:

1. Receives a frame, checks FCS, de-encapsulates to packet
2. Decrements TTL/Hop Limit, looks up destination IP
3. Re-encapsulates into a **new** frame for the next link (new MACs)

**The packet’s source/dest IP usually stay the same end-to-end** (except NAT).  
**MACs change every hop.**

### Mechanism — IPv4 header fields that matter

| Field | Why you care |
|-------|----------------|
| Version | 4 vs 6 |
| IHL | Options presence (rare today) |
| DSCP/ECN | QoS marking |
| Total Length | Packet size |
| Identification + Flags + Frag Offset | Fragmentation |
| TTL | Loop control; traceroute uses expiry |
| Protocol | 6=TCP, 17=UDP, 1=ICMP |
| Header Checksum | IPv4 only; recomputed each hop |
| Source / Dest Address | Identity + routing key |
| Options | Historically source route etc. (mostly avoided) |

**IPv6 differences (must know):** no header checksum, Hop Limit instead of TTL, no in-header fragmentation by routers (hosts use extension headers), 128-bit addresses.

### Packet size, MTU, fragmentation

- **MTU**: max frame payload on a link (Ethernet commonly 1500 → IP packet ≤ 1500 unless jumbo).
- If packet > MTU: IPv4 may fragment (if allowed); IPv6 routers don’t fragment.
- **PMTUD**: hosts discover path MTU using [[ICMP]] “Fragmentation Needed”; if ICMP filtered → **black hole**.

### On the wire

Wireshark display filter examples:

```text
ip
ip.addr == 192.0.2.10
ip.ttl < 5
icmp
```

```bash
sudo tcpdump -ni any -vv ip
sudo tcpdump -ni any 'ip and host 1.1.1.1'
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet / Network | IP packet is the central PDU |
| OSI | 3 | Network layer PDU |

## Lab exercises

### Lab 1 — Watch TTL and hop rewrite of MACs

```bash
ping -c 3 1.1.1.1
sudo tcpdump -ni en0 -e icmp
# -e shows Ethernet MACs. Compare MAC vs IP across hops (local hop only on LAN).
```

### Lab 2 — Packet size vs ping payload

```bash
ping -c 2 -s 1472 1.1.1.1   # 1472 + 8 ICMP + 20 IP = 1500 (typical)
ping -c 2 -s 1473 1.1.1.1   # often needs DF clear or fragments / fails
# On macOS/Linux flags differ; also try: ping -D -s 1473 (Don't Fragment) where supported
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Request timed out mid-path | ACL drop / routing blackhole | traceroute, interface ACLs, VRF |
| Works for small payloads only | MTU / PMTUD black hole | ping size tests, ICMP admin-prohibited/frag-needed |
| Odd source IPs | NAT or spoofing | NAT tables, uRPF |
| TTL exceeded in transit | Loop or too many hops | routing loops, traceroute |

## Common traps / interview gotchas

- Packet ≠ frame. Routing = packets; switching = frames.
- NAT rewrites packet addresses — end-to-end IP transparency dies at the NAT boundary.
- “Packet loss” at Wireshark may be capture drops, not network loss.
- Routers decrement TTL; switches (pure L2) do not.

## Mastery checklist

- [ ] Draw encapsulation from HTTP bytes → Ethernet frame
- [ ] Explain what changes each hop (MAC vs IP vs TTL)
- [ ] Name five IPv4 header fields used in incidents
- [ ] Describe an MTU black hole and how to prove it

## Related notes

- [[Frame]] · [[IP Address]] · [[MAC Address]] · [[ARP]] · [[Bandwidth]] · [[Throughput]]
- [[TCP]] · [[UDP]] · [[ICMP]] · [[Transmission Media Types]]
- ← [[02-Data-Units/Index|Data Units]] · [[01-Basic-Terminology/Index|Basic Terminology]]
