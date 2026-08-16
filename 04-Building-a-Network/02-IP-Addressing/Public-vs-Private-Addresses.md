---
tags: [ip-addressing, networking, ccna, rfc1918, nat]
aliases: [Private IP, Public IP, RFC1918, Public vs Private IP]
layer: Network (Layer 3)
---

# Public vs Private Addresses

## Learning objectives

- Memorize RFC1918 private IPv4 ranges and why they exist
- Contrast routable public space vs non‑internet‑routable private space
- Explain CGNAT as “private‑like” space used by ISPs at scale
- Relate private addressing to [[NAT-vs-PAT]] and the [[IP Address]] note

## One-sentence definition

> **Public** [[IP Address]]es are globally unique and Internet‑routable; **private** addresses (RFC1918) are for internal use only and must be translated or tunneled before they can usefully appear on the public Internet.

## Analogy

> Public IPs are **government‑issued street addresses** the global postal system understands. Private IPs are **apartment numbers inside a gated complex** — unique among neighbors, meaningless to the city post office until the front desk ([[Routers]] doing [[PAT-NAT-Overload]]) rewrites the envelope.

## Why it matters

Almost every home and enterprise [[LAN]] uses private IPv4. Misunderstanding “I have an IP” vs “I have a *public* IP” breaks VPN design, ACLs, hairpin NAT, and cloud allow‑lists. Interviewers love RFC1918 + “can private IPs go on the Internet?”

## Deep dive

### Mental model

```text
Internet  ◄──── public IPs (ISP / RIR space) ────►
                 │
              edge NAT / firewall
                 │
Intranet  ◄──── RFC1918 private IPs ────► hosts
```

### RFC1918 private IPv4 blocks

| Range | CIDR | Common use |
|-------|------|------------|
| `10.0.0.0` – `10.255.255.255` | `10.0.0.0/8` | Large enterprises |
| `172.16.0.0` – `172.31.255.255` | `172.16.0.0/12` | Labs / mid‑size |
| `192.168.0.0` – `192.168.255.255` | `192.168.0.0/16` | Home routers |

Related “not public Internet” spaces (know of them):

| Space | Role |
|-------|------|
| `127.0.0.0/8` | Loopback |
| `169.254.0.0/16` | Link‑local (APIPA) |
| `100.64.0.0/10` | **CGNAT** (RFC6598) shared transition space |
| Multicast / reserved | Not unicast host addressing |

### Public space

Public IPv4 is allocated via RIRs (ARIN, RIPE, APNIC, …) to ISPs and orgs. Your home “WAN IP” may be:

1. A unique public address, or
2. A **CGNAT** address (`100.64/10`) shared behind *another* layer of carrier NAT.

```bash
curl -4 ifconfig.me
# then check if result is RFC1918 or 100.64.0.0/10 → you're behind NAT/CGNAT
```

### IPv6 angle

IPv6 typically uses **global unicast** (`2000::/3`) on the Internet and Unique Local Addresses (`fc00::/7`, commonly `fd00::/8`) for private‑like internals — different story than RFC1918 + NAT overload. See [[IPv4-vs-IPv6]].

### On the wire / fields

Private vs public is a **policy/routing convention**, not a magic bit in the header. A packet with `10.1.1.1` as source can physically leave your NIC; the ISP should drop/refuse to route it on the global Internet. NAT changes the source field at the edge so replies can return.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet (L3) | Which addresses may be globally routed |
| Ops / design | Edge | NAT, VPN, allow‑lists key off public vs private |

## Lab exercises

### Lab 1 — Classify your addresses

```bash
ip -4 addr          # or ifconfig
ip route | head
curl -4 ifconfig.me
```

Label each address: private / loopback / link‑local / public / CGNAT.

### Lab 2 — Trace NAT boundary

From a LAN host, compare:

```bash
# Inside address
ip -4 addr show | grep inet

# Outside address seen by Internet
curl -4 ifconfig.me
```

If they differ, you are behind NAT (home PAT or CGNAT). Sketch where rewrite happens.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| VPN overlap | Same RFC1918 on both sides | change LAN subnet; see [[Subnet-Masks]] |
| Cloud allow‑list fails | Listed private IP | use egress public / CGNAT reality |
| “Public” service unreachable | Port forward / firewall | WAN IP, CGNAT (can’t port‑forward easily) |
| Asymmetric mental model | Hairpin NAT needed | client uses public VIP from inside |

## Common traps / interview gotchas

- Private IPs **can** be routed *inside* your AS — “non‑routable” means **not on the public Internet**, not “routers refuse them always.”
- `172.32.0.0` is **not** RFC1918 (only `172.16/12`).
- CGNAT `100.64/10` looks public‑ish but isn’t unique Internet space — breaks inbound connections.
- Two companies both using `10.0.0.0/8` will feel pain on merger/VPN — plan overlapping RFC1918.
- IPv6 ULA ≠ “never needs security”; still filter.

## Mastery checklist

- [ ] Recite all three RFC1918 blocks with CIDR masks
- [ ] Explain why home LANs reuse `192.168.1.0/24`
- [ ] Detect CGNAT vs unique public WAN IP
- [ ] Connect private addressing to [[PAT-NAT-Overload]]
- [ ] Spot VPN overlap as an addressing design failure

## Related notes

- [[IP Address]] · [[IPv4-vs-IPv6]] · [[NAT-vs-PAT]] · [[PAT-NAT-Overload]] · [[Static-vs-Dynamic-NAT]] · [[Routers]] · [[LAN]] · [[VPN]]
- ← [[02-IP-Addressing/Index|IP Addressing]]
