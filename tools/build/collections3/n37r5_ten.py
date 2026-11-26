# n37 Night Square round 5 (Sam 26 Nov): 10 more. R4: bus shelter 'man!!! dope', cabs at red light 'nice, but taxis arrayed not natural', footbridge grid 'screens so small, so thin, not realistic'.
# Rules: every screen big (no thin strips), traffic natural and uneven, frames and motion.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n37r2_allwhite.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
from _nov_common import sh
C=dict(r2.C);C['id']='n37r5'
C['real']=r2.C['real']+' Every screen is big and generous, a full billboard, never a thin strip or a small sliver. Traffic moves naturally at uneven spacing, never lined up in neat rows.'
ALL=r2.ALL
S=[
 sh(1,'through-rainy-glass-of-our-bus-shelter','From inside our graphite bus shelter, a giant landscape screen across the avenue is seen through the shelter\'s rain-dotted glass wall.',
  'Camera inside the shelter at screen height, 50mm lens, f/4, square to the glass and the far screen. The screen fills about 55 percent of the frame width, sharp through the glass; fine raindrops on the glass are soft in the foreground; the shelter\'s dark frame edges the sides of the photo.',ALL,'the screens',refs=['shelter']),
 sh(2,'through-cab-windscreen-at-red-light','From the back seat of a cab stopped at a red light, a giant landscape screen fills the view through the windscreen.',
  'Camera behind the front seats at screen height, 35mm lens, f/4, square to the far screen. The screen fills about 50 percent of the frame width through the windscreen, sharp; the dark dashboard edge and the rear-view mirror silhouette frame the bottom and top; a red light glows at one side.',ALL,'the screens',aspect='16:9'),
 sh(3,'tour-bus-blur-under-huge-portrait-screen','A huge portrait screen climbs the face of a tower above the street while an open-top tour bus passes below as a long blur.',
  'Camera across the street at screen height, 70mm lens, f/5.6, slow shutter, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; the bus is a long soft red blur along the bottom, never over the screen; wet asphalt shine.',ALL,'the screens'),
 sh(4,'from-elevated-train-platform-across-to-screen','From an elevated train platform, a giant landscape screen on the building across the street sits at platform height.',
  'Camera on the empty platform, 85mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp; the dark platform railing runs across the bottom of the frame; the steel canopy edge runs across the top.',ALL,'the screens',aspect='16:9'),
 sh(5,'crosswalk-stripes-to-giant-screen-low-building','Wet crosswalk stripes lead across an empty junction to a low building whose whole upper face is one giant landscape screen.',
  'Camera low at the kerb, 35mm lens, f/8, square to the building. The screen fills about 60 percent of the frame width, sharp; the white crosswalk stripes run toward it in the lower third and mirror the white light.',ALL,'the screens',aspect='16:9'),
 sh(6,'under-marquee-edge-across-to-giant-screen','From under the edge of a theatre marquee, its warm bulbs running along the top of the frame, a giant screen across the square.',
  'Camera under the canopy edge at street level, 50mm lens, f/4, aimed so the far screen stays square. The screen fills about 55 percent of the frame width, sharp; the row of warm bulbs is a soft band along the top edge; the wet street below.',ALL,'the screens'),
 sh(7,'through-high-hotel-window-sheer-curtains','From a dark high-floor hotel room, a giant screen on the tower opposite fills the tall window between sheer curtains.',
  'Camera inside at screen height, 50mm lens, f/4, square to the window. The window frame is a clean dark rectangle around the screen, which fills about 55 percent of the frame width, sharp; soft sheer curtains hang at both sides; nothing on the glass over the screen.',ALL,'the screens'),
 sh(8,'framed-by-scaffolding-shed-beams','From under a dark steel sidewalk scaffolding shed, its beams framing the view, a giant landscape screen across the street.',
  'Camera under the shed at street level, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the black steel posts and the beam above make a clean frame within the frame; wet pavement shine.',ALL,'the screens'),
 sh(9,'single-cab-streak-past-glass-tower-screen','A single yellow cab streaks past the foot of a glass tower whose lower floors carry one giant landscape screen.',
  'Camera across the street at screen height, 50mm lens, f/4, slow shutter, square to the screen. The screen fills about 55 percent of the frame width, sharp; one long yellow cab blur crosses the bottom of the frame, below the screen, never over it.',ALL,'the screens',aspect='16:9'),
 sh(10,'from-raised-plaza-stone-ledge-to-two-screens','From a raised stone plaza, a low stone ledge in the foreground, two giant screens stacked on the facade across the street.',
  'Camera on the plaza at the height of the screens, 85mm lens, f/5.6, square to the facade. The two stacked screens together fill about 60 percent of the frame height on the centre line, sharp; the stone ledge is a dark band along the bottom.',ALL,'the screens'),
]
