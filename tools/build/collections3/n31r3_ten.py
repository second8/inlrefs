# n31 Open Air round 3 (Sam 19 Oct): r2 finals all but 09 totem. 'Really nice, 10 more, keep this creativity going.' Same clean clear-day look, new places only.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n31r2_ten.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
C=dict(r2.C);C['id']='n31r3'
sh,PRINT,FEW=r2.sh,r2.PRINT,r2.FEW
BAN='THE BANNER IS PLAIN MATTE WHITE VINYL, pulled flat and taut with crisp edges, nothing printed on it and nothing crossing it.'
S=[
 sh(1,'billboard-on-seafront-promenade-wide','A billboard stands on the clean concrete wall of a seafront promenade; the calm sea line runs behind and below it.',
  'Camera on the promenade at billboard height, 50mm lens, f/8, square to it. The billboard fills about 55 percent of the frame width, sharp; the flat blue sea and a straight horizon behind it at the lower third; a simple railing and clean paving below; deep blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard',people=FEW,wide=True),
 sh(2,'row-of-ad-panels-along-tram-platform-wide','A row of identical portrait ad panels stands evenly spaced along a clean modern tram platform in the sun.',
  'Camera across the tracks at panel height, 35mm lens, f/8, square to the platform. The panels form an even row across the frame, the middle one on the centre line filling about 20 percent of the frame width, all sharp; the thin platform canopy above throws a crisp shadow band; the rails cross the foreground; blue sky.',
  'EVERY PANEL IS PLAIN PAPER-WHITE behind clean glass, flat with crisp corners, nothing printed on any of them.','the panels',wide=True),
 sh(3,'poster-on-white-park-pavilion-lawn-wide','A large landscape poster is fixed on the plain white side wall of a small modernist pavilion in a park, with a mown lawn in front.',
  'Camera on the lawn at poster height, 50mm lens, f/8, square to the wall. The poster fills about 55 percent of the frame width, sharp; the flat white wall and thin roof edge around it; the green lawn across the bottom; one tree at the frame edge; deep blue sky.',
  PRINT('THE POSTER'),'the poster',wide=True),
 sh(4,'banner-between-car-park-pillars-wide','A wide banner hangs taut between two concrete pillars across one level of a clean multi-storey car park facade.',
  'Camera across the street at banner height, 70mm lens, f/8, square to the facade. The banner fills about 60 percent of the frame width, sharp, tied to the pillars at its corners; the horizontal concrete floor slabs above and below; the dark open levels at the edges; hard sun.',
  BAN,'the banner',wide=True),
 sh(5,'long-banner-on-footbridge-side-from-riverbank-wide','A long horizontal banner is fixed along the side of a slim concrete footbridge over a river.',
  'Camera on the riverbank at the height of the bridge deck, 70mm lens, f/8, square to the bridge side. The banner runs across the frame, filling about 65 percent of the frame width, sharp; the calm river below reflects the bridge; the far bank and blue sky above.',
  BAN,'the banner',wide=True),
 sh(6,'pair-of-lamppost-banners','Two identical vertical banners hang side by side from a slim grey lamppost on a clean city street.',
  'Camera from across the street at banner height with a long lens, 135mm, f/8, square to them. The two banners hang on the centre line, together filling about 50 percent of the frame width, sharp, held flat by their top and bottom arms; the lamp head above; a clean white facade softly behind; blue sky.',
  'BOTH BANNERS ARE PLAIN MATTE WHITE FABRIC, flat and taut on their arms with crisp edges, nothing printed on them.','the banners'),
 sh(7,'billboard-on-terraced-house-gable-from-back-lane','A billboard is fixed high on the plain gable end of a row of terraced houses, seen from a quiet back lane.',
  'Camera in the lane at billboard height with a long lens, 100mm, f/8, square to the gable. The billboard fills about 60 percent of the frame width, sharp; the clean pale brick gable and the roof slope edges around it; the tops of garden walls at the bottom; blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard'),
 sh(8,'poster-in-glass-case-museum-colonnade','A portrait poster sits in a slim glass display case on the white wall of a museum colonnade, between two columns.',
  'Camera at poster height, 50mm lens, f/8, square to the case. The poster fills about 55 percent of the frame height on the centre line, sharp, behind clean glass with no reflection over it; two pale columns frame it; hard bars of sun and shadow fall across the stone floor.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE behind clean glass, flat with crisp corners, nothing printed on it and nothing crossing it.','the poster',comp='C'),
 sh(9,'tall-banner-down-stairwell-tower','A tall vertical banner hangs down the flat concrete face of a building\'s stairwell tower.',
  'Camera across the street with a long lens, 135mm, f/8, at mid height so the verticals stay parallel. The banner fills about 45 percent of the frame width and most of its height, sharp; the plain concrete tower around it with a thin strip of windows; blue sky above.',
  BAN,'the banner'),
 sh(10,'pasted-poster-white-lane-wall-sun-stripes','A portrait poster is pasted flat on a freshly painted white wall in a narrow lane; bars of hard sun and shadow fall across the wall beside it.',
  'Camera at poster height, 50mm lens, f/8, square to the wall. The poster fills about 55 percent of the frame height on the centre line, sharp, fully in the sun; crisp diagonal stripes of shadow from a railing cross the white wall around it, never over it; clean paving below.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted perfectly flat with crisp edges, nothing printed on it and nothing crossing it.','the poster'),
]
