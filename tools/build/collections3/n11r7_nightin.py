# n11 round 6 (files n11r7). Close to done (13 finals). Only new device types: our e-reader (prop 37) and a projection over the bed.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n11r5_nightin.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I2=_m.I2;I3=_m.I3;FILM=_m.FILM
C=dict(_m.C);C['id']='n11r7';C['name']='Night In (round 6)'
C['world_short']='A well-designed city apartment at night: rumpled oatmeal linen on a low bed, warm limewash plaster walls, a walnut headboard. Mostly dark.'
C['avoid']=_m.C['avoid']+['a nightstand','an open book']
S=[
 {'n':1,'slug':'ereader-on-pillow-top-down','kind':'tag','noun':'the e-reader screen','refs':['ereader'],'people':'none','comp':'B','looks':[(I2,FILM+', and its top-down camera')],
  'moment':'Our charcoal e-reader lying on the oatmeal linen pillow, the lamp warm from one side.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, tight. The e-reader lies flat, square to the frame, filling about 60 percent of the frame height, sharp. The pillow seam runs as one soft diagonal beside it; the lamp warms one side, the other falls into deep shadow.',
  'surface':'THE E-READER SCREEN IS PLAIN MATTE LIGHT GREY-WHITE, like paper, not glowing, lit only by the lamp, crisp corners inside its thin border, nothing on it.'},
 {'n':2,'slug':'projection-over-bed-headboard','kind':'screen','noun':'the projected image','refs':[],'people':'none','comp':'A','looks':[(I3,FILM)],
  'moment':'A film projected onto the plaster wall above the walnut headboard, the room dark around it.',
  'shot':'Straight on from the foot of the bed, camera at the centre of the projection, 35mm, f/2. The landscape projection sits on the centre line above the headboard, square to the camera, filling about 70 percent of the frame width; the headboard runs straight across below it and the rumpled duvet fills the bottom edge, soft and dark.',
  'surface':'THE PROJECTION IS A SHARP RECTANGLE OF PLAIN WHITE LIGHT on the warm plaster wall, evenly bright with crisp edges and corners, clearly the brightest thing in the room; nothing in it.'},
]
