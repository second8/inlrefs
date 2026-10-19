# n28 Atelier round 15 (Sam 19 Oct): r14 05 nameplate 'works' (final). 01 neck label 'makes no sense' (hands came from the camera side while she faced away; label stuck outside the coat back),
# 02 tee on hanger 'overdone, scale bad', 03 dust bag 'glitched', 04 tissue seal 'overdone' (repeat of r1). New real touchpoints only, same street, sun and soft colour.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r14=_m('n28r14_kit')
C=dict(r14.C);C['id']='n28r15'
sh,BL=r4.sh,r4.BL
S=[
 {'n':1,'slug':'neck-label-inside-coat-laid-flat-top-down','kind':'print','noun':'the design surface','refs':['look_coat'],'comp':'B','people':'none',
  'moment':'The long black coat lies flat on a sunlit pale stone bench, folded open at the top so the inside of the back neck faces up, showing the small woven label sewn into the black lining just below the collar seam.',
  'shot':'Camera straight down, 85mm lens, f/8, very close. The inside back neck of the coat fills the frame: the black lining, the collar seam running straight across the upper part, and the woven label sewn flat on the centre line just below it, at its true size of about 5 by 2.5 centimetres, filling about 35 percent of the frame width, sharp, its four stitched edges visible; a hard diagonal sun shadow of the folded front edge falls across one corner of the lining, never over the label; a sliver of pale stone at one edge.',
  'surface':'THE WOVEN LABEL IS PLAIN IVORY WOVEN DAMASK, flat with fine visible weave, neatly stitched into the lining on all four edges, crisp, '+BL+'.'},
 sh(2,'shoe-box-on-pavement-by-boots-top-down',[],
  'A lidded shoe box sits closed on the sunlit stone pavement; the pointed toes of her black boots stand at its edge.',
  'Camera straight down, 50mm lens, f/8. The lid of the shoe box sits on the centre line, its edges parallel to the frame, filling about 50 percent of the frame width, sharp, a real shoe box of true size beside her boots; the toes of her two black boots and the hem of the wide trousers enter from the bottom edge; the box throws a crisp hard shadow onto the smooth stone pavement to one side.',
  'coat','Only the toes of her boots and the hem of the trousers are in frame at the bottom edge, in exactly the outfit from the reference.',
  'THE SHOE BOX LID IS PLAIN MATTE WARM IVORY BOARD with a slim espresso side band, flat, crisp corners, '+BL+'.'),
 {'n':3,'slug':'blade-sign-on-brass-bracket-above-door','kind':'print','noun':'the design surface','refs':[],'comp':'A','people':'none',
  'moment':'A square enamel shop sign hangs from a slim brushed brass bracket sticking out from the pale stone wall above the atelier\'s doorway, the way old shop signs hang over a street.',
  'shot':'Camera on the pavement a few metres down the street at the height of the sign, 85mm lens, f/8, looking along the wall so the sign faces the camera square-on. The sign sits on the centre line, filling about 40 percent of the frame width, sharp, at its true size of about 60 centimetres square, hanging from the bracket by two short rods; the stone wall runs away along one side in hard sun; the top of the deep doorway below it; clear pale sky above, no other signs.',
  'surface':'THE SIGN FACE IS PLAIN MATTE IVORY ENAMEL inside a thin brushed brass edge, flat, crisp corners, '+BL+'.'},
 {'n':4,'slug':'silk-scarf-laid-flat-on-stone-ledge-top-down','kind':'print','noun':'the design surface','refs':[],'comp':'B','people':'none',
  'moment':'A square silk scarf is laid out flat on a broad sunlit pale stone ledge outside the atelier.',
  'shot':'Camera straight down, 50mm lens, f/8. The scarf lies on the centre line, its four hemmed edges parallel to the frame, filling about 70 percent of the frame width, sharp, flat with only one soft natural ripple near a corner; its rolled hand-stitched hem visible; the weathered stone ledge around it; a crisp hard shadow from the edge of the wall cuts diagonally across the stone beside it, never over the scarf.',
  'surface':'THE SCARF IS PLAIN IVORY SILK TWILL with a soft sheen and a hand-rolled hem, flat, '+BL+'.'},
 {**sh(5,'clothing-box-under-arm-mid-stride-side-crop',[],
  'She walks along the sunlit stone wall carrying a flat clothing box tucked under her arm against the long black coat.',
  'Camera at the height of the box from the side, 85mm lens, f/5.6, square to the box. The large flat face of the box faces the camera on the centre line, held under her arm against her side, filling about 50 percent of the frame width, sharp; her forearm and hand hold its lower edge; the black wool coat around it; hard sun from the side and her hard shadow on the pale stone wall behind.',
  'coat','Only her body from the shoulder to the hip is in frame, side on, in exactly the outfit from the reference.',
  'THE BOX FACE IS PLAIN MATTE WARM IVORY BOARD with a slim espresso grosgrain ribbon around it at one end, flat, crisp corners, '+BL+'.'),'comp':'D'},
]
