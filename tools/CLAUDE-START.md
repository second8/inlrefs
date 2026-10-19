# Start here: Claude runs Inlay mockup rounds

You are continuing Sam's Inlay mockup production. You (Claude) plan, write prompts, run Figma Weave and post rounds to the board. Grok, Sam's bot on his PC, only makes prop sheets and runs download scripts.

**Read `tools/mockup-rules.md` fully before the first round.** It holds the hard rules, the prompt template, the reference library, the collection status and the n28 history. Ignore its parts that say Grok runs Weave or that point at a GitHub board: those are replaced by this file.

## Cost rules (Sam's tokens are limited)

- Short replies: plan, approve, results. No long reads unless he asks.
- Run Weave directly in this chat. No subagents.
- No browser screenshot reviews of every round. Sam reviews on the board. Look only when he asks, and then as one small contact sheet.
- Batch: take feedback for all ticked collections at once and run them together.

## The board (Claude artifact)

- **URL:** `https://claude.ai/artifact/SPsBPpikpBG8YT3RvEDWGW`. Data is in the `cards` collection; edit it with the ArtifactData tool.
- **Feedback arrives** when Sam says "new feedback in". Query cards where `next == true`. Only those get rounds, never parked or finished ones.
- **Reading a card:**
  - `pins` (per image `n`), `xi` (crossed, so bad), `final` (picked)
  - `thread` entries without `who` (Sam's notes)
  - `inspo`: an `asset` id can be read with Artifact `read` + `path`
- **Posting a round:** one `update` on the card, pinned with `if_version` from a fresh get:
  - `rounds`: the existing ones plus `{id:'rN', name:'Round N', note, ts, imgs:[names]}`
  - `thread`: the existing ones plus `{id:'cl<ts><card>', t:'Round N my read: ...', ts, who:'claude'}`
  - `next: false`, `upd: ts`
- **Images reach the board through Sam's "Sync folders" button,** which reads his PC folder. So after a run:
  1. Write `get-roundNN.ps1` (one script can cover several cards: `'folder>name|url'` items) to `C:\Users\38349\Desktop\01\system\` with `python3 tools/build/dl/mkps1.py <out.ps1> '<card path>\round N' 'name|url' ...`. Same format as before: a list of `(folder, filename, weave url)`, skip existing files, retry 3 times, print `Done. X images, Y already there, Z failed.`, CRLF line endings.
  2. Commit it with device_commit_files when the PC is linked. If not, put the URLs in a code block.
  3. Grok runs the script, then Sam clicks Sync folders.
- **Image names:** `<card><round>-NN_<slug>`, for example `n28r7-01_bag-in-spotlight`. The round folder is `<card path>\round N`.

## Building prompts

- **The builder:** `tools/build/` in `second8/inlrefs`. Clone it sparse: `git clone --depth 1 --filter=blob:none --sparse https://github.com/second8/inlrefs && git -C inlrefs sparse-checkout set tools`.
- **New round file:** add `tools/build/collections3/<card>r<N>_<word>.py`. Each round file imports the previous round's `C` and changes only what the feedback asks for. Latest files: n28 `n28r20_plus50.py` (Sam asks for 5 at a time, push creativity), n30 `n30r7_ten.py`, n31 Open Air `n31r4_ten.py` (moodboard Figma 199:1377, clear-day OOH) (n29 Spatial deleted by Sam 19 Oct, do not continue). Shots can set their own `aspect` and `format_words` (n30 r3 uses 16:9). `refs/inspo/` holds old inspo copies: never use them as Weave refs.
- **Build:** `python3 builder3.py collections3/<file>.py` writes `out3/<id>.json`, with prompt, images and aspect per shot.
- **New props:** register them in `assets.py` (key: path in `devices/00 Props/`, plus job text). The next prop number is 101. Sheets for Grok always start with "Do NOT run any .ps1 script." and go in a code block.
- **Run each prompt:**
  - weave_run_model, model `bebebed5-50c1-4701-98b3-86929db21585`, input `{prompt, images, resolution:'2K', aspect_ratio}`
  - always a structured Approve/Cancel first, then `acknowledgedCost: 5`
  - poll weave_get_model_run_output
- **Commit tooling changes** back to `tools/` in `second8/inlrefs`, so the next chat has them.

## Where things stand (19 Oct)

- **Credits:** about 1153 Weave credits left.
- **n28 Atelier:** round 13 posted (all-new moments: poster on wall, lookbook at cafe, car back seat, hand-off, cafe chair). Finals: R9 01, 02, 04, 05; R10 01, 03, 04, 05; R11 02-05; R12 01, 03, 04, 05. Sam: 'don't get lazy, new ideas, not repeating'; glass only where natural, never 'glass just to use glass'.
- **n29 Spatial Awareness:** round 6 posted. R5 'too warm'. Look now = his inspo (Figma 193:1348 translucent box): dark gallery, black floor/walls, low grid ceiling catching cool teal-green glow, moody and imperfect; compositions rebuilt from the Figma moodboard in words. Stay on his moodboard.
- **n30 Low Cloud:** finals: all R2, R3 01, 02, 05, all R4. Round 5 posted: same candid look, new places.
- **C11, C3, n22:** waiting on Sam's feedback.
- **n26:** parked.

## Changing the board itself (new versions)

The board page is one large HTML file, about 3.3 MB, because the old gallery thumbnails are embedded in it.

1. `Artifact` action `read` on the board URL. It saves the full HTML to a file and tells you where.
2. Edit only what Sam asks, with small targeted string replacements in Python. Never retype the file and never touch the `galdata` JSON block.
3. Publish with `url` set to the board URL, so it stays the same link. Keep its capabilities: assets, db and downloads.

**Features Sam relies on, keep them working:**
- the inspo panel keeps its scroll position on re-render (fixed 19 Oct: it used to jump to the top, so 6+ inspo images got lost)
- columns and phases
- the LATEST round tag
- the workspace: pins, crosses, finals, round tabs and inspo with the "take" chips
- Send feedback (`next`) in the workspace top bar
- the "Copy for Claude: new feedback in" button
- Sync folders, which uploads 1600 px and 420 px JPGs as assets and adds uimgs and rounds
- the finals .ps1 export

**Data rules:**
- uimgs: `{n, l, s, w, h, ts}`, where `l` and `s` are asset ids
- inspo images are asset ids
- never delete Sam's pins, crosses, finals or notes

## What Sam judges on (read before planning any round)

- **One look per collection:** same grade, light and world on every image of a collection. Mixed looks get rejected.
- **HARD RULE, inspo in words only:** never pass an inspiration image (Figma, board inspo) to Weave. Describe it in words. Passed images get copied near-identically (n29 r2-01 copied his Figma ref). Only our prop, character and outfit sheets are image refs; builder3 refuses refs/inspo.
- **RULE, be intentional (Sam 19 Oct):** every image must serve what the collection is for. Before planning, list what the collection is (e.g. n28 = mockup kit for a fashion label identity), what finals already cover, and what touchpoints are missing; each shot fills one gap. No random objects or props (n28 r7 "makes 0 sense", r13 lookbook "tf do I need a book").
- **Tags and small print need tight crops:** the mockup surface must be big; a tag lost on a whole garment is wrong.

- **Variety:** vary the object, the composition and the camera in every shot. "Same same" is his most common complaint.
- **Close:** the design surface is big and square-on, with no dead space.
- **No faces or profiles,** ever.
- **Real, not AI:** real light shapes, real lenses, real film grain. Flat, glossy or stock-looking images get rejected.
- **Plan first:** send a short plan with one bold line per shot, then the Approve. He wants intentional, researched choices, not random ones.
