---
tags: [application-protocols, networking, ccna, http, https]
aliases: [HTTP, HTTPS, Hypertext Transfer Protocol]
layer: Application (HTTPS = HTTP over TLS)
---

# HTTP / HTTPS

## Learning objectives

- Explain HTTP as a request/response application protocol over [[TCP]] (usually)
- Read methods, status codes, and critical headers fluently
- Understand what HTTPS adds ([[SSL-TLS]]) including SNI and certificates
- Debug with `curl -v` and captures like a network engineer

## One-sentence definition

> **HTTP** is the application protocol that transfers web resources using requests and responses; **HTTPS** is HTTP secured by **TLS** on the wire (commonly TCP/443).

## Analogy

> HTTP is **ordering from a catalog by filling a form** (methods, headers, URLs). HTTPS is the same form slid through a **sealed pneumatic tube** ([[SSL-TLS]]) so eavesdroppers on the street can’t read your order — they may still see *that* you visited the shop (IP/SNI).

## Why it matters

APIs, health checks, package repos, cloud control planes, and captive portals are HTTP. “Website down” decomposes into DNS → TCP → TLS → HTTP. You must know which layer failed.

## Deep dive

### Mental model

```text
Client                  Server
  TCP connect (80 or 443)
  [TLS handshake if HTTPS]
  HTTP request  ─────────►
  ◄──────────── HTTP response
```

### Mechanism — request line & response line

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: curl/8.x
Accept: */*

HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
```

**Methods:** GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS (know semantics at ops level).  
**Status codes:** 1xx informational, 2xx success, 3xx redirect, 4xx client, 5xx server — memorize 200, 301/302, 304, 400, 401, 403, 404, 502, 503, 504.

**Host header / virtual hosting:** many sites share one IP; Host selects which site.  
**HTTPS SNI:** ClientHello carries hostname so VIP can present the right certificate.

### Versions (ops view)

| Version | Notes |
|---------|-------|
| HTTP/1.0 | Short-lived connections historically |
| HTTP/1.1 | Keep-alive, pipelining issues; still everywhere |
| HTTP/2 | Multiplexed streams over one TCP; binary framing |
| HTTP/3 | QUIC over [[UDP]] — evolves around TCP ossification |

### On the wire

- HTTP cleartext: TCP/80 (or any port)
- HTTPS: TLS records on TCP/443; HTTP inside after handshake

```bash
curl -v http://example.com/ -o /dev/null
curl -vI https://example.com/
openssl s_client -connect example.com:443 -servername example.com </dev/null | head
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | HTTP semantics |
| TCP/IP | + TLS | Presentation-ish security for HTTPS |
| OSI | 7 (+6 for TLS) | App (+ presentation) |

## Lab exercises

### Lab 1 — Trace failure layer

```bash
dig example.com +short
nc -vz example.com 443
curl -vI https://example.com/
```

### Lab 2 — See redirects and headers

```bash
curl -vI http://neverssl.com/
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| TCP OK, TLS fail | Cert/SNI/cipher | `openssl s_client`, clock ([[NTP]]) |
| TLS OK, 502/504 | Upstream origin / proxy | reverse proxy logs |
| 403 from CDN | WAF / geo / auth | request headers, IP reputation |
| Works in browser not curl | SNI/HTTP2/cookies | flags, ALPN |

## Common traps / interview gotchas

- HTTPS encrypts HTTP — middleboxes see SNI (unless ECH) and IPs/ports, not URLs/paths.
- “Port 443 open” ≠ “site healthy.”
- Captive portals intercept HTTP; HTTPS fails oddly until portal auth.
- gRPC and many APIs are HTTP/2 semantics on 443.

## Mastery checklist

- [ ] Map URL → DNS → TCP → TLS → HTTP
- [ ] Interpret 301 vs 302 vs 304 vs 502
- [ ] Explain Host vs SNI
- [ ] Use curl -v to isolate the failing step

## Related notes

- [[SSL-TLS]] · [[TCP]] · [[DNS]] · [[Port]] · [[Socket]] · [[NTP]]
- ← [[01-Web-and-Security/Index|Web & Security]] · [[03-Application-Protocols/Index|Application Protocols]]
