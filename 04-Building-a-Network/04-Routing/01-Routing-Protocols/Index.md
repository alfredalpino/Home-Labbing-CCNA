---
tags: [moc, routing-protocols, networking, ccna]
aliases: [Routing Protocols, IGPs and BGP]
---

# Routing Protocols

Control-plane languages routers use to **learn and advertise** reachability. Pair with [[Static-vs-Dynamic-Routing]] for when to use them.

## Analogy

> Protocols are **different radio languages for traffic control**:
> - [[RIP]] — backyard gossip (hop counts)
> - [[EIGRP]] — taxi dispatch with ready backups (DUAL)
> - [[OSPF]] — shared city blueprints (link-state)
> - [[BGP]] — international airline diplomacy (policy / AS paths)
> - [[MPLS]] — airport baggage tags on the provider conveyor (underlay labels)

## Notes in this section

| Note | One-line idea |
|------|----------------|
| [[OSPF]] | Link-state IGP; LSDB + SPF; CCNA core |
| [[EIGRP]] | Cisco advanced DV; successor / feasible successor |
| [[RIP]] | Hop-count DV; teaching / legacy |
| [[BGP]] | Path-vector between ASes; Internet & edge |
| [[MPLS]] | Label-switching underlay (not the VPN service itself) |

## Study order

1. [[RIP]] — distance-vector intuition  
2. [[OSPF]] — primary IGP mastery  
3. [[EIGRP]] — DUAL + Cisco labs  
4. [[BGP]] — edge / policy awareness  
5. [[MPLS]] — how provider cores forward  

## Compare at a glance

| Protocol | Type | “Best path” vibe | Typical AD (Cisco) |
|----------|------|------------------|--------------------|
| RIP | DV | Fewest hops | 120 |
| EIGRP | Adv. DV | Composite metric + DUAL | 90 |
| OSPF | Link-state | Lowest cost | 110 |
| BGP | Path-vector | Policy attributes | 20 e / 200 i |

## Related

- Parent: [[04-Routing/Index|Routing]]
- Services that use these: [[MPLS-VPN]] · [[SD-WAN]] · [[VRFs]]
