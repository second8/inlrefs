# n28 Atelier round 3 (Sam 18 Oct): r2 direction better; only 5 images; r2 felt flat, 'almost AI', lens/camera not a creative campaign.
# New inspo: dramatic campaign (huge glowing light ceiling over a dark hall, polished floor reflecting it, figures in motion, low wide lens),
# colours too strong for him: keep the vibe, neutral colours. Marble 'looks cheap': dropped. Devices crossed in r2: none this round.
from builder3 import SQ
C={
 'id':'n28r3','name':'Atelier','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A bold luxury fashion campaign photograph',
 'world':'A vast dark hall used as a fashion set: a huge glowing ceiling of soft white light hangs overhead like a luminous disc, everything outside its pool falls to near black, and a polished dark floor reflects the light in long soft streaks. Only what the shot names is on set.',
 'light':'All the light comes from the huge glowing ceiling overhead: soft, even, neutral white, falling down onto her shoulders and the fabric and spilling onto the polished floor; no fill, deep falloff into darkness at the edges of the pool, shapes carved by top light.',
 'palette':'Neutral, almost monochrome colour: neutral white light, charcoal and deep black space, natural skin, the clothes in their own black, white and ivory; no blue, teal, orange or any colour cast. The design surface is the cleanest white in the frame.',
 'finish':'Shot on 35mm film by a campaign photographer with a wide 24mm to 35mm lens from a bold, low camera position, real depth and perspective, a touch of motion blur on moving fabric only, fine visible grain, deep rich blacks, soft rolled highlights, no halation, no haze. Cinematic, confident, never a catalogue picture.',
 'cast':{'her':'ch13'},
 'real':("Real: this is a product mockup photograph for a fashion campaign, so the design surface is the hero: sharp, large and close to the lens, with the light, the space and the movement around it. "
         "It is a real photograph of a real moment on set, not a render: real heavy fabric in motion, real reflections on the floor, honest exposure. "+SQ+
         " Only the objects named in the shot are on set. The design surface is new and clean, crisp at its edges and corners, without blowing out. No halation or glow spilling over the design surface."),
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','a blue or coloured cast','marble','any object not named in the shot','a stiff, posed or catalogue look'],
}
LOOK={'coat':'look_coat','shirt':'look_shirt','slip':'look_slip','gown':'look_gown'}
NOFACE=' Her face is never visible: she is turned away from the camera or cropped by the frame, and no face, cheek, chin or profile shows.'
def sh(n,slug,refs,moment,shot,look,pl,surface,comp=None):
    d={'n':n,'slug':slug,'kind':'print','noun':'the design surface','refs':list(refs)+['ch13',LOOK[look]],'moment':moment,'shot':shot,
       'people':'line','people_line':pl+NOFACE,'surface':surface}
    if comp: d['comp']=comp
    return d
BL='nothing printed on it'
BAG='THE BAG FRONT IS PLAIN MATTE PAPER-WHITE BOARD, flat with crisp folded edges and a deep folded top cuff, '+BL+'.'
S=[
 sh(1,'walking-into-the-light-bag-on-back',['bag_atelier'],
  'She walks away from the camera into the pool of light under the glowing ceiling, our bag hanging from its handles over her shoulder and resting flat against the back of the long black coat.',
  'Low camera at hip height a few steps behind her, 28mm lens, f/4. The bag front faces the camera square, on the centre line in the lower half of the frame, filling about 40 percent of the frame width, sharp; above and beyond her the huge glowing ceiling fills the top of the frame; the coat hem swings mid-stride; her reflection and the bag\'s stretch down the polished floor.',
  'coat','She is seen from behind, from the back of her head down to her boots, in exactly the outfit from the reference, mid-stride.',BAG),
 sh(2,'bag-swung-out-mid-turn',['bag_atelier'],
  'Mid-turn on the polished floor, the black gown flaring around her, she swings our bag out on her straight arm toward the camera, caught in the moment.',
  'Camera at the height of the bag, close, 35mm lens, f/4. The bag front faces the camera square on the centre line, filling about 50 percent of the frame width, sharp and frozen; behind it her arm in the long black glove, her body twisting away in a strong diagonal, the gown fanning out with a little motion blur; the glowing ceiling light catches the top of her shoulder.',
  'gown','Only her body from the shoulder down is in frame, in exactly the outfit from the reference, twisting away from the camera in a strong diagonal.',BAG),
 sh(3,'garment-cover-under-the-light',['gcover'],
  'Our garment cover hangs alone from one slim black hook in the middle of the dark hall, right under the edge of the glowing ceiling, and she reaches in from the side to the top of the zip.',
  'Low camera, 35mm lens, f/4, square to the front panel. The cover hangs on the centre line, front square to the camera, filling about 60 percent of the frame height, the pale panel sharp; top light rakes down the canvas; her arm in the white shirt dress enters from the side, the deep stiff cuff catching the light; the polished floor below holds a long soft reflection of the cover.',
  'shirt','Only her arm, the deep white cuff and the edge of the sleeve are in frame, in exactly the outfit from the reference.',
  'THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
 sh(4,'hang-tag-arm-reaching-to-lens',['hangtag'],
  'She reaches her arm straight out toward the camera, the long black coat sleeve falling back, our hang tag hanging from the cuff on its cord, the glowing ceiling far behind.',
  'Very close, low camera looking slightly up, 35mm lens, f/4, square to the tag. The tag hangs on the centre line, filling about 45 percent of the frame height, sharp; her hand and the heavy black cuff around it; behind, out of focus, her shoulder turned away and the huge glowing ceiling as a soft white field across the top of the frame.',
  'coat','Only her outstretched arm, hand and coat sleeve are sharp; the rest of her is a soft dark shape turned away behind, in exactly the outfit from the reference.',
  'THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'),
 sh(5,'invitation-held-out-seated-on-floor',[],
  'She sits on the polished floor in the pool of light, leaning back on one hand, legs long, the ivory satin slip pooling, and holds a show invitation card out toward the camera between two fingers.',
  'Camera low at floor level, close, 28mm lens, f/4, square to the card. The card fills about 45 percent of the frame width on the centre line, sharp; her fingers pinch its corner; behind it her arm runs back to her body leaning away in a long diagonal, the satin spilling across the floor and catching the top light, the glowing ceiling soft across the top of the frame.',
  'slip','Only her arm, hand and her body from the collarbone down are in frame, leaning back, in exactly the outfit from the reference.',
  'THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'),
]
