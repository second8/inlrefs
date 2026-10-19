# C3 Flash remake (Sam: "good, but recreate; the black guy and those clothes are similar to another collection I found online").
# Keep: night street, direct on-camera flash, colour-negative film, candid crops from above. Change: ch10, new outfit (prop 73),
# our perforated steel bench (prop 72), a ribbed concrete wall instead of plaster, no coffee cups. Sam picked 6.
C={
 'id':'c3r','name':'Flash (remake)','aspect':'2:3','format_words':'portrait 2:3',
 'register':'A candid street mockup photograph at night, taken with direct on-camera flash',
 'world':'A city sidewalk at night: fine dark asphalt, our galvanised perforated steel bench with graphite end frames, a ribbed precast concrete wall. Everything beyond a metre or two falls into near black.',
 'world_short':'A city sidewalk at night: fine dark asphalt, our galvanised perforated steel bench, a ribbed precast concrete wall, near black beyond.',
 'light':'Direct on-camera flash only: hard frontal light, crisp short shadows right behind every object, quick falloff into a near-black background, slight natural vignette. No flash hotspot or reflection on any screen.',
 'palette':'Cream knit, deep navy poplin, mid-grey wool, dark brown suede and leather, light olive skin, galvanised steel, near-black asphalt, and the white screen. No other colours.',
 'finish':'35mm compact film camera, colour negative film: saturated but natural, warm whites, faint green in the blacks, clearly visible grain, crisp, framing grabbed but the device square to camera. No light leaks, no date stamp, no film border, no halation.',
 'cast':{'his':'ch10'},'wear':{'his':'the outfit from the reference'},
 'avoid':['a face, profile or chin','a white t-shirt, denim or sneakers','a coffee cup','daylight or neon','glare on the screen'],
}
PL='Only his hands, forearms, lap, legs and loafers are in frame, wearing exactly the outfit from the reference; his head and face are never in frame.'
W=['ch10','wear_c3']
S=[
 {'n':1,'slug':'phone-hand-on-lap-from-above','kind':'phone','refs':['phone']+W,'people_line':PL,'comp':'D',
  'moment':'Sitting on the perforated bench at night, he holds his phone low over his lap, screen up.',
  'shot':'From above, his point of view, 35mm, f/8, camera square to the screen. The phone fills about 45 percent of the frame height on the centre line, screen dead square, sharp; the grey pleated trousers fill the frame behind it, a brown loafer at one corner on dark asphalt; hard flash shadow tight behind his hand.'},
 {'n':2,'slug':'phone-two-hands-between-knees','kind':'phone','refs':['phone']+W,'people_line':PL,'comp':'D',
  'moment':'Seated on the bench, elbows on knees, he holds the phone in both hands between his knees.',
  'shot':'From above and in front, close, 35mm, f/8, camera square to the screen. The phone is upright on the centre line in both hands, screen dead square, filling about 40 percent of the frame height, sharp; the rolled navy cuffs and the cream vest hem frame the top; the grey trousers and loafers below on the asphalt.'},
 {'n':3,'slug':'watch-hand-in-trouser-pocket','kind':'watch','refs':['watch']+W,'people_line':PL,'comp':'D',
  'moment':'Standing by the ribbed concrete wall, his hand rests in his trouser pocket, the watch face turned out.',
  'shot':'Straight on, very close, 50mm, f/8, camera square to the watch face. The watch face sits on the centre line filling about 35 percent of the frame width, dead square, sharp; the rolled navy sleeve above, the grey pleated trouser and pocket around his hand, the cream vest hem at the top edge; hard flash shadow on the ribbed wall behind.'},
 {'n':4,'slug':'watch-crown-turn-close','kind':'watch','refs':['watch']+W,'people_line':PL,'comp':'D',
  'moment':'Sitting on the bench, he turns the watch crown with two fingers of his other hand.',
  'shot':'Very close, 50mm, f/8, camera square to the watch face. The watch face fills about 45 percent of the frame width on the centre line, dead square, sharp; two fingers of the other hand on the crown at the side; the navy cuff rolled above; the galvanised perforated bench seat soft below.'},
 {'n':5,'slug':'tablet-on-knee-from-above','kind':'ipad','refs':['ipad']+W,'people_line':PL,'comp':'B',
  'moment':'Sitting on the bench with one ankle on his knee, a tablet rests on his leg as he reads.',
  'shot':'From directly above, his point of view, 35mm, f/8. The tablet lies on his grey trouser leg, square to the frame, filling about 60 percent of the frame width, screen sharp; one hand holds its edge; the perforated bench and a brown loafer show at the edges; hard flash shadow tight under the tablet.'},
 {'n':6,'slug':'laptop-on-bench-beside-him','kind':'laptop','refs':['laptop','bench_perf']+W,'people_line':PL,'comp':'A',
  'moment':'Sitting at one end of the perforated bench, his laptop is open on the seat beside him.',
  'shot':'Low, at bench-seat height, 35mm, f/8, camera square to the screen. The laptop sits on the centre line on the perforated seat, screen dead square to the camera, filling about 55 percent of the frame width, sharp; his hand rests flat on the seat at the right edge with a slice of grey trouser behind; crisp flash shadow behind the laptop; black beyond.'},
]
