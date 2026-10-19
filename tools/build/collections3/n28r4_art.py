# n28 Atelier round 4 (Sam 18 Oct): 4 more; r3 'none felt artistic enough: effects, lens, lighting, camera, grain all bland'.
# Each shot built on ONE strong in-camera technique a campaign photographer would use. Neutral colour, heavy pushed film grain.
from builder3 import SQ
C={
 'id':'n28r4','name':'Atelier','aspect':'4:5','format_words':'portrait 4:5',
 'register':'An art-directed luxury fashion campaign photograph with a strong in-camera technique',
 'world':'A dark fashion set: black space, a polished dark floor, nothing else unless the shot names it.',
 'light':'Hard, sculpted, deliberate light as described in the shot; deep true blacks around it, no fill, nothing evenly lit.',
 'palette':'Neutral, almost monochrome colour: neutral white light, charcoal and true black, natural skin, the clothes in their own black, white and ivory; no blue, teal, orange or any colour cast. The design surface is the cleanest white in the frame.',
 'finish':'Shot on 35mm Tri-X pushed two stops: coarse, clearly visible film grain over the whole frame, crushed rich blacks, hard contrast, highlights that roll off softly, tiny real imperfections of film. Bold, artistic and physical, the opposite of a clean digital catalogue image; never smooth, never glossy.',
 'cast':{'her':'ch13'},
 'real':("Real: this is a product mockup photograph for a fashion campaign, so the design surface is the hero: it stays sharp, clean and fully readable inside the effect, never covered by it. "
         "It is a real photograph made in camera by a campaign photographer, not a render and not a digital filter. "+SQ+
         " Only the objects named in the shot are on set. The design surface is new and clean, crisp at its edges and corners, without blowing out."),
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','jewellery','a blue or coloured cast','marble','any object not named in the shot','fog or haze','a clean, smooth digital look'],
}
LOOK={'coat':'look_coat','shirt':'look_shirt','slip':'look_slip','gown':'look_gown'}
NOFACE=' Her face is never visible: she is turned away or cropped by the frame, and no face, cheek, chin or profile shows.'
def sh(n,slug,refs,moment,shot,look,pl,surface):
    return {'n':n,'slug':slug,'kind':'print','noun':'the design surface','refs':list(refs)+['ch13',LOOK[look]],'moment':moment,'shot':shot,
            'people':'line','people_line':pl+NOFACE,'surface':surface}
BL='nothing printed on it'
BAG='THE BAG FRONT IS PLAIN MATTE PAPER-WHITE BOARD, flat with crisp folded edges and a deep folded top cuff, '+BL+'.'
S=[
 sh(1,'flash-and-drag-spin-bag-frozen',['bag_atelier'],
  'She spins on the dark floor with our bag held out on her arm; the photographer drags the shutter and fires the flash at the end of the exposure.',
  'Technique: slow shutter, half a second, with rear-curtain flash. The bag front is frozen dead sharp by the flash, square to the camera on the centre line, filling about 50 percent of the frame width; around it the long black coat and her turning body leave soft ghost trails and smeared streaks of motion across the black, layered over the sharp moment. 35mm lens, camera at bag height, close.',
  'coat','Only her body from the shoulder down is in frame, turning away, in exactly the outfit from the reference.',BAG),
 sh(2,'blade-of-light-across-the-bag',['bag_atelier'],
  'She stands still in total darkness; one narrow blade of hard light cuts across the set and lands exactly on our bag held at her hip.',
  'Technique: a single hard spotlight shaped through a narrow slit into a sharp-edged horizontal band of light. The band lights the whole bag front, square to the camera on the centre line, filling about 45 percent of the frame width, sharp; the band also catches a slice of the deep white cuff and the belt of the shirt dress, and everything above and below it falls into pure black. 50mm lens, straight on, camera at bag height.',
  'shirt','Only her body from the waist to the knee is in frame, mostly lost in black outside the band of light, in exactly the outfit from the reference.',BAG),
 sh(3,'invitation-through-fluted-glass',[],
  'She holds a show invitation card up in front of the black gown; the photographer shoots past the edge of a sheet of fluted glass held close to the lens.',
  'Technique: the left third of the frame is seen through fluted glass right in front of the lens, breaking her gloved arm and the gown into repeated vertical ghost slices; the card itself sits in the clear part of the frame, square to the camera on the centre line, filling about 45 percent of the frame width, dead sharp, never behind the glass. One hard side light from the right. 50mm lens, close.',
  'gown','Only her gloved hand, arm and the gown from the shoulder to the waist are in frame, in exactly the outfit from the reference.',
  'THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'),
 sh(4,'long-lens-spotlight-bag-at-her-feet',['bag_atelier'],
  'Our bag stands on the dark floor at her feet inside one hard round spotlight; she stands beside it, the ivory satin catching the edge of the light.',
  'Technique: a long 200mm lens from far away and very low, compressing the space, shooting past a soft dark out-of-focus shape of satin in the foreground at the frame edge; one hard overhead spotlight makes a sharp-edged round pool on the floor with a hard shadow under the bag. The bag front is square to the camera on the centre line, filling about 45 percent of the frame width, sharp; her satin hem and heels at one side; black all around the pool.',
  'slip','Only her legs, the satin hem and her heels are in frame, in exactly the outfit from the reference.',BAG),
]
