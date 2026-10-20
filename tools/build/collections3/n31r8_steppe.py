# n31 Open Air round 8 (Sam 20 Oct): r7 13 of 20 finals; 05 circular window 'don't make these, more realistic'; 10 railway 'too AI'; 11 containers 'not real';
# 08 basketball 'perfect, more like this'; 13 underpass 'really nice candid'; 16 track 'nice, I like the sport theme'.
# 'I need 5 more final images, comp and everything in the style of the new inspo' (board inspo, WORDS ONLY): a lone blank billboard on bare scaffolding
# in vast dry steppe scrubland, low mountains, scattered cumulus, warm low sun, quiet editorial landscape photography, board medium-small in frame, 4:3.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r3',os.path.join(os.path.dirname(__file__),'n31r3_ten.py'));r3=importlib.util.module_from_spec(_s);_s.loader.exec_module(r3)
C=dict(r3.C);C['id']='n31r8'
C['register']='A quiet, real editorial landscape photograph of a lone billboard far out in open country'
C['world']='Vast open steppe: flat dry scrubland of tawny grass and low grey-green bushes, a few thin wooden fence posts, low brown mountains along the horizon; no buildings, no town.'
C['light']='Warm low late-afternoon sun from one side, raking across the grass and lighting the board face fully; long soft shadows; a soft blue sky with a few scattered white cumulus clouds along the horizon.'
C['palette']='Natural, slightly muted film colour: tawny ochre grass, olive scrub, dusty brown hills, soft blue sky, white clouds; the design surface clean neutral white in the warm light. The same grade on every image of this set.'
C['finish']='Shot on medium-format film like a calm documentary landscape series: fine natural grain, soft contrast, gentle colour, honest exposure; real and unstaged, never a render, never HDR.'
C['avoid']=['a face, chin, lips or profile','logos, letters or brand names anywhere','any image or text on the billboard','buildings, towns or roads unless the shot names them','an HDR or over-saturated look','a clean smooth 3D render look']
C['real']=C['real'].replace('it is large in the frame and the camera is close enough that it dominates, never a tiny board in a wide view','it is clearly the subject of the photograph, standing on the centre line at a medium size in a wide, calm landscape').replace('in a real city','in open country')
sh,PRINT=r3.sh,r3.PRINT
BB='THE BILLBOARD FACE IS PLAIN MATTE WHITE, flat and taut edge to edge with crisp corners on its simple frame, lit by the low sun, nothing printed on it and nothing crossing it.'
F=dict(aspect='4:3',format_words='landscape 4:3')
def S4(n,slug,moment,shot):
    d=sh(n,slug,moment,shot,BB,'the billboard');d.update(F);d['comp']=None;return d
S=[
 S4(1,'lone-billboard-on-scaffold-steppe-empty-frame-beside','A lone billboard stands on bare steel scaffolding far out in the steppe; beside it stands an empty scaffold frame with no board.','Camera at standing height, 50mm lens, f/8, almost square to the board. The billboard sits a little right of centre, filling about 35 percent of the frame width, sharp, raised on its thin legs and diagonal braces; the empty scaffold frame stands at the left edge; tawny grass and scrub in soft focus in the foreground; low mountains and a line of clouds on the horizon; generous blue sky above.'),
 S4(2,'billboard-beside-straight-empty-steppe-road','A lone billboard stands on simple scaffolding beside a straight empty two-lane road running across the steppe.','Camera at the roadside at standing height, 50mm lens, f/8, almost square to the board. The billboard fills about 35 percent of the frame width, sharp, set back from the road; the grey road edge and a few fence posts cross the foreground; flat scrubland to the low mountains; clouds along the horizon.'),
 S4(3,'billboard-across-dry-gravel-riverbed','A lone billboard on bare scaffolding stands on the far side of a wide dry gravel riverbed in open country.','Camera on the near bank at standing height, 50mm lens, f/8, almost square to the board. The pale stones of the dry riverbed fill the lower third; the billboard fills about 35 percent of the frame width, sharp, on the far bank among scrub; low brown hills and soft clouds behind.'),
 S4(4,'billboard-behind-wire-fence-tall-grass','A lone billboard on scaffolding stands behind a sagging wire fence in tall golden grass.','Camera low in the grass at the fence, 50mm lens, f/8, almost square to the board. A few weathered fence posts and thin wires cross the very bottom of the frame, soft, never over the board; the billboard fills about 35 percent of the frame width, sharp, beyond; the long grass catches the low sun; mountains and clouds on the horizon.'),
 S4(5,'billboard-before-far-snowy-range','A lone billboard on bare scaffolding stands in the open steppe with a far range of snow-topped mountains behind.','Camera at standing height with a longer lens, 85mm, f/8, almost square to the board. The billboard fills about 35 percent of the frame width, sharp, raised on its frame; the distant snowy peaks rise softly behind it; tawny scrub around; clean blue sky with a few clouds.'),
]
