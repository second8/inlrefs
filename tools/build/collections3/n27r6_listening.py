# n27 round 6, agreed 16 Oct ("go"). Wins r5: 01 menu card front, 04 phone held, 05 laptop booth front: one object, square-on, black behind.
# Fail: 03 tablet top-down had a host story + hand -> angled. No hands on top-down. Object-first moments.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r5_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I3=_m.I3;LOOK=_m.LOOK
C=dict(_m.C);C['id']='n27r6';C['name']='Listening Room (round 6)'
C['avoid']=_m.C['avoid']+['a glass, a bill or a receipt']
S=[
 {'n':1,'slug':'tablet-walnut-stand-front','kind':'ipad','refs':['ipad'],'people':'none','looks':[(I3,LOOK)],
  'moment':'A tablet standing upright in a slim walnut stand on the counter, under a pinspot.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/1.4, close. The tablet stands in portrait, facing the camera dead square, filling about 70 percent of the frame height, sharp. The slim walnut stand is a simple low slotted block. The counter edge runs across the bottom, soft; behind is black.'},
 {'n':2,'slug':'gatefold-open-counter-top-down','kind':'print','noun':'the open gatefold sleeve','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'An open 12-inch gatefold record sleeve lying flat on the walnut counter in the pinspot.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2, close. The opened gatefold, two square panels side by side, lies flat and square to the frame, filling about 85 percent of the frame width, sharp. Walnut grain shows around it and falls into black at the corners.',
  'surface':'BOTH INNER PANELS ARE PLAIN BLANK WHITE matte board, lying flat with a crisp centre fold and square corners, nothing printed on them.','avoid':['a record or vinyl','a curled or lifted corner']},
 {'n':3,'slug':'phone-counter-top-down-pinspot','kind':'phone','refs':['phone'],'people':'none','looks':[(I3,LOOK)],
  'moment':'A phone lying face up on the walnut counter, alone in the warm pool of the pinspot.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2, close. The phone lies flat and square to the frame, filling about 60 percent of the frame height, sharp. The pinspot pool sits around it on the walnut; the counter falls into black at the edges.'},
 {'n':4,'slug':'coaster-counter-top-down','kind':'card','noun':'the coaster','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'One square paperboard coaster lying on the walnut counter in the pinspot, nothing on it.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2, close. The square coaster lies flat and square to the frame, filling about 55 percent of the frame width, sharp; its thick edge just visible. Walnut grain around it falls into black.',
  'surface':'THE COASTER FACE IS PLAIN BLANK WHITE thick matte paperboard, perfectly flat, crisp square corners, nothing printed on it and nothing standing on it.'},
 {'n':5,'slug':'member-card-held-front','kind':'card','noun':'the member card','refs':[],'people':'her','edge':'bottom','looks':[(I3,LOOK)],
  'moment':'A member card held up between two fingertips in the pinspot, its face turned to the camera.',
  'shot':'Straight on, 85mm, f/1.4, close. Two fingertips hold the card at its bottom edge, the card upright and facing the camera dead square, filling about 70 percent of the frame width, sharp. Everything behind is black with one warm pendant blur.',
  'surface':'THE CARD IS PLAIN BLANK WHITE thick matte card, flat and rigid, crisp rounded corners, nothing printed on it.'},
]
