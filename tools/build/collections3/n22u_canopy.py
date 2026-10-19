# n22 round 4 (Sam on r3: all five work, but boring, same objects, framing and compositions). Every shot a different object AND a
# different composition: top-down roof, through a window, through a steering wheel, hanging sign, fabric flag, cup on a bollard.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n22t_canopy.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n22u';C['name']='Canopy (round 4)'
C['avoid']=_m.C['avoid']+['the same straight-on post shot as before']
S=[
 {'n':1,'slug':'phone-on-car-roof-top-down','kind':'phone','refs':['phone'],'people':'none','comp':'B',
  'moment':'A phone left lying face up on the roof of the graphite car while it charges under the canopy.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The phone lies square to the frame on the graphite roof, filling about 45 percent of the frame height, sharp; the canopy LED panels reflect in the paint as a soft grid of pale rectangles beside it, never over the screen; the roof edge curves away at one side.'},
 {'n':2,'slug':'charger-screen-through-side-window','kind':'screen','noun':'the charger screen','refs':['ev_post'],'people':'none','comp':'C',
  'moment':'From inside the parked car, the charger screen seen through the open side window.',
  'shot':'From the driver seat, camera square to the charger screen, 50mm, f/2.8. The dark window frame and door top form a rectangle parallel to the photo edges; inside it, the charger post screen sits on the centre line, dead square, filling about 40 percent of the frame height, sharp; the dark car interior frames the bottom and sides.'},
 {'n':3,'slug':'dashboard-screen-through-wheel','kind':'screen','noun':'the dashboard screen','refs':[],'people':'none','comp':'C',
  'moment':'Inside the graphite car at 2am, the landscape dashboard screen seen through the rim of the steering wheel.',
  'shot':'Straight on from the driver seat, camera square to the screen, 50mm, f/2.8. The dark steering wheel rim frames the frame; the landscape screen sits centred inside the rim, dead square, filling about 45 percent of the frame width, sharp; the dashboard and wheel stay dark and soft; canopy light through the windscreen above.'},
 {'n':4,'slug':'height-bar-sign-on-chains','kind':'sign','noun':'the height bar panel','refs':[],'people':'none','comp':'A',
  'moment':'The height bar hanging on two chains across the forecourt entrance, its long panel lit by the canopy.',
  'shot':'Straight on, camera at the height of the bar, 85mm, f/4. The long landscape panel hangs level on the centre line from two thin chains, its face dead square, filling about 70 percent of the frame width, sharp; the canopy soffit a white band above; black night below and beyond.',
  'surface':'THE PANEL FACE IS PLAIN MATTE WHITE, flat and rigid, crisp edges, nothing printed on it.'},
 {'n':5,'slug':'feather-flag-forecourt-edge','kind':'print','noun':'the flag','refs':[],'people':'none','comp':'A',
  'moment':'A tall feather flag on a slim pole at the edge of the forecourt, still in the night air, the canopy glow behind it.',
  'shot':'Straight on, camera at the middle of the flag, 85mm, f/4. The tall curved feather flag stands on the centre line, its face square to the camera, filling about 75 percent of the frame height, sharp, hanging smooth with a soft natural curve; behind, the lit canopy edge; the rest is black night.',
  'surface':'THE FLAG IS PLAIN WHITE polyester fabric, smooth, crisp hemmed edges, nothing printed on it.'},
 {'n':6,'slug':'vending-cup-on-bollard-top','kind':'print','noun':'the cup sleeve','refs':['pr05'],'people':'none','comp':'D',
  'moment':'A takeaway cup from the vending kiosk left standing on top of a steel bollard under the canopy.',
  'shot':'Straight on, very close, camera at cup height, 90mm, f/2.8. The cup stands on the centre line on the round bollard top, its sleeve square to the camera, filling about 60 percent of the frame height, sharp; the brushed steel bollard top below; the canopy light from above; black beyond.',
  'surface':'THE CUP SLEEVE IS PLAIN MATTE WHITE paper wrapped around the cup, smooth, crisp edges, nothing printed on it.'},
]

# +10 (Sam: "at least 30"). Inside the car while it charges, plus forecourt surfaces not yet shot. Each a different composition.
CAR='Inside the graphite car parked under the canopy at 2am, dark leather and black trim, canopy light falling through the windscreen.'
S+=[
 {'n':7,'slug':'phone-on-console-charging-pad','kind':'phone','refs':['phone'],'people':'none','comp':'B',
  'moment':'Inside the car, a phone lying on the wireless charging pad in the centre console while the car charges.',
  'shot':'Directly from above, lens pointing straight down, 35mm, f/2.8, close. The phone lies square to the frame on the black rubber pad, filling about 50 percent of the frame height, sharp; the console trim edges run parallel around it; canopy light from above. '+CAR},
 {'n':8,'slug':'watch-wrist-on-steering-wheel','kind':'watch','refs':['watch'],'people':'edge','who':'his','edge':'left','comp':'D',
  'moment':'Waiting for the charge, a wrist with a smartwatch rests on top of the steering wheel.',
  'shot':'Very close, 85mm, f/2.8, camera square to the watch face. The watch face fills about 40 percent of the frame width on the centre line, dead square, sharp; the dark leather wheel rim runs across under the wrist; the windscreen glows faintly behind. '+CAR},
 {'n':9,'slug':'tablet-on-passenger-seat-top-down','kind':'ipad','refs':['ipad'],'people':'none','comp':'B',
  'moment':'A tablet left on the passenger seat while the car charges.',
  'shot':'Directly from above, lens pointing straight down, 35mm, f/2.8. The tablet lies square to the frame on the black leather seat, filling about 60 percent of the frame width, sharp; the seat stitching runs straight around it. '+CAR},
 {'n':10,'slug':'laptop-steering-wheel-desk-tray','kind':'laptop','refs':['laptop'],'people':'none','comp':'A',
  'moment':'A laptop open on a slim desk tray clipped to the steering wheel, working while the car charges.',
  'shot':'Straight on from the driver seat, camera at screen height, 35mm, f/2.8. The laptop sits on the centre line on the tray, screen dead square, filling about 60 percent of the frame width, sharp; the wheel rim curves under it; the windscreen and canopy glow beyond, soft. '+CAR},
 {'n':11,'slug':'night-pay-window-small-screen','kind':'screen','noun':'the small screen','refs':['paywindow'],'people':'none','comp':'C',
  'moment':'The kiosk night window after midnight: thick glass, steel tray, and the small screen beside it lit.',
  'shot':'Straight on, camera at the height of the screen, 50mm, f/2.8. The steel window frame forms a rectangle at one side, the dim shop soft behind the glass; the small screen beside it sits on the centre line, dead square, filling about 30 percent of the frame width, sharp; graphite wall around.'},
 {'n':12,'slug':'kiosk-front-lightbox-poster','kind':'print','noun':'the poster','refs':[],'people':'none','comp':'A',
  'moment':'A lit poster case fixed to the dark kiosk front under the canopy.',
  'shot':'Straight on, camera at the centre of the case, 50mm, f/2.8. The slim steel poster case sits on the centre line, its lit portrait poster dead square, filling about 65 percent of the frame height, sharp; the dark glass kiosk front either side.',
  'surface':'THE POSTER IS PLAIN EVENLY BACKLIT WHITE behind clear acrylic, crisp edges, nothing printed on it, not blown out.'},
 {'n':13,'slug':'car-wash-gantry-led-sign','kind':'screen','noun':'the gantry sign','refs':[],'people':'none','comp':'A',
  'moment':'The long LED sign across the top of the car wash entrance, lit, the wash bay dark beyond.',
  'shot':'Straight on, camera at the height of the sign, 85mm, f/4. The long landscape LED panel sits level on the centre line across the gantry, dead square, filling about 70 percent of the frame width, sharp; the steel gantry frame below; black night above.'},
 {'n':14,'slug':'bollard-wrap-close','kind':'print','noun':'the bollard wrap','refs':[],'people':'none','comp':'D',
  'moment':'A steel bollard at the edge of the bay with a printed wrap band around it.',
  'shot':'Straight on, very close, 90mm, f/4, camera square to the band. The wrap band runs around the bollard on the centre line, its front facing the camera, filling about 55 percent of the frame width, sharp; brushed steel above and below; the asphalt dark behind.',
  'surface':'THE WRAP IS A PLAIN MATTE WHITE VINYL BAND around the bollard, smooth, crisp edges, nothing printed on it.'},
 {'n':15,'slug':'door-jamb-tyre-label','kind':'print','noun':'the label','refs':[],'people':'none','comp':'D',
  'moment':'The driver door open at the charger, the tyre label on the door jamb catching the canopy light.',
  'shot':'Straight on, very close, 90mm, f/4, camera square to the label. The small landscape label sits on the centre line on the graphite painted jamb, filling about 50 percent of the frame width, sharp; the door seal and hinge soft at the edges.',
  'surface':'THE LABEL IS PLAIN MATTE WHITE, flat, crisp corners, nothing printed on it.'},
 {'n':16,'slug':'kiosk-glass-door-decal','kind':'print','noun':'the door decal','refs':[],'people':'none','comp':'C',
  'moment':'The closed kiosk glass door at 2am, one plain decal panel on the glass, the dim shop behind.',
  'shot':'Straight on, camera at the decal, 50mm, f/2.8. The slim steel door frame forms a tall rectangle parallel to the photo edges; the decal sits on the centre line of the glass, square, filling about 45 percent of the frame width, sharp; the shop inside soft and dim.',
  'surface':'THE DECAL IS A PLAIN MATTE WHITE VINYL PANEL flat on the glass, crisp edges, nothing printed on it.'},
]
