# n28 Atelier round 7 (Sam 19 Oct): r6 all bad except 05 hang tag 'good image quality but bad environment'.
# r5 all 'almost good' (04 prism: really like how glass is used), r5-05 generic.
# Read: the black void / seamless sets are the problem, not the camera. Keep r6's film finish, go back to r5's glass,
# and put the glass where it belongs: the atelier's own fluted glass partitions, vitrines and fitting-room doors, after hours.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r6=_m('n28r6_campaign')
C=dict(r6.C);C['id']='n28r7'
C['register']='An art-directed luxury fashion campaign photograph made inside a real couture atelier after hours'
C['world']=('A real couture atelier after closing: raw warm-grey lime plaster walls, a worn dark oiled-oak floor, and the house\'s own tall '
            'steel-framed fluted glass partitions, vitrines and fitting-room doors. Seen only in fragments at the edges, falling into deep shadow.')
C['light']=('Real light of the room after hours: one hard neutral key light from a single source as the shot describes, the fluted glass catching '
            'thin bright edges where the light hits its ridges; deep shadow around it, no fill unless named.')
C['avoid']=['a face, chin, lips or profile','logos, letters or brand names anywhere','marble','a blue or coloured cast','any object not named in the shot','fog or haze','seamless paper, a black void or a clean smooth digital look']
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CLEAR=' The design surface itself is never behind the glass: it sits in the clear, dead sharp, single and undistorted.'
CARD='THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'
TAG='THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'
S=[
 sh(1,'invitation-prism-ghost-plaster-wall',[],
  'She holds a show invitation card up against the black gown in front of the atelier\'s plaster wall; the photographer holds a glass prism against the side of the lens.',
  'The prism throws a soft offset ghost of her gloved hand and the gown drape across the left edge of the frame with thin bright refracted edges; the card appears only once, square to the camera on the centre line, filling about 45 percent of the frame width, dead sharp, never doubled. Behind her the warm-grey plaster wall falls into shadow. One hard key from the right. 50mm lens, f/4, close, camera at card height.'+CLEAR,
  'gown','Only her gloved hand, arm and the gown from the shoulder to the waist are in frame, in exactly the outfit from the reference.',CARD),
 {'n':2,'slug':'garment-cover-in-open-glass-vitrine','kind':'print','noun':'the design surface','refs':['gcover'],
  'comp':'C','people':'trace',
  'moment':'Our garment cover hangs alone on its oak hanger inside a tall steel-framed atelier vitrine whose fluted glass door stands open.',
  'shot':'Camera straight on, 35mm lens, f/5.6, at the height of the cover. The open vitrine\'s black steel frame forms an even margin around the cover; the open fluted glass door at the right edge of the frame slices the plaster wall behind it into soft vertical ridges; the front panel of the cover hangs square to the camera on the centre line inside the frame, filling about 60 percent of the frame height, sharp, one hard top light raking down its canvas.'+CLEAR,
  'surface':'THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'},
 sh(3,'bag-carried-past-glass-door-satin-sliced',['bag_atelier'],
  'She walks out through the atelier\'s fluted glass door in the ivory satin slip and cardigan; our bag swings in her hand, already through the door into the clear.',
  'Camera at bag height, 50mm lens, f/4, square to the bag. The left 40 percent of the frame is the fluted glass door close to the lens, breaking the ivory satin and her moving legs into repeated vertical slices of light and shadow; at the right, past the door\'s clean steel edge, the bag front hangs in the clear, square to the camera, filling about 45 percent of the frame width, sharp, its handles in her relaxed hand. Off-centre: the bag sits on the right third.'+CLEAR,
  'slip','Only her body from the waist to the knee and her hand are in frame, in exactly the outfit from the reference.',BAG),
 {**sh(4,'hang-tag-on-cuff-on-vitrine-glass-top-down',['hangtag'],
  'Her hand rests flat on the clear glass top of a low atelier display vitrine; our hang tag, tied to the deep white cuff of her shirt dress, lies flat on the glass beside her fingers.',
  'Camera straight down, 50mm lens, f/4, close. The tag lies flat on the glass, its edges parallel to the frame, filling about 40 percent of the frame height, sharp; her hand and the stiff white cuff fill the lower edge; through the glass, deep below and soft, folded ivory knitwear on the vitrine shelf, and the vitrine\'s fluted glass side panel at the top edge turns the dark floor into soft ridges. One hard key from the upper left, a clean shadow of the tag on the glass.'+CLEAR,
  'shirt','Only her hand, wrist and the deep white cuff are in frame, in exactly the outfit from the reference.',TAG),'comp':'B'},
 sh(5,'bag-handed-out-of-fitting-room',['bag_atelier'],
  'Wit: from behind the fluted glass doors of a fitting room, her arm in the long black coat sleeve reaches out through the narrow gap and holds our bag out toward the camera, as if handing it back.',
  'Camera straight on at bag height, 50mm lens, f/4. The two fluted glass fitting-room doors fill the frame edge to edge, her dark shape behind them sliced into soft vertical ghosts; through the narrow gap between the doors her black coat sleeve and hand come out into the clear, holding the bag by its handles; the bag front sits on the centre line, square to the camera, filling about 50 percent of the frame width, sharp, fully in front of the glass.'+CLEAR,
  'coat','Only her arm in the coat sleeve and her hand come out of the gap; the rest of her is only a sliced dark shape behind the glass, in exactly the outfit from the reference.',BAG),
]
