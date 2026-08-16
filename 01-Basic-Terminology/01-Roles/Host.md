---
tags: [basic-terminology, networking, ccna, host]
aliases: [End System, Network Host, Node]
layer: End system (L3-capable)
---

# Host

## Learning objectives

- Define host precisely in IETF/Cisco study language
- Contrast host vs router vs switch (roles can overlap on one box)
- Know what makes a device “on the network” (interfaces, addresses, stacks)
- Use host tooling to inventory identity: hostname, IPs, MACs, routes

## One-sentence definition

> A **host** is an end system that can send and receive IP packets — typically a computer, phone, VM, container, or appliance — as opposed to a pure forwarding device.

## Analogy

> A host is any **building with a street address** on the IP map — house, shop, or warehouse. Routers are more like **interchanges**; they may also have a small office (management IP), but their main job is directing traffic between roads.

## Why it matters

Addressing, ACLs, monitoring, and inventory are all host-centric: “which host owns this IP?”, “which host is scanning?”, “which host failed DHCP?”. Ambiguous language (“the switch did DNS”) hides real fault domains.

## Deep dive

### Mental model

In classical Internet architecture:

- **Hosts** = endpoints that *originate or terminate* application traffic
- **Routers** = forward packets between networks (may also be hosts for management)
- **Switches** (L2) = forward frames inside a broadcast domain

Modern reality: a “L3 switch,” firewall, or load balancer is often **both** a forwarder and a host (has an IP management plane).

### Mechanism — what every host has

1. One or more network interfaces (physical, VLAN, Wi-Fi, tunnel, loopback)
2. Link-layer address(es) where applicable ([[MAC Address]])
3. IP address configuration ([[IP Address]], often via [[DHCP]])
4. A protocol stack (ARP/ND, IP, ICMP, TCP/UDP, apps)
5. A routing table (even if only “default gateway”)

**Hostname** is a human label; it is *not* the network identity. DNS may map names ↔ IPs, but the packet carries addresses, not hostnames (except inside app payloads).

### Host vs node vs device

| Term | Typical meaning |
|------|-----------------|
| Host | IP end system |
| Node | Vague; any networked entity |
| Device | Hardware/appliance emphasis |
| Endpoint | Security/Zero Trust language for host |

### On the wire / fields

A host is visible as:

- Source/destination IP in [[Packet]]s
- Source/destination MAC in local [[Frame]]s
- Sometimes DHCP client ID / FQDN options

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | All layers on the end system | Full stack runs on hosts |
| OSI | 1–7 | Host implements full stack; routers mainly 1–3 |

## Lab exercises

### Lab 1 — Inventory a host

```bash
hostname
ifconfig           # or: ip addr
netstat -rn        # or: ip route
arp -a             # local L2/L3 bindings
scutil --dns       # macOS resolver config
```

### Lab 2 — Loopback is still a host interface

```bash
ping -c 2 127.0.0.1
ping -c 2 ::1
```

Traffic never leaves the machine — still valid IP host behavior.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Host online but “no network” | No default route / wrong mask | Routing table, DHCP lease |
| Duplicate IP | Two hosts same address | ARP flaps, switch CAM, `arp -a` |
| Wrong hostname in logs | Local name ≠ DNS name | `hostname`, PTR/A records |
| Can ping gateway, not Internet | Upstream / DNS / firewall | Path beyond gateway, DNS |

## Common traps / interview gotchas

- Routers have host functions (SSH, SNMP, NTP client) — management VRF vs data plane matters.
- Containers/VMs are hosts with virtual NICs; underlay vs overlay addressing confuses beginners.
- “Host route” (`/32` or `/128`) means a route to a single address — terminology overlap.
- Broadcast/multicast delivery is about *networks*, but senders/receivers are still hosts.

## Mastery checklist

- [ ] Define host vs router in one breath
- [ ] List the minimum config a host needs to reach another subnet
- [ ] Inventory IP, MAC, gateway, DNS on macOS without a GUI
- [ ] Explain why hostname ≠ identity on the wire

## Related notes

- [[Client]] · [[Server]] · [[IP Address]] · [[MAC Address]] · [[ARP]]
- [[DHCP]] · [[DNS]] · [[Packet]] · [[Frame]]
- ← [[01-Roles/Index|Roles]] · [[01-Basic-Terminology/Index|Basic Terminology]]
