# n22 round 3 (Sam on r2: 02 phone + charger screen = "2 screens, AI, bad"; 06 card tap bad; 04 pump-top works). One screen per frame,
# no hands, no card or payment words (content filter), our props 76 and new 80, 81.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n22s_canopy.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n22t';C['name']='Canopy (round 3)'
C['avoid']=_m.C['avoid']+['a second screen or a phone','a hand']
S=[
 {'n':3,'slug':'canopy-column-portrait-screen','kind':'screen','noun':'the column screen','refs':[],'people':'none','comp':'A',
  'moment':'A slim portrait digital screen fixed flat to one of the steel canopy columns, glowing at 2am.',
  'shot':'Straight on, camera exactly at the centre of the screen, 50mm, f/2.8, close. The portrait screen sits on the centre line on the column, dead square, filling about 65 percent of the frame height, sharp; the steel column runs straight up and down the frame; the dark forecourt falls to black either side.'},
 {'n':4,'slug':'bay-blade-sign-on-column','kind':'sign','noun':'the blade sign','refs':[],'people':'none','comp':'A',
  'moment':'A projecting blade sign on a short steel bracket from a canopy column, marking the bay, lit by the canopy.',
  'shot':'Straight on to the face of the blade, camera at its height, 85mm, f/4. The landscape blade panel sits on the centre line, its face dead square, filling about 60 percent of the frame width, sharp; the bracket and the column at one edge; the canopy soffit a white strip above; black night beyond.',
  'surface':'THE BLADE FACE IS PLAIN MATTE WHITE, flat, crisp edges and corners, nothing printed on it.'},
 {'n':5,'slug':'dispenser-small-screen-close','kind':'screen','noun':'the small screen','refs':['pay_unit'],'people':'none','comp':'D',
  'moment':'The small landscape screen on the side of our steel fuel dispenser, lit under the canopy.',
  'shot':'Straight on, very close, 90mm, f/4, camera exactly at the screen. The small screen sits on the centre line filling about 55 percent of the frame width, dead square, sharp; brushed steel runs to the frame edges around it with one clean highlight along an edge.'},
]
S_PROPS=[
 {'n':1,'slug':'air-tower-pressure-display','kind':'screen','noun':'the display','refs':['airtower'],'people':'none','comp':'D',
  'moment':'The small digital display on our steel air tower at the edge of the forecourt, glowing.',
  'shot':'Straight on, very close, 90mm, f/4, camera exactly at the display. The display sits on the centre line filling about 50 percent of the frame width, dead square, sharp; the two round steel buttons below; the coiled black hose soft at one edge.'},
 {'n':2,'slug':'car-wash-column-screen','kind':'screen','noun':'the column screen','refs':['carwash'],'people':'none','comp':'A',
  'moment':'Our graphite car wash pay column on its concrete island at the side of the forecourt, its portrait screen lit.',
  'shot':'Straight on, camera exactly at the screen, 50mm, f/2.8, close. The portrait screen sits on the centre line in its steel bezel, dead square, filling about 60 percent of the frame height, sharp; the sloped graphite head above; the yellow bollard soft at one edge; black night behind.'},
]
if os.environ.get('WITH_PROPS'): S=sorted(S+S_PROPS,key=lambda s:s['n'])
