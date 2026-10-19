# n16 round 6. Sam on r5: scanner "works amazing, +1 creativity", tablet, poster, intercom work; tag unclear ("where is mockup"). Retire gowning poster.
# New: ID badge on the coverall, reticle pod label in gloved hands, gowning timer in the airlock. Props pr07, 42.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n16r5_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n16r6';C['name']='Yellow Room (round 6)'
C['avoid']=_m.C['avoid']+['a poster']
S=[
 {'n':1,'slug':'id-badge-coverall-chest','kind':'card','noun':'the ID badge','refs':['pr07'],'comp':'D',
  'people_line':'Only a section of the white clean-room coverall chest fills the frame, its fabric reading honey-amber in the safelight; no head, face, neck or hands are visible.',
  'moment':'A blank ID badge clipped to the chest of a white clean-room coverall in the amber bay.',
  'shot':'Straight on, very close, 90mm, f/4, camera square to the badge. The badge hangs flat on the centre line from its metal clip, its face square to the camera, filling about 55 percent of the frame height, sharp; the coverall fabric shows fine woven texture and a soft zip line to one side. Crisp amber highlight on the clip, deep umber at the corners.',
  'surface':'THE BADGE FACE IS PLAIN BLANK WHITE matte card behind a clear sleeve, flat, crisp rounded corners, nothing printed on it.'},
 {'n':2,'slug':'reticle-pod-label-gloved-hands','kind':'card','noun':'the pod label','refs':['reticle_pod'],'comp':'D',
  'people_line':'Only two violet-black nitrile gloved hands, in white coverall cuffs, hold the pod at its sides in a careful, natural working grip; nothing else of the person is in frame.',
  'moment':'Two gloved hands carry our reticle pod to the tool, lid up, its white label toward the camera.',
  'shot':'From slightly above, close, 50mm, f/2.8, camera square to the pod lid. The pod lid fills about 65 percent of the frame width, its edges parallel to the photo edges; the white label sits on the centre line above the dark photomask seen through the translucent lid, sharp. Amber light, strong contrast, the bay soft and dark behind.',
  'surface':'THE LABEL IS PLAIN BLANK WHITE matte, flat on the lid, crisp corners, nothing printed on it; it alone reads neutral white.'},
 {'n':3,'slug':'gowning-timer-airlock-wall','kind':'screen','noun':'the gowning timer display','refs':[],'people':'none','comp':'A',
  'moment':'In the cool grey gowning airlock, a flush landscape display set into the white wall above the gowning bench.',
  'shot':'Straight on, camera exactly at the centre of the display, 50mm, f/2.8, close. The display sits on the centre line flush in the white panel wall, facing the camera dead square, filling about 65 percent of the frame width, sharp; the top edge of the white gowning bench runs straight across the bottom. Cool pale grey light, crisp; a thin amber glow from the bay door at one edge.'},
]
