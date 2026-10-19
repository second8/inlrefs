# n28 Atelier round 10 (Sam 19 Oct): finals picked from r9: 01, 02, 04, 05. r9-03 'too big, not realistic, especially the rope and placement'.
# 'can we add soft coloring too'. So: same hard-sun stone street world and crops, in soft muted colour; new objects and moments.
# HARD RULE (Sam 19 Oct): never pass an inspiration image as a reference. Describe it in words only.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r9=_m('n28r9_sun')
C=dict(r9.C);C['id']='n28r10'
C['register']='A luxury fashion campaign photograph in soft muted colour, made on a city street in hard midday sun'
C['palette']='Soft, muted colour: pale warm limestone, soft faded blacks, ivory and stone tones, natural skin, gently desaturated like a faded colour print; no strong or saturated colour, no blue or orange cast. The design surface is the cleanest white in the frame.'
C['finish']='Shot on 35mm Kodak Portra 160, slightly overexposed and printed soft: fine visible grain, gentle faded colour, soft blacks, smooth highlights, the hard sun shadows still crisp. Calm and editorial like a printed fashion campaign; never glossy, never a digital render.'
C['avoid']=['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','saturated or strong colour','any object not named in the shot','other people','a clean, smooth digital look']
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD=r9.CARD;TAG=r9.TAG
S=[
 sh(1,'garment-cover-carried-by-hanger-walking',['gcover'],
  'She walks along a sunlit pale stone wall carrying our garment cover by its hanger hook at her side.',
  'Camera at hip height, 50mm lens, f/8, side on to her. The frame runs from her shoulder to her knee; the garment cover hangs straight from her hand, its flat front panel square to the camera, filling about 45 percent of the frame width, sharp and sunlit; the long black coat moves with her stride; her hard shadow falls on the stone wall behind.',
  'coat','Only her body from the shoulder to the knee and her hand are in frame, side on, in exactly the outfit from the reference.',
  'THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
 sh(2,'seated-stone-steps-bag-beside-boots',['bag_atelier'],
  'She sits on sunlit pale stone steps in the ivory satin slip and cardigan; our bag stands upright on the step beside her feet.',
  'Camera low at bag height, 50mm lens, f/8, straight on. The frame runs from her knees to the step below her feet; the bag stands on the step on the right of centre, its front square to the camera, filling about 40 percent of the frame width, sharp and sunlit; her satin hem and ivory mules beside it; the hard shadows of the steps cut clean horizontal lines across the frame.',
  'slip','Only her legs from the knee down and her feet are in frame, seated, in exactly the outfit from the reference.',BAG),
 sh(3,'hang-tag-on-cardigan-cuff-medium-close',['hangtag'],
  'Her hand rests on a sunlit stone ledge; our hang tag hangs naturally from the cuff of her oversized ivory cardigan on a short cord.',
  'Medium close, 85mm lens, f/5.6, square to the tag. Her hand, wrist and the knit cuff fill the lower half of the frame; the tag hangs at its natural small size just below the cuff, filling about 25 percent of the frame height, sharp, fully in sun, its cord short and simply tied; the pale stone ledge and a hard shadow edge beside it.',
  'slip','Only her hand, wrist and the cardigan cuff are in frame, in exactly the outfit from the reference.',TAG),
 {**sh(4,'invitation-on-stone-ledge-in-tissue-top-down',['tissue'],
  'A show invitation card lies in opened warm ivory tissue on a sunlit stone ledge; her hand rests at the edge of the frame.',
  'Camera straight down, 50mm lens, f/8. The card lies flat, its edges parallel to the frame, filling about 50 percent of the frame width, sharp; the soft folds of opened tissue around it; the pale limestone ledge with its fine pores; her fingers in the black coat sleeve at the lower edge; one hard diagonal shadow from a window frame crosses beside the card, never over it.',
  'coat','Only her fingers and the end of the coat sleeve are in frame, in exactly the outfit from the reference.',CARD),'comp':'B'},
 sh(5,'bag-held-in-deep-stone-doorway-light',['bag_atelier'],
  'She stands in the hard light at the mouth of a deep stone doorway in the white shirt dress, holding our bag at her side.',
  'Camera at bag height, 50mm lens, f/8, straight on. The frame runs from her waist to her knee; the bag hangs on the centre line from her hand, square to the camera, filling about 45 percent of the frame width, sharp and fully in sun; the deep stiff cuff of the sleeve beside it; the doorway behind falls into deep shadow and its hard vertical shadow edge runs beside the bag, never over it.',
  'shirt','Only her body from the waist to the knee and her hand are in frame, in exactly the outfit from the reference.',BAG),
]
