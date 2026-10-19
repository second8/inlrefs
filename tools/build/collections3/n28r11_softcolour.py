# n28 Atelier round 11 (Sam 19 Oct): r10 finals 01, 03, 04, 05 ('amazing', 'really really nice, keep in mind proportions and scales', 'works great').
# r10-02 (seated on steps, bag by boots) 'something looks AI'. Keep r10 world and soft colour; real scale; nothing staged. Words only, no inspo images.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r10=_m('n28r10_softcolour')
C=dict(r10.C);C['id']='n28r11'
C['real']=r10.C['real']+' Every object is at its true real-world size next to her hands and body; nothing is enlarged for the camera.'
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD=r10.CARD;TAG=r10.TAG
GC='THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'
S=[
 sh(1,'bag-hooked-over-forearm-stone-balustrade',['bag_atelier'],
  'She stands by a sunlit stone balustrade in the long black coat, our bag hooked over her bent forearm by its ribbon handles.',
  'Camera at waist height, 50mm lens, f/8, straight on. The frame runs from her chest to her hip; the bag hangs from her forearm on the right of centre, its front square to the camera, filling about 40 percent of the frame width, sharp and sunlit, at its true size against her arm; the pale stone balustrade behind casts a row of hard shadows across the pavement.',
  'coat','Only her body from the chest to the hip, her bent arm and hand are in frame, in exactly the outfit from the reference.',BAG),
 {'n':2,'slug':'garment-cover-on-hook-sunlit-stone-doorway','kind':'print','noun':'the design surface','refs':['gcover'],'comp':'C','people':'none',
  'moment':'Our garment cover hangs alone on a simple brass hook inside a sunlit pale stone doorway, just delivered.',
  'shot':'Camera straight on at the height of the cover, 50mm lens, f/8. The stone door frame forms an even margin around it; the cover hangs on the centre line, its front panel square to the camera, filling about 60 percent of the frame height, sharp; a hard band of sun falls across the doorway floor and the lower stone, the deep interior behind falling to shadow.',
  'surface':GC},
 sh(3,'invitation-between-fingers-at-side-mid-stride',[],
  'Mid-stride along a sunlit stone street in the long black coat, she holds a show invitation card loosely between two fingers at her side.',
  'Camera at hip height, 50mm lens, f/8, side on. The frame runs from her waist to her knee; the card hangs from her fingertips on the centre line, its face square to the camera, filling about 30 percent of the frame width, sharp and sunlit, at its true small size against her hand; the black coat moves behind it; her long shadow on the pale pavement.',
  'coat','Only her body from the waist to the knee and her hand are in frame, side on, in exactly the outfit from the reference.',CARD),
 {'n':4,'slug':'bag-on-stone-ledge-hang-tag-on-handle','kind':'print','noun':'the design surface','refs':['bag_atelier','hangtag'],'people':'none',
  'moment':'Our bag stands on a sunlit stone window ledge, our small hang tag tied to one of its ribbon handles.',
  'shot':'Camera straight on at bag height, 50mm lens, f/8. The bag stands on the centre line, its front square to the camera, filling about 55 percent of the frame width, sharp; the hang tag hangs from the handle at its true small size, about the size of a business card against the bag; the window recess behind it in soft shadow; a hard diagonal shadow from the window frame falls on the ledge beside the bag, never over it.',
  'surface':BAG},
 {**sh(5,'garment-cover-past-fluted-shop-glass',['gcover'],
  'She stands outside a shop with a fluted glass window in hard sun, holding our garment cover up by its hanger hook; the photographer shoots past the edge of the fluted glass.',
  'The left third of the frame is the fluted glass close to the lens, breaking her black coat and arm into repeated vertical slices with bright sun edges; the garment cover hangs in the clear part of the frame, its front panel square to the camera, filling about 50 percent of the frame height, dead sharp, never behind the glass. Hard sun from the right. 50mm lens, camera at the height of the cover.',
  'coat','Only her raised hand, arm and the coat from the shoulder down are in frame, in exactly the outfit from the reference.',GC)},
]
