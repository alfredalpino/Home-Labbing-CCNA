---
tags: [moc, application-protocols, email]
aliases: [Email]
---

# Email

How mail leaves a client, traverses MTAs, and lands in a mailbox — useful for ports, TLS, and “why is SMTP blocked outbound?” tickets.

## Notes in this section

| Note | Role |
|------|------|
| [[SMTP-IMAP]] | Sending (SMTP) vs retrieving (IMAP) mail |

## Ports to remember

| Service | Common port | Notes |
|---------|-------------|-------|
| SMTP submission | 587 | Preferred for clients + STARTTLS |
| SMTPS | 465 | Implicit TLS |
| IMAPS | 993 | Encrypted retrieval |

← [[03-Application-Protocols/Index|Application Protocols]]
