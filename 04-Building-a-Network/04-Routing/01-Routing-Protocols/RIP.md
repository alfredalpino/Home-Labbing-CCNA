---
tags: [routing-protocols, networking, ccna, rip]
aliases: [Routing Information Protocol, RIPv2, RIP]
layer: Network (Layer 3) / control plane
---

# RIP

## Learning objectives

- Explain RIP as a hop-count distance-vector protocol (legacy but conceptually important)
- Contrast RIPv1 vs RIPv2 (classful vs classless, broadcast vs multicast)
- Configure RIPv2 and see split horizon / poison reverse ideas in a lab
- Know why OSPF/EIGRP replaced RIP in real networks

## One-sentence definition

> **RIP** (Routing Information Protocol) is a simple **distance-vector** IGP that chooses paths by **hop count** (max 15), periodically advertising routes to neighbors — easy to understand, slow and chatty at scale.

## Analogy

> RIP is **gossip over the backyard fence**. Every 30 seconds each neighbor shouts how many fences away each destination is. You believe the lowest hop count. Rumors travel slowly; a bad rumor (routing loop) can bounce until the hop count hits **16 = infinity** (“count to infinity”). Modern cities use shared blueprints ([[OSPF]]) instead of endless gossip.

## Why it matters

CCNA still uses RIP to teach distance-vector rules: hop count, timers, split horizon, poison reverse, triggered updates. You’ll rarely design greenfield RIP — but interviewers love “why not RIP?”

## Deep dive

### Mental model

```text
Every ~30s: send full (or changed) route table to neighbors
On hear: if better hop count → install; hop = neighbor hops + 1
Max useful metric 15; 16 = unreachable
```

### Mechanism

| Feature | RIPv1 | RIPv2 |
|---------|-------|-------|
| Masks | Classful (no VLSM in updates) | Classless (sends mask) |
| Transport | UDP/520 broadcast | UDP/520 multicast `224.0.0.9` |
| Auth | No | Yes (simple/MD5 awareness) |
| Status | Historic | Lab / legacy edges |

**Loop mitigation classics**

- Split horizon: don’t advertise a route out the iface you learned it on  
- Route poisoning: advertise metric 16 for down routes  
- Hold-down timers: believe “maybe flapping” rumors carefully  
- Triggered updates: announce changes sooner than 30s  

### On the wire

UDP port **520**. RIPv2 multicast to `224.0.0.9`. No TCP session — pure UDP advertisements.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Application-ish control | RIP over UDP | Control plane messaging |
| Routing | L3 | Installs hop-count routes (AD 120) |

## Lab exercises

### Lab 1 — RIPv2 three-router chain (GNS3)

```ios
router rip
 version 2
 network 10.0.0.0
 no auto-summary
```

`show ip protocols`, `show ip route rip`, then shut a middle link — time how long recovery takes vs OSPF.

### Lab 2 — Count-to-infinity demo (careful teaching lab)

Disable split horizon on a link (`no ip split-horizon` on iface) in a small loop topology; observe metric climb toward 16 when a network is withdrawn. Re-enable split horizon. **Lab only.**

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| No RIP routes | v1/v2 mismatch / auto-summary | `show ip protocols` |
| Wrong mask | RIPv1 or auto-summary | force v2, `no auto-summary` |
| Slow failover | Timers / DV nature | compare to OSPF lab |
| Loops | Split horizon off / misuse | interface split-horizon |

## Common traps / interview gotchas

- Hop count ignores bandwidth — a 1-hop T1 “wins” over 2-hop 10G.
- 15-hop diameter limit kills large networks.
- AD 120 loses to OSPF/EIGRP — RIP routes may never install if better sources exist.
- “RIP is distance vector; OSPF is link state” — keep that crisp.

## Mastery checklist

- [ ] Configure RIPv2 with `no auto-summary`
- [ ] Explain hop count and infinity = 16
- [ ] Name split horizon and poison reverse
- [ ] Argue why enterprises prefer OSPF/EIGRP

## Related notes

- [[OSPF]] · [[EIGRP]] · [[BGP]] · [[Static-vs-Dynamic-Routing]] · [[UDP]] · [[Routers]]
- ← [[01-Routing-Protocols/Index|Routing Protocols]] · [[04-Routing/Index|Routing]]
