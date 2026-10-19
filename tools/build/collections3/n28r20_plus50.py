# n28 Atelier round 20 (Sam 19 Oct): r19 both finals. 'Nice, all is being even better. So +50 creativity now in 6 new images.' Same world and grade, high-fashion poses, mixed outfits.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour');r16=_m('n28r16_chic')
C=dict(r16.C);C['id']='n28r20'
sh,BAG,GC,CARD,TAG,GLOVE=r4.sh,r4.BAG,r11.GC,r11.CARD,r11.TAG,r16.GLOVE
S=[
 sh(1,'leap-off-step-coat-flaring-bag-frozen',['bag_atelier'],
  'She leaps off the bottom pale stone step in full sun; the long black coat flares out behind her and our bag swings out at her side, everything frozen in mid-air.',
  'Camera at the height of the bag, 50mm lens, f/8, fast shutter, square to the bag front. The bag hangs frozen in the air on the centre line, front square to the camera, filling about 35 percent of the frame width, dead sharp; around it the flaring black coat, her legs mid-leap with pointed boots off the ground, and her sharp shadow on the stone below; the steps behind; frame cropped at her shoulders.',
  'coat','Her body from the shoulders down is in frame mid-leap, in exactly the outfit from the reference.',BAG),
 {**sh(2,'lying-on-warm-stone-invitation-on-chest-top-down',[],
  'She lies on her back on the warm pale stone pavement in the long black coat, her gloved hands holding a show invitation card flat on her chest.',
  'Camera straight down from above, 50mm lens, f/8. Her figure in the black coat lies diagonally across the pale stone; the card sits flat on her chest on the centre line, face up and square to the camera, filling about 35 percent of the frame width, sharp; her two gloved hands rest at its edges; the frame is cropped just below her chin; her hard shadow hugs her along one side.',
  'coat','Only her body from just below the chin down to the waist is in frame, lying down, in exactly the outfit from the reference; her face is outside the frame.'+GLOVE,CARD),'comp':'B'},
 sh(3,'bag-tossed-over-shoulder-mid-turn-from-behind',['bag_atelier'],
  'Seen from behind, she walks away and flings our bag back over her shoulder mid-turn; the bag hangs frozen in the air behind her shoulder, its front facing us.',
  'Camera behind her at shoulder height, 85mm lens, f/8, fast shutter, square to the bag front. The bag hangs frozen in the air just behind her shoulder on the centre line, front square to the camera, filling about 35 percent of the frame width, sharp; her back in the white shirt dress, the slim black belt and her auburn hair tucked low; the sunlit pale stone street ahead of her.',
  'shirt','She is seen from behind; only the back of her head with the hair tucked low, her back and her raised arm are in frame, in exactly the outfit from the reference.',BAG),
 {**sh(4,'blade-of-sun-in-dark-passage-hang-tag',['hangtag'],
  'In a narrow dark stone passage, one thin blade of sunlight falls through a gap between the buildings and lights only her gloved hand holding our hang tag; everything else is deep shadow.',
  'Camera at the height of the tag, 85mm lens, f/5.6, square to it. The hang tag sits on the centre line in the shaft of hard sun, flat to the camera, filling about 35 percent of the frame width, sharp and bright; her gloved fingers hold its cord; the black coat sleeve dissolves into the dark; the edges of the light shaft are crisp; the rest of the frame falls to deep shadow with only faint stone texture.',
  'coat','Only her gloved hand and the end of the coat sleeve are in frame.'+GLOVE,TAG),'comp':'D'},
 sh(5,'seated-fountain-rim-legs-crossed-garment-cover',['gcover'],
  'She sits on the wide rim of a pale stone fountain basin in the sun, legs crossed high, leaning back on one hand; our garment cover lies flat along the stone rim beside her.',
  'Camera at the height of the rim, 50mm lens, f/5.6, square to the garment cover panel. The cover lies flat along the rim on the centre line, its front panel square to the camera, filling about 40 percent of the frame width, sharp; beside it her crossed legs and the satin slip spilling over the stone; a sliver of still water behind with sun glints; frame cropped at her shoulders.',
  'slip','Her body from the shoulders down is in frame in a relaxed, elegant high-fashion pose, in exactly the outfit from the reference.',GC),
 sh(6,'tiptoe-on-step-edge-bag-behind-calves',['bag_atelier'],
  'She stands on tiptoe right on the edge of a pale stone step in black slingback heels; our bag hangs from one finger of her lowered hand just behind her calves.',
  'Camera low at calf height, 50mm lens, f/5.6, square to the bag front. The bag hangs on the centre line behind and between her legs, front square to the camera, filling about 40 percent of the frame width, sharp; her bare ankles and calves, the heels lifted off the step edge, the hem of the white shirt dress at the top edge; long hard shadows of her legs fall down the steps.',
  'shirt','Only her legs from the knee down, the hem of the dress and one hand are in frame, in exactly the outfit from the reference.',BAG),
]
