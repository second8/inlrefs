# C3 round 4 (Sam on r3: tote, magazine, bag, sleeve final; bike works but makes no sense, recreate; laptop broken; cap too close,
# redo; no more iPad). Redo bike, cap, laptop with sense; new: ticket, compact camera rear screen (prop 82).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c3r_flash.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c3r3';C['name']='Flash (round 4)'
C['avoid']=_m.C['avoid']+['a watch','a tablet','a bent, broken or warped laptop']
PL=_m.PL;W=_m.W
def sh(n,slug,kind,noun,refs,comp,moment,shot,surface=None,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs+W,'people_line':PL,'comp':comp,'moment':moment,'shot':shot}
    if surface: d['surface']=surface
    d.update(kw);return d
S=[
 sh(1,'bike-phone-mount-standing-beside','phone','the phone',['bike'],'A','He stands beside his black city bike at the kerb, one hand on the bar, checking the route on the phone in the handlebar mount.',
  'Straight on to the front of the handlebar at bar height, 35mm, f/8, camera square to the phone. The phone in its mount sits on the centre line, screen dead square, filling about 35 percent of the frame height, sharp; the straight bar and grips run across the frame; his hand on one grip and his grey trousers and loafers beside the front wheel; hard flash shadow on the ribbed wall behind.'),
 sh(2,'cap-on-perforated-bench-seat','print','the cap front',['cap','bench_perf'],'A','His plain cap rests on the perforated steel bench seat beside him, front panels facing out.',
  'Straight on, camera low at seat height, 35mm, f/8. The cap sits on the centre line on the perforated seat, its front panels square to the camera, filling about 40 percent of the frame width, sharp; his grey trouser leg and hand resting on the seat at one side; hard flash shadow behind the cap.',
  'THE FRONT PANELS ARE PLAIN OFF-WHITE COTTON TWILL, smooth, nothing printed on them.'),
 sh(3,'laptop-open-bench-hand-close','laptop','the laptop',['laptop','bench_perf'],'D','His laptop stands open on the perforated bench seat right beside his hand.',
  'Straight on, close, camera at seat height, 35mm, f/8, camera square to the screen. The intact, straight laptop sits on the centre line, its screen dead square, filling about 65 percent of the frame width, sharp; his hand rests flat on the seat at one edge; hard flash shadow behind the lid on the ribbed wall.'),
 sh(4,'concert-ticket-between-fingers','print','the ticket',[],'D','Outside the venue, he holds his concert ticket up between two fingers.',
  'Straight on, very close, 50mm, f/8, camera square to the ticket. The long ticket fills about 60 percent of the frame width on the centre line, sharp; his two fingers hold one end; the navy cuff and cream vest soft behind; hard flash shadow.',
  'THE TICKET FACE IS PLAIN MATTE WHITE thick card, flat and rigid, crisp corners, a neat perforation line near one end, nothing printed on it.'),
 sh(5,'compact-camera-rear-screen','screen','the camera screen',['camera'],'D','He holds our silver compact camera, checking the flash shot he just took on its rear screen.',
  'Straight on, very close, 50mm, f/8, camera square to the rear screen. The compact camera fills about 55 percent of the frame width on the centre line, its rear screen dead square, sharp; his fingers wrap the sides; the navy cuff and cream vest soft behind; hard flash.'),
]

# +9 (Sam 20:38: "why not make more, I would make at least 30"). Night-out moments with our props 83-87, no watch, no tablet.
S+=[
 sh(6,'wheat-paste-poster-ribbed-wall','print','the poster',[],'A','A freshly pasted poster on the ribbed concrete wall; he walks past it at the edge of the frame.',
  'Straight on, camera at the centre of the poster, 35mm, f/8. The portrait poster sits on the centre line flat on the ribs, square to the camera, filling about 60 percent of the frame height, sharp, the paper following the ribs slightly; his grey trouser leg and loafer pass at one edge; hard flash shadows.',
  'THE POSTER IS PLAIN MATTE WHITE paper pasted flat, crisp edges, faintly following the wall ribs, nothing printed on it.'),
 sh(7,'bus-shelter-lightbox-beside-bench','screen','the lightbox face',['shelter'],'C','The lit lightbox panel at the end of our bus shelter beside the bench; he sits at the far end of the bench.',
  'Straight on to the panel, camera at its centre, 35mm, f/8. The graphite frame of the shelter end forms a tall rectangle parallel to the photo edges; the lit panel fills about 60 percent of the frame height, dead square, sharp; his crossed grey trouser legs and loafers at one edge on the bench; flash on the frame.',
  'THE LIGHTBOX FACE IS PLAIN EVENLY LIT WHITE, crisp edges inside the frame, nothing printed on it, not blown out.'),
 sh(8,'sticker-on-bike-top-tube','print','the sticker',['bike'],'D','A square sticker on the top tube of his black city bike, his hand resting on the saddle above.',
  'Very close, 50mm, f/8, camera square to the sticker. The square sticker on the matte black tube fills about 45 percent of the frame width on the centre line, sharp; the tube runs across the frame; his hand on the saddle soft at the top edge; hard flash.',
  'THE STICKER IS PLAIN GLOSS WHITE vinyl, flat on the tube with gently rounded corners, nothing printed on it, no glare.'),
 sh(9,'soda-bottle-label-in-hand','print','the bottle label',['soda'],'D','Sitting on the bench, he holds a cold soda by its neck, the label toward the camera.',
  'Straight on, very close, 50mm, f/8, camera square to the label. The bottle fills about 65 percent of the frame height on the centre line, the label dead square, sharp; dry glass; his fingers at the neck; grey trouser and the bench soft behind; hard flash.',
  'THE LABEL IS PLAIN MATTE WHITE PAPER, flat on the glass, crisp edges, nothing printed on it.',avoid=['condensation drops']),
 sh(10,'leather-key-tag-in-fingers','print','the key tag',['keytag'],'D','At the door, he holds up his keys by the leather tag.',
  'Straight on, very close, 85mm, f/8, camera square to the tag. The tan leather tag fills about 50 percent of the frame width on the centre line, sharp; the brass ring and keys hang below; his fingers pinch the ring at the top; the cream vest soft behind; hard flash.',
  'THE TAG FACE IS PLAIN SMOOTH TAN LEATHER with stitched edges, blank, nothing embossed.'),
 sh(11,'event-flyer-handed-to-camera','print','the flyer',[],'D','Outside the venue, he hands a flyer straight toward the camera.',
  'Straight on, very close, 35mm, f/8, camera square to the flyer. The A5 flyer fills about 65 percent of the frame height on the centre line, sharp, held by his fingers at one corner; the navy cuff and cream vest behind; hard flash shadow.',
  'THE FLYER IS PLAIN MATTE WHITE paper, flat, crisp corners, nothing printed on it.'),
 sh(12,'enamel-pin-on-vest','print','the pin face',['pin'],'D','A round enamel pin on the cream cable-knit vest, just below the V neck.',
  'Straight on, very close, 100mm macro, f/8, camera square to the pin. The round pin sits on the centre line filling about 35 percent of the frame width, sharp; the cable-knit texture of the cream vest fills the frame around it; the navy collar at the top edge; hard flash.',
  'THE PIN FACE IS PLAIN FLAT WHITE ENAMEL inside a thin gold rim, nothing on it.'),
 sh(13,'paperback-on-bench-top-down','print','the book cover',['bench_perf'],'B','A paperback left face up on the perforated bench seat beside his hand.',
  'Directly from above, lens pointing straight down, 35mm, f/8. The closed paperback lies square to the frame on the perforated steel, filling about 50 percent of the frame width, sharp; his hand rests flat beside it with a slice of grey trouser; hard flash shadow tight around the book.',
  'THE COVER IS PLAIN MATTE WHITE card, flat, crisp corners, nothing printed on it.'),
 sh(14,'felt-laptop-sleeve-under-arm','print','the leather patch',['sleeve'],'D','Walking home, his charcoal felt laptop sleeve tucked under his arm, the leather patch facing out.',
  'Straight on, close, 35mm, f/8, camera square to the sleeve. The felt sleeve fills about 65 percent of the frame width on the centre line, the small tan leather patch sharp; the navy sleeve of his arm across its top; the cream vest behind; hard flash.',
  'THE LEATHER PATCH IS PLAIN SMOOTH TAN LEATHER, stitched on, blank, nothing embossed.'),
]
