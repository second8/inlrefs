# n28 Atelier round 17, the last 5 (Sam 19 Oct): r16 finals 01, 02; 01 'works but overdone', 02 'nice, +1 for changing and being creative', 03 broken, 04 'amazing creativity'.
# 'This is the last 5 images: think out of the box, things not done, creative, new explorations.' Same world and grade as r16, gloves and poise kept.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour');r16=_m('n28r16_chic')
C=dict(r16.C);C['id']='n28r17'
sh,BL,BAG,GC,GLOVE=r4.sh,r4.BL,r4.BAG,r11.GC,r16.GLOVE
S=[
 {**sh(1,'appointment-card-tucked-into-glove-cuff',[],
  'A small appointment card is tucked under the cuff of her black leather glove at the inside of her wrist, her hand held still against the long black coat.',
  'Very close, 100mm lens, f/5.6, square to the card. The card sits on the centre line, flat to the camera, filling about 40 percent of the frame width, sharp, its lower half slipped under the soft edge of the glove cuff; the fine grain of the black leather and the wool sleeve around it; hard side sun carves the leather; a sliver of pale stone behind.',
  'coat','Only her gloved hand, wrist and the coat sleeve are in frame, in exactly the outfit from the reference.'+GLOVE,
  'THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, small, flat, crisp corners, '+BL+'.'),'comp':'D'},
 {**sh(2,'wax-sealed-envelope-gloved-fingertips-on-stone',[],
  'Her gloved fingertips hold an envelope flat against a sunlit pale stone wall, its flap closed with a round espresso wax seal.',
  'Close, 85mm lens, f/5.6, square to the envelope. The back of the envelope sits on the centre line, flat against the stone, filling about 55 percent of the frame width, sharp, its pointed flap and the deep espresso wax seal with a soft pressed rim at the centre; two gloved fingertips rest at one corner; the weathered limestone texture around it; a crisp shadow line crosses the stone beside it, never over the envelope.',
  'coat','Only her gloved fingertips and the end of the black coat sleeve are in frame, in exactly the outfit from the reference.'+GLOVE,
  'THE ENVELOPE IS PLAIN THICK PAPER-WHITE COTTON PAPER, flat, crisp folded edges, the wax seal blank and smooth, '+BL+'.'),'comp':'D'},
 {**sh(3,'garment-cover-seen-from-dark-atelier-doorway',['gcover'],
  'From deep inside the dark atelier we look out through its tall stone doorway: she crosses the bright sunlit street outside, carrying our garment cover by its hook, side on to us.',
  'Camera inside in the shadow, 50mm lens, f/5.6, square to the doorway. The black interior and the dark stone jambs frame the bright opening; inside the opening the garment cover hangs from her raised hand, its front panel square to the camera on the centre line, filling about 40 percent of the frame width, sharp; her long black coat and stride behind it; the sunlit pale stone of the street beyond.',
  'coat','Only her raised gloved hand, the coat and her stride are in frame, side on, her head cropped by the top of the doorway, in exactly the outfit from the reference.'+GLOVE,GC),'comp':'C'},
 sh(4,'bag-mid-swing-pavement-level-long-shadow',['bag_atelier'],
  'She walks toward the camera along the pale stone pavement; our bag swings out at the end of her arm, frozen in the air; her long hard shadow stretches along the stone toward us.',
  'Camera very low at knee height on the pavement, 50mm lens, f/8, fast shutter, square to the bag front. The bag hangs frozen mid-swing on the centre line, front square to the camera, filling about 40 percent of the frame width, sharp; below it her long sharp shadow runs across the stone toward the lens; her black wide trousers and pointed boots in step behind; pale stone wall and sky above.',
  'coat','Only her body from the waist down, her gloved hand and her shadow are in frame, in exactly the outfit from the reference.'+GLOVE,BAG),
 {**sh(5,'unboxing-coat-in-tissue-note-card-top-down',[],
  'On the sunlit stone steps an open clothing box holds the long black coat folded in ivory tissue; her gloved hand lays a folded note card on top.',
  'Camera straight down, 50mm lens, f/8. The open box fills most of the frame, its edges parallel to the frame; inside, the black wool folded in soft ivory tissue; the folded note card lies on the centre line on top of the coat, flat to the camera, filling about 35 percent of the frame width, sharp; her gloved hand just releasing it from one side; the box lid leans on the step beside it; a hard diagonal shadow from the step edge crosses one corner, never over the card.',
  'coat','Only her gloved hand and the coat folded in the box are in frame.'+GLOVE,
  'THE NOTE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, folded once, flat, crisp edges, '+BL+'.'),'comp':'B'},
]
