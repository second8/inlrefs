# n28 Atelier round 16 (Sam 19 Oct): all five r15 finals; 'need more elegant, more chic, more high fashion'.
# Same world, light and grade; elevate styling: poise, long coat line, graceful gloved hands, generous pale stone negative space. Kit items: bag, invitation, clothing box, garment cover, hang tag.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour');r15=_m('n28r15_kit2')
C=dict(r15.C);C['id']='n28r16'
C['register']='A high-fashion luxury campaign photograph, elegant, chic and poised, in soft muted colour, made on a quiet stone street in hard midday sun'
C['finish']=C['finish']+(' Styled like a top fashion house campaign: poised, unhurried posture, the long clean line of the coat, slender hands with relaxed, graceful fingers, '
                         'generous calm negative space of pale stone, quiet and expensive, never casual or snapshot-like.')
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD,TAG,GC=r11.CARD,r11.TAG,r11.GC
GLOVE=' She wears thin, fitted black leather gloves.'
S=[
 sh(1,'bag-from-fingertips-against-stone-column',['bag_atelier'],
  'She stands still and upright against a pale fluted stone column, the long black coat falling straight, our bag hanging lightly from the fingertips of one lowered hand.',
  'Camera at bag height, 85mm lens, f/5.6, square to the bag. Framed from her shoulder to just below the knee: the long vertical line of the coat on one side, the pale column and stone wall filling the rest with calm empty space; the bag front on the centre line, square to the camera, filling about 40 percent of the frame width, sharp, its ribbon handles over her relaxed fingers; a long hard diagonal shadow on the stone beside it.',
  'coat','Only her body from the shoulder to below the knee is in frame, in exactly the outfit from the reference.',BAG),
 {**sh(2,'invitation-in-gloved-hand-against-coat-lapel',[],
  'She holds a show invitation card flat against the wide black lapel of the coat with one gloved hand, fingers resting lightly at its edge.',
  'Very close, 85mm lens, f/5.6, square to the card. The card sits on the centre line, flat against the black wool, its face square to the camera, filling about 45 percent of the frame width, sharp, at its true size; two gloved fingertips touch one edge; the soft fold of the black lapel and a sliver of pale stone behind; hard sun from the side carves the wool.',
  'coat','Only her gloved hand and the coat front from the collar to the chest are in frame, in exactly the outfit from the reference.'+GLOVE,CARD),'comp':'D'},
 sh(3,'clothing-box-on-knee-seated-stone-steps',[],
  'She sits on wide pale stone steps with her legs crossed, a flat clothing box resting upright on her knee, held lightly with one hand.',
  'Camera at the height of the box, 85mm lens, f/5.6, square to it. The box lid faces the camera on the centre line, filling about 45 percent of the frame width, sharp; the long black coat drapes over the step around her crossed legs; one black pointed boot extends elegantly at the lower edge; the empty pale steps rise behind in hard sun with crisp horizontal shadows.',
  'coat','Only her body from the waist down and one hand are in frame, seated, in exactly the outfit from the reference.',
  'THE BOX LID IS PLAIN MATTE WARM IVORY BOARD with a slim espresso grosgrain ribbon around it at one end, flat, crisp corners, '+BL+'.'),
 sh(4,'garment-cover-over-shoulder-walking-away-colonnade',['gcover'],
  'She walks away from the camera down a long pale stone colonnade, our garment cover carried over one shoulder by its hanger hook, hanging straight down her back.',
  'Camera behind her at shoulder height, 85mm lens, f/5.6, square to the cover. The front panel of the garment cover hangs flat down her back on the centre line, square to the camera, filling about 45 percent of the frame width, sharp; her auburn hair tucked low above it; the columns repeat into the distance with hard bars of sun and shadow across the floor; calm and symmetric.',
  'coat','She is seen from behind; only the back of her head with the hair tucked low, her shoulders and the coat are in frame, in exactly the outfit from the reference.',GC),
 {**sh(5,'gloved-hand-turns-coat-cuff-hang-tag',['hangtag'],
  'With one gloved hand she turns back the cuff of the long black coat on her other wrist, revealing our hang tag on its cord.',
  'Very close, 100mm lens, f/5.6, square to the tag. The hang tag sits on the centre line, flat to the camera, filling about 40 percent of the frame width, sharp, its cord looped to the cuff; the folded black wool cuff and the two gloved hands frame it; a sliver of pale stone in hard sun behind.',
  'coat','Only her two gloved hands and the coat cuff are in frame, in exactly the outfit from the reference.'+GLOVE,TAG),'comp':'D'},
]
