---
tags: [moc, application-protocols, remote-access]
aliases: [Remote Access]
---

# Remote Access

Secure remote access is how operators reach routers, switches, Linux boxes, and lab VMs without sitting in front of them.

## Why it matters

- Production gear is rarely local — SSH is the default ops door
- Bad remote-access hygiene (Telnet, shared passwords, open WAN SSH) shows up in every audit
- Same channel often carries file transfer ([[FTP-SFTP|SFTP]]) and tunnels

## Notes in this section

| Note | Role |
|------|------|
| [[SSH]] | Encrypted remote shell, port forwarding, and SFTP transport |

## Study checklist

- [ ] Explain SSH vs Telnet in one sentence (confidentiality + integrity)
- [ ] Know default port 22 and why changing it is not “security”
- [ ] Practice key-based auth in a lab before touching production

← [[03-Application-Protocols/Index|Application Protocols]]
