# n31 Open Air round 2 (Sam 19 Oct): r1 finals all but 06; 06 subway 'just make it cleaner, don't use dirt'. 'You nailed this direction, make 10 more, all great.'
import importlib.util,os
_s=importlib.util.spec_from_file_location('r1',os.path.join(os.path.dirname(__file__),'n31r1_openair.py'));r1=importlib.util.module_from_spec(_s);_s.loader.exec_module(r1)
C=dict(r1.C);C['id']='n31r2'
C['real']=C['real'].replace('with small honest signs of weather and age on the place only','with the place clean and well kept, no dirt, grime, stains or graffiti')
C['avoid']=C['avoid']+['dirt, grime, stains or graffiti']
sh,PRINT,FEW=r1.sh,r1.PRINT,r1.FEW
SCR='THE SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, bright and clean in the daylight, evenly lit edge to edge, crisp corners meeting its thin dark frame; nothing crosses it.'
S=[
 sh(1,'three-small-posters-on-black-hoarding-bench-wide','Three identical small posters are pasted in a neat row on a long matte black painted hoarding beside a pavement; a simple metal bench stands in front.',
  'Camera across the pavement at poster height, 50mm lens, f/8, square to the hoarding. The three posters sit side by side with even gaps, together filling about 55 percent of the frame width, the middle one on the centre line, all sharp; the low metal bench below them; a plain building and blue sky above the hoarding; hard sun and a crisp shadow line across the black.',
  'EVERY POSTER IS PLAIN MATTE PAPER-WHITE, pasted flat with crisp edges, nothing printed on any of them.','the posters',wide=True),
 sh(2,'poster-on-pale-corrugated-metal-wall-wide','A large landscape poster is fixed flat on a long pale grey corrugated metal wall in hard sun.',
  'Camera across the road at poster height, 50mm lens, f/8, square to the wall. The poster fills about 55 percent of the frame width, sharp, flat on a smooth backing board over the ribs; the vertical ribs of the metal throw fine parallel shadows on either side; a strip of pavement below and deep blue sky above with the top of a tree at one edge.',
  PRINT('THE POSTER'),'the poster',wide=True),
 sh(3,'ad-on-side-of-parked-truck-trailer-wide','A clean white truck trailer is parked along a quiet street, its long flat side carrying a full-length advertising panel.',
  'Camera across the street at the height of the panel, 50mm lens, f/8, square to the trailer. The panel fills about 70 percent of the frame width, sharp, edge to edge along the trailer side; the wheels and a sliver of the cab at one end; clean asphalt below; low buildings and blue sky above.',
  'THE TRAILER PANEL IS PLAIN MATTE WHITE VINYL, flat and taut edge to edge with crisp corners, nothing printed on it and nothing crossing it.','the trailer panel',wide=True),
 sh(4,'long-billboard-under-bridge-shade-bright-street-wide','A long landscape billboard is fixed on a concrete wall in the deep shade under a bridge; beyond the bridge the street is bright with sun.',
  'Camera in the shade at billboard height, 35mm lens, f/8, square to the wall. The billboard fills about 70 percent of the frame width, sharp, evenly lit by soft reflected daylight; the dark underside of the bridge forms a band across the top of the frame; at the edges the opening shows the bright sunlit street and blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard',wide=True),
 sh(5,'clean-long-poster-on-white-subway-tiles-wide','A long landscape poster is pasted perfectly flat on a spotless wall of small white square tiles in a modern, very clean underground station.',
  'Camera on the opposite platform at poster height, 35mm lens, f/8, square to the wall. The poster fills about 70 percent of the frame width, sharp, its edges parallel to the clean tile grid; bright white tiles on all sides, crisp grout lines; a clean dark platform edge strip along the bottom; even bright station light.',
  'THE POSTER IS PLAIN MATTE PAPER-WHITE, pasted perfectly flat with crisp edges, nothing printed on it and nothing crossing it.','the poster',wide=True),
 sh(6,'bus-shelter-panel-sunny-kerb','A clean modern bus shelter stands on a sunny pavement; its tall ad panel faces the camera.',
  'Camera on the kerb at panel height, 50mm lens, f/8, square to the panel. The portrait panel fills about 60 percent of the frame height on the centre line, sharp, in its slim aluminium frame; the thin shelter roof above casts a crisp shadow line; clean pavement, a low wall and blue sky behind.',
  'THE PANEL IS PLAIN PAPER-WHITE behind clean glass, flat edge to edge with crisp corners, nothing printed on it and nothing crossing it.','the panel',people=FEW),
 sh(7,'banner-wrapping-side-of-tall-building','A huge vertical banner covers almost the whole blank side wall of a tall plain building.',
  'Camera from a long way down the street, 135mm lens, f/8, at mid height so the verticals stay parallel. The banner fills about 55 percent of the frame width and most of the height, sharp, taut on its frame; the plain wall edges and a few windows of the neighbouring buildings at the sides; a strip of blue sky above.',
  'THE BANNER IS PLAIN MATTE WHITE VINYL, pulled flat and taut with crisp edges, nothing printed on it and nothing crossing it.','the banner'),
 sh(8,'billboard-above-tree-lined-avenue','A billboard stands on a rooftop at the far end of a straight tree-lined avenue.',
  'Camera in the middle of the avenue with a long lens, 200mm, f/8, square to the billboard. The billboard fills about 60 percent of the frame width, sharp, compressed above the rooftops; rows of green trees on both sides frame it; clean road below; deep blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard',comp='C'),
 sh(9,'digital-totem-in-sunny-plaza','A slim portrait digital totem stands on a wide sunny stone plaza.',
  'Camera at standing height, 50mm lens, f/8, square to the screen. The totem screen fills about 60 percent of the frame height on the centre line, sharp; its hard shadow falls across the pale paving; a low modern building and blue sky behind.',
  SCR,'the screen',people=FEW,kind='led'),
 sh(10,'billboard-on-white-rooftop-from-terrace','A billboard stands on the flat roof of a clean white modern building, seen from a rooftop terrace across the street.',
  'Camera on the terrace at billboard height, 70mm lens, f/8, square to it. The billboard fills about 65 percent of the frame width, sharp, on its slim steel frame; the clean white roof edge below; the top edge of the terrace railing runs across the very bottom of the frame, never over the billboard; deep blue sky.',
  PRINT('THE BILLBOARD FACE'),'the billboard'),
]
