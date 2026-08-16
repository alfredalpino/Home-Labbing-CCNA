---
tags: [application-protocols, networking, ccna, ftp, sftp]
aliases: [FTP, SFTP, File Transfer Protocol, FTPS]
layer: Application
---

# FTP / SFTP

## Learning objectives

- Explain classic FTP control vs data channels and active vs passive mode
- Contrast FTP, FTPS, and SFTP clearly (SFTP ≠ FTP over SSH branding alone — it is an SSH subsystem)
- Know firewall implications that make FTP painful
- Prefer secure file transfer patterns in modern designs

## One-sentence definition

> **FTP** transfers files using a control connection plus separate data connections (historically cleartext); **SFTP** is a secure file-transfer protocol that runs as a subsystem of [[SSH]], encrypting the session end-to-end.

## Analogy

> Classic FTP is a **warehouse with two doors**: one for talking to the clerk (control) and one for forklifts (data) — awkward with security guards (firewalls). SFTP is **one secure loading bay under SSH**: talk and cargo share the same guarded tunnel.

## Why it matters

Legacy integrations still demand FTP. Passive/active mode breaks through NAT/firewalls constantly. Using the wrong mental model (“just open 21”) fails. SFTP is what you should deploy for human/ops file movement when possible.

## Deep dive

### FTP mental model

```text
Control channel: client → server TCP/21  (commands)
Data channel:    PORT/EPRT (active) or PASV/EPSV (passive) negotiates second TCP connection
```

| Mode | Who initiates data TCP? | NAT/firewall friendliness |
|------|-------------------------|---------------------------|
| Active | Server → client ephemeral | Often broken (client-side firewall) |
| Passive | Client → server data port | Preferred through firewalls; server must allow port range |

**FTPS:** FTP + [[SSL-TLS]] (explicit AUTH TLS or implicit). Still has dual-channel complexity.

### SFTP mental model

```text
Single SSH connection (TCP/22) → subsystem sftp → encrypted file ops
No separate FTP data ports.
```

Do **not** confuse with “Simple FTP.” SFTP = SSH File Transfer Protocol.

### On the wire

```bash
# Prefer SFTP
sftp user@host
scp file user@host:
ssh user@host 'ls'

# FTP (lab only)
ftp host
curl -v --ftp-pasv ftp://ftp.example.com/
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | File transfer |
| Transport | TCP | 21 + data ports (FTP); 22 (SFTP) |

## Lab exercises

### Lab 1 — SFTP basics

```bash
sftp localhost
# or any lab SSH host
```

### Lab 2 — Think through PASV ports

Document why a firewall rule “allow TCP/21” is insufficient for FTP data transfers.

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Login OK, LIST hangs | Data channel blocked | active vs passive, port range |
| Works on-net, fails remote | NAT ALG / no ALG | force PASV, modern gateways |
| Auth fails SFTP | SSH keys/perms | same as [[SSH]] |
| Confused vendor “SFTP” | They meant FTPS | ask port 22 vs 21/990 |

## Common traps / interview gotchas

- FTP credentials historically cleartext — assume compromised on shared networks.
- Active FTP + stateful firewall = classic interview question.
- SCP/SFTP/rsync-over-SSH are modern replacements for many FTP jobs.
- HTTP(S) file download is often simpler for distribution.

## Mastery checklist

- [ ] Draw active vs passive FTP
- [ ] Explain why SFTP is easier through firewalls
- [ ] Name ports involved for FTP vs SFTP
- [ ] Reject cleartext FTP for sensitive data

## Related notes

- [[SSH]] · [[TCP]] · [[SSL-TLS]] · [[Port]] · [[Port]]
- ← [[04-File-Transfer/Index|File Transfer]] · [[03-Application-Protocols/Index|Application Protocols]]
