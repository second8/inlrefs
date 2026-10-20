# n34 Desk Light round 1 (Sam 20 Oct, he named it): cozy working place. Moodboard Figma 202:125 (WORDS ONLY). Materials and comp of 202:120: a laptop on a warm
# honey-oak desk in late sun with leafy plant shadows, a clear glass of water throwing a caustic, a pale grey office chair. Mockup under glass reflections like 202:119:
# a poster behind a shop window with soft street reflections drifting across the glass.
from builder3 import SQ
C={
 'id':'n34r1','name':'Desk Light','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A warm, calm photograph of a cozy, well-made workplace',
 'world':'A quiet studio workspace: solid honey-oak desks, white walls, a pale grey office chair, a plant somewhere out of frame; nothing else unless the shot names it.',
 'light':'Warm low late-afternoon sun through a window: long crisp shadows, the soft leafy shadow pattern of a plant across the desk, and bright caustics thrown by clear glass.',
 'palette':'Warm honey oak, soft white, pale grey, dark aluminium; deep but soft shadows; the screen or design surface clean neutral white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup photograph, so the design surface is the hero: large, sharp and fully readable; shadows and caustics fall beside it, never over it. "
         "It is a real photograph, never a render. "+SQ+" Only the objects named in the shot are on set. Every object is at its true real-world size."),
 'finish':'Shot like a calm editorial interior on a full-frame camera: natural warm colour, soft fine grain, crisp sun shadows; quiet and premium, never a render.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any image, icon or text on the screen or surface','any object not named in the shot','a clean smooth 3D render look'],
}
SCR='THE SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, evenly lit edge to edge, crisp corners inside its thin black bezel, nothing on it.'
def sh(n,slug,refs,moment,shot,surface=SCR,noun='the screen',comp=None,aspect=None):
    d={'n':n,'slug':slug,'kind':'print','noun':noun,'refs':refs,'moment':moment,'shot':shot,'surface':surface,'comp':comp,'people':'none'}
    if aspect=='w': d.update(aspect='16:9',format_words='landscape 16:9')
    return d
S=[
 sh(1,'laptop-on-oak-desk-late-sun-water-glass',['laptop','keys'],'Our laptop stands open on a honey-oak desk in warm late sun, with a clear glass of water beside it and the leafy shadow of a plant across the wood.','Camera in front of the desk, a little above the keyboard, 50mm lens, f/5.6, square to the screen. The screen fills about 50 percent of the frame width on the centre line, sharp; the glass of water at one side throws a bright caustic and long shadow on the oak; the pale grey chair back at the far edge; leafy shadows across the desk, never over the screen.',aspect='w'),
 sh(2,'ipad-on-oak-desk-ceramic-mug-top-down',['ipad'],'Our iPad lies flat on the honey-oak desk in warm sun beside a ceramic mug of coffee.','Camera straight down, 50mm lens, f/5.6. The iPad lies on the centre line, edges parallel to the frame, filling about 60 percent of the frame width, sharp; the mug at one corner casts a long soft shadow; the leafy shadow pattern falls across the wood beside it, never over the screen.',comp='B'),
 sh(3,'phone-and-notebook-oak-desk-top-down',['phone'],'Our phone lies face up on the honey-oak desk next to a closed linen notebook and a pen, in warm late sun.','Camera straight down, 50mm lens, f/5.6. The phone lies on the centre line, edges parallel to the frame, filling about 35 percent of the frame width, sharp; the notebook and pen beside it; long crisp shadows and leaf shadows across the oak.',comp='B'),
 sh(4,'monitor-on-oak-desk-white-wall-plant-shadow',[],'A slim desktop monitor on a thin aluminium stand sits on a honey-oak desk against a white wall, the leafy shadow of a plant falling across the wall.','Camera at desk height in front, 50mm lens, f/5.6, square to the screen. The monitor screen fills about 55 percent of the frame width on the centre line, sharp; the leaf shadows dance on the white wall around it, never over the screen; the edge of the pale grey chair at the corner.',aspect='w'),
 sh(5,'poster-behind-studio-window-street-reflections',[],'A poster stands on a slim easel inside the street window of a small design studio; soft reflections of the street, the facades opposite and a passing car drift across the glass.','Camera on the pavement, 50mm lens, f/5.6, square to the window. The poster fills about 50 percent of the frame height on the centre line, sharp and readable through the glass; pale soft reflections of the facades and the car float lightly across the window and the edges of the poster, never hiding it; a thin dark window frame.',surface='THE POSTER IS PLAIN MATTE PAPER-WHITE, flat with crisp edges, nothing printed on it.',noun='the poster',comp='A'),
]
