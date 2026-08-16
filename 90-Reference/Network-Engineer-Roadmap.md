# Network Engineer Roadmap

**Verdict:** Do not try all 25 roadmaps. Make [Network Engineer](https://roadmap.sh/network-engineer) the spine, graft only the pieces that make you hireable in 30 days, and ship public lab proof. Certs are assumed done — from now on, **labs + GitHub + interview fluency** matter more than more certificates.

One month will not make you a senior CCNP architect. Done hard, it *can* make you a standout junior/mid Network Engineer / strong NOC→NE hire for GCC roles — stronger than most “CCNA + no portfolio” applicants.

---

## Which roadmaps to keep vs kill

| Priority | Roadmaps | Why |
|---|---|---|
| **Spine** | Network Engineer | Your whole job: L2/L3, routing, security, VPN, HA, packet analysis, cloud networking, automation |
| **Month-1 grafts** | Linux (networking), Shell/Bash, Cyber Security *(network slice only)*, Terraform *(networking)*, Docker *(basics)*, Cloudflare *(DNS/Tunnel/WAF edge)* | These show up in real NE / hybrid / edge ops jobs |
| **Practice, not “study the roadmap”** | Azure (you already have AZ-104), Python automation | Build VNets/VPN/Terraform; Netmiko/Ansible scripts |
| **Month 2+ only** | AWS deep, Kubernetes, DevOps/DevSecOps full, System Design | Useful later; will dilute this sprint |
| **Drop now** | Design System, Software Architect, Software Design, DSA deep, CS full, PostgreSQL DBA, Technical Writer track, Prompt Engineering, AI Red Teaming, Code Review, API Security career track | Wrong career for this month |

---

## Your one-month roadmap (certs done → learning starts)

**Daily rhythm (≈9 hrs):** 6h lab/build · 2h write-up + GitHub · 1h applications / interview drills  
**Weekly output rule:** every Sunday, something public on GitHub with configs + failure notes + screenshots.

### Week 1 — Beyond CCNA memory (deep L2/L3)

Close the gaps the Network Engineer roadmap puts after “basics”:

- Multi-switch VLANs, trunks, inter-VLAN, STP failure & recovery
- OSPF: adjacency, LSDB, multi-area basics, route selection
- NAT/PAT, ACLs, DHCP/DNS break/fix
- Wireshark methodology: capture → filter → prove the fault

**Ship:**

- `LAB-01` VLAN Segmentation — **done**, public repo
- `LAB-02` OSPF Single-Area — **done**, public repo
- Short Loom/YouTube: “break STP / fix OSPF” walkthrough

### Week 2 — Network security that Security+ unlocked

Take Cyber Security roadmap topics that are *network*, not CTF:

- Firewall types, stateful vs NGFW
- Site-to-site + remote-access VPN (IPSec vs SSL)
- Segmentation / DMZ / Zero Trust *as network design*
- IDS/IPS awareness + ACL hardening playbooks

**Ship:**

- `LAB-03` ISP Edge Playbook (Tikona-style L1→L2→CPE→escalate) — written runbook
- `LAB-04` Site-to-Site VPN + segmented VLANs — configs + packet captures

### Week 3 — Hybrid cloud networking (your AZ-104 edge)

This is how you beat “CCNA-only” candidates in GCC enterprise jobs:

- Azure: VNets, subnets, peering, NSGs, VPN Gateway, UDRs
- ExpressRoute *concepts* (interview fluency)
- Terraform: VNet + NSG + VPN module (`plan`/`apply`/`destroy`)
- Light AWS VPC compare (so you speak multi-cloud)
- Cloudflare edge: DNS, Tunnel, WAF basics — not Workers career path

**Ship:**

- `LAB-05` Hybrid: on-prem sim ↔ Azure VPN Gateway (diagram + Terraform + verify routes)

### Week 4 — Automation + job package

From Network Engineer roadmap “Network Automation” + Linux/Bash:

- Bash networking toolkit: `ip`, `ss`, `tcpdump`, scripts
- Python + Netmiko (or Ansible) to push VLAN/ACL configs
- Docker networking basics only (bridge, ports, not K8s)
- Interview drills: subnetting under pressure, “how do you isolate this outage?”
- Apply daily to Network Engineer / NOC / Network Analyst roles

**Ship:**

- `LAB-06` Automation demo repo (script + before/after config)
- Resume + portfolio fully rewritten for **certified** status
- 20+ targeted applications that week

---

## Resume analysis (current PDF)

What’s already strong:

- Clear NE target, GCC intent, Tikona ISP edge story
- Skills mapped by layer (Access / Routing / Ops)
- Lab section exists (rare for juniors)

What must change *immediately* if certs are done:

1. **Headline:** drop “Cisco CCNA Candidate” → `Network Engineer · CCNA · Security+ · AZ-104 · ITIL`
2. **Summary:** stop “building toward CCNA.” Lead with certs + ISP ops + hybrid Azure.
3. **Certs block:** mark all four **Completed** (add dates).
4. **Labs:** nothing left as “In progress / Queued.” Completed labs with GitHub links beat another cert.
5. **Tikona bullets:** make them metric/method heavy (SLA, triage loop, devices, escalation hygiene) — that’s your real networking proof.
6. **Torpedo / crypto roles:** keep 1 line each for “ships systems / ops under pressure,” don’t let them outrank networking.
7. **Education:** resume shows BCA in progress; you said “no bachelor’s.” If BCA is real and ongoing, keep it. If not, remove it and lead harder with certs + labs. Degree is not required for NE if proof is loud.
8. **Adjacent skills:** promote Azure networking, Bash, Python, Terraform (after Week 3) out of “studying.”

---

## Portfolio tips ([alubaid.xyz](https://alubaid.xyz)) — what would be “crazy”

The site design is already distinctive. The gap is **proof**, not polish.

Update first (day 1–2):

- Title: stop “CCNA Candidate”
- Certification Track: all four **DONE**
- Focus Domains: Security+ / AZ-104 as completed, not “studying”

Crazy differentiators (do these in the 30 days):

1. **Public GitHub monorepo** `network-lab-bench` with LAB-01…06, configs, topologies, pcaps, README runbooks
2. **Clickable Lab Bench** — each card opens the repo + a 2–4 min video of you breaking/fixing it
3. **Live “failure gallery”** — screenshots of broken OSPF adjacency, STP loop symptoms, ACL denying traffic, then the fix
4. **Hybrid diagram** — Packet Tracer/GNS3 edge ↔ Azure VNet (this is rare on junior portfolios)
5. **NOC-style runbook page** — Tikona triage as a public playbook (shows ops maturity)
6. Optional wild card: Cloudflare Tunnel protecting a homelab dashboard — proves edge/DNS/security thinking

Do **not** spend the month redesigning the UI. Ship artifacts.

---

## Exact to-do list (start today)

1. Rewrite resume headline + certs to **Completed**
2. Update alubaid.xyz credential language to match
3. Create GitHub `network-lab-bench`
4. Finish LAB-01 + LAB-02 this week (public)
5. Block calendar for Weeks 1–4 as above — no DSA, no K8s rabbit holes
6. Apply to 5 roles/day starting Week 2 (don’t wait for “perfect”)
7. Record one lab video per week
8. End of month: 6 labs live + resume/portfolio aligned + 50+ applications out

---

**Bottom line:** Religiously follow the Network Engineer roadmap, with Week 2 security, Week 3 Azure+Terraform hybrid, Week 4 automation — and put every lab on GitHub. That is the unified path. Everything else on your list waits until you have a job, or Month 2.
