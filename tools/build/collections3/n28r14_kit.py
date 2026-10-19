# n28 Atelier round 14 (Sam 19 Oct): 'be intentional, create images that match this collection, not random objects; think what a collection is for, what it needs.'
# r13: poster 'works but more about fashion', lookbook 'tf do I need a book', car 'great, creative, AI messed up', cafe chair 'nice'.
# The collection = mockup kit for a fashion label's identity. Finals cover bag (6), invitation (6), garment cover (4), hang tag (3), poster (1).
# Missing touchpoints: woven neck label, printed tee, dust bag, tissue seal, shop nameplate. One per shot, same world (hard sun, pale stone, soft colour).
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour')
C=dict(r11.C);C['id']='n28r14'
C['world']='A quiet city street of the fashion house at midday: pale weathered stone walls and steps, smooth pavement, the atelier\'s deep stone doorway; nothing else unless the shot names it.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
NOFACE_BACK='She is seen from behind; only the back of her neck, her hair tucked up and her hands are in frame; no face, cheek, ear or profile shows.'
S=[
 {**sh(1,'woven-neck-label-inside-coat-collar-from-behind',[],
  'She stands with her back to the camera in hard sun and folds the collar of the long black coat down with both hands, showing the woven label sewn inside at the neck.',
  'Very close from behind, 85mm lens, f/5.6, square to the label. The folded-down black wool collar and her two hands fill the frame; the woven label sits on the centre line inside the collar, flat, filling about 35 percent of the frame width, sharp, its stitched ends visible; the back of her neck and tucked-up auburn hair soft at the top edge; hard sun from the side on the wool.',
  'coat',NOFACE_BACK,
  'THE WOVEN LABEL IS PLAIN IVORY WOVEN DAMASK, flat with fine visible weave and neat stitched ends, crisp edges, nothing woven or printed on it.'),'comp':'D'},
 {'n':2,'slug':'printed-tee-on-oak-hanger-sunlit-doorway','kind':'print','noun':'the design surface','refs':['hanger_tee'],'comp':'C','people':'none',
  'moment':'Our plain off-white tee hangs on its oak hanger from the frame of the atelier\'s sunlit stone doorway.',
  'shot':'Camera straight on at chest height, 50mm lens, f/8. The stone door frame forms an even margin around the tee; the tee hangs on the centre line, flat and square to the camera, its chest filling about 50 percent of the frame width, sharp; hard sun falls across the cotton and throws its soft shadow on the stone; the deep interior behind falls to shadow.',
  'surface':'THE TEE CHEST IS PLAIN OFF-WHITE HEAVY COTTON, smooth and flat across the print area, with a natural soft fold at the hem, nothing printed on it.'},
 sh(3,'cotton-dust-bag-on-stone-ledge-by-boots',[],
  'A cotton dust bag for shoes sits upright on a sunlit stone ledge; her black pointed boots stand on the pavement just below it.',
  'Camera at the height of the dust bag, 50mm lens, f/8, square to it. The dust bag sits on the centre line, its flat front panel square to the camera, filling about 45 percent of the frame width, sharp, its drawstring neck gathered and tied; the pale stone ledge and a hard shadow beside it; the tips of her black boots and the hem of the coat at the bottom edge.',
  'coat','Only her boots and the hem of the coat are in frame at the bottom edge, in exactly the outfit from the reference.',
  'THE DUST BAG IS PLAIN WARM IVORY BRUSHED COTTON with a thin espresso drawstring, its front panel flat and smooth, crisp seams, nothing printed on it.'),
 {'n':4,'slug':'tissue-seal-inside-open-bag-top-down','kind':'print','noun':'the design surface','refs':['tissue','bag_atelier'],'comp':'B','people':'none',
  'moment':'Looking straight down into our open shopping bag standing on a sunlit stone step: folded ivory tissue closed with one round sticker seal.',
  'shot':'Camera straight down, 50mm lens, f/8. The rim of the bag\'s folded cuff frames the frame edges; inside, the folded tissue fills the opening, and the round sticker seal sits on the centre line where the folds meet, flat to the camera, filling about 30 percent of the frame width, sharp; a hard shadow of the cuff edge falls across one side of the tissue, never over the seal.',
  'surface':'THE ROUND STICKER SEAL IS PLAIN MATTE IVORY PAPER, perfectly round and flat on the tissue, crisp edge, nothing printed on it.'},
 sh(5,'atelier-nameplate-beside-stone-doorway',[],
  'A flat nameplate is fixed on the pale stone beside the atelier\'s deep doorway; she walks in past it in the long black coat.',
  'Camera straight on to the wall at the height of the nameplate, 50mm lens, f/8. The nameplate sits on the centre line, square to the camera, filling about 35 percent of the frame width, sharp, fixed with four small brass screws; the stone door jamb and the dark doorway at the right; the edge of her black coat passing into the doorway, soft; hard sun and a crisp shadow line across the stone beside the plate, never over it.',
  'coat','Only the edge of her coat and one hand pass at the right edge, in exactly the outfit from the reference.',
  'THE NAMEPLATE FACE IS PLAIN MATTE IVORY ENAMEL in a thin brushed brass frame, flat, crisp corners, nothing engraved or printed on it.'),
]
