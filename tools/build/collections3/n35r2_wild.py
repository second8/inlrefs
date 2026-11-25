# n35 Nature round 2 (Sam 25 Nov). R1: dusk-jungle display 'niceeee' (final); lavender sign 'more realistic, flowers too arrayed, wood not realistic and sizing';
# Lite iPad 'bad phone'; leaves top-down 'not bad not good'; easel on dunes 'not good'. Push: devices glowing in real nature, wild irregular plants, true scale.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n35r1_nature.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
from _nov_common import sh,PRINT,SCREEN
C=dict(r1.C);C['id']='n35r2'
C['real']=r1.C['real'].replace('never floating.','never floating. Nature is wild and irregular, plants grow naturally and never in neat planted rows; every object is at its true real-world size.')
S=[
 sh(1,'laptop-open-on-mossy-boulder-rainforest-dusk','Our laptop sits open on a flat, moss-covered boulder deep in a dark rainforest at dusk; its screen is the brightest light in the scene.',
  'Camera at screen height a little above the keyboard, 50mm lens, f/2.8, square to the screen. The screen fills about 50 percent of the frame width on the centre line, sharp; the keyboard is foreshortened and soft; wet ferns and dark leaves surround it, lit softly by the screen and the last deep blue dusk light.',
  SCREEN('THE LAPTOP'),'the screen',aspect='16:9',refs=['laptop','keys']),
 sh(2,'ipad-on-flat-rock-wild-alpine-meadow-golden-hour','Our iPad stands upright in a slim black stand on a flat grey rock in a wild alpine meadow at golden hour, scattered wild flowers growing unevenly around it.',
  'Camera low at screen height, 85mm lens, f/2.8, square to the screen. The screen fills about 45 percent of the frame width on the centre line, sharp; uneven tufts of grass and a few wild flowers soft in the foreground; distant mountain slopes in warm soft focus behind.',
  SCREEN('THE IPAD'),'the screen',comp=None,refs=['ipad']),
 sh(3,'sign-panel-on-steel-post-among-wild-poppies','A plain white sign panel, about sixty by ninety centimetres, is bolted to a single weathered galvanised steel post standing among wild red poppies and tall grass at the edge of a field.',
  'Camera at panel height, 85mm lens, f/5.6, square to it. The panel fills about 45 percent of the frame width on the centre line, sharp; the poppies and grass grow wild and uneven around the post, soft in front; a soft summer sky behind.',
  PRINT('THE SIGN PANEL'),'the sign panel'),
 sh(4,'print-flat-on-black-volcanic-pebbles-top-down','A large print lies flat on a beach of smooth black volcanic pebbles.',
  'Camera straight down, 50mm lens, f/5.6. The print lies on the centre line with its edges parallel to the frame, filling about 60 percent of the frame width, sharp and perfectly flat; the round black pebbles fill the rest of the frame with soft highlights; bright overcast light.',
  PRINT('THE PRINT'),'the print',comp='B'),
 sh(5,'phone-on-sunlit-rock-by-turquoise-mountain-stream-top-down','Our phone lies face up on a flat, sun-warmed rock beside a clear turquoise mountain stream.',
  'Camera straight down, 50mm lens, f/5.6. The phone lies on the centre line with its edges parallel to the frame, filling about 40 percent of the frame width, sharp; the clear turquoise water and smooth stream stones fill one side; hard summer sun gives the phone a crisp soft-edged shadow.',
  SCREEN('THE PHONE'),'the screen',comp='B',refs=['phone']),
]
