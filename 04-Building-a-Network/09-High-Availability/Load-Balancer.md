---
tags: [high-availability, networking, ccna, load-balancer, vip]
aliases: [Load Balancer, Server Load Balancer, SLB, ADC]
layer: L4–L7 distribution / VIP
---

# Load Balancer

## Learning objectives

- Define a load balancer as distributing client sessions across a server (or path) pool via a VIP
- Contrast L4 vs L7 balancing and health checks
- Relate algorithms [[Round-Robin]] and [[Least-Connections]]
- Separate server LB from gateway FHRP ([[HSRP]] / [[VRRP]] / [[GLBP]])

## One-sentence definition

> A **load balancer** fronts a pool of backends with one (or few) **virtual IPs**, steering each new connection or request according to an algorithm and health so no single server is the only door — while providing a pivot point for [[Failover]].

## Analogy

> A load balancer is an **airport check-in hall with one address on the map (VIP)** and many open counters (servers). A greeter ([[Round-Robin]] / [[Least-Connections]]) sends each passenger to a free counter. If a counter’s light goes dark (failed health check), the greeter stops sending people there. FHRP is different: that’s **redundant doors into the airport roads** (default gateway), not the check-in counters.

## Why it matters

Apps, firewalls, and even [[VPN]] concentrators sit behind LBs. CCNA-adjacent ops need VIP, pool, health check, and SNAT awareness to debug “works on server IP, fails on VIP.”

## Deep dive

### Mental model

```text
Client → VIP (LB) → chosen healthy server
              ↑ health probes
Optional: LB SNAT so return path comes back through LB
```

### Mechanism

1. Client resolves app name to VIP ([[DNS]]).
2. LB accepts connection; picks member via algorithm.
3. Health checks remove bad members.
4. Persistence/sticky may pin a client to one server.
5. Failures: connection drain, backup pool, or [[Failover]] pair of LBs.

### L4 vs L7

| Mode | Sees | Use |
|------|------|-----|
| L4 | IP/ports/TCP-UDP | Fast, TLS passthrough common |
| L7 | HTTP/path/headers | Content steer, WAF features |

### On the wire

Clients talk to VIP. Backend packets may show LB as source if SNATed. [[Packet-Analysis]] on the server without understanding SNAT confuses return routing.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Transport / Application | L4–L7 service front end |
| OSI | 4–7 | Port vs payload decisions |

## Lab exercises

### Lab 1 — VIP vs real IP

Access an app via public VIP and (if lab allows) directly via member IP. Note cert/name and path differences.

### Lab 2 — Algorithm prediction

With three equal servers and [[Round-Robin]], predict distribution of 30 connections. Redo mentally with [[Least-Connections]] if one server is slow.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| VIP down for all | LB HA / VIP free | LB pair, ARP for VIP |
| Some users fail | Bad member / persistence | pool health, sticky |
| Server sees wrong client IP | SNAT | X-Forwarded-For, logs |
| Works direct, not VIP | Health/firewall | probe path, security groups |

## Common traps / interview gotchas

- Load balancer ≠ [[HSRP]]; different problem domain.
- Health check success ≠ app correctness (check the right URL).
- Persistence can hide broken balancing until a node dies.
- Source NAT changes security logs and geolocation — know your mode.

## Mastery checklist

- [ ] Draw client → VIP → pool
- [ ] Contrast L4 vs L7
- [ ] Name [[Round-Robin]] and [[Least-Connections]]
- [ ] Separate LB from FHRP gateway HA

## Related notes

- [[Round-Robin]] · [[Least-Connections]] · [[Failover]] · [[HSRP]] · [[DNS]] · [[VPN]] · [[Packet-Analysis]]
- ← [[09-High-Availability/Index|High Availability]] · [[04-Building-a-Network/Index|Building a Network]]
