# n37 Night Square round 4 (Sam 25 Nov): all R3 final. Steps 'niceeeeeee', bus blur 'amazing!!!!!!', subway and hotel 'works!', puddle 'not bad'. More motion and frames.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n37r2_allwhite.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
from _nov_common import sh
C=dict(r2.C);C['id']='n37r4'
ALL=r2.ALL
S=[
 sh(1,'billboard-above-yellow-cabs-at-red-light','A giant landscape billboard covers a facade above the street while a row of yellow cabs waits at a red light below it.',
  'Camera across the street at billboard height, 85mm lens, f/5.6, square to it. The billboard fills about 55 percent of the frame width on the centre line, sharp; the cab roofs and their roof lights line the bottom of the frame, a red traffic light at one edge; wet asphalt shine.',ALL,'the screens'),
 sh(2,'through-restaurant-window-to-giant-billboard','Seen from inside a dark upper-floor restaurant, a giant billboard on the tower across the street fills the big window.',
  'Camera inside at the billboard height, 50mm lens, f/4, square to the window. The black window frame is a clean rectangle around the billboard, which fills about 55 percent of the frame width, sharp; the dark empty table edge runs along the bottom; a faint reflection on the glass, never over the screen.',ALL,'the screens'),
 sh(3,'tall-screen-at-end-of-side-street-fire-escapes','A tall portrait screen on a tower closes the end of a narrow side street lined with black iron fire escapes.',
  'Camera in the middle of the side street, 135mm lens, f/5.6, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; the fire escapes frame both sides in dark silhouette; the wet street shines below.',ALL,'the screens'),
 sh(4,'from-our-bus-shelter-across-to-giant-screen','From beside our graphite bus shelter, a giant landscape screen across the avenue; the shelter\'s own tall lightbox panel stands at the frame edge.',
  'Camera at the kerb by the shelter, 50mm lens, f/5.6, square to the far screen. The far screen fills about 50 percent of the frame width, sharp; the shelter\'s lit panel is a crisp white rectangle at one side, square-on too; a cab streaks between them as a soft yellow blur.',ALL,'the screens',aspect='16:9',refs=['shelter']),
 sh(5,'from-footbridge-wall-of-screens-traffic-trails','From a footbridge over a wide avenue, a building face covered in a grid of flat screens stands at the end, red and white traffic trails running toward it.',
  'Camera on the footbridge at the height of the grid middle, 135mm lens, f/5.6, slow shutter, square to the facade. The screen grid fills about 60 percent of the frame width on the centre line, sharp; long light trails fill the lower third; dark towers either side.',ALL,'the screens'),
]
