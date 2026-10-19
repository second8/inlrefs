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
  1. Write `get-roundNN.ps1` to `C:\Users\38349\Desktop\01\system\`. Same format as before: a list of `(folder, filename, weave url)`, skip existing files, retry 3 times, print `Done. X images, Y already there, Z failed.`, CRLF line endings.
  2. Commit it with device_commit_files when the PC is linked. If not, put the URLs in a code block.
  3. Grok runs the script, then Sam clicks Sync folders.
- **Image names:** `<card><round>-NN_<slug>`, for example `n28r7-01_bag-in-spotlight`. The round folder is `<card path>\round N`.

## Building prompts

- **The builder:** `tools/build/` in `second8/inlrefs`. Clone it sparse: `git clone --depth 1 --filter=blob:none --sparse https://github.com/second8/inlrefs && git -C inlrefs sparse-checkout set tools`.
- **New round file:** add `tools/build/collections3/<card>r<N>_<word>.py`. Each round file imports the previous round's `C` and changes only what the feedback asks for. Latest n28 file: `n28r6_campaign.py`.
- **Build:** `python3 builder3.py collections3/<file>.py` writes `out3/<id>.json`, with prompt, images and aspect per shot.
- **New props:** register them in `assets.py` (key: path in `devices/00 Props/`, plus job text). The next prop number is 99. Sheets for Grok always start with "Do NOT run any .ps1 script." and go in a code block.
- **Run each prompt:**
  - weave_run_model, model `bebebed5-50c1-4701-98b3-86929db21585`, input `{prompt, images, resolution:'2K', aspect_ratio}`
  - always a structured Approve/Cancel first, then `acknowledgedCost: 5`
  - poll weave_get_model_run_output
- **Commit tooling changes** back to `tools/` in `second8/inlrefs`, so the next chat has them.

## Where things stand (19 Oct)

- **Credits:** about 2088 Weave credits left.
- **n28 Atelier:** round 6 posted. Sam liked the glass gap and prism ideas, and the campaign camera settings from his Behance refs. Next round waits for his feedback. Full history is in mockup-rules section 9.
- **C11, C3, n22:** waiting on Sam's feedback.
- **n26:** parked.
