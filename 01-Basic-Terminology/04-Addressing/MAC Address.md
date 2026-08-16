---
tags: [basic-terminology, networking, ccna, mac]
aliases: [MAC, Hardware Address, EUI-48, Burned-In Address]
layer: Data Link (Layer 2)
---

# MAC Address

## Learning objectives

- Define MAC as the link-layer interface identifier
- Decode EUI-48 format, OUI, and unicast/multicast/local bits
- Explain MAC learning, flooding, and why MACs are local-scope
- Relate MAC to [[ARP]] and Ethernet [[Frame]] delivery

## One-sentence definition

> A **MAC address** (Media Access Control address) is a 48-bit (EUI-48) link-layer address that identifies a network interface on a local network segment for frame delivery.

## Analogy

> A MAC address is the **burned-in serial sticker on a network doorway** (NIC). Switches learn which doorway is plugged into which switch port — like a receptionist learning which desk sits on which hallway.

## Why it matters

Switching, Wi-Fi association, port security, MAC ACLs, and DHCP sticky bindings all use MACs. When two hosts share a VLAN but can’t talk, you’re often in MAC/ARP/VLAN territory — not OSPF.

## Deep dive

### Mental model

```text
MAC  = local delivery ID (this LAN / VLAN)
IP   = end-to-end logical ID (routed)
```

MACs are **not** global routing identifiers. They get rewritten every routed hop.

### Format

```text
aa:bb:cc:dd:ee:ff
│└──── OUI (vendor) ────┘└── nic-specific ──┘
```

Common writings: `aa:bb:cc:dd:ee:ff`, `aa-bb-cc-dd-ee-ff`, `aabb.ccdd.eeff` (Cisco).

**Special addresses:**

| Address | Meaning |
|---------|---------|
| `ff:ff:ff:ff:ff:ff` | Broadcast |
| `01:00:5e:…` | IPv4 multicast mapped MACs |
| `33:33:…` | IPv6 multicast MACs |

**I/G bit (least significant bit of first octet):** 0=unicast, 1=multicast/broadcast.  
**U/L bit:** 0=globally unique (burned-in), 1=locally administered (virtualization, spoofing, some Wi-Fi privacy MACs).

### Mechanism — switches

- Learn source MAC → port
- Forward known unicast to one port
- Flood unknown/broadcast/multicast (per VLAN policy)

MAC tables age out; instability → flaps.

### On the wire / fields

Dest/Src MAC at the start of Ethernet frames.

```bash
ifconfig en0 | grep ether
arp -a
sudo tcpdump -ni en0 -e -c 10
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Link / Network Access | Interface ID for frames |
| OSI | 2 | MAC sublayer addressing |

## Lab exercises

### Lab 1 — Find OUI

Take your MAC’s first three octets and look up the vendor OUI list (or `curl` an OUI API). Virtual adapters often show local admin bit set.

### Lab 2 — Gateway MAC

```bash
ping -c 1 $(route -n get default | awk '/gateway:/ {print $2}')
arp -a | head
```

Your default gateway’s MAC is the L2 next hop for off-subnet IPv4 traffic.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| MAC flapping between ports | Loop / mis-cabling | STP, cables, dual NICs |
| Port security violation | Unexpected MAC | allowed list, phone+PC daisy chain |
| Can’t resolve ARP | Wrong VLAN / blocked | SVI, VLAN membership |
| Random Wi-Fi MAC | Privacy feature | DHCP leases look “new” devices |

## Common traps / interview gotchas

- Changing IP does not change MAC (unless you also spoof).
- VM vNICs have virtual MACs — collisions possible if poorly cloned.
- EtherChannel/MLAG and mobility can make MAC location move — design for it.
- “MAC address filtering” on home Wi-Fi is weak security theater.

## Mastery checklist

- [ ] Expand a MAC and identify broadcast
- [ ] Explain OUI and local/admin bit
- [ ] Describe switch learning/flooding
- [ ] Find gateway MAC on your LAN

## Related notes

- [[Frame]] · [[ARP]] · [[IP Address]] · [[Packet]] · [[Host]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
