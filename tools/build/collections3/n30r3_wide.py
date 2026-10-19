# n30 Low Cloud round 3 (Sam 19 Oct): all five r2 picked as finals. 'Make the clouds/fog a bit more simple, not too many layers; I want some horizontal compositions.'
# Same grade as r2, words only (r2 used look images; that is now forbidden, so the look is written out). Shots 1-3 are 16:9.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n30r2_dusk.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
C=dict(r2.C);C['id']='n30r3'
C['world']='A real city at dusk under one simple, even layer of low grey cloud: the tops of tall buildings disappear into it; wet stone and asphalt; small warm windows and street lights far off. The cloud is one flat soft layer, never stacked banks of fog.'
C['palette']=r2.C['palette']+' Like an overcast civic square at dusk on a smoggy day: flat grey-brown sky, muted stone, silhouetted people, the screen glowing clean.'
C['avoid']=r2.C['avoid'][:4]+['layered or swirling fog banks','a clean smooth digital look']
SCR=r2.SCR;BACK=r2.BACK
BB='THE BILLBOARD FACE IS PLAIN PAPER-WHITE, evenly lit by its lamps edge to edge, flat and taut with crisp corners inside its thin dark frame, nothing printed on it and nothing crossing it.'
W={'aspect':'16:9','format_words':'landscape 16:9'}
def sh(n,slug,moment,shot,surface,kind='led',noun='the screen',people=None,wide=False):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':[],'moment':moment,'shot':shot+BACK,'surface':surface,'comp':'A'}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    if wide: d.update(W)
    return d
TINY=r2.TINY
S=[
 sh(1,'long-led-screen-river-embankment-wide','A long horizontal LED screen is set into a stone river embankment wall at dusk; the river in front reflects it.',
  'Camera from the opposite bank at the height of the screen, 85mm lens, f/2.8, square to it. The long screen fills about 75 percent of the frame width on the centre line, sharp; the dark stone embankment wall above and below it; its light lies in a long soft stripe on the slow river in the foreground; behind, buildings rise into one flat layer of grey cloud.',
  'THE LONG SCREEN '+SCR,people=TINY,wide=True),
 sh(2,'rooftop-billboard-across-boulevard-wide','A wide lit billboard stands on the roof of a long building across a broad boulevard at dusk; tram wires cross the street below.',
  'Camera from a window across the boulevard at roof height, 85mm lens, f/2.8, square to the billboard. It fills about 60 percent of the frame width on the centre line, sharp; the thin tram wires run straight across the lower part of the frame, never over the billboard; the wet boulevard glints far below; one flat layer of grey cloud above.',
  BB,'print','the billboard',wide=True),
 sh(3,'arena-led-screen-empty-plaza-wide','A large landscape LED screen is mounted on the curved concrete outside wall of an arena above an empty plaza at dusk.',
  'Camera at standing height across the plaza, 50mm lens, f/2.8, square to the screen. The screen fills about 65 percent of the frame width on the centre line, sharp; the grey concrete of the arena around it; the wet plaza below reflects it; a few small figures cross the plaza; the arena roof edge meets one flat layer of low cloud.',
  'THE ARENA SCREEN '+SCR,people=TINY,wide=True),
 sh(4,'tall-banner-screen-facade-side-street','A tall narrow banner screen runs up the facade of a building at the end of a narrow side street at dusk.',
  'Camera down the side street at the middle height of the screen, 85mm lens, f/2.8, square to it. The banner screen fills about 70 percent of the frame height on the centre line, sharp; the dark walls of the side street frame it on both sides; the wet street below; the top of the building fades into one flat layer of low cloud.',
  'THE BANNER SCREEN '+SCR),
 sh(5,'two-pole-billboard-bridge-end-wet-road','A large lit billboard on two steel poles stands at the end of a bridge at dusk, above a wet road.',
  'Camera on the bridge at billboard height, 85mm lens, f/2.8, square to its face. The billboard fills about 75 percent of the frame width on the centre line, sharp; its two poles drop out of the frame; the wet road curves away below with small red tail lights; one flat layer of low grey cloud behind.',
  BB,'print','the billboard'),
]
