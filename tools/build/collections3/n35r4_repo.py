# n35 Nature round 4 (Sam 25 Nov): R3 display on long desk 'good' (final); lightbox X 'not as artistic, realistic'; TV, framed poster, magazine 'bad'.
# Sam: 'please use objects from the git repo, don't use new tables etc... always. be consistent.' So every object is a repo ref: oak bench, travertine plinth, devices.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n35r3_dusk.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
from _nov_common import sh,SCREEN
C=dict(r3.C);C['id']='n35r4'
C['world']='A dense, real tropical forest at dusk: giant monstera, banana and palm leaves, dark wet trunks, a soft carpet of fallen leaves; only our own objects from the references are placed in it as a deliberate set; nothing else man-made.'
C['light']='The last deep blue dusk light falls softly through the canopy; the glowing screen is the main light and softly lights the nearest leaves and the object it stands on; true soft shadows, never studio light.'
S=[
 sh(1,'display-on-our-oak-bench-monstera-dusk','Our display stands on our honey-oak bench among giant monstera leaves in the forest at dusk; its screen is the brightest light in the scene.',
  'Camera at screen height, 50mm lens, f/4, square to the screen. The screen fills about 50 percent of the frame width on the centre line, sharp; the bench top and its chamfered legs stand on the leafy ground below; giant monstera leaves either side, lit softly by the screen.',
  SCREEN('THE DISPLAY'),'the screen',aspect='16:9',refs=['display','bench_oak']),
 sh(2,'laptop-open-on-our-oak-bench-palms-dusk','Our laptop sits open on our honey-oak bench among dark palms in the forest at dusk; its screen is the brightest light in the scene.',
  'Camera at screen height a little above the keyboard, 50mm lens, f/2.8, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp; the keyboard is foreshortened and soft; the bench edge runs across the lower frame; palm fronds frame the edges, lit softly by the screen.',
  SCREEN('THE LAPTOP'),'the screen',refs=['laptop','keys','bench_oak']),
 sh(3,'display-on-our-travertine-plinth-banana-leaves-dusk','Our display stands on our travertine plinth among banana leaves in the forest at dusk; its screen is the brightest light in the scene.',
  'Camera at screen height, 70mm lens, f/4, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp; the honed travertine block below catches the screen glow; dark banana leaves arch behind and either side.',
  SCREEN('THE DISPLAY'),'the screen',refs=['display','plinth_trav']),
 sh(4,'our-grey-crt-on-oak-bench-fern-dusk','Our warm grey CRT monitor sits on our honey-oak bench among ferns and monstera in the forest at dusk; its curved screen glows white, the brightest light in the scene.',
  'Camera at screen height, 50mm lens, f/4, square to the screen. The screen fills about 45 percent of the frame width on the centre line, sharp; the bench top below; ferns and monstera close around, lit softly by the screen.',
  SCREEN('THE CRT SCREEN'),'the screen',refs=['crt','bench_oak']),
 sh(5,'our-lilac-tv-on-travertine-plinth-dusk','Our lilac enamel portable TV sits on our travertine plinth among palms in the forest at dusk; its screen glows white, the brightest light in the scene.',
  'Camera at screen height, 70mm lens, f/4, square to the screen. The TV fills about 45 percent of the frame width on the centre line, sharp, its lilac enamel the one soft colour against the deep greens; the travertine block below; dark palms behind.',
  SCREEN('THE TV SCREEN'),'the screen',refs=['tv_lilac','plinth_trav']),
]
