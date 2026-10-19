# C11 round 4 (Sam on r3: "boring, almost 100% the same, no creativity, please focus"; 07 image wrong). Same world, new ways to use the
# wall: a backlit print in a square, an LED square, glossy-desk reflections from above, over-the-shoulder from behind, a wall-arm tablet.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c11r2_lightbox.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c11r3';C['name']='Lightbox (round 4)'
GW=['glasswall']
OS='The back of a head and one shoulder fill the {e} third of the frame as a large, soft, dark silhouette in the foreground, turned fully away; no face, cheek, ear or profile is visible.'
S=[
 {'n':1,'slug':'backlit-print-in-glass-square','kind':'print','noun':'the backlit print','refs':GW,'people':'none','comp':'C',
  'moment':'One square of the frosted glass wall holds a backlit print, glowing through like a real lightbox film.',
  'shot':'Straight on, camera square to the wall, 50mm, f/4. The print fills one glass square on the centre line, edge to edge inside the black grid, dead square, sharp; the squares around it glow plain; the dark desk edge low in the frame.',
  'surface':'THE BACKLIT PRINT IS A PLAIN WHITE TRANSLUCENT FILM lit evenly from behind, slightly brighter and cleaner than the frosted glass around it, crisp square edges inside the grid, nothing printed on it.'},
 {'n':2,'slug':'led-screen-square-in-grid','kind':'screen','noun':'the screen square','refs':GW,'people':'none','comp':'C',
  'moment':'One square of the glass wall is a flush screen built into the grid.',
  'shot':'Straight on, camera square to the wall, 50mm, f/4. The flush screen fills one square on the centre line exactly, edge to edge inside the black grid, dead square, sharp and crisp, its cooler clean white standing apart from the warm glow of the frosted squares around it.'},
 {'n':3,'slug':'phone-glossy-desk-grid-reflection','kind':'phone','refs':['phone']+GW,'people':'none','comp':'B',
  'moment':'A phone lying face up on a glossy black desk in front of the wall, the glowing grid reflected in the gloss around it.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/4, close. The phone lies square to the frame on the glossy black lacquer, filling about 50 percent of the frame height, sharp; the reflected grid of glowing squares lies in the gloss around it as soft pale rectangles, never over the screen.'},
 {'n':4,'slug':'laptop-over-shoulder-from-behind','kind':'laptop','refs':['laptop']+GW,'people':'line','people_line':OS.format(e='left'),'comp':'D',
  'moment':'Seen from behind someone sitting at the desk, the laptop screen beyond their shoulder, the glowing grid behind it.',
  'shot':'Over the shoulder, close, 50mm, f/4, camera square to the screen. The screen sits on the centre-right, dead square, filling about 55 percent of the frame width, sharp; the grid runs level behind it.'},
 {'n':5,'slug':'phone-over-shoulder-held-up','kind':'phone','refs':['phone']+GW,'people':'line','people_line':OS.format(e='right'),'comp':'D',
  'moment':'Seen from just behind, a phone held up at arm length past the shoulder, its screen toward the camera against the glowing wall.',
  'shot':'Over the shoulder, close, 85mm, f/4, camera square to the screen. The phone sits on the centre-left, screen dead square, filling about 45 percent of the frame height, sharp; the hand is a dark shape at its base; one glass square frames it behind.'},
 {'n':6,'slug':'tablet-on-wall-arm-mullion','kind':'ipad','refs':['ipad']+GW,'people':'none','comp':'A',
  'moment':'A tablet mounted on a slim black arm fixed to one of the steel grid mullions, like a wall kiosk.',
  'shot':'Straight on, camera at screen height, 50mm, f/4, close. The tablet sits on the centre line on its short arm, screen dead square, filling about 55 percent of the frame width, sharp; the arm meets the black mullion behind; the squares glow around it.'},
 {'n':7,'slug':'watch-wrist-glossy-desk-top-down','kind':'watch','refs':['watch']+GW,'people':'edge','who':'his','edge':'right','comp':'B',
  'moment':'A wrist with a smartwatch resting on the glossy black desk, the grid reflected in the gloss.',
  'shot':'Directly from above, lens pointing straight down, 85mm, f/4, close. The watch face sits on the centre line, dead square, filling about 40 percent of the frame width, sharp; the forearm runs in from the right as a dark shape; the reflected grid lies in the gloss around it, never over the face.'},
 {'n':8,'slug':'portrait-display-on-floor-in-square','kind':'screen','noun':'the portrait display','refs':GW,'people':'none','comp':'A',
  'moment':'A tall portrait display standing on the floor against the glass wall, set exactly inside one column of squares.',
  'shot':'Straight on, camera at the centre of the screen, 50mm, f/4. The portrait display stands on the centre line, dead square, filling about 70 percent of the frame height, sharp, its edges aligned with the vertical grid lines either side; the floor a dark band below.'},
]
