---
tags: [basic-terminology, networking, ccna, socket]
aliases: [Network Socket, Berkeley Socket, Endpoint]
layer: Transport API / endpoint
---

# Socket

## Learning objectives

- Define a socket as an OS endpoint (IP + port + protocol)
- Explain the TCP 5-tuple and connection uniqueness
- Contrast listening sockets vs connected sockets
- Use `ss`/`netstat`/`lsof` to read socket state fluently

## One-sentence definition

> A **socket** is an operating-system abstraction representing one endpoint of communication — typically specified by protocol ([[TCP]]/[[UDP]]), local [[IP Address]], and local [[Port]] (and for connections, the remote IP/port as well).

## Analogy

> A socket is a **phone handset already wired to a specific call**: your number + their number + whether it’s a landline style (TCP) or walkie-talkie style (UDP). The OS hands apps a handset (file descriptor), not raw wire access.

## Why it matters

Applications don’t “send packets to the Internet” in the abstract — they write to sockets. When you hit `TIME_WAIT` exhaustion, file descriptor limits, or “address already in use,” you are debugging sockets. Load balancers and firewalls track socket-level flows (5-tuples).

## Deep dive

### Mental model

```text
Process
  └── Socket descriptor (fd)
        ├── protocol: TCP/UDP
        ├── local  IP:port
        └── remote IP:port   (for connected TCP; sometimes UDP too)
```

**TCP connection uniqueness** = 5-tuple:

```text
(protocol, src IP, src port, dst IP, dst port)
```

Two browsers can both talk to `93.184.216.34:443` simultaneously because **source ports** differ.

### Listening vs established

| Socket kind | Meaning |
|-------------|---------|
| LISTEN | Server waiting for new TCP clients |
| ESTABLISHED | Active connection |
| TIME_WAIT | Local side closed; waiting to ensure old duplicates die |
| CLOSE_WAIT | Remote closed; local app hasn’t closed yet (often app bug) |

UDP sockets are usually unconnected (datagrams from anyone) unless `connect()` was used to set a default peer.

### On the wire / fields

Sockets map directly to the transport header ports + IP addresses in packets. The socket API is host-local; the wire sees the resulting headers.

```bash
ss -tan
ss -tanp
netstat -anv
lsof -nP -iTCP -sTCP:ESTABLISHED
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Transport (+ OS API) | Endpoint for apps |
| OSI | 4–5 | Transport addressing; session-ish state in TCP |

## Lab exercises

### Lab 1 — Map process → socket

```bash
# macOS
lsof -nP -iTCP -sTCP:LISTEN
# Linux
ss -ltnp
```

### Lab 2 — Watch TIME_WAIT

```bash
for i in $(seq 1 20); do curl -s -o /dev/null http://example.com; done
netstat -an | grep TIME_WAIT | head
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Address already in use | Port bound / TIME_WAIT | `lsof`, SO_REUSEADDR patterns |
| Too many open files | FD limit / leak | `lsof -p PID`, ulimit |
| CLOSE_WAIT pileup | App not closing sockets | application bug |
| Cannot connect outbound | ephemeral port exhaustion (rare) / policy | local port range, NAT pools |

## Common traps / interview gotchas

- Socket ≠ port. Port is a number; socket is the OS object/endpoint.
- “Socket programming” errors often look like network outages.
- Reverse proxies terminate client sockets and open *new* sockets to origins — two 5-tuples.
- QUIC multiplexes streams over UDP — still sockets underneath.

## Mastery checklist

- [ ] Write the TCP 5-tuple from memory
- [ ] Explain LISTEN vs ESTABLISHED vs TIME_WAIT
- [ ] Find which process owns a listening port
- [ ] Explain how multiple clients share one server port

## Related notes

- [[Port]] · [[TCP]] · [[UDP]] · [[IP Address]] · [[Client]] · [[Server]]
- ← [[04-Addressing/Index|Addressing]] · [[01-Basic-Terminology/Index|Basic Terminology]]
