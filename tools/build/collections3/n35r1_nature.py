# n35 Nature round 1 (Sam 25 Nov). Moodboard Figma 293:132 (WORDS ONLY): print and devices set out in real nature; the nature and colour vary
# (pink lichen, dark jungle at dusk, mossy boulder, white rocks under blue sky, blank sign in a yellow rapeseed field). Calm editorial, real.
# Shots take the feel only, never the moodboard's compositions.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
from builder3 import SQ
from _nov_common import sh,PRINT,SCREEN
C={
 'id':'n35r1','name':'Nature','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A calm, real editorial photograph of a design piece set out in nature',
 'world':'Real, unspoiled nature exactly as each shot names it; clean and quiet; nothing man-made except the objects named in the shot.',
 'light':'Natural light exactly as the shot says, soft and real with true shadows; never studio light.',
 'palette':'True natural colour, rich but never over-saturated: each place keeps its own real colours; soft film highlights; the design surface pure neutral white. The same grade and finish on every image of the collection.',
 'real':("Real: this is a product mockup photograph, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates, never a small object in a wide landscape. "
         "The objects stand in nature as a deliberate editorial set, placed the way a photographer would place them, stable and believable, never floating. "+SQ+
         " Only the objects named in the shot are in frame. The design surface is new and clean, bright without blowing out; its edges and corners stay crisp."),
 'finish':'Shot on medium-format film like a calm nature editorial for a design studio: fine natural grain, soft contrast, honest exposure, gentle lens falloff; real and unstaged, never a render, never HDR.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any print or text on the design surface','any object not named in the shot','fog, haze or glow','an over-saturated, HDR or fantasy look','a clean smooth 3D render look'],
}
S=[
 sh(1,'sign-panel-on-posts-edge-of-lavender-field','A plain white sign panel stands on two weathered wooden posts at the edge of a lavender field in full bloom.',
  'Camera between the rows at the height of the panel, 85mm lens, f/5.6, square to it. The panel fills about 45 percent of the frame width on the centre line, sharp; the purple lavender rows run toward it in the soft foreground; a line of low green hills and a pale blue sky behind. Warm low late-afternoon sun from one side gives the posts long soft shadows.',
  PRINT('THE SIGN PANEL'),'the sign panel'),
 sh(2,'ipad-upright-on-mossy-stone-fern-forest','Our iPad stands upright in a slim black stand on a flat, moss-edged stone in a quiet fern forest.',
  'Camera at screen height, 85mm lens, f/2.8, square to the screen. The screen fills about 45 percent of the frame width on the centre line, sharp; soft fern fronds frame the edges out of focus; a gentle shaft of daylight through the canopy falls on the stone beside it, never across the screen; deep green background bokeh.',
  SCREEN('THE IPAD'),'the screen',comp=None,refs=['ipad']),
 sh(3,'poster-flat-on-red-autumn-leaves-top-down','A large poster lies flat on a thick carpet of fallen red, orange and amber autumn leaves on a forest floor.',
  'Camera straight down, 50mm lens, f/5.6. The poster lies on the centre line with its edges parallel to the frame, filling about 60 percent of the frame width, sharp; a few leaves touch only its outer edge, none lie on it; soft overcast light makes the leaf colours rich and even.',
  PRINT('THE POSTER'),'the poster',comp='B'),
 sh(4,'display-on-oak-desk-in-dark-tropical-forest-dusk','Our display stands on a simple honey-oak desk set out among huge dark tropical leaves in a forest at dusk; its screen is the brightest light in the scene.',
  'Camera at screen height, 50mm lens, f/4, square to the screen. The screen fills about 45 percent of the frame width on the centre line, sharp; the front edge of the desk runs across the lower part of the frame; giant monstera and palm leaves fill the dark surroundings, lit softly by the screen and the last blue dusk light.',
  SCREEN('THE DISPLAY'),'the screen',aspect='16:9',refs=['display']),
 sh(5,'poster-board-on-oak-easel-white-sand-dunes','A large poster board rests on our slim oak easel standing on the crest of white sand dunes under a deep blue sky.',
  'Camera at board height, 70mm lens, f/8, square to it. The board fills about 45 percent of the frame width on the centre line, sharp; clean wind ripples in the sand fill the foreground with crisp small shadows; hard clear sun; empty deep blue sky behind.',
  PRINT('THE POSTER BOARD'),'the poster board',aspect='16:9',refs=['easel_oak']),
]
