---
tags: [ip-addressing, networking, ccna, arp, mac]
aliases: [IP vs MAC vs ARP, Layer 2 vs Layer 3 Addressing]
layer: Network + Data Link
---

# IP vs MAC vs ARP

## Learning objectives

- Separate Layer‑3 identity ([[IP Address]]) from Layer‑2 identity ([[MAC Address]])
- Explain [[ARP]] as the resolver that maps IPv4 → MAC on a [[LAN]]
- Trace one hop: when ARP fires, what Ethernet [[Frame]] fields change vs IP [[Packet]] fields
- Avoid the “MAC routes across the Internet” misconception

## One-sentence definition

> **IP** addresses name hosts for routing across networks; **MAC** addresses name interfaces for delivery inside a broadcast domain; **ARP** (IPv4) is the question‑and‑answer protocol that binds “this IP is at that MAC” so a frame can be built.

## Analogy

> Delivering a letter across the country: the **IP** is the **city + street address** on the envelope (end‑to‑end intent). At each local post office truck, workers only care about the **bag tag for this truck route** — that’s the **MAC**. **ARP** is asking the loading dock: “Who currently holds the bag for street address 10.1.1.5?” so they can slap on the right local tag.

## Why it matters

Switching exams, “why can’t I ping,” and “duplicate IP” incidents all collapse to this trio. If you mix L2 and L3, you will mis‑blame [[Routers]], mis‑read Wireshark, and fail behavioral questions.

## Deep dive

### Mental model

```text
Same LAN / VLAN (one broadcast domain)
─────────────────────────────────────
Host A                          Host B
IP 10.1.1.10                    IP 10.1.1.20
MAC aa:aa:aa:…                  MAC bb:bb:bb:…
        │                              │
        └──── ARP: who has 10.1.1.20? ─┘
              then Frame: dst MAC = bb:…

Different networks
─────────────────────────────────────
Host A → default gateway MAC (ARP for GW IP)
       → Router strips L2, routes L3, new L2 on next hop
```

### Roles compared

| Thing | Layer | Scope | Changes on path? |
|-------|-------|-------|------------------|
| [[IP Address]] | L3 | End‑to‑end (except NAT) | Stable across hops (ideally) |
| [[MAC Address]] | L2 | One broadcast domain / hop | **Rewritten every hop** |
| [[ARP]] | L2/L3 glue | IPv4 on Ethernet/LAN | Cache on hosts/routers |

IPv6 uses **NDP** (Neighbor Discovery), not ARP — same job, different protocol. See [[IPv4-vs-IPv6]].

### Mechanism — ARP in four beats

1. Host needs to send IP packet to `T` on local subnet (or to gateway if remote).
2. Check ARP table; if miss → ARP request (broadcast MAC `ff:ff:ff:ff:ff:ff`).
3. Owner of `T` unicasts ARP reply with its MAC.
4. Sender builds Ethernet frame: dst MAC from ARP, ethertype IPv4, payload = IP packet.

### On the wire / fields

**ARP packet (simplified):** Hardware type, Protocol type (IPv4), opcode (request/reply), sender MAC/IP, target MAC/IP.

**Ethernet frame carrying IP:** Dest MAC | Src MAC | Ethertype `0x0800` | IP header (src/dst IP) | L4…

After a router hop, **src/dst MAC change**; **src/dst IP usually stay** (until [[NAT-vs-PAT]]).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | L3 | IP identity & routing |
| OSI | L2 | MAC delivery on link |
| OSI | L2/L3 | ARP/ND resolution |
| TCP/IP | Internet + Network Access | Same split |

## Lab exercises

### Lab 1 — Watch ARP resolve

```bash
# Clear one entry if permitted, then ping a quiet LAN host
ping -c 1 192.168.1.1

# Linux
ip neigh
# macOS / general
arp -a

sudo tcpdump -ni any arp
```

### Lab 2 — Prove MAC rewrite across a hop (conceptual / lab)

In a two‑router Packet Tracer/GNS3 lab, capture on both sides of a router while pinging end‑to‑end. Confirm:

- IP src/dst unchanged
- MAC src/dst different on each segment
- ARP only for the *local* next hop, not the remote IP

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Incomplete ARP / nowhere | Target down, wrong subnet, VLAN | `ip neigh`; same VLAN? mask? |
| Dup IP weirdness | Two hosts claim one IP | ARP flaps; switch MAC table |
| Ping remote fails, local OK | Gateway ARP / route | ARP for GW; default route |
| Wrong host answers | Gratuitous ARP / MITM / misconfig | capture ARP replies |

## Common traps / interview gotchas

- You do **not** ARP for a remote Internet IP; you ARP for the **gateway**.
- Switches forward by MAC; they don’t need your IP to switch (but DHCP snooping/ARP inspection may care).
- MAC is not a “more permanent IP” for Internet routing — it’s hop‑local.
- Proxy ARP can hide mask mistakes — looks like magic, breaks later.
- “Layer 2 hop” vs “Layer 3 hop” is the difference between frame rewrite and route decision.

## Mastery checklist

- [ ] Explain IP vs MAC with the postal / truck‑tag analogy
- [ ] State when ARP runs vs when the default gateway is used
- [ ] Read an ARP cache and a MAC table and know which device shows which
- [ ] Predict which header fields change across a router
- [ ] Name NDP as IPv6’s ARP cousin

## Related notes

- [[IP Address]] · [[MAC Address]] · [[ARP]] · [[Frame]] · [[Packet]] · [[Switches]] · [[Routers]] · [[LAN]] · [[IPv4-vs-IPv6]] · [[Public-vs-Private-Addresses]]
- ← [[02-IP-Addressing/Index|IP Addressing]]
