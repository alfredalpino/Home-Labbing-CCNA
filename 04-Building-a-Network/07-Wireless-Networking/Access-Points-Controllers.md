---
tags: [wireless, networking, ccna, access-point, wlc, controller]
aliases: [AP Controllers, Lightweight AP, Autonomous AP, Wireless LAN Controller, WLC]
layer: Architecture / management plane
---

# Access Points & Controllers

## Learning objectives

- Contrast **autonomous** vs **lightweight/controller-based** [[Access Points]]
- Explain what a wireless LAN controller (WLC) centralizes vs what stays at the AP
- Sketch CAPWAP-style tunnels at awareness level
- Choose a design story for SOHO vs enterprise [[WLAN]]

## One-sentence definition

> **AP architecture** is how you run radios: each [[Access Points|AP]] as a full local brain (**autonomous**), or as a remote radio managed by a central **controller** (**lightweight**), so SSIDs, RF, and policy stay consistent across a campus.

## Analogy

> Autonomous APs are **independent coffee carts** — each barista sets their own menu and prices; great for one cart, chaos for fifty. A controller is a **franchise HQ**: carts (lightweight APs) still brew on-site (RF/forwarding), but recipes, branding (SSIDs), and security policy come from HQ so every store tastes the same.

## Why it matters

Enterprise Wi‑Fi tickets are often “config drift” or “controller/AP join failed,” not just weak RSSI. CCNA expects you to know *why* controllers exist and how traffic still hits switches/VLANs like any [[LAN]].

## Deep dive

### Mental model

```text
Autonomous:
  Client ))) AP (local config) === Switch === Router

Lightweight:
  Client ))) AP ══ CAPWAP/control ══► Controller (WLC)
              \\
               === data path to switch/VLAN (local or tunneled, design-dependent)
```

### Comparison

| Aspect | Autonomous | Lightweight + controller |
|--------|------------|---------------------------|
| Config | Per AP (or scripts) | Central templates / profiles |
| Scale | Fine for few APs | Campus / multi-site |
| RF features | Limited / vendor tools | RRM, central monitoring |
| Failure domain | One AP | Controller HA matters |
| SOHO | Common (home gateway) | Overkill |

### Mechanism

1. Lightweight AP boots, discovers controller (DHCP option, DNS, broadcast — vendor-specific).
2. Secure join (certificates/keys); AP downloads image/config.
3. Client associates to AP radio; auth/policy may involve controller + RADIUS.
4. User data is bridged to the wired [[LAN]] (local switching) or tunneled per design.

### On the wire

Expect management/control traffic between AP and controller (often UDP-based tunnels such as CAPWAP in Cisco lore). Client data may appear as normal Ethernet on the access VLAN, or as encapsulated frames toward the WLC — **know your vendor’s default**.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Network Access + management overlay | RF access + control plane IP |
| OSI | 1–2 (user) / 3–4 (control) | Data at L2; join/control often IP/UDP |

## Lab exercises

### Lab 1 — Label your home box

Open your home gateway admin page. Note: integrated AP? separate mesh nodes? Is config local-only (autonomous-like) or cloud-managed (controller-as-a-service)?

### Lab 2 — Draw join path

Sketch: AP PoE switch port → management VLAN → controller IP. Mark where SSID maps to data VLAN. Compare to [[Access Points]] mental model.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| AP not joining WLC | Discovery/certs/time | DHCP option, DNS, [[NTP]], firewall |
| SSID missing on one AP | AP group / RF profile | controller assignment, AP up |
| Clients auth fail everywhere | Central policy/RADIUS | WLC AAA, not just one AP |
| Controller down, APs dark | No HA / local mode | failover design, AP mode |

## Common traps / interview gotchas

- “Controller” does not always mean all user data hairpins through the WLC (local switching is common).
- Autonomous ≠ obsolete — branch/SOHO and some OT still use it.
- Cloud-managed APs are still “controller-based”; the HQ just moved to SaaS.
- Don’t confuse AP Ethernet uplink issues with RF issues — link [[Access Points]] PoE/VLAN first.

## Mastery checklist

- [ ] Define autonomous vs lightweight in one sentence each
- [ ] Explain why enterprises want central policy
- [ ] Sketch AP → switch → controller discovery
- [ ] Link back to physical [[Access Points]] role in a [[WLAN]]

## Related notes

- [[Access Points]] · [[WLAN]] · [[WiFi-Standards]] · [[Roaming-and-Band-Steering]] · [[Wireless-Security]] · [[Switches]] · [[VPN]]
- ← [[07-Wireless-Networking/Index|Wireless Networking]] · [[04-Building-a-Network/Index|Building a Network]]
