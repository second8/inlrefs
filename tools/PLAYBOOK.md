# Inlay Mockup Playbook

The single learning place for Inlay's photographed mockups. Read this before planning any round. It merges `CLAUDE-START.md`, `mockup-rules.md`, Sam's saved preferences and every pin and note on the Inlay Board (52 cards, read 25 Nov 2026).

## 1. What a good Inlay mockup is

- **It is a mockup, not a scene.** The design surface (screen, poster, billboard, card) is the hero: big, sharp, close, almost square-on. Sam, again and again: "you try too much to grab the scene, you forget the mockup."
- **It looks like a real photograph** of a real place on a real day. Never glossy CGI, never stock photo, never "AI". A slightly heightened, clean, movie-like look is good; gritty chaos is not.
- **It is usable on the site.** It must match the look and settings of the mockups already live on inlay.supply (Sam, 22 Nov). The screen comes first, then the environment, and both must be good (21 Nov).
- **One look per collection.** Same grade, light and world on every image. Mixed looks get rejected (n29: "one bright, one snow, one dark, this is bad").

## 2. Hard rules (never break)

**The design surface**
- Large in frame. No wide establishing shots, no tiny boards, no dead space.
- Square-on within about 15 degrees, a true rectangle, never a trapezoid. Flat things on a table are shot from straight above. Bad angles that stretch the design are the most repeated complaint ("again you are doing it from an angle that would stretch the design so much").
- Plain white or paper-white, nothing printed on it, nothing crossing it. Screens are the brightest thing in frame without blowing out ("brighter screen" is a frequent note).
- One clear place for the design per frame. Two mockups in one frame is bad (C4 r6-04). Two screens trip the content filter.
- No halation, fog, haze or glow over the design surface.

**People**
- No faces or profiles. Ever.
- Never tiny people (21 Nov: "don't ever do tiny humans"). People only when they add real life, and never as the subject.
- Real things a real person would do. No staged nonsense (two people holding one phone, a man sitting on a table, a hand hanging limp over a table edge, a glass on a bed).
- Never characters 05 or 08, never the slate mock-neck, don't overuse character 03, no older or unattractive characters.

**Inspiration**
- HARD RULE: never pass an inspiration image to Weave. Describe it in words only. A passed image gets copied almost identically (n29 r2-01). Only our own prop, character and outfit sheets go in as images. `builder3` refuses `refs/inspo` paths.
- Take the feel, light, grade and materials from inspo. Never its exact composition, props or layout ("you stole too much", C4; "comp too similar to the Figma", n32).

**Props and scenes**
- Every object must belong to the world and to the collection's purpose ("tf do I need a book" in a fashion set). No random or cringe props (a bill on a counter, a lone fork).
- Vary the surface type. n32: "all things are just a card, why are you lazy." Plan different objects, not the same object in new places.
- No packaging boxes unless asked. No curled paper corners. No dirt, no "poverty wall", nothing cheap-looking.
- Laptop keyboards: never show too much of them, always with some foreshortening.

**Look**
- Real light shapes, real lenses, real film grain. Fix the AI look with real imperfections and real optics, not with more adjectives.
- Reflections (floor, water) must blend in, never end in a harsh line (3 Nov).
- Don't try too hard to be unique or gimmicky ("too unique, more candid"; "trying too hard"). Candid beats clever.

**Never repeat**
- Never redo a shot that already exists in the finals. Vary object, composition, camera height, lens and light every time. "Same same" is the most common criticism. When Sam says "works, don't overdo it", that shot type is closed.

## 3. Workflow, every round

1. **New feedback:** query board cards where `next == true`. Read finals, pins, crosses, Sam's thread notes and inspo.
2. **Diagnose** in 3 to 5 lines why things failed (angle, distance, light, props, sameness, AI look).
3. **Plan** one bold line per shot: object, composition and camera all different. Say what changed from last round.
4. **Structured Approve** (AskUserQuestion with Approve/Cancel), showing shot count and credits. Never run without it. Never rerun a failure without asking. One approval per batch, never a second cost question.
5. **Run** each prompt on Weave, then poll. Since 25 Nov the model costs **10 credits per image** (it was 5): always quote the real price.
6. **Post** the round to the board card (rounds, a "Round N my read" thread line, `next:false`).
7. **Download script:** `get-roundNN.ps1` to `C:\Users\38349\Desktop\01\system\` via device_commit_files; Sam runs it and clicks Sync folders.
8. **Commit** collection files and docs to `second8/inlrefs` (`tools/`).
9. **Reply short:** what's done, one bold line per item, credits left, the run command in a code block.

## 4. Prompt recipe (builder3)

Blocks in this order, blank line between them:

```
<REGISTER>: <MOMENT, one sentence>
[References: Image 1 is ... ] The output is one single photograph, <format words>.
[Composition line] Shot: <camera position, lens, aperture, where the surface sits, percent of frame it fills, what surrounds it>. <people line>
Place: <world>
Light: <a real light setup>
Palette and grade: <palette; "The same grade on every image of the collection.">
Real: <real block incl. the square-on sentence>
Design surface: <SURFACE LINE IN CAPITALS>
Finish: <camera/film/grain>
Avoid: <max 7 items; the builder drops extras>
```

- **Compositions:** A centred symmetric; B top-down grid; C frame within a frame; D tight crop. None for dynamic shots.
- **Always give the percent of frame** the design surface fills (45 to 85 percent is the working range).
- **Lens language that worked:** 50mm to 135mm, f/4 to f/8, "square to the wall", camera at the height of the board's middle so verticals stay parallel.
- **Aspect:** 4:5 default; 16:9 for wide boards and walls; mix vertical and horizontal when Sam asks.
- **25 Nov:** all 3 prompts that passed our device or easel sheets as GitHub raw URLs failed with a "prompt" error; the 12 without images worked. Before the next ref shot, test one ref (maybe upload it with weave_upload_asset first).
- **Content filter words to avoid:** card slot, card pad, card reader, keypad, chest, sample bag, payment words.
- **Files:** `tools/build/collections3/<id>r<N>_<word>.py`, each round imports the last round's `C` and changes only what feedback asks for. Build with `python3 builder3.py collections3/<file>.py`.

## 5. What Sam praised (do more of this)

- **n31 Open Air (86 finals, "you nailed this direction"):** clear hard daylight, deep blue sky, boards near square-on, clean architectural-documentation finish on medium format. Creativity from vantage, framing and foreground, never from bending the board: water and puddle reflections, frames within frames (viaduct arch, tram window, cable car), sport life (basketball mid-jump, sprinter blur), candid sun shafts. "Pushing creativity to 70% helped a lot."
- **n30 Low Cloud:** moody but still realistic; candid looks; mixed vertical and horizontal; simple fog, kept behind the screen.
- **C4 Beam, n27 Listening Room, n16 Yellow Room:** one hard beam or pinspot, darker shadows, close geometric framing; props that belong to the world (turntable lid, listening post, lot scanner) earned "+1 for creativity".
- **n28 Atelier:** real moments, side crops, hard sun on stone, glass only where it makes sense.
- **n32 Restaurant:** fixed material kit used consistently; push the fanciness; caustics from real glass.

## 6. What Sam rejected (never again)

- Far, wide, scene-grabbing frames. Broken angles. Dead space.
- AI tells: too-perfect hands, glossy materials, too much light, stock-photo framing, illustrative fog.
- Doing the same shot or object over and over (cards, phones, watches, posters, the same table shot).
- Gimmicks that try too hard: railway lines to infinity, circular lobby windows, stacked containers, novelty subjects.
- Glass used just to use glass. Cheap marble. Dirt and grime.
- Things that make no sense: why is this object here, why would a person do that.

## 7. Collection setup checklist (new collection)

1. Read Sam's Figma moodboard with get_screenshot. Describe it in words only.
2. Write the collection's purpose: what kind of designer would use it, and which surfaces belong in that world.
3. List surfaces and moments that fill different gaps; no two shots alike.
4. Fix one world, light, palette and finish for the whole collection.
5. Start with 5 shots, run, post, wait for feedback.
