---
tags: [vpn, tunneling, networking, ccna, gre, ipsec, gre-ipsec]
aliases: [GRE, GRE Tunnel, GRE over IPsec, GRE IPsec, IPIP]
layer: Overlay / tunneling
---

# GRE-IPSec-Tunnels

## Learning objectives

- Explain GRE as a simple IP encapsulation tunnel (protocol 47)
- Explain why GRE alone is unencrypted and why GRE+IPsec is a classic combo
- Configure a point-to-point GRE tunnel and protect it with IPsec in IOS labs
- Troubleshoot recursive routing and MTU/fragmentation issues

## One-sentence definition

> **GRE** (Generic Routing Encapsulation) wraps packets in a new IP header to build a virtual point-to-point link; **GRE over IPsec** adds encryption/integrity so that tunnel can safely cross untrusted networks.

## Analogy

> GRE is a **clear plastic pneumatic tube** between buildings: anything you stick in (IP, even multicast/routing hellos) pops out the other end — but anyone along the alley can *see* the papers. IPsec is sliding that tube **inside a locked armored sleeve**. Together: flexible routing-friendly tunnel + confidentiality.

## Why it matters

Pure IPsec (tunnel mode) protects IP unicast well but historically awkward for multicast/IGP over the VPN. GRE gives a clean `Tunnel0` interface for OSPF/EIGRP; IPsec wraps it for security. DMVPN and many labs still teach this pattern (even as SD-WAN / VTI evolve).

## Deep dive

### Mental model

```text
Without crypto:
  Inner IP → GRE header → Outer IP (proto 47)

With IPsec (common):
  Inner IP → GRE → outer IP  then  ESP protects that outer packet
  (transport mode protecting GRE is a frequent design)

Router sees Tunnel0 as a normal interface for routing.
```

### Mechanism

| Piece | Role |
|-------|------|
| Tunnel source/dest | Underlay endpoints (public/routable IPs) |
| Tunnel mode gre ip | Classic GRE |
| IPsec profile | Encrypts GRE (or uses VTI instead of GRE) |
| Keepalives | Optional GRE keepalives detect dead peer |
| Recursive routing | Tunnel destination learned *via* the tunnel — death spiral |

**Recursive routing fix:** ensure tunnel destination is reached via underlay (static/default/IGP on physical), never via Tunnel0.

### On the wire

- GRE: IP protocol **47**; header includes flags/key/seq optional  
- IPsec: ESP (proto 50) or UDP 4500 if NAT-T  
- Overhead stacks → lower effective MTU; DF bit + PMTUD drama common

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| GRE | Overlay interface | L3-in-L3 (or other payload) |
| IPsec | Security | Confidentiality/integrity for GRE/IP |
| Related | [[IPSec-vs-SSL-VPN]] | Crypto framework |

## Lab exercises

### Lab 1 — GRE only (GNS3)

```ios
interface Tunnel0
 ip address 172.16.0.1 255.255.255.252
 tunnel source GigabitEthernet0/0
 tunnel destination 203.0.113.2
 tunnel mode gre ip
ip route 192.168.2.0 255.255.255.0 172.16.0.2
```

Verify `show interfaces tunnel 0`, ping, then run OSPF over Tunnel0.

### Lab 2 — GRE + IPsec

Add IKE + IPsec profile protecting traffic between tunnel endpoints (or `tunnel protection ipsec profile ...` on IOS). Confirm Wireshark shows ESP, not clear GRE, on the Internet link. Intentionally create recursive routing and fix it.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Tunnel up/up but no ping | Routes / ACL | tunnel IPs, `show ip route` |
| Tunnel flapping | Recursive routing | remove route via Tunnel to dest |
| OSPF won’t adj | MTU / network type | `ip ospf mtu-ignore` lab, fix MTU |
| Cleartext on wire | IPsec not applied | crypto ACL/profile, ESP present |

## Common traps / interview gotchas

- GRE ≠ encryption. Saying “we have GRE VPN” without IPsec is incomplete for Internet.
- Tunnel destination must be underlay-reachable.
- Double encapsulation hurts MTU — lower tunnel IP MTU (e.g. 1400) in labs.
- Modern alternative: IPsec **VTI** (tunnel without GRE) — know GRE+IPsec still appears in exams/legacy.

## Mastery checklist

- [ ] Configure GRE and route over Tunnel0
- [ ] Explain why add IPsec
- [ ] Prevent/fix recursive routing
- [ ] Relate to [[Site-to-Site-vs-Remote-Access]] designs

## Related notes

- [[VPN]] · [[IPSec-vs-SSL-VPN]] · [[Site-to-Site-vs-Remote-Access]] · [[OSPF]] · [[EIGRP]] · [[WAN]] · [[Packet]]
- ← [[06-Tunneling-and-VPNs/Index|Tunneling & VPNs]] · [[04-Building-a-Network/Index|Building a Network]]
