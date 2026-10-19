# n29 Spatial Awareness round 7 (Sam 19 Oct): all five r6 finals. Same dark gallery, teal-green grid ceiling, moody imperfect grade; new installations. WORDS ONLY.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r6=_m('n29r6_teal')
C=dict(r6.C);C['id']='n29r7'
s,SIL,WHITE=r6.s,r6.SIL,r6.WHITE
S=[
 s(1,'row-of-three-portrait-lightboxes-dark-hall',[],
  'Three identical tall portrait lightboxes stand in a straight row on low black plinths down the middle of the dark gallery, as one series.',
  'Camera at chest height, 35mm lens, f/2.8, square to the row. The three lightboxes stand side by side with equal gaps, together filling about 70 percent of the frame width, the middle one on the centre line and sharp; their glow washes the low grid ceiling above in a cool teal-green and lies as soft smears on the black floor; one visitor stands before the left one as a dark silhouette.',
  WHITE,None,SIL,'print','the lightboxes'),
 s(2,'single-screen-hung-on-cables-eye-height',[],
  'One large landscape screen hangs on two thin steel cables from the low ceiling, floating at eye height in the middle of the dark room.',
  'Camera at eye height, 35mm lens, f/2.8, square to the screen. The screen fills about 55 percent of the frame width on the centre line, sharp, its two thin cables rising to the panel ceiling; a visitor stands a few steps before it as a dark silhouette from behind, small at the lower edge; its glow lights the grid ceiling teal-green; black all around.',
  WHITE,None,SIL,'screen','the screen'),
 s(3,'tall-monolith-screen-floor-reflection',[],
  'A single tall portrait screen stands alone like a monolith on the black floor of the dark gallery.',
  'Camera low at hip height, 35mm lens, f/2.8, square to it. The tall screen stands on the centre line, filling about 70 percent of the frame height, sharp; its long glow reflects softly in the dark floor below it; the low grid ceiling above catches a cool teal-green glow; nothing else in the room.',
  WHITE,None,None,'screen','the screen'),
 s(4,'projection-on-hanging-scrim-silhouettes',[],
  'A large white image is projected onto a thin fabric scrim hanging from the ceiling in the middle of the dark room; a few visitors stand on both sides of it.',
  'Camera at standing height, 35mm lens, f/2.8, square to the scrim. The projected rectangle on the scrim fills about 60 percent of the frame width, a crisp-edged field of white light, the fabric hanging straight; two visitors stand in front of it as dark silhouettes, small; the grid ceiling catches a faint teal-green glow.',
  'THE PROJECTED IMAGE IS PLAIN WHITE, a clean, crisp-edged rectangle of light on the scrim, evenly bright without blowing out; nothing is projected on it.','A',SIL,'print','the projection'),
 s(5,'screen-at-end-of-narrow-dark-corridor',[],
  'At the end of a long, narrow, black corridor a single portrait screen glows on the end wall.',
  'Camera at the start of the corridor at eye height, 35mm lens, f/2.8, straight down its centre line. The two black walls and the low grid ceiling run toward the screen, framing it; the screen sits on the centre line filling about 35 percent of the frame width, sharp; its light spills along the floor and walls toward the camera with a cool teal-green tint on the ceiling panels.',
  WHITE,'C',None,'screen','the screen'),
]
