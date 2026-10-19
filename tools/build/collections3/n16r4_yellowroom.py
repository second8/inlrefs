# n16 round 4, agreed 16 Oct ("go"). Wins r3: 01 microscope monitor, 03 laptop trolley, r2-05 swing-arm monitor. Fails: 02 vertical again,
# 04 held tablet fakey (posed), 05 hanging sign makes no sense. More contrast, sleek, candid. No vertical screens.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n16r3_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n16r4';C['name']='Yellow Room (round 4)'
C['avoid']=_m.C['avoid']+['a portrait or vertical screen']
S=[
 {'n':1,'slug':'tablet-stainless-bench-fingertip','kind':'ipad','refs':['ipad'],'people':'tip','edge':'right','tipon':'right edge of the screen',
  'moment':'A tablet lying flat on the brushed stainless bench, a gloved fingertip just touching it mid-task.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The tablet lies flat in landscape, square to the frame, filling about 70 percent of the frame width, sharp. Crisp amber highlights on the brushed steel around it, deep umber at the corners.'},
 {'n':2,'slug':'monitor-stainless-bench-front','kind':'monitor','noun':'the monitor','refs':['display'],'people':'none',
  'moment':'A slim landscape monitor standing on the brushed stainless bench in the amber bay.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/2.8, close. The monitor faces the camera dead square, filling about 70 percent of the frame width, sharp. The steel bench edge runs across the bottom with a crisp amber highlight; behind falls into deep umber.'},
 {'n':3,'slug':'laptop-airlock-white-bench','kind':'laptop','refs':['laptop'],'people':'none',
  'moment':'A laptop open on the white bench inside the cool grey gowning airlock.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/2.8, close. The laptop faces the camera dead square, filling about 70 percent of the frame width, screen sharp and keyboard slightly soft. Cool pale grey light, crisp; a thin amber edge glows through the glass door at one side; strong contrast.'},
 {'n':4,'slug':'tool-touchscreen-flush-panel','kind':'screen','noun':'the tool touchscreen','refs':[],'people':'none',
  'moment':'A landscape touchscreen set flush into the white panel face of a lithography tool.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/2.8, close. The touchscreen faces the camera dead square, filling about 70 percent of the frame width, sharp, framed by the white panel with hairline seams. Amber light rakes across the panel; the edges fall into umber.'},
 {'n':5,'slug':'batch-sheet-clipboard-top-down','kind':'print','noun':'the batch sheet','refs':[],'people':'none',
  'moment':'A batch sheet on a white clean-room clipboard lying flat on the brushed stainless bench.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The clipboard lies flat and square to the frame, the sheet filling about 70 percent of the frame height, sharp. Crisp amber highlights on the steel around it, deep umber at the corners.',
  'surface':'THE SHEET IS PLAIN BLANK WHITE clean-room paper, lying perfectly flat under the clip, crisp corners, nothing printed on it; it alone reads neutral white.','avoid':['a pen','a curled corner']},
]
