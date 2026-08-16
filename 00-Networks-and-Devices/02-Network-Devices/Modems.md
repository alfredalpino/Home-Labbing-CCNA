---
tags: [network-devices, networking, ccna, modem]
aliases: [Modem, Cable Modem, DSL Modem, ONT]
layer: Physical / WAN access
---

# Modems

## Learning objectives

- Define modem as modulator/demodulator for access technologies
- Contrast modem vs [[Routers]] vs ONT
- Understand SOHO “modem/router” combos
- Place the modem at the WAN edge of a home/branch diagram

## One-sentence definition

> A **modem** converts digital data to the analog or encoding format required by an access network (cable, DSL, dial-up historically) and back — the on-ramp translator between your CPE and the provider’s last mile.

## Analogy

> Your devices speak **digital English**. The ISP’s cable plant might speak **radio-frequency Spanish**. A modem is the **interpreter at the border checkpoint**: it translates so both sides can talk. A [[Routers|router]] is the **customs officer deciding which trucks ([[Packet]]s) may enter which cities (subnets)**. Many home boxes hire one person to do both jobs.

## Why it matters

When “Internet is down,” first question: is it modem/ONT sync (WAN light) or LAN/routing/Wi‑Fi? Wrong layer = wrong reboot ritual.

## Deep dive

### Mental model

```text
ISP plant ── Modem/ONT ── Ethernet ── Router ── LAN/Wi‑Fi
              ▲
         signal lock / provisioning
```

### Types you’ll meet

| Device | Access |
|--------|--------|
| Cable modem | DOCSIS HFC |
| DSL modem | Phone copper |
| Fiber ONT | Optical (often not called “modem,” same edge role) |
| Cellular modem | LTE/5G |

### Combo units

ISP gateway = modem + router + switch + AP. Bridge mode turns it into mostly modem, letting *your* router own NAT/Wi‑Fi.

### On the wire

LAN side looks like Ethernet with a public or CGNAT address on the router WAN port. Provider side is technology-specific RF/optics.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Classic modem | L1 | Signal conversion |
| Gateway box | L1–L3+ | Often multiple roles |

## Lab exercises

### Lab 1 — Read the lights

Identify Power / Downstream / Upstream / Online on a cable modem story; map to “PHY sync vs IP provisioning.”

### Lab 2 — Boundary sketch

Draw: coax/fiber → modem/ONT → Ethernet → your router WAN → LAN. Label [[WAN]] vs [[LAN]].

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| WAN light down | Plant/signal/provisioning | modem logs, ISP outage |
| WAN up, no browsing | Router/DNS/NAT | router WAN IP, DNS |
| Frequent renego | SNR/plant issues | modem event log |

## Common traps / interview gotchas

- ONT isn’t always called a modem — same conceptual edge translator.
- Rebooting Wi‑Fi AP won’t fix DOCSIS loss of sync.
- Bridged modem + third-party router: double-NAT if both route.

## Mastery checklist

- [ ] Interpreter analogy vs router role
- [ ] Place modem on a home diagram
- [ ] Contrast modem-only vs gateway combo
- [ ] Triage WAN sync vs LAN problem

## Related notes

- [[Routers]] · [[WAN]] · [[LAN]] · [[Access Points]] · [[Transmission Media Types]]
- ← [[02-Network-Devices/Index|Network Devices]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
