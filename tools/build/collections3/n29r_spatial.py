# n29 Spatial Awareness round 1 (Sam 19 Oct). Art installations: the screen or lightbox is the artwork, visitors only small silhouettes.
# Moodboard: Figma Inlay Brand Design, section 194:1373. Strongest: 191:1327 (huge lightbox in a dark hall), 191:1326 (room of CRTs),
# 193:1348 (screens in a dark box room), 193:1344 (lit cubes in a dark hall), 191:1328 (lightbox in snow: 'if outside, do snow').
from builder3 import SQ
C={
 'id':'n29r1','name':'Spatial Awareness','aspect':'4:5','format_words':'portrait 4:5',
 'register':'Documentation photograph of a contemporary art installation',
 'world':'A real art space or real outdoor site exactly as the shot describes, quiet and spare; the installation is the only thing that glows.',
 'light':"The installation's own glow is the main light: it spills onto the floor, walls and people around it and falls off into deep shadow. Any other light is the real ambient light named in the shot.",
 'palette':'Neutral and cool: charcoal, concrete grey, soft blacks and natural skin; the glowing design surface is pure neutral white; no teal, green or orange cast, except the natural blue of snow at blue hour where the shot names it.',
 'real':("Real: this is a product mockup photograph of an art installation, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates, the way an exhibition photographer frames the work, never a tiny object in a big room. "
         "It is a real photograph made in camera by an art documentation photographer, not a render. "+SQ+
         " Only the objects named in the shot are in frame. The space shows small honest signs of use; the design surface itself is new and clean. "
         "The glowing surface is bright and clean, clearly the brightest thing in the frame, without blowing out; its edges and corners stay crisp. No halation, bloom, haze or glow over it."),
 'finish':'Shot on 35mm Kodak Portra 800 pushed one stop: natural visible grain in the shadows, true neutral film colour, gentle lens falloff toward the corners, honest exposure that lets the room go dark. Quiet and real, like a page in an exhibition catalogue; never a smooth digital render.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any image, text or colour on the glowing surface','any object not named in the shot','fog or haze','a clean smooth digital look'],
}
SIL='Visitors appear only as small dark silhouettes, seen from behind against the light, never more than a fraction of the frame; no face or profile shows.'
def s(n,slug,refs,moment,shot,surface,comp=None,people=None,kind='screen',noun='the screen'):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs,'moment':moment,'shot':shot,'surface':surface}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    if comp: d['comp']=comp
    return d
LB='THE LIGHTBOX FACE IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, clearly the brightest thing in the frame yet not blown out, with crisp corners meeting its thin black frame; nothing on it and nothing crossing it.'
S=[
 s(1,'monumental-lightbox-dark-hall',['gal_lightbox'],
  'A single monumental lightbox stands alone in a vast, dark, empty exhibition hall; one visitor has stopped in front of it.',
  'Camera at chest height straight on, 35mm lens, f/4. The lightbox, scaled up to about four metres tall, stands on the centre line and fills about 65 percent of the frame height; its glow spills across a polished grey concrete floor and makes a long soft reflection of it below; a low ceiling with one long recessed light slot runs across the top edge; dark walls fall away to black at both sides; one visitor stands far to the right of it.',
  LB,'A',SIL,'print','the lightbox'),
 s(2,'lightbox-in-snowfield-blue-hour',['gal_lightbox'],
  'Our freestanding lightbox stands alone in a deep snowfield at blue hour, switched on, as a land art installation.',
  'Camera low, just above the snow, 50mm lens, f/4, straight on. The lightbox stands on the centre line, its feet buried in snow, a thin ridge of snow resting on its top edge, filling about 55 percent of the frame height; its white glow lights a soft pool on the snow around it; behind, a long line of leaning fence posts and a low dark tree line under a deep blue dusk sky. No footprints, no falling snow in front of it.',
  LB,'A',None,'print','the lightbox'),
 s(3,'one-lit-crt-before-stacked-dark-crts',['crt'],
  'An installation in a dim lived-in room: a wall of stacked grey CRT monitors, all switched off, and in front of them one CRT that is on.',
  'Camera close at screen height, 50mm lens, f/2.8, square to the lit monitor. The lit CRT sits on the worn oak floor on the centre line, its screen filling about 50 percent of the frame width, sharp; behind it, out of focus, rows of identical grey CRTs stacked to the ceiling, every one switched off, their dark glass catching only faint reflections of the lit screen; the edge of an old fabric sofa at the frame edge.',
  'THE LIT CRT SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly the brightest thing in the frame, evenly lit edge to edge across its softly curved glass yet not blown out, with crisp corners meeting its grey bezel; every other monitor is off and dark.',
  None,None,'screen','the CRT monitor'),
 s(4,'flat-screen-on-white-gallery-floor',['pr04'],
  'A white gallery in daylight: one slim flat screen stands directly on the pale concrete floor as a sculpture, its black cable trailing away across the floor.',
  'Camera low, close to the floor, 35mm lens, f/5.6, square to the screen. The screen stands upright on its low stand on the centre line, filling about 60 percent of the frame width, sharp; its black cable runs in one long loose curve across the pale floor to the frame edge; behind, clean white walls and the soft light of a tall window out of frame on the left. Soft cool daylight, gentle shadows.',
  'THE SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly the brightest thing in the frame, evenly lit edge to edge yet not blown out, with crisp corners meeting its thin black border; nothing crosses the screen.',
  'A',None,'screen','the screen'),
 s(5,'projection-wall-dark-room-silhouettes',[],
  'A dark screening room in a museum: a large projected image fills the back wall and a few visitors stand watching it.',
  'Camera at standing height from the back of the room, 35mm lens, f/2.8. The projected rectangle sits on the centre line of the back wall, filling about 60 percent of the frame width, a crisp-edged field of white light on the matte wall; its light falls on the bare floor and on the backs of three visitors standing in the lower third of the frame, who read as dark cut-out silhouettes against it; the side walls fall to black.',
  'THE PROJECTED IMAGE IS PLAIN WHITE, a clean, crisp-edged rectangle of light on the matte wall, evenly bright edge to edge without blowing out; nothing is projected on it and no shadow crosses it.',
  'A',SIL,'print','the projection'),
]
