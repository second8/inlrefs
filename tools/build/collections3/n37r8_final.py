# n37 Night Square round 8, last (Sam 26 Nov: '10 more and we done with this too'). R7 finals 01,02,05,06,07,08,09; shelter drips 'toooooo much'; hydrant and food cart not picked.
# No foreground props; subtle weather only.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r7',os.path.join(os.path.dirname(__file__),'n37r7_weather.py'));r7=importlib.util.module_from_spec(_s);_s.loader.exec_module(r7)
from _nov_common import sh
C=dict(r7.C);C['id']='n37r8'
ALL=r7.ALL
SN='light snow falls softly; a thin fresh layer of snow on the ground and ledges.'
DR='a subtle drizzle; the street glistens.'
S=[
 sh(1,'fresh-tyre-tracks-snowy-avenue-giant-screen','Fresh tyre tracks run through a thin layer of new snow down an empty avenue toward a low building whose upper face is one giant landscape screen.',
  f'Camera low in the middle of the avenue, 50mm lens, f/5.6, square to the building. The screen fills about 55 percent of the frame width, sharp; the dark tyre tracks lead toward it; {SN}',ALL,'the screens',aspect='16:9'),
 sh(2,'stone-colonnade-drizzle-to-giant-screen','From inside a dark stone colonnade, two columns framing the view, a giant portrait screen on the tower across the street in a light drizzle.',
  f'Camera between the columns at screen height, 50mm lens, f/4, square to the far screen. The screen fills about 55 percent of the frame height, sharp; the dark columns frame both sides; {DR}',ALL,'the screens'),
 sh(3,'waterfront-screen-mirrored-in-still-river','A giant landscape screen on a waterfront building across a calm river, mirrored in the still dark water below it.',
  f'Camera on the opposite bank at screen height, 85mm lens, f/5.6, square to the building. The screen fills about 50 percent of the frame width in the upper half, sharp; its reflection lies softly in the water below and fades at its edges; {SN}',ALL,'the screens',aspect='16:9'),
 sh(4,'giant-screen-above-department-store-glass-doors','A giant landscape screen covers the facade above the tall glass entrance doors of a closed department store.',
  'Camera across the street at screen height, 70mm lens, f/5.6, square to the facade. The screen fills about 60 percent of the frame width on the centre line, sharp; the dark glass doors below with a soft warm glow inside; wet pavement shine.',ALL,'the screens'),
 sh(5,'long-lens-screen-between-dark-towers-snow','A giant portrait screen on a tower, seen tight between the dark edges of two nearer towers through a long lens in light snow.',
  f'Camera far down the street, 200mm lens, f/5.6, square to the screen. The screen fills about 65 percent of the frame height on the centre line, sharp; the two dark tower edges frame it close on both sides; {SN}',ALL,'the screens'),
 sh(6,'through-open-doors-dark-train-car-to-screen','From inside a dark empty elevated train car, its open sliding doors frame a giant portrait screen across the street.',
  'Camera inside at screen height, 35mm lens, f/4, square to the doorway and the far screen. The door opening is a clean dark rectangle around the screen, which fills about 55 percent of the frame height, sharp; the platform edge runs across the bottom.',ALL,'the screens'),
 sh(7,'empty-ice-rink-below-giant-screen-snow','An empty outdoor ice rink lies below a giant landscape screen on the tower beyond, the smooth ice mirroring the white light.',
  f'Camera at the rink edge at the height of the screen middle, 85mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width, sharp; the ice is a soft white reflection across the lower third; {SN}',ALL,'the screens',aspect='16:9'),
 sh(8,'shuttered-shops-below-giant-screen-drizzle','A row of closed shops with dark rolling shutters runs along the ground floor below one giant landscape screen.',
  f'Camera across the street at screen height, 50mm lens, f/5.6, square to the facade. The screen fills about 60 percent of the frame width, sharp; the dark shutters make a clean band below it; {DR}',ALL,'the screens',aspect='16:9'),
 sh(9,'snowy-balcony-railing-to-giant-screen','From a dark balcony with fresh snow on its plain steel railing, a giant landscape screen on the tower opposite at balcony height.',
  f'Camera on the balcony at screen height, 50mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width, sharp; the snowy railing runs across the bottom of the frame; {SN}',ALL,'the screens'),
 sh(10,'station-canopy-edge-drizzle-to-giant-screen','From under the steel and glass canopy of a station entrance, its edge framing the top of the view, a giant portrait screen across the street.',
  f'Camera under the canopy at street level, 50mm lens, f/5.6, aimed so the far screen stays square. The screen fills about 55 percent of the frame height, sharp; the canopy edge is a clean dark band along the top; {DR}',ALL,'the screens'),
]
