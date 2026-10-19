# c4 round 5, agreed with Sam 16 Oct: back to the round 2 look (r2-01 red stool sun grid, r2-02 oak bench beam, r2-03 dusk window),
# our own props (prop_25 ochre stool, prop_26 oak bench), no inspo props or compositions, square-on design, brighter screens.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c4r3_beam.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
R2_1='https://media.weavy.ai/image/upload/v1792156550/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/crllqyc7jyxvnjsol00t.png'
R2_2='https://media.weavy.ai/image/upload/v1792156559/uploads/UIgNcQSdhvf7IEtHbILU1Ra8CZC3/mtnoeh1naoghf3yk7cvh.png'
LOOK='hard late sunlight, the crisp window-grid shadows, warm colour, grade, grain and deep shadow'
C=dict(_m.C);C['id']='c4r5';C['name']='Beam (round 5)'
C['world']='A dim old apartment with wide honey-oak floorboards, dark charcoal limewash walls and deep windows with slim dark mullions. Almost everything sits in shadow; only where the sun lands is anything bright.'
C['avoid']=['readable lettering or logos','a face or profile','a second light source or fill','any object not named in the shot','a glass, a cup, earbuds or a red stool','halation or glow']
S=[
 {'n':1,'slug':'laptop-oak-bench-sun-grid','kind':'laptop','refs':['laptop','bench_oak'],'people':'none','looks':[(R2_2,LOOK)],
  'moment':'A laptop left open on the low oak bench, hard late sun falling across it in a window-grid pattern.',
  'shot':'From standing, about 35 degrees down, 50mm, f/2.8, close. The laptop sits on the bench top with its screen facing the camera almost square-on, filling about 65 percent of the frame width; screen sharp, keyboard slightly soft. A folded oatmeal linen cloth lies at the right end of the bench, nothing else. The sun grid crosses the bench and the floorboards; the charcoal wall behind is nearly black.'},
 {'n':2,'slug':'laptop-ochre-stool-sun-grid','kind':'laptop','refs':['laptop','stool_ochre'],'people':'none','looks':[(R2_1,LOOK)],
  'moment':'A laptop open on the small ochre stool, standing in a patch of late sun broken by window-frame shadows on the oak floor.',
  'shot':'From standing, about 40 degrees down, 50mm, f/2.8, close. The laptop sits on the stool top, its screen facing the camera nearly square-on, filling about 65 percent of the frame width, sharp. The broken grid of mullion shadows falls across the stool and the floorboards; the room around falls into shadow at the frame edges.'},
 {'n':3,'slug':'display-desk-steel-window-dusk','kind':'display','refs':['display'],'people':'none',
  'moment':'After sunset, a desktop display on an oak desk sits side-on to a tall steel-framed window over dusk city rooftops.',
  'shot':'Camera at desk height, 50mm, f/2.8. The display faces the camera almost square-on, filling about 55 percent of the frame width, sharp. To its left, the tall window with slim black steel frames divided into small panes shows a blue-grey dusk sky over dark city rooftops, soft. The display is the main light, falling on the oak desk; the rest of the room is deep shadow.'},
 {'n':4,'slug':'tablet-window-seat-sun-grid','kind':'ipad','refs':['ipad'],'people':'none','looks':[(R2_1,LOOK)],
  'moment':'A tablet lying flat on the deep oak window seat, the late sun laying the window grid across the seat beside it.',
  'shot':'From nearly straight above, 50mm, f/2.8, close. The tablet lies flat on the oak seat, filling about 65 percent of the frame width, sharp; one mullion shadow line crosses the seat next to it but never the screen. The edge of the seat and the floor below fall into shadow.'},
 {'n':5,'slug':'poster-on-bench-sun-grid','kind':'print','noun':'the poster','refs':['bench_oak'],'people':'none','looks':[(R2_2,LOOK)],
  'moment':'A large poster stands on the low oak bench, leaning back against the charcoal wall, the sun grid lying across it.',
  'shot':'Straight on, camera at bench height, 50mm, f/2.8, close. The portrait poster on thick board leans on the wall, its bottom edge resting on the bench top, filling about 70 percent of the frame height, sharp, facing the camera square-on. The window-grid shadow lies across its upper half; the wall and floor fall to near black.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE thick matte board, perfectly flat and rigid, crisp square corners, nothing printed on it.','avoid':['a curled or warped corner','a frame or glass']},
]
