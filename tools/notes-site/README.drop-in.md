# notes/ — drop-in web reader for alubaid.xyz

Static HTML export of the CCNA mastery vault. Designed to live at:

`https://www.alubaid.xyz/notes/...`

No homepage nav link required — share the URL directly (same idea as the existing `/wire` section).

## What’s inside

| Path | Purpose |
|------|---------|
| `index.html` | Notes home (from `Home.md`) |
| `00-…` / `01-…` / … | Curriculum HTML mirroring vault folders |
| `assets/notes.css` | alubaid design tokens + light/dark |
| `assets/notes.js` | Theme toggle (uses `localStorage.theme`), mobile nav, search |
| `manifest.json` | Machine-readable page list |
| `robots.txt` | `Disallow: /` (unlisted) |
| `INTEGRATION-PROMPT.md` | Paste into Cursor on the UBAID-Site repo |

## Rebuild after editing vault notes

```bash
# from Home-Labbing-CCNA repo root
tools/notes-site/.venv/bin/python tools/notes-site/build.py --base /notes
```

## Deploy onto alubaid.xyz

1. Copy this entire `notes/` folder into `UBAID-Site/public/notes/`
2. Follow `INTEGRATION-PROMPT.md`
3. Deploy — do **not** add a visible homepage link unless you want it public

Theme toggle shares `localStorage.theme` with the portfolio.
