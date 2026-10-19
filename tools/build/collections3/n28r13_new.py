# n28 Atelier round 13 (Sam 19 Oct): r12 finals 01, 03, 04, 05; 02 (bag on glass shelf) 'glass just to use glass'; 'don't overdo glass anymore';
# 'now don't get lazy, I need new ideas, new things, not repeating. We did those.' Same world (hard sun, pale stone, soft colour), all-new objects and moments.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour')
C=dict(r11.C);C['id']='n28r13'
C['world']='A city street at midday: pale weathered stone walls, smooth pavement, deep doorways, a quiet pavement cafe; nothing else unless the shot names it.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD=r11.CARD
S=[
 {**sh(1,'show-poster-pasted-on-stone-wall-shadow-passing',[],
  'A show poster is pasted flat on a sunlit pale stone wall; she walks past it in the long black coat and her hard shadow falls across the wall beside it.',
  'Camera straight on to the wall, 50mm lens, f/8. The poster sits on the centre line, square to the camera, filling about 50 percent of the frame width, sharp, pasted flat with a few tiny real wrinkles at its edges; her long hard shadow crosses the stone to its left, never over it; only the edge of her black coat and one boot pass at the left frame edge.',
  'coat','Only the edge of her coat and one boot are in frame at the left edge, in exactly the outfit from the reference.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted flat on the stone, crisp edges, nothing printed on it and nothing crossing it.'),'comp':'A'},
 {**sh(2,'lookbook-open-in-hands-cafe-table',[],
  'At a sunlit pavement cafe table she holds a softcover lookbook open in both hands, looking through it.',
  'Camera from just above her shoulder line, looking down at the book, 50mm lens, f/5.6, square to the open spread. The open spread fills about 60 percent of the frame width, its two pages flat and square to the camera, sharp; her fingers hold its outer edges; the small round cafe table and a white cup soft at the lower edge; hard sun and the shadow of an awning edge across the table beside the book.',
  'slip','Only her hands, wrists and the cardigan cuffs are in frame, in exactly the outfit from the reference.',
  'THE OPEN SPREAD IS TWO PLAIN MATTE PAPER-WHITE PAGES, flat with a soft gutter, crisp outer edges, nothing printed on them.'),'comp':'D'},
 sh(3,'bag-on-car-back-seat-door-open-sun',['bag_atelier'],
  'Our bag sits upright on the cream leather back seat of a car with its door open on a sunlit street; her hand reaches in for the handles.',
  'Camera at the open door at seat height, 35mm lens, f/5.6, square to the bag. The bag fills about 45 percent of the frame width on the seat, front square to the camera, sharp; the stitched cream leather seat and the dark door frame around it; hard sun rakes in through the far window across the seat; her hand in the black coat sleeve enters from the right edge toward the handles.',
  'coat','Only her hand and the end of the coat sleeve enter from the right edge, in exactly the outfit from the reference.',BAG),
 sh(4,'invitation-passed-hand-to-hand-in-sun',[],
  'In hard sun on the street, her hand passes a show invitation card to another person\'s hand.',
  'Very close, 85mm lens, f/5.6, square to the card. The card sits on the centre line between two hands, its face square to the camera, filling about 40 percent of the frame width, sharp, at its true size; her fingers at one side in the black coat sleeve, the other person\'s fingers in a grey wool sleeve taking it at the other side; soft pale stone behind.',
  'coat','Only two hands and the ends of their sleeves are in frame: hers in exactly the black coat from the reference, the other in a plain grey wool sleeve.',CARD),
 sh(5,'bag-on-cafe-chair-water-glass-caustic',['bag_atelier'],
  'At a sunlit pavement cafe our bag stands on a woven cafe chair beside a small round pale stone-top cafe table with a glass of water on it.',
  'Camera at bag height, 50mm lens, f/5.6, square to the bag. The bag stands on the chair seat on the centre line, front square to the camera, filling about 45 percent of the frame width, sharp; on the table edge beside it the glass of water throws a small bright caustic of sunlight onto the tabletop, never onto the bag; her legs in the satin hem and mules at the edge of the frame.',
  'slip','Only her legs from the knee down are in frame at the edge, seated, in exactly the outfit from the reference.',BAG),
]
