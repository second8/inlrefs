# n27 round 4. Sam's finals already cover the sleeve, streamer and projection shots from round 3, so round 4 is new subjects in the same
# close, dark, no-halation style.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n27r3_listening.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n27r4';C['name']='Listening Room (round 4)'
I3=_m.I3;LOOK=_m.LOOK
S=[
 {'n':1,'slug':'member-card-on-counter','kind':'card','noun':'the member card','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'A member card left on the worn walnut counter in a pinspot, next to the bar tab.',
  'shot':'Close, 50mm, f/1.4, from a seat at the counter, looking down at about 35 degrees. The card lies flat on the walnut counter, filling about 45 percent of the frame width, sharp; a folded paper bar tab lies soft beside it. Everything beyond the pinspot falls to black.',
  'surface':'THE CARD FACE IS PLAIN BLANK WHITE, matte, crisp rounded corners, lying perfectly flat, nothing printed on it.'},
 {'n':2,'slug':'menu-card-in-holder','kind':'card','noun':'the drink menu card','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'The single drink menu card stands in a small walnut holder on the counter, lit by its own pinspot.',
  'shot':'Close and low, 50mm, f/1.4, at counter height. The tall card stands upright in a slim walnut block holder, filling about 70 percent of the frame height, sharp. The counter top runs off soft in front; behind, black with one pendant as a small warm blur.',
  'surface':'THE CARD IS PLAIN BLANK WHITE thick matte card, standing straight and flat, crisp corners, nothing printed on it.'},
 {'n':3,'slug':'phone-on-wool-armrest','kind':'phone','refs':['phone'],'people':'none','looks':[(I3,LOOK)],
  'moment':'A phone left face up on the wide moss-green wool armrest of an empty listening chair.',
  'shot':'Close, 50mm, f/1.4, from standing beside the chair, looking down at about 50 degrees. The phone lies on the armrest in a pinspot, filling about 50 percent of the frame height, sharp; the wool shows soft nap. The seat and the floor drop into black.'},
 {'n':4,'slug':'amp-display-window-close','kind':'screen','noun':'the amplifier display','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'The integrated amplifier glows on the low aluminium rack while a side plays.',
  'shot':'Close and low, camera level with the amp, 50mm, f/1.4. The brushed-aluminium amplifier front fills the frame width; its wide display window sits beside a large plain unmarked volume knob and fills about 55 percent of the frame width, sharp. Fine dust on the aluminium; above and behind is black.',
  'surface':'THE DISPLAY WINDOW SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, the brightest thing in the frame but not blown out, crisp corners; nothing crosses it.'},
 {'n':5,'slug':'framed-poster-felt-wall','kind':'print','noun':'the framed poster','refs':[],'people':'none','looks':[(I3,LOOK)],
  'moment':'A single framed poster hangs on the moss-green felt wall in a pinspot between the slats.',
  'shot':'Frontal and slightly off-axis, 50mm, f/1.4, close. The portrait poster in a thin walnut frame fills about 70 percent of the frame height, sharp, in a tight pool of warm light; the felt around it falls into darkness and the walnut slats are barely visible at the edges.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE matte paper lying perfectly flat behind non-reflective glass in the thin walnut frame, crisp edges, nothing printed on it.'},
]
