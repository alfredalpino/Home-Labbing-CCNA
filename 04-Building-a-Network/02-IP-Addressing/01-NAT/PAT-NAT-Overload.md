---
tags: [nat, networking, ccna, pat, ip-addressing]
aliases: [PAT, NAT Overload, Port Address Translation]
layer: Network (Layer 3) + Transport ports
---

# PAT NAT Overload

## Learning objectives

- Explain many‑to‑one translation using source ports
- Read a PAT translation table entry end‑to‑end
- Configure IOS `overload` mental model and home‑router equivalent
- Troubleshoot port exhaustion, broken apps, and inbound limits

## One-sentence definition

> **PAT** (NAT overload) maps many inside IP addresses to one (or a few) outside IP addresses by also translating **TCP/UDP port numbers**, so return traffic demuxes to the correct host and socket.

## Analogy

> An entire apartment building shares **one street address** (public IP). The postal clerk writes a **unique box number** (source port) on each outbound letter. Replies come back to the street address + box number, and the clerk forwards to the right apartment (private IP + real port). That’s PAT.

## Why it matters

This is how nearly all consumer networks and most enterprise Internet egress work. Without PAT, RFC1918 hosts couldn’t share scarce IPv4. CCNA expects you to know *why ports are in the table* and why unsolicited inbound connections fail without port forwards / static entries.

## Deep dive

### Mental model

```text
Host A 10.1.1.10:51000 ─┐
Host B 10.1.1.11:51000 ─┼─► PAT ─► 203.0.113.5:40001  (A's flow)
                        └────────► 203.0.113.5:40002  (B's flow)
Same inside ports OK — outside ports differ.
```

### Mechanism

1. Inside host sends to Internet; source IP private, source port ephemeral.
2. PAT device picks outside IP (often the WAN interface) + **unique** source port.
3. Stores: inside local IP:port ↔ inside global IP:port (+ protocol, sometimes dest).
4. Return packet matches global IP:port → rewrite back to inside local IP:port.

IOS shape:

```text
access-list 1 permit 10.1.1.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/0 overload
```

### On the wire / fields

| Side | Source IP | Source port | Dest |
|------|-----------|-------------|------|
| Inside capture | `10.1.1.10` | `51000` | `8.8.8.8:53` |
| Outside capture | `203.0.113.5` | `40001` | `8.8.8.8:53` |

Checksums updated. ICMP is trickier (no ports) — devices use query IDs / embedding to track.

### Limits and inbound

- Concurrent flows limited by port space (~65k per public IP per protocol, less in practice).
- Unsolicited inbound to the public IP has **no mapping** → drop (unless static PAT / port forward).
- CGNAT ([[Public-vs-Private-Addresses]]) adds another overload layer at the ISP.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | L3 + L4 | Rewrites IP and ports |
| TCP/IP | Internet + Transport | Multiplexes many hosts onto one address |

## Lab exercises

### Lab 1 — See overload translations (IOS / PT)

```text
show ip nat translations
show ip nat statistics
```

Generate traffic from two inside hosts; confirm different `global` ports for the same outside IP.

### Lab 2 — Host proof of shared public IP

```bash
# On two devices behind same home router
curl -4 ifconfig.me
```

Same public IP → PAT (or CGNAT). Optional: run `tcpdump` on a lab outside interface and spot port remapping.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Random outbound failures | Port pool exhausted | NAT stats; add publics / reduce idle |
| Game/VoIP one‑way | Port/ALG / timeout | UPnP/port forward; longer timers |
| Inbound service dead | No static PAT | port‑forward rule; CGNAT |
| VPN fails behind PAT | NAT‑T / keepalive | UDP/4500; vendor NAT guide |

## Common traps / interview gotchas

- PAT is a **type of NAT**, not a totally separate protocol.
- Ephemeral port collisions are solved on the **outside** port, not by changing the client’s listen port.
- “Open a port” on a home router = static PAT / DNAT, not turning off PAT.
- Logging user identity by public IP alone is weak under PAT — need port + timestamp.
- FTP active mode / some SIP break without helpers — prefer modern designs (passive FTP, STUN, tunnels).

## Mastery checklist

- [ ] Draw many‑to‑one with two hosts sharing one public IP
- [ ] Explain why source ports are rewritten
- [ ] Read an IOS NAT translation line
- [ ] Predict inbound behavior without port forwards
- [ ] Contrast with [[Static-vs-Dynamic-NAT]] pool NAT

## Related notes

- [[NAT-vs-PAT]] · [[Static-vs-Dynamic-NAT]] · [[NAT64]] · [[Public-vs-Private-Addresses]] · [[TCP]] · [[UDP]] · [[IP Address]] · [[Routers]]
- ← [[01-NAT/Index|NAT]]
