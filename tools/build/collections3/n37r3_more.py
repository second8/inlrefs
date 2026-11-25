# n37 Night Square round 3 (Sam 25 Nov): R2 all-white all final, 'really nice, do more'. Same world, 5 new vantage points and screen setups.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n37r2_allwhite.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
from _nov_common import sh
C=dict(r2.C);C['id']='n37r3'
ALL=r2.ALL
S=[
 sh(1,'from-raised-steps-across-square-to-stacked-screens','From a set of raised outdoor seating steps in the middle of the square, a facade across the street carries three big flat screens stacked one above another.',
  'Camera on the top of the steps at the height of the middle screen, 85mm lens, f/5.6, square to the facade. The three stacked screens fill about 60 percent of the frame width on the centre line, sharp; the edge of the empty steps runs along the bottom of the frame; dark towers either side.',ALL,'the screens',aspect='16:9'),
 sh(2,'screen-above-subway-entrance-lamp-posts','A big landscape screen sits on the facade directly above a subway entrance with two old iron lamp posts glowing either side of its stairs.',
  'Camera across the street at screen height, 70mm lens, f/5.6, square to it. The screen fills about 55 percent of the frame width on the centre line, sharp; the stair railing and the two lamp globes sit below it; the wet pavement shines.',ALL,'the screens'),
 sh(3,'double-height-screen-over-glass-storefront-bus-blur','A double-height flat screen covers the front of a building above a tall glass storefront; a city bus passes in front as a long blur.',
  'Camera across the street at screen height, 50mm lens, f/4, slow shutter, square to it. The screen fills about 55 percent of the frame width, sharp; the bus is a long soft blur along the bottom third, below the screen, never over it; the lit glass storefront below.',ALL,'the screens'),
 sh(4,'twin-vertical-screens-flanking-hotel-canopy','Two tall vertical flat screens flank the entrance of a grand hotel on the square, above its lit canopy.',
  'Camera across the street at the height of the screens middle, 85mm lens, f/5.6, square to the facade, centred between them. Both screens together fill about 60 percent of the frame width, sharp, mirror-symmetric; the warm canopy lights below; wet street in front.',ALL,'the screens'),
 sh(5,'big-billboard-and-its-puddle-reflection','A giant landscape billboard on a tower across the square and its reflection in a wide, still rain puddle on the asphalt.',
  'Camera low just above the puddle, 50mm lens, f/8, aimed so the billboard stays square and its edges parallel to the frame. The billboard fills about 50 percent of the frame width in the upper half, sharp; the still puddle mirrors it cleanly in the lower half and the reflection fades softly at its edges; other white screens on the towers around.',ALL,'the screens'),
]
