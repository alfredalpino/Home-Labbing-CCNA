---
tags: [network-security, encryption, networking, ccna, cryptography]
aliases: [Encryption, Crypto Basics, Encryption Fundamentals]
layer: Cross-layer security property
---

# Encryption Basics

## Learning objectives

- Explain confidentiality, integrity, and authenticity in plain language
- Know where encryption sits (in transit vs at rest) for network engineers
- Relate to [[SSL-TLS]], [[SSH]], [[VPN]], and wireless security
- Avoid classic operational failures (clock skew, weak ciphers, broken trust)

## One-sentence definition

> **Encryption** transforms readable data into ciphertext so unauthorized parties cannot understand it; network engineers mostly operationalize **encryption in transit** (TLS, IPsec, SSH, Wi‑Fi) plus the trust systems (keys/certs) that make it safe.

## Analogy

> Encryption is a **lockable diary**. Anyone can see you carry a book ([[Packet]]s still have destinations), but without the key they can’t read the pages. A **certificate/PKI** is like a notary stamp proving the diary really belongs to the shop you meant to visit — not an impostor on the corner ([[SSL-TLS]] identity). Hashing/HMAC is a **wax seal** — you detect if pages were swapped.

## Why it matters

Cleartext protocols leak credentials and PII on shared networks. Most modern outages labeled “security” that hit neteng are TLS trust/cipher/SNI/MTU issues — not novel cryptanalysis.

## Deep dive

### CIA (ops framing)

| Goal | Rough meaning | Network examples |
|------|---------------|------------------|
| Confidentiality | Can’t read | TLS, IPsec, SSH |
| Integrity | Can’t alter undetected | TLS AEAD, hashes |
| Authenticity | Who are you talking to? | Certs, SSH host keys |

### In transit vs at rest

- **In transit:** protect on the wire ([[HTTP-HTTPS]], [[VPN]], [[SSH]])
- **At rest:** disks/backups (important, but different team ownership often)

### Symmetric vs asymmetric (enough for engineers)

| | Symmetric | Asymmetric |
|-|-----------|------------|
| Keys | Same shared secret | Public/private pair |
| Use | Bulk data encryption | Key exchange, signatures, identity |
| Everyday | AES inside TLS | Certificates, handshakes |

You don’t need to implement AES — you need to **configure and verify** it correctly.

### On the wire

Encrypted payloads look random; metadata often remains (IPs, ports, SNI, sizes, timing). Encryption ≠ anonymity.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Often | Presentation-ish / app security | TLS atop TCP |
| Also | Network | IPsec |

## Lab exercises

### Lab 1 — See identity, not just padlock

```bash
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Lab 2 — Break trust with time

Relate clock skew to cert validity — fix with [[NTP]].

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Cert expired / not yet valid | Time or lifecycle | dates, NTP |
| Unknown CA | Missing chain / intercept | intermediates, corp CA |
| Protocol alert | Version/cipher mismatch | TLS policy both sides |
| App OK on IP, fail on name | SNI/cert SAN | hostname |

## Common traps / interview gotchas

- HTTPS encrypts HTTP — path/query hidden; destination IP (and often SNI) not.
- “Encrypted” internal protocols still need authZ and patching.
- Double encryption (TLS inside TLS) can hurt MTU/performance.

## Mastery checklist

- [ ] Diary + wax seal + notary analogy
- [ ] Place TLS/SSH/IPsec on “in transit”
- [ ] Run openssl/curl identity checks
- [ ] Link NTP to encryption failures

## Related notes

- [[SSL-TLS]] · [[SSH]] · [[VPN]] · [[HTTP-HTTPS]] · [[NTP]] · [[Zero Trust Architecture]]
- ← [[04-Network-Security/Index|Network Security]]
