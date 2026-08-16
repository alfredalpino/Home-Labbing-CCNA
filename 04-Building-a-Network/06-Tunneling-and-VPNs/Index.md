---
tags: [moc, vpn, tunneling, networking, ccna]
aliases: [Tunneling and VPNs, Tunneling & VPNs, VPNs]
---

# Tunneling & VPNs

Private overlays across shared networks: user and site VPNs, provider MPLS VPNs, and classic GRE+IPsec tunnels.

## Analogy

> The Internet and provider backbones are **public transit and shared airports**. This section is about **sealed capsules and special cargo handling**:
> - [[VPN]] (foundation) — private path over shared underlay  
> - [[IPSec-vs-SSL-VPN]] — freight container vs briefcase crypto styles  
> - [[Site-to-Site-vs-Remote-Access]] — warehouse tunnel vs employee badge  
> - [[MPLS-VPN]] — airline pallets on the provider conveyor  
> - [[GRE-IPSec-Tunnels]] — clear tube inside an armored sleeve  

## Notes in this section

| Note | One-line idea |
|------|----------------|
| [[IPSec-vs-SSL-VPN]] | IPsec packet crypto vs TLS-based remote VPN |
| [[Site-to-Site-vs-Remote-Access]] | Network-to-network vs user-to-network |
| [[MPLS-VPN]] | L3VPN with VRFs + MP-BGP + labels |
| [[GRE-IPSec-Tunnels]] | GRE flexibility + IPsec confidentiality |

## Study order

1. Re-read [[VPN]] and [[SSL-TLS]]  
2. [[Site-to-Site-vs-Remote-Access]] — pick the pattern  
3. [[IPSec-vs-SSL-VPN]] — pick the crypto/client model  
4. [[GRE-IPSec-Tunnels]] — classic lab overlay  
5. [[MPLS-VPN]] + [[MPLS]] — provider WAN service  

## Related

- Upstream: [[04-Building-a-Network/Index|Building a Network]]
- Pair with: [[04-Routing/Index|Routing]] · [[SD-WAN]] · [[VRFs]] · [[WAN]] · [[LAN]]
