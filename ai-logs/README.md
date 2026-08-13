# AI Logs — Home-Labbing-CCNA

Permanent archive of every Cursor AI question and answer in this workspace.

## Layout

| Path | Purpose |
|------|---------|
| `a.txt` | Master chronological Q&A log (all sessions) |
| `index.md` | Session catalog |
| `sessions/<id>/qa.md` | Per-chat Q&A |
| `sessions/<id>/words.txt` | Every word the AI wrote |
| `sessions/<id>/tables.md` | Every markdown table |
| `sessions/<id>/files-touched.md` | Files the AI wrote/edited |
| `sessions/<id>/meta.json` | Counts and metadata |
| `scripts/backfill-from-transcripts.py` | Import past Cursor chats |
| `scripts/append-turn.py` | Append one live turn |

## Catch up past chats

```bash
python3 ai-logs/scripts/backfill-from-transcripts.py
# Re-import everything:
python3 ai-logs/scripts/backfill-from-transcripts.py --force
```

Source: `~/.cursor/projects/Users-ubaid-Home-Labbing-CCNA/agent-transcripts/`

## Forever logging

Enforced by Cursor rule: `.cursor/rules/ai-conversation-logging.mdc` (`alwaysApply: true`).

Every agent turn must call `append-turn.py` (or equivalent) before finishing.
