# n36 Terminal round 5 (Sam 26 Nov): 10 more. R4 finals: our wall display between brass lift doors, lightbox at end of glass jet bridge.
# R4: metro across tracks 'not bad but the screen is not realistic'; gallery lightbox with our oak bench 'bad bench'; library 'bad'. Screens must look like real units.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n36r3_more.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
from _nov_common import sh,SCREEN
C=dict(r3.C);C['id']='n36r5'
C['real']=r3.C['real']+' Every screen and lightbox is a real commercial unit with real thickness, a slim frame and real fixings, lit like a real panel, never a flat glowing shape pasted on the wall.'
LB=r3.LB
S=[
 sh(1,'wall-display-inside-brass-hotel-lift','Our wall display is fixed to the back wall of a brushed brass hotel lift car with the doors open.',
  'Camera in the open doorway at screen height, 35mm lens, f/5.6, square to the back wall. The screen fills about 50 percent of the frame width on the centre line, sharp; the brass walls and a slim handrail frame it; soft warm downlight from the ceiling.',
  SCREEN('THE WALL DISPLAY'),'the screen',refs=['pr01']),
 sh(2,'wall-display-concert-foyer-oak-wall-between-doors','Our wall display hangs on a warm oak-panelled wall between two padded doors in a concert hall foyer.',
  'Camera across the foyer at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 45 percent of the frame width on the centre line, sharp; the two closed doors frame it; pale stone floor with a soft fading reflection; soft evening light.',
  SCREEN('THE WALL DISPLAY'),'the screen',aspect='16:9',refs=['pr01']),
 sh(3,'portrait-lightbox-on-tiled-metro-column-train-blur','A portrait backlit lightbox is mounted on a white-tiled column on a clean metro platform while a train glides past behind.',
  'Camera on the platform at lightbox height, 50mm lens, f/5.6, slow shutter, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp, with its real aluminium frame and depth; the train is a soft horizontal blur behind.',
  LB,'the lightbox'),
 sh(4,'wall-display-spa-reception-travertine-reflecting-pool','Our wall display is set into a warm travertine wall above a low stone bench in a calm spa reception, a still reflecting pool in front.',
  'Camera at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 45 percent of the frame width on the centre line, sharp; the still pool across the lower frame mirrors it softly and fades at its edges; soft daylight.',
  SCREEN('THE WALL DISPLAY'),'the screen',aspect='16:9',refs=['pr01']),
 sh(5,'portrait-screen-beside-revolving-door-marble-lobby','A tall portrait digital screen stands on a slim steel foot beside the revolving door of a marble office lobby.',
  'Camera at screen height, 70mm lens, f/5.6, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; the glass revolving door softly out of focus beside it; polished marble floor with a soft reflection.',
  SCREEN('THE SCREEN'),'the screen'),
 sh(6,'screen-above-door-end-of-premium-train-carriage','A landscape screen sits above the sliding door at the end of a calm premium train carriage, leather seats either side of the aisle.',
  'Camera in the aisle at screen height, 50mm lens, f/5.6, square to the end wall. The screen fills about 55 percent of the frame width on the centre line, sharp; the seat backs and luggage racks converge toward it; soft daylight from the windows.',
  SCREEN('THE SCREEN'),'the screen'),
 sh(7,'lightbox-beside-arrival-doors-frosted-glass','A large landscape backlit lightbox is set into the pale stone wall beside the frosted sliding arrival doors of an airport arrivals hall.',
  'Camera across the hall at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 50 percent of the frame width, sharp; the frosted doors beside it glow softly; polished floor with a soft reflection.',
  LB,'the lightbox',aspect='16:9'),
 sh(8,'wall-display-private-jet-lounge-aircraft-nose','Our wall display hangs on a dark stone wall in a quiet private jet terminal lounge, beside a tall window with the nose of a parked jet outside.',
  'Camera at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 45 percent of the frame width, sharp; the jet nose is soft through the glass at one side; low leather chairs at the frame edge; soft daylight.',
  SCREEN('THE WALL DISPLAY'),'the screen',aspect='16:9',refs=['pr01']),
 sh(9,'portrait-lightbox-end-of-curved-white-tiled-tunnel','A portrait backlit lightbox closes the end wall of a curved, clean white-tiled pedestrian tunnel with a steel handrail.',
  'Camera in the middle of the tunnel at lightbox height, 50mm lens, f/5.6, square to the end wall. The lightbox fills about 60 percent of the frame height on the centre line, sharp; the tiled vault and handrails converge toward it; glossy floor with a soft fading reflection.',
  LB,'the lightbox'),
 sh(10,'wall-display-above-walnut-concierge-desk-evening','Our wall display hangs on a dark walnut-panelled wall above a walnut and brass concierge desk in a hotel lobby in the evening.',
  'Camera across the lobby at screen height, 50mm lens, f/5.6, square to the wall. The screen fills about 45 percent of the frame width on the centre line, sharp; the empty desk runs across the lower frame; warm low lamps either side.',
  SCREEN('THE WALL DISPLAY'),'the screen',refs=['pr01']),
]
