---
tags: [meta, obsidian, vault]
aliases: [Obsidian Setup, How to open this vault]
---

# Obsidian setup for this vault

## Open the vault

1. Install [Obsidian](https://obsidian.md).
2. **Open folder as vault** → `/Users/ubaid/Home-Labbing-CCNA`
3. Start at [[Home]]

## Folder nesting (how the graph should look)

```text
Home
├── 00-Networks-and-Devices/
│   ├── 01-Network-Types/
│   └── 02-Network-Devices/
├── 01-Basic-Terminology/
│   ├── 01-Roles/
│   ├── 02-Data-Units/
│   ├── 03-Performance/
│   ├── 04-Addressing/
│   └── 05-Physical/
├── 02-Core-Protocols/
├── 03-Application-Protocols/
│   ├── 01-Web-and-Security/
│   ├── 02-Remote-Access/
│   ├── 03-Time/
│   ├── 04-File-Transfer/
│   ├── 05-Email/
│   ├── 06-Host-Config/
│   └── 07-Name-Resolution/
│       └── DNS-Servers/
├── 04-Building-a-Network/
│   ├── 01-Linux-for-Networking/
│   ├── 02-IP-Addressing/
│   │   └── 01-NAT/
│   ├── 03-Subnetting/
│   ├── 04-Routing/
│   │   └── 01-Routing-Protocols/
│   ├── 05-Switching/
│   ├── 06-Tunneling-and-VPNs/
│   ├── 07-Wireless-Networking/
│   │   └── 01-Wireless-Technologies/
│   ├── 08-Packet-Analysis/
│   ├── 09-High-Availability/
│   └── 10-Traffic-Management/
├── 90-Reference/          (roadmaps — dim in graph)
├── ai/                    (context + logs — hide from graph)
│   ├── context/
│   └── logs/
└── roadmap-extracts/      (hidden from graph filter)
```

## Graph filters (already in `.obsidian/graph.json`)

If bubbles look noisy again:

1. Open Graph view
2. Open the filter search box
3. Confirm it contains:

```text
-path:ai -path:roadmap-extracts -path:Templates -path:GNS3 -path:.cursor -path:bash-learn -path:my_directory -path:91-System
```

4. Turn **Orphans** off, **Unresolved** off
5. Use color groups by path (preconfigured)

## Local graph (best for one topic)

Right-click a note → **Open local graph** — shows only that bubble’s neighborhood (cleaner than global).

## Templates & attachments

- Templates folder = `Templates`
- Attachments folder = `Attachments`
