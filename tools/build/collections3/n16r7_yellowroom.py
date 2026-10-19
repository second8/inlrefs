# n16 round 7, final big round (Sam: "we need 9 more"). Scanner "+1 creativity", pod "really nice". New lab surfaces only, props 66-70,
# pr07 badge, passthrough. Badge retried with no body words (r6 badge blocked by the content filter).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n16r6_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n16r7';C['name']='Yellow Room (round 7)'
BL='nothing printed on it; it alone reads neutral white'
def sh(n,slug,kind,noun,refs,comp,moment,shot,surface=None,avoid=None,**kw):
    d={'n':n,'slug':slug,'kind':kind,'noun':noun,'refs':refs,'people':'none','comp':comp,'moment':moment,'shot':shot}
    if surface: d['surface']=surface
    if avoid: d['avoid']=avoid
    d.update(kw);return d
S=[
 sh(1,'id-badge-coverall-pocket','card','the ID badge',['pr07'],'D',
  'A blank ID badge clipped to the pocket flap of a white clean-room coverall hanging on a steel hook in the airlock.',
  'Straight on, very close, 90mm, f/4, camera square to the badge. The badge hangs flat on the centre line from its metal clip, filling about 55 percent of the frame height, sharp; the white coverall fabric with its pocket seam fills the background in fine woven texture, cool grey light with a thin amber edge.',
  'THE BADGE FACE IS PLAIN BLANK WHITE matte card in a clear sleeve, flat, crisp rounded corners, '+BL+'.'),
 sh(2,'resist-bottle-chemical-cabinet','print','the bottle label',['resist'],'A',
  'Our amber photoresist bottle standing alone on the steel shelf of the open chemical cabinet in the yellow room.',
  'Straight on, camera exactly at the label, 85mm, f/4, close. The bottle stands on the centre line, label square to the camera, filling about 65 percent of the frame height, sharp; the cabinet sides form clean verticals either side; crisp amber highlights on the glass and steel.',
  'THE LABEL IS PLAIN MATTE WHITE, flat on the glass, crisp edges, '+BL+'.',['hazard symbols','other bottles']),
 sh(3,'garment-bag-hook-airlock','print','the bag label',['garmentbag'],'A',
  'Our sealed cleanroom garment bag hanging from a steel hook on the white wall of the cool grey airlock.',
  'Straight on, camera exactly at the label pocket, 50mm, f/2.8, close. The bag hangs on the centre line, its white label pocket square to the camera, filling about 70 percent of the frame height, sharp; the folded white coverall shows soft through the clear film; cool pale grey light, one thin amber edge from the bay door.',
  'THE LABEL IS PLAIN MATTE WHITE card in the flat pocket, crisp corners, '+BL+'.'),
 sh(4,'label-printer-screen-label-out','screen','the printer screen',['labelprinter'],'D',
  'Our white label printer on the stainless bench, a fresh blank label coming out of its slot, its small screen lit.',
  'Straight on, very close, 90mm, f/4, camera exactly at the screen. The small landscape screen sits on the centre line, square to the camera, filling about 50 percent of the frame width, sharp; below it the three keys and the blank label strip emerging from the slot; amber light, deep umber at the corners.',avoid=['printed text on the label']),
 sh(5,'particle-counter-dock-stainless','screen','the counter screen',['particle'],'A',
  'Our handheld particle counter standing in its white dock on the brushed stainless bench, its portrait screen lit.',
  'Straight on, camera exactly at the screen, 85mm, f/4, close. The counter stands on the centre line, its screen square to the camera, filling about 65 percent of the frame height, sharp; the stainless sampling probe points up; amber highlights along the bench edge; deep umber behind.',avoid=['numbers or graphs on the screen']),
 sh(6,'door-nameplate-interlocked-door','print','the nameplate',[],'D',
  'A small flush nameplate on the white wall panel beside the interlocked glass door of the yellow room.',
  'Straight on, very close, 90mm, f/4, camera exactly at the plate. The landscape nameplate sits on the centre line, square to the camera, filling about 60 percent of the frame width, sharp; at one edge the brushed steel door frame runs vertically; amber light rakes across the panel.',
  'THE NAMEPLATE IS PLAIN MATTE WHITE ACRYLIC, flat, crisp corners, '+BL+'.'),
 sh(7,'glovebox-screen-beside-gloves','screen','the glovebox screen',['glovebox'],'C',
  'Our stainless glovebox in the bay, its long black gloves hanging in the ports, the flush screen lit above the window.',
  'Straight on, camera exactly at the screen, 50mm, f/2.8. The steel panel frames the landscape screen on the centre line with an even margin, square to the camera, filling about 50 percent of the frame width, sharp; below, the slanted window and the two glove ports show soft; amber reflections on the steel.'),
 sh(8,'cleanroom-notebook-stainless-top-down','print','the notebook cover',[],'B',
  'A white cleanroom notebook lying closed on the brushed stainless bench.',
  'Directly from above, lens pointing straight down, 50mm, f/2.8, close. The notebook lies square to the frame, filling about 60 percent of the frame height, sharp; the brushed grain of the steel runs in one direction; one clean diagonal amber highlight crosses the steel beside it, never over it.',
  'THE COVER IS PLAIN MATTE WHITE synthetic cleanroom paper board, flat, crisp corners and spine, '+BL+'.',['a pen','a spiral binding']),
 sh(9,'sample-bag-label-through-hatch','print','the sample bag label',['passthrough'],'C',
  'Seen through the glass door of our pass-through hatch, a sealed clear sample bag with a white label lies inside on the steel floor of the hatch.',
  'Straight on, camera at the centre of the hatch, 50mm, f/2.8. The square steel hatch frame sits on the centre line with its edges parallel to the photo edges; through the clean glass, the bag lies flat with its label square to the camera, the label filling about 40 percent of the frame width, sharp. Amber light, one soft reflection at a glass corner.',
  'THE LABEL IS PLAIN MATTE WHITE, flat on the clear bag, crisp corners, '+BL+'.'),
]
