# n28 Atelier round 21 (Sam 19 Oct): r20 finals 03 toss, 04 blade of sun, 06 tiptoe. 'This collection has potential, I keep going back to it; 8 more that we have not done, something unique.'
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour');r16=_m('n28r16_chic')
C=dict(r16.C);C['id']='n28r21'
sh,BL,BAG,CARD,GLOVE=r4.sh,r4.BL,r4.BAG,r11.CARD,r16.GLOVE
BOX='THE BOX LID IS PLAIN MATTE WARM IVORY BOARD with a slim espresso grosgrain ribbon around it at one end, flat, crisp corners, '+BL+'.'
S=[
 sh(1,'bag-held-up-as-mask-hiding-face',['bag_atelier'],
  'She stands against the sunlit pale stone wall holding our bag up in front of her face with both hands, a high-fashion gesture; only her auburn hair and the stand collar of the white shirt dress frame it.',
  'Camera at the height of the bag, 85mm lens, f/5.6, square to the bag front. The bag front covers her whole face on the centre line, square to the camera, filling about 45 percent of the frame width, sharp; her slender fingers hold the handles and sides; her auburn hair shows at both sides, the stand collar and the shoulders of the white shirt dress below; a hard shadow of the bag falls on the stone wall behind.',
  'shirt','Her head is completely hidden behind the bag; only her hair edges, collar, shoulders and hands show, in exactly the outfit from the reference.',BAG),
 sh(2,'clothing-box-balanced-on-head-walking-away',[],
  'Seen from behind, she walks away down the sunlit stone street balancing a flat clothing box on her head, hands relaxed at her sides, the long black coat swinging.',
  'Camera behind her at the height of the box, 85mm lens, f/5.6, square to the end face of the box. The end face of the box sits on the centre line on top of her head, square to the camera, filling about 30 percent of the frame width, sharp; her auburn hair tucked low under it, her shoulders and the black coat below; the pale stone street ahead; her long shadow stretches beside her.',
  'coat','She is seen from behind; only the back of her head, her shoulders and the coat are in frame, in exactly the outfit from the reference.',
  'THE END FACE OF THE BOX IS PLAIN MATTE WARM IVORY BOARD, flat, crisp corners, '+BL+'.'),
 {**sh(3,'top-down-seated-in-grid-of-six-boxes',[],
  'In a sunlit pale stone courtyard she sits cross-legged on the ground inside a neat grid of six identical ribbon-tied clothing boxes, laid two by three around her.',
  'Camera straight down from high above, 35mm lens, f/8. The six box lids lie in a precise grid, edges parallel to the frame; the centre-front box sits on the centre line, its lid filling about 25 percent of the frame width, sharp; she sits among them seen from directly above, the satin slip and cardigan pooling around her crossed legs, the top of her auburn head; crisp shadows of the boxes fall the same way across the stone.',
  'slip','She is seen from directly above; only the top of her head, her shoulders, arms and the outfit show, never her face, in exactly the outfit from the reference.',BOX),'comp':'B'},
 {**sh(4,'handover-of-bag-between-two-gloved-hands',['bag_atelier'],
  'On the sunlit street, her gloved hand passes our bag by its ribbon handles to another gloved hand reaching in from the other side.',
  'Close, 85mm lens, f/5.6, square to the bag front. The bag hangs on the centre line between the two hands, front square to the camera, filling about 45 percent of the frame width, sharp; her black gloved hand and coat sleeve from the left hold the handles, the other black gloved hand in a pale grey wool sleeve takes them from the right; pale stone wall behind with a hard shadow.',
  'coat','Only two gloved hands and the ends of their sleeves are in frame: hers in exactly the black coat from the reference, the other in a plain pale grey wool sleeve.'+GLOVE,BAG),'comp':'D'},
 sh(5,'twirl-in-shirt-dress-flash-frozen-bag',['bag_atelier'],
  'She twirls on the sunlit stone, the white shirt dress flaring; the photographer drags the shutter and fires a flash, so the dress and her legs smear into soft motion while our bag held out at her side is frozen sharp.',
  'Technique: slow shutter with a flash. Camera at the height of the bag, 50mm lens, square to the bag front. The bag is frozen dead sharp on the centre line, front square to the camera, filling about 35 percent of the frame width; around it the white poplin and her legs leave soft streaks of motion against the pale stone; hard sun; frame cropped at her shoulders.',
  'shirt','Her body from the shoulders down is in frame, mid-turn, in exactly the outfit from the reference.',BAG),
 sh(6,'bag-on-roof-of-black-car-gloved-hand-on-door',['bag_atelier'],
  'Our bag stands upright on the roof of a polished black car parked on the sunlit stone street; her gloved hand is on the door handle, about to open it.',
  'Camera at roof height, 50mm lens, f/5.6, square to the bag front. The bag stands on the black roof on the centre line, front square to the camera, filling about 40 percent of the frame width, sharp, its reflection soft in the glossy paint; the top edge of the car window and door below; her gloved hand and coat sleeve on the door at one side; pale stone facade behind.',
  'coat','Only her gloved hand and coat sleeve are in frame at one side, in exactly the outfit from the reference.'+GLOVE,BAG),
 sh(7,'three-identical-bags-in-row-on-steps-crossed-legs',['bag_atelier'],
  'Three identical bags stand in a neat row on a wide pale stone step; she sits on the step above, legs crossed, the satin slip falling beside them.',
  'Camera low at bag height, 50mm lens, f/5.6, square to the bags. The three bags stand evenly spaced, the middle one on the centre line, front square to the camera, filling about 30 percent of the frame width, all sharp; her crossed legs and ivory mules above and to one side; hard stepped shadows.',
  'slip','Her body from the waist down is in frame, seated, in exactly the outfit from the reference.',
  'EVERY BAG FRONT IS PLAIN MATTE PAPER-WHITE BOARD, flat with crisp folded edges and a deep folded top cuff, '+BL+'.'),
 {**sh(8,'invitations-one-per-step-top-down-staircase',[],
  'Looking straight down a wide pale stone staircase in the sun: one show invitation card lies on each step in a straight line; the tips of her black pointed boots stand on the top step.',
  'Camera straight down from above the staircase, 35mm lens, f/8. The steps run across the frame as bands of light and shadow; one card lies flat on each step on the centre line, edges parallel to the frame; the middle card is the hero, filling about 25 percent of the frame width, sharp; her boot tips and the coat hem at the top edge.',
  'coat','Only the tips of her boots and the coat hem are in frame at the top edge, in exactly the outfit from the reference.',CARD),'comp':'B'},
]
