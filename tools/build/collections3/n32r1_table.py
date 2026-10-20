# n32 (name TBD, Sam 20 Oct) round 1: 'something more lux, like a restaurant, elegant chic, aesthetic; really like some of the glass reflections.'
# Moodboard: Figma Inlay Brand Design 202:123 (WORDS ONLY): dark bar, amber coupe and a stack of coasters on a bronze table in a pool of light;
# top-down menu card on white marble with a ribbed green water glass throwing caustics, espresso cup, a hand; coaster on olive linen with a tipped coupe and its caustic.
from builder3 import SQ
C={
 'id':'n32r1','name':'Restaurant','aspect':'4:5','format_words':'portrait 4:5',
 'register':'An elegant, chic restaurant and bar photograph for a luxury hospitality brand',
 'world':'A refined restaurant and bar: white marble, linen tablecloths, bronze and dark walnut surfaces, fine glassware; nothing else unless the shot names it.',
 'light':'One hard, directional beam of warm light, like late sun through a window or a single spotlight: crisp shadows, and bright refracted caustics thrown by the glassware onto the table.',
 'palette':'Warm and rich: creamy marble whites, deep olive, bronze, walnut and amber, inky shadows; the design surface clean warm white. The same grade on every image of the collection.',
 'real':("Real: this is a product mockup photograph for a hospitality brand, so the design surface is the hero: it is large in the frame, sharp and fully readable; caustics and reflections fall beside it, never over it. "
         "It is a real editorial photograph, never a render. "+SQ+" Only the objects named in the shot are on set. The design surface is new and clean, crisp at its edges, without blowing out. Every object is at its true real-world size."),
 'finish':'Shot on 35mm film like a high-end restaurant editorial: fine grain, rich but natural colour, deep shadows, crisp highlights in the glass; never glossy stock, never a render.',
 'avoid':['a face, chin, lips or profile','logos, letters or brand names anywhere','any print or text on the design surface','any object not named in the shot','a clean smooth 3D render look'],
}
CARD=lambda w: f'THE {w} IS PLAIN THICK WARM WHITE COTTON CARD, flat, crisp corners, nothing printed on it.'
CO='THE TOP COASTER IS PLAIN THICK WARM WHITE ROUND BOARD, flat with a crisp edge, nothing printed on it.'
def sh(n,slug,moment,shot,surface,noun,comp='B',people=None):
    d={'n':n,'slug':slug,'kind':'print','noun':noun,'refs':[],'moment':moment,'shot':shot,'surface':surface,'comp':comp}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    return d
S=[
 sh(1,'menu-card-on-marble-ribbed-glass-caustic-top-down','A menu card lies on a white marble bistro table beside a ribbed green water glass that throws bright caustic light across the stone; an espresso cup sits nearby.','Camera straight down, 50mm lens, f/5.6. The menu card lies on the centre line, edges parallel to the frame, filling about 45 percent of the frame width, sharp; the ribbed green glass at the top edge casts a long caustic shadow full of bright refracted streaks beside the card, never over it; the espresso cup on its saucer at the side; a woman\'s relaxed hand rests at the lower edge.',CARD('MENU CARD'),'the menu card',people='Only one slender hand rests at the lower edge; no face shows.'),
 sh(2,'stack-of-coasters-bronze-bar-table-amber-coupe','In a dark bar, a small stack of round coasters sits on a polished bronze table in a single pool of warm spotlight, beside a coupe glass of amber cocktail.','Camera looking down at about 70 degrees, 50mm lens, f/4, square to the top coaster. The stack sits on the centre line, its top coaster filling about 40 percent of the frame width, sharp; the coupe stands just above it, its amber glow and caustic falling on the bronze beside the stack; the rest falls into deep black.',CO,'the top coaster',comp=None),
 sh(3,'coaster-on-olive-linen-tipped-coupe-caustic','A single coaster lies on an olive linen tablecloth; an empty coupe glass lies tipped on its side touching it, throwing a bright caustic in the hard light.','Camera straight down, 50mm lens, f/5.6. The coaster sits on the centre line, flat to the camera, filling about 45 percent of the frame width, sharp; the tipped coupe lies beside it at one side, its stem reaching off the frame edge, its crisp shadow and bright caustic arc falling on the linen next to the coaster, never over it; fine linen weave visible.','THE COASTER IS PLAIN THICK WARM WHITE ROUND BOARD, flat with a crisp edge, nothing printed on it.','the coaster'),
 sh(4,'reservation-card-white-tablecloth-wine-glass-light','A small folded reservation card stands on a crisp white tablecloth beside a wine glass whose light falls across the cloth.','Camera at table height, 85mm lens, f/4, square to the card face. The card stands on the centre line, its face filling about 40 percent of the frame width, sharp; the wine glass beside it throws a warm caustic onto the cloth, never over the card; soft dark restaurant behind.',CARD('CARD FACE'),'the card face',comp=None),
 sh(5,'business-card-walnut-bar-top-whisky-caustic','A business card lies on a dark polished walnut bar top beside a heavy crystal glass of whisky that throws an amber caustic across the wood.','Camera straight down, 50mm lens, f/5.6. The card lies on the centre line, flat, filling about 40 percent of the frame width, sharp; the whisky glass at one side casts a glowing amber caustic and crisp shadow on the wood beside it, never over the card; the rich walnut grain all around.',CARD('BUSINESS CARD'),'the business card'),
]
