# n28 Atelier, new collection (Sam 17 Oct: "create a mockup like this, high fashion" with a reference of a cropped figure in grey
# tailoring carrying a white shopping bag). Sam chose: warm greige tonal (not B&W), ch13, 12 shots, mostly print plus 3 devices.
# Our own props 89-93 and outfit; reference used for feeling only (light, crop, drape), never its bag or design.
C={
 'id':'n28','name':'Atelier','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A quiet high-fashion campaign photograph shot in a photo studio',
 'world':'A fashion photo studio: a seamless warm greige paper backdrop that falls off into deep espresso shadow toward the edges and top, a pale stone floor sweep. Only what the shot names is on set.',
 'world_short':'A fashion photo studio: a seamless warm greige paper backdrop falling off into deep espresso shadow, a pale stone floor sweep.',
 'light':'One very large soft box from the side, about 4500K, wrapping the fabric in long soft gradients and deep soft shadows; no fill, so one side of every form falls into warm shadow. The design surface catches the light cleanly.',
 'palette':'Tonal greige: stone #B8AFA2, greige #CFC7BA, ivory #EEE8DD, espresso #3A2C24 for the darks, warm grey shadows. The design surface is the only clean white. Very low saturation, rich soft contrast.',
 'finish':'Medium-format film look, 80mm and 120mm macro, f/4 to f/5.6, fine visible grain, soft rolled highlights, no halation, no haze. Quiet, expensive, editorial.',
 'cast':{'her':'ch13'},'wear':{'her':'the outfit from the reference'},
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','bright colours','any object not named in the shot','a glossy computer-generated look'],
}
PL='Only her body from the shoulder to the knee is in frame, in exactly the outfit from the reference, the fabric falling in large soft folds; her head and face are never in frame.'
PLH='Only her hand and the end of the blazer sleeve are in frame, in exactly the outfit from the reference; nothing else of her is visible.'
W=['ch13','wear_n28']
def sh(n,slug,kind,noun,refs,comp,moment,shot,pl=PL,surface=None,who=True,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs+(W if who else []),'people_line':pl if who else None,'people':'line' if who else 'none','comp':comp,'moment':moment,'shot':shot}
    if not who: d.pop('people_line')
    if surface: d['surface']=surface
    d.update(kw);return d
BL='nothing printed on it'
S=[
 sh(1,'bag-carried-side-profile','print','the bag front',['bag_atelier'],'A','She walks out of the fitting with our ivory shopping bag hanging from her hand at her side, body in profile.',
  'Straight on to the bag, camera at the height of the bag, 80mm, f/4. The bag front faces the camera square, filling about 55 percent of the frame width, sharp, on the centre line; her body in profile behind it, the blazer and wide trousers draping in long folds; the espresso handles over her fingers; the backdrop falls into dark at the edges.',
  surface='THE BAG FRONT IS PLAIN MATTE WARM IVORY BOARD, flat with crisp folded edges, '+BL+'.'),
 sh(2,'bag-at-her-feet-low','print','the bag front',['bag_atelier'],'A','Her shopping bag set down on the stone floor beside her, the wide trouser hems breaking over the loafers.',
  'Low, camera at floor height, 80mm, f/4. The bag stands on the centre line, front square to the camera, filling about 55 percent of the frame height, sharp; her trouser hems and one loafer at the side; long soft shadow behind.',
  pl='Only her lower legs, the wide trouser hems and the loafers are in frame, in exactly the outfit from the reference.',surface='THE BAG FRONT IS PLAIN MATTE WARM IVORY BOARD, flat, crisp edges, '+BL+'.'),
 sh(3,'hang-tag-on-cuff','print','the hang tag',['hangtag'],'D','A hang tag still pinned to the blazer cuff, hanging against the stone wool.',
  'Very close, 100mm macro, f/5.6, camera square to the tag. The tag hangs on the centre line from its brass pin, filling about 55 percent of the frame height, sharp; the stone wool crepe cuff and sleeve folds fill the frame around it.',
  pl=PLH,surface='THE TAG FACE IS PLAIN THICK WARM IVORY CARD, flat, softly rounded corners, '+BL+'.'),
 sh(4,'tissue-seal-in-open-bag-top-down','print','the seal',['tissue','bag_atelier'],'B','Looking down into our open shopping bag: the folded ivory tissue closed with a round seal.',
  'Directly from above, lens pointing straight down, 80mm, f/5.6. The square opening of the bag frames the tissue bundle; the round seal sits on the centre line, filling about 25 percent of the frame width, sharp; the bag rim and espresso handles at the edges.',
  who=False,surface='THE SEAL FACE IS A PLAIN MATTE ESPRESSO ROUND, flat, crisp edge, '+BL+'.'),
 sh(5,'garment-cover-on-rail','print','the front panel',['gcover'],'A','Our canvas garment cover hanging alone on a slim steel rail in the studio.',
  'Straight on, camera at the front panel, 80mm, f/5.6. The cover hangs on the centre line, front square to the camera, filling about 75 percent of the frame height; the ivory front panel sharp; the oak hanger and steel rail at the top; the backdrop falls to dark.',
  who=False,surface='THE FRONT PANEL IS PLAIN WARM IVORY COTTON, flat and stitched, crisp corners, '+BL+'.'),
 sh(6,'neck-label-inside-collar-macro','print','the neck label',[],'D','The inside of the blazer collar, folded back, showing the woven neck label.',
  'Macro, 120mm, f/5.6, camera square to the label. The small woven label sits on the centre line, filling about 45 percent of the frame width, sharp, stitched at both ends; the stone wool and ivory lining fill the frame in soft folds.',
  pl='Only the folded-back inside of the blazer collar is in frame.',surface='THE LABEL IS PLAIN WOVEN IVORY RIBBON with a fine weave texture, flat, '+BL+'.'),
 sh(7,'invitation-card-against-blazer','print','the invitation card',[],'D','She holds a show invitation card flat against the front of her blazer.',
  'Straight on, close, 80mm, f/5.6, camera square to the card. The card fills about 50 percent of the frame width on the centre line, sharp; her fingers at its edges; the blazer lapel and ivory silk shell soft around it.',
  surface='THE CARD IS PLAIN THICK WARM IVORY COTTON CARD, flat, crisp corners, '+BL+'.'),
 sh(8,'lookbook-under-arm','print','the lookbook cover',[],'D','A slim lookbook tucked under her arm against the blazer, cover facing out.',
  'Straight on, close, 80mm, f/5.6, camera square to the cover. The lookbook cover fills about 55 percent of the frame height on the centre line, sharp; the stone sleeve crosses its top edge; the blazer drape behind.',
  surface='THE COVER IS PLAIN MATTE WARM IVORY board, flat, crisp corners and spine, '+BL+'.'),
 sh(9,'ribbon-tied-on-handles','print','the ribbon',['bag_atelier'],'D','A grosgrain ribbon tied in a flat bow around the espresso handles of our bag.',
  'Very close, 100mm macro, f/5.6, camera square to the ribbon tail. The ribbon tail hangs on the centre line, filling about 45 percent of the frame height, sharp; the handles and the bag cuff soft behind.',
  who=False,surface='THE RIBBON IS PLAIN IVORY GROSGRAIN with its fine ribbed texture, flat, '+BL+'.'),
 sh(10,'phone-in-hand-sleeve-drape','phone','the phone',['phone'],'D','Her phone held loosely at her side, the long blazer sleeve falling over her wrist.',
  'Straight on, close, 80mm, f/4, camera square to the screen. The phone fills about 45 percent of the frame height on the centre line, screen sharp; the sleeve drapes over the back of her hand; the trouser folds behind.',pl=PLH),
 sh(11,'tablet-at-waist-blazer-frame','ipad','the tablet',['ipad'],'C','She holds a tablet at waist height, the open blazer fronts framing it.',
  'Straight on, close, 80mm, f/4, camera square to the screen. The tablet fills about 55 percent of the frame width on the centre line, screen sharp; the two blazer fronts fall either side like a frame; the ivory silk shell behind.'),
 sh(12,'laptop-on-stone-plinth-figure-behind','laptop','the laptop',['laptop'],'A','A laptop open on a pale stone plinth in the studio; she walks past behind, softly out of focus.',
  'Straight on, camera at screen height, 80mm, f/2.8. The laptop sits on the centre line, screen square to the camera, filling about 55 percent of the frame width, sharp; behind it her figure in the stone suit passes as a soft blur, head out of frame.',
  pl='Behind, only her body from the shoulder down passes as a soft blur, in the outfit from the reference; her head is out of frame.'),
]
