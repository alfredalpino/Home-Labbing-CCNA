# How to use these extracted roadmaps

This folder is an **offline study library**, not a second curriculum. Your living plan stays in [`../Network-Engineer-Roadmap.md`](../Network-Engineer-Roadmap.md) and [`../ai-context/03-roadmap-and-curriculum.md`](../ai-context/03-roadmap-and-curriculum.md). Use these extracts to look up topics, open curated links, and stay aligned with the Network Engineer spine.

---

## 1. What each file is for

Inside every roadmap folder under `network-engineering-roadmap/...`:

### `outline.md` — primary study file

- Full section → topic → subtopic tree
- Short description for each node (from roadmap.sh content)
- Resource links under each node, tagged by type:
  - `[official]` — vendor / standards docs
  - `[video]` — YouTube / course videos
  - `[article]` — explainers
  - `[course]` / `[book]` / `[opensource]` / `[roadmap]` — as tagged upstream

**Use when:** learning a topic, building a lab checklist, or drilling interview fluency.

### `links.md` — bookmark / audit file

- Deduplicated flat list of every resource URL
- Sorted by type then title

**Use when:** you only need URLs (browser bookmarks, link checkers, “what videos exist for X”).

### `data.json` — for scripts / AI / filtering

- Structured sections, items, resources, stats, related roadmaps

**Use when:** searching programmatically, generating week plans, or asking an agent to filter nodes.

---

## 2. Which folder to open

| Goal | Open |
|------|------|
| Main career spine (L2/L3, VPN, HA, cloud networking, certs) | [`network-engineering-roadmap/network-engineer/`](network-engineering-roadmap/network-engineer/) |
| CLI, files, systemd, Linux networking basics | [`network-engineering-roadmap/linux/`](network-engineering-roadmap/linux/) |
| Security overlay (firewall, Zero Trust, attacks, IR) | [`network-engineering-roadmap/cyber-security/`](network-engineering-roadmap/cyber-security/) |
| Scripting, pipes, automation for labs | [`network-engineering-roadmap/shell-bash/`](network-engineering-roadmap/shell-bash/) |
| Docs craft (runbooks, how-tos, structure — few external links) | [`network-engineering-roadmap/technical-writer/`](network-engineering-roadmap/technical-writer/) |

Index of all five: [README.md](README.md)

---

## 3. Recommended workflow (daily)

Match your existing rhythm (~6h lab / 2h docs / 1h applications):

1. **Pick one spine section** from Network Engineer `outline.md` (e.g. Switching, OSPF, VPN).
2. **Graft helpers only if needed**
   - Linux networking / troubleshooting → Linux outline  
   - Automate verify steps → Shell/Bash outline  
   - ACL / firewall / VPN hardening → Cyber outline (**network slice only**)
3. **Lab it** in GNS3 / Packet Tracer / Azure as per current LAB-0x.
4. **Document it** using Technical Writer topics as a checklist (audience, structure, how-to, troubleshooting section) — write the runbook in your repo, don’t chase the TW career track.
5. **Save proof** — configs, captures, failure notes, public GitHub update.

### Month-1 graft rule (binding)

From your curriculum:

- **KEEP:** Network Engineer spine  
- **GRAFT:** Linux networking, Bash for labs, Cyber *network-relevant* nodes  
- **DROP:** full Cyber CTF career, full DevOps/K8s, Technical Writer *as a career*, etc.

If a node conflicts with DROP, skip it and return to the spine + current lab.

---

## 4. Suggested study sequence

```text
Week rhythm (conceptually)
──────────────────────────
Linux (fundamentals)  ─┬─►  Shell/Bash (parallel)
                       │
                       ▼
              Network Engineer (spine)
                       │
                       ▼
         Cyber Security (network slice only)
                       │
                       ▼
     Technical Writer practices (every lab write-up)
```

Concrete order:

1. **Linux + Shell/Bash in parallel** — enough CLI to run labs confidently  
2. **Network Engineer** — primary depth (matches LAB-01…LAB-06)  
3. **Cyber Security** — only nodes that support edge/security labs (ACL, VPN, firewall types, segmentation, Zero Trust *as design*, IDS/IPS awareness)  
4. **Technical Writer** — continuous; use the outline as a *docs quality checklist*, not a link rabbit hole (only ~8 external URLs exist upstream)

---

## 5. How to search quickly

From the repo root:

```bash
# Find a topic across all outlines
rg -n "OSPF|VLAN|Zero Trust" roadmap-extracts --glob '**/outline.md'

# List only official Cisco / Cloudflare-style resources in Network Engineer
rg -n "\[official\]" roadmap-extracts/network-engineering-roadmap/network-engineer

# Dump section names from JSON
python3 -c "import json; d=json.load(open('roadmap-extracts/network-engineering-roadmap/network-engineer/data.json')); print('\n'.join(s['section'] for s in d['sections']))"
```

In the editor: open `outline.md`, use search for the node name, expand the `####` heading for resources.

---

## 6. Reading `outline.md` efficiently

1. Skim `## Topic outline + resources` headings (`###` = major section).  
2. Open only the `####` nodes you need for this week’s lab.  
3. Prefer `[official]` then one good `[video]` or `[article]` — don’t binge every link.  
4. Scroll to `## All unique resource URLs` only if you want a bulk list (same data as `links.md`).

Resource type tags appear as `[article]`, `[video]`, `[official]`, etc. before each markdown link.

---

## 7. Cyber Security — how to prune

The Cyber extract is large (~675 links). For Network Engineer hiring proof, prioritize:

- Networking Knowledge (OSI, ports, protocols, subnetting, VPN, VLAN, DMZ)
- Firewalls / ACL / secure vs unsecure protocols
- Zero Trust / segmentation concepts
- Auth basics (as they affect network access)
- Incident response *awareness* (not full DFIR career)

Defer or skip for Month 1: deep CTF platforms, full OSCP-style exploit paths, unrelated programming tracks, generic cloud SaaS browsing.

---

## 8. Technical Writer — how to use despite few links

Upstream content has almost no curated URLs. Treat `outline.md` as a **checklist**:

- Who is the audience? (NOC engineer, hiring manager, future you)
- Structure: goal → topology → steps → verify → failure notes  
- Include troubleshooting and references  
- Ship it publicly with the lab

That matches the 2h/day docs rhythm without switching careers.

---

## 9. Refreshing extracts later

Data came from roadmap.sh’s API + GitHub content at extraction time. To refresh:

1. Re-fetch `https://roadmap.sh/api/v1-official-roadmap/{slug}`  
2. Re-sync `roadmaps/{slug}/content/*.md` from [developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)  
3. Keep this folder structure (`network-engineering-roadmap/{slug}/` + `outline.md` / `links.md` / `data.json`)

Ask the agent: *“Refresh roadmap-extracts from roadmap.sh using the current folder layout.”*

---

## 10. Quick start (right now)

1. Open [network-engineering-roadmap/network-engineer/outline.md](network-engineering-roadmap/network-engineer/outline.md)  
2. Jump to the section that matches your current LAB  
3. Open 1–2 resources, lab the skill, write the runbook  
4. Pull Bash/Linux helpers only when the lab blocks on CLI  
5. Return to [README.md](README.md) when switching roadmaps
