# n30 Low Cloud round 1 (Sam 19 Oct, he named it). City screens on a low-cloud day, towers dissolving into cloud and mist.
# Moodboard: Figma Inlay Brand Design, section 194:1376. Look and feel: 192:1336 (tall LED tower in a wet plaza, skyline lost in cloud).
# Others: 192:1337 (wide screen on a plinth in a smoggy square, silhouettes), 193:1343 (lit billboard at night). Fog stays behind the screen.
from builder3 import SQ
C={
 'id':'n30r1','name':'Low Cloud','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A city photograph on a day of low cloud',
 'world':'A real city centre under low cloud: towers and distant buildings dissolve into soft grey cloud and mist; wet stone, wet asphalt, puddles.',
 'light':'Flat, heavy overcast light or late dusk exactly as the shot says; the city lights are small and soft in the distance; the screen is the brightest thing in the frame.',
 'palette':'Muted cool greys, wet charcoal and soft blacks, a few small warm city lights far off; the design surface is pure neutral white. No teal or orange grade.',
 'cast':{'his':'ch11'},
 'real':("Real: this is a product mockup photograph in a real city, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates, never a tiny screen in a wide view. "
         "It is an unstaged photograph of a real place on a real day, with small honest signs of weather and age on the place only; the design surface itself is new and clean. "+SQ+
         " Only the objects named in the shot are in frame. Exposure is honest, but the design surface is bright and clean, clearly the brightest thing in the frame, without blowing out; its edges and corners stay crisp. No halation or bloom around lights."),
 'finish':'Shot on 35mm Kodak Portra 800 pushed one stop: visible natural grain, soft muted film colour, gentle lens falloff, honest exposure. Real street photography from a real day, never a smooth digital render.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','mist, haze or glow over or around the design surface','any object not named in the shot','a teal and orange grade','a clean smooth digital look'],
}
BACK=' The mist and cloud stay far behind the design surface: it is crisp and clear, with nothing soft, hazy or glowing over its face or edges.'
SCR='SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly the brightest thing in the frame, evenly lit edge to edge yet not blown out, with crisp corners meeting its thin black frame; nothing crosses it.'
S=[
 {'n':1,'slug':'led-tower-wet-plaza-skyline-in-cloud','kind':'led','noun':'the LED tower','refs':[],'comp':'A','people':'line',
  'people_line':'Two or three tiny figures with umbrellas pass at its foot, dark and small, seen from far away; no face shows.',
  'moment':'A tall slim LED screen tower stands in a wide granite plaza at dusk while the skyline behind disappears into low cloud.',
  'shot':'Camera from across the plaza at the height of the tower middle, 85mm lens, f/4, so its verticals stay parallel. The tower, about fifteen metres tall, stands on the centre line, its screen filling about 70 percent of the frame height, sharp; its light reflects as a long bright column in the thin film of water on the granite; behind it skyscrapers rise and vanish into grey cloud, their lit windows faint.'+BACK,
  'surface':'THE TOWER SCREEN '+SCR},
 {'n':2,'slug':'wide-screen-on-plinth-smog-square','kind':'led','noun':'the screen','refs':[],'people':'line',
  'people_line':'People stand and walk across the square below it as dark silhouettes in winter coats, small in the frame, seen from behind or far away; no face shows.',
  'moment':'A wide public screen sits on a heavy stone plinth in a civic square on a grey day of smog and low cloud.',
  'shot':'Camera at standing height, 50mm lens, f/5.6, straight on and close enough that the wide screen fills about 85 percent of the frame width, sharp, sitting a little above the centre; the grey stone plinth below it; tall flagpoles and the outline of a stone building fade into the grey haze behind; the people stand in the lower third.'+BACK,
  'surface':'THE WIDE SCREEN '+SCR},
 {'n':3,'slug':'lit-billboard-night-low-cloud','kind':'print','noun':'the billboard','refs':[],'comp':'A','people':'none',
  'moment':'One large billboard high on a steel frame glows at night under its row of lamps, low cloud lit dull grey by the city behind.',
  'shot':'Camera level with the billboard from a raised walkway across the road, 85mm lens, f/2.8, square to it. The billboard face fills about 75 percent of the frame width, sharp; its lamp arms reach over the top edge and throw even light down its face; the dark steel catwalk runs under it; above and behind, low cloud glows dull grey.'+BACK,
  'surface':'THE BILLBOARD FACE IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.'},
 {'n':4,'slug':'bus-shelter-lightbox-fog-night','kind':'print','noun':'the lightbox panel','refs':['shelter'],'people':'none',
  'moment':'Our bus shelter on an empty street late at night in fog and drizzle, its tall lightbox panel the only bright thing on the block.',
  'shot':'Camera straight on to the lit panel at its middle, 50mm lens, f/2.8, close enough that the panel fills about 60 percent of the frame height, sharp; rain-wet pavement in front mirrors it; the street lights beyond dissolve into soft points in the fog; the glass walls of the shelter catch thin lines of light.'+BACK,
  'surface':'THE LIGHTBOX PANEL IS PLAIN EVENLY LIT WHITE, glowing bright and clean edge to edge, crisp corners inside its graphite frame, nothing on it and nothing crossing it.'},
 {'n':5,'slug':'phone-in-hand-on-bridge-city-in-cloud','kind':'phone','refs':['phone'],'people':'edge','who':'his','edge':'bottom',
  'wear':{'his':'a camel wool coat'},
  'moment':'On a bridge on a grey morning a man holds his phone up in front of him; the skyline across the river is swallowed by low cloud.',
  'shot':'Camera just behind his hand, 50mm lens, f/2.8, square to the phone. The phone stands upright on the centre line, its screen filling about 55 percent of the frame height, sharp; behind it, soft and far, the bridge railing runs across the frame and the towers across the river fade up into grey cloud.'+BACK,
  'surface':'THE PHONE '+SCR},
]
