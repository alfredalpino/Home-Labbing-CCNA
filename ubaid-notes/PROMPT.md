# Paste this entire prompt into the UBAID-Site / alubaid.xyz project chat

---

I added a folder called `ubaid-notes/` to this project. Integrate it as an **unlisted** notes section on my portfolio.

## Goal

- Live at: `https://www.alubaid.xyz/notes/.../.../`
- Example: `/notes/00-Networks-and-Devices/01-Network-Types/LAN/`
- **No visible link** on the homepage, main nav, footer CTAs, or sitemap promotion (direct URL only — same idea as `/wire`)
- Keep existing `/wire` React notes as-is (do not replace unless I ask)
- Match my **main site design line** exactly:
  - Fonts: IBM Plex Sans + IBM Plex Mono
  - Signal teal: light `#1f8f78`, dark `#3dbaa0`
  - Surfaces: dark `#0b0f0e` / light `#f4f7f6`
  - Text: dark `#f2f4f3` / light `#101614`
  - Accent muted greys as on the homepage
  - Sharp `2px` radius, terminal/ops aesthetic (same as `src/styles/index.css` + `/wire`)
  - Theme toggle via `data-theme="light|dark"` and `localStorage` key **`theme`** (must stay in sync with the homepage `useTheme` toggle)

## What to do

1. Copy (or move) the static site from:
   ```text
   ubaid-notes/site/  →  public/notes/
   ```
   After this, `public/notes/index.html`, `public/notes/assets/`, and the curriculum folders must exist.

2. Ensure Vite/Vercel serves `/notes/**` as **static files** from `public/`.
   - Do **not** SPA-rewrite `/notes/*` to the React `index.html`.
   - Keep existing `/wire` rewrites unchanged.
   - Optional: add `X-Robots-Tag: noindex, nofollow` for `/notes/(.*)` (pages already have meta robots noindex).

3. Homepage / Root routing:
   - Do **not** add a Notes link anywhere public.
   - Do **not** add `/notes` to `sitemap.xml` or promote it in `llms.txt`.
   - Optionally add `Disallow: /notes/` in root `robots.txt`.

4. Design continuity check:
   - If anything looks off vs the homepage, restyle `public/notes/assets/notes.css` to pull the same CSS variables / fonts as `src/styles/index.css` and `Notes.module.css` — do not invent a new visual system.
   - Theme button must flip light/dark with a short fade like the site, and persist across `/` ↔ `/notes/`.

5. QA before done:
   - [ ] `/notes/` loads curriculum home
   - [ ] Deep links work (e.g. `/notes/04-Building-a-Network/05-Switching/VLANs/`)
   - [ ] Internal note links work
   - [ ] Theme toggle works and syncs with homepage
   - [ ] Mobile menu/sidebar works
   - [ ] Homepage has **no** Notes link
   - [ ] `/wire` still works

## Done when

I can open a private URL like `alubaid.xyz/notes/...` with portfolio-quality typography + theme toggle, and the public site never mentions Notes.
