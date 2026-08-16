---
tags: [application-protocols, networking, ccna, email, smtp, imap]
aliases: [SMTP, IMAP, Email Protocols]
layer: Application
---

# SMTP / IMAP

## Learning objectives

- Separate mail *submission/transport* (SMTP) from mail *retrieval/access* (IMAP)
- Know critical ports and STARTTLS vs implicit TLS patterns
- Trace a message path MUA → MSA/MTA → destination
- Spot DNS dependencies (MX, SPF/DKIM/DMARC at awareness level)

## One-sentence definition

> **SMTP** moves email between clients and servers (and server-to-server); **IMAP** lets a client access and manage messages stored on a mail server — together they are the core “send” and “read” protocols of Internet email.

## Analogy

> SMTP is the **postal truck that moves letters between post offices**. IMAP is your **PO box browser** — leave mail on the server, sync folders to phone and laptop. Mixing them up is like trying to read your PO box by stuffing letters into a departing truck.

## Why it matters

Phishing, spam relays, and “email down” incidents are network + DNS + auth problems. Port 25 blocked on residential ISPs, TLS requirements, and MX misconfig are everyday ops.

## Deep dive

### Mental model

```text
Compose (MUA)
  ─SMTP submission (587/465)─► Mail server (MSA)
  ─SMTP relay (25)───────────► Destination MX (MTA)
Mailbox stored
  ◄─IMAP (143/993)──────────── MUA reads/syncs
```

**POP3** (110/995) is download-oriented legacy; IMAP is the modern multi-device accessor.

### Ports (ops table)

| Protocol | Port | Notes |
|----------|------|-------|
| SMTP relay | 25 | Server-to-server; often blocked on consumer networks |
| SMTP submission | 587 | Authenticated client submit + STARTTLS |
| SMTPS | 465 | Implicit TLS submission (common) |
| IMAP | 143 | STARTTLS possible |
| IMAPS | 993 | Implicit TLS |

### Security / abuse awareness

- Open relays = weaponized spam — never run one.
- SPF/DKIM/DMARC = DNS-published email auth (engineer awareness).
- StartTLS upgrades cleartext to TLS mid-session — opportunistic vs required.

### On the wire

```bash
nc -vz smtp.gmail.com 587
openssl s_client -connect imap.gmail.com:993 -quiet
# Full mail lab needs an account; focus on port/TLS/DNS MX checks
dig example.com MX +short
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Messaging |
| Transport | TCP | ports above |

## Lab exercises

### Lab 1 — MX lookup

```bash
dig cisco.com MX +short
dig $(dig cisco.com MX +short | awk '{print $2}' | head -1) A +short
```

### Lab 2 — Port reachability from your network

```bash
nc -vz -w 3 8.8.8.8 25 || true
# Many networks block outbound 25 — explain why
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Can’t send | Auth/TLS/port | 587 vs 25, credentials, cert |
| Can’t receive | MX/DNS/firewall | MX records, A/AAAA of MX, graylist |
| Intermittent | Reputation/RBL | SMTP logs, reverse DNS |
| IMAP sync issues | Idle / proxy | client logs, TLS inspection |

## Common traps / interview gotchas

- SMTP delivers *to servers*; IMAP is not used server-to-server for relay.
- Blocking ICMP won’t stop spam; blocking open relay and auth abuse will.
- “Email uses UDP” — false; these are TCP protocols (except some side services).

## Mastery checklist

- [ ] Draw MUA/MSA/MTA path
- [ ] Recite 25/587/465/143/993
- [ ] Lookup MX and explain next query
- [ ] Contrast IMAP vs POP3 briefly

## Related notes

- [[DNS]] · [[TCP]] · [[SSL-TLS]] · [[Port]] · [[HTTP-HTTPS]]
- ← [[05-Email/Index|Email]] · [[03-Application-Protocols/Index|Application Protocols]]
