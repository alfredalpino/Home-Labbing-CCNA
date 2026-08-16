---
tags: [network-security, firewalls, networking, ccna, waf]
aliases: [WAF, Web Application Firewall]
layer: Application (HTTP/HTTPS)
---

# Web Application Firewall

## Learning objectives

- Define WAF as HTTP(S)-centric application protection
- Know common protections (OWASP-ish categories) at awareness level
- Contrast WAF vs [[Next-Generation Firewall]] vs [[Proxy Firewall]]
- Troubleshoot false positives that break apps

## One-sentence definition

> A **web application firewall (WAF)** inspects and filters **HTTP/HTTPS application traffic** to block common web exploits and abuse (injection, path attacks, bots, etc.), usually as a reverse-proxy or cloud front door.

## Analogy

> An NGFW is the **city wall**. A WAF is the **nightclub doorman who understands the guest list language** for one club (your web app): they read the request (“ticket type,” weird characters in the name field, suspiciously huge coats) and bounce exploit-shaped behavior — even if the person already passed the city gate on port 443.

## Why it matters

Public web apps get scanned constantly. Network allow-443 is necessary but nowhere near sufficient. Engineers collaborate with app/security teams when WAF rules break releases.

## Deep dive

### Mental model

```text
Client ──HTTPS──► WAF / CDN edge ──► Origin app servers
                 inspect HTTP semantics
```

### Typical controls (awareness)

| Category | Examples of intent |
|----------|--------------------|
| Injection defenses | Block obvious SQLi/XSS patterns |
| Protocol compliance | Weird methods/headers |
| Rate limiting / bots | Credential stuffing slowing |
| Geo/IP reputation | Coarse allow/deny |
| Virtual patching | Buy time before code fix |

### WAF vs NGFW

| | WAF | NGFW |
|-|-----|------|
| Focus | Web apps | Networks/segments |
| Sweet spot | HTTP(S) | Mixed ports/apps |
| Placement | App front door | Perimeter/segmentation |

### On the wire

Often TLS terminates at WAF/CDN; origin may see HTTP or re-encrypted HTTPS. Logs show rule IDs, not just 5-tuples.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Application | HTTP | Primary |
| Depends on | [[SSL-TLS]] | Visibility |

## Lab exercises

### Lab 1 — Placement drawing

Draw Internet → WAF → LB → app. Mark where certs live.

### Lab 2 — False positive drill

App upgrade fails only through WAF: list log fields you’d collect (rule ID, URL, payload snippet policy-safe).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| 403 from edge | WAF rule | rule ID, exception process |
| Works direct to origin | WAF/CDN path | DNS to WAF, headers |
| Uploads fail | Size/body inspection limits | limits, file rules |

## Common traps / interview gotchas

- WAF ≠ secure application by itself (authZ bugs remain).
- Encrypted origins without decrypt still limit some inspections.
- “Cloudflare/Akamai in front” often includes WAF features — know the layer.

## Mastery checklist

- [ ] Nightclub-doorman analogy vs city wall
- [ ] Place WAF on a web architecture sketch
- [ ] Contrast WAF vs NGFW
- [ ] Describe a false-positive handling approach

## Related notes

- [[HTTP-HTTPS]] · [[SSL-TLS]] · [[Proxy Firewall]] · [[Next-Generation Firewall]] · [[IDS IPS]]
- ← [[01-Firewalls/Index|Firewalls]] · [[04-Network-Security/Index|Network Security]]
