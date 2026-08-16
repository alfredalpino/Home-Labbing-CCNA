---
tags: [network-security, firewalls, networking, ccna]
aliases: [Packet Filtering, Packet Filter Firewall, Stateless Firewall]
layer: Network / Transport headers
---

# Packet Filtering Firewall

## Learning objectives

- Define packet filtering as stateless header-based allow/deny
- Know which fields are typically matched
- Contrast with [[Stateful Inspection Firewall]]
- Spot strengths and blind spots for CCNA/ops work

## One-sentence definition

> A **packet filtering firewall** permits or denies each [[Packet]] individually by inspecting **header fields** (IPs, ports, protocol, sometimes flags) **without tracking connection state**.

## Analogy

> Packet filtering is a guard who checks **each envelope’s from/to addresses and stamp type**, then stamps APPROVED or REJECTED — but **forgets you the moment you walk past**. Every packet is a stranger again. That’s fast, but forged “replies” can sometimes look like legitimate return mail.

## Why it matters

Classic router [[ACLs]] are often packet filters. You must understand them before stateful/NGFW features, because many outages are still “ACL line 40 deny IP any any” problems.

## Deep dive

### Mental model

```text
Packet arrives → match rules top-down → first hit wins → permit/deny/log
No memory of SYN/ACK relationship unless the platform adds state elsewhere
```

### Typical match fields

| Field | Example use |
|-------|-------------|
| Src/Dst IP | Networks, host allows |
| Protocol | TCP / UDP / ICMP |
| Ports | Service allow ([[Port]]) |
| ICMP type/code | Ping/traceroute policy |
| In/out interface | Directional policy |

### Strengths / weaknesses

| Strengths | Weaknesses |
|-----------|------------|
| Fast, simple, ubiquitous | No true session awareness |
| Easy to reason line-by-line | Hard to express “only established replies” without established keyword / state |
| Great first layer | Blind to app abuse inside allowed ports |

### On the wire

A permit for `TCP any any eq 443` allows SYNs to 443 — and without state/`established`, poorly written filters may mishandle return traffic or be too open.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet + Transport headers | L3/L4 filtering |
| OSI | 3–4 | Network/transport |

## Lab exercises

### Lab 1 — Read an ACL like a packet filter

On a lab router, write a standard/extended ACL that allows SSH from one host and denies other VTY attempts — then test.

### Lab 2 — Order matters

Put a broad `permit ip any any` above a deny and observe why the deny never hits.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Intermittent app breaks | Return traffic denied | direction, established/state |
| “Nothing works” after ACL | Implicit deny / wrong bind | interface direction, ACL counters |
| Ping fails, TCP works | ICMP filtered | intentional vs accident |

## Common traps / interview gotchas

- Packet filter ≠ stateful firewall.
- Top-down first-match; implicit deny at end on Cisco ACLs.
- Allowing a port is not “application security.”

## Mastery checklist

- [ ] Define stateless packet filtering
- [ ] List common match fields
- [ ] Explain first-match + implicit deny
- [ ] Contrast with stateful inspection

## Related notes

- [[Stateful Inspection Firewall]] · [[ACLs]] · [[Firewalls]] · [[TCP]] · [[UDP]] · [[ICMP]]
- ← [[01-Firewalls/Index|Firewalls]] · [[04-Network-Security/Index|Network Security]]
