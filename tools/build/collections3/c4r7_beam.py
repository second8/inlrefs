# c4 round 7 (18:06 16 Oct). Sam: "dont over do shots", "be more intentional", new props OK (Grok props 27-29). Finals cover laptop x3,
# phone x2, tablet x2, book. Gaps: print in use, small print. Each shot: one of our props + one named composition + the sun as geometry.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c4r5_beam.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
R2_1=_m.R2_1;R2_2=_m.R2_2;LOOK=_m.LOOK
C=dict(_m.C);C['id']='c4r7';C['name']='Beam (round 7)'
C['world_short']='A dim old apartment: wide honey-oak floorboards, dark charcoal limewash walls, deep windows with slim dark mullions. Only where the sun lands is anything bright.'
C['avoid']=_m.C['avoid']+['a window view, sky or rooftops','a laptop']
S=[
 {'n':1,'slug':'poster-oak-easel-sun-rectangle','kind':'print','noun':'the poster','refs':['easel_oak'],'people':'none','comp':'A','looks':[(R2_2,LOOK)],
  'moment':'A large poster on thick board resting on our slim oak easel, standing exactly inside a tall rectangle of late sun on the charcoal wall.',
  'shot':'Straight on, camera at the centre of the poster, 50mm, f/2.8. The easel and poster stand on the centre line; the portrait poster faces the camera dead square, filling about 60 percent of the frame height, sharp, fully inside the bright sun rectangle. The mullion shadows fall on the wall and floor around it, never on the poster. The easel legs run down to the floorboards; the rest falls to near black.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE thick matte board, perfectly flat and rigid, crisp square corners, nothing printed on it.','avoid':['a curled or warped corner','a canvas or paint']},
 {'n':2,'slug':'phone-travertine-plinth-sun-patch','kind':'phone','refs':['phone','plinth_trav'],'people':'none','comp':'C','looks':[(R2_1,LOOK)],
  'moment':'A phone lying face up on the top of our travertine plinth, where one small square of late sun lands exactly on the stone.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The square plinth top fills the frame; a sharp square of sun lies on it with an even dark margin of stone around, and the phone lies inside that square, square to the frame, filling about 55 percent of the frame height, sharp. The open pores of the travertine show in the light; the margin falls into shadow.'},
 {'n':3,'slug':'framed-print-charcoal-wall-grid','kind':'print','noun':'the framed print','refs':[],'people':'none','comp':'A','looks':[(R2_2,LOOK)],
  'moment':'A framed print hung alone on the charcoal limewash wall, the late sun grid sliding across the wall beside it.',
  'shot':'Straight on, camera exactly at the centre of the print, 50mm, f/2.8, close. The portrait print in a thin honey-oak frame hangs on the centre line, facing the camera dead square, filling about 70 percent of the frame height, sharp and lit by the sun. The window-grid shadows fall on the wall to both sides in even bands; the mottled limewash texture shows; the corners fall to near black.',
  'surface':'THE PRINT IS PLAIN BLANK WHITE matte paper lying flat behind non-reflective glass, crisp edges, nothing printed on it.'},
 {'n':4,'slug':'card-travertine-vase-shadow','kind':'card','noun':'the business card','refs':['plinth_trav','vase_char'],'people':'none','comp':'B','looks':[(R2_1,LOOK)],
  'moment':'One business card lying on the travertine plinth top, the curved shadow of our charcoal vase falling across the stone beside it.',
  'shot':'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The single card lies square to the frame on the sunlit travertine, filling about 45 percent of the frame width, sharp. The vase stands just outside the frame; only its long soft curved shadow crosses the stone diagonally beside the card, never over it.',
  'surface':'THE CARD IS PLAIN BLANK WHITE thick uncoated card, lying perfectly flat, crisp square corners, nothing printed on it.','avoid':['a second card or paper','a pen']},
]
