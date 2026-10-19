# n28 Atelier round 18 (Sam 19 Oct): r17 finals 01, 03, 04, 05; 02 envelope 'does not work'; 03 'nice, don't overdo it anymore' (doorway framing).
# 'The last had creativity +10, now do 5 more with creativity +30.' Old inspo note: other outfits, high-fashion poses not corporate. Same world and grade.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour');r16=_m('n28r16_chic')
C=dict(r16.C);C['id']='n28r18'
sh,BL,BAG,GC,CARD,TAG,GLOVE=r4.sh,r4.BL,r4.BAG,r11.GC,r11.CARD,r11.TAG,r16.GLOVE
S=[
 {**sh(1,'birds-eye-garment-cover-laid-flat-long-shadow',['gcover'],
  'Seen from three floors above, she stands still on the pale stone pavement beside our garment cover, which lies flat on the stone at her feet; her long hard shadow cuts across the frame.',
  'Camera straight down from high above, 50mm lens, f/8. A graphic bird\'s-eye view: the garment cover lies flat on the stone on the centre line, its front panel facing straight up, edges parallel to the frame, filling about 35 percent of the frame width, sharp; she stands beside it seen from directly above, the top of her auburn head and the shoulders of the long black coat; her long black shadow stretches in a clean diagonal across the pale stone; nothing else on the pavement.',
  'coat','She is seen from directly above; only the top of her head, her shoulders and the coat show, never her face.',GC),'comp':'B'},
 sh(2,'invitation-held-out-with-its-shadow-double-on-wall',[],
  'Standing close to a sunlit pale stone wall, she holds a show invitation card out at arm\'s length; on the wall behind, her own crisp shadow holds a shadow card, like a double.',
  'Camera square to the wall, 50mm lens, f/8. The real card sits on the centre line, square to the camera, filling about 35 percent of the frame width, sharp, between her slender fingers at the end of her outstretched arm; on the pale wall beside it the hard black shadow of her arm, hand and the card repeats the gesture larger; her shoulder and the satin enter from the frame edge.',
  'slip','Only her outstretched arm, hand and shoulder are in frame, in exactly the outfit from the reference; her shadow on the wall shows only the arm and card.',CARD),
 sh(3,'tower-of-ribbon-tied-boxes-in-gloved-arms',[],
  'She walks along the sunlit stone street carrying a tall stack of four flat clothing boxes, each tied with espresso grosgrain ribbon, held in her gloved arms against the long black coat.',
  'Camera at chest height, 85mm lens, f/5.6, square to the stack. The four boxes rise in a slightly uneven tower on the centre line, the front face of the largest middle box square to the camera, filling about 45 percent of the frame width, sharp; her gloved hands hold the bottom box; the black coat around them; hard side sun; pale stone wall behind.',
  'coat','Only her body from the shoulder to the hip and her gloved hands are in frame, the stack hiding her chest, in exactly the outfit from the reference.'+GLOVE,
  'THE FRONT FACE OF THE MIDDLE BOX IS PLAIN MATTE WARM IVORY BOARD, flat, crisp corners, with the espresso ribbon crossing only at its edge; '+BL+'.'),
 {**sh(4,'hang-tag-spinning-from-gloved-finger-shadow-on-stone',['hangtag'],
  'Our hang tag hangs from its cord over one gloved finger, caught mid-turn in the sun, its large crisp shadow falling on the pale stone below.',
  'Camera at the height of the tag, 100mm lens, f/5.6, fast shutter, square to the tag face at the instant it turns toward the lens. The tag sits on the centre line, flat to the camera, filling about 35 percent of the frame width, sharp; the cord rises to her gloved fingertip at the top edge; below and behind, its long hard shadow and the shadow of her hand stretch across the sunlit stone ground.',
  'coat','Only her gloved hand and the end of the coat sleeve are in frame at the top edge.'+GLOVE,TAG),'comp':'D'},
 sh(5,'editorial-crouch-on-steps-bag-at-boots',['bag_atelier'],
  'She crouches low on the pale stone steps in a high-fashion editorial pose, knees apart, forearms draped over her knees, hands hanging loose; our bag stands upright on the step at her feet.',
  'Camera low at the height of the bag, 50mm lens, f/5.6, square to the bag front. The bag stands on the centre line, front square to the camera, filling about 40 percent of the frame width, sharp; her crouched figure behind and above it, the belted shirt dress folding sharply at the knees, her hands hanging loose over her knees; hard sun throws a strong shadow down the steps; frame cropped at her shoulders.',
  'shirt','Her body from the shoulders down is in frame in a strong, angular high-fashion crouch, in exactly the outfit from the reference.',BAG),
]
