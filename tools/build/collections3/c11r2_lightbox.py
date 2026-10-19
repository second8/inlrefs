# C11 round 3 (Sam on r2: all 5 finals; "this styling works great, lets do them good now", "not get lazy, intentional thinking";
# 02 watch: two grids close together = broken grid; 03 laptop a bit far). One regular grid, never doubled; closer; new device moments.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c11r_lightbox.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c11r2';C['name']='Lightbox (round 3)'
C['avoid']=_m.C['avoid']+['two grid lines close together, a doubled or broken grid','a second wall or grid in front of the first']
C['world_short']=_m.C['world_short']+' The grid is one single regular grid of equal squares, every line straight, evenly spaced and unbroken.'
GW=['glasswall']
S=[
 {'n':1,'slug':'laptop-close-hands-on-keys','kind':'laptop','refs':['laptop']+GW,'people':'edge','who':'his','edge':'bottom','comp':'D',
  'moment':'Close on a laptop open on the dark steel desk, two hands resting on its keys as dark silhouettes, the glass grid glowing behind the screen.',
  'shot':'Straight on, close, 50mm, f/4, camera exactly at screen height. The screen fills about 70 percent of the frame width on the centre line, dead square, sharp; one vertical grid line runs exactly behind its centre; the hands are crisp dark shapes on the keyboard at the bottom edge.'},
 {'n':2,'slug':'phone-landscape-two-hands-square','kind':'phone','refs':['phone']+GW,'people':'edge','who':'her','edge':'bottom','comp':'C',
  'moment':'A phone held sideways in two hands, filming, its landscape screen sitting inside one glowing glass square.',
  'shot':'Straight on, camera square to the wall, 80mm, f/4. One glass square sits on the centre line framed by the black grid; the phone is held in landscape inside it, screen dead square to the camera, filling about 60 percent of the square width, sharp; both hands are clean dark silhouettes at its ends.'},
 {'n':3,'slug':'phone-on-stand-desk-centred','kind':'phone','refs':['phone']+GW,'people':'none','comp':'A',
  'moment':'A phone standing in a slim black stand on the dark steel desk, centred on one glass square of the wall behind.',
  'shot':'Straight on, camera exactly at screen height, 85mm, f/4, close. The phone stands on the centre line, screen dead square, filling about 55 percent of the frame height, sharp; it sits exactly centred in the glowing square behind it, the grid lines framing it evenly; the desk is a thin dark band across the bottom.'},
 {'n':4,'slug':'tablet-stand-hand-reaching','kind':'ipad','refs':['ipad']+GW,'people':'edge','who':'her','edge':'right','comp':'A',
  'moment':'A tablet standing in landscape in a low black stand on the desk, a dark hand reaching in from the side to touch its edge.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/4, close. The tablet sits on the centre line, screen dead square, filling about 65 percent of the frame width, sharp; one horizontal grid line runs exactly behind its top edge; the hand is a crisp dark silhouette at the right edge, fingertips just touching the frame of the tablet.'},
 {'n':5,'slug':'display-two-backs-either-side','kind':'display','refs':['display']+GW,'people':'line',
  'people_line':'Two people sit with their backs to the camera, one at each side of the frame, as soft dark silhouettes of heads and shoulders only, turned fully away; no face, cheek, ear or profile is visible.',
  'comp':'A','moment':'A desktop display on the dark steel desk between two people seen from behind, both looking at it.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/4. The display sits on the centre line between the two dark shoulders, screen dead square, filling about 50 percent of the frame width, sharp; the grid runs level and plumb behind, one grid square centred behind the display.'},
 {'n':6,'slug':'tv-low-console-against-glass','kind':'tv','noun':'the television','refs':['pr04']+GW,'people':'none','comp':'A',
  'moment':'A slim television on a long low black console standing against the glowing glass wall.',
  'shot':'Straight on, camera exactly at the centre of the screen, 50mm, f/4. The television sits on the centre line, dead square, filling about 70 percent of the frame width, sharp; the console is a dark band below; the grid squares rise behind it, one horizontal line running exactly along its top edge.'},
 {'n':7,'slug':'laptop-on-knees-low-bench','kind':'laptop','refs':['laptop']+GW,'people':'line',
  'people_line':'Only a seated lap and two forearms show as crisp dark silhouettes; the rest of the person is out of frame.',
  'comp':'D','moment':'Sitting on a low black bench in front of the glowing wall, a laptop open on the knees, screen toward the camera.',
  'shot':'Straight on, close, 50mm, f/4, camera at screen height. The screen fills about 65 percent of the frame width on the centre line, dead square, sharp; the knees and forearms are dark shapes around its base; the glowing grid fills the background.'},
 {'n':8,'slug':'tablet-portrait-one-hand-square','kind':'ipad','refs':['ipad']+GW,'people':'edge','who':'his','edge':'left','comp':'C',
  'moment':'A tablet held upright in portrait by one hand from the side, placed exactly inside one glowing glass square.',
  'shot':'Straight on, camera square to the wall, 80mm, f/4. The tablet stands on the centre line inside one square, screen dead square to the camera, filling about 60 percent of the frame height, sharp, an even margin of glow around it inside the grid; the hand and wrist are a dark silhouette at its left edge.'},
]
