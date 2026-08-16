---
tags: [application-protocols, networking, ccna, tls, ssl]
aliases: [TLS, SSL, Transport Layer Security]
layer: Presentation / security layer above TCP
---

# SSL / TLS

## Learning objectives

- Explain TLS as the encryption/authentication layer under HTTPS and other apps
- Understand certificates, chains of trust, and validation failures
- Know handshake goals (confidentiality, integrity, auth) without becoming a cryptographer
- Relate clock sync ([[NTP]]) and SNI to real outages

## One-sentence definition

> **TLS** (Transport Layer Security), historically called **SSL**, is a cryptographic protocol that provides encryption, integrity, and authentication for application data — most famously wrapping HTTP to make [[HTTP-HTTPS|HTTPS]].

## Analogy

> TLS is a **tamper-evident sealed courier pouch with ID check**: before secrets move, both sides agree on locks (keys/ciphers) and you verify the courier’s badge (certificate) against a trusted issuer list. HTTP then rides inside the pouch.

## Why it matters

Certificate expiry, broken chains, wrong clocks, and TLS version mismatches cause high-severity outages that look like “network is down.” Engineers must isolate: TCP up, TLS fail, HTTP never starts.

## Deep dive

### Mental model

```text
App bytes → TLS records → TCP → IP
         ▲
   Handshake establishes keys + verifies identity (usually server cert)
```

### Mechanism — what the handshake achieves

1. Agree version/ciphers (TLS 1.2 / 1.3)
2. Establish shared secrets (forward secrecy with ephemeral key exchange)
3. Authenticate server via X.509 certificate (client auth optional)
4. Protect application data with AEAD ciphers

**Certificate chain:** leaf → intermediate(s) → trusted root in client store.  
**SNI:** hostname in ClientHello for cert selection on shared IPs.  
**ALPN:** negotiates HTTP/1.1 vs h2, etc.

### SSL vs TLS naming

“SSL” is legacy branding. Modern protocols are TLS 1.2/1.3. Disable ancient SSL/TLS versions.

### On the wire

```bash
openssl s_client -connect example.com:443 -servername example.com -tls1_2
curl -vI https://example.com/
# Look for: verify return code, certificate chain, protocol version
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI | 6 (Presentation) approx. | Encryption/encoding |
| TCP/IP | Between transport & app | Security sublayer |

## Lab exercises

### Lab 1 — Inspect a live cert

```bash
echo | openssl s_client -showcerts -servername example.com -connect example.com:443 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

### Lab 2 — Break trust intentionally (thought)

Wrong system date → cert “not yet valid” / “expired.” Sync with [[NTP]].

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Cert expired | Lifecycle miss | dates, automation |
| Unknown CA | Missing intermediate | full chain on server |
| Name mismatch | Wrong cert/SNI | SAN vs URL host |
| Protocol alert | Version/cipher mismatch | openssl, client policy |

## Common traps / interview gotchas

- Padlock ≠ “site is safe from all threats” — only channel security + identity of cert subject.
- TLS interception (corp proxy) requires trusting enterprise CA on clients.
- TLS 1.3 reduces round trips — latency sensitive.
- Client certificates exist (mTLS) in zero-trust designs.

## Mastery checklist

- [ ] Separate TCP success from TLS success from HTTP success
- [ ] Read subject/issuer/dates from a cert
- [ ] Explain SNI and chain of trust
- [ ] Link NTP failure to TLS validation failure

## Related notes

- [[HTTP-HTTPS]] · [[TCP]] · [[NTP]] · [[DNS]] · [[SSH]]
- ← [[01-Web-and-Security/Index|Web & Security]] · [[03-Application-Protocols/Index|Application Protocols]]
