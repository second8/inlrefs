# n29 Spatial Awareness round 4 (Sam 19 Oct): r3 'ugly' (generic museum lobbies, no art installation). 'You ruined this collection... it has nothing to do
# with an art installation. Follow the rules and stay on track.' r2-01 was the one ('looks really good') but it copied Figma 191:1327.
# So: ONE space and light for all, the r2-01 hall described in words; each shot a different installation from his Figma moodboard (194:1373).
# HARD RULE: no inspo images as refs. Words only.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n29r2_museum.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
C=dict(r2.C);C['id']='n29r4'
C['register']='Documentation photograph of an art installation in a museum exhibition hall at night'
C['world']=('One and the same exhibition hall in every image: a low, dim entrance hall of a museum with smooth cream plaster walls, a continuous warm amber band of hidden light '
            'along the ceiling soffit, tall dark wood-framed glass doors at one side, and a polished brown-grey stone floor that carries long soft reflections.')
C['light']='The installation glows as the main light; the warm amber ceiling band gives a low warm glow at the top of the frame; everything else is dim, with soft shadow and long reflections on the polished floor.'
C['palette']='Warm and dim: warm amber and peach at the ceiling band, cream plaster in shadow, warm brown-grey stone, soft blacks; every glowing face is pure neutral white. The same grade on every image of the collection.'
C['avoid']=['a face, chin, lips or profile','any image, photo, face, text or colour on any screen or lightbox','logos, letters or brand names anywhere','a blue, green or teal cast','any object not named in the shot','fog or haze','a clean smooth digital look']
s,SIL,WHITE=r2.s,r2.SIL,r2.WHITE
S=[
 s(1,'backlit-wall-hall-new-angle',[],
  'A huge backlit wall panel, the size of the whole end wall, glows in the dim exhibition hall; one visitor stands before it.',
  'Camera low, close to the polished floor, 35mm lens, f/4, square to the panel. The glowing panel fills about 70 percent of the frame width; its long reflection runs across the polished floor toward the lens; the warm amber ceiling band crosses the top of the frame; the dark wood-framed glass doors at the left edge; one visitor stands small at its foot.',
  'THE WALL PANEL FACE IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, clearly the brightest thing in the frame yet not blown out, with crisp corners; nothing on it.','A',SIL,'print','the wall panel'),
 s(2,'stack-of-grey-crts-one-white-image',['crt'],
  'In the dim exhibition hall a sculpture of old grey CRT monitors is stacked like a wall, three high, every monitor showing the same plain white image.',
  'Camera at chest height, 50mm lens, f/4, square to the stack. The largest monitor sits at the centre of the stack, its screen filling about 30 percent of the frame width, sharp; the other monitors around it glow the same white, their grey plastic bodies and cables between them; their light falls on the polished floor; the warm amber ceiling band above.',
  WHITE,'A',None,'screen','the monitors'),
 s(3,'lit-wooden-cubes-grouped-on-floor',[],
  'In the dim exhibition hall a group of plain pale-oak cubes of different heights stands on the floor, each with one face lit as a lightbox; a visitor walks between them.',
  'Camera at chest height, 35mm lens, f/2.8. The nearest cube stands close on the centre line, its lit face square to the camera, filling about 45 percent of the frame width, sharp; the oak cubes are clean and well made, about knee to shoulder height, at true scale to the visitor; the other cubes glow softer behind it; the warm ceiling band at the top; one visitor as a silhouette.',
  WHITE,None,SIL,'print','the lightbox cube faces'),
 s(4,'translucent-screen-room-box',[],
  'In the dim exhibition hall stands a room-sized box made of large translucent screen walls in slim dark frames, glowing from inside.',
  'Camera at standing height, 35mm lens, f/4, square to the nearest wall of the box. That translucent wall fills about 65 percent of the frame width on the centre line, sharp, glowing evenly; the next wall turns away at the right side; the polished floor reflects it; the warm amber ceiling band above.',
  WHITE,'A',None,'screen','the translucent screen wall'),
 s(5,'large-screen-hanging-on-wires',[],
  'In the middle of the dim exhibition hall one large flat screen hangs in the air on four thin steel wires, glowing; a visitor stands beneath it looking up.',
  'Camera at standing height, 50mm lens, f/4, square to the screen. The screen hangs on the centre line, filling about 55 percent of the frame width, sharp, its wires running straight up out of the frame; its light falls on the polished floor below; the warm amber ceiling band behind it; one visitor small beneath it.',
  WHITE,'A',SIL,'screen','the hanging screen'),
]
