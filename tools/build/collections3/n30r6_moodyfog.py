# n30 Low Cloud round 6 (Sam 19 Oct): r5 finals 01, 04, 05; 'more moody fog'. Darker dusk, thicker lower fog swallowing everything behind the screen; still one even layer, never in front of the design surface.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r5=_m('n30r5_candid')
C=dict(r5.C);C['id']='n30r6'
C['world']=('A real city at late dusk in thick low fog: the fog sits low and heavy, swallowing the upper floors and everything a block behind the billboard or screen into soft grey; wet stone and asphalt; '
            'small warm lights blur into halos in the fog. The fog is one even, dense layer, never swirling banks, and never in front of the design surface.')
C['light']='Late blue-grey dusk under thick fog, darker than before; the billboard or screen is the brightest thing in the frame and makes a soft glow in the fog around it; street lights are soft halos.'
sh,SCR,BB,TINY,STD=r5.sh,r5.SCR,r5.BB,r5.TINY,r5.STD
S=[
 sh(1,'billboard-beside-motorway-overpass-fog-wide','A billboard stands beside a concrete motorway overpass at dusk in thick fog.',
  'Camera from the road below at billboard height, 70mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; the dark concrete underside of the overpass crosses the top of the frame; car headlights blur into soft streaks on the wet road below; the fog closes in behind it.'+STD,
  BB,'print','the billboard',wide=True),
 sh(2,'screen-above-shopping-centre-entrance-fog-wide','A landscape LED screen is fixed on the plain facade above the entrance of an ordinary shopping centre at dusk in thick fog.',
  'Camera from the car park at screen height, 85mm lens, f/2.8, square to it. The screen fills about 55 percent of the frame width, sharp; the lit glass entrance below with a few people walking in; the top of the building dissolves into fog.',
  'THE SCREEN '+SCR,people=TINY,wide=True),
 sh(3,'billboard-at-roundabout-headlights-fog-wide','A billboard stands at the edge of a large roundabout at dusk in thick fog.',
  'Camera at the roadside at billboard height, 50mm lens, f/2.8, square to it. The billboard fills about 50 percent of the frame width, sharp; cars curve around the roundabout below it, their headlights and tail lights glowing in the fog; wet asphalt; the far side of the roundabout lost in grey.'+STD,
  BB,'print','the billboard',wide=True),
 sh(4,'portrait-screen-elevated-train-platform-fog','A portrait digital screen stands on the platform of an elevated train station at dusk in thick fog.',
  'Camera on the platform at screen height, 50mm lens, f/2.8, square to it. The screen fills about 60 percent of the frame height on the centre line, sharp; the platform edge and rails run off to one side into fog; a single waiting figure in a dark coat stands further along the platform, small; platform lights are soft halos.',
  'THE SCREEN '+SCR,people=TINY),
 sh(5,'rooftop-billboard-long-street-into-fog','A billboard stands on the roof of a building far down a long, straight street that fades into thick fog at dusk.',
  'Camera in the middle of the street, 135mm lens, f/2.8, square to the billboard. The billboard fills about 55 percent of the frame width, sharp, glowing through the fog; the street lights in two lines recede into grey halos below it; the buildings around it are only soft grey shapes.'+STD,
  BB,'print','the billboard'),
]
