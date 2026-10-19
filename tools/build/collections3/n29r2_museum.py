# n29 Spatial Awareness round 2 (Sam 19 Oct). r1 all bad: 'the look and feel should be the same for the whole collection, one bright, one snow, one dark = bad';
# 'please look at the figma inspiration, you can just recreate those with prompts'; CRT 'too bland, gaming'; projection 'super ugly'.
# New inspo: Modern Gothic lobby lightbox ('light, environment good, professional'), hall of suspended screens ('how the screens, layout and light').
# So: one look for all (dark museum at night, polished floor, the work as only light), recreate the refs, every face plain white.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n29r_spatial.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
C=dict(r1.C);C['id']='n29r2'
C['register']='Professional documentation photograph of a contemporary art installation in a museum at night'
C['world']='A large contemporary art museum after dark: polished dark stone or concrete floors that reflect the light, dark walls, a dark ceiling; the installation is the only light in the room.'
C['light']="The installation's own glow is the only light: it spills onto the polished floor in long reflections and onto the people near it, then falls off into deep shadow. No other lamps."
C['palette']='Neutral: soft blacks, charcoal, warm grey stone, natural skin; the glowing surfaces are pure neutral white. No green, teal, blue or orange cast. The same grade on every image of the collection.'
C['finish']='Shot on a full-frame camera at ISO 1600 by a professional exhibition photographer: honest dark exposure, fine natural grain, true neutral colour, crisp lines, gentle lens falloff. Quiet, expensive and real, like the press image of a major museum show; never a render.'
C['avoid']=['a face, chin, lips or profile','any image, photo, face, text or colour on any screen or lightbox','logos, letters or brand names anywhere','a green or teal cast','any object not named in the shot','fog or haze','a clean smooth digital look']
s,SIL=r1.s,r1.SIL
WHITE='EVERY SCREEN, LIGHTBOX FACE OR PANEL IN THE ROOM IS PLAIN EVENLY LIT WHITE, glowing bright and clean, never blown out, with crisp edges and corners; nothing on any of them.'
S=[
 s(1,'backlit-wall-panel-dark-museum-lobby',['r29_lobby'],
  'In a dark museum lobby at night a huge backlit wall panel glows above a polished stone floor; one visitor walks past it.',
  'Camera at standing height, straight on, 35mm lens, f/4. The wall panel sits on the centre line, filling about 60 percent of the frame width, its face square to the camera; its light makes a long soft reflection on the polished floor below; a low ceiling with a warm wood soffit crosses the top of the frame; dark glass doors at one side. One visitor walks past at the right edge, small.',
  'THE WALL PANEL FACE IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, clearly the brightest thing in the frame yet not blown out, with crisp corners; nothing on it.','A',SIL,'print','the wall panel'),
 s(2,'hall-of-suspended-screens',['r29_hall'],
  'A long dark museum hall whose ceiling and walls are lined with dozens of flat screens hung on thin wires at different angles; visitors walk through it.',
  'Camera at standing height looking straight down the hall, 24mm lens, f/4. The screens hang in a dense grid across the ceiling and both walls, all glowing; the nearest large screen hangs on the centre line square to the camera, filling about 35 percent of the frame width, sharp; at the far end a bright doorway; visitors walk through as dark silhouettes, small.',
  WHITE,None,SIL,'screen','the screens'),
 s(3,'dark-hall-of-lit-cubes',['r29_cubes'],
  'A dark old industrial hall filled with large wooden cubes stacked at different heights; the faces of the cubes glow as lightboxes; a visitor stands among them.',
  'Camera at chest height, 35mm lens, f/2.8. The nearest cube stands close on the right of centre, its lit face square to the camera, filling about 45 percent of the frame width, sharp; behind it more lit cubes step back into the dark at different heights, softer; one visitor stands in the gap between them as a dark silhouette.',
  WHITE,None,SIL,'print','the lightbox cube faces'),
 s(4,'room-of-translucent-screens-dark-hall',['r29_box'],
  'A room-sized box made of large translucent screens stands in the middle of a dark gallery; light glows through its walls.',
  'Camera at standing height, straight on to the nearest wall of the box, 35mm lens, f/4. The facing translucent screen wall sits on the centre line, square to the camera, filling about 65 percent of the frame width, sharp, glowing evenly; the corner and the next wall turn away at one side; a low grid ceiling with small lights above; the floor dark and polished below.',
  WHITE,'A',None,'screen','the translucent screen wall'),
 s(5,'ring-of-screens-on-truss-benches',[],
  'In a dark museum room a ring of large screens hangs from a black steel truss overhead, facing inward; low wooden benches sit in the circle below.',
  'Camera low from a bench, looking up slightly at one screen of the ring, 35mm lens, f/4. That screen sits on the centre line, square to the camera, filling about 50 percent of the frame width, sharp; the next screens of the ring curve away at both sides, glowing; the black truss and cables above; the tops of two low benches in the dark below.',
  WHITE,None,None,'screen','the screens'),
]
