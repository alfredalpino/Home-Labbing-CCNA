---
tags: [moc, core-protocols, networking, ccna]
aliases: [Core Protocols, 02-Core-Protocols/_Index]
---

# Core Protocols — Map of Content

These three protocols are the nervous system of IP networks.

## Study order

1. [[ICMP]] — reachability and error signaling
2. [[UDP]] — simple datagram transport
3. [[TCP]] — reliable, ordered, congestion-aware transport

## Notes

| Protocol | Layer | Job |
|----------|-------|-----|
| [[TCP]] | Transport | Reliable byte stream |
| [[UDP]] | Transport | Unreliable datagrams |
| [[ICMP]] | Network (companion to IP) | Errors + diagnostics |

## How they fit

```text
Your app ──► TCP or UDP ──► IP (+ ICMP for errors) ──► Ethernet/Wi-Fi
```

← [[Home]] · Back: [[01-Basic-Terminology/Index|Basic Terminology]] · Next: [[03-Application-Protocols/Index|Application Protocols]]
