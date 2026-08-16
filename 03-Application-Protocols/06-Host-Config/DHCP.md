---
tags: [application-protocols, networking, ccna, dhcp]
aliases: [Dynamic Host Configuration Protocol, DORA]
layer: Application
---

# DHCP

## Learning objectives

- Explain DHCP as dynamic IPv4 host configuration
- Master DORA and lease lifecycle
- Understand relays (`ip helper-address`) across subnets
- Troubleshoot APIPA, wrong scope, and rogue servers (awareness)

## One-sentence definition

> **DHCP** dynamically assigns IP addresses and options (mask, gateway, DNS, etc.) to hosts using a Discover–Offer–Request–Ack exchange, primarily over [[UDP]] ports **67/68**.

## Analogy

> DHCP is the **hotel front desk assigning room keys**: you walk in (Discover), they offer a room (Offer), you accept (Request), they confirm (Ack) with checkout time (lease) and info like Wi‑Fi password sheet (options: gateway, DNS).

## Why it matters

Most endpoints are DHCP clients. Wrong option 3 (gateway) or option 6 (DNS) takes down “the Internet” for humans while routing looks fine. Relays make DHCP a routed design problem, not only L2.

## Deep dive

### Mental model — DORA

```text
Client                Server
Discover (broadcast) ─────────►
◄────────────── Offer
Request  ─────────────────────►
◄────────────── Ack (lease + options)
```

| Port | Role |
|------|------|
| UDP 67 | Server |
| UDP 68 | Client |

### Mechanism

- Lease times; T1/T2 renewal timers; NAK if wrong network after move
- Options: 1 mask, 3 router, 6 DNS, 15 domain, 42 NTP, 43 vendor, …
- **Relay:** router forwards DHCP to centralized servers; inserts giaddr so server knows subnet/scope
- Static mappings / reservations by MAC for printers, etc.

### IPv6 note

SLAAC + ICMPv6 RA often provides addressing; DHCPv6 also exists for options/addresses depending on design.

### On the wire

```bash
# macOS see lease info
ipconfig getpacket en0
ipconfig getifaddr en0

sudo tcpdump -ni en0 port 67 or port 68
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Host config service |
| Link | Broadcast domain matters for Discover | |

## Lab exercises

### Lab 1 — Read your lease

```bash
ipconfig getpacket en0
# Note: server_identifier, router, domain_name_server, lease_time
```

### Lab 2 — Capture DORA on a lab segment

Use GNS3 or a spare VLAN; tcpdump while renewing:

```bash
sudo ipconfig set en0 DHCP
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| 169.254.x.x | No Offer/Ack | server up, VLAN, relay, DHCP pool |
| Has IP, wrong GW/DNS | Wrong scope/options | relay giaddr, overlapping helpers |
| Lease conflicts | Overlapping scopes / dual servers | authorize servers, split scopes carefully |
| Works until roam | NAK / old lease | release-renew, correct VLAN |

## Common traps / interview gotchas

- DHCP Discover is broadcast — routers don’t forward without relay.
- Rogue DHCP on a VLAN hands bad gateways (MITM) — port security / DHCP snooping (Cisco) mitigate.
- “DNS is down” may be DHCP handing wrong option 6.
- Reservations still need unique MACs — cloned VMs collide.

## Mastery checklist

- [ ] Write DORA from memory
- [ ] Explain ports 67/68
- [ ] Describe why relays exist
- [ ] Recognize APIPA as DHCP failure symptom

## Related notes

- [[UDP]] · [[IP Address]] · [[MAC Address]] · [[ARP]] · [[DNS]] · [[NTP]]
- ← [[06-Host-Config/Index|Host Config]] · [[03-Application-Protocols/Index|Application Protocols]]
