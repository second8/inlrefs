# n37 Night Square round 1 (Sam 25 Nov, working name). Moodboard Figma 293:134 (WORDS ONLY): Times Square inspired; giant curved and flat LED screens
# glowing pink, blue, orange and purple at night, stacked facades, wet streets. Hero screen plain white; the others show soft colour only, never text.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
from builder3 import SQ
from _nov_common import sh,PRINT,SCREEN
C={
 'id':'n37r1','name':'Night Square','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A real night photograph of giant digital billboards in a dense city entertainment square',
 'world':'A dense city entertainment square at night: tall towers stacked with giant LED screens, wet asphalt and pavements; every screen except the hero shows only soft solid colour gradients in magenta, electric blue, violet and amber, with no text, logos or pictures.',
 'light':'Night lit by the giant screens: saturated coloured spill across the wet streets and facades; the hero screen is the brightest thing in the frame; clean air, no smoke.',
 'palette':'Deep near-black night with vivid magenta, electric blue, violet and amber spill from the surrounding screens; the hero design surface pure neutral white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup photograph of a giant digital billboard, so the design surface is the hero: it is large in the frame and the camera is close enough that it dominates. "
         "It is a real place on a real wet night, shot from a real vantage point. "+SQ+
         " Only the objects named in the shot are in frame. The hero screen is crisp at its edges and corners, with no bloom around it."),
 'finish':'Shot on a full-frame camera at night like real street photography: fine natural grain, true deep blacks, crisp highlights without bloom; real, never a render, never cyberpunk.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any image or text on the design surface','tiny people in the street','halation, bloom or glow around the screen','smoke or haze','a sci-fi or 3D render look'],
}
HERO=SCREEN('THE HERO SCREEN')
S=[
 sh(1,'giant-led-billboard-on-tower-long-lens','A giant flat LED billboard covers the upper floors of a tower on the square, surrounded by smaller glowing screens.',
  'Camera on a raised spot across the square at the billboard height, 135mm lens, f/5.6, square to it. The billboard fills about 55 percent of the frame width on the centre line, sharp; neighbouring screens glow magenta and electric blue at the frame edges; the dark tops of the towers above.',
  HERO,'the hero screen'),
 sh(2,'curved-led-screen-wrapping-stone-building-corner','A tall curved LED screen wraps around the rounded corner of an old stone building above the square.',
  'Camera across the street at screen height, 85mm lens, f/5.6. The front of the screen faces the camera square-on and the curve wraps away at one side; the screen fills about 50 percent of the frame width, sharp; a streetlight arm and a traffic light cross the lower foreground, never over it; the wet street below catches its light.',
  'THE CURVED HERO SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE edge to edge around its curve, glowing bright and clean, clearly the brightest thing in the frame, not blown out, crisp at its edges; nothing crosses it.','the curved screen'),
 sh(3,'three-led-ribbon-bands-across-facade','Three long horizontal LED ribbon screens run one above another across the facade of a modern building on the square.',
  'Camera across the street at the height of the middle band, 50mm lens, f/5.6, square to the facade. The three bands fill about 80 percent of the frame width, sharp, separated by dark glass floors; a violet screen glows on the corner below.',
  'ALL THREE RIBBON SCREENS SHOW A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, evenly lit edge to edge yet not blown out, with crisp ends; nothing crosses them.','the ribbon screens',aspect='16:9'),
 sh(4,'big-screen-above-theatre-marquee-cab-streak','A huge landscape LED screen sits above a theatre\'s bright bulb-lit marquee canopy on the square; a yellow cab streaks past in the foreground.',
  'Camera from across the square at the kerb, 50mm lens, f/4, slow shutter, aimed so the screen stays square. The screen fills about 55 percent of the frame width, sharp; the marquee bulbs glow below it with no letters; the cab is a long yellow blur low in the frame; the wet asphalt mirrors the colours.',
  HERO,'the hero screen',aspect='16:9'),
 sh(5,'slim-vertical-led-tower-end-of-square','A slim vertical LED tower stands at the far end of the square, framed by walls of glowing coloured screens on both sides of the street.',
  'Camera on a raised point in the middle of the street, 135mm lens, f/5.6, square to the tower. The tower screen fills about 65 percent of the frame height on the centre line, sharp; magenta screens on the left and electric blue screens on the right converge toward it; red and white traffic light trails run along the bottom; no people.',
  'THE TOWER SCREEN SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly the brightest thing in the frame, evenly lit edge to edge yet not blown out, with crisp corners; nothing crosses it.','the tower screen'),
]
