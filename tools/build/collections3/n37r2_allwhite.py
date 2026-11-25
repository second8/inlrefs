# n37 Night Square round 2 (Sam 25 Nov): comps good on 01, 02, 04, 05 but 'all the screens should be geometric, white, so mockup design goes in it'; 03 bands bad.
# Recreate 01, 02, 04, 05 with every screen plain white, clean geometric rectangles; plus 1 new multi-screen wall.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n37r1_nightsquare.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
from _nov_common import sh
C=dict(r1.C);C['id']='n37r2'
C['world']='A dense city entertainment square at night: tall towers stacked with giant LED screens, wet asphalt and pavements. Every screen in the square is a clean geometric shape with crisp edges and every screen shows a plain white full-screen image, ready for a design; no colour, text, logos or pictures on any screen.'
C['light']='Night lit by the giant white screens: cool clean light spills across the wet streets and facades; small warm accents from traffic lights, street lamps and marquee bulbs; clean air, no smoke.'
C['palette']='Deep near-black night, glowing pure white screens, wet asphalt reflections, a few small red, amber and yellow accents from traffic and street lights. The same grade on every image of the collection.'
ALL='EVERY SCREEN IN THE FRAME SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, evenly lit edge to edge yet not blown out, each a crisp geometric shape with sharp corners; nothing crosses them.'
S=[
 sh(1,'giant-tower-billboard-all-screens-white','A giant flat LED billboard covers the upper floors of a tower on the square, with smaller flat screens on the neighbouring towers.',
  'Camera on a raised spot across the square at the billboard height, 135mm lens, f/5.6, square to it. The main billboard fills about 55 percent of the frame width on the centre line, sharp; the neighbouring screens at the frame edges are smaller clean rectangles; dark tower tops above.',ALL,'the screens'),
 sh(2,'curved-corner-screen-stone-building-all-white','A tall curved LED screen wraps around the rounded corner of an old stone building above the square, with flat screens on the buildings either side.',
  'Camera across the street at screen height, 85mm lens, f/5.6. The front of the curved screen faces the camera square-on and the curve wraps away at one side; it fills about 50 percent of the frame width, sharp; a streetlight arm and a traffic light cross the lower foreground, never over it; the wet street catches the light.',ALL,'the screens'),
 sh(3,'screen-above-theatre-marquee-cab-streak-all-white','A huge landscape LED screen sits above a theatre\'s bulb-lit marquee canopy on the square, with more flat screens on the facades beside it; a yellow cab streaks past in the foreground.',
  'Camera from across the square at the kerb, 50mm lens, f/4, slow shutter, aimed so the screen stays square. The main screen fills about 55 percent of the frame width, sharp; the marquee bulbs glow below it with no letters; the cab is a long yellow blur low in the frame; the wet asphalt mirrors the white light.',ALL,'the screens',aspect='16:9'),
 sh(4,'vertical-tower-end-of-square-walls-of-white-screens','A slim vertical LED tower stands at the far end of the square, framed by walls of flat screens on both sides of the street.',
  'Camera on a raised point in the middle of the street, 135mm lens, f/5.6, square to the tower. The tower screen fills about 65 percent of the frame height on the centre line, sharp; the walls of rectangular screens on both sides converge toward it; red and white traffic light trails run along the bottom; no people.',ALL,'the screens'),
 sh(5,'corner-wall-of-stacked-flat-screens-mixed-sizes','One building corner on the square is covered in a stacked grid of eight flat screens of different sizes, fitted together edge to edge.',
  'Camera across the square at the height of the grid middle, 85mm lens, f/5.6, square to the main face. The grid fills about 70 percent of the frame width, sharp, its screens aligned in clean horizontal and vertical lines; dark facade between them; the wet street below.',ALL,'the screens'),
]
