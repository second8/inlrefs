# n28 Atelier round 6 (Sam 18 Oct): r5 'started to work great': 04 prism ghost really nice, 03 glass gap really nice, 02 weak, 05 glass for its own sake = bad.
# New camera/settings refs (Behance): Fashion Flip Book (grey seamless, round spotlight halo behind the model, 35mm colour film, bold seated poses),
# Randez-Vous (accessory campaign: floor-level camera, glossy black floor mirror reflections, hard shaped light: slats, pools; legs-only crops, silhouettes),
# Gstaad Guy x Yung (intimate 50mm hand-and-product crops, wit in the pose, tactile film colour). Take settings only, never their compositions or framing borders.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r4',os.path.join(os.path.dirname(__file__),'n28r4_art.py'));r4=importlib.util.module_from_spec(_s);_s.loader.exec_module(r4)
C=dict(r4.C);C['id']='n28r6'
C['register']='An art-directed luxury accessories campaign photograph'
C['world']='A fashion set built only from what the shot names: seamless paper, a glossy floor or a plain wall, nothing else.'
C['light']='Hard, shaped light exactly as the shot describes, real light from real lamps; deep true blacks or clean greys around it, no fill unless named.'
C['finish']='Shot on real 35mm colour negative film, Portra 400 pushed one stop, with a 35mm or 50mm lens: natural visible grain, true film colour that stays neutral, gentle lens falloff toward the corners, slightly imperfect sharpness at the edges, highlights rolling off softly. Confident and tactile, like a printed campaign, never a smooth digital render. No halation, no haze.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD='THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'
S=[
 sh(1,'bag-legs-glossy-floor-reflection',['bag_atelier'],
  'Our bag stands on a glossy black floor; she steps past it in black slingback heels, only her legs in frame.',
  'Camera right on the floor, 35mm lens, f/4. One hard spotlight from high behind makes a sharp oval pool on the glossy black floor; the bag stands in it on the centre line, front square to the camera, filling about 45 percent of the frame width, sharp, with a clear mirror reflection of the bag below it on the floor; her legs in sheer black tights cross the frame mid-step behind the bag as long dark shapes, one heel lifted, their reflections stretching down; the background falls from grey to black.',
  'shirt','Only her legs below the knee and the black slingback heels are in frame, in exactly the outfit from the reference.',BAG),
 sh(2,'seated-stool-spotlight-halo-invitation',[],
  'She sits forward on a plain chrome studio stool, elbow on her knee, in the long black coat, and holds a show invitation card out toward the camera.',
  'A grey seamless paper backdrop with one hard round spotlight behind her making a soft-edged halo of light on the paper. Camera slightly low, 35mm lens, f/5.6. The card sits on the centre line, square to the camera, filling about 35 percent of the frame width, sharp; her body from the shoulders down to her boots folds into a strong angular seated pose around it; the coat leather-heavy and dark against the grey.',
  'coat','Her body from the shoulders down to her boots is in frame, seated, in exactly the outfit from the reference.',CARD),
 sh(3,'lying-on-floor-bag-held-over-face',['bag_atelier'],
  'Playful: she lies on her back on grey seamless paper in the ivory satin slip and holds our bag up above her face with both arms straight, as if shading herself from the light.',
  'Camera directly above, looking straight down, 50mm lens, f/5.6. The bag front faces the camera square on the centre line, filling about 50 percent of the frame width, sharp, completely covering her face; her arms rise to its handles; the satin slip and her hair spread on the paper around it; one hard light from the side throws a long clean shadow of the bag across the satin.',
  'slip','Her face is fully hidden behind the bag; her arms, shoulders and the satin slip down to the knee are in frame, in exactly the outfit from the reference.',BAG),
 sh(4,'bag-prism-ghost',['bag_atelier'],
  'She holds our bag in front of the black gown; the photographer holds a glass prism against the side of the lens.',
  'The prism throws a soft offset ghost copy of her gloved arm and the gown drape across one side of the frame with thin bright refracted edges; the bag itself appears only once, front square to the camera on the centre line, filling about 50 percent of the frame width, dead sharp, never doubled or covered. One hard side light on a dark set. 50mm lens, close, camera at bag height.',
  'gown','Only her gloved hand, arm and the gown from the shoulder to the knee are in frame, in exactly the outfit from the reference.',BAG),
 sh(5,'hang-tag-slatted-light-hand',['hangtag'],
  'Her hand rests at her waist on the black coat; hard light through a slatted blind falls across her in sharp diagonal bars, and our hang tag hangs from the cuff.',
  'Very close, 50mm lens, f/4, square to the tag. Sharp diagonal bars of hard light and shadow cross the black wool and her hand; one clean bar of light lands fully on the tag, which hangs on the centre line, filling about 45 percent of the frame height, sharp and evenly lit, no bar crossing it; deep black between the bars.',
  'coat','Only her hand, wrist, coat cuff and the coat front at the waist are in frame, in exactly the outfit from the reference.',
  'THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'),
 sh(6,'garment-cover-between-glass-panels-top-light',['gcover'],
  'Our garment cover hangs in the narrow clear gap between two tall fluted glass panels, lit from straight above; her gloved hand holds its hanger.',
  'Two tall fluted glass panels at the frame edges close to the lens slice the dark set and her gown behind them into vertical ghosts with thin bright edges; through the clear gap the cover hangs on the centre line, front square to the camera, filling about 65 percent of the frame height, sharp, one hard top light raking down its canvas and leaving a bright pool on the glossy floor below. 50mm lens, straight on.',
  'gown','Only her arm in the long black glove reaches in at the top of the cover; the rest of her is a sliced dark shape behind the glass, in exactly the outfit from the reference.',
  'THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
]
