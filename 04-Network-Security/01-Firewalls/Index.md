---
tags: [moc, network-security, firewalls, networking, ccna]
aliases: [Firewalls, Firewall Types]
---

# Firewalls

A **firewall** enforces policy on traffic crossing a trust boundary — usually between networks with different risk levels (Internet ↔ DMZ ↔ inside).

## Analogy

> A firewall is the **security checkpoint at a building entrance**. Different checkpoints inspect differently: some only glance at the address on the envelope ([[Packet Filtering Firewall]]), some remember the whole conversation ([[Stateful Inspection Firewall]]), some open the letter and judge content ([[Proxy Firewall]] / [[Web Application Firewall]]), and modern ones add metal detectors + ID systems + threat intel ([[Next-Generation Firewall]]).

## Firewall types in this vault

| Type | Inspection style | Note |
|------|------------------|------|
| Packet Filtering | Per-packet header rules | [[Packet Filtering Firewall]] |
| Stateful Inspection | Connection/state aware | [[Stateful Inspection Firewall]] |
| Next-Generation | App ID, users, IPS, intel | [[Next-Generation Firewall]] |
| Proxy | Terminates & re-initiates sessions | [[Proxy Firewall]] |
| Circuit-Level Gateway | Session/circuit approval (SOCKS-ish) | [[Circuit-Level Gateway]] |
| Web Application | HTTP(S) app-layer defenses | [[Web Application Firewall]] |

## Where firewalls sit

```text
Internet ── Edge NGFW/router ACL ── DMZ ── Internal FW ── LAN
                ▲
         also: cloud security groups, host firewalls
```

## Related

- [[ACLs]] · [[IDS IPS]] · [[Routers]] · [[VPN]] · [[Zero Trust Architecture]]

← [[04-Network-Security/Index|Network Security]]
