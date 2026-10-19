# c4 round 6, agreed with Sam 16 Oct 17:11 ("go"). Wins r5: 01 laptop bench, 04 tablet seat, 05 poster bench: one object, one surface,
# sun grid, no scenery. Fails: 03 display named window/rooftops -> wide and angled; 02 another laptop. No laptops this round.
# Object-first moment lines, no scenery, no people.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c4r5_beam.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
R2_1=_m.R2_1;R2_2=_m.R2_2;LOOK=_m.LOOK
C=dict(_m.C);C['id']='c4r6';C['name']='Beam (round 6)'
C['avoid']=_m.C['avoid']+['a window view, sky or rooftops']
S=[
 {'n':1,'slug':'display-on-oak-bench-sun-wall','kind':'display','refs':['display','bench_oak'],'people':'none','looks':[(R2_2,LOOK)],
  'moment':'A desktop display standing on the low oak bench against the charcoal wall, hard late sun falling in a window grid on the wall beside it.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/2.8, close. The display faces the camera dead square, filling about 70 percent of the frame width, sharp. The bench top runs across the bottom of the frame; the sun grid lands on the wall to one side, never on the screen. Everything else falls to near black.'},
 {'n':2,'slug':'magazine-spread-window-seat-top-down','kind':'print','noun':'the open magazine spread','refs':[],'people':'none','looks':[(R2_1,LOOK)],
  'moment':'An open magazine lying flat on the oak window seat, the late sun laying a window grid across the seat beside it.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The open spread lies flat and square to the frame, filling about 75 percent of the frame width, sharp. The sun grid crosses the oak beside it but never the pages; the seat edge falls into shadow.',
  'surface':'BOTH PAGES OF THE SPREAD ARE PLAIN BLANK WHITE matte paper, lying flat with only a soft dip at the centre fold, crisp corners, nothing printed on them.','avoid':['a curled or lifted corner','text or images on the pages']},
 {'n':3,'slug':'phone-ochre-stool-top-down','kind':'phone','refs':['phone','stool_ochre'],'people':'none','looks':[(R2_1,LOOK)],
  'moment':'A phone lying face up on the top of the small ochre-lacquered stool, in a patch of hard late sun.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The phone lies flat and square to the frame on the stool top, filling about 60 percent of the frame height, sharp. The stool top is clearly ochre-yellow satin lacquer, not brown wood; one mullion shadow line crosses the lacquer beside the phone, never the screen. The floorboards around fall into shadow.'},
 {'n':4,'slug':'letterhead-card-oak-bench-top-down','kind':'print','noun':'the letterhead and business card','refs':['bench_oak'],'people':'none','looks':[(R2_2,LOOK)],
  'moment':'A single letterhead sheet with one business card resting on its lower corner, lying on the oak bench top in the late sun.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The A4 sheet lies flat and square to the frame on the open-grain oak, filling about 70 percent of the frame height, sharp; the card overlaps its lower right corner. A sharp edge of sun crosses the oak beside the sheet; the rest of the bench falls into shadow.',
  'surface':'THE SHEET AND THE CARD ARE PLAIN BLANK WHITE thick uncoated paper, lying perfectly flat, crisp square corners, nothing printed on them.','avoid':['a curled or lifted corner','a pen or any other object']},
 {'n':5,'slug':'hardcover-standing-oak-sill','kind':'print','noun':'the book cover','refs':[],'people':'none','looks':[(R2_2,LOOK)],
  'moment':'A closed hardcover book standing upright on the deep oak window sill, its front cover facing out, a beam of late sun on the charcoal wall beside it.',
  'shot':'Straight on, camera exactly at cover height, 50mm, f/2.8, close. The book stands face out, its front cover square to the camera, filling about 70 percent of the frame height, sharp. The sun lands on the wall beside it in a sharp-edged band; the sill edge runs across the bottom; the rest falls to near black.',
  'surface':'THE FRONT COVER IS PLAIN BLANK WHITE matte paper wrap, perfectly flat, crisp corners and a tight spine edge, nothing printed on it.','avoid':['other books','a curled or worn cover']},
]
