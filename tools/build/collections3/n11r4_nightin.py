# n11 round 3 (third look). Sam: too much dead space, should be vertical; bad framing; "poverty wall" (bare cheap walls); a glass on the
# bed makes no sense; 02 (nightstand from above) works but less staged, more candid. Final so far: n11-25 book on nightstand.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n11r3_nightin.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C.update({'id':'n11r4','name':'Night In (round 3)','aspect':'4:5','format_words':'portrait 4:5'})
C['world']='A well-kept, well-designed city apartment at night: deep walnut nightstand, rumpled oatmeal linen on a low bed, a brown corduroy sofa with a grey wool throw. Walls are rarely seen; when they are, they are warm limewash plaster with a wooden picture rail or oak panelling, never bare or cheap. A little real life: a book, a charging cable. Mostly dark; only a small part of the room is ever in frame.'
C['avoid']=_m.C['avoid']+['bare cheap walls or empty space around the subject','a glass placed on the bed or sheets']
I2=_m.I2;I3=_m.I3;FILM=_m.FILM
S=[
 {'n':1,'slug':'phone-in-hands-bed-close','kind':'phone','refs':['phone'],'people':'her','edge':'bottom','looks':[(I3,FILM)],
  'moment':'Late in bed, she holds her phone close in both hands, reading.',
  'shot':'Tight, 50mm, f/2, from just beside her at chest height. Her two hands hold the phone, filling about 55 percent of the frame height, sharp, screen toward camera; the oatmeal duvet folds fill the rest of the frame, the bedside lamp a warm glow at the top edge. No wall in frame.'},
 {'n':2,'slug':'phone-nightstand-candid','kind':'phone','refs':['phone'],'people':'none','looks':[(I2,FILM+', and its top-down camera')],
  'moment':'Her phone on the walnut nightstand, put down without thinking, cable still trailing.',
  'shot':'Directly top-down, tight, 50mm, f/2.8. The phone lies slightly skewed on the walnut top, filling about 55 percent of the frame height, sharp; a charging cable trails loosely off one side and a closed paperback sits half in frame at the edge. Warm lamp light falls across one corner; nothing else.'},
 {'n':3,'slug':'ipad-lap-corduroy','kind':'ipad','refs':['ipad'],'people':'her','edge':'bottom','looks':[(I3,FILM)],
  'moment':'Curled into the corduroy sofa, she reads on a tablet resting on her lap.',
  'shot':'Tight, 50mm, f/2, from above her shoulder line looking down. The tablet rests on her lap, filling about 60 percent of the frame height, sharp; her hands hold its lower edge; brown corduroy and the grey wool throw fill the edges. The floor lamp makes a small warm pool at one corner; everything else is dark.'},
 {'n':4,'slug':'book-under-lamp','kind':'print','noun':'the book cover','refs':[],'people':'none','looks':[(I2,FILM)],
  'moment':'A closed hardback left on the walnut nightstand right under the reading lamp.',
  'shot':'Tight, 50mm, f/2.8, from standing beside the bed, looking down at about 55 degrees. The hardback lies flat, filling about 60 percent of the frame height, sharp, in the lamp pool; the lamp base crops in softly at the top corner and the linen edge at the bottom.',
  'surface':'THE BOOK COVER IS PLAIN BLANK WHITE linen-textured board, lying flat, crisp corners, nothing printed on it.'},
 {'n':5,'slug':'laptop-on-duvet-night','kind':'laptop','refs':['laptop'],'people':'none','looks':[(I3,FILM)],
  'moment':'A laptop left open on the rumpled duvet late at night, the only bright thing in the room.',
  'shot':'Tight three-quarter, 50mm, f/2, from the edge of the bed at mattress height. The open laptop sits slightly tilted on the duvet folds, filling about 60 percent of the frame width, sharp; the oatmeal linen catches its light; the headboard and the room behind are near black, no wall visible.'},
]
