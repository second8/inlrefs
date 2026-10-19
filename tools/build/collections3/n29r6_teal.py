# n29 Spatial Awareness round 6 (Sam 19 Oct): r5 'too warm'. New inspo (dark gallery, translucent screen box, grid ceiling lit teal-green, moody, imperfect):
# 'follow this look, image should not be perfect but rather moody', and 'get compositions from the figma board, recreate them'. WORDS ONLY, no image refs.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r2',os.path.join(os.path.dirname(__file__),'n29r2_museum.py'));r2=importlib.util.module_from_spec(_s);_s.loader.exec_module(r2)
C=dict(r2.C);C['id']='n29r6'
C['register']='A moody, imperfect documentation photograph of a video and light installation in a dark gallery'
C['world']='A dark contemporary gallery: black floor, black walls, and a low dropped ceiling of square panels with small recessed spots; the installation is the main light in the room.'
C['light']=('The installation glows and its light washes up onto the low panel ceiling, which picks up a soft cool teal-green glow and shows its square grid; the floor and walls stay near black. '
            'No other lamps; uneven, natural falloff.')
C['palette']=('Cool and dark: deep blacks, a soft muted teal-green cast in the ceiling and air, desaturated; the glowing design faces are clean white with a faint cool tint. '
              'The same grade on every image of the collection.')
C['finish']=('Not a perfect image: like a real press photo of a video installation shot in near darkness, slightly soft, low contrast in the shadows, noisy grain, a little compression and softness, '
             'imperfect but moody. Never crisp CGI, never polished.')
C['avoid']=['a face, chin, lips or profile','any image, photo, face, text or colour on any screen or lightbox','logos, letters or brand names anywhere','warm orange or peach light','any object not named in the shot','a clean, sharp, polished digital look']
s,SIL,WHITE=r2.s,r2.SIL,r2.WHITE
S=[
 s(1,'translucent-screen-box-corner-dark-gallery',[],
  'A room-sized box made of large translucent screen walls stands in the middle of the dark gallery, glowing; we see it at its corner.',
  'Camera at standing height from the dark floor, 35mm lens, f/2.8, looking at the near corner of the box so that two glowing walls show, the left wall almost square to the camera and filling about 45 percent of the frame width, the right wall turning gently away; the low grid ceiling above catches their teal-green glow; black floor below with a faint reflection.',
  WHITE,None,None,'screen','the translucent screen walls'),
 s(2,'huge-lightbox-end-of-dark-lobby',[],
  'A huge backlit lightbox fills most of the far wall of a dark low gallery lobby.',
  'Camera at chest height, straight on, 35mm lens, f/2.8. The lightbox fills about 60 percent of the frame width, square to the camera, a little left of centre; its glow lights the low panel ceiling above in a cool teal-green and lies as a soft smear on the dark floor; a dark doorway at the left edge.',
  'THE LIGHTBOX FACE IS PLAIN EVENLY LIT WHITE, glowing bright, clearly the brightest thing in the frame yet not blown out, with crisp corners; nothing on it.','A',None,'print','the lightbox'),
 s(3,'dark-hall-stacked-crates-lit-faces',[],
  'In a dark old industrial hall with tall arched windows high up, plain wooden crates of different sizes are stacked in loose clusters at different heights, one face of each lit as a lightbox; a few visitors stand among them.',
  'Camera at chest height, 35mm lens, f/2.8, looking into the clusters. The nearest crate stands close on the left, its lit face square to the camera, filling about 40 percent of the frame width, sharp; the other lit faces glow softer deeper in the dark at different heights; two visitors stand among them as dark silhouettes; the cool teal-green glow sits on the high ceiling.',
  WHITE,None,SIL,'print','the lightbox crate faces'),
 s(4,'wall-of-stacked-crts-sofa-foreground',['crt'],
  'In a dark room a whole wall is built from stacked grey CRT televisions of mixed sizes, every one showing the same plain white image; an old soft sofa sits in the foreground.',
  'Camera low from beside the sofa, 35mm lens, f/2.8, square to the wall of televisions. The stacked CRTs fill about 70 percent of the frame width from floor to ceiling, the largest one near the centre square to the camera and sharp; the arm of the dark sofa crosses the lower right corner, soft; the white glow of the screens lights the room cool and dim.',
  WHITE,None,None,'screen','the televisions'),
 s(5,'huge-projection-end-wall-tiny-silhouettes',[],
  'In a very dark, deep gallery a huge projected white image fills the end wall; a few visitors stand and sit on the floor in front of it, tiny against it.',
  'Camera from the back of the room at standing height, 35mm lens, f/2.8, square to the end wall. The projected rectangle fills about 65 percent of the frame width, a crisp-edged field of white light; small visitors stand and sit on the floor below it as dark cut-out silhouettes; the low grid ceiling catches a faint teal-green glow; the rest is black.',
  'THE PROJECTED IMAGE IS PLAIN WHITE, a clean, crisp-edged rectangle of light on the wall, evenly bright without blowing out; nothing is projected on it.','A',SIL,'print','the projection'),
]
