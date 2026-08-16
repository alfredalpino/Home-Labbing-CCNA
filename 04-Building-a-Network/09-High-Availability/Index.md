---
tags: [moc, high-availability, networking, ccna, fhrp]
aliases: [High Availability, HA, FHRP]
---

# High Availability

Keep gateways and services alive when boxes and links die.

## Analogy

> HA is **understudies, spare ovens, and dual bridges**: first-hop protocols ([[HSRP]], [[VRRP]], [[GLBP]]) keep the default gateway podium staffed; [[Load-Balancer]]s spread and health-check the counters; algorithms ([[Round-Robin]], [[Least-Connections]]) choose who gets the next guest; [[Failover]] is the moment the understudy actually steps on stage.

## First-hop redundancy (FHRP)

| Note | One-line idea |
|------|----------------|
| [[HSRP]] | Cisco Active/Standby virtual gateway |
| [[VRRP]] | Standards-based Master/Backup gateway |
| [[GLBP]] | Cisco VIP with multiple forwarders |

## Service distribution

| Note | One-line idea |
|------|----------------|
| [[Load-Balancer]] | VIP in front of a healthy pool |
| [[Round-Robin]] | Take turns |
| [[Least-Connections]] | Prefer least-busy member |
| [[Failover]] | Detect, promote, recover |

## Study order

1. [[Failover]] mindset → [[HSRP]] / [[VRRP]]
2. [[GLBP]] when asked about FHRP load-share
3. [[Load-Balancer]] + [[Round-Robin]] + [[Least-Connections]]
4. Prove cutovers with [[Packet-Analysis]]

← [[04-Building-a-Network/Index|Building a Network]]
