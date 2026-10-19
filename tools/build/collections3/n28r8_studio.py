# n28 Atelier round 8 (Sam 19 Oct): r7 all bad, 'makes 0 sense' (people stuck between glass, garment in a vitrine).
# 'r4 still the closest and best: camera, position, framing and people. What I don't like is the art direction. Glass usage there was better.'
# 'The og inspo with the black bg studio look is the art direction I want.' New inspo: bag carried in profile crop on black (B&W),
# hang tags on garments on a rail in hard light, shirt on a hanger with tag on plain grey, card in folded tissue.
# So: r4 base (camera, Tri-X), black studio, black and white, believable moments only. Glass only as r4-03 did it.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r4',os.path.join(os.path.dirname(__file__),'n28r4_art.py'));r4=importlib.util.module_from_spec(_s);_s.loader.exec_module(r4)
C=dict(r4.C);C['id']='n28r8'
C['register']='A black and white luxury fashion campaign photograph made in a black photo studio'
C['world']='A black photo studio: a matte black backdrop and a dark floor, nothing else unless the shot names it.'
C['light']='One real light source exactly as the shot describes; deep true blacks around it, no fill, nothing evenly lit.'
C['palette']='Black and white photograph: deep true blacks, soft graded greys, clean paper whites; no colour at all. The design surface is the cleanest white in the frame.'
C['finish']='Shot on 35mm Kodak Tri-X at box speed, developed in D-76 and printed on fibre paper: fine but clearly visible film grain, rich blacks, smooth tonal roll-off in the highlights, tiny real imperfections of film. Calm, quiet and physical, like a printed campaign; never smooth, never glossy, never a digital render.'
C['avoid']=['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','marble','any colour','any object not named in the shot','glass panels or vitrines unless named','a clean, smooth digital look']
sh,BL,BAG=r4.sh,r4.BL,r4.BAG
CARD='THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'
TAG='THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'
def still(n,slug,refs,moment,shot,surface,comp=None):
    d={'n':n,'slug':slug,'kind':'print','noun':'the design surface','refs':refs,'moment':moment,'shot':shot,'people':'none','surface':surface}
    if comp: d['comp']=comp
    return d
S=[
 sh(1,'bag-carried-side-crop-on-black',['bag_atelier'],
  'She walks slowly across the black studio in the ivory satin slip and cardigan, our bag hanging from her hand at her side.',
  'Camera at hip height, 50mm lens, f/2.8, side on to her. The frame is cropped from just below her shoulder to her knee; the bag hangs on the right half of the frame by its ribbon handles from her relaxed hand, the bag front square to the camera, filling about 45 percent of the frame width, sharp. One large soft light from the left, like a tall window, wraps the satin and the bag and falls off into pure black on the right.',
  'slip','Only her body from just below the shoulder to the knee and her hand are in frame, side on, in exactly the outfit from the reference.',BAG),
 still(2,'hang-tag-on-coat-on-rail-hard-slash',['hangtag','look_coat'],
  'The long black cocoon coat hangs alone on a slim black steel rail in the black studio; our hang tag hangs from its cuff on the espresso cord.',
  'Camera close and straight on, 50mm lens, f/4. The coat fills the frame as heavy dark folds of wool; one hard slash of light from a single spot, like late sun through a door gap, cuts diagonally across the wool and lands fully on the tag, which hangs on the centre line, square to the camera, filling about 40 percent of the frame height, sharp and evenly lit; outside the slash everything falls to black.',
  TAG),
 still(3,'shirt-dress-on-hanger-tag-at-collar',['hangtag','look_shirt'],
  'The white poplin shirt dress hangs on a plain black hanger from a thin steel rail against a dark grey studio wall; our hang tag hangs at the collar.',
  'Camera straight on at collar height, 85mm lens, f/5.6. The rail runs straight across the top of the frame; the shirt dress hangs on the centre line from the stand collar down past the deep cuffs, its poplin crisp and slightly creased; the tag hangs flat at the collar, square to the camera, filling about 30 percent of the frame width, sharp. One soft light from the upper left, a soft shadow of the dress on the wall behind.',
  TAG,'A'),
 still(4,'invitation-tucked-in-tissue-top-down',['tissue'],
  'A show invitation card lies tucked into folded warm ivory tissue on a dark table, just unwrapped.',
  'Camera straight down, 50mm lens, f/4. The card lies flat, its edges parallel to the frame, filling about 55 percent of the frame width, sharp; soft crumpled folds of tissue rise around three of its sides; the round sticker seal sits broken at one edge of the tissue. One soft window light from the upper left, soft shadows in the folds, the corners of the frame falling to black.',
  CARD,'B'),
 sh(5,'invitation-past-fluted-glass-studio',[],
  'She holds a show invitation card up in front of the black gown in the black studio; the photographer shoots past the edge of a sheet of fluted glass held close to the lens.',
  'The left third of the frame is seen through fluted glass right in front of the lens, breaking her gloved arm and the gown into repeated vertical ghost slices; the card sits in the clear part of the frame, square to the camera on the centre line, filling about 45 percent of the frame width, dead sharp, never behind the glass. One hard side light from the right. 50mm lens, close, camera at card height.',
  'gown','Only her gloved hand, arm and the gown from the shoulder to the waist are in frame, in exactly the outfit from the reference.',CARD),
]
