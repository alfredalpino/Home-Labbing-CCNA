---
tags: [basic-terminology, networking, ccna, server]
aliases: [Network Server, Server Role, Daemon]
layer: Application / End-system role
---

# Server

## Learning objectives

- Define server as a **role** (listen/accept), not a hardware class
- Explain binding, listening, backlog, and multi-client concurrency
- Map common services to ports and transport ([[TCP]] / [[UDP]])
- Distinguish origin servers, proxies, VIPs, and anycast “servers”

## One-sentence definition

> A **server** is a process (or cluster of processes behind a VIP) that **listens** for incoming requests and **responds** according to an application protocol.

## Analogy

> A server is the **shop that stays open with a listed address and hours**. Customers ([[Client]]s) walk in; the shop doesn’t roam the neighborhood looking for shoppers. One strip mall (host) can contain many shops (many listening ports).

## Why it matters

When users say “the server is down,” they might mean: process crashed, host up but port closed, DNS points wrong, load balancer drained, certificate expired, or dependency (DB/DNS/NTP) failed. Your job is to decompose “server” into **listener + path + identity + dependencies**.

## Deep dive

### Mental model

```text
Client ──request──► [ NIC → IP → Port → Process ] ──response──► Client
                         ▲
                    Server role lives here
```

Hardware “server” in a rack is just a powerful [[Host]]. The networking meaning is the **listening service**.

### Mechanism

1. Process requests OS to `bind()` to an IP (or `0.0.0.0` / `::`) + [[Port]].
2. For TCP: `listen()` → kernel accepts SYNs → `accept()` returns connected sockets.
3. For UDP: process reads datagrams on a bound port (DNS, DHCP server side, NTP).
4. Application protocol parses request → business logic → response.
5. Scaling patterns: threads/processes, event loops, reverse proxies, load balancers, anycast.

**Well-known pattern:** server uses a low / well-known port ([[Port]]); clients use ephemeral ports.

### Types you’ll meet

| Kind | Meaning |
|------|---------|
| Origin server | Holds the authoritative content/app |
| Reverse proxy / LB | Client-facing “server”; forwards to pool |
| VIP / anycast IP | Address clients hit; many real servers behind |
| Daemon / service | Background process implementing the server role |

### On the wire / fields

Server identity on the wire is usually:

- Destination IP of the request (or VIP)
- Destination port of the service
- TCP: responds to `SYN` with `SYN-ACK` if listening

```bash
# Who is listening?
ss -ltnup          # Linux
netstat -anv | grep LISTEN  # macOS
lsof -nP -iTCP -sTCP:LISTEN
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Implements HTTP, SSH, DNS, etc. |
| TCP/IP | Transport | Listening socket on TCP/UDP port |
| OSI | 7 | Application service |
| OSI | 4 | Port binding |

## Lab exercises

### Lab 1 — Run a tiny server and hit it as client

```bash
# Terminal A — TCP server on 9090
nc -l 9090

# Terminal B
echo 'hello' | nc 127.0.0.1 9090
```

Observe LISTEN → ESTABLISHED. You are both [[Client]] and [[Server]] on loopback.

### Lab 2 — Identify real listeners on your Mac

```bash
lsof -nP -iTCP -sTCP:LISTEN
sudo lsof -nP -iUDP
```

Map a few to known services ([[SSH]] `:22`, mDNS, etc.).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Connection refused | No listener / wrong port / bound to other IP | `ss`/`lsof`, bind address, container publish ports |
| Timed out | Filtered on path / blackhole | traceroute, ACL, security group, SYN seen on server? |
| Intermittent 502/504 | Upstream origin unhealthy behind LB | LB pool health, origin logs |
| Works locally, fails remotely | Bound to 127.0.0.1 only | Listen on `0.0.0.0` or correct interface |
| Wrong certificate name | VIP/SNI mismatch | TLS cert SAN vs hostname clients use |

## Common traps / interview gotchas

- “Server” in diagrams may be a **VIP**, not a single host.
- Binding to `127.0.0.1` is a classic “works on box, dead to network” bug.
- UDP servers don’t “listen” the same way — they bind and recv; no handshake to prove liveness besides app response.
- A host can run dozens of servers; outage may be one process, not the machine.
- Load balancers terminate TCP (and often TLS) — the “server” your client sees is the LB.

## Mastery checklist

- [ ] Distinguish hardware server vs listening service
- [ ] Use `ss`/`lsof` to find what listens where
- [ ] Explain VIP vs origin
- [ ] Diagnose refused vs timeout vs reset

## Related notes

- [[Client]] · [[Host]] · [[Port]] · [[Socket]] · [[Protocol]]
- [[TCP]] · [[HTTP-HTTPS]] · [[SSH]] · [[DNS]] · [[DHCP]]
- ← [[01-Roles/Index|Roles]] · [[01-Basic-Terminology/Index|Basic Terminology]]
