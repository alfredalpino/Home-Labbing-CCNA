# Session 6a134408-48fb-408c-8378-461d7e04c03b__subagent__e81b52c0-dca4-4b8a-adfd-056f5f48082e

**Title:** Create a complete set of AI context / guardrail documents for Ubaid Ur Rahman (Alfred Alpino) so he can paste/feed them 

**Started:** Friday, Aug 7, 2026, 1:04 AM (UTC+5:30)

## Turn 1 — USER
_Timestamp: Friday, Aug 7, 2026, 1:04 AM (UTC+5:30)_

Create a complete set of AI context / guardrail documents for Ubaid Ur Rahman (Alfred Alpino) so he can paste/feed them into ChatGPT or any AI model and get consistent, high-quality help.

## Goal
Produce 4–6 markdown documents in `/Users/ubaid/Home-Labbing-CCNA/ai-context/` that together form a full "operating system" for any AI helping him. Cover: who he is, what he did, what he wants, certs, where he's going / not going, what to do / not do, how to do / not do — proper guardrails + full context.

## Source facts (use these; do not invent jobs/dates)

### Identity
- Name: Ubaid Ur Rahman (also Alfred Alpino)
- Email: hi@alubaid.xyz
- Phone: +91-8303796759
- Portfolio: https://alubaid.xyz (also www.alubaid.xyz)
- GitHub: github.com/AlfredAlpino
- LinkedIn: linkedin.com/in/alfredalpino
- Target geography: GCC (UAE, Saudi, Qatar, Oman, Kuwait) — onsite or remote; sponsorship OK
- Target roles: Network Engineer, NOC Engineer, Network Analyst
- Education: IGNOU Lucknow BCA (2022–present) — may be incomplete; lead with certs+labs if degree not finished. User may position as "no bachelor's but great work experience" depending on status.
- No bachelor's degree assumed for career strategy framing unless BCA is completed — still keep BCA on resume if real/ongoing.

### Assumed certifications (DONE — treat as completed for all docs)
- Cisco CCNA
- CompTIA Security+
- Microsoft Azure Administrator (AZ-104)
- ITIL Foundation
- Also has: Google IT Support (completed)

### Experience (from resume)
1. Torpedo Web, Delaware US — Remote — Software Engineer — Feb 2026 – Aug 2026 — delivered web systems end-to-end
2. 3Poch Labs, UAE — Remote — Research Analyst — May 2024 – Sep 2025 — monitoring workflows, founder dashboards, Python tooling ($58.9K volume)
3. Radarblock, UAE — Remote — Analyst, Founder's Office — Nov 2024 – Jan 2025 — KPI dashboards, stand-ups
4. Amazon, India — Remote — Virtual Customer Support Associate — Aug 2023 – Jan 2024 — SLA-driven triage
5. Tikona Infinet Ltd., India — Remote — IT Support Specialist (ISP Networking) — Dec 2022 – Mar 2023 — L1/L2 faults, CPE/router config, backbone escalation
6. Docket Care Systems, India — On-site — Computer Repair Technician — Jun 2022 – Sep 2022

### Skills / labs
- Access & Switching: L1/L2 troubleshooting, Ethernet, VLANs, STP, cabling
- Routing & IP: TCP/IP, IPv4 subnetting, static routing, OSPF foundations, ACL basics, DNS/DHCP
- Ops: ISP/CPE troubleshooting, router config, escalation hygiene, Packet Tracer
- Adjacent: network security, Azure networking, Bash, Python
- Labs: VLAN Segmentation, OSPF Single-Area, ISP Edge Playbook (must become DONE with public GitHub)

### Unified 30-day roadmap (from prior analysis) — THIS IS THE CANONICAL PATH
Spine: roadmap.sh Network Engineer
Month-1 grafts: Linux (networking), Shell/Bash, Cyber Security (network slice only), Terraform (networking), Docker basics, Cloudflare (DNS/Tunnel/WAF edge)
Practice: Azure hybrid (AZ-104 already done), Python/Netmiko/Ansible automation
Week 1: Deep L2/L3 beyond CCNA — VLAN/STP/OSPF/NAT/ACL/Wireshark — ship LAB-01, LAB-02
Week 2: Network security applied — firewall/VPN/segmentation — ship LAB-03 ISP playbook, LAB-04 VPN lab
Week 3: Azure hybrid + Terraform — ship LAB-05 hybrid on-prem↔Azure
Week 4: Automation + job package — LAB-06 Netmiko/Ansible; rewrite portfolio; apply daily
Daily: ~6h lab, 2h docs/GitHub, 1h applications
DROP for month 1: Design System, Software Architect, Software Design, DSA deep, CS full, PostgreSQL DBA, Technical Writer track, Prompt Engineering, AI Red Teaming, Code Review, API Security career track, full K8s, full DevOps/DevSecOps, AWS deep

### Portfolio rules
- Site is strong aesthetically; update credential language from "CCNA Candidate" to certified
- Differentiator = public GitHub lab monorepo with configs, pcaps, runbooks, videos — NOT UI redesign
- Crazy tips: failure gallery, hybrid diagram, NOC runbook, Cloudflare Tunnel optional

### Resume rewrite priorities when AI helps with resume
- Headline: Network Engineer · CCNA · Security+ · AZ-104 · ITIL
- Certs = Completed
- Labs = completed with GitHub links
- Amplify Tikona; don't let Torpedo/crypto outrank networking
- Keep BCA if real/ongoing; else remove

## Documents to create

Create these files under `/Users/ubaid/Home-Labbing-CCNA/ai-context/`:

1. `00-README.md` — How to use these docs with ChatGPT/Claude/Cursor (what to paste first, order, refresh cadence)
2. `01-identity-and-profile.md` — Who I am, contact, experience timeline, skills, certs, portfolio links, positioning (no fluff)
3. `02-goals-and-north-star.md` — What I want, 30-day outcome, 90-day outcome, career north star (top-notch network engineer), GCC target
4. `03-roadmap-and-curriculum.md` — Canonical path, week-by-week, labs to ship, which roadmap.sh tracks to keep/graft/drop
5. `04-ai-guardrails.md` — THE CRITICAL FILE: system-prompt style rules for any AI
   - Always assume certs are DONE
   - Always prioritize Network Engineer spine
   - Never push DSA/K8s/design systems/full DevOps rabbit holes in Month 1
   - Prefer labs+GitHub proof over new certs
   - How AI should answer (concrete, actionable, lab-first)
   - How AI should NOT answer (vague timelines, cert stacking, career pivoting away from networking)
   - Tone, honesty about 30-day ceiling, resume/portfolio update rules
   - Forbidden advice list + required advice patterns
6. `05-do-dont-playbook.md` — Explicit DO / DON'T / HOW / HOW NOT tables for learning, labs, portfolio, resume, job search, AI usage

Optional if useful: `06-prompt-templates.md` — ready-to-paste prompts ("help me plan today", "review this lab README", "rewrite this resume bullet", "mock NOC interview") that reference the other docs.

## Writing standards
- Write in second person OR first person consistently — prefer first person for identity docs ("I am...") so models treat it as user context; use imperative/"You must" for guardrails addressed TO the AI.
- Be concrete and ruthless. No motivational fluff.
- These docs will be fed to AIs — make them scannable with clear headings, bullets, tables.
- Include a short "Conflict resolution" section in guardrails: if user asks for something off-path, AI should warn once then comply only if user insists, or redirect to Month 2 backlog.
- Do NOT create empty placeholder files. Every file must be complete and usable today.
- After writing, list the files created and a one-line purpose each in your final response to the parent.

## Also
Read the resume PDF if needed at `/Users/ubaid/Home-Labbing-CCNA/Ubaid-Ur-Rahman-Network-Engineer.pdf` for accuracy. Do not modify the resume PDF or portfolio site — only create the ai-context markdown docs.

## Turn 2 — ASSISTANT
I'll build a complete AI context pack from your facts and resume, then write scannable guardrail docs under `ai-context/`.

## Turn 3 — ASSISTANT
Resume confirms the timeline; certs will be treated as done per your brief. Planning the doc set next, then writing all files.
