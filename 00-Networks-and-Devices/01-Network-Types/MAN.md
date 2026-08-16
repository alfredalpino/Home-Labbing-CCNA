---
tags: [network-types, networking, ccna, man]
aliases: [Metropolitan Area Network, MAN]
layer: Scope / architecture
---

# MAN

## Learning objectives

- Place MAN between [[LAN]] and [[WAN]] on the distance ladder
- Give real examples (city fiber rings, metro Ethernet)
- Avoid overusing “MAN” when LAN/WAN is clearer
- Relate metro Ethernet to enterprise design language

## One-sentence definition

> A **MAN** (Metropolitan Area Network) spans a city or metro region — larger than a single LAN/campus, smaller than a classic long-haul WAN — often built on metro fiber/Ethernet services.

## Analogy

> If LAN is neighborhood streets and WAN is cross‑country interstate, a MAN is the **city metro / ring road system**: multiple campuses or buildings across town share a high-capacity urban fabric, still “local-ish,” but not one office switch stack.

## Why it matters

You’ll hear “metro Ethernet,” “dark fiber across the city,” or “campus + metro ring.” Exam questions still list MAN as a standard type. In jobs, precise SLA/provider terms matter more than the acronym — but you must recognize it.

## Deep dive

### Mental model

```text
Building A LAN ─┐
Building B LAN ─┼── Metro Ethernet / city fiber ring ──► optional WAN handoff
Building C LAN ─┘
```

### Characteristics

| Trait | Typical MAN |
|-------|-------------|
| Distance | City / metro (tens of km) |
| Speed | Often high (1G–100G class possible) |
| Provider | City carrier, utility, ISP metro |
| Use cases | Multi-building org, universities, municipal nets |

### MAN vs large LAN vs small WAN

- One org flooding broadcasts across a whole city on L2 = *dangerous extended LAN*, even if marketed as metro.
- Proper design often routes between sites (L3) even on metro fiber.

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| Scope term | Cross-layer | City-scale interconnect |
| Delivery | Often L2 service or L3 VPN | Depends on product |

## Lab exercises

### Lab 1 — Classify your school/office

Is multi-building connectivity LAN extension, MAN service, or WAN? Write one sentence justification.

### Lab 2 — Provider language hunt

Find a “Metro Ethernet” product page; note bandwidth and whether it’s E-Line/E-LAN (point-to-point vs multipoint).

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Site-to-site down in-city | Metro handoff / fiber cut | CE links, provider NOC |
| Broadcast storms multi-site | Accidental L2 extension | break into L3, storm control |

## Common traps / interview gotchas

- MAN is less common in daily speech than LAN/WAN — don’t force the label.
- “Metro” distance ≠ permission to build one giant Layer‑2 domain.
- WLAN city-wide mesh is *not* automatically a MAN in the classic wired sense.

## Mastery checklist

- [ ] Place MAN on the LAN–MAN–WAN ladder
- [ ] Give one real metro example
- [ ] Explain risk of city-wide L2
- [ ] Contrast metro Ethernet vs Internet VPN

## Related notes

- [[LAN]] · [[WAN]] · [[Routers]] · [[Switches]] · [[VPN]]
- ← [[01-Network-Types/Index|Network Types]] · [[00-Networks-and-Devices/Index|Networks & Devices]]
