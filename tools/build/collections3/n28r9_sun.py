# n28 Atelier round 9 (Sam 19 Oct): r8-01 'really like this, pose framing comp', r8-04 'nice works', r8-05 'now this is something i really like'.
# r8-02: shadow good, but the tag was almost the size of the clothes; go close. r8-03: way too far for a mockup, work on framing.
# New inspo: B&W street fashion, hard midday sun, stone city walls, long hard shadows, oversized black coats ('look how fashiony').
# So: r8 crops and B&W Tri-X, taken outside into hard sun; product big and close.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r8=_m('n28r8_studio')
C=dict(r8.C);C['id']='n28r9'
C['register']='A black and white luxury fashion campaign photograph made on a city street in hard midday sun'
C['world']='A city street at midday: pale weathered stone walls, smooth pavement, deep doorways; nothing else unless the shot names it.'
C['light']='Hard, direct midday sun from high on one side: crisp black shadows with sharp edges, long shadows on the pavement, bright stone, no fill.'
C['finish']='Shot on 35mm Kodak Tri-X with a red filter, developed in D-76: fine, clearly visible film grain, deep inky blacks in the shadows, bright clean stone, strong graphic contrast like a printed fashion editorial. Never smooth, never glossy, never a digital render.'
C['avoid']=['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','any colour','any object not named in the shot','other people','a clean, smooth digital look']
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD=r8.CARD;TAG=r8.TAG
S=[
 sh(1,'bag-carried-side-crop-hard-sun-stone-wall',['bag_atelier'],
  'She walks along a pale stone wall in hard midday sun in the long black coat, our bag hanging from her hand at her side.',
  'Camera at hip height, 50mm lens, f/8, side on to her. The frame is cropped from just below her shoulder to her knee; the bag hangs on the right half of the frame from her relaxed hand by its ribbon handles, the bag front square to the camera, filling about 45 percent of the frame width, sharp and sunlit; the heavy black coat swings with her stride; her hard black shadow falls across the bright stone wall behind her.',
  'coat','Only her body from just below the shoulder to the knee and her hand are in frame, side on, in exactly the outfit from the reference.',BAG),
 {**sh(2,'hang-tag-on-coat-cuff-tight-hard-sun',['hangtag'],
  'Close detail as she walks in hard sun: our hang tag hangs from the cuff of her black coat on its espresso cord.',
  'Very close, 85mm lens, f/5.6, square to the tag. Only the coat sleeve, the cuff and her bare hand fill the frame; the tag hangs from the cuff on the centre line, filling about 40 percent of the frame height, sharp, fully in sun; a hard diagonal shadow edge crosses the black wool beside it, never over the tag; the bright pavement soft far below.',
  'coat','Only her hand, wrist and the coat cuff and sleeve are in frame, in exactly the outfit from the reference.',TAG),'comp':'D'},
 {**sh(3,'hang-tag-at-shirt-collar-very-tight',['hangtag'],
  'She stands still in hard sun in the white shirt dress; our hang tag hangs at the stand collar.',
  'Very close, 100mm lens, f/5.6, straight on. The stand collar, the top buttons and the crisp white poplin fill the frame from edge to edge; the tag hangs at the collar on the centre line, filling about 45 percent of the frame width, sharp; the hard sun throws a crisp shadow of the tag onto the poplin beside it.',
  'shirt','Only the collar, the top of the shirt dress and the base of her neck are in frame, cropped below the chin, in exactly the outfit from the reference.',TAG),'comp':'D'},
 sh(4,'invitation-at-hip-mid-stride-hard-shadow',[],
  'Mid-stride on a sunlit pavement in the long black coat, she holds a show invitation card flat against her hip.',
  'Camera at hip height, 50mm lens, f/8, straight on. The frame runs from her waist to her knee; the card sits on the centre line against the black coat, square to the camera, filling about 40 percent of the frame width, sharp and sunlit; a hard diagonal shadow from a doorway cuts across the coat beside the card, never over it; the bright pavement and her long shadow below.',
  'coat','Only her body from the waist to the knee and her hand are in frame, in exactly the outfit from the reference.',CARD),
 sh(5,'bag-past-fluted-shop-window-hard-sun',['bag_atelier'],
  'She stands by a shop window of fluted glass in hard sun, holding our bag out to her side; the photographer shoots past the edge of the fluted glass.',
  'The left third of the frame is seen through the fluted glass of the shop window close to the lens, breaking her black coat and arm into repeated vertical ghost slices with bright sun edges; the bag hangs in the clear part of the frame, square to the camera, filling about 45 percent of the frame width, dead sharp, never behind the glass. Hard sun from the right. 50mm lens, close, camera at bag height.',
  'coat','Only her arm, hand and the coat from the shoulder to the knee are in frame, in exactly the outfit from the reference.',BAG),
]
