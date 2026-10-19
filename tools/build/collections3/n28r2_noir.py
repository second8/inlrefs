# n28 Atelier round 2 (Sam 17 Oct feedback): round 1 'bad studio', clothes too close to his inspo, poses corporate, not elegant.
# His new inspo (B&W, black backdrop to grey floor, grain): take its feel. New: 4 looks (props 94-97) + marble block (98).
# Never his inspo's bag, wordmark or exact pose. 18 shots.
from builder3 import SQ
C={
 'id':'n28r2','name':'Atelier','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A black-and-white luxury fashion campaign photograph shot in a photo studio',
 'world':'A fashion photo studio: a deep charcoal-black seamless backdrop fading to near black at the top and edges, meeting a pale grey floor sweep that catches a soft pool of light. Only what the shot names is on set.',
 'light':'One very large soft box from the side at about head height, wrapping the fabric in long soft gradients; no fill, so one side of every form falls away into deep shadow and the studio around her goes nearly black, while the floor catches a soft pool of light.',
 'palette':'Black and white only, no colour anywhere: rich neutral greys, deep soft blacks, the design surface the cleanest paper white in the frame. Soft rich contrast.',
 'finish':'Medium-format black-and-white film, 80mm and 100mm macro, f/4 to f/5.6, heavy fine film grain over the whole frame, soft rolled highlights, deep blacks, no halation, no haze. Quiet, expensive, editorial, like a luxury house campaign.',
 'cast':{'her':'ch13'},
 'real':("Real: this is a product mockup photograph for a fashion campaign, so the design surface is the hero: it is large in the frame and the camera is close to it, never a wide shot of the studio. "
         "It is a real photograph taken on set by a fashion photographer, not a render, and the clothes are real heavy fabric with real weight and folds. "+SQ+
         " Only the objects named in the shot are on set. Framing is deliberate and geometric: the design surface's edges line up with the frame. "
         "Exposure is honest; the design surface is new and clean, crisp at its edges and corners; any lit screen is bright and clean, clearly the brightest surface in the frame, without blowing out. No halation or glow around lights."),
 'avoid':['a face, head, chin, lips or profile','logos, letters or brand names anywhere','jewellery','any colour','any object not named in the shot','a stiff or corporate pose','a glossy computer-generated look'],
}
POSE=' Her pose is a deliberate high-fashion pose: long angled lines, weight dropped onto one hip, shoulders loose, never stiff or corporate.'
def PL(span='from the shoulder down to below the knee'):
    return f'Only her body {span} is in frame, in exactly the outfit from the reference, the heavy fabric falling in large soft folds; her head and face are never in frame.'+POSE
def HAND(what='her hand and the end of her sleeve'):
    return f'Only {what} are in frame, in exactly the outfit from the reference; nothing else of her is visible, no head or face.'
LOOK={'coat':'look_coat','shirt':'look_shirt','slip':'look_slip','gown':'look_gown'}
def sh(n,slug,kind,noun,refs,comp,moment,shot,look=None,pl=None,surface=None,**kw):
    r=list(refs)+(['ch13',LOOK[look]] if look else [])
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':r,'comp':comp,'moment':moment,'shot':shot}
    if look: d['people_line']=pl or PL(); d['people']='line'
    else: d['people']='none'
    if surface: d['surface']=surface
    d.update(kw); return d
BL='nothing printed on it'
BAG='THE BAG FRONT IS PLAIN MATTE PAPER-WHITE BOARD, flat with crisp folded edges and a deep folded top cuff, '+BL+'.'
S=[
 sh(1,'bag-in-elbow-crook-stride','print','the bag front',['bag_atelier'],'A',
  'She strides across the studio with our shopping bag hooked in the crook of her bent elbow, the long black coat swinging open behind her.',
  'Straight on to the bag, camera at the height of the bag, 85mm, f/4. The bag front faces the camera square on the centre line, filling about 55 percent of the frame width, sharp; her forearm is raised level across the top of the frame with the handles over it and the wrist hanging loose; her body is in mid-stride behind the bag, the coat hem flaring in a long curve.',
  look='coat',pl=PL('from the collar down to below the knee'),surface=BAG),
 sh(2,'bag-held-out-at-arms-length','print','the bag front',['bag_atelier'],'D',
  'Standing side-on, she holds our bag out at full arm\'s length toward the camera by its handles, the deep stiff white cuff of her shirt dress at the top of the frame.',
  'Very close, 85mm, f/4, camera square to the bag front. The bag front fills about 65 percent of the frame on the centre line, sharp; her hand, wrist and the big white cuff hold the handles at the top edge; her long figure falls away soft and dark behind.',
  look='shirt',pl='Her arm, hand and the deep white shirt cuff are sharp at the top of the frame; behind, her figure from the shoulder down is soft and dark, in exactly the outfit from the reference; her head and face are never in frame.'+POSE,surface=BAG),
 sh(3,'seated-on-marble-bag-beside','print','the bag front',['bag_atelier','marble'],'A',
  'She sits on our white marble block with her legs crossed, the satin slip pooling over the stone, our bag standing on the block beside her hip.',
  'Camera at the height of the block top, 80mm, f/4. The bag stands on the marble on the centre line, front square to the camera, filling about 45 percent of the frame width, sharp; beside it her seated figure leans back on one straight arm, the cardigan sliding off one shoulder, the satin spilling over the block edge.',
  look='slip',pl=PL('from the shoulder down to her ankles'),surface=BAG),
 sh(4,'crouched-low-bag-on-floor','print','the bag front',['bag_atelier'],'A',
  'She crouches low on one heel, the black gown pooling around her on the floor, one gloved hand resting on top of our bag\'s handles.',
  'Low, camera at floor height, 80mm, f/4. The bag stands on the grey floor on the centre line, front square to the camera, filling about 55 percent of the frame height, sharp; her gloved hand rests on the handles; behind it her folded figure and the matte black jersey spread out across the floor in soft folds.',
  look='gown',pl=PL('from the shoulder down, crouched'),surface=BAG),
 sh(5,'walking-away-bag-on-shoulder','print','the bag front',['bag_atelier'],'A',
  'She walks away from the camera, our bag hanging from its handles hooked over her shoulder and resting against the back of the black coat.',
  'Straight on from behind, camera at the height of the bag, 85mm, f/4. The bag front faces the camera square on the centre line, filling about 50 percent of the frame width, sharp, lying flat against her back; the coat falls in long soft folds below it, one boot lifting mid-step.',
  look='coat',pl=PL('from the collar down to the floor, seen from behind'),surface=BAG),
 sh(6,'hang-tag-on-coat-cuff','print','the hang tag',['hangtag'],'D',
  'Her arm lifted, the hand relaxed at the coat collar, our hang tag hanging from the black coat cuff on its cord.',
  'Very close, 100mm macro, f/5.6, camera square to the tag. The tag hangs on the centre line, filling about 55 percent of the frame height, sharp; the thick black wool cuff and her slim wrist fill the frame around it in soft folds.',
  look='coat',pl=HAND('her hand, wrist and the black coat cuff'),surface='THE TAG FACE IS PLAIN THICK PAPER-WHITE CARD, flat, softly rounded corners, '+BL+'.'),
 sh(7,'tissue-seal-on-marble','print','the seal',['tissue','marble'],'B',
  'Our folded tissue bundle closed with its round seal, resting on the white marble block.',
  'Directly from above, lens pointing straight down, 80mm, f/5.6. The tissue bundle sits on the honed marble on the centre line, its edges parallel to the frame; the round seal at its centre fills about 25 percent of the frame width, sharp; the soft grey veins run across the stone around it and one clean diagonal of shadow crosses the marble beside it.',
  surface='THE SEAL FACE IS A PLAIN MATTE BLACK ROUND, flat, crisp edge, '+BL+'.'),
 sh(8,'garment-cover-on-black-hook','print','the front panel',['gcover'],'A',
  'Our garment cover hangs alone from a single black steel hook in the studio, and her gloved hand reaches in to the top of its zip.',
  'Straight on, camera at the front panel, 80mm, f/5.6. The cover hangs on the centre line, front square to the camera, filling about 75 percent of the frame height; the pale front panel sharp; the side light rakes across the canvas; her long black glove enters from the side at the top of the zip; the backdrop falls to black.',
  look='gown',pl=HAND('her arm in the long black glove'),surface='THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
 sh(9,'woven-label-inside-open-coat','print','the woven label',[],'D',
  'She holds one side of the black coat wide open with her hand, showing the inside and the woven label stitched there.',
  'Very close, 100mm macro, f/5.6, camera square to the label. The label sits on the centre line, filling about 45 percent of the frame width, sharp, stitched at both ends onto the black lining; her fingers grip the coat edge at the frame side; the heavy wool curves away in soft shadow.',
  look='coat',pl=HAND('her hand and the open edge of the coat'),surface='THE LABEL IS PLAIN WOVEN WHITE RIBBON with a fine weave texture, flat, '+BL+'.'),
 sh(10,'invitation-between-gloved-fingers','print','the invitation card',[],'D',
  'Her gloved hand holds a show invitation card between two fingers at her hip, against the matte black gown.',
  'Straight on, close, 85mm, f/5.6, camera square to the card. The card fills about 50 percent of the frame width on the centre line, sharp; two black satin fingertips pinch its corner; the gown drape gathers at her hip behind it.',
  look='gown',pl=HAND('her gloved hand and the gown at her hip'),surface='THE CARD IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp corners, '+BL+'.'),
 sh(11,'lookbook-on-marble-satin-spill','print','the lookbook cover',['marble'],'B',
  'A slim lookbook lies closed on the white marble block, the ivory satin of her slip spilling over the stone beside it as she sits there.',
  'Directly from above, lens pointing straight down, 80mm, f/5.6. The lookbook cover sits on the marble on the centre line, edges parallel to the frame, filling about 55 percent of the frame width, sharp; along one side the satin and the edge of her knee pool in liquid folds over the stone.',
  look='slip',pl=HAND('the satin of her skirt and the edge of her knee'),surface='THE COVER IS PLAIN MATTE PAPER-WHITE BOARD, flat, crisp corners and spine, '+BL+'.'),
 sh(12,'place-card-on-marble','print','the place card',['marble'],'A',
  'A folded show place card stands on the white marble block, waiting for a guest.',
  'Low, camera at the height of the block top, 100mm, f/5.6. The tent-folded place card stands on the centre line, front square to the camera, filling about 45 percent of the frame width, sharp; the marble edge runs level across the lower frame; the backdrop behind is near black.',
  surface='THE CARD FRONT IS PLAIN THICK PAPER-WHITE COTTON CARD, flat, crisp fold and corners, '+BL+'.'),
 sh(13,'phone-at-hip-black-coat','phone','the phone',['phone'],'D',
  'Hand on her hip, she holds her phone flat against the black coat, screen facing out.',
  'Straight on, close, 85mm, f/4, camera square to the screen. The phone fills about 45 percent of the frame height on the centre line, screen sharp; her fingers wrap its side; the black wool and her bent elbow make a sharp angle around it.',
  look='coat',pl=HAND('her hand, wrist and the coat around her hip')+POSE),
 sh(14,'phone-framed-by-deep-cuff','phone','the phone',['phone'],'C',
  'Her arm reaches out slightly, the phone held lightly in her fingers, the deep stiff white cuff of the shirt dress around her wrist.',
  'Straight on, close, 85mm, f/4, camera square to the screen. The phone fills about 45 percent of the frame height on the centre line, screen sharp; the tall white cuff and the full gathered sleeve rise behind and around it like a frame.',
  look='shirt',pl=HAND('her hand, the white cuff and the full sleeve')),
 sh(15,'tablet-on-knees-against-marble','ipad','the tablet',['ipad','marble'],'A',
  'She sits on the floor leaning back against the marble block, knees drawn up, the tablet resting on her knees, screen facing the camera.',
  'Camera low at knee height, 85mm, f/4, square to the screen. The tablet fills about 55 percent of the frame width on the centre line, screen sharp; her gloved hands hold its sides; the matte black gown falls over her knees and pools on the floor; the white marble edge runs level behind.',
  look='gown',pl=PL('from the shoulder down, seated on the floor')),
 sh(16,'laptop-on-marble-figure-passing','laptop','the laptop',['laptop','marble'],'A',
  'A laptop open on the white marble block in the studio; she walks past behind in the white shirt dress, a soft blur.',
  'Straight on, camera at screen height, 80mm, f/2.8. The laptop sits on the centre line, screen square to the camera, filling about 55 percent of the frame width, sharp; the honed marble and its grey veins under it; behind, her white figure passes as a soft motion blur, head out of frame.',
  look='shirt',pl='Behind, only her body from the shoulder down passes as a soft motion blur, in the outfit from the reference; her head is out of frame.'),
 sh(17,'bag-hanging-low-hand-on-hip','print','the bag front',['bag_atelier'],'A',
  'Weight on one hip, one hand on her hip, she lets our bag hang low from her other hand by the handles beside her calf.',
  'Camera at the height of the bag, 80mm, f/4. The bag front faces the camera square on the centre line in the lower half of the frame, filling about 50 percent of the frame width, sharp; above it the satin slip falls in liquid lines and the draped cardigan sleeve swings.',
  look='slip',pl=PL('from the waist down to the floor'),surface=BAG),
 sh(18,'garment-cover-over-shoulder','print','the front panel',['gcover'],'A',
  'She carries our garment cover over her shoulder by its hanger hook as she walks past, the front panel facing the camera.',
  'Straight on, camera at the front panel, 85mm, f/4. The cover hangs down her back and side on the centre line, front square to the camera, filling about 65 percent of the frame height, the pale panel sharp; her hand grips the hanger hook at the top edge; the white shirt dress and its big cuff move beside it.',
  look='shirt',pl=PL('from the shoulder down to below the knee'),surface='THE FRONT PANEL IS PLAIN PAPER-WHITE COTTON, flat and stitched, crisp corners, '+BL+'.'),
]
