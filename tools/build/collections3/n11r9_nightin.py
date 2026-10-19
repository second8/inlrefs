# n11 round 8 (files n11r9), final big round (Sam: "we need 10 more"). Console "amazing", projection "+1". New device and print types only,
# props 60-65, plus watch and display. No nightstand, no open book.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n11r8_nightin.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I2=_m.I2;I3=_m.I3;FILM=_m.FILM
C=dict(_m.C);C['id']='n11r9';C['name']='Night In (round 8)'
C['world_short']='A well-designed city apartment at night: rumpled oatmeal linen, a low walnut sideboard, warm limewash plaster walls, a grey wool throw. Mostly dark; one small lamp.'
BL='nothing printed on it'
def sh(n,slug,kind,noun,refs,comp,look,moment,shot,surface=None,avoid=None,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs,'people':'none','comp':comp,'looks':[(look,FILM)],'moment':moment,'shot':shot}
    if surface: d['surface']=surface
    if avoid: d['avoid']=avoid
    d.update(kw);return d
S=[
 sh(1,'smartwatch-wrist-duvet-edge','watch','the watch',['watch'],'D',I3,
  'In bed in the dark, a wrist with a smartwatch rests on the folded edge of the duvet, the watch face lit.',
  'Very close, 85mm, f/2, camera square to the watch face. The watch face fills about 45 percent of the frame width on the centre line, dead square to the camera, sharp; the linen folds around it glow faintly in its light and fall into deep shadow.',
  people='edge',who='her',edge='right'),
 sh(2,'smart-display-walnut-sideboard','screen','the display',['smartdisplay'],'A',I3,
  'Our small smart display standing on the low walnut sideboard in the living room at night, the only light on that wall.',
  'Straight on, camera exactly at the screen, 50mm, f/2, close. The display sits on the centre line, its screen square to the camera, filling about 55 percent of the frame width, sharp; the sideboard top runs straight across the bottom; the plaster wall above falls into darkness.'),
 sh(3,'playing-cards-fanned-wool-throw','print','the card backs',['cards'],'B',I2,
  'A deck of cards fanned out on the grey wool throw on the sofa, mid-game, in the lamp light.',
  'Directly from above, lens pointing straight down, 50mm, f/2.8, tight. The cards fan in one smooth arc on the centre line, filling about 65 percent of the frame width, sharp, all backs up; the lamp warms one side, the wool falls into shadow at the corners.',
  'THE CARD BACKS ARE PLAIN MATTE OFF-WHITE with rounded corners, '+BL+'.',['card faces or suits','chips or a drink']),
 sh(4,'tablet-bath-caddy-tub','ipad','the tablet',['ipad','caddy'],'D',I3,
  'A tablet standing in the slot of our walnut bath caddy laid across a deep white tub, the bathroom dark, a show playing.',
  'Straight on, very close, 50mm, f/2, camera exactly at the screen. The tablet faces the camera dead square, filling about 70 percent of the frame width, sharp; the walnut caddy runs straight across the bottom; behind is soft dark tile and a faint warm glow.',avoid=['bubbles or foam','candles','a person in the bath']),
 sh(5,'home-office-monitor-desk-lamp','display','the display',['display'],'A',I3,
  'A desktop display on a small walnut desk in the corner of the apartment late at night, one desk lamp on.',
  'Straight on, camera exactly at the screen, 50mm, f/2, close. The display sits on the centre line, facing the camera dead square, filling about 65 percent of the frame width, sharp; the desk edge runs straight across the bottom; the small lamp makes one warm pool at one side; the wall falls to darkness.',avoid=['a keyboard in focus','clutter']),
 sh(6,'round-thermostat-dark-hallway','screen','the thermostat screen',['thermostat'],'D',I3,
  'Our round thermostat on the limewash wall of the dark hallway, its screen lit.',
  'Straight on, very close, 90mm, f/2.8, camera exactly at the screen. The round thermostat sits on the centre line, its screen square to the camera, filling about 50 percent of the frame width, sharp; the brushed ring catches a thin highlight; the plaster around falls into darkness.'),
 sh(7,'envelope-doormat-top-down','print','the envelope',[],'B',I2,
  'An envelope lying on the doormat inside the front door, late, the hallway dark.',
  'Directly from above, lens pointing straight down, 35mm, f/2.8. The envelope lies square to the frame on the coir doormat, filling about 50 percent of the frame width, sharp; a thin line of warm light from under the door crosses the floorboards beside the mat.',
  'THE ENVELOPE FRONT IS PLAIN MATTE OFF-WHITE PAPER, flat, crisp corners, '+BL+'.',['a stamp','handwriting']),
 sh(8,'folded-sweatshirt-on-bed-top-down','print','the sweatshirt chest',['sweatshirt'],'B',I2,
  'Our oatmeal-grey crewneck folded on the rumpled bed, chest up, in the lamp light.',
  'Directly from above, lens pointing straight down, 50mm, f/2.8, tight. The folded sweatshirt lies square to the frame on the oatmeal linen, filling about 65 percent of the frame width, sharp, the ribbed collar at the top; the lamp warms one side; the linen falls into shadow.',
  'THE CHEST PANEL IS PLAIN SOFT OATMEAL-GREY COTTON, smooth and flat, '+BL+'.',['graphics on the sweatshirt']),
 sh(9,'instant-photo-taped-plaster-wall','print','the instant photo',[],'D',I3,
  'One instant photo taped to the warm plaster wall beside the bed with a strip of paper tape, lit by the bedside lamp.',
  'Straight on, very close, 90mm, f/2.8, camera exactly at the photo. The instant print sits on the centre line, square to the camera, filling about 55 percent of the frame height, sharp, the thick white frame and the paper tape strip at its top crisp; the plaster texture shows and falls into darkness.',
  'THE PHOTO AREA IS PLAIN WHITE inside the thick white instant frame, flat, '+BL+'.',['an image in the photo','several photos']),
 sh(10,'wine-bottle-label-coffee-table','print','the wine label',['wine'],'A',I3,
  'Our dark green wine bottle standing on the low walnut coffee table in the lamp light, late in the evening.',
  'Straight on, camera exactly at the label, 85mm, f/2, close. The bottle stands on the centre line, its label square to the camera, filling about 70 percent of the frame height, sharp; one warm vertical highlight runs down the glass beside the label; behind is the soft dark sofa.',
  'THE LABEL IS PLAIN TEXTURED OFF-WHITE PAPER, flat on the glass, crisp edges, '+BL+'.',['a glass','a corkscrew']),
]
