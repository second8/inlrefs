# c4 round 8. Sam on r7: all four work (finals); wall too bright on 01; retire phone, posters, card on travertine. New props 38-39 + pr05 cup + pr06 tote.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c4r7_beam.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
R2_1=_m.R2_1;R2_2=_m.R2_2;LOOK=_m.LOOK
C=dict(_m.C);C['id']='c4r8';C['name']='Beam (round 8)'
C['world_short']='A dim old apartment: wide honey-oak floorboards, deep charcoal limewash walls that stay dark even near the sun, deep windows with slim dark mullions. Only where the sun lands is anything bright.'
C['avoid']=_m.C['avoid']+['a phone','a poster or framed print','a bright or washed-out wall']
S=[
 {'n':1,'slug':'tote-oak-peg-rail-sun-band','kind':'print','noun':'the tote bag front','refs':['pr06','peg_rail'],'people':'none','comp':'A','looks':[(R2_2,LOOK)],
  'moment':'Our plain canvas tote hanging from one peg of the oak peg rail, a single band of late sun falling across it on the dark wall.',
  'shot':'Straight on, camera exactly at the centre of the tote, 50mm, f/2.8, close. The rail runs level across the top of the frame; the tote hangs on the centre line from the middle peg, its front panel facing the camera dead square, filling about 65 percent of the frame height, sharp and fully in the sun band. The charcoal wall around stays deep and dark, the mullion shadows soft at the edges.',
  'surface':'THE TOTE FRONT IS PLAIN NATURAL OFF-WHITE CANVAS, hanging flat and smooth with only a soft natural drape near the handles, a clear woven texture, nothing printed on it.','avoid':['a coat or other bags','a logo on the tote']},
 {'n':2,'slug':'watch-oak-stand-sun-tight','kind':'watch','refs':['watch','watch_stand'],'people':'none','comp':'D','looks':[(R2_1,LOOK)],
  'moment':'A smartwatch resting on our small oak watch stand on the deep oak sill, its face catching the last hard sun.',
  'shot':'Straight on, very close, 90mm macro, f/4, camera exactly at the watch face. The watch face looks dead square at the camera on the centre line, filling about 50 percent of the frame height, sharp; the band wraps the rounded oak upright, the base sits on the sill. One hard edge of sun crosses the sill below; the wall behind is near black.'},
 {'n':3,'slug':'ceramic-cup-oak-sill-hard-sun','kind':'print','noun':'the cup','refs':['pr05'],'people':'none','comp':'A','looks':[(R2_1,LOOK)],
  'moment':'One plain white ceramic cup standing alone on the deep oak window sill in hard late sun.',
  'shot':'Straight on, camera exactly at the height of the cup, 85mm, f/2.8, close. The cup stands on the centre line, its handle turned to the side, its facing side square to the camera, filling about 55 percent of the frame height, sharp. The sun throws one long crisp shadow of the cup across the oak; the mullion shadows lie on the sill to one side; the wall behind stays dark.',
  'surface':'THE FACING SIDE OF THE CUP IS PLAIN SMOOTH GLOSS WHITE CERAMIC, clean, nothing printed on it, with one soft natural highlight at the edge only.','avoid':['a saucer','a takeaway cup','steam or coffee','a spoon']},
]
