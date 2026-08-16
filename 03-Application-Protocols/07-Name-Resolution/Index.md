---
tags: [moc, application-protocols, dns, name-resolution]
aliases: [Name Resolution]
---

# Name Resolution

DNS theory first, then public resolvers you will actually configure.

| Note | Role |
|------|------|
| [[DNS]] | Hierarchical name system |
| [[DNS-Servers/Index|DNS Servers]] | Cloudflare · Google · OpenDNS · Quad9 |

```mermaid
flowchart LR
  DNS[DNS] --> Resolvers[DNS Servers]
  Resolvers --> CF[Cloudflare]
  Resolvers --> G[Google]
  Resolvers --> O[OpenDNS]
  Resolvers --> Q[Quad9]
```

← [[03-Application-Protocols/Index|Application Protocols]]
