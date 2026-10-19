# c4 round 4. Sam: r3-01 and r3-04 are finals. r3-02 (laptop + cushion on the floor) makes no sense; r3-03 too much room, bad angle;
# r3-05 repeats a laptop we have. "We need new, more creative prompts." Brighter screens in all. Same room, no inspo images.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c4r3_beam.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c4r4';C['name']='Beam (round 4)'
C['avoid']=_m.C['avoid'][:5]+['a wide view of the room']
S=[
 {'n':1,'slug':'display-sideboard-beam-wall','kind':'display','refs':['display'],'people':'none',
  'moment':'A desktop display stands on a low oak sideboard against the charcoal wall, a beam of late sun crossing the wall beside it.',
  'shot':'Three-quarter from the left at standing height, 50mm, f/2.8, close. The display fills about 60 percent of the frame width on the oak sideboard top, sharp. A sharp-edged band of sun falls diagonally across the limewash wall just to its right and onto the sideboard; everything else is deep charcoal shadow. A short stack of two closed hardback books lies flat at the left edge, soft.'},
 {'n':2,'slug':'tablet-on-book-stand','kind':'ipad','refs':['ipad'],'people':'none',
  'moment':'A tablet rests upright on a small oak book stand on the bench, catching the edge of the sun.',
  'shot':'Close, 50mm, f/2.8, at bench height, slightly from the right. The tablet stands in a simple low oak book stand on the worn oak bench top, filling about 65 percent of the frame height, sharp. The sun lands across the bench in front of it and on the lower edge of the stand, with one crisp mullion shadow line; behind is near-black charcoal wall.'},
 {'n':3,'slug':'phone-on-open-book','kind':'phone','refs':['phone'],'people':'none',
  'moment':'A phone left face up on an open hardback book on the bench, in a patch of late sun.',
  'shot':'From standing, looking down at about 55 degrees, 50mm, f/2.8. The phone lies on the open pages of a large hardback book on the oak bench, filling about 50 percent of the frame height, sharp; the pages are plain cream with soft text-free tone. A mullion shadow crosses the book beside the phone but never the screen; the bench edge falls into shadow.'},
 {'n':4,'slug':'poster-pinned-wall-mullion','kind':'print','noun':'the poster','refs':[],'people':'none',
  'moment':'A large unframed poster pinned to the charcoal limewash wall, the window grid of late sun sliding across it.',
  'shot':'Frontal and slightly off-axis, 50mm, f/2.8, at eye height, close. The portrait poster on the wall fills about 70 percent of the frame height, sharp, held flat by four small brass pins. A broken grid of mullion shadows lies across its lower half; the wall around it falls to deep charcoal; a sliver of the oak floor at the very bottom.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE heavy matte paper lying perfectly flat against the wall, crisp square corners, nothing printed on it.','avoid':['a curled or lifted corner','a frame or glass']},
 {'n':5,'slug':'watch-on-sill-sun','kind':'watch','refs':['watch'],'people':'none',
  'moment':'A watch taken off and left face up on the deep oak window sill as the sun comes in low.',
  'shot':'Macro-close, 90mm, f/2.8, from standing at the sill. The watch lies on its back on the oak sill in the sun patch, band curled naturally, the case filling about 45 percent of the frame width, sharp; a slim mullion shadow falls across the sill beside it. The window reveal is dark brown and soft behind.'},
]
