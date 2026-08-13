# Roadmap extracts — index

Offline extracts of five [roadmap.sh](https://roadmap.sh) learning paths for this CCNA / Network Engineer home-lab repo.

**Spine:** [Network Engineer](network-engineering-roadmap/network-engineer/outline.md)  
**Start here for usage:** [HOW-TO-USE.md](HOW-TO-USE.md)

---

## Folder layout

```text
roadmap-extracts/
├── README.md                      ← you are here (index)
├── HOW-TO-USE.md                  ← how to study / navigate these files
└── network-engineering-roadmap/   ← all five roadmaps in one place
    ├── network-engineer/
    ├── linux/
    ├── cyber-security/
    ├── shell-bash/
    └── technical-writer/
```

Each roadmap folder contains the same three files:

| File | Purpose |
|------|---------|
| `outline.md` | Full topic tree + descriptions + resource links under each node |
| `links.md` | Flat list of every unique resource URL (quick scan / bookmarking) |
| `data.json` | Machine-readable dump (stats, sections, resources) for scripts |

**Collection README:** [network-engineering-roadmap/README.md](network-engineering-roadmap/README.md)

---

## Network engineering roadmap

| Roadmap | Official page | Outline | Links only | JSON |
|---------|---------------|---------|------------|------|
| Network Engineer | [roadmap.sh/network-engineer](https://roadmap.sh/network-engineer) | [outline.md](network-engineering-roadmap/network-engineer/outline.md) | [links.md](network-engineering-roadmap/network-engineer/links.md) | [data.json](network-engineering-roadmap/network-engineer/data.json) |
| Linux | [roadmap.sh/linux](https://roadmap.sh/linux) | [outline.md](network-engineering-roadmap/linux/outline.md) | [links.md](network-engineering-roadmap/linux/links.md) | [data.json](network-engineering-roadmap/linux/data.json) |
| Cyber Security | [roadmap.sh/cyber-security](https://roadmap.sh/cyber-security) | [outline.md](network-engineering-roadmap/cyber-security/outline.md) | [links.md](network-engineering-roadmap/cyber-security/links.md) | [data.json](network-engineering-roadmap/cyber-security/data.json) |
| Shell / Bash | [roadmap.sh/shell-bash](https://roadmap.sh/shell-bash) | [outline.md](network-engineering-roadmap/shell-bash/outline.md) | [links.md](network-engineering-roadmap/shell-bash/links.md) | [data.json](network-engineering-roadmap/shell-bash/data.json) |
| Technical Writer | [roadmap.sh/technical-writer](https://roadmap.sh/technical-writer) | [outline.md](network-engineering-roadmap/technical-writer/outline.md) | [links.md](network-engineering-roadmap/technical-writer/links.md) | [data.json](network-engineering-roadmap/technical-writer/data.json) |

---

## Stats snapshot

| Roadmap | Topics | Subtopics | Content pages | Resource links | Unique URLs |
|---------|-------:|----------:|--------------:|---------------:|------------:|
| [Network Engineer](network-engineering-roadmap/network-engineer/outline.md) | 29 | 166 | 196 | 450 | 431 |
| [Linux](network-engineering-roadmap/linux/outline.md) | 16 | 86 | 102 | 290 | 253 |
| [Cyber Security](network-engineering-roadmap/cyber-security/outline.md) | 6 | 295 | 301 | 675 | 627 |
| [Shell / Bash](network-engineering-roadmap/shell-bash/outline.md) | 30 | 144 | 174 | 453 | 407 |
| [Technical Writer](network-engineering-roadmap/technical-writer/outline.md) | 21 | 63 | 84 | 8 | 8 |

---

## How these five connect

`relatedRoadmaps` on roadmap.sh (among *your* five, then others):

- **Network Engineer** → linux, shell-bash, cyber-security · also devops-beginner, terraform, mlops, system-design
- **Linux** → cyber-security · also devops, backend, docker
- **Cyber Security** → linux · also computer-science, docker, python, cpp
- **Shell / Bash** → _(none of the five)_ · also backend, full-stack, devops, system-design, nodejs
- **Technical Writer** → _(none of the five)_ · also devrel, engineering-manager, git-github

Shared skill clusters:

1. **Networking core** — OSI/TCP-IP, subnetting, routing/switching, DNS/DHCP, VPN, firewalls
2. **Ops tooling** — Linux CLI, processes/services, `tcpdump`/`wireshark`, `ping`/`traceroute`/`nmap`, Bash automation
3. **Security overlay** — Zero Trust, IDS/IPS, encryption, hardening, IR (graft network-relevant slices)
4. **Docs craft** — runbooks / how-tos via Technical Writer practices

---

## Suggested study order

1. Linux fundamentals + Shell/Bash in parallel  
2. Network Engineer (spine)  
3. Cyber Security — network-relevant nodes only  
4. Technical Writer practices continuously (lab docs / runbooks)

Detail and workflows: [HOW-TO-USE.md](HOW-TO-USE.md)

---

## Sources

- Graph JSON: `https://roadmap.sh/api/v1-official-roadmap/{slug}`
- Topic content: [kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap) → `roadmaps/{slug}/content/`
- Local curriculum context: [`../ai-context/03-roadmap-and-curriculum.md`](../ai-context/03-roadmap-and-curriculum.md), [`../Network-Engineer-Roadmap.md`](../Network-Engineer-Roadmap.md)
