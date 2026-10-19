# n30 Low Cloud round 2 (Sam 19 Oct): r1-01 'closest, still not as moody as I wanted', r1-02 'too bright, daylight, not moody'; 03, 04 bad; 05 'no phones, this is all about city and billboards'.
# 'More moody, but don't overdo it, still realistic. I like 1 and 2. The whole collection has the same look: same colour grading, language.'
# So: both look refs on every shot (same grade), dusk under low cloud, screens and billboards only.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n30r_lowcloud.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
C=dict(r1.C);C['id']='n30r2'
C['register']='A moody but realistic city photograph at dusk under low cloud'
C['world']='A real city at dusk under heavy low cloud: the tops of towers disappear into grey cloud, mist sits in the middle distance, streets and stone are wet; small warm windows and street lights far off.'
C['light']='Last blue-grey dusk light under heavy cloud, quite dark; the screen or billboard is the brightest thing in the frame and lights the wet ground near it; city lights small and soft in the distance.'
C['palette']='The same grade on every image: muted desaturated greys and charcoal, a slight cool tint in the cloud, small warm sodium lights, deep but not crushed shadows; the design surface pure neutral white.'
C['finish']='Shot on 35mm Kodak Portra 800 pushed one stop in low light: visible natural grain, muted soft film colour, slight lens falloff, honest underexposed dusk. Moody but believable, like a real photograph from a real evening; never a render, never cinematic teal and orange.'
LOOKS=['r30_tower','r30_square']
SCR=r1.SCR;BACK=r1.BACK
def sh(n,slug,refs,moment,shot,surface,kind='led',noun='the screen',comp='A',people=None):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs,'moment':moment,'shot':shot+BACK,'surface':surface,'comp':comp}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    if not comp: d.pop('comp')
    return d
TINY='A few tiny figures in dark coats stand or pass far below it, small dark shapes; no face shows.'
S=[
 sh(1,'led-tower-fog-plaza-dusk',['r30_tower_rec','r30_square'],
  'A tall slim LED screen tower stands in a shallow reflecting pool on a city plaza at dusk while the skyscrapers behind dissolve into low cloud.',
  'Camera from across the plaza at the height of the tower middle, 85mm lens, f/2.8, verticals parallel. The tower stands on the centre line, its screen filling about 70 percent of the frame height, sharp; its light lies as a long column on the wet stone and water below; skyscrapers to both sides fade up into grey cloud, their windows faint.',
  'THE TOWER SCREEN '+SCR,people=TINY),
 sh(2,'wide-screen-plinth-smog-square-dusk',['r30_square_rec','r30_tower'],
  'A wide public screen on a heavy stone plinth glows in a vast civic square at dusk on a day of smog and low cloud; people stand scattered across the square.',
  'Camera at standing height from the square, 50mm lens, f/2.8, straight on, close enough that the screen fills about 80 percent of the frame width, sharp; flagpoles and a long stone building fade into the grey murk behind; the people in the lower third as dark silhouettes.',
  'THE WIDE SCREEN '+SCR,comp=None,people=TINY),
 sh(3,'led-facade-screen-corner-building-cloud',LOOKS,
  'A large portrait LED screen covers the corner of a city building above a wet intersection at dusk; the upper floors vanish into low cloud.',
  'Camera from a window across the street at the height of the screen, 85mm lens, f/2.8, square to its face. The screen fills about 60 percent of the frame height on the centre line, sharp; the dark facade around it, a few lit windows; the building above disappears into grey cloud; the wet street glints far below at the bottom edge.',
  'THE FACADE SCREEN '+SCR),
 sh(4,'roadside-billboard-single-pole-low-cloud',LOOKS,
  'A tall roadside billboard on a single steel pole glows over an empty ring road at dusk, low cloud dragging across the hills and towers behind.',
  'Camera from an overpass at the height of the billboard, 85mm lens, f/2.8, square to its face. The billboard fills about 75 percent of the frame width on the centre line, sharp, lit evenly by its own row of lamps; the steel pole drops out of the bottom of the frame; behind it grey cloud and the faint shapes of distant towers.',
  'THE BILLBOARD FACE IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.','print','the billboard'),
 sh(5,'rooftop-billboard-over-shuttered-shops-mist',LOOKS,
  'A large lit billboard stands on the roof of a low row of shuttered shops on a wet street at dusk, mist settling over the city behind it.',
  'Camera from across the street at roof height, 50mm lens, f/2.8, square to the billboard. The billboard fills about 70 percent of the frame width on the centre line, sharp, its steel frame and catwalk below it; the shut metal shutters of the shops along the bottom edge; the wet street reflecting its light; mist and the soft lights of the city behind.',
  'THE BILLBOARD FACE IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.','print','the billboard'),
]
