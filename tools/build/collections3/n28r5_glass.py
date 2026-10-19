# n28 Atelier round 5 (Sam 18 Oct): from r4 only 03 (invitation through fluted glass) 'has potential', the rest trash.
# Push that technique: glass close to the lens slicing body and fabric, design surface sharp in the clear part. 5 shots.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r4',os.path.join(os.path.dirname(__file__),'n28r4_art.py'));r4=importlib.util.module_from_spec(_s);_s.loader.exec_module(r4)
C=dict(r4.C);C['id']='n28r5'
C['register']='An art-directed luxury fashion campaign photograph shot past glass held close to the lens'
C['light']='One hard side light, so the glass ridges catch thin bright edges and the fabric falls into deep shadow; true blacks around it, no fill.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CLEAR=' The design surface itself is never behind the glass: it sits in the clear part of the frame, dead sharp and undistorted.'
S=[
 sh(1,'bag-beside-fluted-glass-coat-sliced',['bag_atelier'],
  'She holds our bag at her side in the long black coat; the photographer shoots past the edge of a sheet of fluted glass held close to the lens.',
  'Technique: the left 40 percent of the frame is seen through vertical fluted glass right in front of the lens, breaking the black coat and her arm into repeated vertical ghost slices with thin bright edges; the bag front sits in the clear part, square to the camera, filling about 45 percent of the frame width, sharp. 50mm lens, close, camera at bag height.'+CLEAR,
  'coat','Only her body from the shoulder to the knee is in frame, in exactly the outfit from the reference.',BAG),
 sh(2,'hang-tag-beside-reeded-glass',['hangtag'],
  'Her arm is raised, the hand relaxed; our hang tag hangs from the black coat cuff while the photographer shoots past reeded glass.',
  'Technique: the right half of the frame is behind fine reeded glass close to the lens, turning the coat sleeve and her shoulder into many thin soft vertical stripes; the tag hangs in the clear left half, square to the camera, filling about 45 percent of the frame height, sharp, its cord crossing into the glass. 100mm macro, very close.'+CLEAR,
  'coat','Only her hand, wrist and the coat sleeve are in frame, in exactly the outfit from the reference.',
  'THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'),
 sh(3,'garment-cover-through-gap-in-glass-screen',['gcover'],
  'Our garment cover hangs on a slim black hook behind a tall screen of fluted glass panels with a gap between two panels; her gloved hand rests on its hanger.',
  'Technique: two tall fluted glass panels fill the left and right edges of the frame close to the lens, slicing the dark set and the gown behind them into vertical ghosts; through the clear gap between them the front panel of the cover hangs square to the camera on the centre line, filling about 60 percent of the frame height, sharp. 50mm lens, straight on.'+CLEAR,
  'gown','Only her arm in the long black glove reaches in at the top of the cover; the rest of her is only a sliced dark shape behind the glass, in exactly the outfit from the reference.',
  'THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
 sh(4,'invitation-prism-ghost',[],
  'She holds a show invitation card up against the black gown; the photographer holds a glass prism against the side of the lens.',
  'Technique: the prism at the edge of the lens throws a soft, offset ghost copy of her gloved hand and the gown drape across one side of the frame, with thin bright refracted edges; the card itself appears only once, square to the camera on the centre line, filling about 45 percent of the frame width, dead sharp, never doubled. One hard side light. 50mm lens, close.'+CLEAR,
  'gown','Only her gloved hand, arm and the gown from the shoulder to the waist are in frame, in exactly the outfit from the reference.',
  'THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'),
 sh(5,'bag-held-past-ribbed-glass-wall',['bag_atelier'],
  'She walks behind a wall of ribbed glass in the white shirt dress and holds our bag out past the end of the wall into the clear.',
  'Technique: most of the frame is the ribbed glass wall close to the lens, her walking figure behind it broken into many vertical slices of white and shadow; at the right, past the clean end of the wall, her hand holds the bag out in the clear, the bag front square to the camera, filling about 40 percent of the frame width, sharp, the deep white cuff at its handles. 35mm lens, camera at bag height.'+CLEAR,
  'shirt','Only her figure from the shoulder down shows, sliced behind the glass, plus her hand and cuff in the clear, in exactly the outfit from the reference.',BAG),
]
