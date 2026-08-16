---
tags: [subnetting, networking, ccna, summarization, routing]
aliases: [Supernetting, Route Aggregation, Route Summarization]
layer: Network (Layer 3) — routing scalability
---

# Supernetting

## Learning objectives

- Define supernetting / route summarization as advertising one larger prefix for many smaller ones
- Compute a summary address and mask from a set of contiguous networks
- Know when summarization helps (table size, stability) and when it hides holes
- Contrast with subnetting ([[VLSM]]) — opposite direction on the same [[CIDR]] ladder

## One-sentence definition

> **Supernetting** (route aggregation / summarization) combines multiple contiguous prefixes into a **shorter** (less specific) prefix so routers can carry one route instead of many.

## Analogy

> Subnetting chops a city into **neighborhoods**. Supernetting is printing one **metro‑area** label on the highway sign instead of listing every street. Drivers ([[Packet]]s) still reach the right street locally; long‑haul maps ([[Routers]]’ tables) stay readable.

## Why it matters

Internet and enterprise routing scales because of aggregation. Without summarization, BGP and IGP tables explode and flaps cascade. CCNA expects you to build a correct summary and to spot **non‑contiguous** blocks that won’t summarize cleanly.

## Deep dive

### Mental model

```text
Specific routes:     192.168.0.0/24
                     192.168.1.0/24
                     192.168.2.0/24
                     192.168.3.0/24
Summary:             192.168.0.0/22
```

Subnetting: longer prefixes (more specific).  
Supernetting: shorter prefixes (less specific).

### Mechanism — how to summarize

1. List networks in binary (focus on the octet that changes).
2. Find the common bit prefix shared by all.
3. Prefix length = number of common bits; address = that common prefix with host bits 0.
4. Verify the summary does **not** cover unwanted networks (holes).

Example: `10.1.8.0/24`–`10.1.11.0/24` → `10.1.8.0/22`.

### Benefits and risks

| Upside | Downside |
|--------|----------|
| Smaller tables | May advertise space you don’t own (holes) |
| Hides child flaps | Blackholes if summary too broad |
| Cleaner policies | Harder troubleshooting (less specifics) |

### On the wire / fields

Summaries live in **routing updates** (OSPF areas, EIGRP auto/manual summary, BGP aggregates), not in data packet headers. Forwarding still uses longest prefix match when more specific routes exist.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Internet | Control‑plane scalability |
| Routing design | Hierarchy | Address plans that summarize well |

## Lab exercises

### Lab 1 — Paper summary

Summarize:

- `172.16.0.0/24`
- `172.16.1.0/24`
- `172.16.2.0/24`
- `172.16.3.0/24`

Confirm with:

```bash
python3 - <<'PY'
import ipaddress
nets=[ipaddress.ip_network(n) for n in
 ["172.16.0.0/24","172.16.1.0/24","172.16.2.0/24","172.16.3.0/24"]]
print(ipaddress.collapse_addresses(nets))
PY
```

### Lab 2 — IOS‑style summarization awareness

In Packet Tracer/CML, advertise four loopbacks and configure a summary route on the edge:

```text
interface Loopback0
 ip address 172.16.0.1 255.255.255.0
! ... additional loopbacks ...
ip route 0.0.0.0 0.0.0.0 ...   ! not a summary — contrast
! EIGRP example idea:
! ip summary-address eigrp 1 172.16.0.0 255.255.252.0
```

Compare `show ip route` on a neighbor before/after.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Traffic to hole blackholed | Summary too broad | covered ranges vs reality |
| Table still huge | Non‑contiguous space | renumber for alignment |
| Suboptimal path | Summary vs specific mix | longest prefix match |
| Flap still visible | Specifics leaked | summarization boundary |

## Common traps / interview gotchas

- Supernetting ≠ “getting more hosts for one LAN” — that’s a larger subnet assignment; aggregation is primarily a **routing** concept.
- Non‑contiguous networks (e.g. `10.1.1.0/24` and `10.1.5.0/24`) don’t make a tight summary without including gaps.
- Always check: does the summary include addresses you **don’t** control?
- Auto‑summary to classful boundaries is old/dangerous — prefer manual, intentional CIDR summaries.
- Longest prefix match means a leftover /24 inside a /16 summary still wins locally.

## Mastery checklist

- [ ] Summarize four contiguous /24s into a /22
- [ ] Explain supernet vs subnet directionally
- [ ] Spot a discontinuous set that won’t summarize cleanly
- [ ] State one benefit and one risk of aggregation
- [ ] Tie address planning ([[VLSM]]) to summarizable design

## Related notes

- [[CIDR]] · [[VLSM]] · [[Subnet-Masks]] · [[IP Address]] · [[Routers]] · [[Packet]]
- ← [[03-Subnetting/Index|Subnetting]]
