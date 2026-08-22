# ubaid-notes

Drop this **entire folder** into your `UBAID-Site` project root, then paste [`PROMPT.md`](PROMPT.md) into that project’s Cursor chat.

## Layout

| Path | Purpose |
|------|---------|
| `PROMPT.md` | **Paste this** into the UBAID-Site chat |
| `site/` | Static HTML to become `public/notes/` |
| `README.md` | This file |

## Quick deploy (manual)

```bash
cp -R ubaid-notes/site/.  /path/to/UBAID-Site/public/notes/
```

Then follow `PROMPT.md` (or paste it into Cursor on that repo).

## Rebuild from the vault (Home-Labbing-CCNA)

```bash
tools/notes-site/.venv/bin/python tools/notes-site/build.py --out ubaid-notes/site --base /notes
```

URLs look like: `https://www.alubaid.xyz/notes/00-Networks-and-Devices/01-Network-Types/LAN/`
