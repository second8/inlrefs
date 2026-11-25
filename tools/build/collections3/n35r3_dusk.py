# n35 Nature round 3 (Sam 25 Nov): direction = R1 dusk-jungle display (final). 'works but needs more consistency, not all over the place.'
# R2: laptop on boulder final but 'works, don't do this much more'; iPad bad again; poppies sign too faded; pebbles and stream 'looks ai'.
# One world for the whole set: dark tropical forest at dusk, honey-oak furniture, screen or one warm lamp as the light. No iPad, phone, laptop-on-rock.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n35r1_nature.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
from _nov_common import sh,PRINT,SCREEN
C=dict(r1.C);C['id']='n35r3'
C['register']='A calm, real editorial photograph of a design piece set out in a dark tropical forest at dusk'
C['world']='A dense, real tropical forest at dusk: giant monstera, banana and palm leaves, dark wet trunks, a soft carpet of fallen leaves; simple honey-oak furniture placed in it as a deliberate set; nothing else man-made unless the shot names it.'
C['light']='The last deep blue dusk light falls softly through the canopy; the design surface, or one small warm lamp where the shot names it, is the main light and softly lights the nearest leaves and oak; true soft shadows, never studio light.'
C['palette']='Deep forest greens going to near-black, cool blue dusk in the shadows, warm honey oak, the design surface pure neutral white. The same dusk grade and finish on every image of the collection.'
C['real']=r1.C['real'].replace('never floating.','never floating. Plants grow wild and irregular, never in rows; every object is at its true real-world size.')
LB='THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim oak frame, clearly the brightest thing in the frame, nothing printed on it and nothing crossing it.'
S=[
 sh(1,'display-on-long-oak-desk-under-banana-leaves-dusk','Our display stands on a long honey-oak desk under giant banana leaves in the forest at dusk; its screen is the brightest light in the scene.',
  'Camera a little closer and lower than eye level, at screen height, 50mm lens, f/4, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp; the long desk top runs across the lower frame catching the screen glow; huge banana leaves arch over the top of the frame, dark and softly lit by the screen.',
  SCREEN('THE DISPLAY'),'the screen',refs=['display']),
 sh(2,'freestanding-oak-lightbox-on-forest-floor-dusk','A tall freestanding portrait lightbox in a slim oak frame stands on the leafy forest floor among dark palms at dusk, glowing.',
  'Camera at lightbox height, 85mm lens, f/4, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp; its glow falls softly on the fallen leaves at its base and on the nearest monstera leaves either side; deep dark green and blue dusk behind.',
  LB,'the lightbox'),
 sh(3,'tv-on-low-oak-bench-jungle-clearing-dusk','A large flat television stands on a low honey-oak bench in a small clearing of the forest at dusk; its screen is the brightest light in the scene.',
  'Camera low, at screen height, 50mm lens, f/4, square to the screen. The screen fills about 60 percent of the frame width on the centre line, sharp; the low bench runs across the lower frame; dark palm trunks and leaves surround it, lit softly by the screen; a few soft out-of-focus leaves in the near foreground at the frame edges, never over the screen.',
  SCREEN('THE TELEVISION'),'the screen',aspect='16:9',refs=['display']),
 sh(4,'framed-poster-on-oak-desk-under-warm-lamp-dusk','A large poster in a thin honey-oak frame stands upright on an oak desk in the forest at dusk, lit by one small warm oak desk lamp beside it.',
  'Camera at poster height, 70mm lens, f/4, square to it. The framed poster fills about 50 percent of the frame width on the centre line, sharp; the lamp makes a soft warm pool of light on the poster and desk; dark monstera leaves around, blue dusk in the shadows.',
  PRINT('THE POSTER'),'the poster'),
 sh(5,'open-magazine-on-oak-desk-top-down-lamp-dusk','An open magazine lies flat on a honey-oak desk in the forest at dusk, under the warm light of a small desk lamp just out of frame.',
  'Camera straight down, 50mm lens, f/5.6. The open double spread lies on the centre line with its edges parallel to the frame, filling about 65 percent of the frame width, sharp; a warm soft pool of lamp light on the pages; the tips of dark tropical leaves reach into the frame corners over the oak, never over the pages.',
  'THE OPEN MAGAZINE SPREAD IS PLAIN MATTE PAPER-WHITE on both pages, lying flat with a soft natural curve at the spine and crisp corners, nothing printed on it and nothing crossing it.','the magazine spread',comp='B'),
]
