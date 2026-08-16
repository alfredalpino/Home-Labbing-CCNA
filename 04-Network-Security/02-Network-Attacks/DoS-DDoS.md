---
tags: [network-security, attacks, networking, ccna, dos, ddos]
aliases: [DoS, DDoS, Denial of Service, Distributed Denial of Service, DoS & DDoS]
layer: Availability threat
---

# DoS & DDoS

## Learning objectives

- Define DoS vs DDoS clearly
- Classify volumetric, protocol, and application-layer floods at awareness level
- Recognize symptoms vs “just a busy Monday”
- Know defensive controls network engineers actually use

## One-sentence definition

> **DoS** (Denial of Service) makes a service unavailable to legitimate users; **DDoS** is the same goal using **many distributed sources**, amplifying scale and making simple IP blocks ineffective.

## Analogy

> DoS is **one person jamming a store’s doorway**. DDoS is a **flash mob of thousands blocking every entrance and the street outside**. Staff can’t tell shoppers from blockers easily; calling one police car (blocking one IP) does nothing — you need crowd control, bigger roads, and filters that recognize stampede patterns.

## Why it matters

Availability is a security property (CIA triad). Outages from floods look like “network is down” and hit routers, firewalls, DNS, and apps. You will help triage even if a scrubbing provider does the heavy lift.

## Deep dive

### Mental model

```text
Attack traffic + legit traffic → target link / state tables / CPU / app
Defense: detect → divert/scrub/absorb → restore → postmortem
```

### Common categories (awareness — not a how-to)

| Category | Targets roughly | Defensive idea |
|----------|-----------------|----------------|
| Volumetric | Link bandwidth | Provider scrubbing, anycast, capacity |
| Protocol / state | Firewalls, LB, stacks | SYN cookies, state limits, ACLs |
| Application | HTTP/DNS/app logic | WAF/rate limits, caching, scale |

### What you will observe

- Sudden saturation of WAN/Internet link
- State table exhaustion on [[Stateful Inspection Firewall]] / NGFW
- High CPS (connections per second), unusual geo spread
- Collateral damage to other services on shared edges

### Defensive controls (engineer toolkit)

| Control | Role |
|---------|------|
| Upstream blackhole / flowspec | Provider drops |
| CDN / anycast scrubbing | Absorb & filter |
| Rate limiting / policing | Buy time |
| ACL / SG tighten | Reduce exposure |
| Anycast DNS / hardened DNS | Protect name plane |
| Architecture | Separate critical planes, capacity headroom |

### On the wire

Captures may show floods; often links are too melted to capture usefully on-box — use NetFlow/sFlow, interface counters, provider portals.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Cross-layer | L3–L7 | Different floods hit different layers |
| Ops | Availability | Detection + mitigation process |

## Lab exercises

### Lab 1 — Baseline so you can spot abnormal

```bash
ping -c 20 1.1.1.1
# Document normal RTT/loss to key VIPs in your lab
```

### Lab 2 — Playbook writing (no attack)

Write a 1-page triage: who to call (ISP/CDN), what graphs to screenshot, what to avoid (random ACL panic without metrics).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Everything external slow | Link flood / peering | interface util, provider DDoS status |
| New connections fail, old OK | State exhaustion | firewall session counts |
| One website only | App-layer flood | WAF/CDN analytics |
| DNS intermittent | DNS query flood | recursive/auth metrics |

## Common traps / interview gotchas

- Not every outage is DDoS — validate with traffic analytics.
- Hosting a /24 doesn’t mean you can “absorb” modern floods alone.
- Blocking ICMP “for security” doesn’t stop DDoS and may hurt diagnostics.
- Sharing attack tooling or practicing floods on third-party networks is illegal/harmful — lab only on systems you own with permission.

## Mastery checklist

- [ ] Define DoS vs DDoS with flash-mob analogy
- [ ] Name three flood categories at awareness level
- [ ] List four defensive controls
- [ ] Draft a triage call tree for your lab/home ISP scenario

## Related notes

- [[Stateful Inspection Firewall]] · [[Next-Generation Firewall]] · [[Web Application Firewall]] · [[DNS]] · [[Bandwidth]] · [[ACLs]]
- ← [[02-Network-Attacks/Index|Network Attacks]] · [[04-Network-Security/Index|Network Security]]
