---
tags: [basic-terminology, networking, ccna, protocol]
aliases: [Network Protocol, Communications Protocol]
layer: All (definition is cross-layer)
---

# Protocol

## Learning objectives

- Define what a protocol is (syntax, semantics, timing)
- Explain standards (RFCs, IEEE) vs vendor implementations
- Place major protocols in the TCP/IP model
- Reason about protocol layering and encapsulation

## One-sentence definition

> A **protocol** is an agreed set of rules that defines message formats (**syntax**), meanings (**semantics**), and the sequencing/timing of exchanges so two or more parties can communicate unambiguously.

## Analogy

> A protocol is a **shared board game rulebook**: what pieces look like (syntax), what moves mean (semantics), and whose turn it is (timing). Without the same rulebook, two devices are just making noise.

## Why it matters

Without protocols, interoperability dies. Your entire career is “which protocol is misbehaving, at which layer, under which constraints?” Mastery means knowing not just names, but **state machines**, **failure modes**, and **what is guaranteed vs best-effort**.

## Deep dive

### Mental model — three ingredients

1. **Syntax** — bit layouts, fields, encodings (headers)
2. **Semantics** — what fields mean (ACK number, opcode)
3. **Timing / procedure** — who sends what when (handshake, retries, timeouts)

Example: [[TCP]] specifies segment layout, meaning of flags, and connection state machine.

### Layered protocols

| Layer (TCP/IP) | Example protocols |
|----------------|-------------------|
| Application | [[HTTP-HTTPS|HTTP]], [[DNS]], [[SSH]], [[DHCP]], [[SMTP-IMAP|SMTP]] |
| Transport | [[TCP]], [[UDP]] |
| Internet | IP, [[ICMP]], [[ARP]] (ARP is link-adjacent but critical to IPv4 LAN) |
| Link / Network Access | Ethernet, Wi-Fi (802.11), PPP |

Lower layers offer services to upper layers; upper layers **encapsulate** their PDUs in lower-layer PDUs ([[Packet]], [[Frame]]).

### Standards vs dialects

- **RFCs** (IETF): TCP, IP, TLS, HTTP
- **IEEE**: Ethernet, Wi-Fi
- Vendors extend with proprietary options — still must interoperate on the wire for the core.

### On the wire / fields

“Protocol” appears literally in the IPv4 header **Protocol** field (e.g. 6=TCP, 17=UDP, 1=ICMP). At other layers, demux uses EtherType, UDP/TCP ports, TLS ALPN, HTTP Host/SNI, etc.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Both | Every layer | Each layer runs one or more protocols |
| OSI | 1–7 | Finer split (presentation/session) — TLS often mapped to presentation |

## Lab exercises

### Lab 1 — Identify protocols in a capture

```bash
sudo tcpdump -ni en0 -c 30
# Classify: ARP, DNS/UDP/53, HTTPS/TCP/443, ICMP, etc.
```

### Lab 2 — Same app, different protocols

```bash
curl http://example.com  -o /dev/null
curl https://example.com -o /dev/null
# HTTP vs HTTP over TLS — different wire protocols below the URL scheme
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Intermittent app failures | Protocol mismatch / middlebox | versions, ALPN, DPI breaking traffic |
| “Protocol unreachable” ICMP | IP proto blocked | ICMP type 3 code 2 |
| Works in tool A not B | Different protocol profile | cipher suites, HTTP version, IPv6 |

## Common traps / interview gotchas

- OSI is a **teaching model**; Internet uses TCP/IP. Don’t force every technology into seven layers pedantically — but *do* know the mapping questions for exams.
- Proprietary “protocols” still ride on IP/TCP.
- Versioning (TLSv1.0 disabled) is a protocol compatibility problem, not “routing.”

## Mastery checklist

- [ ] Define protocol using syntax/semantics/timing
- [ ] Map 10 common protocols to TCP/IP layers
- [ ] Explain encapsulation with a concrete HTTP GET example
- [ ] Identify protocol from IP proto + ports in a capture

## Related notes

- [[Packet]] · [[Frame]] · [[Port]] · [[Socket]] · [[TCP]] · [[UDP]] · [[ICMP]]
- [[HTTP-HTTPS]] · [[DNS]] · [[SSL-TLS]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
