# n27 round 9, final big round (Sam: "we need 10 more"). New mockup types only, our props (56-59, pr02, mixer, watch). Finals already cover
# sleeves, menus, posters, projection, streamer, phones, tablet, coaster, laptop, niche, ticket, divider, listening post, slipmat.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r8_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
I3=_m.I3;LOOK=_m.LOOK
C=dict(_m.C);C['id']='n27r9';C['name']='Listening Room (round 9)'
BL='nothing printed on it'
def sh(n,slug,kind,noun,refs,comp,moment,shot,surface=None,avoid=None,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs,'people':'none','comp':comp,'looks':[(I3,LOOK)],'moment':moment,'shot':shot}
    if surface: d['surface']=surface
    if avoid: d['avoid']=avoid
    d.update(kw);return d
S=[
 sh(1,'card-terminal-walnut-counter','screen','the terminal screen',['pr02'],'D',
  'Our card terminal standing in its dock on the walnut bar counter, its screen lit under the pinspot.',
  'Straight on, very close, 85mm, f/2, camera exactly at the screen. The terminal faces the camera dead square on the centre line, its screen filling about 55 percent of the frame height, sharp; the walnut counter edge runs straight across the bottom; behind is black with one warm pendant blur.',avoid=['a receipt or bill','a card in the slot']),
 sh(2,'walnut-lightbox-felt-wall','screen','the lightbox face',['lightbox'],'A',
  'Our walnut-framed lightbox glowing on the moss-green felt wall by the entrance.',
  'Straight on, camera exactly at the centre of the lightbox, 50mm, f/2. The lightbox hangs on the centre line, its face square to the camera, filling about 65 percent of the frame width, sharp, the felt texture warm around it and falling into darkness at the edges.',
  'THE LIGHTBOX FACE IS PLAIN OPAL WHITE ACRYLIC, evenly lit from inside, the brightest thing in the frame without blowing out, crisp edges inside the walnut frame, '+BL+'.'),
 sh(3,'cd-jewel-case-counter-top-down','print','the CD insert',['cdcase'],'B',
  'A clear CD jewel case lying on the walnut counter in the pinspot, its plain insert behind the lid.',
  'Directly from above, lens pointing straight down, 50mm, f/2, close. The square case lies square to the frame, filling about 60 percent of the frame width, sharp; one small soft highlight on the clear lid near a corner, never over the centre. Walnut grain around it falls into black.',
  'THE INSERT IS PLAIN MATTE WHITE paper behind the clear lid, flat, crisp corners, '+BL+'.',['album art','a disc on top']),
 sh(4,'smartwatch-wrist-by-mixer','watch','the watch',['watch','mixer'],'D',
  'At the booth, a wrist with a smartwatch rests beside our rotary mixer between two tracks, the watch face turned up.',
  'From above, very close, 85mm, f/2, camera square to the watch face. The watch face fills about 45 percent of the frame width, on the centre line, dead square to the camera, sharp; the knurled knobs of the mixer sit soft beside it. Warm pinspot light, deep shadow.',
  people='edge',who='his',edge='left'),
 sh(5,'entrance-door-glass-decal-night','print','the door decal',[],'C',
  'From inside the bar at night, the glass entrance door with one plain decal panel on the glass at eye height.',
  'Straight on, camera exactly at the decal, 50mm, f/2. The slim walnut door frame forms a tall rectangle parallel to the photo edges; the rectangular decal sits on the centre line of the glass, square to the camera, filling about 45 percent of the frame width, sharp; beyond the glass the street is a soft dark blue blur with one warm streetlight.',
  'THE DECAL IS A PLAIN MATTE WHITE VINYL PANEL applied flat to the glass, crisp edges and corners, '+BL+'.',['readable signs outside','people outside']),
 sh(6,'felt-banner-walnut-dowel','print','the banner',['banner'],'A',
  'Our off-white felt banner hanging from its walnut dowel on the moss-green felt wall, under one pinspot.',
  'Straight on, camera exactly at the centre of the banner, 50mm, f/2. The banner hangs on the centre line, flat and square to the camera, filling about 70 percent of the frame height, sharp, the black cord making a neat triangle above the dowel; the felt wall falls into darkness either side.',
  'THE BANNER IS PLAIN OFF-WHITE WOOL FELT, hanging flat, straight cut edges, '+BL+'.'),
 sh(7,'brown-bottle-label-counter-pinspot','print','the bottle label',['beer'],'A',
  'Our brown longneck bottle standing alone on the walnut counter under the pinspot.',
  'Straight on, camera exactly at the label, 85mm, f/1.8, close. The bottle stands on the centre line, its body label square to the camera, filling about 70 percent of the frame height, sharp; one clean vertical highlight runs down the glass beside the label. Behind is black with one warm pendant blur.',
  'THE BODY LABEL IS PLAIN MATTE WHITE PAPER, flat on the glass, crisp edges, '+BL+'.',['a glass','foam','condensation']),
 sh(8,'photo-book-face-out-record-shelf','print','the book cover',[],'A',
  'A large hardcover photo book standing face-out on the walnut record shelf, between rows of dark sleeve spines.',
  'Straight on, camera exactly at the cover, 50mm, f/2, close. The book stands on the centre line, its cover square to the camera, filling about 65 percent of the frame height, sharp; the dark sleeve spines on both sides make soft vertical rhythm and fall into shadow.',
  'THE COVER IS PLAIN MATTE WHITE cloth-bound board, flat, crisp corners, '+BL+'.',['album art','readable spines']),
 sh(9,'walnut-info-plaque-by-hifi','print','the plaque',[],'D',
  'A small walnut-framed info plaque mounted on the felt wall beside the hi-fi, like a museum label for the system.',
  'Straight on, very close, 90mm, f/2.8, camera exactly at the plaque. The landscape plaque sits on the centre line, square to the camera, filling about 60 percent of the frame width, sharp; at one edge the soft dark shape of a walnut speaker cabinet shows. One pinspot.',
  'THE PLAQUE FACE IS PLAIN MATTE WHITE card under a thin walnut frame, flat, crisp edges, '+BL+'.'),
 sh(10,'wall-tv-behind-dj-booth','tv','the television',['pr04'],'A',
  'A slim television mounted on the walnut wall behind the empty DJ booth, glowing in the dark room.',
  'Straight on, camera exactly at the centre of the screen, 50mm, f/2. The television sits on the centre line, facing the camera dead square, filling about 70 percent of the frame width, sharp; the top of the walnut booth runs straight across the bottom of the frame, soft; the walls fall to black.'),
]
