# n36 Terminal round 4 (Sam 25 Nov): R3 works = hotel travertine reception, white-tiled tunnel lightbox ('good'), concert foyer lightbox; bad = totem at check-in, marble lounge bar.
# Use repo objects where they fit (wall display, gallery lightbox, oak bench).
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n36r3_more.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
from _nov_common import sh,SCREEN
C=dict(r3.C);C['id']='n36r4'
LB=r3.LB
GL='THE LIGHTBOX IS PLAIN EVENLY LIT OPAL WHITE, flat edge to edge with crisp corners inside its slim matte black frame, nothing printed on it and nothing crossing it.'
S=[
 sh(1,'lightbox-across-the-tracks-white-tiled-metro','A large landscape backlit lightbox is set into the curved white-tiled wall across the tracks in a clean modern metro station.',
  'Camera on the near platform edge at lightbox height, 50mm lens, f/5.6, square to the far wall. The lightbox fills about 55 percent of the frame width on the centre line, sharp; the tile grid runs parallel to its edges; the empty track bed is a dark band along the bottom of the frame; a soft line of light along the vault.',
  LB,'the lightbox',aspect='16:9'),
 sh(2,'screen-between-brass-lift-doors-hotel-lobby','Our wall display hangs on a pale limestone wall between two brushed brass lift doors in a calm hotel lift lobby.',
  'Camera at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 45 percent of the frame width on the centre line, sharp; the two closed brass lift doors frame it either side; polished stone floor with a soft fading reflection.',
  SCREEN('THE WALL DISPLAY'),'the screen',refs=['pr01']),
 sh(3,'our-gallery-lightbox-with-our-oak-bench-museum','Our tall freestanding gallery lightbox stands in a quiet museum gallery with pale walls, our honey-oak bench in front of it.',
  'Camera at lightbox height, 70mm lens, f/5.6, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the bench runs across the lower frame in front; pale oak floor with a soft reflection; soft skylight from above.',
  GL,'the lightbox',refs=['gal_lightbox','bench_oak']),
 sh(4,'wall-display-library-atrium-oak-shelves','Our wall display hangs on a pale stone pier between tall oak bookshelves in the bright atrium of a modern public library.',
  'Camera at screen height, 50mm lens, f/5.6, square to the pier. The screen fills about 50 percent of the frame width on the centre line, sharp; the oak shelves rise either side, softly out of focus; daylight from a glass roof.',
  SCREEN('THE WALL DISPLAY'),'the screen',aspect='16:9',refs=['pr01']),
 sh(5,'lightbox-at-end-of-glass-jet-bridge','A large portrait backlit lightbox is set into the end wall of a glass-walled jet bridge leading to an aircraft door.',
  'Camera in the middle of the jet bridge at lightbox height, 50mm lens, f/5.6, square to the end wall. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the glass walls and ribbed floor converge toward it; soft daylight and a blurred apron outside the glass.',
  LB,'the lightbox'),
]
