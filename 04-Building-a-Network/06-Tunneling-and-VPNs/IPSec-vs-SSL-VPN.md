---
tags: [vpn, tunneling, networking, ccna, ipsec, ssl-vpn]
aliases: [IPsec vs SSL VPN, IPSec vs SSL, IPsec VPN, SSL VPN]
layer: Overlay / security
---

# IPSec-vs-SSL-VPN

## Learning objectives

- Contrast IPsec VPN and SSL/TLS VPN by layer, client experience, and typical use
- Map each to site-to-site vs remote-access patterns (see [[Site-to-Site-vs-Remote-Access]])
- Know common ports and NAT-T behavior at CCNA depth
- Troubleshoot “tunnel up, apps fail” for both families

## One-sentence definition

> **IPsec** protects IP packets with network-layer security associations; **SSL VPN** (really [[SSL-TLS]]-based) protects user sessions—often via client or portal—typically over TCP/443, trading different deployability and policy models for similar “private over public” goals as [[VPN]].

## Analogy

> Both are **sealed capsules on the public subway** ([[VPN]] analogy).  
> **IPsec** is a **hardened freight container** bolted around every crate (IP packet) — great for warehouse-to-warehouse (site) and full-device tunnels.  
> **SSL VPN** is a **personal security briefcase** you carry through the passenger gate (HTTPS/443) — IT loves it when hotels block weird UDP, and users get app or portal access without rewriting the whole freight system.

## Why it matters

CCNA and job screens ask “IPsec or SSL VPN?” The answer is use-case: site crypto and always-on network tunnels lean IPsec; user-friendly remote access and firewall-friendly 443 lean SSL VPN. Many vendors offer both.

## Deep dive

### Mental model

```text
IPsec (typical):
  Host/Site -- ESP/AH (+ IKE) -- Peer
  Outer IP + ESP; inner original IP packet
  Ports: UDP 500 (IKE), UDP 4500 (NAT-T), IP proto 50 (ESP)

SSL VPN (typical):
  User -- TLS -- Portal/gateway (TCP 443)
  Then: full tunnel adapter OR clientless portal apps OR DTLS data plane
```

### Mechanism — comparison

| Dimension | IPsec | SSL / TLS VPN |
|-----------|-------|----------------|
| Layer vibe | L3 packet protection | Session/app or tunneled L3 over TLS |
| Clients | Network OS / hardware | Agent or browser portal |
| Firewall traversal | UDP 500/4500; ESP may break | Usually TCP/443 — easier |
| Site-to-site | Excellent (IKEv2 common) | Less common as pure site |
| Remote access | Always-on / AnyConnect-style IPsec modes exist | Very common |
| Standards | IKE + ESP (IPsec suite) | TLS ([[SSL-TLS]]) productized as “SSL VPN” |

**IPsec phases (classic story):** IKE negotiates SA (auth, DH, proposals) → ESP protects data. IKEv2 simplified lifetimes/rekey vs IKEv1.

**SSL VPN modes:** clientless (portal), thin client, full tunnel (virtual adapter) — products differ.

### On the wire

- IPsec: look for ISAKMP/IKE and ESP; behind NAT expect UDP encapsulation (NAT-T).  
- SSL VPN: TLS handshake to concentrator; may switch to DTLS for data. Inner traffic may be IP or proxied HTTP.

## Relationship to OSI / TCP-IP

| Model | IPsec | SSL VPN |
|-------|-------|---------|
| Primary | Internet layer (packet) | Session/presentation (TLS) + often tunneled L3 |
| Underlay | Any IP path | Usually HTTPS-friendly path |
| Related note | [[VPN]] | [[SSL-TLS]] |

## Lab exercises

### Lab 1 — Compare reachability requirements

On paper or GNS3 firewall ACL: allow only TCP/443 vs allow UDP 500/4500 + ESP. Predict which remote-user hotel Wi‑Fi breaks IPsec but allows SSL VPN.

### Lab 2 — Observe adapters / routes (real client)

Connect a corporate or lab SSL VPN; note tunnel interface and routes. If you have an IPsec client lab (strongSwan / Cisco), compare `ip route` and MTU. Document split vs full tunnel.

```bash
ip addr; ip route; curl -I https://example.com
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| IKE fails | PSK/cert, proposal mismatch, UDP blocked | Phase1 propos, time ([[NTP]]), ACL |
| IPsec up, no traffic | Interesting traffic / NAT / routes | SA selectors, NAT-T, split tunnel |
| SSL VPN auth OK, apps fail | Split tunnel / DNS / MFA session | internal DNS, routes, portal bookmarks |
| Slow apps | MTU / TCP-over-TCP | lower MSS/MTU, prefer DTLS if available |

## Common traps / interview gotchas

- “SSL VPN” today is **TLS**; SSL is the legacy name.
- IPsec is not automatically a [[VPN]] product — it’s the crypto framework; policy defines the VPN.
- ESP alone struggles with NAT — NAT-T wraps ESP in UDP.
- Encrypted tunnels don’t fix bad underlay loss — see [[Latency]] / [[Bandwidth]].

## Mastery checklist

- [ ] Contrast IPsec vs SSL VPN with freight vs briefcase analogy
- [ ] List key ports/protocols for each
- [ ] Pick a technology for site-to-site vs user-from-hotel
- [ ] Link explanations to [[VPN]] and [[SSL-TLS]]

## Related notes

- [[VPN]] · [[SSL-TLS]] · [[Site-to-Site-vs-Remote-Access]] · [[GRE-IPSec-Tunnels]] · [[MPLS-VPN]] · [[WAN]]
- ← [[06-Tunneling-and-VPNs/Index|Tunneling & VPNs]] · [[04-Building-a-Network/Index|Building a Network]]
