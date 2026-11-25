# n36 Terminal round 1 (Sam 25 Nov, working name). Moodboard Figma 293:133 (WORDS ONLY), but Sam prefers enclosed, polished public spaces:
# airport gate lounges with glass walls onto the apron, museum lobbies with polished concrete reflecting a white wall graphic, a framed screen in a station.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
from builder3 import SQ
from _nov_common import sh,PRINT,SCREEN
C={
 'id':'n36r1','name':'Terminal','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A polished, real architectural photograph of advertising inside a modern public building',
 'world':'The calm, spotless interior of a modern public building as each shot names it: polished terrazzo or stone floors, tall glass walls, brushed steel and pale stone; nothing else unless the shot names it.',
 'light':'Clean soft daylight through large glass walls mixed with even architectural ceiling light; the polished floor carries soft true reflections that fade out gently; the design surface is the brightest surface.',
 'palette':'Clean neutral architecture: warm pale stone, soft greys, brushed steel, true whites, a little soft sky blue through the glass; the design surface pure neutral white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup photograph in a real public building, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates, never a small sign in a wide hall. "
         "It is an unstaged photograph of a real place in use, polished and spotless. "+SQ+
         " Only the objects named in the shot are in frame. The design surface is bright and clean without blowing out; its edges and corners stay crisp. Floor reflections blend away softly, never ending in a hard line."),
 'finish':'Shot like premium architectural photography on a medium-format camera with a shift lens: straight verticals, crisp detail, natural colour, a gentle film softness in the highlights; real, never a render.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any image or text on the design surface','any object not named in the shot','tiny far-away people','haze, bloom or glow','a clean smooth 3D render look'],
}
SIT='Two or three travellers sit or walk in the middle ground, seen from behind, at normal size, one softly motion-blurred; no face shows.'
S=[
 sh(1,'landscape-screen-on-stone-pillar-gate-lounge','A large landscape screen is mounted on a slim pale-stone pillar in a quiet airport gate lounge, a full-height glass wall onto the apron behind.',
  'Camera at screen height, 50mm lens, f/5.6, square to the screen. The screen fills about 45 percent of the frame width on the centre line, sharp; through the glass behind, the tails of parked aircraft sit softly out of focus; rows of low seats in the middle ground; the glossy floor holds a soft reflection of the screen.',
  SCREEN('THE SCREEN'),'the screen',people=SIT,aspect='16:9'),
 sh(2,'white-wall-panel-museum-lobby-polished-concrete','A huge freestanding white wall panel stands in the bright lobby of a contemporary museum; the polished concrete floor mirrors it softly.',
  'Camera low, 35mm lens, f/8, square to the panel. The panel fills about 60 percent of the frame width on the centre line, sharp; slanted white steel columns frame it on both sides; its reflection lies on the polished floor below and fades out gently; daylight from a glass roof.',
  PRINT('THE WALL PANEL'),'the wall panel',people='One or two visitors pass at the edge of the frame, at normal size and softly motion-blurred, never in front of the panel; no face shows.'),
 sh(3,'backlit-lightbox-dark-stone-wall-metro-concourse','A large backlit lightbox is set flush into a wall of polished dark grey stone in a new metro station concourse.',
  'Camera across the concourse at lightbox height, 50mm lens, f/5.6, square to the wall. The lightbox fills about 55 percent of the frame width on the centre line, sharp; the stone joints run parallel to its edges; a thin brushed-steel handrail runs along the bottom of the frame; the glossy granite floor reflects it softly.',
  'THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim steel frame, nothing printed on it and nothing crossing it.','the lightbox',aspect='16:9'),
 sh(4,'long-lightbox-beside-moving-walkway-airport-corridor','A long backlit lightbox runs along the wall of a bright airport connector corridor beside a moving walkway.',
  'Camera standing on the moving walkway at lightbox height, square to the wall, 35mm lens, f/8, slow shutter so the black walkway handrail in the foreground streaks softly while the lightbox stays dead sharp. The lightbox fills about 60 percent of the frame width; clean white ceiling light above; nobody in frame.',
  'THE LIGHTBOX IS PLAIN EVENLY LIT PAPER-WHITE behind clean glass, flat edge to edge with crisp corners inside its slim steel frame, nothing printed on it and nothing crossing it.','the lightbox',aspect='16:9'),
 sh(5,'portrait-totem-premium-lounge-runway-windows','A tall portrait digital totem stands in a quiet premium airport lounge beside floor-to-ceiling windows overlooking the runway.',
  'Camera at screen height, 85mm lens, f/4, square to the screen. The totem screen fills about 70 percent of the frame height on the centre line, sharp; soft leather lounge chairs and a stone side table sit out of focus behind; soft daylight and the runway beyond the glass.',
  SCREEN('THE TOTEM SCREEN'),'the totem screen'),
]
