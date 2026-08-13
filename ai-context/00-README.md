# AI Context Pack — Ubaid Ur Rahman (Alfred Alpino)

Feed these files into ChatGPT, Claude, or Cursor so every answer stays aligned with who I am, what I’m building, and what I refuse to waste time on.

**Scope of this folder:** AI context / guardrails only. Do not edit the resume PDF or portfolio site from this pack’s instructions alone — those are separate update tasks.

---

## Paste order (load in this sequence)

| Order | File | Why first |
|------:|------|-----------|
| 1 | `01-identity-and-profile.md` | Who I am — prevents invented bio |
| 2 | `02-goals-and-north-star.md` | What “good” looks like — 30/90-day targets |
| 3 | `03-roadmap-and-curriculum.md` | Canonical path — labs, grafts, drops |
| 4 | `04-ai-guardrails.md` | System rules for the AI |
| 5 | `05-do-dont-playbook.md` | Operational DO/DON’T tables |
| 6 | `06-prompt-templates.md` | Ready prompts (optional; paste when needed) |

`00-README.md` is for humans. Do not paste it into the model unless you want the AI to also know how the pack is structured.

---

## What each file does

| File | Audience | Role |
|------|----------|------|
| `00-README.md` | You | How to load and maintain this pack |
| `01-identity-and-profile.md` | AI (as my voice) | Identity, contacts, timeline, skills, certs, portfolio stance |
| `02-goals-and-north-star.md` | AI | Career north star, GCC targets, 30-/90-day outcomes |
| `03-roadmap-and-curriculum.md` | AI | Network Engineer spine, Month 1 weeks, LAB-01..06, keep/graft/drop |
| `04-ai-guardrails.md` | AI | Must / must-not, conflict resolution, tone, forbidden advice |
| `05-do-dont-playbook.md` | AI + me | Learning, labs, portfolio, resume, job search, AI use |
| `06-prompt-templates.md` | Me → AI | Copy-paste prompts that assume 01–05 are loaded |

---

## How to feed into each tool

### ChatGPT / Claude (chat UI)

1. Start a new project/space or custom GPT/project knowledge if available.
2. Upload or paste **01 → 05** in order (full text).
3. Pin or save as project instructions / custom instructions if the product supports it.
4. Use templates from `06` for recurring tasks (lab design, resume bullets, job apps).
5. When the AI drifts, re-paste `04` + the relevant section of `03` or `05`.

### Cursor

1. Keep this folder in the workspace: `ai-context/`.
2. Reference in chat: `@ai-context/01-identity-and-profile.md` … through `05` (or `@ai-context`).
3. For agent rules: point Cursor rules / AGENTS notes at `04-ai-guardrails.md` + `03-roadmap-and-curriculum.md`.
4. Prefer `@`-mentions of specific files over vague “remember my profile.”

### System / custom instructions (short slot)

If the tool only allows a short system prompt, paste a condensed pointer:

> Follow my AI context pack. Identity/goals/roadmap/guardrails live in project files `01`–`05`. Prefer labs + GitHub proof over more certs. Month-1 DROP list is binding. Never invent employers, metrics, or certifications. GCC Network Engineer / NOC / Network Analyst is the target.

Then attach or `@` the full files.

---

## Refresh cadence

| Cadence | Action |
|---------|--------|
| **Weekly (Sunday)** | Update `03` lab status (LAB-01..06). Sync `01` skills if a lab shipped. |
| **After any cert / job / portfolio change** | Update `01` immediately. Fix conflict notes if resume/site lag. |
| **Every 30 days** | Rewrite `02` 30-day outcomes; roll unfinished items into next window. |
| **Every 90 days** | Review north star + GCC targeting in `02`; prune `03` grafts if unused. |
| **When AI keeps wrong advice** | Strengthen `04` conflict rules; add a row to `05`. |
| **Never** | Invent experience to “fill gaps.” Prefer honest lab proof. |

---

## Hard truths this pack encodes

1. **Spine** = [roadmap.sh Network Engineer](https://roadmap.sh/network-engineer). Everything else is graft or drop.
2. **Month 1** = labs + docs + applications — not shiny adjacent careers.
3. **Proof > paper** — prefer public GitHub lab monorepo over stacking more certs.
4. **Portfolio** — update CCNA Candidate → certified language; ship labs; **do not redesign UI**.
5. **Education** — IGNOU BCA may be incomplete; lead with certs + labs in narratives.

---

## Completeness check

All of these must exist and be real content (not placeholders):

- [x] `00-README.md`
- [x] `01-identity-and-profile.md`
- [x] `02-goals-and-north-star.md`
- [x] `03-roadmap-and-curriculum.md`
- [x] `04-ai-guardrails.md`
- [x] `05-do-dont-playbook.md`
- [x] `06-prompt-templates.md`
