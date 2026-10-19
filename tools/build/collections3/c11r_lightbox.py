# C11 Lightbox remake (Sam 16 Oct 19:3x: "recreate 5, too generic, but I really like the lightbox concept from behind"). Library already
# has a live Lightbox set of silhouettes on a plain panel, so ours is a real backlit frosted-glass wall with a black steel grid (prop 71):
# the grid gives geometric framing, people only as dark backs and hands, no profiles or faces.
C={
 'id':'c11r','name':'Lightbox (remake)','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A quiet, graphic campaign photograph in front of a huge backlit frosted-glass wall',
 'world':'A dark interior in front of a floor-to-ceiling wall of large frosted glass panels in a fine matte black steel grid, lit evenly from behind. In front of the wall, only what the shot names: a dark steel desk, a person seen from behind. Everything in front of the glass is dark.',
 'world_short':'A dark interior in front of a floor-to-ceiling backlit frosted-glass wall with a fine black steel grid. Everything in front of the glass is dark.',
 'light':'The glass wall is the only light: warm white, about 3500K, glowing evenly across every panel with no hot spots, so everything in front of it reads as a crisp dark silhouette with a faint thin rim along its edges. The device screen is as bright and clean as the glass and stays crisp.',
 'palette':'Warm ivory glass #F3E9D6, matte black steel grid #121212, near-black silhouettes #0B0B0B with faint warm rim, and the white screen. Nothing else.',
 'finish':'Medium-format digital, 80mm, f/4, verticals and grid lines perfectly straight and parallel to the frame, fine grain, no halation, no flare, no haze. Graphic and calm, like a design campaign still.',
 'cast':{'her':'ch06','his':'ch11'},'wear':{'her':'a fine black knit','his':'a black crew-neck knit'},
 'avoid':['a face, profile, cheek, ear or chin','glow or halation around the glass','hot spots or visible lamps in the glass','any object not named in the shot','a tilted grid'],
}
GW=['glasswall']
S=[
 {'n':1,'slug':'phone-held-in-one-glass-square','kind':'phone','refs':['phone']+GW,'people':'back','who':'her','edge':'left','comp':'C',
  'moment':'A phone held up at eye level, its screen sitting exactly inside one glowing glass square of the wall.',
  'shot':'Straight on, camera square to the wall, 80mm, f/4. One glass square sits on the centre line framed by the black grid; the phone is held upright inside it, screen facing the camera dead square, filling about 50 percent of the frame height, sharp; the hand and wrist are a dark silhouette below it.'},
 {'n':2,'slug':'watch-raised-wrist-grid-square','kind':'watch','refs':['watch']+GW,'people':'edge','who':'his','edge':'right','comp':'D',
  'moment':'A raised wrist with a smartwatch held still against the glowing wall, the watch face centred in one glass square.',
  'shot':'Very close, 90mm, f/4, camera square to the watch face. The watch face sits on the centre line, dead square, filling about 40 percent of the frame width, sharp; the forearm runs in from the right as a crisp dark silhouette; one black grid line crosses the frame behind, perfectly straight.'},
 {'n':3,'slug':'laptop-steel-desk-grid-behind','kind':'laptop','refs':['laptop']+GW,'people':'none','comp':'A',
  'moment':'A laptop open on a long dark steel desk in front of the glowing glass wall, nobody there.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/4. The laptop sits on the centre line, screen facing the camera dead square, filling about 55 percent of the frame width, sharp; one vertical grid line runs exactly behind its centre and one horizontal grid line just above its screen; the desk is a thin dark band across the bottom.'},
 {'n':4,'slug':'tablet-two-hands-one-panel','kind':'ipad','refs':['ipad']+GW,'people':'edge','who':'her','edge':'bottom','comp':'C',
  'moment':'A tablet held up in two hands against the glowing wall, aligned to one glass panel like a frame inside a frame.',
  'shot':'Straight on, camera square to the wall, 80mm, f/4. The tablet is held upright on the centre line inside one glass square, screen dead square to the camera, filling about 55 percent of the frame height, sharp; both hands hold its lower corners as clean dark silhouettes; the black grid frames it with an even margin.'},
 {'n':5,'slug':'display-desk-dark-shoulder','kind':'display','refs':['display']+GW,'people':'back','who':'his','edge':'right','comp':'A',
  'moment':'A desktop display on the dark steel desk, centred against the glowing glass grid, someone sitting just out of frame.',
  'shot':'Straight on, camera exactly at screen height, 50mm, f/4. The display sits on the centre line facing the camera dead square, filling about 55 percent of the frame width, sharp; the grid runs perfectly level and plumb behind it; a dark shoulder fills the lower right corner, out of focus.'},
]
