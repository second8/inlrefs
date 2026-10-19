# n30 Low Cloud round 7 (Sam 19 Oct): all five r6 finals. 'keep going, right track, like the candid looks. do 10 now, mix vertical and horizontal.' Same look as r6 (moody fog).
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r6=_m('n30r6_moodyfog')
C=dict(r6.C);C['id']='n30r7'
sh,SCR,BB,TINY,STD=r6.sh,r6.SCR,r6.BB,r6.TINY,r6.STD
S=[
 sh(1,'billboard-behind-bus-depot-fog-wide','A billboard stands behind a city bus depot at dusk in thick fog.',
  'Camera at the depot fence at billboard height, 70mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; a row of parked buses with a few lit windows sits below it; wet tarmac; the fog swallows everything behind.'+STD,
  BB,'print','the billboard',wide=True),
 sh(2,'billboard-on-slope-above-suburban-road-fog-wide','A billboard stands on a grassy slope above a quiet suburban road at dusk in thick fog.',
  'Camera from the opposite side of the road at billboard height, 85mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; the road curves below it with a line of street lights fading into fog; one car passing with soft headlights.'+STD,
  BB,'print','the billboard',wide=True),
 sh(3,'billboard-on-harbour-edge-cranes-in-fog-wide','A billboard stands on the edge of a harbour at dusk; tall cranes behind it fade into thick fog.',
  'Camera on the quay at billboard height, 70mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; the dark water and quay edge below it; the cranes and stacked containers behind are only grey shapes in the fog.'+STD,
  BB,'print','the billboard',wide=True),
 sh(4,'billboard-beside-level-crossing-fog-wide','A billboard stands beside a railway level crossing at dusk in thick fog; the barrier is down and its red lights glow.',
  'Camera at the crossing at billboard height, 50mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; the striped barrier arm and its two small red lights cross the lower part of the frame, never over the billboard; rails running off into fog.'+STD,
  BB,'print','the billboard',wide=True),
 sh(5,'billboard-on-warehouse-roof-ring-road-fog-wide','A billboard stands on the flat roof of a long warehouse beside a ring road at dusk in thick fog; a truck passes below.',
  'Camera from the road shoulder at billboard height, 85mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; the plain warehouse wall below; one truck with soft lights passes on the wet road; everything beyond lost in fog.'+STD,
  BB,'print','the billboard',wide=True),
 sh(6,'portrait-screen-at-pedestrian-underpass-entrance-fog','A portrait digital screen is fixed on the concrete wall at the entrance of a pedestrian underpass at dusk in thick fog.',
  'Camera at the top of the ramp at screen height, 50mm lens, f/2.8, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; the ramp slopes down beside it into the lit tunnel; a handrail; fog hangs in the street behind.',
  'THE SCREEN '+SCR,people=TINY),
 sh(7,'poster-billboard-end-of-narrow-residential-street-fog','A poster billboard is fixed to the end wall of a narrow residential street at dusk in thick fog.',
  'Camera in the middle of the street, 85mm lens, f/2.8, square to it. The poster fills about 60 percent of the frame width, sharp, lit by its small lamps; parked cars line both sides of the street leading to it; the rooftops above dissolve into fog.',
  'THE POSTER IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.','print','the poster'),
 sh(8,'portrait-screen-at-parking-garage-ramp-fog','A portrait digital screen stands at the entrance ramp of a concrete parking garage at dusk in thick fog.',
  'Camera on the pavement at screen height, 50mm lens, f/2.8, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; the dark ramp mouth and low concrete beams beside it with a few strip lights inside; wet ground; fog behind.',
  'THE SCREEN '+SCR),
 sh(9,'billboard-above-canal-from-footbridge-fog','A billboard stands above the far bank of a city canal at dusk in thick fog, seen from a small footbridge.',
  'Camera on the footbridge at billboard height, 85mm lens, f/2.8, square to it. The billboard fills about 60 percent of the frame width, sharp; its light lies as a soft long reflection on the still dark water below; the canal walls run off into fog.'+STD,
  BB,'print','the billboard'),
 sh(10,'pole-screen-small-square-bare-trees-fog','A portrait digital screen on a simple grey pole stands in a small city square with bare winter trees at dusk in thick fog.',
  'Camera at standing height, 50mm lens, f/2.8, square to the screen. The screen fills about 60 percent of the frame height on the centre line, sharp; the bare black branches of the trees behind fade into the fog; wet paving; one person in a dark coat walks past far behind, small.',
  'THE SCREEN '+SCR,people=TINY),
]
