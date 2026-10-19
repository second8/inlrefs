# Inlay Board (GitHub version)

Sam's mockup review board. It lives in this folder and is shown by GitHub Pages at:
**https://second8.github.io/inlrefs/board/**

- `index.html`: the board page. Don't edit it unless Sam asks.
- `board.json`: all the board data (cards, rounds, images, pins, crosses, finals, notes). One file, `{"cards":[ ... ]}`.
- `img/<card id>/<name>.jpg`: a round image (max 1600 px). `img/<card id>/<name>_s.jpg` is its thumbnail (max 420 px).
- `img/inspo/`: inspiration images Sam added. `img/up/`: images uploaded from the page itself.
- `g/`: the old built-in gallery images. Leave them alone.

Sam reads and writes the board in his browser with his own GitHub token. Grok reads and writes the same files with git.

---

## A card (one collection)

```json
{
 "id": "n28",
 "title": "n28 Atelier",
 "col": "make",                    // column: live, upload, upscale, make, test, planned, ideas, parked
 "path": "N28 Atelier - Weave",    // folder under C:\Users\38349\Desktop\01\
 "note": "short brief shown on the card",
 "next": true,                     // Sam sent feedback and wants the next round (the "Send feedback" button)
 "nextTs": 1792316558856,
 "uimgs": [ {"n":"n28r6-01_bag-legs-glossy-floor-reflection","l":"n28/n28r6-01_bag-legs-glossy-floor-reflection.jpg","s":"n28/n28r6-01_bag-legs-glossy-floor-reflection_s.jpg","w":1288,"h":1600,"ts":1792321500000} ],
 "rounds": [ {"id":"r6","name":"Round 6","note":"what this round is","ts":1792321500000,"imgs":["n28r6-01_bag-legs-glossy-floor-reflection"]} ],
 "pins":  { "<image n>": [ {"id":"..","t":"Sam's comment","x":49.5,"y":37.8,"done":false,"ts":...} ] },
 "xi":    [ "<image n>", ... ],    // images Sam crossed out (rejected)
 "final": [ "<image n>", ... ],    // images Sam picked for the final collection
 "inspo": [ {"id":"..","asset":"inspo/<file>.jpg","note":"what he wants from it","take":["light","grade",...],"ts":...}, {"id":"..","url":"https://...","note":"..."} ],
 "thread":[ {"id":"..","t":"text","ts":...,"who":"claude"} ],   // who "claude" = the bot (Grok now), no who = Sam
 "upd": 1792321500000              // last time the bot changed the card
}
```

---

## Reading Sam's feedback

1. `git pull`, then open `board/board.json`.
2. Find the cards where `"next": true`. Only those get a new round, never parked or finished ones.
3. For each one, read:
   - `pins` on the images of the latest round
   - `xi` (crossed out, so bad) and `final` (picked, so good)
   - `thread` entries without `who`, newest first (Sam's general notes)
   - `inspo` with its `note` and `take`
4. Use the image `n` names to see which shot each comment is about.

## Posting a round

1. Save each new image as a JPG, max 1600 px on the long side, to `board/img/<card id>/<name>.jpg`, plus a thumbnail of max 420 px to `board/img/<card id>/<name>_s.jpg`. `<name>` is the shot name, for example `n28r7-01_bag-in-spotlight`.
2. `git pull` right before you edit `board.json`, so you have Sam's latest pins.
3. In that card, change only:
   - add one `uimgs` entry per image (`n`, `l`, `s`, `w`, `h`, `ts` = now in milliseconds)
   - add one `rounds` entry `{"id":"r7","name":"Round 7","note":"...","ts":now,"imgs":[names]}`
   - add one `thread` entry with your read: `{"id":"g<now>","t":"Round 7 my read: ...","ts":now,"who":"claude"}`
   - set `"next": false` and `"upd": now`
4. Keep everything else in the file exactly as it is. Never remove Sam's pins, crosses, finals, notes or inspo.
5. Commit and push straight away (`board: n28 round 7`). If the push is rejected, `git pull` and redo step 3 on the fresh file, then push again.

The page picks up changes within about 15 seconds. Images can take a minute to appear.

## Rules

- Never delete images or cards. If something has to go, ask Sam.
- Keep `board.json` valid JSON. Check it before you push (`python -m json.tool board/board.json`).
- One commit per round, not one per image.
