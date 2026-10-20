# n33 (name TBD, Sam 20 Oct) round 1: 'really precise high quality device renders, advanced.' Moodboard Figma 202:124 (WORDS ONLY): pure black void,
# brushed-aluminium horizontal control unit with a central screen and two round dials; a tall steel and black EV charger pillar with a portrait screen;
# a rounded soft-touch handheld with a screen above three square buttons; a dark smart ring. Single soft key light, precise industrial-design renders.
from builder3 import SQ
C={
 'id':'n33r1','name':'Devices','aspect':'4:3','format_words':'landscape 4:3',
 'register':'A precise, photoreal studio product render of a premium device by a top industrial design studio',
 'world':'A pure black seamless void; nothing else in the frame but the device.',
 'light':'One large soft key light from above and one side, with a thin rim light: crisp highlights running along machined edges and chamfers, soft gradients on brushed metal, the rest falling to pure black.',
 'palette':'Neutral and cool: brushed aluminium, satin steel, matte black and graphite on pure black; the screen a clean neutral white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup render, so the screen is the hero: large, sharp and fully readable, glowing evenly. "
         "It is a flawless photoreal render with real material physics: fine brushed-metal grain, precise machined chamfers, tight tolerances, tiny screws and seams. "+SQ+" Only the device named is in frame."),
 'finish':'Ultra-precise, high-end industrial-design render: perfectly clean, sharp detail, accurate reflections, subtle depth; no noise, no clutter, no text.',
 'avoid':['logos, letters, numbers or brand names anywhere','any image, icon or text on the screen','any object other than the device','a cheap plastic look','a cartoon or toy look'],
}
SCR='THE SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, evenly lit edge to edge, crisp corners inside its black border, nothing on it.'
def sh(n,slug,moment,shot,aspect=None):
    d={'n':n,'slug':slug,'kind':'print','noun':'the screen','refs':[],'moment':moment,'shot':shot,'surface':SCR,'comp':'A','people':'none'}
    if aspect=='w': d.update(aspect='16:9',format_words='landscape 16:9')
    if aspect=='v': d.update(aspect='4:5',format_words='portrait 4:5')
    return d
S=[
 sh(1,'brushed-aluminium-control-unit-two-dials','A long horizontal control unit in brushed aluminium floats in the black void: a central landscape screen set in a black glass panel, a large round machined dial at each end.','Camera straight on, 100mm lens. The unit spans about 80 percent of the frame width on the centre line; the screen fills about 40 percent of the frame width, sharp, perfectly square-on; the dials have fine knurled edges catching the light; a thin highlight runs along the top chamfer.','w'),
 sh(2,'ev-charging-pillar-portrait-screen','A tall EV charging pillar in satin stainless steel and matte black stands in the black void, a portrait screen set into its face and a charging handle docked below.','Camera straight on at screen height, 85mm lens. The pillar stands on the centre line; the portrait screen fills about 35 percent of the frame height, sharp; crisp vertical highlights run down the steel sides; the black base fades into the void.','v'),
 sh(3,'rounded-handheld-screen-over-three-buttons','A small rounded handheld device in soft-touch dark graphite floats in the black void: a landscape screen in its upper half and three square tactile buttons in a row below.','Camera straight on, 100mm lens. The device fills about 60 percent of the frame width on the centre line; the screen fills about 45 percent of the frame width, sharp; the three buttons have soft rounded edges and a subtle sheen; a gentle rim light outlines the rounded body.'),
 sh(4,'wall-thermostat-panel-square-screen','A square smart thermostat panel in anodised dark aluminium with a square screen, shown floating in the black void.','Camera straight on, 100mm lens. The panel fills about 55 percent of the frame width on the centre line; the square screen fills about 40 percent of the frame width, sharp; a fine chamfer around the panel catches a thin line of light; a single small machined button on its side.'),
 sh(5,'smart-home-hub-on-aluminium-stand','A smart home hub with a landscape screen sits on a slim angled brushed-aluminium stand in the black void.','Camera straight on at screen height, 85mm lens. The hub fills about 60 percent of the frame width on the centre line; the screen fills about 50 percent of the frame width, sharp, square-on; the stand\'s bent aluminium plate catches a soft gradient highlight; a faint reflection below.'),
]
