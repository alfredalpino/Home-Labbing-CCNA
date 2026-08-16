---
tags: [routing, networking, ccna, default-gateway, gateway]
aliases: [Default Gateway, Gateway of Last Resort, Default Route]
layer: Network (Layer 3) / host config
---

# Default Gateway

## Learning objectives

- Define default gateway from the **host** and **router** perspectives
- Relate default gateway to the default route `0.0.0.0/0` (IPv4) / `::/0` (IPv6)
- Configure and verify gateway on Linux and Cisco IOS
- Troubleshoot “local OK, Internet broken” and wrong-gateway loops

## One-sentence definition

> A **default gateway** is the next-hop IP (usually on the local subnet) that a host or router uses when **no more-specific route** matches — the “way out” to the rest of the network or Internet.

## Analogy

> Your house only knows its own street. The default gateway is the **neighborhood on-ramp attendant**: “If you don’t know the destination address locally, drive to *me* and I’ll put you on the bigger roads.” If you point at the wrong attendant (wrong IP) or the ramp is closed (down gateway), you never leave the block — even though your driveway works.

## Why it matters

Hosts don’t run OSPF. They need one correct gateway (or a few via DHCP/FHRP). Mis-set gateway is the #1 home-lab “no Internet” cause. On routers, **gateway of last resort** is how stubs and edges reach everything else.

## Deep dive

### Mental model

```text
Host wants 8.8.8.8
  → is 8.8.8.8 on my subnet? NO
  → send to default gateway MAC (ARP for GW IP)
  → L2 frame to gateway → gateway routes onward

Router with 0.0.0.0/0 via ISP
  → unknown prefixes → ISP next hop (“gateway of last resort”)
```

### Host vs router language

| Context | Term | Typical source |
|---------|------|----------------|
| PC / server | Default gateway | DHCP option 3, or static |
| Cisco router | Gateway of last resort | `ip route 0.0.0.0 0.0.0.0 …` or dynamic default |
| Linux | default / `default via` | NetworkManager, `ip route`, DHCP |

Same idea: **least-specific catch-all route**.

### Requirements that bite people

1. Gateway IP must be **on-link** (same subnet / VLAN) as the host (unless proxy-ARP tricks — don’t rely on them).
2. Host must [[ARP]] for the gateway successfully.
3. Gateway must have a path **back** (return routing / NAT / firewall).
4. With [[VLANs]], each SVI/subnet has its own gateway IP (often `x.x.x.1`).

### On the wire

No special “gateway protocol” for basic IPv4 hosts: Ethernet frame to gateway MAC, IP dst remains the remote address. Router decrements TTL and forwards. IPv6 uses Neighbor Discovery (RA can advertise default router).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Host stack | L3 decision, L2 delivery | Who gets the frame leaving the NIC |
| Router | L3 | Default route installs last-resort path |

## Lab exercises

### Lab 1 — Break and fix the PC gateway (Linux)

```bash
ip route show
# Note current default, then (lab only):
sudo ip route del default
ping -c 2 8.8.8.8          # should fail
ping -c 2 $(hostname -I | awk '{print $1}')  # local may still work
sudo ip route add default via <GATEWAY_IP>
```

### Lab 2 — Router default + verify (Cisco IOS)

```ios
ip route 0.0.0.0 0.0.0.0 203.0.113.1
show ip route
show ip route 0.0.0.0
```

Confirm `Gateway of last resort is 203.0.113.1`. From a PC behind the router, traceroute to an external IP and ensure first hop is the router’s LAN interface.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Local ping OK, Internet fail | Wrong/missing GW | `ip route` / `ipconfig` / DHCP |
| No ARP for gateway | Wrong VLAN / GW IP | `arp -a`, switch VLAN, cable |
| Intermittent off-net | FHRP / dual GW fight | HSRP/VRRP active, duplicate IPs |
| One subnet works | Missing SVI / ACL | Per-VLAN gateway, ACL on SVI |

## Common traps / interview gotchas

- Default gateway is an **IP on your subnet**, not “the Internet” or a DNS server.
- Changing DNS alone never fixes a missing gateway.
- Two defaults without policy = asymmetric / unpredictable paths.
- “Gateway” in marketing (IoT “gateway”) ≠ L3 default gateway — clarify in interviews.

## Mastery checklist

- [ ] Draw host → ARP → gateway → routed path
- [ ] Set/remove default on Linux and IOS
- [ ] Explain gateway of last resort on `show ip route`
- [ ] Diagnose VLAN mismatch to gateway IP

## Related notes

- [[Static-vs-Dynamic-Routing]] · [[IP Address]] · [[ARP]] · [[DHCP]] · [[Routers]] · [[VLANs]] · [[LAN]]
- ← [[04-Routing/Index|Routing]] · [[04-Building-a-Network/Index|Building a Network]]
