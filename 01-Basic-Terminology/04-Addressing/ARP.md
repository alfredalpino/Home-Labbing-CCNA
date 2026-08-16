---
tags: [basic-terminology, networking, ccna, arp]
aliases: [Address Resolution Protocol, ARP Cache]
layer: Link-adjacent (IPv4 ↔ Ethernet)
---

# ARP

## Learning objectives

- Explain why IPv4 needs ARP on Ethernet/Wi-Fi LANs
- Detail request/reply frames and cache behavior
- Understand gratuitous ARP, proxy ARP, and timeout effects
- Defend against ARP spoofing conceptually (detection/mitigation overview)

## One-sentence definition

> **ARP** (Address Resolution Protocol) maps an IPv4 address to a [[MAC Address]] on the local link so a host can encapsulate an IP [[Packet]] inside an Ethernet [[Frame]] destined to the correct next hop.

## Analogy

> ARP is yelling down the hallway: **“Who has apartment 192.168.1.20?”** and hearing back the doorway sticker (MAC). For remote apartments in another city, you don’t yell across the country — you ask the lobby desk (default gateway) for *its* doorway.

## Why it matters

No ARP → no local IPv4 delivery. Wrong ARP → traffic black-holed or intercepted. “Intermittent connectivity after failover” is often stale ARP/gratuitous ARP timing. Engineers live in `arp -a` and dynamic ARP inspection discussions.

## Deep dive

### Mental model

```text
Want to send IP packet to 192.168.1.20 on my LAN
  → Need dest MAC for .20
  → ARP: "Who has 192.168.1.20? Tell 192.168.1.10"
  → Reply: ".20 is at aa:bb:cc:dd:ee:ff"
  → Cache binding; send frame
```

For **remote** destinations: ARP for the **default gateway’s IP**, not the remote host. The gateway MAC is your L2 next hop.

### Mechanism

1. Check ARP cache for IP → MAC.
2. If miss: send **ARP Request** (Ethernet broadcast, EtherType `0x0806`).
3. Target unicasts **ARP Reply**.
4. Cache entry (complete); incomplete entries may exist while waiting.
5. Entries time out and are refreshed.

**Gratuitous ARP:** announce/update own IP↔MAC (failover, detect duplicates).  
**Proxy ARP:** router answers ARP for remote IPs (legacy/special designs; can be messy).

### On the wire / fields

ARP packet fields: Hardware type, Proto type, opcode (1 request / 2 reply), sender MAC/IP, target MAC/IP.

```bash
arp -a
arp -d 192.168.1.1     # delete entry (may need sudo; syntax OS-specific)
sudo tcpdump -ni en0 arp
```

Wireshark: `arp`, `arp.opcode == 1`

### IPv6 note

IPv6 uses **Neighbor Discovery** (ICMPv6 NS/NA), not ARP. Mental model is analogous; protocol differs.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Link ↔ Internet glue | Resolve next-hop MAC for IPv4 |
| OSI | Between 2 and 3 | Often taught as L3-ish helper on L2 |

## Lab exercises

### Lab 1 — Force an ARP exchange

```bash
GW=$(route -n get default | awk '/gateway:/ {print $2}')
sudo arp -d "$GW" 2>/dev/null || true
sudo tcpdump -ni en0 -e arp &
ping -c 1 "$GW"
```

### Lab 2 — Read the cache after browsing

```bash
arp -a
# Identify gateway vs local peers vs incomplete entries
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Incomplete ARP | Host down / wrong subnet / VLAN | ping, VLAN, switch port |
| Flapping MAC for one IP | Conflict / spoof | both stations, DAI, port security |
| Works after clear ARP | Stale entry post-failover | GARP on VIP move, timers |
| Remote IP ARP attempts | Missing gateway / proxy ARP oddity | routing table |

## Common traps / interview gotchas

- You never ARP for a remote Internet IP on a normal host — only for on-link next hop.
- Switches flood ARP requests as broadcasts; huge L2 domains amplify noise.
- ARP poisoning/MITM: attacker claims victim IPs — mitigate with DAI, sticky MAC, 802.1X, monitoring (defensive knowledge).
- Static ARP is rare glue for broken gear — document why.

## Mastery checklist

- [ ] Draw request (broadcast) vs reply (unicast)
- [ ] Explain gateway ARP vs on-link host ARP
- [ ] Capture ARP in tcpdump and decode fields
- [ ] Describe gratuitous ARP use in HA VIP move

## Related notes

- [[MAC Address]] · [[IP Address]] · [[Frame]] · [[Packet]] · [[ICMP]] · [[DHCP]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
