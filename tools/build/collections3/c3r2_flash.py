# C3 round 3 (Sam on r2: 01 nice; 02 same as 01, more creative; 03/06 too far; watch overdone now; tablet-on-knee pose done;
# "need more props that go with this scene"). Night out props: tote (pr06), magazine, paper bag (45), record sleeve, cap (52), bike (79).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c3r_flash.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c3r2';C['name']='Flash (round 3)'
C['avoid']=_m.C['avoid']+['a watch','a person standing far from the camera']
PL=_m.PL;W=_m.W
BL='nothing printed on it'
def sh(n,slug,kind,noun,refs,comp,moment,shot,surface=None,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs+W,'people_line':PL,'comp':comp,'moment':moment,'shot':shot}
    if surface: d['surface']=surface
    d.update(kw);return d
S=[
 sh(1,'tote-on-shoulder-front-tight','print','the tote front',['pr06'],'D','Walking out at night, our canvas tote hangs from his shoulder, its front panel flat against his side.',
  'Straight on, very close, 35mm, f/8, camera square to the tote. The tote front fills about 70 percent of the frame height on the centre line, sharp; the strap runs up over the navy shoulder at the top edge; the cream vest and grey trousers frame it; hard flash shadow tight behind.',
  'THE TOTE FRONT IS PLAIN NATURAL OFF-WHITE CANVAS, hanging flat and smooth, clear weave, '+BL+'.'),
 sh(2,'magazine-cover-in-hand-by-thigh','print','the magazine cover',[],'D','Standing by the ribbed concrete wall, he holds a magazine loosely at his side by his thigh, cover facing out.',
  'Straight on, very close, 35mm, f/8, camera square to the cover. The magazine cover fills about 60 percent of the frame height on the centre line, sharp, his fingers at its top edge; the grey pleated trouser behind it; the ribbed wall at one edge; hard flash shadow.',
  'THE COVER IS PLAIN GLOSSY WHITE paper, flat, crisp corners, '+BL+', with no flash glare on it.'),
 sh(3,'paper-bag-by-loafers-bench','print','the bag front',['paper_bag','bench_perf'],'A','Sitting on the perforated bench, a paper shopping bag stands on the asphalt between his loafers.',
  'From above and in front, close, 35mm, f/8, camera square to the bag front. The bag stands on the centre line, its front panel square, filling about 55 percent of the frame height, sharp; the two brown loafers either side, grey trouser hems above; hard flash shadow behind the bag.',
  'THE BAG FRONT IS PLAIN MATTE OFF-WHITE PAPER, flat with crisp folded edges, '+BL+'.'),
 sh(5,'laptop-on-knees-from-above-tight','laptop','the laptop',['laptop'],'D','Sitting on the bench, a laptop open on his knees, screen tilted up toward him.',
  'From above, his point of view, very close, 35mm, f/8, camera square to the screen. The screen fills about 70 percent of the frame width on the centre line, dead square, sharp; the keyboard in the shadow of his forearms; grey trousers at the edges; hard flash shadow behind the lid.'),
 sh(6,'record-sleeve-under-arm','print','the record sleeve',[],'D','Walking home from the record shop, a 12-inch record sleeve tucked under his arm against his side.',
  'Straight on, very close, 35mm, f/8, camera square to the sleeve. The square sleeve fills about 65 percent of the frame width on the centre line, sharp; the navy sleeve of his arm crosses only its top edge; the cream vest behind; hard flash shadow tight behind it.',
  'THE SLEEVE FRONT IS PLAIN MATTE WHITE board, flat and rigid, crisp corners, '+BL+'.'),
 sh(7,'cap-in-hand-front-panel','print','the cap front',['cap'],'D','He holds a plain cap in his hand at his side, about to put it on, the front panels facing out.',
  'Straight on, very close, 35mm, f/8, camera square to the cap front. The cap front panels fill about 55 percent of the frame width on the centre line, sharp; his fingers hold the brim from below; grey trouser behind; hard flash shadow.',
  'THE FRONT PANELS ARE PLAIN OFF-WHITE COTTON TWILL, smooth, '+BL+'.'),
 sh(8,'tablet-two-hands-ribbed-wall','ipad','the tablet',['ipad'],'D','Standing against the ribbed concrete wall, he holds a tablet up in front of his chest with both hands.',
  'Straight on, close, 35mm, f/8, camera square to the screen. The tablet fills about 65 percent of the frame height on the centre line, dead square, sharp; both hands at its lower corners, rolled navy cuffs; the cream vest behind; the ribbed wall shows at the edges in hard flash.'),
]
S_BIKE=sh(4,'phone-bike-handlebar-mount','phone','the phone',['bike'],'D','Stopped at the kerb on his black city bike, his phone sits in the mount at the centre of the handlebar.',
  'From above, his point of view, close, 35mm, f/8, camera square to the phone. The phone fills about 45 percent of the frame height on the centre line, dead square, sharp; the straight black bar and leather grips cross the frame, his hands resting on the grips at both edges; the asphalt below in hard flash.')
if os.environ.get('WITH_PROPS'): S=sorted(S+[S_BIKE],key=lambda s:s['n'])
