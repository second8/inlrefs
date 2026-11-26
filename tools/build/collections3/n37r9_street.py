# n37 Night Square round 9 (Sam 26 Nov): 'Lets do 15 more, this time, not just big screens, a bit more city focused and smaller details.'
# R8: long-lens between towers 'LOVE IT!'; finals 01,03,04,05,09,10. Hero now often a street-level screen/poster; giant white screens behind.
import os,sys;sys.path.insert(0,os.path.dirname(__file__))
import importlib.util
_s=importlib.util.spec_from_file_location('r8',os.path.join(os.path.dirname(__file__),'n37r8_final.py'));r8=importlib.util.module_from_spec(_s);_s.loader.exec_module(r8)
from _nov_common import sh
C=dict(r8.C);C['id']='n37r9'
C['register']='A real night street photograph in a dense city entertainment district with giant digital billboards and street-level screens'
C['real']=r8.C['real'].replace('Every screen is big and generous, a full billboard, never a thin strip or a small sliver.','The city is detailed and lived-in: wet kerbs, street furniture, traffic lights, awnings and fire escapes in true scale; the hero surface named in the shot is clear, sharp and generous in the frame, and the giant screens behind are never thin strips.')
ALL='EVERY SCREEN, LIGHTBOX AND POSTER IN THE FRAME IS PLAIN WHITE: screens glow bright and clean, posters are matte paper-white, each a crisp rectangle with sharp corners; nothing printed on them and nothing crossing them.'
SN='light snow falls softly; a thin fresh layer of snow on the ground.'
DR='a subtle drizzle; the street glistens.'
def s(n,slug,m,shot,aspect='4:5',refs=None): return sh(n,slug,m,shot,ALL,'the screens',aspect=aspect,refs=refs)
S=[
 s(1,'pavement-kiosk-totem-giant-screens-behind','A slim two-sided digital kiosk totem stands on the wet pavement of the square, giant white screens on the towers behind.',
  f'Camera at totem height, 85mm lens, f/2.8, square to its face. The totem fills about 45 percent of the frame height on the centre line, sharp; the giant screens behind are soft out of focus; {DR}'),
 s(2,'parked-cab-roof-screen-close','A single yellow cab parked at the kerb with its slim roof-top ad screen glowing white, the square behind.',
  'Camera at roof height beside the cab, 85mm lens, f/2.8, square to the roof screen. The roof screen fills about 40 percent of the frame width, sharp; the yellow cab roof below it; the giant screens behind soft and glowing; wet street.',aspect='16:9'),
 s(3,'our-shelter-panel-wet-corner-street-level','Our graphite bus shelter on a wet street corner, its tall lightbox panel facing the camera, giant screens rising behind.',
  f'Camera at panel height, 50mm lens, f/4, square to the panel. The lightbox panel fills about 50 percent of the frame height, sharp; the shelter glass and frame around it; the giant screens soft behind; {DR}',refs=['shelter']),
 s(4,'hoarding-of-white-paste-up-posters','A dark construction hoarding along the pavement carries a neat row of plain white paste-up posters under a street lamp, the square glowing beyond.',
  'Camera across the pavement, 50mm lens, f/5.6, square to the hoarding. The row of posters fills about 60 percent of the frame width, sharp and flat; warm street light from above; the giant screens soft at the top of the frame.',aspect='16:9'),
 s(5,'subway-kiosk-lightbox-city-behind','A glass subway entrance kiosk with a lit lightbox panel on its side, the screen-covered towers behind.',
  'Camera at panel height, 70mm lens, f/4, square to the lightbox. The lightbox fills about 45 percent of the frame height, sharp; the green globe lamps of the entrance glow beside it; the towers soft behind.'),
 s(6,'newsstand-with-white-posters-closed','A closed metal newsstand on the pavement, its side covered with plain white posters in clean frames.',
  f'Camera at poster height, 50mm lens, f/4, square to the side of the stand. The posters fill about 50 percent of the frame width, sharp; the square glows soft behind; {SN}'),
 s(7,'long-lens-avenue-stacked-screens-traffic-lights','A deep avenue seen through a long lens: screens of different sizes stacked up the facades on both sides, traffic lights hanging over the street.',
  f'Camera far down the avenue, 200mm lens, f/5.6. The compressed facades and their white screens fill the frame, the nearest screen sharp on the centre line filling about 35 percent of the frame height; the hanging traffic lights glow red; {DR}'),
 s(8,'small-screen-above-deli-awning-fire-escapes','A small landscape screen sits above a lit deli awning between black fire escapes on a narrow side street.',
  'Camera across the side street, 135mm lens, f/4, square to the screen. The screen fills about 40 percent of the frame width, sharp; the awning below and the fire escapes above in clean silhouette; wet pavement.'),
 s(9,'portrait-screen-in-shop-window-street','A portrait digital screen stands inside the window of a closed shop on the square, the wet street reflected faintly in the glass beside it.',
  'Camera on the pavement at screen height, 50mm lens, f/4, square to the window. The screen fills about 50 percent of the frame height, sharp; the reflections stay at the window edges, never over the screen.'),
 s(10,'twin-lamppost-banners-city-behind','A lamppost on the square carries two plain white vertical banners on steel arms, the giant screens glowing behind.',
  f'Camera at banner height, 85mm lens, f/4, square to the banners. The two banners fill about 45 percent of the frame height, sharp; the lamp glows warm above them; {SN}'),
 s(11,'bus-side-panel-at-stop','A city bus waits at a stop on the square, the big white ad panel on its side facing the camera.',
  'Camera across the pavement at panel height, 50mm lens, f/5.6, square to the bus side. The side panel fills about 55 percent of the frame width, sharp; the bus windows above it dark; the giant screens soft behind.',aspect='16:9'),
 s(12,'sign-above-bodega-door-drizzle','A small corner bodega with one landscape lit sign panel above its door, its window glowing warm, the square behind.',
  f'Camera across the street, 85mm lens, f/4, square to the sign. The sign fills about 45 percent of the frame width, sharp; the warm window and door below; {DR}',aspect='16:9'),
 s(13,'street-kiosk-two-screen-faces-snow','A tall slim street kiosk on the pavement with a portrait screen face, snow settling on its top.',
  f'Camera at screen height, 85mm lens, f/2.8, square to the face. The kiosk fills about 50 percent of the frame height, sharp; the giant screens soft behind; {SN}'),
 s(14,'long-lens-screen-cluster-on-corner','A cluster of six flat screens of different sizes on one building corner, seen tight through a long lens from far down the street.',
  'Camera far away, 200mm lens, f/5.6, square to the main face. The screen cluster fills about 60 percent of the frame, sharp; dark windows and ledges around them; traffic light glows below.'),
 s(15,'tight-avenue-135mm-mid-screens-drizzle','A tighter view up the avenue at street level: mid-size screens on the lower floors of the facades recede in a row, red and white traffic trails below.',
  f'Camera at street level, 135mm lens, f/5.6, slow shutter. The nearest screen on the centre line fills about 35 percent of the frame width, sharp; the rest recede softly; {DR}',aspect='16:9'),
]
