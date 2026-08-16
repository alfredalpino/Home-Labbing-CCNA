---
tags: [moc, switching, networking, ccna]
aliases: [Switching, LAN Switching]
---

# Switching

How Ethernet frames move inside a site: learning, VLANs, loop control, bundling, and modern overlays.

## Analogy

> Routing is **airports between cities**. Switching is the **building’s internal hallways**: nameplates on doors ([[MAC-Address-Tables]]), colored badge zones ([[VLANs]]), emergency rules that lock extra doors during a fire drill ([[STP]]), multi-lane corridors that count as one ([[Link-Aggregation]]), and shipping whole rooms across campus in containers ([[VXLAN]]).

## Notes in this section

| Note | One-line idea |
|------|----------------|
| [[VLANs]] | Logical L2 broadcast domains + 802.1Q trunks |
| [[MAC-Address-Tables]] | MAC → port learning; forward / filter / flood |
| [[STP]] | Loop-free tree; RSTP/MSTP awareness |
| [[Link-Aggregation]] | EtherChannel / LACP bundles |
| [[VXLAN]] | L2 overlay over L3; VNI + VTEP |

## Study order

1. [[MAC-Address-Tables]] — how a switch thinks  
2. [[VLANs]] — segmentation + trunks  
3. [[STP]] — redundancy without meltdown  
4. [[Link-Aggregation]] — fatter uplinks  
5. [[VXLAN]] — fabric overlay idea  

## Related

- Upstream: [[04-Building-a-Network/Index|Building a Network]]
- Pair with: [[04-Routing/Index|Routing]] · [[Switches]] · [[LAN]] · [[Hub]]
