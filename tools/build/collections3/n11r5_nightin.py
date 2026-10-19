# n11 round 4 (Sam: r3-02, 03, 04, 05 work, follow them: candid, tight, warm lamp; 01 had too much white and no shadows).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n11r4_nightin.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n11r5';C['name']='Night In (round 4)'
C['avoid']=_m.C['avoid']+['any object not named in the shot','a large area of bright white bedding']
I2=_m.I2;I3=_m.I3;FILM=_m.FILM
S=[
 {'n':1,'slug':'phone-on-book-nightstand','kind':'phone','refs':['phone'],'people':'none','looks':[(I2,FILM+', and its top-down camera')],
  'moment':'Her phone put down on top of a closed book on the walnut nightstand.',
  'shot':'Directly top-down, tight, 50mm, f/2.8. The phone lies on the closed hardback, slightly skewed, filling about 55 percent of the frame height, sharp. Warm lamp light falls across one corner; the walnut around falls into shadow.'},
 {'n':2,'slug':'ipad-against-cushion','kind':'ipad','refs':['ipad'],'people':'none','looks':[(I3,FILM)],
  'moment':'A tablet propped upright against a corduroy cushion on the sofa, a show paused.',
  'shot':'Straight on at seat height, 50mm, f/2, close. The tablet leans against the brown corduroy cushion, facing the camera square-on, filling about 65 percent of the frame height, sharp. The floor lamp lights it from one side; deep shadow on the other side.'},
 {'n':3,'slug':'magazine-on-duvet','kind':'print','noun':'the magazine cover','refs':[],'people':'none','looks':[(I2,FILM)],
  'moment':'A magazine left on the rumpled duvet next to the pillow, in the lamp light.',
  'shot':'From nearly straight above, tight, 50mm, f/2.8. The magazine lies flat on the oatmeal duvet, filling about 65 percent of the frame height, sharp; the duvet folds around it are warm and fall into shadow quickly.',
  'surface':'THE MAGAZINE COVER IS PLAIN BLANK WHITE matte paper, lying flat, crisp corners, nothing printed on it.','avoid':['a curled or lifted corner']},
 {'n':4,'slug':'laptop-bed-closer-dark','kind':'laptop','refs':['laptop'],'people':'none','looks':[(I3,FILM)],
  'moment':'A laptop open on the bed late at night, the only bright thing in the room.',
  'shot':'Straight on at mattress height, 50mm, f/2, close. The laptop faces the camera square-on, filling about 70 percent of the frame width, sharp; the duvet folds in front are soft; behind is near black.'},
 {'n':5,'slug':'phone-hand-sofa-shadow','kind':'phone','refs':['phone'],'people':'her','edge':'right','looks':[(I3,FILM)],
  'moment':'On the sofa in the dark, she holds her phone low, the lamp off to one side.',
  'shot':'Close, 50mm, f/2. Her hand holds the phone facing the camera nearly square-on, filling about 55 percent of the frame height, sharp; brown corduroy and the grey throw fill the rest, mostly in deep shadow. The lamp lights only one side of the hand.'},
]
