#!/usr/bin/env python3
"""Build a drop-in static notes site for alubaid.xyz/notes/.

Usage:
  tools/notes-site/.venv/bin/python tools/notes-site/build.py
  tools/notes-site/.venv/bin/python tools/notes-site/build.py --base /notes
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

import markdown
from markdown.extensions.tables import TableExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.toc import TocExtension

WORKSPACE = Path(__file__).resolve().parents[2]
ASSETS_SRC = Path(__file__).resolve().parent / "assets"
DEFAULT_OUT = WORKSPACE / "ubaid-notes" / "site"
PACKAGE_ROOT = WORKSPACE / "ubaid-notes"

INCLUDE_ROOTS = [
    "Home.md",
    "Obsidian-Setup.md",
    "00-Networks-and-Devices",
    "01-Basic-Terminology",
    "02-Core-Protocols",
    "03-Application-Protocols",
    "04-Building-a-Network",
    "04-Network-Security",
    "90-Reference",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKI_RE = re.compile(r"\[\[([^\]]+)\]\]")
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


@dataclass
class Note:
    src: Path
    rel_md: str
    title: str
    body_md: str
    tags: list[str] = field(default_factory=list)
    aliases: list[str] = field(default_factory=list)
    url_path: str = ""
    out_file: Path | None = None


def parse_frontmatter(text: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            meta[key] = [x.strip().strip("'\"") for x in inner.split(",") if x.strip()]
        else:
            meta[key] = val.strip("'\"")
    return meta, text[m.end() :]


def collect_sources() -> list[Path]:
    files: list[Path] = []
    for name in INCLUDE_ROOTS:
        path = WORKSPACE / name
        if path.is_file() and path.suffix == ".md":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
    return files


def md_to_url_parts(rel: Path) -> list[str]:
    parts = list(rel.parts)
    if parts[-1].lower() == "index.md":
        parts = parts[:-1]
    else:
        parts[-1] = Path(parts[-1]).stem
    if parts and parts[0] == "Home":
        return []
    return parts


def build_notes(out_dir: Path, base: str) -> list[Note]:
    notes: list[Note] = []
    for src in collect_sources():
        rel = src.relative_to(WORKSPACE)
        text = src.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        title_m = TITLE_RE.search(body)
        title = title_m.group(1).strip() if title_m else src.stem.replace("-", " ")
        tags = meta.get("tags") if isinstance(meta.get("tags"), list) else []
        aliases = meta.get("aliases") if isinstance(meta.get("aliases"), list) else []
        if isinstance(meta.get("aliases"), str):
            aliases = [meta["aliases"]]

        parts = md_to_url_parts(rel)
        url_path = "/" + "/".join(parts) + ("/" if parts else "")
        if base != "/":
            url_path = base.rstrip("/") + (url_path if parts else "/")
        else:
            url_path = url_path if parts else "/"

        if parts:
            out_file = out_dir.joinpath(*parts) / "index.html"
        else:
            out_file = out_dir / "index.html"

        notes.append(
            Note(
                src=src,
                rel_md=str(rel).replace("\\", "/"),
                title=title,
                body_md=body,
                tags=tags,
                aliases=aliases,
                url_path=url_path,
                out_file=out_file,
            )
        )
    return notes


def link_index(notes: list[Note]) -> dict[str, Note]:
    idx: dict[str, Note] = {}
    for n in notes:
        keys = {
            n.title,
            n.src.stem,
            Path(n.rel_md).stem,
            n.rel_md.replace(".md", ""),
            n.rel_md,
        }
        for a in n.aliases:
            keys.add(a)
        # path-style keys without extension
        keys.add(n.rel_md[:-3] if n.rel_md.endswith(".md") else n.rel_md)
        for k in keys:
            if not k:
                continue
            idx[k] = n
            idx[k.lower()] = n
    return idx


def resolve_wiki(target: str, idx: dict[str, Note], current: Note, base: str) -> str | None:
    raw = target.strip().replace("\\|", "|")
    display = None
    if "|" in raw:
        raw, display = [x.strip() for x in raw.split("|", 1)]
    # strip .md
    if raw.endswith(".md"):
        raw = raw[:-3]
    candidates = [
        raw,
        raw.replace("\\", "/"),
        Path(raw).name,
        raw.replace(" ", "-"),
        raw.replace(" ", "/"),
        raw.replace("/", "-"),
    ]
    # relative to current note directory
    cur_dir = current.src.parent
    maybe = (cur_dir / raw).resolve()
    try:
        rel = maybe.relative_to(WORKSPACE)
        candidates.append(str(rel).replace("\\", "/"))
        candidates.append(str(rel.with_suffix("")).replace("\\", "/"))
    except Exception:
        pass
    # also try Index under a folder name
    for c in list(candidates):
        candidates.append(f"{c}/Index")
        candidates.append(f"{c}/index")

    for c in candidates:
        hit = idx.get(c) or idx.get(c.lower())
        if hit:
            label = display or hit.title
            return f'<a href="{html.escape(hit.url_path)}">{html.escape(label)}</a>'
    label = display or raw
    return f'<span class="wiki-missing" title="Unresolved link">{html.escape(label)}</span>'


def convert_wikilinks(md_text: str, idx: dict[str, Note], current: Note, base: str) -> str:
    def repl(m: re.Match[str]) -> str:
        return resolve_wiki(m.group(1), idx, current, base) or m.group(0)

    # Replace wiki links with HTML anchors before markdown pass by using placeholders
    # that survive markdown: use raw HTML
    return WIKI_RE.sub(repl, md_text)


def md_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            FencedCodeExtension(),
            TableExtension(),
            TocExtension(permalink=False),
            "sane_lists",
            "smarty",
        ],
    )


def module_tree(notes: list[Note]) -> list[dict]:
    """Build sidebar sections from top-level curriculum folders."""
    modules = [
        ("00-Networks-and-Devices", "0 · Networks & Devices"),
        ("01-Basic-Terminology", "1 · Basic Terminology"),
        ("02-Core-Protocols", "2 · Core Protocols"),
        ("03-Application-Protocols", "3 · Application Protocols"),
        ("04-Building-a-Network", "4 · Building a Network"),
        ("04-Network-Security", "4b · Network Security"),
        ("90-Reference", "Reference"),
    ]
    sections = []
    for prefix, label in modules:
        items = [
            n
            for n in notes
            if n.rel_md.startswith(prefix + "/") or n.rel_md == prefix + ".md"
        ]
        # Prefer Index pages first, then alphabetical
        items.sort(
            key=lambda n: (
                0 if n.src.name.lower() == "index.md" else 1,
                n.rel_md.lower(),
            )
        )
        if items:
            sections.append({"id": prefix, "label": label, "items": items})
    return sections


def render_sidebar(notes: list[Note], current: Note, base: str) -> str:
    sections = module_tree(notes)
    chunks = [
        '<label class="sidebar-label" for="note-search">Search</label>',
        '<input class="search" id="note-search" type="search" placeholder="Filter notes…" autocomplete="off" />',
        f'<p class="sidebar-label"><a class="nav-module" href="{html.escape(base if base.endswith("/") else base + "/")}">Home</a></p>',
    ]
    for sec in sections:
        open_attr = " open" if current.rel_md.startswith(sec["id"]) else ""
        chunks.append(f'<details class="nav-section"{open_attr}>')
        chunks.append(f'<summary>{html.escape(sec["label"])}</summary>')
        chunks.append('<ul class="nav-list">')
        for n in sec["items"]:
            active = " active" if n.url_path == current.url_path else ""
            label = n.title
            if n.src.name.lower() == "index.md":
                label = f"Index · {n.title}" if n.title.lower() != "index" else "Index"
            chunks.append(
                f'<li data-nav-item="{html.escape(n.title + " " + n.rel_md)}">'
                f'<a class="{active.strip()}" href="{html.escape(n.url_path)}">{html.escape(label)}</a></li>'
            )
        chunks.append("</ul></details>")
    return "\n".join(chunks)


def asset_href(base: str, name: str) -> str:
    root = base.rstrip("/") if base != "/" else ""
    return f"{root}/assets/{name}"


def page_shell(
    *,
    note: Note,
    body_html: str,
    sidebar: str,
    base: str,
    prev_n: Note | None,
    next_n: Note | None,
    is_home: bool,
) -> str:
    site_home = "https://www.alubaid.xyz/"
    notes_home = base if base.endswith("/") else base + "/"
    tags = " · ".join(f"#{t}" for t in note.tags[:6])
    meta_bits = [note.rel_md]
    if tags:
        meta_bits.append(tags)

    pager = ['<nav class="pager">']
    if prev_n:
        pager.append(f'<a href="{html.escape(prev_n.url_path)}">← {html.escape(prev_n.title)}</a>')
    else:
        pager.append("<span></span>")
    if next_n:
        pager.append(f'<a href="{html.escape(next_n.url_path)}">{html.escape(next_n.title)} →</a>')
    else:
        pager.append("<span></span>")
    pager.append("</nav>")

    title = note.title if not is_home else "Network Notes · Ubaid Ur Rahman"
    desc = (
        "CCNA / network engineering study notes — unlisted on alubaid.xyz."
        if is_home
        else f"{note.title} — network study note by Ubaid Ur Rahman."
    )

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="robots" content="noindex, nofollow" />
  <meta name="theme-color" content="#0b0f0e" media="(prefers-color-scheme: dark)" />
  <meta name="theme-color" content="#f4f7f6" media="(prefers-color-scheme: light)" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{html.escape(asset_href(base, 'notes.css'))}" />
  <script>
    (function(){{
      try {{
        var t = localStorage.getItem('theme');
        if (t !== 'light' && t !== 'dark') {{
          t = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        }}
        document.documentElement.setAttribute('data-theme', t);
      }} catch (e) {{}}
    }})();
  </script>
</head>
<body>
  <header class="topbar">
    <div class="top-left">
      <button type="button" class="menu-btn" id="menu-toggle" aria-label="Open curriculum">Menu</button>
      <a class="crumb" href="{html.escape(site_home)}">← Home</a>
      <span class="sep" aria-hidden="true">/</span>
      <a class="brand" href="{html.escape(notes_home)}">Notes</a>
    </div>
    <div class="top-right">
      <button type="button" class="theme-btn" id="theme-toggle" aria-label="Switch theme">Light</button>
      <a class="crumb" href="{html.escape(site_home)}">alubaid.xyz</a>
    </div>
  </header>
  <div class="backdrop" id="nav-backdrop"></div>
  <div class="layout">
    <aside class="sidebar" id="sidebar">{sidebar}</aside>
    <main class="main">
      <article class="article{" home-hero" if is_home else ""}">
        <div class="article-meta">{html.escape(" · ".join(meta_bits))}</div>
        {body_html}
      </article>
      {"".join(pager)}
      <footer class="footer">Unlisted path · theme syncs with alubaid.xyz</footer>
    </main>
  </div>
  <script src="{html.escape(asset_href(base, 'notes.js'))}"></script>
</body>
</html>
"""


def enhance_home_html(body_html: str, notes: list[Note], base: str) -> str:
    cards = []
    for prefix, label, blurb in [
        ("00-Networks-and-Devices", "Networks & Devices", "Types + devices — start here"),
        ("01-Basic-Terminology", "Basic Terminology", "Roles, PDUs, performance, addressing"),
        ("02-Core-Protocols", "Core Protocols", "TCP · UDP · ICMP"),
        ("03-Application-Protocols", "Application Protocols", "DNS, DHCP, HTTP, SSH, mail…"),
        ("04-Building-a-Network", "Building a Network", "Design & ops spine"),
        ("04-Network-Security", "Network Security", "Firewalls, ACLs, Zero Trust"),
    ]:
        target = next((n for n in notes if n.rel_md == f"{prefix}/Index.md"), None)
        href = target.url_path if target else (base.rstrip("/") + f"/{prefix}/")
        cards.append(
            f'<a class="module-card" href="{html.escape(href)}"><strong>{html.escape(label)}</strong><span>{html.escape(blurb)}</span></a>'
        )
    grid = '<div class="module-grid">' + "".join(cards) + "</div>"
    # Insert grid after first paragraph block if possible
    if "</p>" in body_html:
        parts = body_html.split("</p>", 1)
        return parts[0] + "</p>" + grid + parts[1]
    return grid + body_html


def build(out_dir: Path, base: str) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True)
    assets_out = out_dir / "assets"
    shutil.copytree(ASSETS_SRC, assets_out)

    notes = build_notes(out_dir, base)
    idx = link_index(notes)

    # Reading order for prev/next: Home, then modules in INCLUDE order
    ordered = sorted(
        notes,
        key=lambda n: (
            0 if n.rel_md == "Home.md" else 1,
            n.rel_md.lower(),
        ),
    )

    for i, note in enumerate(ordered):
        linked_md = convert_wikilinks(note.body_md, idx, note, base)
        body_html = md_to_html(linked_md)
        is_home = note.rel_md == "Home.md"
        if is_home:
            body_html = enhance_home_html(body_html, notes, base)
        sidebar = render_sidebar(notes, note, base)
        prev_n = ordered[i - 1] if i > 0 else None
        next_n = ordered[i + 1] if i + 1 < len(ordered) else None
        page = page_shell(
            note=note,
            body_html=body_html,
            sidebar=sidebar,
            base=base,
            prev_n=prev_n,
            next_n=next_n,
            is_home=is_home,
        )
        assert note.out_file is not None
        note.out_file.parent.mkdir(parents=True, exist_ok=True)
        note.out_file.write_text(page, encoding="utf-8")

    # manifest for debugging / future search
    manifest = [
        {
            "title": n.title,
            "path": n.url_path,
            "source": n.rel_md,
            "tags": n.tags,
        }
        for n in ordered
    ]
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    # robots hint inside notes folder
    (out_dir / "robots.txt").write_text(
        "User-agent: *\nDisallow: /\n", encoding="utf-8"
    )

    # Keep package docs at ubaid-notes/ (PROMPT.md / README.md live outside site/)
    package = out_dir.parent if out_dir.name == "site" else out_dir
    prompt_src = Path(__file__).resolve().parent / "PROMPT.package.md"
    if prompt_src.exists() and package == PACKAGE_ROOT:
        # Prefer the curated package prompt if present at package root already
        pass

    print(f"Built {len(notes)} pages → {out_dir}")
    print(f"Base path: {base}")
    print(f"Package: {package}")
    print(f"Open: {out_dir / 'index.html'}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build alubaid.xyz/notes static site")
    parser.add_argument(
        "--out",
        type=Path,
        default=DEFAULT_OUT,
        help="Output folder (drop this into the site as /notes)",
    )
    parser.add_argument(
        "--base",
        default="/notes",
        help="URL base path (default: /notes)",
    )
    args = parser.parse_args()
    base = args.base.rstrip("/") or "/"
    if base != "/" and not base.startswith("/"):
        base = "/" + base
    build(args.out.resolve(), base if base != "/" else "/notes")


if __name__ == "__main__":
    main()
