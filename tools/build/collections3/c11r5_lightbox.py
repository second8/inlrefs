# C11 round 6 (Sam 21:1x: "more intentional design with more character; screens most important; the lightbox behind should be like a
# screen too, whatever is on the device screen is shown there too; not everything forward: angles, perspective, depth of field; 10 new").
# Wall = one huge plain white screen divided by the fine black grid (like a video wall's thin bezels). Natural actions only (r5: two
# people holding one phone, sitting on a table made no sense). Moderate angles 20-40 degrees, shallow depth of field, screens readable.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'c11r2_lightbox.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='c11r5';C['name']='Lightbox (round 6)'
C['world']='A dark room in front of a floor-to-ceiling wall that works as one huge screen: large panels of plain, evenly lit clean white divided by a fine regular matte black grid, like the thin bezels of a video wall. In front of it only what the shot names. Everything in front of the wall is dark.'
C['world_short']='A dark room in front of a floor-to-ceiling wall that works as one huge plain white screen, divided by a fine regular black grid like thin video-wall bezels.'
C['light']='The wall is the only light: clean warm white, evenly bright across every panel with no hot spots, so everything in front of it reads as a crisp dark silhouette with a faint thin rim. The device screen is as bright and clean as the wall.'
C['real_angle']=('The design surface is turned to the camera at a moderate angle of about 20 to 40 degrees as the shot says, so the photograph has real perspective and depth, but the whole screen stays fully visible, readable and evenly lit, with crisp corners and no lens distortion; the wall behind falls softly out of focus with shallow depth of field.')
C['avoid']=['a face, profile, cheek, ear or chin','a person facing the camera','glow or halation','hot spots in the wall','two grid lines close together or a broken grid','any object not named in the shot','two people holding one device']
WALLSURF=' THE WALL BEHIND IS PLAIN EVENLY LIT WHITE IN EVERY PANEL, nothing shown on it.'
GW=['glasswall'];HER=['ch06'];HIM=['ch11']
def sh(n,slug,kind,refs,pl,moment,shot,**kw):
    d={'n':n,'slug':slug,'kind':kind,'refs':refs+GW,'people':'line','people_line':pl,'moment':moment,'shot':shot};d.update(kw);return d
BACK='seen from behind, head turned away from the camera; no face, cheek, ear or profile is visible.'
S=[
 sh(1,'tablet-held-up-three-quarter-back','ipad',['ipad']+HER,'Her head, long straight hair and shoulders are a dark silhouette at the left, '+BACK,
  'She holds a tablet up in front of the huge white wall to check the design before it goes up on the wall.',
  'From behind her left shoulder, 85mm, f/2, the tablet turned about 30 degrees to the camera, filling about 45 percent of the frame width, screen sharp; the wall and grid behind fall softly out of focus.'),
 sh(2,'laptop-foreground-figure-at-wall','laptop',['laptop']+HIM,'Far behind, one man stands at the wall as a soft dark silhouette, '+BACK,
  'A laptop open on the dark desk in the foreground; behind it, a colleague stands at the glowing wall.',
  'Low, at desk height, 50mm, f/1.8. The laptop sits in the foreground right, its screen turned about 30 degrees toward the camera, filling about 45 percent of the frame width, sharp; the desk recedes in perspective; the figure and the grid behind melt into soft focus.'),
 sh(3,'phone-in-hand-wall-bokeh','phone',['phone'],'Only her hand and wrist hold the phone, a dark silhouette entering from the bottom right.',
  'A phone held up in front of the huge white wall, the grid behind blurred into soft lines.',
  'Close, 85mm, f/1.8, the phone turned about 25 degrees to the camera, filling about 50 percent of the frame height, screen sharp; the wall and black grid behind fall into soft bokeh.'),
 sh(4,'display-side-angle-seated-figure','display',['display']+HIM,'He sits at the desk beside the display, a dark silhouette of back and shoulders at the right edge, '+BACK,
  'A desktop display on the long dark desk, seen from the side; he sits beside it looking up at the wall.',
  'From the side at desk height, 50mm, f/2, the display turned about 35 degrees to the camera, filling about 45 percent of the frame width, sharp; the desk edge runs away in perspective; the wall behind soft.'),
 sh(5,'watch-wrist-angled-macro','watch',['watch'],'Only a forearm and hand enter from the left as a dark silhouette.',
  'A wrist raised to check the watch in front of the huge white wall.',
  'Macro, 100mm, f/2.8, the watch face turned about 25 degrees to the camera, filling about 40 percent of the frame width, sharp; the wall behind is soft glowing white with the grid as faint blurred lines.'),
 sh(6,'presenter-beside-wall-phone-in-hand','phone',['phone']+HIM,'He stands at one side of the frame in front of the wall, a full dark silhouette, '+BACK+' One arm is raised toward the wall as if presenting; the other hand holds the phone at chest height.',
  'He presents from his phone to the huge white wall, which shows what is on the phone.',
  'Straight on to the wall, 35mm, f/4, the phone in his lower hand turned about 30 degrees to the camera, filling about 20 percent of the frame height, sharp; the whole wall fills the frame behind him as one huge clean white screen with its fine grid, sharp.'),
 sh(7,'two-at-low-table-laptop-between','laptop',['laptop']+HER+HIM,'Two people sit on low stools at a low dark table with their backs three-quarter to the camera, dark silhouettes, both looking at the laptop; '+BACK,
  'A small meeting in front of the glowing wall: a laptop open on a low table between two people.',
  'From behind and slightly above, 50mm, f/2, the laptop between them turned about 30 degrees to the camera, filling about 40 percent of the frame width, sharp; their shoulders soft in the foreground at both sides; the wall behind soft.'),
 sh(8,'tablet-stand-side-angle-hand','ipad',['ipad']+HER,'Only her hand reaches in from the right to touch the edge of the tablet, a dark silhouette.',
  'A tablet in a slim stand on the desk, seen from the side as she reaches to swipe.',
  'From the side at desk height, 85mm, f/2, the tablet turned about 35 degrees to the camera, filling about 50 percent of the frame width, sharp; the desk and stand in crisp perspective; the wall soft behind.'),
 sh(9,'portrait-totem-foreground-blur-passerby','screen',[]+HIM,'In the near foreground, a man walks past as a large soft dark blur crossing one edge of the frame, '+BACK,
  'A tall portrait display stands on the floor against the glowing wall; someone walks past close to the camera.',
  'Low angle from near the floor, 35mm, f/2, the portrait display turned about 25 degrees, filling about 55 percent of the frame height, sharp; the passer-by in the foreground is a soft dark shape at the edge, never covering the screen.',noun='the portrait display'),
 sh(10,'laptop-layered-depth-shoulder-foreground','laptop',['laptop']+HER,'In the foreground, the edge of her shoulder and hair is a large soft dark blur at the left, '+BACK,
  'Layers of depth: a soft dark shoulder close to the camera, a laptop sharp in the middle, the glowing wall soft behind.',
  'From behind, 85mm, f/1.8, the laptop in the middle distance turned about 30 degrees to the camera, filling about 45 percent of the frame width, sharp; foreground and background both soft.'),
]
for s in S:
    k=s['kind'];noun=s.get('noun') or {'ipad':'the tablet','laptop':'the laptop','phone':'the phone','display':'the display','watch':'the watch'}.get(k,'the screen')
    s['surface']=f"THE {noun.replace('the ','').upper()} SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, bright and clean, evenly lit edge to edge, crisp corners in its thin black border, nothing crossing it."+WALLSURF
