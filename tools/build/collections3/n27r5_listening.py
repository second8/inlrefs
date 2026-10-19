# n27 round 5, agreed with Sam: square-on angles so the design is never distorted, closer, no extra props (no bill), no repeats
# (no amp, sleeve, streamer, projection). Builds on 02 (menu card) and 05 (framed poster, softer light with some shadow).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r3_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n27r5';C['name']='Listening Room (round 5)'
C['avoid']=_m.C['avoid']+['any object not named in the shot','a steep or tilted camera angle on the design']
I3=_m.I3;LOOK=_m.LOOK
S=[
 {'n':1,'slug':'menu-card-holder-front','kind':'card','noun':'the drink menu card','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'The single drink menu card stands in its slim walnut holder on the counter under a pinspot.',
  'shot':'Straight on at counter height, 50mm, f/1.4, close. The tall card faces the camera square-on, filling about 75 percent of the frame height, sharp. The counter edge runs across the bottom, soft; behind is black with one pendant as a small warm blur.',
  'surface':'THE CARD IS PLAIN BLANK WHITE thick matte card, standing straight and flat, crisp corners, nothing printed on it.'},
 {'n':2,'slug':'framed-poster-front-soft','kind':'print','noun':'the framed poster','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'A framed poster on the moss-green felt wall, lit softly so a little shadow falls across it.',
  'shot':'Straight on at eye height, 50mm, f/1.4, close. The portrait poster in a thin walnut frame faces the camera square-on, filling about 75 percent of the frame height, sharp. A soft, slightly dimmer pinspot from above leaves a gentle gradient and a soft shadow from the frame across the top edge; the felt around falls into darkness.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE matte paper lying perfectly flat behind non-reflective glass, crisp edges, nothing printed on it; it sits in soft light, not blown out.'},
 {'n':3,'slug':'tablet-counter-top-down','kind':'ipad','refs':['ipad'],'people':'her','edge':'right','looks':[(I3,LOOK)],
  'moment':'The host browses the library on a tablet lying flat on the walnut counter.',
  'shot':'From directly above, 50mm, f/2, close. The tablet lies flat and square to the frame on the walnut counter, filling about 70 percent of the frame width, sharp; her fingertips rest at its right edge. Walnut grain around it, falling into black at the corners.'},
 {'n':4,'slug':'phone-held-upright-pinspot','kind':'phone','refs':['phone'],'people':'her','edge':'bottom','looks':[(I3,LOOK)],
  'moment':'A phone held upright in the pinspot, its screen turned toward the camera to show the track.',
  'shot':'Straight on, 50mm, f/1.4, close. Her hand holds the phone upright from the bottom edge, the phone facing the camera square-on and filling about 60 percent of the frame height, sharp. Everything behind is black with one warm pendant blur.'},
 {'n':5,'slug':'laptop-dj-booth-front','kind':'laptop','refs':['laptop'],'people':'none','looks':[(I3,LOOK)],
  'moment':'A laptop open on the walnut DJ booth shelf, ready for the next set.',
  'shot':'Straight on at booth height, 50mm, f/1.4, close. The open laptop faces the camera square-on, filling about 65 percent of the frame width, screen sharp and keyboard soft; the walnut shelf edge runs across the bottom; behind is black.'},
]
