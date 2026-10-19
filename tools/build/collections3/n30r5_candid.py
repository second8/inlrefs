# n30 Low Cloud round 5 (Sam 19 Oct): all five r4 picked as finals. Same candid look, new everyday places.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r4',os.path.join(os.path.dirname(__file__),'n30r4_candid.py'));r4=importlib.util.module_from_spec(_s);_s.loader.exec_module(r4)
C=dict(r4.C);C['id']='n30r5'
sh,SCR,BB,TINY,STD=r4.sh,r4.SCR,r4.BB,r4.TINY,r4.STD
S=[
 sh(1,'billboard-above-petrol-station-canopy-wide','A standard billboard stands on poles behind a petrol station at dusk, rising above the lit canopy.',
  'Camera from across the road at billboard height, 70mm lens, f/2.8, square to it. The billboard fills about 55 percent of the frame width, sharp; the flat white canopy of the petrol station glows below it with a couple of cars at the pumps; wet forecourt; one flat layer of low cloud above.'+STD,
  BB,'print','the billboard',people=TINY,wide=True),
 sh(2,'billboard-side-of-multistorey-car-park-wide','A billboard is fixed to the concrete side of a multi-storey car park at dusk.',
  'Camera from the street at billboard height, 85mm lens, f/2.8, square to it. The billboard fills about 55 percent of the frame width, sharp; the plain concrete levels of the car park with their horizontal openings above and below it, a few car lights inside; one flat layer of low cloud above.'+STD,
  BB,'print','the billboard',wide=True),
 sh(3,'billboard-behind-chain-link-fence-empty-lot-wide','A billboard stands behind a chain-link fence across an empty gravel lot at dusk.',
  'Camera at the fence, standing height, 50mm lens, f/2.8, square to the billboard. The billboard fills about 55 percent of the frame width, sharp, on its steel frame across the lot; the out-of-focus top of the chain-link fence runs across the very bottom of the frame, never over the billboard; puddles in the gravel; one flat layer of low cloud.'+STD,
  BB,'print','the billboard',wide=True),
 sh(4,'screen-top-of-metro-entrance-stair','A portrait digital screen hangs on the wall at the top of a metro entrance stair at dusk.',
  'Camera at the top of the stair at screen height, 50mm lens, f/2.8, square to the screen. The screen fills about 60 percent of the frame height, sharp, set into the tiled wall; the handrail and the first steps going down at the lower edge; wet pavement light from the street behind; one flat layer of low cloud through the opening.',
  'THE SCREEN '+SCR,people=TINY),
 sh(5,'rooftop-billboard-past-tram-stop','A billboard stands on the roof of a low building seen past a tram stop at dusk.',
  'Camera from the tram platform at billboard height, 85mm lens, f/2.8, square to it. The billboard fills about 70 percent of the frame width, sharp; the thin tram wires cross the sky above it, never over its face; the edge of the tram stop roof at the lower corner; one flat layer of low cloud.'+STD,
  BB,'print','the billboard'),
]
