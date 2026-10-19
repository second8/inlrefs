# n28 Atelier round 12 (Sam 19 Oct): r11 finals 02, 03 ('amazing'), 04, 05; 01 'really fine'; 02 'a bit unnatural but works'.
# 'Bring glass more now, don't overdo it, but use it creatively.' Same r10/r11 world (hard sun, pale stone, soft colour); glass belongs to the street; design surface clear of it.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r11=_m('n28r11_softcolour')
C=dict(r11.C);C['id']='n28r12'
C['world']='A city street at midday: pale weathered stone walls, smooth pavement, deep doorways, and the glass of its old shopfronts (fluted glass, clear display glass, thick glass blocks); nothing else unless the shot names it.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD=r11.CARD;TAG=r11.TAG;GC=r11.GC
CLEAR=' The design surface itself is never behind or under the glass and no refracted light crosses it: it sits in the clear, sharp, single and undistorted.'
S=[
 sh(1,'invitation-in-gap-between-fluted-glass-doors',[],
  'She holds a show invitation card up in the narrow open gap between two fluted glass shop doors in hard sun.',
  'Camera straight on at card height, 50mm lens, f/5.6. The two fluted glass doors fill the left and right of the frame, breaking her black coat and hand behind them into soft vertical slices with bright sun edges; in the clear gap between them her fingers hold the card on the centre line, its face square to the camera, filling about 35 percent of the frame width, sharp, at its true size against her hand.'+CLEAR,
  'coat','Only her hand, wrist and the coat behind the glass are in frame, in exactly the outfit from the reference.',CARD),
 {'n':2,'slug':'bag-on-glass-shelf-shop-window','kind':'print','noun':'the design surface','refs':['bag_atelier'],'comp':'A','people':'none',
  'moment':'Our bag stands on a clear glass shelf in a shop-window display, seen from the sunlit street.',
  'shot':'Camera outside, straight on at bag height, 50mm lens, f/5.6, close to the window. The bag stands on the centre line on the thick clear glass shelf, its front square to the camera, filling about 50 percent of the frame width, sharp, its soft shadow and the green edge of the glass shelf below it; faint reflections of the sunlit street sit only at the outer edges of the window, never over the bag; the shop interior behind in soft shade.'+CLEAR,
  'surface':BAG},
 {**sh(3,'hang-tag-on-cuff-by-glass-block-caustics',['hangtag'],
  'Her hand rests against a sunlit stone wall beside a panel of thick glass blocks; our hang tag hangs from her coat cuff.',
  'Medium close, 85mm lens, f/5.6, square to the tag. Her hand, wrist and the black coat cuff fill the lower part of the frame; the tag hangs at its natural small size, filling about 25 percent of the frame height, sharp and in plain sun; beside it on the pale stone, sun passing through the glass blocks throws a soft rippling caustic pattern of light, never touching the tag.'+CLEAR,
  'coat','Only her hand, wrist and the coat cuff are in frame, in exactly the outfit from the reference.',TAG)},
 {'n':4,'slug':'garment-cover-before-glass-brick-wall','kind':'print','noun':'the design surface','refs':['gcover'],'comp':'A','people':'none',
  'moment':'Our garment cover hangs on a slim black hook in front of a sunlit wall of old glass bricks in a stone passage.',
  'shot':'Camera straight on at the height of the cover, 50mm lens, f/5.6. The wall of square glass bricks fills the background edge to edge, glowing softly with sun from the other side, its grid running parallel to the frame; the cover hangs on the centre line in front of it, its front panel square to the camera, filling about 60 percent of the frame height, sharp and opaque, lit from the front by the sunny passage.'+CLEAR,
  'surface':GC},
 {**sh(5,'invitation-on-ledge-glass-caustic-top-down',['tissue'],
  'A show invitation card lies in opened ivory tissue on a sunlit stone ledge beside a glass-block window; her hand rests at the edge of the frame.',
  'Camera straight down, 50mm lens, f/8. The card lies flat, its edges parallel to the frame, filling about 50 percent of the frame width, sharp; the soft tissue around it; beside the card, never on it, sun through the glass blocks throws a bright rippling caustic pattern across the pale stone; her fingers in the black coat sleeve at the lower edge.'+CLEAR,
  'coat','Only her fingers and the end of the coat sleeve are in frame, in exactly the outfit from the reference.',CARD),'comp':'B'},
]
