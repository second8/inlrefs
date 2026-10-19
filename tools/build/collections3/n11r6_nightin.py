# n11 round 6, agreed 16 Oct ("go"). Wins r5: 01 phone on book, 03 magazine duvet, 04 laptop bed, 02 ipad cushion (almost AI).
# Fail: 05 phone in hand on sofa: person story + room -> wide, angled. No nightstand this round ("dont over do this table shot").
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n11r5_nightin.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I2=_m.I2;I3=_m.I3;FILM=_m.FILM
C=dict(_m.C);C['id']='n11r6';C['name']='Night In (round 5)'
C['avoid']=_m.C['avoid']+['a nightstand']
S=[
 {'n':1,'slug':'phone-on-duvet-top-down','kind':'phone','refs':['phone'],'people':'none','looks':[(I2,FILM+', and its top-down camera')],
  'moment':'A phone lying face up on the rumpled oatmeal duvet, warm lamp light from one side.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, tight. The phone lies flat and square to the frame on the linen, filling about 60 percent of the frame height, sharp. The lamp warms one side of the folds; the other side falls into deep shadow.'},
 {'n':2,'slug':'record-sleeve-leaning-floor','kind':'print','noun':'the record sleeve','refs':[],'people':'none','looks':[(I3,FILM)],
  'moment':'A 12-inch record sleeve leaning upright against oak wall panelling on the floor, the floor lamp lighting it from one side.',
  'shot':'Straight on, camera exactly at sleeve height near the floor, 50mm, f/2, close. The square sleeve faces the camera dead square, filling about 75 percent of the frame width, sharp. Warm lamp light from one side leaves a soft gradient across it; the oak panelling and floor fall into shadow.',
  'surface':'THE SLEEVE FRONT IS PLAIN BLANK WHITE matte board, flat and rigid, crisp square corners, nothing printed on it.','avoid':['a record or vinyl','other sleeves']},
 {'n':3,'slug':'framed-print-plaster-wall-lamp','kind':'print','noun':'the framed print','refs':[],'people':'none','looks':[(I3,FILM)],
  'moment':'A framed print on the warm limewash plaster wall, lit only by the floor lamp from one side.',
  'shot':'Straight on, camera exactly at frame height, 50mm, f/2, close. The portrait print in a thin walnut frame faces the camera dead square, filling about 75 percent of the frame height, sharp. The lamp from one side leaves a soft gradient and a soft frame shadow; the plaster around falls into darkness.',
  'surface':'THE PRINT IS PLAIN BLANK WHITE matte paper lying flat behind non-reflective glass, crisp edges, nothing printed on it; it sits in soft lamp light, not blown out.'},
 {'n':4,'slug':'tv-front-dark-room','kind':'tv','noun':'the television','refs':[],'people':'none','looks':[(I3,FILM)],
  'moment':'A slim television on a low walnut media unit, the only bright thing in the dark room.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/2, close. The television faces the camera dead square, filling about 80 percent of the frame width, sharp, with thin even black bezels. The top of the walnut unit runs across the bottom edge; the wall behind falls to near black.'},
 {'n':5,'slug':'paperback-open-throw-top-down','kind':'print','noun':'the open paperback','refs':[],'people':'none','looks':[(I2,FILM)],
  'moment':'An open paperback lying face up on the grey wool throw, in the lamp light.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, tight. The open book lies flat and square to the frame, filling about 70 percent of the frame width, sharp. The lamp pool falls across it; the wool around goes into deep shadow.',
  'surface':'BOTH OPEN PAGES ARE PLAIN BLANK WHITE matte paper, lying flat with only a soft curve into the spine, crisp edges, nothing printed on them.','avoid':['text on the pages']},
]
