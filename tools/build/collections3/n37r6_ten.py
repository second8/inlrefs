# n37 Night Square round 6 (Sam 26 Nov): R5 finals 01 shelter rain glass, 03 tour bus, 04 elevated platform, 05 crosswalk, 07 hotel window, 08 scaffolding.
# Not picked: cab windscreen, marquee edge, plaza. 'just careful with the screens, dont make them too complex.' Cab streak 'has been done already'.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r5',os.path.join(os.path.dirname(__file__),'n37r5_ten.py'));r5=importlib.util.module_from_spec(_s);_s.loader.exec_module(r5)
from _nov_common import sh
C=dict(r5.C);C['id']='n37r6'
C['real']=r5.C['real'].replace('never a thin strip or a small sliver.','never a thin strip or a small sliver. Each screen is one simple plain rectangle, a single clean panel, never complex, curved, split or oddly shaped.')
ALL=r5.ALL
S=[
 sh(1,'through-elevated-train-window-to-giant-screen','From inside a dark, empty elevated train car, a giant landscape screen on the building across the street fills the train window.',
  'Camera inside at the window, 35mm lens, f/4, square to the glass and the far screen. The screen fills about 55 percent of the frame width through the window, sharp; the dark window frame and a steel grab pole edge the photo; faint reflections on the glass, never over the screen.',ALL,'the screens'),
 sh(2,'under-elevated-track-across-to-giant-screen','From under an elevated railway track, its dark steel girders framing the top of the view, a giant landscape screen across the street.',
  'Camera at street level, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the black steel girder runs across the top of the frame and two riveted columns frame the sides; wet street shine below.',ALL,'the screens',aspect='16:9'),
 sh(3,'rain-streaks-stop-light-giant-screen','Rain falls in fine streaks across a giant portrait screen on a tower, a red stop light on a pole in the near foreground at one side.',
  'Camera across the street at screen height, 85mm lens, f/4, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; fine rain streaks catch the white light; the red stop light glows soft at the frame edge, never over the screen.',ALL,'the screens'),
 sh(4,'from-rooftop-terrace-to-giant-screen-at-roof-height','From a dark rooftop terrace, a giant landscape screen on the tower opposite sits at terrace height.',
  'Camera on the terrace, 85mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp; the terrace glass railing and its steel top rail run across the bottom of the frame; dark tower tops around.',ALL,'the screens',aspect='16:9'),
 sh(5,'from-dark-bar-doorway-to-giant-screen','From inside a dark bar, its open doorway frames a giant portrait screen across the street.',
  'Camera inside the bar at screen height, 50mm lens, f/4, square to the doorway and the far screen. The door frame is a clean dark rectangle around the screen, which fills about 50 percent of the frame height, sharp; the wet pavement outside shines.',ALL,'the screens'),
 sh(6,'past-closed-kiosk-shutter-to-giant-screen','A closed newsstand kiosk with its ribbed metal shutter down stands in the foreground; a giant landscape screen fills the facade across the street behind it.',
  'Camera at the kiosk, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the kiosk roof edge and shutter run along the bottom third; wet street shine.',ALL,'the screens'),
 sh(7,'from-top-of-subway-stairs-to-giant-screen','From the top of subway stairs, the green iron railings framing the bottom of the view, a giant landscape screen across the street.',
  'Camera at the top step at street level, 50mm lens, f/5.6, square to the far screen. The screen fills about 55 percent of the frame width, sharp; the two iron railings frame the lower corners; wet pavement between.',ALL,'the screens',aspect='16:9'),
 sh(8,'through-dark-cafe-window-counter-edge','From inside a dark, closed ground-floor café, a giant screen across the street fills the big front window above the empty counter.',
  'Camera inside behind the counter at screen height, 50mm lens, f/4, square to the window. The window frame is a clean dark rectangle around the screen, which fills about 55 percent of the frame width, sharp; the dark counter edge runs along the bottom.',ALL,'the screens'),
 sh(9,'from-parking-garage-level-concrete-slabs','From an open level of a concrete parking garage, the slab above and the parapet below frame a giant landscape screen on the tower opposite.',
  'Camera on the parking deck at screen height, 50mm lens, f/5.6, square to the screen. The screen fills about 55 percent of the frame width, sharp; the dark concrete slab edge across the top and the parapet across the bottom make a clean wide frame.',ALL,'the screens',aspect='16:9'),
 sh(10,'inside-glass-skywalk-to-one-big-screen','From inside a glass-walled pedestrian skywalk over the avenue, one big landscape screen on the building across fills the view.',
  'Camera in the skywalk at screen height, 50mm lens, f/5.6, square to the glass and the screen. The screen fills about 60 percent of the frame width, sharp; the skywalk mullions frame the sides; faint red and white traffic trails far below.',ALL,'the screens'),
]
