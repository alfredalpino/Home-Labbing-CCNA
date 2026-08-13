# Tables from session 8e6371ab-8660-425c-a4c2-019d7280c2da

## Table 1

| System | Levels that exist | What it is | Job title meaning? |
|--------|-------------------|------------|--------------------|
| **Support / NOC / SOC tiers** | **L1, L2, L3** (rarely L4) | Ticket escalation depth | **Yes** — this is what your JDs mean |
| **OSI model** | **Layer 1–7 only** | How networks are designed (Physical → App) | **No** — technical layers, not seniority |
| **Big Tech IC ladder** | e.g. Google L3–L10+, Amazon L4–L12 | Company-internal SWE/eng ranks | **Only inside that company** — not NOC industry standard |

## Table 2

| Level | Typical title | What you do | Escalates to |
|-------|---------------|-------------|--------------|
| **L1** | NOC Analyst, L1 Support, Helpdesk Network | Monitor alerts, basic checks, password/CPE basics, open/close tickets, follow runbooks | L2 |
| **L2** | Network Engineer, L2 NOC | Real troubleshooting: VLANs, routing, ACLs, CPE, configs, RCA notes | L3 / vendor |
| **L3** | Senior NE, L3 Specialist | Hard faults, design changes, complex OSPF/BGP, architecture fixes, mentor L1/L2 | Architect / vendor TAC |
| **L4** (rare) | Architect / vendor TAC / engineering | Design authority, product bugs, major changes | N/A |

## Table 3

| Layer | Name | Examples |
|------:|------|----------|
| 1 | Physical | Cables, optics, power, link lights |
| 2 | Data Link | Ethernet, MAC, VLANs, STP, switches |
| 3 | Network | IP, routing, OSPF, ACL |
| 4 | Transport | TCP/UDP, ports |
| 5 | Session | Session management |
| 6 | Presentation | Encryption/encoding |
| 7 | Application | HTTP, DNS, SMTP |

## Table 4

| | **NOC** | **SOC** |
|--|---------|---------|
| Full form | **Network** Operations Center | **Security** Operations Center |
| Mission | Keep network **up** (availability, latency, links, CPE) | Keep org **safe** (threats, alerts, IR) |
| Day job | Monitoring, tickets, L1–L3 network triage | SIEM alerts, malware, phishing, hunt |
| Your fit | **Primary target** (Network/NOC/Analyst) | Adjacent only via Security+ / ACLs — not the Month-1 spine |

## Table 5

| Level (approx) | UAE (AED/mo) | Saudi (SAR/mo) | Rough USD/mo |
|----------------|--------------|----------------|--------------|
| Entry / L1–junior NE (0–2y) | 8k–13k | 7k–11k | ~$2.1k–$3.5k |
| Mid / L2–NE (3–6y) | 13k–22k | 11k–20k | ~$3.5k–$6k |
| Senior / L3 (7–12y) | 22k–35k | 20k–32k | ~$6k–$9.5k |
| Principal / Head (12y+) | 35k–52k | 32k–48k | ~$9.5k–$14k |

## Table 6

| Level | Typical INR |
|-------|-------------|
| L1 NOC / fresher NE | ₹2.5–6 LPA |
| L2 / Network Engineer | ₹5–12 LPA |
| Senior / L3 | ₹12–20 LPA |
| Architect / Lead | ₹18–35 LPA (top end higher at product/GCC captives) |
| “Average” mid NE | often cited ~₹7–13 LPA |

## Table 7

| Reality | Typical pay |
|---------|-------------|
| India-based for US company (offshore / contractor) | roughly **$12k–$60k USD/year** depending on L1→senior; many NOC/senior contractor postings cluster ~**$12–$45/hr** or India-local CTC |
| True US-domestic remote NE (US hire, US rates) | often **~$80k–$150k+** — usually needs US work auth / US location |

## Table 8

| Level | Typical titles | What you do | How far it goes |
|-------|----------------|-------------|-----------------|
| **L1** | NOC Analyst, Network Support L1, Helpdesk Network | Monitor alerts, basic triage, reboot/check CPE, ticket docs, escalate by runbook | Industry standard entry |
| **L2** | NOC L2, Network Support Engineer | Deeper diagnostics, config changes within scope, ACL/VLAN/OSPF basics, vendor/ISP escalation hygiene | Most “Network Support / NOC Engineer” roles |
| **L3** | Network Engineer, Senior NOC, L3 Engineer | Complex RCA, design tweaks, advanced routing/security, owns hard incidents | Last common “L” number |
| **L4** (rare) | Escalation eng / SME / TAC-style | Vendor/TAC deep dive, rare/complex break-fix | Not universal |
| **L5–L12** | — | **Not a network-ops standard.** That’s Big Tech **IC leveling** (Google L3–L8, Meta/Amazon similar). Don’t map your career to “become L10.” |

## Table 9

| | **NOC** (Network Operations Center) | **SOC** (Security Operations Center) |
|---|-------------------------------------|--------------------------------------|
| Mission | Keep network **up** (availability, latency, circuits) | Keep org **safe** (threats, malware, abuse) |
| Tools | NMS, SNMP, NetFlow, tickets, ISP portals | SIEM, EDR, threat intel, IR playbooks |
| Your fit | **Your spine** — Tikona L1/L2/CPE + labs | Adjacent (Security+ helps); not Month-1 north star |

## Table 10

| Now | Next | Later (after proof) |
|-----|------|---------------------|
| Ship LAB-01…06 public | Apply L1/L2 NOC / Network Support / Analyst (GCC + remote) | Depth on job + optional CCNP / AZ-700 / automation — **after** labs, not instead of them |

## Table 11

| Band | Typical roles | Approx CTC |
|------|---------------|------------|
| Entry / L1 | NOC L1, junior NE | **₹3–6 LPA** |
| Mid / L2 | NOC L2, Network Engineer | **₹6–12 LPA** (strong metros/carriers higher) |
| L3 / Senior | Senior NOC / NE | **₹12–22 LPA** |
| Architect / lead | Principal / Architect | **₹22–40+ LPA** (top end rare) |

## Table 12

| Band | Approx monthly | Rough annual (AED) |
|------|----------------|--------------------|
| Junior / L1 NOC | **AED 3k–7k** | ~36k–84k |
| Mid Network / NOC | **AED 5.5k–12k** | ~66k–144k |
| Senior / L3 | **AED 12k–20k+** | ~144k–240k+ |

## Table 13

| Band | Approx USD / year |
|------|-------------------|
| Entry / NOC-ish | **~$55k–$80k** (PayScale NOC avg ~$72k) |
| Mid Network Engineer | **~$95k–$145k** |
| Senior / Architect | **~$125k–$200k+** |

## Table 14

| Band | Realistic | Notes |
|------|-----------|--------|
| Support / ops / junior net | **~$15k–$40k/yr** or **₹8–25 L** | Location-adjusted common |
| Mid network / NetOps-ish | **~$35k–$70k/yr** (rough) | Scarcer than SWE remote; often MSP/EOR |
| Strong senior contractor | Can approach **$60k–$100k+** | Rare; English + proof + timezone |

## Table 15

| Cert | What it proves | Fit with your stack |
|------|----------------|---------------------|
| **CCNA** | On-prem L2/L3, VLANs, OSPF, ACLs, ops | Core |
| **Security+** | Security fundamentals | Edge/hardening mindset |
| **AZ-700** | Azure networking: VNets, peering, VPN/ExpressRoute, load balancing, Private Link, network security | **Direct graft** — cloud side of the same job |
| **AZ-104** | Compute, storage, identity, monitoring, *some* networking | Breadth admin — weaker network signal |

## Table 16

| Cert | Role it proves | Fit with CCNA + Sec+ |
|------|----------------|----------------------|
| **AZ-104** | Azure **Administrator** — identity, storage, compute, some VNets, monitoring | Broad cloud admin. Overlaps “I can run Azure,” not “I own networking.” |
| **AZ-700** | Azure **Network Engineer** — VNets, hybrid connectivity, load balancing, private access, Azure network security | Direct graft: CCNA = on-prem L2/L3; Sec+ = security mindset; AZ-700 = **Azure/hybrid network design & ops** |

## Table 17

| What actually gets interviews | What doesn’t |
|-------------------------------|--------------|
| CCNA (already table stakes on many UAE junior Network Engineer JDs) | A fourth/fifth badge with empty GitHub |
| Ticket/ops stories (Tikona L1/L2/CPE) + public labs | “Cert stack” with no verify outputs |
| Daily applications | Waiting until you feel “fully certified” |

## Table 18

| You have | What it proves | What’s still missing on GCC Network JDs |
|----------|----------------|----------------------------------------|
| **CCNA** | Cisco L2/L3, ACL thinking, ops language | Depth (CCNP) or multi-vendor edge |
| **Security+** | Security fundamentals / compliance language | **Hands-on NGFW / perimeter** (Fortinet / Palo / FTD) that JDs list constantly |
| Gap | — | Firewall/SD-WAN product skill **or** Cisco professional depth **or** Azure hybrid networking |

## Table 19

| Rank | Cert | Complements CCNA+Sec+? | GCC hiring signal | Time/cost reality | Instant-job effect |
|------|------|------------------------|-------------------|-------------------|--------------------|
| **1** | **Fortinet FCP / NSE4 FortiGate path** | **Best gap-filler** — turns Sec+ into FortiGate policies/VPN/SD-WAN | Very high in mid-market, MSSPs, SIs; many JDs name Fortinet ([example UAE NE requiring NSE](https://www.gulftalent.com/uae/jobs/network-engineer-573392)); [GCC market notes](https://menajobs.me/job-description/network-engineer) | ~2–3 months typical; cheaper than CCNP | **Highest ROI per month** of study among serious options — still not “instant” |
| **2** | **CCNP Enterprise** | Deepens CCNA (not Sec+); classic NE ladder | Cisco still ~55–65% GCC enterprise share; CCNP increasingly mid-level currency; ~15–25% pay premium cited in [GCC salary comparison](https://menajobs.me/salary-comparison/network-engineer) | ENCOR alone often **3–5+ months**; full CCNP longer/harder | Strong for mid/senior titles; overkill/slow if you need an L1/L2 offer *now* |
| **3** | **AZ-700** ([Azure Network Engineer](https://learn.microsoft.com/en-us/credentials/certifications/azure-network-engineer-associate/)) | Best **Microsoft** complement; hybrid/VNet/ExpressRoute/Azure net security | Growing; Azure strong in UAE enterprise/gov ([UAE cloud cert market](https://profilenova.com/aws-azure-google-cloud-certification-uae-2026/)); appears as must on some hybrid/security NE roles | Often ~4–8 weeks if you already know Azure + networking | Great differentiator for hybrid/cloud NE — **weak** as sole “get NOC hired” lever |
| **4** | **Palo Alto PCNSA → PCNSE** | Excellent Sec+ bridge; banking/gov prestige | Strong in banks/gov; recruiters often want **PCNSE** not just PCNSA | Harder/slower than Fortinet for first firewall cert | High pay niches; fewer volume openings than Fortinet mid-market |
| **5** | **AZ-104** ([Azure Administrator](https://learn.microsoft.com/en-us/credentials/certifications/azure-administrator/)) | Weak network complement (admin generalist) | Volume in *cloud admin* JDs, not Network/NOC spine | — | Skip if already done; wrong “third” for CCNA+Sec+ network story |
| **Skip / later** | CySA+, PenTest+, CISSP, CCIE, AWS ANS | Wrong lane or too senior | CISSP/CCIE = senior filters; AWS ANS less UAE-gov than Azure | CCIE = years | Don’t chase for Month-1 hireability |

## Table 20

| Target role | Best next cert (after labs) |
|-------------|-----------------------------|
| L1/L2 NOC / Network Support (now) | **None** — apply + ship LAB-01…06 |
| Network Engineer (enterprise / SI / telco) | **CCNP Enterprise** |
| Network + firewall / MSSP / GCC mid-market | **Fortinet FCP** |
| Hybrid / Azure-heavy enterprise (UAE gov/bank cloud) | **AZ-700** |
| Bank / gov NGFW specialist | **PCNSA → PCNSE** |

## Table 21

| Cyber lane | Pick this next | Why |
|------------|----------------|-----|
| **Network Security Engineer** (best use of CCNA + Sec+) | **Fortinet FCP (FortiGate)** | Turns Sec+ into firewall/VPN/SD-WAN skills GCC shops hire for |
| **SOC / Security Analyst** | **CompTIA CySA+** | Natural next after Security+; SIEM, detection, triage |
| **Cloud security** | **Microsoft SC-200** or **AZ-500** | Only if Azure/SOC-cloud is the target (you already have Azure admin in the pack) |
| **Offensive / pen test** | **PenTest+** (or wait) | Later; weak for first hire without labs/experience |

## Table 22

| Piece | Role |
|-------|------|
| CCNA | Core network hire filter |
| Security+ | Security language / baseline |
| Fortinet FCP | Firewall/SD-WAN product skill GCC JDs ask for |
| Labs + experience | What actually converts interviews |

## Table 23

| Path | What it buys | Fit for you |
|------|----------------|-------------|
| **CySA+ → cyber/SOC** | SIEM, alerts, threat analysis | Wrong lane. Drops ISP/NOC proof. |
| **CCNP (later)** | Deeper Network Engineer signal | Aligns with spine — **after** labs, not instead of them. |
| **Stay network + Sec+ graft** | ACLs, hardening, edge (LAB-03/04); optional Fortinet later | What your pack allows. |

## Table 24

| Path | What it optimizes for | Fit for you |
|------|------------------------|-------------|
| **CCNP / network labs** | Network Engineer, NOC, L2/L3 ops | Your north star (GCC Network/NOC/Analyst) |
| **CySA+** | SOC analyst, threat detection, SIEM | Different career — adjacent, not your Month-1 target |

## Table 25

| Cred | How it helps red team / pen test |
|------|----------------------------------|
| CCNA / CCNP | Routing, VLANs, ACLs, pivoting, “how the network actually breaks” |
| Security+ | Baseline security language / compliance literacy |
| Fortinet FCP | Firewall/VPN reality — what defenders put in your way |

## Table 26

| Goal | CySA+? |
|------|--------|
| Pen tester / red team / DEF CON CTF | **Not required. Defer or skip.** |
| SOC analyst / blue team first job | **Yes — then**, after Sec+, if you want SOC entry |
| Purple team long-term | Optional later, after you can already attack |

## Table 27

| If you want… | Do this |
|--------------|---------|
| Red team / pen test soon | Offensive labs + eJPT/PNPT/OSCP. **Skip CySA+.** |
| Any cyber job faster (blue) | Sec+ → **CySA+** → SOC → later offensive |
| GCC Network job first, cyber later | Ship network labs, get hired, offensive nights — CySA+ still optional |

## Table 28

| Team | Job | Mindset | Typical work |
|------|-----|---------|--------------|
| **Red team** | Attack like a real adversary | “Can we get in and stay in?” | Phishing, exploitation, AD attacks, C2, reporting how you broke in |
| **Blue team** | Detect and stop attacks | “Can we see it and contain it?” | SIEM, alerts, IR, hardening, threat hunting |
| **Purple team** | Attack + defend together | “Attack, then improve detection” | Red runs a technique; blue tunes detections; both share notes |

## Table 29

| Step | Cert | Why | When you’re ready |
|------|------|-----|-------------------|
| **0** | *(no cert)* TryHackMe → Hack The Box | Builds actual skill | Start **now**; parallel forever |
| **1** | **eJPT** (INE) *or* **PJPT** (TCM) | First offensive proof; gentle | After ~1–2 months solid labs |
| **2** | **PNPT** (TCM) *or* **CRTO**-prep style AD basics | Real-world-ish pentest + AD | After you can own basic HTB boxes |
| **3** | **OSCP** (OffSec) **or** **CPTS** (HTB) | Industry “serious junior/mid pentester” signal | After many writeups + AD practice |
| **4** | **CRTO** / **CRTO II** (ZeroPoint) *or* **OSEP** | Red-team / AD / evasion depth | After OSCP/CPTS-level comfort |
| **5** (optional) | **OSWE** / web deep, or cloud (AWS/Azure offensive) | Specialize | After you know your niche |

## Table 30

| Skip / deprioritize | Why |
|---------------------|-----|
| CySA+ | Blue team |
| CEH as main goal | Weak hands-on signal vs OSCP/PNPT |
| CISSP early | Manager/broad; not offensive entry |
