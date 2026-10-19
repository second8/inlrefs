# n27 round 8. Sam on r7: all four work (finals). New mockup types only: round slipmat, crate divider card, listening post screen. Props 30, 40, 41.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r7_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I3=_m.I3;LOOK=_m.LOOK
C=dict(_m.C);C['id']='n27r8';C['name']='Listening Room (round 8)'
S=[
 {'n':1,'slug':'slipmat-on-platter-top-down','kind':'print','noun':'the slipmat','refs':['turntable'],'people':'none','comp':'B','looks':[(I3,LOOK)],
  'moment':'Our walnut turntable with its lid lifted away, a round slipmat on the platter, under a pinspot.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2, close. The walnut plinth edges run parallel to the photo edges; the round platter and slipmat sit centred, filling about 75 percent of the frame width, sharp; the slim tonearm rests at its post to the right. Warm pinspot pool on the mat; the plinth corners fall into shadow.',
  'surface':'THE SLIPMAT IS A PLAIN WHITE ROUND FELT MAT lying flat on the platter, crisp round edge, a small centre hole with the spindle, nothing printed on it.','avoid':['a record or vinyl','a dust lid over the platter']},
 {'n':2,'slug':'divider-card-walnut-crate','kind':'card','noun':'the divider card','refs':['crate'],'people':'none','comp':'D','looks':[(I3,LOOK)],
  'moment':'In our walnut record crate on the shop shelf, one white divider card rises above the row of dark sleeves.',
  'shot':'Straight on, very close, 85mm, f/2, camera exactly at the card. The divider card stands upright on the centre line, its face square to the camera, filling about 65 percent of the frame height, sharp; the dark sleeve tops run in a soft row on both sides, and the walnut front wall of the crate runs straight across the bottom. One pinspot from above; the rest falls into black.',
  'surface':'THE DIVIDER CARD IS PLAIN BLANK WHITE thick matte board with a square tab, flat and rigid, crisp corners, nothing printed on it.','avoid':['album art','letters on the tab']},
 {'n':3,'slug':'listening-post-felt-wall','kind':'screen','noun':'the listening post screen','refs':['listening_post'],'people':'none','comp':'C','looks':[(I3,LOOK)],
  'moment':'Our walnut listening post mounted on the moss-green felt wall, headphones hanging on its hook, its small screen lit.',
  'shot':'Straight on, close, 50mm, f/2, camera exactly at the screen. The walnut panel stands on the centre line, its edges parallel to the photo edges, framing the landscape screen near its top with an even margin; the screen faces the camera dead square, filling about 55 percent of the frame width, sharp. Below, the knob and the top of the headphone band show, soft. The felt wall falls into darkness at both sides.'},
]
