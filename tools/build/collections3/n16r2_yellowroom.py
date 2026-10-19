# n16 Yellow Room round 2. Sam: "add more contrast, make it more sleek". Look test passed earlier (amber safelight; paper stays white).
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'..','collections2','n16_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C={
 'id':'n16r2','name':'Yellow Room (round 2)','aspect':'4:5','format_words':'portrait 4:5',
 'register':'A sleek industrial product photograph inside a real photolithography clean room',
 'world':'The yellow room of a microfabrication clean room: seamless pale epoxy floor coved into flush white wall panels with hairline seams, a flush ceiling grid of white filter panels and linear lamps, a few white-panelled tools with brushed stainless decks, a flush pass-through hatch and an interlocked glass door to the gowning airlock. Pared back to a few clean, precise lines.',
 'light':'Ceiling lamps wear the real lithography sleeve that removes blue light, so the whole bay glows amber; white balance stays at daylight. High contrast: crisp, bright amber highlights on the lit planes and deep umber shadows that fall away fast. The airlock beyond the glass door is cool pale grey. Screens stay neutral white.',
 'palette':'Monochrome amber: sodium yellow #E8B33A, honey #F2E2B0, warm stainless #B9B4A2, deep umber shadow #2A1D0B, airlock grey #D8DADB, violet-black #2B2A3A gloves. The design surface alone is clean neutral white. Strong contrast, rich blacks, crisp highlights.',
 'finish':'Full-frame camera, 50mm and 90mm, f/2.8 to f/4: crisp but natural, fine grain, no halation or haze. Sleek and precise, like a high-end tech campaign photographed on location.',
 'cast':_m.C['cast'],'wear':{'his':'a white clean-room coverall reading honey-amber in the safelight, with violet-black nitrile gloves','her':'a white clean-room coverall reading honey-amber in the safelight, with violet-black nitrile gloves'},
 'avoid':['lettering, numbers or symbols anywhere','a face, eye, cheek or profile','blue light in the bay','flat, low-contrast light','haze or halation'],
}
S=[
 {'n':1,'slug':'aligner-touchscreen-gloved-close','kind':'screen','noun':'the tool touchscreen','refs':['ipad'],'people':'her','edge':'right',
  'moment':'A gloved fingertip confirms a step on the mask aligner touchscreen.',
  'shot':'Close three-quarter at chest height, 50mm, f/2.8. The landscape touchscreen set flush in the white tool face fills about 60 percent of the frame width, sharp; her violet-black gloved index finger touches its lower right corner. The tool face falls from bright amber to deep umber shadow toward the edges.'},
 {'n':2,'slug':'laptop-airlock-shelf-grey','kind':'laptop','refs':['laptop'],'people':'none',
  'moment':'A laptop open on the stainless shelf in the cool grey airlock, the amber bay glowing through the glass door behind it.',
  'shot':'Three-quarter at standing height, 50mm, f/2.8, close. The open laptop on the slim stainless shelf fills about 60 percent of the frame width, sharp, in cool pale grey light; behind it the glass door frames a slab of saturated amber from the bay, soft. Strong contrast between the grey and the amber.'},
 {'n':3,'slug':'sequence-panel-wall','kind':'sign','noun':'the wall panel','refs':[],'people':'none',
  'moment':'A flush wall panel beside the airlock door shows the gowning sequence.',
  'shot':'Frontal and slightly off-axis, 50mm, f/4, at eye height. The portrait panel, flush in the white wall with a hairline shadow gap, fills about 65 percent of the frame height, sharp. The amber light rakes across the wall from above so the panel edges catch a crisp highlight and the lower wall falls into umber.',
  'surface':'THE PANEL IS PLAIN BLANK WHITE, matte, perfectly flat with crisp square corners, nothing printed on it; it alone reads neutral white.'},
 {'n':4,'slug':'sop-sheet-magnetic-holder','kind':'print','noun':'the laminated SOP sheet','refs':[],'people':'none',
  'moment':'The laminated procedure sheet waits in its slim magnetic holder on the tool side panel.',
  'shot':'Frontal, square to the panel, 85mm, f/4, close. The A4 portrait sheet in a slim stainless magnetic frame fills about 70 percent of the frame height, sharp. Amber light from above leaves a crisp bright top edge and a fast fall into shadow at the bottom.',
  'surface':'THE SHEET IS PLAIN BLANK WHITE under clear laminate, lying perfectly flat in the frame, crisp corners, nothing printed on it; it alone reads neutral white.','avoid':['a curled corner']},
 {'n':5,'slug':'inspection-monitor-swing-arm','kind':'monitor','noun':'the inspection monitor','refs':['display'],'people':'none',
  'moment':'The inspection microscope monitor on its swing arm, pulled out over the stainless deck.',
  'shot':'Three-quarter from below eye height, 50mm, f/2.8. The slim monitor on a brushed-steel swing arm fills about 55 percent of the frame width, sharp; the white microscope body is a soft amber shape behind it. Deep umber shadow in the upper corners, crisp highlights along the arm.'},
]
