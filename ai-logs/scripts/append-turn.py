#!/usr/bin/env python3
"""Append one Q&A turn to ai-logs/a.txt and the current session folder.

Usage:
  python3 ai-logs/scripts/append-turn.py \\
    --session <uuid-or-slug> \\
    --question "user text" \\
    --answer "assistant text" \\
    [--title "optional session title"]

Or pipe JSON on stdin:
  {"session":"...","question":"...","answer":"...","title":"..."}
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
LOG_ROOT = WORKSPACE / "ai-logs"
SESSIONS = LOG_ROOT / "sessions"
A_TXT = LOG_ROOT / "a.txt"

TABLE_RE = re.compile(r"(?:^\|.+\|\s*$\n)+(?:^\|[-:| ]+\|\s*$\n)(?:^\|.+\|\s*$\n)+", re.MULTILINE)


def ensure_session(session_id: str, title: str | None) -> Path:
    dest = SESSIONS / session_id
    dest.mkdir(parents=True, exist_ok=True)
    meta_path = dest / "meta.json"
    if not meta_path.exists():
        meta = {
            "session_id": session_id,
            "source": "live-append",
            "title": title or "Live session",
            "first_timestamp": datetime.now(timezone.utc).isoformat(),
            "user_turns": 0,
            "assistant_turns": 0,
            "table_count": 0,
            "files_touched_count": 0,
            "imported_at": datetime.now(timezone.utc).isoformat(),
        }
        meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        for name, content in {
            "qa.md": f"# Session {session_id}\n\n**Title:** {meta['title']}\n\n",
            "words.txt": "",
            "tables.md": f"# Tables from session {session_id}\n\n",
            "files-touched.md": f"# Files touched by AI — session {session_id}\n\n",
        }.items():
            p = dest / name
            if not p.exists():
                p.write_text(content, encoding="utf-8")
    elif title:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
        if meta.get("title") in (None, "", "Live session", "Untitled"):
            meta["title"] = title
            meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return dest


def bump_meta(dest: Path, *, user: bool, assistant: bool, tables: int, files: list[str]) -> None:
    meta_path = dest / "meta.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if user:
        meta["user_turns"] = int(meta.get("user_turns") or 0) + 1
    if assistant:
        meta["assistant_turns"] = int(meta.get("assistant_turns") or 0) + 1
    meta["table_count"] = int(meta.get("table_count") or 0) + tables
    if files:
        meta["files_touched_count"] = int(meta.get("files_touched_count") or 0) + len(files)
        ft = dest / "files-touched.md"
        with ft.open("a", encoding="utf-8") as fh:
            for path in files:
                fh.write(f"- `live` → `{path}`\n")
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")


def append_a_txt(session_id: str, question: str, answer: str, title: str | None) -> None:
    A_TXT.parent.mkdir(parents=True, exist_ok=True)
    if not A_TXT.exists():
        A_TXT.write_text(
            "=" * 80
            + "\nAI CONVERSATION MASTER LOG — Home-Labbing-CCNA\n"
            + f"Created: {datetime.now(timezone.utc).isoformat()}\n"
            + "=" * 80
            + "\n\n",
            encoding="utf-8",
        )
    now = datetime.now(timezone.utc).isoformat()
    block = [
        "",
        "=" * 80,
        f"SESSION: {session_id}",
        f"TITLE: {title or 'Live session'}",
        f"LOGGED_AT: {now}",
        "SOURCE: live-append",
        "=" * 80,
        "",
        "----- QUESTION (USER) -----",
        question.strip(),
        "",
        "----- ANSWER (AI) -----",
        answer.strip(),
        "",
    ]
    with A_TXT.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(block))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--session", required=False)
    parser.add_argument("--question", required=False)
    parser.add_argument("--answer", required=False)
    parser.add_argument("--title", required=False)
    parser.add_argument("--files", nargs="*", default=[], help="Workspace-relative or absolute file paths touched")
    parser.add_argument("--stdin-json", action="store_true")
    args = parser.parse_args()

    if args.stdin_json or (not args.session and not sys.stdin.isatty()):
        payload = json.load(sys.stdin)
        session_id = payload["session"]
        question = payload["question"]
        answer = payload["answer"]
        title = payload.get("title")
        files = payload.get("files") or []
    else:
        if not args.session or args.question is None or args.answer is None:
            parser.error("--session, --question, and --answer are required (or pass JSON on stdin)")
        session_id = args.session
        question = args.question
        answer = args.answer
        title = args.title
        files = args.files

    dest = ensure_session(session_id, title)
    now = datetime.now(timezone.utc).isoformat()

    with (dest / "qa.md").open("a", encoding="utf-8") as fh:
        fh.write(f"## Turn — USER\n_Timestamp: {now}_\n\n{question.strip()}\n\n")
        fh.write(f"## Turn — ASSISTANT\n_Timestamp: {now}_\n\n{answer.strip()}\n\n")

    with (dest / "words.txt").open("a", encoding="utf-8") as fh:
        fh.write(answer.strip() + "\n\n---\n\n")

    tables = list(TABLE_RE.finditer(answer))
    if tables:
        with (dest / "tables.md").open("a", encoding="utf-8") as fh:
            for i, m in enumerate(tables, 1):
                fh.write(f"## Live table {now} #{i}\n\n{m.group(0).strip()}\n\n")

    bump_meta(dest, user=True, assistant=True, tables=len(tables), files=list(files))
    append_a_txt(session_id, question, answer, title)
    print(f"Logged turn for session {session_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
