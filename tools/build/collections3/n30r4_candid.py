# n30 Low Cloud round 4 (Sam 19 Oct): r3 finals 01, 02, 05. Pins: 01 'too long', 02 'a bit more realistic, works', 03 arena 'trying too much, doesn't make sense',
# 04 'too unique, more candid', 05 'works'. So: ordinary, candid city billboards and screens, same grade, one simple cloud layer, some 16:9.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n30r3_wide.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
C=dict(r3.C);C['id']='n30r4'
C['register']='A candid, ordinary city photograph at dusk under low cloud, the kind a street photographer takes in passing'
sh,SCR,BB,TINY=r3.sh,r3.SCR,r3.BB,r3.TINY
STD=' It is an ordinary, everyday billboard of standard proportions, about three times as wide as it is tall, nothing special about its structure.'
S=[
 sh(1,'standard-billboard-low-rooftop-crossroads-wide','A standard billboard stands on the flat roof of a low corner building at an ordinary city crossroads at dusk.',
  'Camera at the opposite street corner, a little raised, 70mm lens, f/2.8, square to the billboard. It fills about 55 percent of the frame width, sharp, on its plain steel frame above the corner shop; traffic lights and a couple of parked cars below; wet asphalt; one flat layer of low cloud above.'+STD,
  BB,'print','the billboard',people=TINY,wide=True),
 sh(2,'led-screen-building-corner-shopping-street-wide','An ordinary LED advertising screen is fixed to the corner of a building above a shopping street at dusk.',
  'Camera from across the street at the height of the screen, 85mm lens, f/2.8, square to it. The landscape screen fills about 55 percent of the frame width, sharp; plain shop signs-free facades around it with a few lit windows; the street below with passers-by; the building top meets one flat layer of low cloud.',
  'THE SCREEN '+SCR,people=TINY,wide=True),
 sh(3,'billboard-wall-beside-railway-from-platform-wide','A billboard is mounted on a brick wall beside a railway line, seen from the station platform across the tracks at dusk.',
  'Camera on the platform at the height of the billboard, 50mm lens, f/2.8, square to it. The billboard fills about 60 percent of the frame width, sharp, its small lamps lighting it; the empty tracks and gravel run across the lower part of the frame; overhead wires cross the sky above, never over the billboard; one flat layer of low cloud.'+STD,
  BB,'print','the billboard',wide=True),
 sh(4,'poster-billboard-apartment-side-wall','A large poster billboard covers part of the blank side wall of an apartment block at dusk.',
  'Camera from the street at the middle height of the poster, 85mm lens, f/2.8, square to it. The poster fills about 65 percent of the frame height, sharp, lit by a row of small lamps above it; the plain concrete wall around it with a few balconies at the edge; the roof line meets one flat layer of low cloud.',
  'THE POSTER IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.','print','the poster'),
 sh(5,'portrait-digital-screen-pole-pedestrian-street','A portrait digital screen on a simple grey pole stands in a pedestrian street at dusk while people walk past.',
  'Camera at standing height, 50mm lens, f/2.8, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; people in dark coats walk past behind it, soft and small; the wet paving reflects its light; the street of plain facades fades into one flat layer of low cloud.',
  'THE SCREEN '+SCR,people=TINY),
]
