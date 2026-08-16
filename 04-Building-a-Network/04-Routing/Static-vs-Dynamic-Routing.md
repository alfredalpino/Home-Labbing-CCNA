---
tags: [routing, networking, ccna, static-routing, dynamic-routing]
aliases: [Static Routing, Dynamic Routing, Static vs Dynamic]
layer: Network (Layer 3)
---

# Static vs Dynamic Routing

## Learning objectives

- Explain how a router chooses a next hop from a routing table
- Contrast static routes with dynamic routing protocols
- Know when static is the right tool (stub, default, floating) vs when dynamic wins
- Read AD, metrics, and “best path” without confusing them

## One-sentence definition

> **Static routing** means *you* install routes by hand; **dynamic routing** means routers *exchange* reachability and install/withdraw routes automatically — both end up as entries in the same routing table that drives forwarding.

## Analogy

> Static routes are **hand-painted road signs** you nail up: “To City B, take Exit 3.” Dynamic protocols are a **live traffic radio network** between cities: when a bridge collapses, the radios shout and every junction updates its signs. Hand-painted signs don’t gossip — and they don’t lie unless *you* painted wrong.

## Why it matters

Every CCNA forwarding question bottoms out here: how did that route get into the table, how preferred is it (AD), and what happens when the link dies? Static is simple and predictable; dynamic scales and heals. Real designs mix both.

## Deep dive

### Mental model

```text
Packet arrives → longest-match lookup in RIB/FIB
                 ├ connected (directly attached)
                 ├ static (admin-configured)
                 └ dynamic (OSPF / EIGRP / BGP / RIP …)
                 → forward out interface / to next-hop
```

### Mechanism — how a route “wins”

| Concept | Meaning |
|---------|---------|
| Longest prefix match | `/24` beats `/16` for that destination |
| Administrative Distance (AD) | Prefer source: connected 0, static 1, eBGP 20, EIGRP 90, OSPF 110, RIP 120, iBGP 200 (Cisco defaults) |
| Metric | Within one protocol, “cost” to pick among candidates |

Static and dynamic are **sources**. The table still does longest match first; AD only breaks ties among equal-length prefixes from different sources.

### Static patterns you must know

| Pattern | Use |
|---------|-----|
| Default `0.0.0.0/0` | Stub edge → Internet / core |
| Network static | Point at a remote subnet via next-hop or exit iface |
| Floating static | Higher AD backup when dynamic fails |
| Discard/null0 | Blackhole or summarize safely |

**Next-hop IP vs exit interface:** on multi-access Ethernet, prefer next-hop IP (or recursive). Point-to-point serials often use exit interface. Recursive statics resolve via another route — watch dependency loops.

### Dynamic patterns (overview)

| Family | Idea | CCNA focus |
|--------|------|------------|
| [[RIP]] | Hop-count DV | Legacy / concepts |
| [[EIGRP]] | Advanced DV / DUAL | Cisco labs |
| [[OSPF]] | Link-state LSDB | Core CCNA |
| [[BGP]] | Path-vector policy | Edge / ISP awareness |

Dynamic wins when topology churns, many prefixes, or multi-path policy. Cost: CPU, memory, complexity, and misconfig blast radius.

### On the wire

Static: nothing exchanged for the route itself — only data plane follows your config.

Dynamic: protocol hellos, updates/LSAs, or BGP UPDATEs over TCP/UDP/multicast depending on protocol. Control plane ≠ data plane (packets still follow the FIB).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| OSI / TCP-IP | Network (L3) | Routing decision & forwarding |
| Control plane | Above L3 data | Protocol messages install routes |

## Lab exercises

### Lab 1 — Static triangle (GNS3 / Cisco IOS)

Three routers: R1—R2—R3. Put LAN on R1 (`192.168.1.0/24`) and R3 (`192.168.3.0/24`). On R1:

```ios
ip route 192.168.3.0 255.255.255.0 10.0.12.2
```

Mirror on R3 toward R1. Verify `show ip route`, `ping`, then shut the R1–R2 link — observe **no** automatic reroute.

### Lab 2 — Floating static over OSPF

Run [[OSPF]] between R1–R2–R3 so R1 learns `192.168.3.0/24`. Add:

```ios
ip route 192.168.3.0 255.255.255.0 10.0.13.3 210
```

Confirm AD 210 does not override OSPF until the OSPF path fails.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Ping fails, route missing | No static / no protocol adjacency | `show ip route`, interfaces up |
| Wrong next hop | Typo / recursive fail | `show ip route <prefix>`, traceroute |
| Flap / blackhole after change | Stale static still preferred | AD vs dynamic; floating static AD |
| Asymmetric path | Different statics each side | Both directions; return path |

## Common traps / interview gotchas

- AD is **not** a metric — don’t say “OSPF has lower AD than EIGRP so lower cost.”
- Static AD 1 beats almost everything — accidental statics override OSPF.
- Exit-interface static on Ethernet can look “connected” and confuse ARP behavior — prefer next-hop.
- Dynamic does not remove the need for a good default / redistribution design.

## Mastery checklist

- [ ] Explain longest match → AD → metric order
- [ ] Write a default and a floating static in IOS
- [ ] Name when static beats dynamic (stub, simple, backup)
- [ ] Contrast control-plane chat vs data-plane forwarding

## Related notes

- [[Default-Gateway]] · [[OSPF]] · [[EIGRP]] · [[RIP]] · [[BGP]] · [[Routers]] · [[IP Address]]
- ← [[04-Routing/Index|Routing]] · [[04-Building-a-Network/Index|Building a Network]]
