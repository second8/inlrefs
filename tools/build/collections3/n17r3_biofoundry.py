# n17 round 3. Sam: 03 (wall display above fume hoods at night) works, just brighter screen; 04 (sign panel by airlock) works;
# 02 (tablet white bench) almost; 01 (gloved touchscreen) too AI; 05 laptop needs a brighter screen.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n17r_biofoundry.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n17r3';C['name']='Biofoundry (round 3)'
C['finish']='Shot on a full-frame camera with 35mm and 50mm lenses at f/2.8 to f/4: fine grain, slightly soft corners, no halation. Feels like a calm documentary frame from inside the lab, sleek but real.'
I1=_m.I1;I2=_m.I2
NIGHT=(I1,'dim blue-hour light, colour, grade and mood')
DAY=(I2,'pale white and blue-grey colour, soft light and grade')
S=[
 {'n':1,'slug':'display-above-freezer-row-night','kind':'monitor','noun':'the wall display','refs':['display'],'people':'none','looks':[NIGHT],
  'moment':'Late in the evening, a slim wall display above the row of stainless freezers shows the overnight run.',
  'shot':'Three-quarter from the corridor, camera at standing height, 35mm, f/2.8. The slim landscape display is mounted on the graphite wall above three brushed-steel upright freezers, filling about 45 percent of the frame width, sharp. The freezer doors catch faint cool reflections; the corridor floor is pale and dim; the far end falls into blue-grey shadow.'},
 {'n':2,'slug':'display-end-of-bench-row','kind':'monitor','noun':'the display','refs':['display'],'people':'none','looks':[NIGHT],
  'moment':'At the end of a row of benches, a large display on a slim stand faces the room after hours.',
  'shot':'From the aisle between benches, standing height, 50mm, f/2.8. The large display on a slim stand sits at the far end of a black resin bench, filling about 50 percent of the frame width, sharp; glass instrument enclosures glow faintly on both sides, soft. The bench surface leads toward it, with a closed graphite binder and a tube rack near the camera, out of focus.'},
 {'n':3,'slug':'sign-panel-freezer-wall','kind':'sign','noun':'the wall sign panel','refs':[],'people':'none','looks':[DAY],
  'moment':'A flush sign panel on the white wall marks the cold-storage zone beside the freezer row.',
  'shot':'Frontal and slightly off-axis, 50mm, f/4, at eye height. The portrait sign panel, a slim flat plate mounted flush on the white wall, fills about 55 percent of the frame height, sharp. The edge of the first brushed-steel freezer is soft at the left; the pale grey floor and a steel kick plate run along the bottom.',
  'surface':'THE SIGN PANEL IS PLAIN BLANK WHITE, matte, perfectly flat with crisp square corners and a fine shadow gap around it, nothing printed on it.'},
 {'n':4,'slug':'tablet-bench-tube-rack','kind':'ipad','refs':['ipad'],'people':'her','edge':'right','looks':[DAY],
  'moment':'A tablet lies on the white bench next to a rack of capped tubes while a run is being set up.',
  'shot':'From standing, looking down at about 65 degrees, 50mm, f/4. The tablet lies flat on the white bench, filling about 60 percent of the frame width, sharp; a white rack of capped tubes stands just above it. Her black-gloved fingertips rest on the bench at the right edge, soft. The rest of the bench falls away pale and out of focus.'},
 {'n':5,'slug':'laptop-steel-bench-close','kind':'laptop','refs':['laptop'],'people':'none','looks':[NIGHT],
  'moment':'A laptop open on a stainless bench in the dim lab after hours, its screen the brightest thing in the room.',
  'shot':'Close three-quarter from the left at seated height, 50mm, f/2.8. The open laptop fills about 65 percent of the frame width on the brushed-steel bench, screen sharp and keyboard slightly soft; the steel shows faint scratches and a cool reflection of the screen. The glass enclosures behind glow faintly blue and soft.'},
]
