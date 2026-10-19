# n31 Open Air round 4 (Sam 19 Oct): r3 all finals. 'This collection is looking amazing, please do 10 more.' Same clean clear-day look, new places.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n31r3_ten.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
C=dict(r3.C);C['id']='n31r4'
sh,PRINT,FEW,BAN=r3.sh,r3.PRINT,r3.FEW,r3.BAN
S=[
 sh(1,'billboard-above-shops-striped-awnings-wide','A billboard stands on the roof edge above a row of small shops with neat striped canvas awnings.',
  'Camera across the street at billboard height, 50mm lens, f/8, square to it. The billboard fills about 55 percent of the frame width, sharp; the row of awnings and shopfronts runs along the bottom of the frame in crisp sun and shadow; deep blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard',people=FEW,wide=True),
 sh(2,'wallscape-terracotta-mediterranean-street-wide','A large flat wallscape is mounted on a warm terracotta-rendered wall on a quiet Mediterranean street.',
  'Camera across the street at wallscape height, 50mm lens, f/8, square to the wall. The wallscape fills about 60 percent of the frame width, sharp; the warm render around it with two shuttered windows at the edges; clean stone paving below; deep blue sky.',
  PRINT('THE WALLSCAPE'),'the wallscape',wide=True),
 sh(3,'banner-on-white-wall-outdoor-pool-wide','A long banner is fixed on the clean white end wall of an outdoor swimming pool; the still blue water lies in front.',
  'Camera on the far side of the pool at banner height, 50mm lens, f/8, square to the wall. The banner fills about 60 percent of the frame width, sharp; the white wall and a thin tiled edge; the calm blue pool water across the lower third with soft reflections; deep blue sky above.',
  BAN,'the banner',wide=True),
 sh(4,'billboard-beside-motorway-long-lens-wide','A large billboard stands on its steel frame beside a motorway on a clear day.',
  'Camera from the opposite verge with a long lens, 200mm, f/8, at billboard height, square to it. The billboard fills about 60 percent of the frame width, sharp; the grey guard rail and a lane of the road run along the bottom; a few cars as soft streaks; dry grass and deep blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard',wide=True),
 sh(5,'side-panel-of-city-bus-at-stop-wide','A clean city bus stands at a stop; its long side carries a full advertising panel between the windows and the wheels.',
  'Camera across the street at panel height, 50mm lens, f/8, square to the bus side. The panel fills about 65 percent of the frame width, sharp; the dark windows above it and the wheels below; clean pavement and a low wall behind; blue sky.',
  'THE BUS PANEL IS PLAIN MATTE WHITE VINYL, flat and taut with crisp corners, nothing printed on it and nothing crossing it.','the bus panel',wide=True),
 sh(6,'lightbox-at-metro-entrance-steps-down','A portrait lightbox stands at the top of a clean metro entrance, beside the steps going down.',
  'Camera at the top of the steps at lightbox height, 50mm lens, f/8, square to it. The lightbox fills about 60 percent of the frame height on the centre line, sharp, in its slim frame; the steps drop away beside it into shade; a clean handrail; the sunny street and blue sky above.',
  'THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat with crisp corners, nothing printed on it and nothing crossing it.','the lightbox'),
 sh(7,'billboard-on-narrow-corner-building','A billboard stands on the roof of a narrow corner building where two streets meet.',
  'Camera far down the street with a long lens, 135mm, f/8, at billboard height, square to it. The billboard fills about 60 percent of the frame width, sharp; the slim pale building rises below it like a prow; deep blue sky around.',
  PRINT('THE BILLBOARD FACE'),'the billboard'),
 sh(8,'banner-under-stone-portico-between-columns','A tall vertical banner hangs under a stone portico between two columns.',
  'Camera at the foot of the portico steps, 50mm lens, f/8, square to the banner. The banner fills about 40 percent of the frame width and most of the height between the two pale columns, sharp; the shaded portico behind; hard sun on the columns and the steps.',
  BAN,'the banner',comp='C'),
 sh(9,'poster-on-plywood-hoarding-tree-shadow','A portrait poster is pasted on a clean pale plywood site hoarding; the sharp shadow of a street tree falls across the boards beside it.',
  'Camera at poster height, 50mm lens, f/8, square to the hoarding. The poster fills about 55 percent of the frame height on the centre line, sharp, fully in sun; the leafy shadow pattern of the tree falls on the plywood around it, never over the poster; clean pavement below.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted perfectly flat with crisp edges, nothing printed on it and nothing crossing it.','the poster'),
 sh(10,'poster-beside-doorway-pale-pink-wall','A portrait poster is pasted flat on a clean pale pink rendered wall next to a single plain doorway.',
  'Camera at poster height, 50mm lens, f/8, square to the wall. The poster fills about 50 percent of the frame height, sharp, a little left of centre; the simple dark doorway beside it; a crisp diagonal shadow from the roof edge crosses the upper wall, never over the poster; clean step and paving below.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted perfectly flat with crisp edges, nothing printed on it and nothing crossing it.','the poster'),
]
