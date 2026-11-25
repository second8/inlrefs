# n36 Terminal round 3 (Sam 25 Nov): R2 all final, 'good work, do more'. Same look, 5 new enclosed polished public places.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n36r1_terminal.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
from _nov_common import sh,PRINT,SCREEN
C=dict(r1.C);C['id']='n36r3'
LB='THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim steel frame, nothing printed on it and nothing crossing it.'
S=[
 sh(1,'landscape-screen-above-travertine-hotel-reception','A large landscape screen is set into a warm travertine wall above a long travertine reception desk in a calm luxury hotel lobby.',
  'Camera across the lobby at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 50 percent of the frame width on the centre line, sharp; the reception desk runs across the lower frame, empty and spotless; soft daylight from the side; the polished stone floor reflects it softly.',
  SCREEN('THE SCREEN'),'the screen',aspect='16:9'),
 sh(2,'lightbox-in-white-tiled-pedestrian-tunnel','A large landscape backlit lightbox is set into the curved white-tiled wall of a clean, modern underground pedestrian tunnel.',
  'Camera across the tunnel at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 55 percent of the frame width on the centre line, sharp; the tile grid runs parallel to its edges; a soft line of ceiling light runs along the top; glossy floor with a soft fading reflection.',
  LB,'the lightbox',people='One traveller walks past at the frame edge, softly motion-blurred, at normal size, never in front of the lightbox; no face shows.'),
 sh(3,'portrait-totem-end-of-check-in-desks-terminal','A tall portrait digital totem stands at the end of a row of empty check-in desks in a bright, airy airport departures hall.',
  'Camera at totem height, 85mm lens, f/5.6, square to it. The totem fills about 60 percent of the frame height on the centre line, sharp; the pale check-in desks run off softly to one side; tall glass and a light steel roof behind, out of focus.',
  SCREEN('THE TOTEM SCREEN'),'the screen'),
 sh(4,'screen-behind-marble-bar-airport-lounge','A large landscape screen is mounted on a dark walnut-panelled wall behind a long white marble bar counter in a quiet premium airport lounge.',
  'Camera on the guest side of the bar at screen height, 50mm lens, f/4, square to the wall. The screen fills about 50 percent of the frame width on the centre line, sharp; the marble counter runs across the lower frame with two clean empty glasses at one end; soft warm ceiling light.',
  SCREEN('THE SCREEN'),'the screen',aspect='16:9'),
 sh(5,'freestanding-lightbox-concert-hall-foyer-oak-wall','A tall freestanding portrait lightbox stands in the foyer of a modern concert hall in front of a sweeping curved wall of vertical oak slats.',
  'Camera at lightbox height, 70mm lens, f/5.6, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the warm oak slats curve away behind it; pale stone floor with a soft reflection; soft evening light.',
  LB,'the lightbox'),
]
