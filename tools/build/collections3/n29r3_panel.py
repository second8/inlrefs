# n29 Spatial Awareness round 3 (Sam 19 Oct): r2-01 'looks really good' (but it copied the Figma image: never pass inspo images, words only).
# 'The direction needs to be like the first one, same for all, just light however is needed.' r2-03 cubes: materials and scale bad; 02, 04, 05 bad.
# So: large backlit wall panel in a museum at night, described in words, five different spaces in one look. No image refs.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n29r2_museum.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
C=dict(r2.C);C['id']='n29r3'
C['register']='Professional photograph of a large backlit wall panel installed in a contemporary museum at night'
C['world']=('A contemporary museum after dark: polished pale grey stone floors that mirror the light, smooth plaster walls, warm honey-oak timber soffits and ceilings, dark glass; '
            'calm, expensive, minimal architecture.')
C['light']='The panel glows as the main light, spilling soft light across the polished floor in a long reflection; the rest of the space is lit only as much as the shot needs, by a few soft warm architectural downlights, and falls into deep shadow.'
C['palette']='Warm neutral: soft blacks, warm grey stone, honey oak, natural skin; the panel face is pure neutral white. No green, teal or blue cast. The same grade on every image of the collection.'
s,SIL=r2.s,r2.SIL
P='THE PANEL FACE IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, clearly the brightest thing in the frame yet not blown out, with crisp corners inside its slim frame; nothing on it and nothing crossing it.'
S=[
 s(1,'panel-end-of-long-corridor',[],
  'A large backlit wall panel closes the far end of a long, dark museum corridor at night.',
  'Camera at standing height on the centre line of the corridor, 50mm lens, f/4. The panel fills about 55 percent of the frame width at the end of the corridor, square to the camera; the polished floor carries its reflection toward the lens in a long bright path; the honey-oak ceiling and the plaster walls converge toward it and fall into shadow; one visitor stands small before it.',
  P,'A',SIL,'print','the wall panel'),
 s(2,'panel-beside-wide-stone-staircase',[],
  'A tall backlit wall panel rises beside a wide stone staircase in a museum atrium at night; a visitor walks up the stairs.',
  'Camera at standing height, straight on to the panel, 35mm lens, f/4. The panel fills the right 55 percent of the frame, square to the camera; the broad pale stone stairs climb on the left side, their edges catching its light; one visitor on the stairs as a small dark silhouette; the polished landing reflects the panel below.',
  P,None,SIL,'print','the wall panel'),
 s(3,'two-storey-atrium-panel-mezzanine-rail',[],
  'A two-storey backlit wall panel fills one wall of a museum atrium at night, seen from the mezzanine.',
  'Camera on the mezzanine at the height of the middle of the panel, 35mm lens, f/4, square to it. The panel fills about 65 percent of the frame width; a slim dark steel railing with an oak handrail runs straight across the lower part of the frame in the foreground; below it the polished atrium floor reflects the panel.',
  P,'C',None,'print','the wall panel'),
 s(4,'panel-low-gallery-oak-bench-seated-visitor',[],
  'In a low, wide museum gallery at night a large backlit wall panel glows above a long oak bench; one visitor sits on it looking at the panel.',
  'Camera at seated eye height from behind the bench, 35mm lens, f/2.8, square to the panel. The panel fills about 60 percent of the frame width on the centre line; the long honey-oak bench runs across the lower third; the seated visitor at one end is a dark silhouette from behind, small, no face; the low oak ceiling crosses the top of the frame.',
  P,'A',SIL,'print','the wall panel'),
 s(5,'panel-through-glass-entrance-wet-plaza',[],
  'From the dark plaza outside a museum at night, a large backlit wall panel glows in the lobby, seen through the tall glass entrance doors.',
  'Camera outside at standing height, straight on, 50mm lens, f/2.8. The tall dark-framed glass doors divide the frame into clean vertical bays; through the wide central bay the panel fills about 50 percent of the frame width, square to the camera, sharp; the wet stone paving outside reflects it; the warm oak soffit of the lobby is visible above it.',
  'THE PANEL FACE, SEEN THROUGH THE CLEAR GLASS, IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, clearly the brightest thing in the frame yet not blown out, with crisp corners; nothing on it, and no reflection or door frame crossing it.','C',None,'print','the wall panel'),
]
