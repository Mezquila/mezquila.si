#!/usr/bin/env python3
"""Rebuild posts/index.json from the Markdown files in posts/.

Each post is posts/<slug>.md with frontmatter:
  title, summary, status (draft | published), date (YYYY-MM-DD, set when published)
Run:  python3 build.py
"""
import json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts")
posts, problems = [], []
for name in sorted(os.listdir(ROOT)):
    if not name.endswith(".md"):
        continue
    slug = name[:-3]
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug):
        problems.append(f"{name}: file name must be lowercase letters, digits and hyphens")
        continue
    text = open(os.path.join(ROOT, name), encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    meta = {}
    if m:
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep and re.fullmatch(r"[A-Za-z_]+", k.strip()):
                meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    draft = meta.get("status", "draft").lower() != "published"
    date = meta.get("date", "") or meta.get("created", "")[:10]
    if not meta.get("title"):
        problems.append(f"{name}: no title in frontmatter")
        continue
    if not draft and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        problems.append(f"{name}: published posts need date: YYYY-MM-DD")
        continue
    posts.append({"slug": slug, "title": meta["title"], "summary": meta.get("summary", ""),
                  "date": "" if draft else date, "draft": draft})

published = sorted([p for p in posts if not p["draft"]], key=lambda p: p["date"], reverse=True)
drafts = sorted([p for p in posts if p["draft"]], key=lambda p: p["title"].lower())
with open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8") as f:
    json.dump(published + drafts, f, ensure_ascii=False, indent=1)
    f.write("\n")
print(f"{len(published)} published, {len(drafts)} drafts")
for p in problems:
    print("SKIPPED", p)
sys.exit(1 if problems else 0)
