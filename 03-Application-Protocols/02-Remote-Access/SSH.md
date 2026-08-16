---
tags: [application-protocols, networking, ccna, ssh]
aliases: [Secure Shell, ssh]
layer: Application
---

# SSH

## Learning objectives

- Explain SSH as encrypted remote shell / file / tunnel protocol over [[TCP]]/22
- Contrast password vs key authentication and known_hosts trust-on-first-use
- Use SSH for ops tasks and understand agent/forwarding risks at a high level
- Differentiate SSH from Telnet and from [[SSL-TLS]] VPNs

## One-sentence definition

> **SSH** (Secure Shell) provides authenticated, encrypted remote command execution, file transfer, and port forwarding over a TCP connection (default port **22**).

## Analogy

> SSH is a **secure walkie-talkie into the server room**: encrypted voice (shell), optional tunnels (port forwards), and a habit of checking the other party’s voiceprint (host key) so an impostor in the hallway can’t impersonate your jump box.

## Why it matters

SSH is how you manage routers, Linux boxes, jump hosts, and Git. Host key mismatches catch MITM — or scare you after legitimate reinstalls. Bastion patterns and ACLs around `:22` are core enterprise design.

## Deep dive

### Mental model

```text
ssh client ──TCP/22──► sshd
  1) version exchange
  2) key exchange → shared secrets
  3) server host key verify (known_hosts)
  4) user auth (keys/password/certs)
  5) channels: shell, exec, sftp, forwards
```

### Mechanism highlights

- **Host authentication:** server proves identity via host key; client caches fingerprint in `~/.ssh/known_hosts`.
- **User authentication:** public-key preferred (`~/.ssh/authorized_keys`); passwords discouraged.
- **Channels:** multiplexed logical streams inside one SSH connection.
- **SFTP:** file protocol *subsystem* of SSH — see [[FTP-SFTP]].

### On the wire

Encrypted application payload after handshake. You mainly see TCP/22. Banner exchange is clear briefly.

```bash
ssh -v user@host
nc -vz host 22
ssh-keygen -t ed25519
ssh-copy-id user@host
```

## Relationship to OSI / TCP-IP

| Model | Layer | Role here |
|-------|-------|-----------|
| TCP/IP | Application | Remote access / tunnels |
| Transport | TCP/22 | |

## Lab exercises

### Lab 1 — Verbose connect

```bash
ssh -v github.com
# Watch host key check and auth methods (don't need a shell success)
```

### Lab 2 — Local port forward mental model

```bash
# ssh -L 8080:internal:80 user@bastion
# Browser → localhost:8080 → over SSH → internal:80
```

## Troubleshooting playbook

| Symptom | Likely cause | What to check |
|---------|--------------|---------------|
| Connection refused | sshd down / wrong IP | listener, security group |
| Host key verification failed | Rebuild / MITM | verify fingerprint out-of-band |
| Permission denied | keys/mode/user | `~/.ssh` perms 700/600, authorized_keys |
| Timeout | ACL / routing | path to :22 |

## Common traps / interview gotchas

- Telnet = cleartext; never for secrets.
- Agent forwarding can expose keys on compromised jump hosts — prefer ProxyJump carefully.
- Changing SSH port ≠ security; still scan-detectable. Use keys + MFA + allowlists.
- Cisco/network devices speak SSH for management — same concepts, different key storage.

## Mastery checklist

- [ ] Explain known_hosts purpose
- [ ] Generate and install an ed25519 key pair
- [ ] Read `ssh -v` enough to spot auth failures
- [ ] Contrast SSH tunnels vs VPN at a high level

## Related notes

- [[TCP]] · [[Port]] · [[SSL-TLS]] · [[FTP-SFTP]] · [[Client]] · [[Server]]
- ← [[02-Remote-Access/Index|Remote Access]] · [[03-Application-Protocols/Index|Application Protocols]]
