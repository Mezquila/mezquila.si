---
title: "Mezquila site"
created: 2026-11-14T18:30:00+01:00
tags: [website]
---

# mezquila.si

Personal homepage of HP Eder. One page, no build step for the page itself.

- `index.html` is the whole site (styles and script are inline).
- `bottle.webp` and `ramon.webp` are the two images.
- `posts/` holds the essays, one Markdown file each.
- `build.py` rebuilds `posts/index.json`, the list the site reads.

## Writing an essay

1. Create `posts/my-title.md`. The file name becomes the address (`#my-title`), so use lowercase letters, digits and hyphens.
2. Start it with this block, then write the text below in Markdown:

   ```
   ---
   title: "My title"
   created: 2026-11-14T19:30:00+01:00
   summary: "One sentence shown in the list."
   status: draft
   ---
   ```

3. To publish, set `status: published` and add `date: 2026-11-20`.
4. Run `python3 build.py`, then commit and push to `main`. GitHub Pages publishes within a minute or two.

A draft shows as a title with a "draft" tag and cannot be opened. Supported Markdown: headings, bold, italic, links, lists, quotes, images and dividers. Put images in the repository and link them by file name.

## Other things you can change

- **Events ("Where to meet me"):** add entries to `events.json`, for example
  `[{"date": "2026-12-05", "title": "Bar Convent talk", "place": "Berlin", "url": "https://example.com"}]`.
  Past dates hide themselves; the widget only shows when something is upcoming.
- **Newsletter:** in `index.html`, set `NEWSLETTER_URL` to the address of the sign-up page. The widget appears once it is set.
- **Languages:** English text is written directly in the page. German and Spanish live in the `STR` list in the script (short labels) and in the `<template data-lang="de|es">` blocks (whole windows). Change all three when you change a text.
- **Guestbook:** shown entries live in `guestbook.json`, newest first, for example
  `[{"name": "Anna", "place": "Vienna", "message": "Salud!"}]`. To let visitors write, set `GUESTBOOK_FORM` in `index.html` to the address of a form service (for example a Formspree form). Entries arrive by email and are added to `guestbook.json` by hand, so nothing appears unread.
- **Visitor statistics:** set `GOATCOUNTER` in `index.html` to the GoatCounter site code. It uses no cookies.
- **Ritual video:** `ritual.mp4` (16:9) with the still image `ritual.jpg`, shown in the Skull ritual window.
- **Portrait:** `hp-eder.webp` (shown on the page) and `hp-eder.jpg` (full size, for press).
- **Share image:** `og.png` is the picture shown when the link is posted on LinkedIn or WhatsApp.

## Domain

The site is served at https://mezquila.si. The `CNAME` file tells GitHub Pages the domain; DNS is managed at Dynadot (four A records to GitHub Pages, `www` as CNAME to `mezquila.github.io`).
