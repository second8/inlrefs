# n36 Terminal round 2 (Sam 25 Nov): all 5 of R1 final ('good', 'nice'). Same look, 5 new enclosed polished public spaces, no repeats.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n36r1_terminal.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
from _nov_common import sh,PRINT,SCREEN
C=dict(r1.C);C['id']='n36r2'
SIT=r1.SIT
LB='THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim steel frame, nothing printed on it and nothing crossing it.'
S=[
 sh(1,'landscape-screen-above-baggage-carousel-arrivals','A large landscape screen hangs above an empty, slowly moving baggage carousel in a bright airport arrivals hall.',
  'Camera at screen height across the carousel, 50mm lens, f/5.6, square to the screen. The screen fills about 50 percent of the frame width on the centre line, sharp; the steel carousel curves across the lower part of the frame; polished floor reflecting it softly.',
  SCREEN('THE SCREEN'),'the screen',people=SIT,aspect='16:9'),
 sh(2,'digital-screen-pale-stone-wall-station-hall-benches','A large landscape digital screen is set into the pale stone wall of a grand railway station hall, above a row of long oak benches, soft light from tall windows.',
  'Camera at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 50 percent of the frame width on the centre line, sharp; the benches run below it; a soft shaft of window light falls across the stone beside it, never over it.',
  SCREEN('THE SCREEN'),'the screen',people='One or two travellers sit on the benches, seen from behind at normal size; no face shows.',aspect='16:9'),
 sh(3,'portrait-lightbox-between-platform-glass-doors','A portrait backlit lightbox stands between two sets of glass platform screen doors on a modern underground platform while a train glides past behind the glass.',
  'Camera on the platform at lightbox height, 50mm lens, f/5.6, slow shutter, square to it. The lightbox fills about 60 percent of the frame height on the centre line, dead sharp; the passing train behind the glass doors is a soft horizontal blur; glossy floor.',
  LB,'the lightbox'),
 sh(4,'freestanding-lightbox-end-of-white-museum-corridor','A tall freestanding portrait lightbox stands at the far end of a long white museum corridor with a polished terrazzo floor.',
  'Camera in the middle of the corridor at lightbox height, 85mm lens, f/5.6, square to it. The lightbox fills about 55 percent of the frame height on the centre line, sharp; the corridor walls and ceiling lines converge symmetrically toward it; the terrazzo mirrors it softly.',
  LB,'the lightbox',comp='A'),
 sh(5,'banner-hanging-in-glass-atrium-from-mezzanine','A large banner hangs from the steel roof of a tall glass atrium in a convention centre, seen from the mezzanine at its height.',
  'Camera on the mezzanine at banner height, 70mm lens, f/8, square to the banner. The banner fills about 50 percent of the frame width on the centre line, sharp, taut on its rods; the glass roof grid and soft daylight behind; the atrium floor far below out of frame.',
  'THE BANNER IS PLAIN MATTE WHITE FABRIC, pulled flat and taut on its rods with crisp edges, nothing printed on it and nothing crossing it.','the banner'),
]
