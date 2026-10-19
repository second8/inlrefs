# n31 Open Air round 1 (Sam 19 Oct, he named it). Out-of-home mockups in daylight. Moodboard: Figma Inlay Brand Design, section 199:1377 (WORDS ONLY, never as refs).
# Moodboard read: clear blue sky, hard daylight, real city architecture; boards shot near square-on, clean architectural documentation;
# wallscapes on white industrial walls, station posters with blurred trains, long construction hoardings under an overpass, pole billboards against empty sky,
# rooftop billboards on brick, long posters on white subway tiles, a billboard in a white concrete courtyard, a banner on a mesh-wrapped scaffold.
from builder3 import SQ
C={
 'id':'n31r1','name':'Open Air','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A clean, bright daylight photograph of out-of-home advertising in a real city',
 'world':'A real city on a clear day: plain concrete, white render, old brick and steel; clean pavements; nothing else unless the shot names it.',
 'light':'Clear, hard daylight from a high sun in a cloudless deep blue sky: crisp shadows with sharp edges, bright walls, natural contrast.',
 'palette':'Clean natural colour: a clear saturated-but-natural blue sky, true neutral whites, warm concrete and brick, deep clean shadows; the design surface pure neutral white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup photograph of out-of-home advertising, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates, never a tiny board in a wide view. "
         "It is an unstaged photograph of a real place on a real day, with small honest signs of weather and age on the place only; the design surface itself is new, flat and clean. "+SQ+
         " Only the objects named in the shot are in frame. The design surface is bright and clean without blowing out; its edges and corners stay crisp."),
 'finish':'Shot like clean architectural documentation on a medium-format digital camera: sharp, precise, straight verticals, fine detail, natural true colour, a light film-like softness in the highlights. Calm and considered, like the case-study photos of a top design studio; never a 3D render, never over-processed or HDR.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any image or text on the design surface','any object not named in the shot','clouds, haze or a hazy sky','an HDR or over-saturated look','a clean smooth 3D render look'],
}
W={'aspect':'16:9','format_words':'landscape 16:9'}
PRINT=lambda what: f'{what} IS PLAIN MATTE PAPER-WHITE, flat and taut edge to edge with crisp corners, nothing printed on it and nothing crossing it.'
FEW='One or two people pass in front of the wall far below the design surface, small and natural, never over it; no face shows.'
def sh(n,slug,moment,shot,surface,noun,comp='A',people=None,wide=False,kind='print'):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':[],'moment':moment,'shot':shot,'surface':surface,'comp':comp}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    if wide: d.update(W)
    return d
S=[
 sh(1,'wallscape-on-white-industrial-building-wide','A huge flat wallscape is mounted on the plain white rendered side wall of a low industrial building on an ordinary city street.',
  'Camera from across the street at the height of the wallscape middle, 50mm lens, f/8, square to the wall. The wallscape fills about 60 percent of the frame width, sharp, a big landscape rectangle on the white wall; a corrugated metal roof edge above, a plain door and pavement below; a few low neighbouring buildings at the frame edges; deep blue sky.',
  PRINT('THE WALLSCAPE'),'the wallscape',people=FEW,wide=True),
 sh(2,'backlit-station-poster-train-blur','A portrait backlit poster in a slim dark frame stands between two tiled pillars on an open-air station platform while a train rushes past behind it.',
  'Camera at poster height on the platform, 50mm lens, f/8, slow shutter, square to the poster. The poster fills about 55 percent of the frame height on the centre line, dead sharp and still; the train behind it is a long horizontal streak of motion blur in muted colours; the grey platform paving in the foreground; daylight from above.',
  'THE POSTER IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim dark frame, nothing printed on it and nothing crossing it.','the poster'),
 sh(3,'run-of-posters-on-hoarding-under-overpass-wide','A long, flat construction hoarding runs along a pavement under the edge of a concrete road overpass, with a run of identical large posters pasted side by side along it.',
  'Camera on the far kerb at poster height, 35mm lens, f/8, square to the hoarding. The posters form a long band across the frame, the middle one on the centre line filling about 30 percent of the frame width, all sharp; the underside of the overpass cuts across the top of the frame in shadow; hard sun falls across the pavement in front; clean concrete paving.',
  'EVERY POSTER ON THE HOARDING IS PLAIN MATTE PAPER-WHITE, flat and taut with crisp edges, nothing printed on any of them.','the posters',wide=True),
 sh(4,'pole-billboard-against-empty-blue-sky','A single billboard stands on one tall grey steel pole above a flat-roofed building, against an empty deep blue sky.',
  'Camera from a distance with a long lens, 135mm, f/8, at nearly the height of the board so it stays square and undistorted. The billboard face fills about 65 percent of the frame width on the centre line, sharp; the pole runs straight down to the top of a plain building at the bottom edge; a lamp arm or two under the board; nothing but clean blue sky around.',
  PRINT('THE BILLBOARD FACE'),'the billboard'),
 sh(5,'rooftop-billboard-on-old-brick-building-wide','A large billboard stands on a steel frame on top of an old red brick building with arched windows.',
  'Camera from a raised position across the street at billboard height, 70mm lens, f/8, square to it. The billboard face fills about 55 percent of the frame width, sharp, its steel catwalk and frame below it; the weathered brick parapet and arched windows across the lower part of the frame; deep blue sky above.',
  PRINT('THE BILLBOARD FACE'),'the billboard',wide=True),
 sh(6,'long-poster-on-white-subway-tiles-wide','A long landscape poster is pasted flat on a wall of small white square tiles in an underground station.',
  'Camera on the opposite platform at poster height, 35mm lens, f/8, square to the wall. The poster fills about 70 percent of the frame width, sharp, its edges parallel to the tile grid; the white tiles run on all sides; a dark platform edge strip along the bottom; clean even station light from above.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted flat with crisp edges and the faintest real paper texture, nothing printed on it and nothing crossing it.','the poster',wide=True),
 sh(7,'billboard-in-white-concrete-courtyard','A billboard hangs flat on the back wall of a quiet white concrete courtyard open to the sky.',
  'Camera standing at the courtyard entrance, 35mm lens, f/8, square to the back wall. The billboard fills about 55 percent of the frame width, sharp, a little above the centre; the white concrete walls frame it on both sides; one hard diagonal shadow from the courtyard wall falls across the pale ground, never over the billboard; a strip of deep blue sky at the top.',
  PRINT('THE BILLBOARD FACE'),'the billboard',comp='C'),
 sh(8,'banner-on-mesh-wrapped-scaffold','A large flat banner is fixed on the front of a building wrapped in scaffolding and translucent white mesh.',
  'Camera from across the street at banner height, 85mm lens, f/8, square to it. The banner fills about 60 percent of the frame width on the centre line, sharp, tied taut at its corners; the soft translucent mesh around it shows the faint grid of scaffold poles behind; hard sun on the mesh; a strip of blue sky at the top.',
  'THE BANNER IS PLAIN MATTE WHITE VINYL, pulled flat and taut with crisp edges and small grommets at its corners, nothing printed on it and nothing crossing it.','the banner'),
]
