---
tags: [network-types, networking, ccna, client-server]
aliases: [Client-Server, Client Server Architecture]
layer: Architecture model
---

# Client-Server Network

## Learning objectives

- Define client–server as a role architecture, not a cable type
- Map to [[Client]] / [[Server]] behavior and well-known ports
- Contrast with [[Peer-to-Peer Network]]
- Spot client–server patterns in web, email, AD, databases

## One-sentence definition

> A **client–server network** organizes communication so **clients initiate requests** and **servers provide specialized services** (files, mail, web, auth) — usually centrally administered.

## Analogy

> Client–server is a **restaurant**: diners ([[Client]]) order; the kitchen ([[Server]]) cooks. Many diners share one kitchen. The kitchen doesn’t wander table-to-table asking who wants food — diners initiate. Compare peer-to-peer: a **potluck** where everyone brings and serves dishes.

## Why it matters

Almost every enterprise service (AD, DNS, web, databases) is client–server. Firewalls, load balancers, and capacity planning assume many clients → fewer servers. Your earlier notes on [[Client]] and [[Server]] are the microscopic view; this is the network *architecture* view.

## Deep dive

### Mental model

```text
Many Clients ──requests──► Server farm / VIP ──► data/apps
```

### Properties

| Trait | Client–server |
|-------|----------------|
| Roles | Asymmetric, specialized |
| Scaling | Scale servers/tiers |
| Admin | Central policy, backups, auth |
| Failure | Server outage hits many clients |

### Examples

- Web: browser → [[HTTP-HTTPS]] server
- Name resolution: stub → [[DNS]] recursive/auth
- Mail: MUA → [[SMTP-IMAP]] servers
- Remote admin: you → [[SSH]] daemon

### On the wire

Look for well-known destination [[Port]]s on the server side; clients use ephemeral ports ([[Socket]]).

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Architecture | Mostly application design | Runs on any LAN/WAN |
| Transport | Often [[TCP]] | Connection-oriented apps |

## Lab exercises

### Lab 1 — Prove roles with a capture mindset

```bash
curl -vI https://example.com/
# Client initiates TCP to server :443
```

### Lab 2 — Inventory servers you depend on

List DNS, DHCP, gateway, email — each is a server role on your path.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| All users fail one app | Server/VIP/path | health, DNS to VIP |
| One user fails | Client config/endpoint | local DNS, proxy, creds |
| Intermittent | LB member / capacity | server metrics |

## Common traps / interview gotchas

- A host can be client *and* server simultaneously.
- “Client–server network” ≠ requires a Windows Server OS.
- P2P apps can still run *on* enterprise client–server infrastructure.

## Mastery checklist

- [ ] Explain restaurant vs potluck analogy
- [ ] Tie to Client/Server notes
- [ ] Give four real protocol examples
- [ ] Contrast failure domains vs P2P

## Related notes

- [[Client]] · [[Server]] · [[Peer-to-Peer Network]] · [[Port]] · [[DNS]] · [[HTTP-HTTPS]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
