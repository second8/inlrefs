# n22 round (Sam ticked; earlier notes: feels AI/edited, chases the scene, no fog; 12 totem and 13 fascia work; 03 holster and 10 kiosk close).
# Mockup-first, close and square, our props 74, 76, 77. No fog, no halation, no wide forecourt.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n22r_forecourt.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n22s';C['name']='Canopy (close)'
C['world_short']='A motorway services forecourt at 2am under a flat white LED canopy; dark asphalt; brushed steel posts; past the canopy edge the night is black.'
C['finish']='Shot handheld on a 35mm film camera, 50mm and 90mm macro, f/2.8, on 800-speed colour negative film: visible grain heavier in the shadows, crisp edges, no halation, no glow around lights, no haze. Feels like a real night photograph, not edited.'
C['avoid']=['readable lettering, numbers or logos','a face, or a person facing the camera','fog, mist or haze','halation or glow around lights','a wide view of the forecourt','any object not named in the shot']
S=[
 {'n':1,'slug':'charger-screen-tight','kind':'screen','noun':'the charger screen','refs':['ev_post'],'people':'none','comp':'D',
  'moment':'The portrait screen of our charger post lit at 2am under the canopy.',
  'shot':'Straight on, very close, 90mm, f/2.8, camera exactly at the screen. The screen fills about 60 percent of the frame height on the centre line, dead square, sharp; the brushed steel body runs to the frame edges, the black card pad just below; canopy light makes one clean highlight along the steel edge.'},
 {'n':2,'slug':'phone-held-at-holster','kind':'phone','refs':['phone','ev_post'],'people':'edge','who':'his','edge':'right','comp':'D',
  'moment':'A driver holds his phone up beside the charger holster to start the charge from the app.',
  'shot':'Close, 50mm, f/2.8, camera square to the phone. The phone is held upright on the centre line, screen dead square, filling about 50 percent of the frame height, sharp; the black cable and connector in the steel holster sit soft behind; the canopy light from above.'},
 {'n':3,'slug':'payment-panel-screen-keypad','kind':'screen','noun':'the payment screen','refs':['pay_unit'],'people':'none','comp':'D',
  'moment':'The payment panel on the side of our steel fuel dispenser, its small screen lit, keypad blank.',
  'shot':'Straight on, very close, 90mm, f/4, camera exactly at the panel. The small screen sits on the centre line filling about 50 percent of the frame width, dead square, sharp; the grid of blank steel keys below, the card slot below that; brushed steel to the edges.',
  'avoid':['digits or letters on the keys']},
 {'n':4,'slug':'pump-top-media-screen','kind':'screen','noun':'the pump-top screen','refs':['pay_unit'],'people':'none','comp':'A',
  'moment':'The landscape media screen on top of our fuel dispenser glowing under the canopy.',
  'shot':'Straight on, camera exactly at the screen, 50mm, f/2.8. The screen sits on the centre line, dead square, filling about 65 percent of the frame width, sharp; the steel housing frames it; above, a thin strip of the white canopy soffit; behind, black night.'},
 {'n':5,'slug':'vending-kiosk-screen-close','kind':'screen','noun':'the kiosk screen','refs':['kiosk'],'people':'none','comp':'A',
  'moment':'Our graphite vending kiosk under the edge of the canopy, its portrait screen lit.',
  'shot':'Straight on, camera exactly at the screen, 50mm, f/2.8, close. The portrait screen sits on the centre line, dead square, filling about 70 percent of the frame height, sharp; the graphite cabinet frames it with the contactless pad just below; the asphalt and night fall to black at the sides.'},
 {'n':6,'slug':'card-tap-charger-reader','kind':'card','noun':'the charge card','refs':['ev_post'],'people':'edge','who':'his','edge':'right','comp':'D',
  'moment':'A driver taps a charge card on the black reader pad of our charger.',
  'shot':'Straight on, very close, 90mm, f/2.8, camera square to the card. The card is held flat against the reader pad on the centre line, its face square to the camera, filling about 45 percent of the frame width, sharp; fingertips at its right edge; the brushed steel post fills the frame around it.',
  'surface':'THE CARD FACE IS PLAIN BLANK WHITE, flat and rigid, crisp rounded corners, nothing printed on it.'},
]
