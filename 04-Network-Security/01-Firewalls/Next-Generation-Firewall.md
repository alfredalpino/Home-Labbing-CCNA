---
tags: [network-security, firewalls, networking, ccna]
aliases: [NGFW, Next Generation Firewall, Next-Gen Firewall]
layer: L3–L7 + identity/threat intel
---

# Next-Generation Firewall

## Learning objectives

- Define NGFW beyond “stateful + marketing”
- Name core NGFW capabilities (App-ID, user-ID, IPS, URL, intel)
- Contrast with [[Stateful Inspection Firewall]] and [[Web Application Firewall]]
- Know operational costs: SSL decryption, false positives, tuning

## One-sentence definition

> A **next-generation firewall (NGFW)** combines stateful firewalling with **application awareness**, **user/identity awareness**, integrated threat prevention ([[IDS IPS]]), and often URL/DNS filtering and threat intelligence — enforcing policy on *what* and *who*, not only ports.

## Analogy

> Classic stateful firewalls check whether you’re on the guest list and carrying a valid ticket stub (ports/sessions). An NGFW is airport security that also asks **which airline app you’re using**, **who your employee badge says you are**, scans bags for known threats, and checks a watchlist — even if your ticket says “gate 443.”

## Why it matters

Port 443 carries almost everything now. Port-based allow lists failed; App-ID and decryption debates dominate enterprise designs. CCNA-level engineers must speak NGFW capabilities even if specialists tune signatures.

## Deep dive

### Capability stack (typical)

| Capability | Purpose |
|------------|---------|
| Stateful base | Session tracking |
| Application identification | Distinguish Slack vs malware C2 on 443 |
| User/group policy | Map to directory identity |
| IPS/AV | Known exploit/malware patterns |
| URL/DNS filtering | Category policy |
| SSL/TLS decryption | See inside HTTPS (privacy/legal tradeoffs) |
| Threat intel feeds | Block known-bad IPs/domains |

### NGFW vs WAF

- **NGFW**: network perimeter / segmentation workhorse
- **[[Web Application Firewall]]**: specialized HTTP(S) app protection (OWASP-ish)

They often coexist.

### On the wire

Without decryption, NGFW still uses SNI, cert attributes, behavioral heuristics, IP intel. With decryption, it can see HTTP hosts/paths — powerful and sensitive.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Cross-layer | L3–L7 | Policy + inspection |
| Identity | Outside classic OSI | Directory integration |

## Lab exercises

### Lab 1 — Port vs app thought

List five apps that use TCP/443. Explain why `allow 443` is not a security policy.

### Lab 2 — Decrypt decision memo

Write 5 bullets: when decrypt, when not (banking, privacy, performance, legal).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| App broken only through NGFW | App-ID / IPS false positive | logs, exception, signature |
| Perf collapse | Decrypt + IPS CPU | hardware offload, exclusions |
| Intermittent TLS errors | Interception cert not trusted | client trust store |

## Common traps / interview gotchas

- Buying NGFW and leaving it in “port mode” wastes money.
- Encrypted traffic visibility requires deliberate decrypt architecture.
- NGFW ≠ Zero Trust by itself — see [[Zero Trust Architecture]].

## Mastery checklist

- [ ] Airport-security analogy
- [ ] Name five NGFW capabilities
- [ ] Contrast NGFW vs stateful vs WAF
- [ ] Explain TLS decrypt tradeoffs

## Related notes

- [[Stateful Inspection Firewall]] · [[Web Application Firewall]] · [[IDS IPS]] · [[SSL-TLS]] · [[HTTP-HTTPS]] · [[Zero Trust Architecture]]
- ← [[01-Firewalls/Index|Firewalls]] · [[04-Network-Security/Index|Network Security]]
