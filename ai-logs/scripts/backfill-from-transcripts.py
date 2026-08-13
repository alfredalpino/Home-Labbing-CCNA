#!/usr/bin/env python3
"""Backfill ai-logs/ from Cursor agent-transcripts JSONL files.

Idempotent: skips sessions that already have a .imported marker unless --force.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[2]
LOG_ROOT = WORKSPACE / "ai-logs"
SESSIONS = LOG_ROOT / "sessions"
A_TXT = LOG_ROOT / "a.txt"
INDEX = LOG_ROOT / "index.md"

DEFAULT_TRANSCRIPTS = Path.home() / ".cursor/projects/Users-ubaid-Home-Labbing-CCNA/agent-transcripts"

USER_QUERY_RE = re.compile(r"<user_query>\s*(.*?)\s*</user_query>", re.DOTALL | re.IGNORECASE)
TIMESTAMP_RE = re.compile(r"<timestamp>\s*(.*?)\s*</timestamp>", re.DOTALL | re.IGNORECASE)
TABLE_RE = re.compile(r"(?:^\|.+\|\s*$\n)+(?:^\|[-:| ]+\|\s*$\n)(?:^\|.+\|\s*$\n)+", re.MULTILINE)
WRITE_TOOLS = {"Write", "EditNotebook", "Delete"}
EDIT_TOOLS = {"StrReplace", "Write", "EditNotebook", "Delete"}


def extract_text_blocks(message: dict) -> list[str]:
    content = message.get("content") if isinstance(message, dict) else None
    if content is None:
        return []
    if isinstance(content, str):
        return [content]
    texts: list[str] = []
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                t = block.get("text")
                if isinstance(t, str) and t.strip():
                    texts.append(t)
    return texts


def extract_tool_uses(message: dict) -> list[dict]:
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, list):
        return []
    tools = []
    for block in content:
        if isinstance(block, dict) and block.get("type") == "tool_use":
            tools.append(block)
    return tools


def clean_user_text(raw: str) -> tuple[str, str | None]:
    ts_match = TIMESTAMP_RE.search(raw)
    ts = ts_match.group(1).strip() if ts_match else None
    q_match = USER_QUERY_RE.search(raw)
    if q_match:
        return q_match.group(1).strip(), ts
    # Fall back to raw without wrapper tags
    cleaned = TIMESTAMP_RE.sub("", raw)
    cleaned = USER_QUERY_RE.sub(r"\1", cleaned)
    return cleaned.strip(), ts


def extract_tables(text: str) -> list[str]:
    return [m.group(0).strip() for m in TABLE_RE.finditer(text)]


def file_paths_from_tools(tools: list[dict]) -> list[dict]:
    out = []
    for t in tools:
        name = t.get("name") or ""
        inp = t.get("input") or {}
        if not isinstance(inp, dict):
            continue
        path = inp.get("path") or inp.get("target_notebook")
        if path:
            out.append({"tool": name, "path": path, "action": "write" if name in WRITE_TOOLS else "edit" if name in EDIT_TOOLS else "other"})
    return out


def discover_jsonl(transcripts_root: Path) -> list[Path]:
    files = sorted(transcripts_root.rglob("*.jsonl"))
    return [p for p in files if p.is_file()]


def session_id_for(path: Path, transcripts_root: Path) -> str:
    rel = path.relative_to(transcripts_root)
    # e.g. uuid/uuid.jsonl or uuid/subagents/sid.jsonl
    parts = list(rel.parts)
    if "subagents" in parts:
        parent = parts[0]
        child = path.stem
        return f"{parent}__subagent__{child}"
    return path.stem


def parse_session(path: Path) -> dict:
    turns = []
    all_ai_words: list[str] = []
    all_tables: list[str] = []
    files_touched: list[dict] = []
    first_ts = None
    last_role = None

    with path.open(encoding="utf-8") as fh:
        for line_no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            role = obj.get("role")
            message = obj.get("message") or {}
            texts = extract_text_blocks(message)
            tools = extract_tool_uses(message)

            if role == "user":
                joined = "\n\n".join(texts)
                body, ts = clean_user_text(joined)
                if ts and not first_ts:
                    first_ts = ts
                turns.append({"role": "user", "text": body, "timestamp": ts, "line": line_no})
            elif role == "assistant":
                joined = "\n\n".join(texts)
                if joined.strip():
                    all_ai_words.append(joined)
                    all_tables.extend(extract_tables(joined))
                    turns.append({"role": "assistant", "text": joined, "line": line_no})
                files_touched.extend(file_paths_from_tools(tools))
            last_role = role

    # Deduplicate file paths preserving order
    seen = set()
    unique_files = []
    for f in files_touched:
        key = (f["tool"], f["path"])
        if key in seen:
            continue
        seen.add(key)
        unique_files.append(f)

    # Deduplicate tables
    seen_t = set()
    unique_tables = []
    for t in all_tables:
        if t in seen_t:
            continue
        seen_t.add(t)
        unique_tables.append(t)

    title = "Untitled"
    for t in turns:
        if t["role"] == "user" and t["text"].strip():
            first_line = t["text"].strip().splitlines()[0]
            title = first_line[:120]
            break

    try:
        mtime = path.stat().st_mtime
    except OSError:
        mtime = 0.0

    return {
        "source": str(path),
        "first_timestamp": first_ts,
        "mtime": mtime,
        "title": title,
        "turns": turns,
        "ai_words": "\n\n---\n\n".join(all_ai_words),
        "tables": unique_tables,
        "files": unique_files,
        "user_turns": sum(1 for t in turns if t["role"] == "user"),
        "assistant_turns": sum(1 for t in turns if t["role"] == "assistant"),
        "last_role": last_role,
    }


def write_session(session_id: str, data: dict, force: bool) -> bool:
    dest = SESSIONS / session_id
    marker = dest / ".imported"
    if marker.exists() and not force:
        return False

    dest.mkdir(parents=True, exist_ok=True)

    meta = {
        "session_id": session_id,
        "source": data["source"],
        "title": data["title"],
        "first_timestamp": data["first_timestamp"],
        "mtime": data.get("mtime", 0),
        "user_turns": data["user_turns"],
        "assistant_turns": data["assistant_turns"],
        "table_count": len(data["tables"]),
        "files_touched_count": len(data["files"]),
        "imported_at": datetime.now(timezone.utc).isoformat(),
    }
    (dest / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    qa_lines = [f"# Session {session_id}", "", f"**Title:** {data['title']}", ""]
    if data["first_timestamp"]:
        qa_lines.append(f"**Started:** {data['first_timestamp']}")
        qa_lines.append("")
    for i, turn in enumerate(data["turns"], 1):
        label = "USER" if turn["role"] == "user" else "ASSISTANT"
        qa_lines.append(f"## Turn {i} — {label}")
        if turn.get("timestamp"):
            qa_lines.append(f"_Timestamp: {turn['timestamp']}_")
            qa_lines.append("")
        qa_lines.append(turn["text"])
        qa_lines.append("")
    (dest / "qa.md").write_text("\n".join(qa_lines).rstrip() + "\n", encoding="utf-8")

    (dest / "words.txt").write_text(data["ai_words"] + ("\n" if data["ai_words"] else ""), encoding="utf-8")

    if data["tables"]:
        table_parts = [f"# Tables from session {session_id}", ""]
        for i, table in enumerate(data["tables"], 1):
            table_parts.append(f"## Table {i}")
            table_parts.append("")
            table_parts.append(table)
            table_parts.append("")
        (dest / "tables.md").write_text("\n".join(table_parts), encoding="utf-8")
    else:
        (dest / "tables.md").write_text(f"# Tables from session {session_id}\n\n_No markdown tables found._\n", encoding="utf-8")

    if data["files"]:
        file_lines = [f"# Files touched by AI — session {session_id}", ""]
        for f in data["files"]:
            file_lines.append(f"- `{f['tool']}` → `{f['path']}`")
        (dest / "files-touched.md").write_text("\n".join(file_lines) + "\n", encoding="utf-8")
    else:
        (dest / "files-touched.md").write_text(
            f"# Files touched by AI — session {session_id}\n\n_No Write/StrReplace/EditNotebook/Delete tool calls recorded._\n",
            encoding="utf-8",
        )

    (dest / "source-path.txt").write_text(data["source"] + "\n", encoding="utf-8")
    marker.write_text(meta["imported_at"] + "\n", encoding="utf-8")
    return True


def rebuild_a_txt(all_sessions: list[tuple[str, dict]]) -> None:
    """Rewrite master a.txt from all session data (deterministic order)."""
    lines = [
        "=" * 80,
        "AI CONVERSATION MASTER LOG — Home-Labbing-CCNA",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "Append-only policy for live turns; full rebuild allowed via backfill script.",
        "=" * 80,
        "",
    ]
    for session_id, data in all_sessions:
        lines.append("=" * 80)
        lines.append(f"SESSION: {session_id}")
        lines.append(f"TITLE: {data['title']}")
        if data["first_timestamp"]:
            lines.append(f"STARTED: {data['first_timestamp']}")
        lines.append(f"SOURCE: {data['source']}")
        lines.append("=" * 80)
        lines.append("")
        for i, turn in enumerate(data["turns"], 1):
            label = "QUESTION (USER)" if turn["role"] == "user" else "ANSWER (AI)"
            lines.append(f"----- {label} | turn {i} -----")
            if turn.get("timestamp"):
                lines.append(f"[{turn['timestamp']}]")
            lines.append(turn["text"])
            lines.append("")
        lines.append("")
    A_TXT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def rebuild_index(metas: list[dict]) -> None:
    lines = [
        "# AI Logs — Session Index",
        "",
        f"_Last updated: {datetime.now(timezone.utc).isoformat()}_",
        "",
        "| Session | Title | User turns | AI turns | Tables | Files |",
        "|---------|-------|------------|----------|--------|-------|",
    ]
    for m in metas:
        title = (m.get("title") or "").replace("|", "\\|")[:80]
        lines.append(
            f"| [`{m['session_id']}`](sessions/{m['session_id']}/) | {title} | "
            f"{m.get('user_turns', 0)} | {m.get('assistant_turns', 0)} | "
            f"{m.get('table_count', 0)} | {m.get('files_touched_count', 0)} |"
        )
    lines.append("")
    lines.append("Master Q&A log: [`a.txt`](a.txt)")
    lines.append("")
    INDEX.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Backfill ai-logs from Cursor transcripts")
    parser.add_argument("--transcripts", type=Path, default=DEFAULT_TRANSCRIPTS)
    parser.add_argument("--force", action="store_true", help="Re-import even if already imported")
    args = parser.parse_args()

    if not args.transcripts.exists():
        print(f"Transcripts root not found: {args.transcripts}", file=sys.stderr)
        return 1

    SESSIONS.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)

    jsonl_files = discover_jsonl(args.transcripts)
    imported = 0
    skipped = 0
    all_data: list[tuple[str, dict]] = []
    metas: list[dict] = []

    for path in jsonl_files:
        sid = session_id_for(path, args.transcripts)
        data = parse_session(path)
        all_data.append((sid, data))
        wrote = write_session(sid, data, force=args.force)
        if wrote:
            imported += 1
            print(f"imported {sid}")
        else:
            skipped += 1
            print(f"skipped  {sid} (already imported)")
        meta_path = SESSIONS / sid / "meta.json"
        if meta_path.exists():
            metas.append(json.loads(meta_path.read_text(encoding="utf-8")))

    # Sort by file mtime (human timestamps in transcripts are not reliably sortable)
    all_data.sort(key=lambda x: (x[1].get("mtime") or 0, x[0]))
    rebuild_a_txt(all_data)
    metas.sort(key=lambda m: (m.get("mtime") or 0, m.get("session_id") or ""))
    rebuild_index(metas)

    print(f"Done. imported={imported} skipped={skipped} total={len(jsonl_files)}")
    print(f"Master log: {A_TXT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
