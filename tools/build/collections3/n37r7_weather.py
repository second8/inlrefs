# n37 Night Square round 7 (Sam 26 Nov): all 10 of R6 final. Pin on rain streaks: 'snowy weather, or rain subtle fits!'. n36 Terminal closed.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r6',os.path.join(os.path.dirname(__file__),'n37r6_ten.py'));r6=importlib.util.module_from_spec(_s);_s.loader.exec_module(r6)
from _nov_common import sh
C=dict(r6.C);C['id']='n37r7'
C['world']=r6.C['world'].replace('wet asphalt and pavements.','wet asphalt and pavements, or a light fresh snowfall where the shot says; the weather is always subtle and real.')
ALL=r6.ALL
SN='Light snow falls softly; a thin fresh layer of snow on the ground and ledges.'
DR='A subtle drizzle; the street glistens.'
S=[
 sh(1,'light-snow-falling-across-giant-tower-screen','Light snow falls across a giant portrait screen on a tower above the square.',
  f'Camera across the street at screen height, 85mm lens, f/4, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; {SN} A few soft flakes catch the white light in front, never hiding the screen.',ALL,'the screens'),
 sh(2,'through-snowy-shop-window-to-giant-screen','From inside a dark closed shop, a giant landscape screen across the street fills the big front window, snow falling outside.',
  f'Camera inside at screen height, 50mm lens, f/4, square to the window. The window frame is a clean dark rectangle around the screen, which fills about 55 percent of the frame width, sharp; a little snow gathered on the outer sill; {SN}',ALL,'the screens'),
 sh(3,'drips-from-our-shelter-roof-to-giant-screen','From under the roof edge of our graphite bus shelter, drops falling from the edge in front, a giant landscape screen across the avenue.',
  f'Camera under the shelter roof at screen height, 50mm lens, f/4, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the dark roof edge runs across the top of the frame with a few soft falling drops; {DR}',ALL,'the screens',aspect='16:9',refs=['shelter']),
 sh(4,'snowy-fire-hydrant-foreground-giant-screen','A snow-capped red fire hydrant on the kerb in the near foreground at one side; a giant landscape screen fills the facade across the street.',
  f'Camera low at the kerb, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the hydrant is a soft red shape at the lower frame edge, never over the screen; {SN}',ALL,'the screens'),
 sh(5,'empty-snow-dusted-bench-plaza-giant-screen','An empty snow-dusted bench at the edge of a small plaza faces a giant landscape screen across the street.',
  f'Camera behind the bench at screen height, 50mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width, sharp; the bench back is a dark line across the lower frame; {SN}',ALL,'the screens',aspect='16:9'),
 sh(6,'high-office-window-snow-giant-screen','From a dark high-floor office, a giant screen on the tower opposite fills the tall window while snow falls outside.',
  f'Camera inside at screen height, 50mm lens, f/4, square to the window. The window frame is a clean dark rectangle around the screen, which fills about 55 percent of the frame width, sharp; soft snowflakes drift past outside; nothing on the glass over the screen.',ALL,'the screens'),
 sh(7,'tram-tracks-drizzle-leading-to-giant-screen','Shining tram tracks run down a quiet street in a light drizzle toward a low building whose upper face is one giant landscape screen.',
  f'Camera low in the middle of the street, 50mm lens, f/5.6, square to the building. The screen fills about 55 percent of the frame width, sharp; the steel rails catch the white light and lead toward it; {DR}',ALL,'the screens',aspect='16:9'),
 sh(8,'snowy-lamppost-two-stacked-screens','A black iron lamppost with snow on its top stands at one side; two giant screens stacked on the facade across the street.',
  f'Camera at the height of the screens, 85mm lens, f/5.6, square to the facade. The two stacked screens together fill about 60 percent of the frame height, sharp; the lamppost is a dark vertical at the frame edge with its warm lamp glowing; {SN}',ALL,'the screens'),
 sh(9,'dark-arched-passage-drizzle-to-giant-screen','From inside a dark arched stone passage, its arch framing the view, a giant portrait screen across the street in a light drizzle.',
  f'Camera inside the passage at screen height, 50mm lens, f/4, square to the far screen. The screen fills about 55 percent of the frame height, sharp, inside the dark arch; the wet paving shines; {DR}',ALL,'the screens'),
 sh(10,'closed-food-cart-snow-giant-screen','A closed steel food cart with its shutter down and snow on its roof stands on the pavement in the foreground; a giant landscape screen across the street.',
  f'Camera at the cart, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the cart roof edge runs along the bottom third; {SN}',ALL,'the screens'),
]
