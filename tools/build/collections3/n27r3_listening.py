# n27 round 3. Sam: 01 (sleeve on stand) works, a bit closer and less of the character; 03 (sleeve from shelf) works, no halation,
# more intentional; 02 (streamer) too perfect and far; 04 bad (crossed); 05 (projection) almost.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n27r3';C['name']='Listening Room (round 3)'
C['finish']='Shot handheld on a 35mm film camera, 50mm lens almost wide open at f/1.4, on tungsten-balanced 800-speed film: heavy fine grain, no halation or glow around the lights, very shallow focus so most of the frame melts into soft dark shapes. It feels like a frame taken quietly during a record.'
C['avoid']=['lettering or logos in focus','a face or profile','a wall packed with records','numbers or markings on knobs and dials','halation or glow around lights']
I3=_m.I3;LOOK=_m.LOOK
S=[
 {'n':1,'slug':'sleeve-on-stand-close','kind':'print','noun':'the record sleeve','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'The sleeve of the record now playing stands on its small walnut stand on the counter, just placed.',
  'shot':'From a seat at the counter, close, 50mm, f/1.4. The square 12-inch sleeve stands upright on a small walnut stand in a pinspot, filling about 75 percent of the frame height, slightly left of centre, sharp. Nobody is in the frame. Behind, almost everything is black: one pendant is a small warm blur, the aluminium rack a faint silver edge.',
  'surface':'THE SLEEVE FRONT IS PLAIN BLANK WHITE matte board, square, standing straight and flat, crisp corners, lit by the pinspot, nothing printed on it.'},
 {'n':2,'slug':'sleeve-half-out-shelf-low','kind':'print','noun':'the record sleeve','refs':[],'people':'her','edge':'top','looks':[(I3,LOOK)],
  'moment':'The next record is drawn halfway out of the walnut shelf, only two fingertips on its top edge.',
  'shot':'Low and close, 50mm, f/1.4, level with the middle of the shelf. The square sleeve is pulled halfway out from between plain dark spines and tilted slightly toward the camera, filling about 70 percent of the frame, sharp; two fingertips touch its top edge from the top of the frame. The spines on either side are soft and dark; beyond the shelf everything is black.',
  'surface':'THE SLEEVE FRONT IS PLAIN BLANK WHITE matte board, square, flat and rigid, crisp corners, lit by the pinspot, nothing printed on it.'},
 {'n':3,'slug':'streamer-display-close-low','kind':'screen','noun':'the streamer display','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'The streamer front display glows on the aluminium rack between the speakers while a side plays.',
  'shot':'Close and low, camera level with the display, 50mm, f/1.4. The brushed-aluminium streamer front fills most of the frame width, its wide display about 70 percent of the frame width, sharp; fine dust and a fingerprint on the aluminium, a cable dropping behind the rack. Everything above and behind falls straight into black.',
  'surface':'THE DISPLAY SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, bright and clean, the brightest thing in the frame but not blown out, crisp corners in a thin black frame; nothing crosses it.'},
 {'n':4,'slug':'projection-from-second-row','kind':'screen','noun':'the projection screen','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'On a film-score night, the projection glows between the horn speakers, seen from the second row of armchairs.',
  'shot':'From a seat in the second row, 50mm, f/1.4. The landscape projection screen fills about 70 percent of the frame width, sharp. The dark curved backs of two front-row wool armchairs crop in along the bottom edge as black shapes; the horn speakers rise soft and dark at both sides. Everything except the screen falls into deep shadow.',
  'surface':'THE SCREEN SHOWS A PLAIN WHITE PROJECTED IMAGE, bright and clean, the brightest thing in the room but not blown out, crisp edges on the matte screen; nothing crosses it.'},
 {'n':5,'slug':'ipad-library-counter-pinspot','kind':'ipad','refs':['ipad'],'people':'her','edge':'right','looks':[(I3,LOOK)],
  'moment':'The host browses the record library on a tablet lying on the worn walnut counter between sides.',
  'shot':'From standing across the counter, looking down at about 55 degrees, 50mm, f/1.4. The tablet lies flat on the walnut counter in a pinspot, filling about 60 percent of the frame width, sharp; her fingertip touches its lower right corner from the right edge. The counter edge, worn paler where elbows rest, falls soft; the rest is black.'},
]
