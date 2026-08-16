---
tags: [basic-terminology, networking, ccna, client]
aliases: [Network Client, Client Role]
layer: Application / End-system role
---
# Client

## Learning objectives

- Define the client role without confusing it with “PC” or “browser only”
- Explain client–server vs peer-to-peer interaction patterns
- Identify client behavior on the wire (who initiates, who listens)
- Lab: prove which side is the client using sockets and packet captures

## One-sentence definition

> A **client** is the process (or system role) that **initiates** a communication request toward a service that is waiting to accept connections or messages.

## Analogy

> A client is the **person who dials the phone**. The server is the call center that answers. Whoever starts the call (sends the first SYN / request) is the client for that conversation — even if that “person” is actually another server calling an API.

## Why it matters

Almost every protocol you troubleshoot is asymmetric at start time: someone dials, someone answers. Misidentifying which side is the client leads to wrong firewall rules (“I opened the server port but the return path is blocked”), wrong NAT expectations, and wrong packet-filter logic. In enterprise networks, “the client” is often a phone, IoT sensor, printer, or container — not a human at a laptop.

## Deep dive

### Mental model

Think **role**, not hardware.

| Role | Typical behavior |
|------|------------------|
| Client | Opens socket toward a known IP/name + port; often ephemeral source port |
| Server | Binds/listens on a well-known or configured port; accepts many clients |

The same machine can be both: your laptop is a **client** to `8.8.8.8:53` ([[DNS]]) and a **server** if you run a local web app on `:8080`.

### Mechanism

1. Application decides it needs a service (resolve name, fetch URL, open SSH).
2. OS creates a socket ([[Socket]]), usually choosing an ephemeral [[Port]].
3. For [[TCP]]: client sends `SYN` to server’s listening port → handshake → request data.
4. For [[UDP]]: client sends a datagram to the destination port (e.g. DNS query); “session” is logical, not handshake-based.
5. Response traffic returns to the client’s IP + ephemeral port (stateful firewalls track this).

**Client–server** = clear initiator/responder.  
**Peer-to-peer** = both sides can initiate (BitTorrent, some SIP setups); still, *each transaction* has an initiator.

### Thin vs thick clients

- **Thin client**: mostly display/input; heavy work on server (VDI, browser apps).
- **Thick client**: significant local logic (native apps, some desktop agents).

Network engineers care less about UI thickness and more about: ports used, idle timers, proxy requirements, and certificate pinning.

### On the wire / fields

There is no “client bit” in IP. You infer client from:

- Who sent the first packet of the flow
- Who has the well-known destination port (often the server)
- Socket state: `ESTABLISHED` with local ephemeral port → usually client

Example TCP 5-tuple (client → web server):

```text
src 192.0.2.10:53122  dst 203.0.113.5:443  proto TCP
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Client process implements app protocol ([[HTTP-HTTPS]], [[SSH]], …) |
| TCP/IP | Transport | Client selects TCP/UDP and source port |
| OSI | 5–7 | Session/presentation/application behaviors live in client software |
| OSI | 4 | Transport endpoints |

## Lab exercises

### Lab 1 — See yourself as a client

```bash
# macOS/Linux: list established TCP as client to HTTPS
ss -tan | grep ':443'    # Linux
netstat -an | grep '\.443 '  # macOS

curl -v https://example.com -o /dev/null
```

Note: destination port `443`, source port random high number.

### Lab 2 — Capture the initiator

```bash
sudo tcpdump -ni any 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0'
# Then curl a site. SYN without ACK = client starting handshake.
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| “Server unreachable” but ping works | Client blocked to service port / wrong VIP | `curl -v`, firewall, listener on server |
| Works on Wi-Fi, fails on corp LAN | Proxy required for clients | Explicit proxy, PAC, transparent proxy |
| Intermittent client timeouts | NAT/firewall idle timeout shorter than app | Keepalives, idle timers, stateful ACL |
| App says “connection refused” | Nothing listening on target (or RST) | Server process, correct IP/port |

## Common traps / interview gotchas

- Client ≠ PC. Servers are often clients too (API calls, LDAP binds, syslog forwarding).
- Destination port identifies the *service*, not which host is “more important.”
- In active [[FTP-SFTP|FTP]], the *server* may initiate the data connection back to the client — classic firewall breaker.
- Reverse connections / callbacks in security tooling still follow client=initiator of that TCP session.

## Mastery checklist

- [ ] Explain client vs server using only “who initiates” and “who listens”
- [ ] Read a 5-tuple and identify the likely client
- [ ] Capture a SYN and explain why that host is the client
- [ ] Give two examples where one host is both client and server simultaneously

## Related notes

- [[Server]] · [[Host]] · [[Socket]] · [[Port]] · [[TCP]] · [[UDP]]
- [[HTTP-HTTPS]] · [[SSH]] · [[DNS]] · [[DHCP]]
- ← [[01-Roles/Index|Roles]] · [[01-Basic-Terminology/Index|Basic Terminology]]
