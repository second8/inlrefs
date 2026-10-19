# Inlay mockup production: handoff to Grok

You now run Inlay's photographed mockup production end to end: research, art direction, reference sheets, prompts, Figma Weave runs, downloads and filing. Sam reviews and gives feedback. Read this whole file before every new round.

Inlay (inlay.supply) is Sam's premium library of device and print mockups. Every image is a **mockup**: a real-looking photograph with a clean blank surface (a screen, a bag, a card, a tag) where a designer later drops their own design. The design surface is always the hero.

---

## 1. Tools and settings

| Thing | Value |
|---|---|
| Generator | Figma Weave, model **Nano Banana 2.1** (model id `bebebed5-50c1-4701-98b3-86929db21585`) |
| Resolution | **2K** (Sam upscales keepers himself) |
| Aspect | `4:5` portrait by default (use `2:3` or `16:9` only if Sam asks) |
| Cost | 5 credits per image. Balance on 18 Oct: about 2088 |
| Reference images | Up to 5 per prompt, passed as public URLs |
| Reference host | GitHub `second8/inlrefs`, branch `main`. Raw URL: `https://raw.githubusercontent.com/second8/inlrefs/main/<path with spaces as %20>` |
| Local library | `C:\Users\38349\Desktop\01\` (`devices\00 Props`, `devices\00 Character`, `devices\00 Clothing`, device folders, `Materials`, `print`) |
| Output folders | `C:\Users\38349\Desktop\01\<Collection folder>\round N\` |

**Spending rule:** before every Weave run, show Sam the shot list and the total credits, and wait for his clear "approve". Never run without it. Never rerun a failure without asking.

---

## 2. The workflow, every round

1. **Read the feedback.** Sam gives notes per image ("bad", "almost works", "really nice") plus inspiration images or links. Note which images he crossed out and which he liked.
2. **Diagnose.** Work out *why* things failed: the lighting, the lens, the pose, the props, the sameness, the AI look? Write that down in 3 to 5 lines.
3. **Research if he sent references.** Study camera angle, lens, light shape, grade, grain, crop and pose. Take the **settings and feel**, never the exact composition, props, layout, logos or frame borders.
4. **Plan the shots.** Each shot gets its own object AND its own composition AND camera position. No two shots alike. Send Sam the plan: one bold line per shot plus what changes from last round.
5. **New props?** If a shot needs a prop, outfit or set piece we don't have, write a reference sheet for it (section 6), make it, check it, push it to `inlrefs` under `devices/00 Props/` and add it to your reference list. Props come from reference sheets, never from the final mockup run.
6. **Build the prompts** with the template in section 5.
7. **Approve.** Show the shot count and the credits, then wait for Sam's approve.
8. **Run** on Weave, one image per prompt.
9. **Check every image yourself** before Sam sees it, against the rules in section 3. Flag faces, doubled objects, warped surfaces and dead space honestly.
10. **Save** each image as `<collection>-<round>-<NN>_<slug>.png` (for example `n28r6-01_bag-legs-glossy-floor-reflection.png`) into the round folder.
11. **Report** to Sam: the links, a short read (the strongest ones, the weak ones and why), and the credits used and left.

---

## 3. Hard rules (Sam has repeated these, never break them)

**The mockup**
- The device or print surface is the hero: large, sharp, close to the lens. No wide establishing shots, no dead space, no tiny products.
- The design surface faces the camera almost square-on: a true rectangle, never a trapezoid, never warped. Flat things on a table are shot from straight above.
- The design surface is blank: plain white (screens) or plain paper-white (print), nothing printed, nothing crossing it.
- Screens are bright and clean, the brightest thing in the frame, without blowing out.
- Laptop keyboards: never show too much of them, always with some foreshortening.
- One clear place for the design per frame. Print shots can share a frame with a person; a frame with two screens trips the content filter.

**People**
- No faces or profiles. Crop at the shoulders or below, or turn her away. Reflections of a face are the only exception.
- The person is never the subject. Hands, sleeves, legs and bodies only support the product.
- Never character 08, never character 05. Don't overuse character 03. No older people, no unattractive characters.
- Never the slate mock-neck knit (old clothing_01).
- Real, natural poses a person would actually do. No floating objects, no wrong scale, no hand hanging limp over a table edge.

**Inspiration images (HARD RULE, Sam 19 Oct)**
- Never pass an inspiration image (Figma, board inspo, links) to Weave as a reference. Look at it, then describe what to take in words. A passed image gets copied almost identically. Only our own prop, character and outfit sheets go in as image references. builder3 refuses refs/inspo paths.

**Props and scenes**
- Use our own props (section 7) in as many shots as possible. Never props, objects or compositions taken from inspiration images.
- No packaging boxes. No curled or lifted paper corners. No dirty or cheap-looking props. No random extra objects ("cringe props").
- Surfaces should belong to the world of the scene (books in a lab, a bag in an atelier), not the same iPhone everywhere.

**Look**
- No halation, no fog, no haze, no glow bleeding over the design.
- It must not look AI: no glossy CGI, no too-perfect hands, no stock-photo feel. It should feel like a real photographer shot it on a real set.
- Never repeat a shot that already exists in the finals. Vary the object, the composition, the camera height, the lens and the light every time. "Same same" is the most common criticism.

**Working with Sam**
- Only work on the collections he has picked as next. Never touch finished or parked ones.
- Short, clear messages. No em dashes. Anything he has to copy goes in a code block.
- Never delete his files.

---

## 4. Content filter (Weave refuses these and still charges 5 credits)

Avoid these words in prompts: **card slot, card pad, card reader, keypad, chest, sample bag**, and "slot ... emerging". Describe objects neutrally ("a small screen beside a steel panel"). Use one screen per frame. Don't use payment words.

---

## 5. Prompt template

Every prompt is these blocks in this order, separated by blank lines. Sentences in quotes are fixed text: copy them as they are.

```
<REGISTER>: <MOMENT: one sentence, what is happening>

References: Image 1 is <JOB TEXT of ref 1>. Image 2 is <JOB TEXT of ref 2>. ... The output is one single photograph, portrait 4:5.

<COMPOSITION line, optional> Shot: <camera position, lens, aperture, where the design surface sits, how much of the frame it fills (as a percent), what surrounds it>. <PEOPLE LINE>

Place: <WORLD: the set, in one or two sentences>

Light: <LIGHT: a real light setup>

Palette and grade: <PALETTE>

Real: <REAL BLOCK>

Design surface: <SURFACE LINE in capitals for the key part>

Finish: <FINISH: film stock, lens, grain>

Avoid: <comma list, max about 10 items>.
```

**Composition lines (pick one, or none for dynamic shots):**
- A: "Composition A, centred and symmetric: the design surface sits on the centre line, square to the camera, with even space on both sides; strong verticals and horizontals run parallel to the frame."
- B: "Composition B, top-down grid: the camera looks straight down; the design surface's edges run exactly parallel to the frame edges; one clean diagonal of light or shadow crosses the frame beside it, never over it."
- C: "Composition C, frame within a frame: the design surface sits inside a real opening or shape of the place, whose edges run parallel to the photo edges and frame it with an even margin."
- D: "Composition D, tight crop: the camera is very close; the design surface fills most of the frame, its edges nearly touching the photo edges; only a sliver of what holds it shows."

**The square-on sentence (always inside the Real block):**
"The design surface faces the camera almost square-on, within about 15 degrees, so it reads flat and undistorted; its four edges run parallel to the edges of the photograph, a true rectangle, never a trapezoid or keystone; flat things on a table are shot from nearly straight above."

**Real block for fashion and print rounds (current n28):**
"Real: this is a product mockup photograph for a fashion campaign, so the design surface is the hero: it stays sharp, clean and fully readable inside the effect, never covered by it. It is a real photograph made in camera by a campaign photographer, not a render and not a digital filter. <square-on sentence> Only the objects named in the shot are on set. The design surface is new and clean, crisp at its edges and corners, without blowing out."

**Real block for device rounds in real places:**
"Real: this is a product mockup photograph, so the design surface is the hero: it fills most of the frame and the camera is close to it, the way a photographer frames a product, never an establishing shot of the room. The place is only context, glimpsed in fragments at the edges and falling into deep shadow. It is an unstaged photograph of a real place in use, with small honest signs of age on the place only; the design surface itself is new and clean. <square-on sentence> Only the objects named in the shot are in frame. Framing is deliberate and geometric. Exposure is honest, but any lit screen is bright and clean, clearly the brightest surface in the frame, without blowing out. No halation or glow around lights."

**Surface lines:**
- Screen: "THE <DEVICE> SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly brighter than everything else in the frame, evenly lit edge to edge yet not blown out, with crisp corners meeting its thin black border; nothing crosses the screen."
- Bag: "THE BAG FRONT IS PLAIN MATTE PAPER-WHITE BOARD, flat with crisp folded edges and a deep folded top cuff, nothing printed on it."
- Card, tag, label, panel: the same pattern ("THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, nothing printed on it.").

**People lines (pick one):**
- Body crop: "Only her body from the shoulder down to below the knee is in frame, in exactly the outfit from the reference; her head and face are never in frame."
- Hand: "Only her hand and the end of her sleeve are in frame, in exactly the outfit from the reference; nothing else of her is visible."
- Back: "She is seen from behind ... Her face is never visible: she is turned away or cropped by the frame, and no face, cheek, chin or profile shows."
- Add for fashion: "Her pose is a deliberate high-fashion pose: long angled lines, weight dropped onto one hip, never stiff or corporate."

**Reference order:** the product or prop first, then the character sheet, then the outfit sheet. Use max 5. Each reference gets its job text from section 7, so the model knows what to take from it ("take only her skin tone and hands; ignore the clothes and face on the sheet").

**Avoid list (start from this):** a face, chin, lips or profile, logos, letters or brand names anywhere, jewellery, any object not named in the shot, fog or haze, a clean smooth digital look.

---

## 6. Reference sheet template (for new props and outfits)

Make each prop as a clean three-view product sheet, then save and push it.

```
Save to: C:\Users\38349\Desktop\01\devices\00 Props\prop_<NN>-<slug>.png
Create one photograph from this brief. Photorealistic, landscape 3:2, high resolution.
{
  "task": "Product reference sheet for a generic <object>. Clean product photographs, three views side by side in one image.",
  "views": "1 exact front view; 2 three-quarter view; 3 <top view / detail / back view>.",
  "product": "<exact size, material, colour, finish, construction details>. The front is completely plain.",
  "background": "Neutral mid-light grey seamless background, the same for all three views.",
  "lighting": "Soft even studio light from above left, soft contact shadows.",
  "format": "landscape 3:2",
  "negative_prompt": "logos, brand names, text, numbers, watermark, <things it must not have>"
}
```
For outfits, use views of an invisible ghost mannequin: side, front, and back or flat lay. Next free prop number: **101**. After pushing, add the prop to your reference list with a one-line job text.

---

## 7. Reference library (in `second8/inlrefs`)

Use the path to build the raw URL. Use the job text as the "Image N is ..." text in the prompt.

| Key | Path | Job text |
|---|---|---|
| `ch01` | `devices/00 Character/character-01_identity.png` | THE MAN (character 01): head shape, dark textured hair, skin tone, hands and build. Thin titanium glasses. Face not shown unless the shot says so. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch01b` | `devices/00 Character/character-01_backlit.png.png` | THE MAN (character 01), backlit version: silhouette, hair edge and build. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch02` | `devices/00 Character/character-02_identity.png` | THE MAN (character 02): early 40s, short crop with grey at the temples, skin tone, hands and build. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch03` | `devices/00 Character/character-03_identity.png` | THE MAN (character 03): deep brown skin, short curly hair, hands and build. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch04` | `devices/00 Character/character-04_identity.png` | THE WOMAN (character 04): dark brown hair, skin tone, hands and build. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch06` | `devices/00 Character/character-06_identity.png` | THE WOMAN (character 06): long straight black hair in a high ponytail, thin metal glasses, skin tone, hands and build. Face not shown unless the shot says so. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `cl02` | `devices/00 Clothing/clothing_02-stone-polo.png` | CLOTHING ONLY: the stone knitted polo. Ignore the person wearing it. |
| `cl03` | `devices/00 Clothing/clothing_03-graphite-half-zip.png` | CLOTHING ONLY: the graphite half-zip knit. Ignore the person wearing it. |
| `cl04` | `devices/00 Clothing/clothing_04-olive-overshirt.png` | CLOTHING ONLY: the olive cotton overshirt. Ignore the person wearing it. |
| `cl05` | `devices/00 Clothing/clothing_05-pebble-tee.png` | CLOTHING ONLY: the pebble grey-beige t-shirt. Ignore the person wearing it. |
| `cl06` | `devices/00 Clothing/clothing_06-white-tee-blue-jeans.png` | CLOTHING ONLY: white heavyweight tee, mid-blue relaxed jeans, off-white leather sneakers. Ignore the person wearing them. |
| `cl07s` | `devices/00 Clothing/clothing_07-dark-suit-woman.png` | CLOTHING ONLY: the charcoal wool suit with ribbed cuffs. Ignore the person wearing it. |
| `cl07t` | `devices/00 Clothing/clothing_07-satin-for-woman.png` | CLOTHING ONLY: the deep chocolate silk satin blouse and trousers. Ignore the person wearing them. |
| `phone` | `devices/01 Phone - iPhone 18 Pro Max/iphone-18-pro-max_2-photos.jpg` | THE PHONE: exact shape, proportions, thin even black bezels, dark frame. |
| `phone_d` | `devices/01 Phone - iPhone 18 Pro Max/iphone-18-pro-max_1-drawing.png` | PHONE PROPORTIONS: height to width ratio, corner radius, bezel. Do not render the drawing lines or dimensions. |
| `air` | `devices/02 Phone - iPhone Air/iphone-air_2-photos.jpg` | THE PHONE (iPhone Air): very thin, exact shape, proportions and light frame. |
| `air_d` | `devices/02 Phone - iPhone Air/iphone-air_1-drawing.png` | PHONE PROPORTIONS. Do not render the drawing lines or dimensions. |
| `ipad` | `devices/03 Tablet - iPad Pro 13/ipad-pro-13_2-photos.jpg` | THE IPAD: exact shape, thin even bezels, proportions, dark frame. No case unless the shot says so. |
| `ipad_d` | `devices/03 Tablet - iPad Pro 13/ipad-pro-13_1-drawing.png` | IPAD PROPORTIONS. Do not render the drawing lines or dimensions. |
| `laptop` | `devices/04 Laptop - MacBook Neo/macbook-neo_3-photo-open-front.jpg` | THE LAPTOP: exact shape, thin bezels, dark body, proportions. No logo on the lid. |
| `keys` | `devices/04 Laptop - MacBook Neo/macbook-neo_4-keyboard-layout-blank.png` | KEYBOARD LAYOUT ONLY: plain blank keycaps with clean even gaps, no letters. |
| `watch` | `devices/05 Watch - Apple Watch Ultra 4/apple-watch-ultra-4_2-photos.jpg` | THE WATCH: exact titanium case, crown guard and side button. Action button dull and dark. |
| `watch_d` | `devices/05 Watch - Apple Watch Ultra 4/apple-watch-ultra-4_1-drawing.png` | WATCH PROPORTIONS. Do not render the drawing lines or dimensions. |
| `stool_ochre` | `devices/00 Props/prop_25-ochre-lacquer-stool.png` | THE OCHRE STOOL: our own low square stool; take its exact shape, proportions, ochre satin lacquer colour and soft edge wear |
| `bench_oak` | `devices/00 Props/prop_26-oak-bench-chamfered.png` | THE OAK BENCH: take its exact slab top, chamfered square legs, proportions and honey-oak grain |
| `plinth_trav` | `devices/00 Props/prop_27-travertine-plinth.png` | THE TRAVERTINE PLINTH: our own solid honey-beige travertine block; take its exact proportions, open pores, faint veins and honed matte finish |
| `easel_oak` | `devices/00 Props/prop_28-oak-easel.png` | THE OAK EASEL: our own slim honey-oak easel; take its exact legs, cross bar, flat ledge, brass hinge and proportions |
| `vase_char` | `devices/00 Props/prop_29-ceramic-vase.png` | THE VASE: our own charcoal stoneware vase; take its exact ovoid shape, small neck and matte speckled clay |
| `turntable` | `devices/00 Props/prop_30-turntable-smoked-lid.png` | THE TURNTABLE: our own walnut turntable; take its exact plinth, dark platter and felt mat, slim tonearm, two small buttons and smoked dust lid; no markings |
| `mixer` | `devices/00 Props/prop_31-rotary-mixer.png` | THE MIXER: our own rotary mixer; take its exact walnut cheeks, brushed dark top, two rows of knurled knobs and toggles; no markings |
| `niche_walnut` | `devices/00 Props/prop_32-walnut-wall-niche.png` | THE WALNUT NICHE: our own recessed walnut wall niche; take its exact frame, depth, hidden warm strip light and the flush display inside |
| `wafer_carrier` | `devices/00 Props/prop_33-wafer-carrier-epaper.png` | THE WAFER CARRIER: our own translucent wafer carrier; take its exact body, slot stack, white door, recessed handle and the small e-paper tag on the door |
| `lot_scanner` | `devices/00 Props/prop_34-lot-scanner.png` | THE SCANNER: our own white handheld lot scanner; take its exact shape, portrait screen, three blank keys and grey grip |
| `tablet_sleeve` | `devices/00 Props/prop_35-cleanroom-tablet-sleeve.png` | THE SLEEVED TABLET: a tablet sealed in our clear cleanroom pouch; take the pouch, heat-sealed edges, soft corner creases and white hanging tab |
| `passthrough` | `devices/00 Props/prop_36-passthrough-intercom.png` | THE PASS-THROUGH: our own flush steel pass-through hatch with glass door and the steel intercom panel with its small screen, grille and round button |
| `ereader` | `devices/00 Props/prop_37-e-reader.png` | THE E-READER: our own slim charcoal e-reader; take its exact shape, wider grip edge, matte paper-like screen and thin border |
| `peg_rail` | `devices/00 Props/prop_38-oak-peg-rail.png` | THE PEG RAIL: our own honey-oak wall rail; take its exact four turned pegs, brass screws and proportions |
| `watch_stand` | `devices/00 Props/prop_39-oak-watch-stand.png` | THE WATCH STAND: our own small honey-oak stand; take its exact rounded upright and flat base |
| `crate` | `devices/00 Props/prop_40-walnut-record-crate.png` | THE CRATE: our own walnut record crate; take its exact finger-jointed box, low front wall, dark sleeves and the one white divider card |
| `listening_post` | `devices/00 Props/prop_41-listening-post.png` | THE LISTENING POST: our own walnut wall panel; take its exact small screen, aluminium knob, brass hook and black headphones with coiled cable |
| `reticle_pod` | `devices/00 Props/prop_42-reticle-pod.png` | THE RETICLE POD: our own reticle carrier; take its exact translucent lid, dark photomask inside, white base, side latches and white label area |
| `console` | `devices/00 Props/prop_43-handheld-console.png` | THE CONSOLE: our own charcoal handheld console; take its exact grips, thumbsticks, blank round buttons and landscape screen |
| `hanger_tee` | `devices/00 Props/prop_44-oak-hanger-tee.png` | THE TEE ON HANGER: our plain off-white tee on a honey-oak hanger with a brass hook; take its exact cut, fabric and hanger |
| `paper_bag` | `devices/00 Props/prop_45-paper-shopping-bag.png` | THE PAPER BAG: our matte off-white shopping bag; take its exact proportions, folded cuff and rope handles |
| `candle` | `devices/00 Props/prop_46-candle-jar.png` | THE CANDLE: our matte white ceramic candle vessel; take its exact shape, wax, wick and wrap label band |
| `plate` | `devices/00 Props/prop_47-stoneware-plate.png` | THE PLATE: our speckled off-white stoneware plate; take its exact rim and glaze |
| `deck` | `devices/00 Props/prop_48-skateboard-deck.png` | THE DECK: our plain skateboard deck; take its exact popsicle shape, maple ply edge and plain white bottom |
| `cushion` | `devices/00 Props/prop_49-linen-cushion.png` | THE CUSHION: our square off-white linen cushion; take its exact shape and weave |
| `choc` | `devices/00 Props/prop_50-chocolate-bar.png` | THE CHOCOLATE BAR: our bar in a plain off-white paper wrap with foil at one end; take its paper and foil, but keep it thin and flat |
| `rug` | `devices/00 Props/prop_51-flatweave-rug.png` | THE RUG: our flat-woven off-white wool rug; take its exact field, darker border band and knotted fringes |
| `cap` | `devices/00 Props/prop_52-baseball-cap.png` | THE CAP: our plain off-white six-panel cap; take its exact shape, brim and button |
| `pump` | `devices/00 Props/prop_53-pump-bottle.png` | THE PUMP BOTTLE: our frosted amber glass bottle with black pump; take its exact shape and white label |
| `soap` | `devices/00 Props/prop_54-soap-bar-band.png` | THE SOAP: our oatmeal soap bar with a plain paper band; take its exact shape, speckle and band |
| `board` | `devices/00 Props/prop_55-oak-serving-board.png` | THE SERVING BOARD: our honey-oak board with a round-hole handle; take its exact shape and grain |
| `lightbox` | `devices/00 Props/prop_56-walnut-lightbox.png` | THE LIGHTBOX: our walnut-framed wall lightbox with an evenly lit opal face; take its exact frame and depth |
| `cdcase` | `devices/00 Props/prop_57-cd-jewel-case.png` | THE CD CASE: a clear jewel case with smoked black tray; take its exact shape and the plain white insert |
| `banner` | `devices/00 Props/prop_58-felt-banner.png` | THE BANNER: our off-white felt banner on a walnut dowel with black cord; take its exact proportions and felt |
| `beer` | `devices/00 Props/prop_59-beer-bottle.png` | THE BOTTLE: our brown glass longneck with gold cap; take its exact shape, white body label and neck label |
| `smartdisplay` | `devices/00 Props/prop_60-smart-display.png` | THE SMART DISPLAY: our small display on a charcoal fabric wedge base; take its exact shape |
| `cards` | `devices/00 Props/prop_61-playing-cards.png` | THE CARDS: our plain off-white card backs with rounded corners; take their exact size and fan |
| `caddy` | `devices/00 Props/prop_62-bath-caddy.png` | THE BATH CADDY: our slim walnut caddy with a tablet slot; take its exact shape |
| `thermostat` | `devices/00 Props/prop_63-smart-thermostat.png` | THE THERMOSTAT: our round thermostat with brushed ring and round screen; take its exact shape |
| `sweatshirt` | `devices/00 Props/prop_64-folded-sweatshirt.png` | THE SWEATSHIRT: our oatmeal-grey crewneck; take its exact fabric, rib and fold |
| `wine` | `devices/00 Props/prop_65-wine-bottle.png` | THE WINE BOTTLE: our dark green bottle with black capsule; take its exact shape and plain off-white label |
| `resist` | `devices/00 Props/prop_66-resist-bottle.png` | THE RESIST BOTTLE: our amber glass bottle with white cap; take its exact shape and white label |
| `garmentbag` | `devices/00 Props/prop_67-garment-bag.png` | THE GARMENT BAG: our clear bag with a folded white coverall and a white label pocket; take its exact look and hook |
| `labelprinter` | `devices/00 Props/prop_68-label-printer.png` | THE LABEL PRINTER: our white desktop printer; take its exact shape, small screen, three keys and label slot |
| `particle` | `devices/00 Props/prop_69-particle-counter.png` | THE PARTICLE COUNTER: our white handheld counter on its dock; take its exact shape, screen, grip and probe |
| `glovebox` | `devices/00 Props/prop_70-glovebox.png` | THE GLOVEBOX: our stainless glovebox; take its exact window, glove ports, black gloves and flush screen |
| `glasswall` | `devices/00 Props/prop_71-frosted-glass-grid-wall.png` | THE GLASS WALL: our backlit wall of frosted glass panels in a fine black steel grid; take its exact grid proportions, even warm glow and etched texture |
| `bench_perf` | `devices/00 Props/prop_72-perforated-steel-bench.png` | THE BENCH: our galvanised perforated steel street bench with graphite cast end frames; take its exact shape and perforation |
| `wear_c3` | `devices/00 Props/prop_73-c3-wardrobe-ch10.png` | THE OUTFIT: take exactly this cream cable-knit vest over a navy poplin shirt with rolled sleeves, grey pleated wide trousers, brown belt and brown suede loafers |
| `ev_post` | `devices/00 Props/prop_74-ev-charger-post.png` | THE CHARGER: our brushed steel charger post; take its exact body, portrait screen, black card pad and side cable holster |
| `totem` | `devices/00 Props/prop_75-price-totem.png` | THE TOTEM: our black price totem with three lit white panels; take its exact shape |
| `pay_unit` | `devices/00 Props/prop_76-fuel-dispenser-pay-unit.png` | THE PAYMENT UNIT: our steel dispenser panel; take its exact small screen, blank steel keypad, card slot, receipt slot and the pump-top screen above |
| `kiosk` | `devices/00 Props/prop_77-vending-kiosk.png` | THE KIOSK: our graphite vending kiosk; take its exact portrait screen, contactless pad and hatch |
| `tv_lilac` | `devices/00 Props/prop_78-lilac-portable-tv.png` | THE PORTABLE TV: our lilac enamel portable TV; take its exact shape, handle, grille and knobs, but as real enamel with tiny honest wear, not plastic |
| `bike` | `devices/00 Props/prop_79-city-bike-phone-mount.png` | THE BIKE: our matte black city bike with straight bar, black leather grips and the black phone mount at the centre of the bar; take its exact parts |
| `airtower` | `devices/00 Props/prop_80-air-tower.png` | THE AIR TOWER: our brushed steel air tower; take its exact column, small display, two round buttons and coiled black hose |
| `carwash` | `devices/00 Props/prop_81-car-wash-pay-column.png` | THE PAY COLUMN: our graphite car wash column; take its exact sloped head, portrait screen in a steel bezel and concrete island |
| `camera` | `devices/00 Props/prop_82-compact-camera.png` | THE CAMERA: our silver compact digital camera; take its exact body, flash window, side buttons and the flush rear screen |
| `shelter` | `devices/00 Props/prop_83-bus-shelter-lightbox.png` | THE SHELTER: our graphite bus shelter with glass walls and a tall lit lightbox panel at one end; take its exact frame and panel |
| `soda` | `devices/00 Props/prop_84-soda-bottle.png` | THE SODA BOTTLE: our clear glass bottle with silver cap and pale amber soda; take its exact shape and white label, but the glass is dry, no drops |
| `keytag` | `devices/00 Props/prop_85-leather-key-tag.png` | THE KEY TAG: our tan stitched leather tag on a brass ring with two brass keys; take its exact shape |
| `pin` | `devices/00 Props/prop_86-enamel-pin.png` | THE PIN: our round enamel pin with a thin gold rim and flat white face; take its exact front |
| `sleeve` | `devices/00 Props/prop_87-felt-laptop-sleeve.png` | THE LAPTOP SLEEVE: our charcoal felt sleeve with a small tan leather patch; take its exact shape and patch |
| `paywindow` | `devices/00 Props/prop_88-night-pay-window.png` | THE NIGHT WINDOW: our steel-framed security glass window with sliding tray in a graphite wall and the small screen with speaker grille beside it |
| `bag_atelier` | `devices/00 Props/prop_89-atelier-shopping-bag.png` | THE SHOPPING BAG: our matte warm ivory bag with flat espresso ribbon handles; take its exact proportions, folded cuff and handles |
| `wear_n28` | `devices/00 Props/prop_90-n28-wardrobe-ch13.png` | THE OUTFIT: take exactly this oversized stone wool-crepe blazer, wide pleated stone trousers, ivory silk shell top and espresso suede loafers |
| `hangtag` | `devices/00 Props/prop_91-hang-tag.png` | THE HANG TAG: our thick ivory tag with an espresso cord and small brass safety pin; take its exact shape |
| `tissue` | `devices/00 Props/prop_92-tissue-seal.png` | THE TISSUE: our folded warm ivory tissue bundle with one round espresso sticker seal at the centre |
| `gcover` | `devices/00 Props/prop_93-garment-cover.png` | THE GARMENT COVER: our stone canvas garment cover with espresso piping on an oak hanger, with a flat ivory front panel |
| `airpods` | `devices/06 Audio - AirPods Pro 3/airpods-pro-3_3-photo.jpg` | THE AIRPODS CASE: exact shape and size, white. |
| `airmax` | `devices/07 Audio - AirPods Max/airpods-max_2-photo-front.jpg` | THE HEADPHONES: exact over-ear shape, mesh headband, cups. No logo. |
| `vision` | `devices/08 Vision - Apple Vision Pro/apple-vision-pro_2-photo-worn.jpg` | THE HEADSET: exact shape of the Vision Pro, worn. No logo. |
| `appletv` | `devices/09 TV - Apple TV 4K and Siri Remote/apple-tv-4k-and-remote_3-photo-angle.png` | THE REMOTE: exact shape of the small silver remote. |
| `airtag` | `devices/10 Accessory - AirTag/airtag_2-photo.png` | THE TAG: exact round white tag. |
| `display` | `devices/11 Display - Studio Display XDR/studio-display-xdr_1-front-and-side.jpg` | THE DISPLAY: exact shape, thin bezel, stand and proportions of the Studio Display XDR. No logo. |
| `p_hard` | `inlrefs-push/print/01 Book - hardcover/hardcover-book_1-photo-held-blank-cover.png` | THE BOOK: a blank cloth hardcover, object design only, not its composition. |
| `p_spiral` | `inlrefs-push/print/02 Book - spiral bound A4/spiral-bound-book_1-photo-lying-hard-shadow.png` | THE BOOK: spiral-bound A4, object design only. |
| `p_cards` | `inlrefs-push/print/04 Cards - business cards/business-cards_2-photo-two-stacks.png` | THE CARDS: blank business cards, object design only. |
| `p_soft` | `inlrefs-push/print/06 Book - softcover perfect bound/softcover-book_2-photo-held-open-spread.png` | THE BOOK: blank softcover perfect-bound, object design only. |
| `ch07` | `devices/00 Character/character-07_identity.png` | THE WOMAN (character 07): about 34, dark curly hair tied back, olive skin, average build, hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch09` | `devices/00 Character/character-09_identity.png` | THE WOMAN (character 09): about 30, East Asian, black blunt bob, small hands, slim build. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `cl08` | `devices/00 Clothing/clothing_08-lab-coat.png` | CLOTHING ONLY: the pale grey lab coat and grey nitrile gloves. Ignore the person wearing it. |
| `cl09` | `devices/00 Clothing/clothing_09-navy-work-jacket.png` | CLOTHING ONLY: the faded navy work jacket. Ignore the person wearing it. |
| `cl10` | `devices/00 Clothing/clothing_10-canvas-apron.png` | CLOTHING ONLY: the canvas bib apron over an ecru workshirt. Ignore the person wearing it. |
| `cl11` | `devices/00 Clothing/clothing_11-navy-overcoat-scarf.png` | CLOTHING ONLY: the navy wool overcoat and oatmeal scarf. Ignore the person wearing it. |
| `cl12` | `devices/00 Clothing/clothing_12-sage-polo.png` | CLOTHING ONLY: the sage knit polo. Ignore the person wearing it. |
| `cl13` | `devices/00 Clothing/clothing_13-cream-silk-set.png` | CLOTHING ONLY: the cream silk shirt and pleated cream trousers. Ignore the person wearing them. |
| `pr01` | `devices/00 Props/prop_01-wall-display.png` | THE WALL DISPLAY: exact shape, thin black bezel, flat wall mount. No logo. |
| `pr02` | `devices/00 Props/prop_02-card-terminal.png` | THE CARD TERMINAL: exact shape, screen, paper roll, dock. No logo. |
| `pr03` | `devices/00 Props/prop_03-metal-card.png` | THE METAL CARD: brushed metal, chip, rounded corners. No logo, no numbers. |
| `pr04` | `devices/00 Props/prop_04-tv.png` | THE TV: exact thin black frame and stand. No logo. |
| `pr05` | `devices/00 Props/prop_05-cafe-cups.png` | THE CUPS: plain white ceramic cup and saucer, plain takeaway cup. No logo. |
| `pr06` | `devices/00 Props/prop_06-canvas-tote.png` | THE TOTE: plain natural canvas tote. No print. |
| `pr07` | `devices/00 Props/prop_07-badge-lanyard.png` | THE BADGE: blank card badge on an off-white lanyard with a metal clip. |
| `pr08` | `devices/00 Props/prop_08-linen-tester.png` | THE LINEN TESTER: folding metal loupe. No logo. |
| `pr09` | `devices/00 Props/prop_09-cabin-suitcase.png` | THE SUITCASE: grey hard-shell cabin case. No logo. |
| `pr10` | `devices/00 Props/prop_10-lab-bench-kit.png` | THE LAB KIT: grey pipettes on a stand, mustard and terracotta tube racks. No logo. |
| `ch10` | `devices/00 Character/character-10_identity.png` | THE MAN (character 10): about 30, Southern Italian, light olive skin, thick dark brown wavy hair pushed back, light stubble, lean athletic build, hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch11` | `devices/00 Character/character-11_identity.png` | THE MAN (character 11): about 28, Danish, fair skin, short ash-blond hair, clean shaven, tall and lean, long slim hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch12` | `devices/00 Character/character-12_identity.png` | THE MAN (character 12): about 32, Korean, light skin, neat thick black hair with a soft side part, clean shaven, slim build, slim hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch13` | `devices/00 Character/character-13_identity.png` | THE WOMAN (character 13): about 28, Irish, fair freckled skin, straight auburn shoulder-length hair, slim build, slim freckled hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch14` | `devices/00 Character/character-14_identity.png` | THE WOMAN (character 14): about 30, Black British, medium-dark skin, short natural tight curls, slim elegant build and hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `ch15` | `devices/00 Character/character-15_identity.png` | THE WOMAN (character 15): about 26, Spanish, warm light-tan skin, long dark brown wavy hair in a loose low ponytail, slim build, small hands. Face not shown. Use only the face, hair, skin, hands and build from this sheet; ignore the clothes in it. |
| `cl14` | `devices/00 Clothing/clothing_14-camel-coat.png` | CLOTHING ONLY: the camel wool coat over the cream roll-neck, dark brown trousers. Ignore the person wearing it. |
| `cl15` | `devices/00 Clothing/clothing_15-oxford-shirt.png` | CLOTHING ONLY: the white oxford shirt, sleeves rolled, navy chinos. Ignore the person wearing it. |
| `cl16` | `devices/00 Clothing/clothing_16-olive-overshirt.png` | CLOTHING ONLY: the olive cotton overshirt over a white tee, ecru trousers. Ignore the person wearing it. |
| `cl17` | `devices/00 Clothing/clothing_17-breton-stripe.png` | CLOTHING ONLY: the navy and ecru breton stripe top, black trousers. Ignore the person wearing it. |
| `cl18` | `devices/00 Clothing/clothing_18-rust-cord.png` | CLOTHING ONLY: the rust corduroy shirt-jacket over a cream tee, indigo jeans. Ignore the person wearing it. |
| `cl19` | `devices/00 Clothing/clothing_19-grey-lounge.png` | CLOTHING ONLY: the soft grey hoodie and joggers. Ignore the person wearing it. |
| `cl20` | `devices/00 Clothing/clothing_20-sand-linen.png` | CLOTHING ONLY: the loose sand linen shirt and ecru linen trousers. Ignore the person wearing it. |
| `cl21` | `devices/00 Clothing/clothing_21-black-blazer.png` | CLOTHING ONLY: the black unstructured blazer over a white tee, black trousers. Ignore the person wearing it. |
| `cl22` | `devices/00 Clothing/clothing_22-green-cardigan.png` | CLOTHING ONLY: the forest green cardigan over a white tee, light grey trousers. Ignore the person wearing it. |
| `cl23` | `devices/00 Clothing/clothing_23-denim-shirt.png` | CLOTHING ONLY: the light blue denim shirt, sleeves rolled, ecru wide trousers. Ignore the person wearing it. |
| `look_coat` | `devices/00 Props/prop_94-n28-look-black-coat.png` | THE OUTFIT: take exactly this long black cocoon coat with the wide wrapped collar, black wide trousers pooling on the floor and black pointed boots |
| `look_slip` | `devices/00 Props/prop_95-n28-look-ivory-slip.png` | THE OUTFIT: take exactly this ankle-length ivory satin slip dress with the cowl neckline and the oversized ivory knit cardigan draped over the shoulders, ivory pointed mules |
| `look_shirt` | `devices/00 Props/prop_96-n28-look-shirt-dress.png` | THE OUTFIT: take exactly this oversized white poplin shirt dress with the stand collar, full sleeves gathered into very deep stiff cuffs, slim black belt, black slingback heels |
| `look_gown` | `devices/00 Props/prop_97-n28-look-black-gown.png` | THE OUTFIT: take exactly this floor-length one-shoulder matte black jersey gown with the drape at the hip, long black gloves, black pumps |
| `gal_lightbox` | `devices/00 Props/prop_99-gallery-lightbox.png` | THE LIGHTBOX: our tall freestanding gallery lightbox; take its exact slim matte black frame, depth, low steel feet and evenly lit opal face, scaled as the shot says |
| `crt` | `devices/00 Props/prop_100-grey-crt-monitor.png` | THE CRT MONITOR: our warm light grey 1990s CRT; take its exact deep rounded back, thin bezel, curved glass and small power button |
| `marble` | `devices/00 Props/prop_98-marble-block.png` | THE MARBLE BLOCK: our solid white honed marble block with soft grey diagonal veining and crisp edges; take its exact proportions |

Retired, never use: character 05, character 08 (`ch08`), and the slate mock-neck clothing_01.

---

## 8. Collections status (18 Oct)

| Collection | Folder | Status |
|---|---|---|
| C4, n27, n11, n16 | their own Weave folders | **Done.** Finals saved. Do not touch. |
| C11 lightbox | `Collection 11\round N` | 6 rounds done. Last ask: more character and intent, screens most important, the wall works as one huge screen with the same design, real angles and depth. Waiting on feedback. |
| C3 | `Collection 3 - Weave` | 4 rounds. ch10 in the cream cable vest look (`wear_c3`), perforated steel bench, ribbed concrete wall, direct flash. Waiting on feedback. |
| n22 Canopy | `N22 Canopy - Weave` | 4 rounds. Fuel forecourt at night and inside the car. Waiting on feedback. |
| n26 Tonal | `N26 Tonal - Weave` | 2 rounds. Parked. |
| **n28 Atelier** | `N28 Atelier - Weave\round N` | **Active.** See section 9. |
| **n29 Spatial Awareness** | `N29 Spatial - Weave\round N` | **Active, new 19 Oct.** Art installation mockups. See CLAUDE-START. |
| **n30 Low Cloud** | `N30 Low Cloud - Weave\round N` | **Active, new 19 Oct.** City screens under low cloud. See CLAUDE-START. |

Only work on the collections Sam says are next.

---

## 9. n28 Atelier: where we are (the active one)

**Brief:** high-fashion campaign mockups of print. Our shopping bag (`bag_atelier`), hang tag (`hangtag`), tissue seal (`tissue`), garment cover (`gcover`), invitation card, lookbook, plus the occasional device. Cast `ch13`, never her face.

**Outfits** (use different ones across a round): `look_coat` (black cocoon coat), `look_slip` (ivory satin slip and cardigan), `look_shirt` (white poplin shirt dress, big cuffs), `look_gown` (one-shoulder black gown, long gloves). The old stone suit `wear_n28` is too close to his inspiration, don't use it.

**What Sam said, round by round:**
- **R1 (warm greige studio, 80mm):** bad studio, corporate poses, not elegant. Too close to his inspo clothing.
- **R2 (black and white, black backdrop, marble block):** better direction. But flat, "almost AI". The marble looks cheap: never use `marble` again. Devices crossed.
- **R3 (dark hall under a glowing light ceiling, wide low lens):** bland, not artistic enough.
- **R4 (one in-camera trick each: flash drag, blade of light, fluted glass, 200mm spotlight):** only the invitation through fluted glass had potential.
- **R5 (glass variations):** "started to work great". Liked best: the invitation with a prism ghost, and the garment cover through a gap in a fluted glass screen. Bad: glass used just to use glass (bag past a ribbed wall). Weaker: hang tag beside reeded glass.
- **R6 (Behance camera settings):** my read was that the strongest were the bag on a glossy black floor with a spotlight pool and mirror reflection, the hang tag in diagonal slatted light, and the garment cover between glass panels. The prism with the bag failed: it doubled the bag and the woman. **Sam on R6: all bad, except the hang tag in slatted light 'good image quality but bad environment'.** R5 he rated all 'almost good', 05 generic.
- **R7 (atelier after hours), rejected:** 'makes 0 sense, why would a person stick between 2 glasses with a bag'. Only the tag on the vitrine glass was 'almost'.
- **R7 plan was:** R6 film finish plus R5 glass, but the glass belongs to the place: lime plaster walls, oak floor, steel-framed fluted glass partitions, vitrines and fitting-room doors. No void, no seamless.

- **R8 (19 Oct):** Sam: 'r4 still is the closest and best, camera, position, framing and people; I don't like the art direction; glass usage there was better.' 'The og inspo with the black bg studio look is the art direction I want.' New inspo: B&W bag carried in a side crop on black, hang tags on garments on a rail in hard light, a shirt on a hanger with a tag on plain grey, a card in folded tissue. R8 = black studio, B&W Tri-X, real moments only.

**The direction that works now (updated R8):** black studio, black and white, R4 camera and crops, every shot a moment that could really happen. Older notes below:
- A real art-directed accessories campaign: hard shaped light (spotlight pools, slats, blades), glossy floors with reflections, grey seamless with a spotlight halo, intimate 35 to 50mm crops of a hand or legs with the product, and wit in the pose.
- Neutral colour: no blue or colour casts. Real film grain, Portra 400 or Tri-X, visible but natural.
- Glass and prism effects only when they add meaning, and the design surface must stay single, sharp and outside the effect.
- **Sam's camera references:** Behance "FASHION FLIP BOOK" (Agata Serge), "Campaign for RANDEZ-VOUS" (Kamilla Hanapova), "THE GSTAAD GUY x YUNG MAG" (Per Appelgren). Take their settings only, never their framing borders or compositions.
- **Sam wants small rounds now:** 4 to 6 images, each one deliberate.

---

## 10. Lessons learned (what fails)

- **Sameness:** the same object, composition and camera across a round. Vary all three every shot.
- **Too wide:** full figures with space around them kill the mockup. Keep it close.
- **Flat AI look:** fix it with real light shapes, real lenses, real film grain and real imperfections, not with more adjectives.
- **Face leaks:** wide or low shots of a standing person show the chin or lips. Crop explicitly or turn her away. Check every image.
- **Effects that double or cover the product:** prism and glass must never touch the design surface.
- **Cheap materials:** marble, glossy CGI and staged scenes read as fake.
- **Taking from the inspiration:** copying its props or composition. Take the feel only.

---

## 11. First job: download n28 rounds 3 to 6

These were made while the office PC was offline. Save each one to `C:\Users\38349\Desktop\01\N28 Atelier - Weave\round N\` under the file name shown.

**round 3**
```
n28r3-01_walking-into-the-light-bag-on-back.png  https://media.weavy.ai/image/upload/v1792317006/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dxb4ar9qimsb3oxjyflv.png
n28r3-02_bag-swung-out-mid-turn.png  https://media.weavy.ai/image/upload/v1792317037/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/lbua93dqntxq2zmx0lpj.png
n28r3-03_garment-cover-under-the-light.png  https://media.weavy.ai/image/upload/v1792317048/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/rcl8uffyv8nxeabqzojs.png
n28r3-04_hang-tag-arm-reaching-to-lens.png  https://media.weavy.ai/image/upload/v1792317056/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/dsxijfagfawzcbjjejme.png
n28r3-05_invitation-held-out-seated-on-floor.png  https://media.weavy.ai/image/upload/v1792317073/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wybk4afvyu1dfdfpo4ol.png
```
**round 4**
```
n28r4-01_flash-and-drag-spin-bag-frozen.png  https://media.weavy.ai/image/upload/v1792320025/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jz8w4gdh0ec0mdqtih1g.png
n28r4-02_blade-of-light-across-the-bag.png  https://media.weavy.ai/image/upload/v1792320039/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/gxyh8pspgbjquvwrfg1l.png
n28r4-03_invitation-through-fluted-glass.png  https://media.weavy.ai/image/upload/v1792320057/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/skugbfkhnotxorlfbi9s.png
n28r4-04_long-lens-spotlight-bag-at-her-feet.png  https://media.weavy.ai/image/upload/v1792320077/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/v3kbfm25fhmrjnq56kn1.png
```
**round 5**
```
n28r5-01_bag-beside-fluted-glass-coat-sliced.png  https://media.weavy.ai/image/upload/v1792320333/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/bscpheks8uokweqdw05f.png
n28r5-02_hang-tag-beside-reeded-glass.png  https://media.weavy.ai/image/upload/v1792320356/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/fiqdqctvgb7axxici8fu.png
n28r5-03_garment-cover-through-gap-in-glass-screen.png  https://media.weavy.ai/image/upload/v1792320378/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/nc4achlrkttpkbjhu2zq.png
n28r5-04_invitation-prism-ghost.png  https://media.weavy.ai/image/upload/v1792320394/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qvt8aokfys4qo9qsh4t0.png
n28r5-05_bag-held-past-ribbed-glass-wall.png  https://media.weavy.ai/image/upload/v1792320407/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/qc424ltypolyhe5344vx.png
```
**round 6**
```
n28r6-01_bag-legs-glossy-floor-reflection.png  https://media.weavy.ai/image/upload/v1792321371/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/ierelkmlybfn2pryat4z.png
n28r6-02_seated-stool-spotlight-halo-invitation.png  https://media.weavy.ai/image/upload/v1792321385/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/x3pgi5uu4wmjkur8ximj.png
n28r6-03_lying-on-floor-bag-held-over-face.png  https://media.weavy.ai/image/upload/v1792321413/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wvz5xaf1gkmraapbdaf3.png
n28r6-04_bag-prism-ghost.png  https://media.weavy.ai/image/upload/v1792321425/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/jtpe9zxclmoy4wixwlpy.png
n28r6-05_hang-tag-slatted-light-hand.png  https://media.weavy.ai/image/upload/v1792321444/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/v1nnkcr4pt7bes5ueatl.png
n28r6-06_garment-cover-between-glass-panels-top-light.png  https://media.weavy.ai/image/upload/v1792321464/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/wenshfe5cniqic48wtwa.png
```

---

## 12. The board (where Sam reviews)

The review board now lives in the repo you already use: `second8/inlrefs`, folder `board/`. Sam sees it at **https://second8.github.io/inlrefs/board/**.

- **Read `board/README.md` first.** It explains the data file, how to read Sam's feedback (pins, crosses, finals, notes, inspo) and how to post a round.
- **After every Weave run:**
  1. Put the images on the board yourself: a JPG of max 1600 px plus a thumbnail of max 420 px, a round entry, and your short read.
  2. Set `"next": false` on that card.
  3. Push.
- **Your downloads:** they still go into the PC folders as before.
- **When you start a round:** only work on cards where Sam set `"next": true`.
