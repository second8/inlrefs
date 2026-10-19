# C11 round 5 (Sam on r4: 6 finals; "I need more that introduce the characters more, like this (over-shoulder laptop), but not exactly
# this, do not redo or overdo"). Six different body-language moments, silhouettes from behind only, device still the hero.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c11r2_lightbox.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c11r4';C['name']='Lightbox (round 5)'
C['avoid']=_m.C['avoid']+['a person facing the camera','a second device']
GW=['glasswall'];HER=['ch06'];HIM=['ch11']
S=[
 {'n':1,'slug':'phone-handover-two-backs','kind':'phone','refs':['phone']+GW,'people':'line','comp':'D',
  'people_line':'Two people stand side by side with their backs to the camera, close, as dark silhouettes of shoulders and arms; one hand passes the phone to the other between them; no face, cheek, ear or profile is visible.',
  'moment':'Two colleagues in front of the glowing wall, one handing the phone to the other to show something.',
  'shot':'From just behind them, close, 50mm, f/4, camera square to the phone. The phone sits on the centre line between the two dark shoulders, screen dead square, filling about 40 percent of the frame height, sharp; both hands touch it, one giving, one taking; one glass square frames it behind.'},
 {'n':2,'slug':'walking-past-tablet-at-side','kind':'ipad','refs':['ipad']+GW+HER,'people':'line','comp':'A',
  'people_line':'Her full figure walks past along the wall as a crisp dark silhouette in mid-stride, long straight hair over one shoulder, head turned away from the camera toward the direction of travel; no face, cheek or profile is visible.',
  'moment':'She walks past the glowing glass wall carrying a tablet at her side, its screen facing out.',
  'shot':'Straight on, camera square to the wall, 50mm, f/4. Her silhouette crosses the frame left of centre; the tablet held low at her side sits on the vertical centre line, screen dead square to the camera, filling about 35 percent of the frame height, sharp; the grid runs level and plumb behind her.'},
 {'n':3,'slug':'pointing-at-display-two-backs','kind':'display','refs':['display']+GW,'people':'line','comp':'A',
  'people_line':'Two people stand behind the desk with their backs to the camera as dark silhouettes, heads and shoulders only at the lower edge; one raises an arm and points at the screen; no face, cheek, ear or profile is visible.',
  'moment':'Two people at the display in front of the glowing wall, one pointing at something on the screen.',
  'shot':'Straight on, camera at screen height, 50mm, f/4. The display sits on the centre line, screen dead square, filling about 50 percent of the frame width, sharp; the pointing arm is a clean dark line toward the screen edge, never crossing the screen; the grid runs behind.'},
 {'n':4,'slug':'two-hands-share-one-tablet','kind':'ipad','refs':['ipad']+GW,'people':'line','comp':'C',
  'people_line':'Two hands come in from opposite edges of the frame as dark silhouettes, one from the left and one from the right, both holding the same tablet; the rest of the two people is out of frame.',
  'moment':'Two people hold one tablet up together against the glowing wall, sharing it.',
  'shot':'Straight on, camera square to the wall, 80mm, f/4. The tablet sits on the centre line inside one glass square, screen dead square, filling about 55 percent of the frame height, sharp; one hand at each side edge; the black grid frames it evenly.'},
 {'n':5,'slug':'forearm-on-glass-phone-in-hand','kind':'phone','refs':['phone']+GW+HER,'people':'line','comp':'C',
  'people_line':'She leans her forearm flat against the glowing glass; her shoulder and long straight hair are a large dark silhouette at the right edge, head turned fully away from the camera; no face, cheek, ear or profile is visible.',
  'moment':'She leans against the glass wall, the phone in the hand of her leaning arm, screen turned toward the camera.',
  'shot':'Close, 85mm, f/4, camera square to the phone. The phone sits on the centre line inside one glass square, screen dead square, filling about 45 percent of the frame height, sharp; her forearm runs along the glass from the right as a crisp dark shape.'},
 {'n':6,'slug':'perched-on-desk-edge-laptop-beside','kind':'laptop','refs':['laptop']+GW+HIM,'people':'line','comp':'A',
  'people_line':'He sits relaxed on the edge of the desk with his back to the camera, a dark silhouette of back, shoulders and the back of his head, one hand resting on the desk; no face, cheek, ear or profile is visible.',
  'moment':'He perches on the edge of the dark steel desk in front of the glowing wall, the laptop open on the desk beside him.',
  'shot':'Straight on, camera at screen height, 50mm, f/4. The laptop sits on the centre line, screen dead square to the camera, filling about 50 percent of the frame width, sharp; his silhouette sits just right of it, not overlapping the screen; the grid runs level behind.'},
]
