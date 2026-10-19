# n26 Tonal, 5 more (Sam: "lets do 5 more"; look test read as a real painted set but safe). Lilac set, design surface the only white,
# square-on devices on painted set pieces, look test image for light/colour/materials only, lilac TV prop 78.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'..','collections2','n26_tonal.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n26r';C['name']='Tonal (round 2)'
C['world_short']='A commercial photo studio set built entirely in lilac: a seamless painted lilac cove with no horizon and a few real painted set pieces in tints and shades of lilac.'
LT='https://media.weavy.ai/image/upload/v1792102681/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/szqzuukwub8zxhu3ztfe.png'
LK='the lilac set look: its light, colour, painted materials and soft tinted shadows'
C['avoid']=_m.C['avoid']+['any object not named in the shot']
def sh(n,slug,kind,refs,comp,moment,shot,**kw):
    d={'n':n,'slug':slug,'kind':kind,'refs':refs,'people':'none','comp':comp,'looks':[(LT,LK)],'moment':moment,'shot':shot};d.update(kw);return d
S=[
 sh(1,'phone-lacquer-stand-plinth','phone',['phone'],'A','A phone standing upright in a low deep violet gloss lacquer stand on top of a tall lilac plinth.',
  'Straight on, camera exactly at the screen, 100mm macro, f/8. The phone stands on the centre line, screen dead square to the camera, filling about 55 percent of the frame height, sharp; the plinth top is pale lilac flocked velvet with a soft contact shadow; the lilac cove behind falls off gently.'),
 sh(2,'watch-glazed-ceramic-pillow','watch',['watch'],'D','A watch closed around a small glazed lilac ceramic pillow on a plinth.',
  'Straight on, very close, 120mm macro, f/8, camera exactly at the watch face. The watch face sits on the centre line, dead square, filling about 50 percent of the frame width, sharp; the glazed pillow shows a gentle sheen; pale lilac flocked plinth top below; deep violet tinted shadow.'),
 sh(3,'lilac-portable-tv-on-step','tv',['tv_lilac'],'A','Our lilac enamel portable TV sitting on the second step of the flocked lilac riser, switched on.',
  'Straight on, camera exactly at the screen, 80mm, f/8. The TV sits on the centre line, its screen facing the camera dead square, filling about 60 percent of the frame width, sharp; real enamel with a soft sheen and a tiny chip at one corner; the flocked step edge runs straight across below; contact shadow tinted deep violet.',
  noun='the TV screen',surface='THE CURVED TV SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, evenly bright, not blown out, softly rounded corners inside a thin black surround, one faint soft highlight at the top left only, nothing crossing it.'),
 sh(4,'laptop-on-lacquer-block','laptop',['laptop'],'A','A laptop open on a long low lilac satin-lacquer block at table height.',
  'Straight on, camera exactly at screen height, 80mm, f/8. The laptop sits on the centre line, screen facing the camera dead square, filling about 60 percent of the frame width, sharp; the keyboard deck foreshortened in the soft shadow of the screen; the block front face satin lilac with an eased edge catching a thin highlight.'),
 sh(5,'tablet-on-felt-wedge','ipad',['ipad'],'A','A tablet standing in landscape on a lilac wool felt reading wedge on a low painted block.',
  'Straight on, camera exactly at the screen, 80mm, f/8. The tablet sits on the centre line, screen dead square to the camera, filling about 65 percent of the frame width, sharp; the felt wedge shows fine nap; the block and cove in tints of lilac, a deep violet gloss edge as the one accent.'),
]
