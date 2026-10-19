# n16 round 3 (Sam: r2-05 inspection monitor "really like it"; r2-04 too similar to 03, don't repeat; more contrast, sleek).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n16r2_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n16r3';C['name']='Yellow Room (round 3)'
C['avoid']=_m.C['avoid']+['any object not named in the shot']
S=[
 {'n':1,'slug':'microscope-monitor-arm-tight','kind':'monitor','noun':'the inspection monitor','refs':['display'],'people':'none',
  'moment':'At the second inspection station, the monitor on its swing arm is pulled close over the microscope.',
  'shot':'Close, 50mm, f/2.8, camera at monitor height. The slim monitor faces the camera square-on, filling about 65 percent of the frame width, sharp; the white microscope head is a soft amber shape at one side. Deep umber shadow in the corners, crisp highlight along the steel arm.'},
 {'n':2,'slug':'booking-pillar-portrait-screen','kind':'screen','noun':'the pillar screen','refs':[],'people':'none',
  'moment':'At the bay entrance, a slim white pillar with a portrait screen shows the tool bookings.',
  'shot':'Straight on at eye height, 50mm, f/2.8. The slim pillar and its portrait screen face the camera square-on, the screen filling about 60 percent of the frame height, sharp. The amber aisle falls away behind into soft shadow.'},
 {'n':3,'slug':'laptop-stainless-trolley-amber','kind':'laptop','refs':['laptop'],'people':'none',
  'moment':'A laptop open on the stainless trolley in the amber bay, next to the aligner.',
  'shot':'Straight on at trolley height, 50mm, f/2.8, close. The laptop faces the camera square-on on the brushed-steel trolley top, filling about 65 percent of the frame width, sharp. Amber light gives crisp highlights on the steel; the white tool behind is soft and falls into umber.'},
 {'n':4,'slug':'tablet-gloved-hand-front','kind':'ipad','refs':['ipad'],'people':'his','edge':'bottom',
  'moment':'A gloved hand holds a tablet up toward the camera to show a run plan.',
  'shot':'Straight on, 50mm, f/2.8, close. The tablet faces the camera square-on, held from the bottom edge by violet-black gloved hands, filling about 65 percent of the frame height, sharp. The amber bay behind is soft with strong contrast.'},
 {'n':5,'slug':'hanging-aisle-sign-front','kind':'sign','noun':'the hanging sign','refs':[],'people':'none',
  'moment':'A slim sign panel hangs from the ceiling grid over the amber aisle.',
  'shot':'Straight on from just below, 85mm, f/4. The landscape sign panel hangs on two thin steel cables, facing the camera square-on, filling about 60 percent of the frame width, sharp. The ceiling grid around it glows amber and falls into umber at the edges.',
  'surface':'THE SIGN PANEL IS PLAIN BLANK WHITE, matte, perfectly flat with crisp edges, nothing printed on it; it alone reads neutral white.'},
]
