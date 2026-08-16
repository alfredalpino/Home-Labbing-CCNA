---
tags: [basic-terminology, networking, ccna, port]
aliases: [TCP Port, UDP Port, Port Number]
layer: Transport (Layer 4)
---

# Port

## Learning objectives

- Explain ports as transport-layer demultiplexing identifiers
- Know well-known vs registered vs ephemeral ranges
- Memorize critical service ports for CCNA/ops work
- Troubleshoot “wrong port,” conflicts, and firewall port confusion

## One-sentence definition

> A **port** is a 16-bit number (0–65535) in [[TCP]] or [[UDP]] that identifies a specific application endpoint on a host so many services can share one [[IP Address]].

## Analogy

> An IP address is the **apartment building**; a port is the **apartment number**. Many residents (apps) share one building (host). Mail to building-only with no apartment gets lost — hence destination ports on servers.

## Why it matters

Firewalls, security groups, NAT, and sockets all key off ports. Saying “open the server” is meaningless; you open **protocol + port** (and usually direction). Most outages labeled “network” are really “traffic never reached port 443/22/53.”

## Deep dive

### Mental model

```text
IP address  = which host
Port        = which application process on that host
Protocol    = TCP or UDP (separate port spaces!)
```

TCP port 53 and UDP port 53 are **different** endpoints. [[DNS]] uses both.

### Ranges (IANA)

| Range | Numbers | Typical use |
|-------|---------|-------------|
| Well-known | 0–1023 | System services (often root/admin to bind) |
| Registered | 1024–49151 | User services / apps |
| Dynamic / ephemeral | 49152–65535 | Client source ports (OS-dependent; Linux often different range) |

### Must-know ports

| Service | Port | Proto |
|---------|------|-------|
| SSH | 22 | TCP |
| DNS | 53 | UDP/TCP |
| DHCP | 67/68 | UDP |
| HTTP | 80 | TCP |
| NTP/SNTP | 123 | UDP |
| HTTPS | 443 | TCP |
| SMTP | 25/587 | TCP |
| IMAP | 143/993 | TCP |
| FTP control | 21 | TCP |

### On the wire / fields

TCP/UDP headers start with Source Port / Destination Port (16 bits each).

Client perspective:

```text
src_port = ephemeral (e.g. 52444)
dst_port = service (e.g. 443)
```

Server listening socket: dst_port of incoming SYNs equals the service port.

```bash
lsof -nP -iTCP:443 -sTCP:LISTEN
ss -ltnp | grep ':443'
nc -vz example.com 443
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Transport | Demux to applications |
| OSI | 4 | Transport SAP addressing |

## Lab exercises

### Lab 1 — Ephemeral source ports

```bash
curl -s https://example.com -o /dev/null &
netstat -an | grep '\.443 '
# Note client source port changes per connection
```

### Lab 2 — Port conflict

```bash
nc -l 8080 &
nc -l 8080
# Second bind fails — address already in use
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Connection refused | Nothing on that port | listeners, container port map |
| Timed out | Filter dropping | ACL/SG/firewall path |
| Wrong service answers | Port reuse / reverse proxy | banner, TLS cert, HTTP Host |
| Works then fails after reboot | Service not enabled / different bind | systemd, docker publish |

## Common traps / interview gotchas

- Opening TCP 53 doesn’t fix UDP DNS (and vice versa for large responses needing TCP).
- NAT port translation: many inside clients share one public IP via different ports.
- “Port scanning” hits closed vs filtered differences (RST vs silence).
- ICMP has no ports — don’t look for them.

## Mastery checklist

- [ ] Recite the critical port table above from memory
- [ ] Explain why TCP and UDP ports are separate namespaces
- [ ] Identify client vs server from a 5-tuple’s ports
- [ ] Resolve a local port conflict

## Related notes

- [[Socket]] · [[TCP]] · [[UDP]] · [[Client]] · [[Server]] · [[Protocol]]
- [[DNS]] · [[DHCP]] · [[HTTP-HTTPS]] · [[SSH]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
