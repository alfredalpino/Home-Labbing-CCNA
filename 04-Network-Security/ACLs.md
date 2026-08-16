---
tags: [network-security, acls, networking, ccna]
aliases: [ACL, Access Control List, Access Control Lists]
layer: Policy on devices
---

# ACLs

## Learning objectives

- Define ACLs as ordered permit/deny policy lists
- Master first-match logic and implicit deny (Cisco-style)
- Apply ACLs on interfaces with direction (in/out)
- Troubleshoot with counters and careful change control

## One-sentence definition

> An **ACL** (Access Control List) is an ordered set of permit/deny rules that a device uses to filter traffic — commonly by IP addresses, protocols, and ports — applied to interfaces, services (VTY), or features (NAT, QoS matches).

## Analogy

> An ACL is a **bouncer’s checklist read from top to bottom**. The first line that matches the guest decides fate; lower lines never get read for that guest. If nobody matches, many venues have an unspoken rule: **no entry** (implicit deny). Order isn’t bureaucracy — order *is* the policy.

## Why it matters

ACLs are the lingua franca of network filtering on routers, switches (ported ACLs), firewalls (policy cousins), and cloud security groups (related idea). Mis-ordered ACLs cause some of the most embarrassing outages in the field.

## Deep dive

### Mental model

```text
Packet → evaluate statements top-down → first match wins → stop
End of list → implicit deny (platform-dependent wording)
```

### Standard vs extended (Cisco teaching)

| Kind | Matches | Typical use |
|------|---------|-------------|
| Standard | Source IP mainly | Simple filters, some routing tricks |
| Extended | Src/dst IP, proto, ports, etc. | Real service control |

### Direction matters

| Direction | Meaning |
|-----------|---------|
| Inbound | As traffic enters an interface |
| Outbound | As traffic leaves an interface |

Always ask: “From whose perspective?” Draw the arrow.

### ACL vs firewall object-policy

ACLs are often stateless packet filters ([[Packet Filtering Firewall]]). Firewalls may wrap similar ideas with state, apps, and users ([[Stateful Inspection Firewall]], [[Next-Generation Firewall]]).

### On the wire / verification

```text
show access-lists
show ip interface
# Watch hit counters while testing
```

Lab: generate traffic that should match line N and confirm counters increment.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Typically | L3–L4 fields | Classic IP ACLs |
| Also | Control-plane ACLs | Protect device CPU |

## Lab exercises

### Lab 1 — VTY protection

Permit SSH only from your management host; deny others; verify with a second host.

### Lab 2 — Order bug

Intentionally put `permit ip any any` above a deny; document why the deny never hits; fix.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Suddenly nothing passes | Implicit deny / wrong ACL | bind, direction, counters |
| One service broken | Port/proto wrong | extended ACL lines |
| Works one direction | Direction or return traffic | stateful vs ACL, reverse path |
| ACL “does nothing” | Not applied / wrong iface | running-config interfaces |

## Common traps / interview gotchas

- First match wins — forever.
- Applying ACL outbound on the wrong interface is a classic facepalm.
- “Deny host then permit any” vs opposite order — draw it.
- ACL for NAT/QoS classification may not filter; feature context matters.

## Mastery checklist

- [ ] Checklist/bouncer analogy
- [ ] Explain first-match + implicit deny
- [ ] Apply and verify an extended ACL in lab
- [ ] Relate ACL to packet filtering firewalls

## Related notes

- [[Packet Filtering Firewall]] · [[Routers]] · [[Port]] · [[TCP]] · [[UDP]] · [[ICMP]] · [[Zero Trust Architecture]]
- ← [[04-Network-Security/Index|Network Security]]
