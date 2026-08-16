---
tags: [moc, routing, networking, ccna]
aliases: [Routing, How Routing Works]
---

# Routing

How packets leave a subnet and find remote networks: tables, gateways, protocols, overlays, and virtual routers.

## Analogy

> Switching is the **mailroom inside one building**. Routing is the **postal and airline system between cities**. You need road signs ([[Static-vs-Dynamic-Routing]]), an on-ramp from each neighborhood ([[Default-Gateway]]), sometimes private airspaces ([[VRFs]]), fancy dispatcher WANs ([[SD-WAN]]), and a whole radio language between junctions ([[01-Routing-Protocols/Index|Routing Protocols]]).

## Notes in this section

| Note | One-line idea |
|------|----------------|
| [[Static-vs-Dynamic-Routing]] | Hand-configured routes vs protocol-learned routes |
| [[Default-Gateway]] | Host/router catch-all next hop (`0.0.0.0/0`) |
| [[SD-WAN]] | Controller-driven, multi-transport WAN overlay |
| [[VRFs]] | Multiple routing tables on one device |
| [[01-Routing-Protocols/Index\|Routing Protocols]] | RIP, OSPF, EIGRP, BGP, MPLS underlay |

## Study order

1. [[Default-Gateway]] — how hosts leave the LAN  
2. [[Static-vs-Dynamic-Routing]] — how routers learn paths  
3. [[01-Routing-Protocols/Index|Routing Protocols]] — OSPF first, then EIGRP/RIP, BGP awareness, MPLS idea  
4. [[VRFs]] — isolation  
5. [[SD-WAN]] — modern WAN overlay thinking  

## Related

- Upstream: [[04-Building-a-Network/Index|Building a Network]]
- Pair with: [[05-Switching/Index|Switching]] · [[06-Tunneling-and-VPNs/Index|Tunneling & VPNs]] · [[Routers]]
