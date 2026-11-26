# n36 Terminal round 6 (Sam 26 Nov): R5 finals 03-09 (metro column, spa, revolving door, train carriage, arrival doors, jet lounge, tiled tunnel end).
# Not picked: brass lift, concert foyer, walnut concierge. Pin on metro column: 'stuff like this, not exact this one, but not over the top and unusual objects or materials.'
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r5',os.path.join(os.path.dirname(__file__),'n36r5_ten.py'));r5=importlib.util.module_from_spec(_s);_s.loader.exec_module(r5)
from _nov_common import sh,SCREEN
C=dict(r5.C);C['id']='n36r6'
C['real']=r5.C['real']+' Ordinary real public-building materials only: tile, terrazzo, pale stone, glass and brushed steel; nothing unusual, luxurious or over the top.'
LB=r5.LB
S=[
 sh(1,'portrait-lightbox-on-terrazzo-pillar-departure-gate','A portrait backlit lightbox is mounted on a pale terrazzo-clad pillar in an airport departure gate area.',
  'Camera at lightbox height, 70mm lens, f/5.6, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp, with its real aluminium frame and depth; rows of gate seats soft behind; tall glass and daylight beyond.',LB,'the lightbox'),
 sh(2,'landscape-lightbox-station-underpass-stairs','A large landscape backlit lightbox is set into the white-tiled wall of a clean station underpass, a flight of stairs rising at one side.',
  'Camera across the underpass at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 50 percent of the frame width, sharp; the tile grid runs parallel to its edges; the stairs and handrail at the frame edge; glossy floor with a soft fading reflection.',LB,'the lightbox',aspect='16:9'),
 sh(3,'portrait-screen-on-stone-pillar-mall-atrium','A portrait digital screen is mounted on a pale stone pillar in a bright shopping centre atrium with a glass roof.',
  'Camera at screen height, 70mm lens, f/5.6, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; the atrium balconies soft behind; polished stone floor with a soft reflection.',SCREEN('THE SCREEN'),'the screen'),
 sh(4,'landscape-screen-above-metro-escalators','A large landscape screen hangs on the end wall above a pair of long escalators in a modern metro station.',
  'Camera on the upper concourse at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 50 percent of the frame width on the centre line, sharp; the escalator handrails descend below it; brushed steel and pale tile.',SCREEN('THE SCREEN'),'the screen',aspect='16:9'),
 sh(5,'portrait-lightbox-end-of-moving-walkway','A portrait backlit lightbox stands on the end wall where a moving walkway finishes in a bright airport corridor with glass walls.',
  'Camera on the walkway at lightbox height, 50mm lens, f/5.6, square to the end wall. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the black walkway handrails converge toward it; daylight through the glass.',LB,'the lightbox'),
 sh(6,'lightbox-on-tiled-wall-beside-ticket-gates','A large landscape backlit lightbox is set into a grey-tiled wall just behind a line of glass ticket gates in a metro station.',
  'Camera at lightbox height behind the gates, 50mm lens, f/5.6, square to the wall. The lightbox fills about 50 percent of the frame width, sharp; the glass gate paddles are soft in the lower foreground, never over it.',LB,'the lightbox',aspect='16:9'),
 sh(7,'portrait-screen-on-column-baggage-reclaim','A portrait digital screen is mounted on a pale column in a quiet airport baggage reclaim hall.',
  'Camera at screen height, 70mm lens, f/5.6, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; an empty carousel soft behind; polished floor with a soft reflection.',SCREEN('THE SCREEN'),'the screen'),
 sh(8,'landscape-lightbox-ferry-terminal-sea-windows','A large landscape backlit lightbox is set into a pale stone wall in a calm ferry terminal waiting hall, tall windows onto the sea beside it.',
  'Camera across the hall at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 50 percent of the frame width, sharp; the sea and sky soft through the glass at one side; terrazzo floor with a soft reflection.',LB,'the lightbox',aspect='16:9'),
 sh(9,'portrait-lightbox-station-lift-lobby-steel-doors','A portrait backlit lightbox is mounted between two brushed steel lift doors in a clean train station lift lobby with white tiles.',
  'Camera at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 55 percent of the frame height on the centre line, sharp; the steel lift doors frame it either side; glossy floor with a soft fading reflection.',LB,'the lightbox'),
 sh(10,'portrait-lightbox-end-wall-glass-skywalk','A portrait backlit lightbox closes the end wall of a bright glass skywalk between two terminal buildings.',
  'Camera in the middle of the skywalk at lightbox height, 50mm lens, f/5.6, square to the end wall. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the glass walls and floor lines converge toward it; soft daylight.',LB,'the lightbox'),
]
