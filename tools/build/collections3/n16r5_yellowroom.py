# n16 round 5. Sam: "lazy, same shots, same devices, nothing new; think what devices and mockups are in this lab". Props 33-36 (Grok).
# Real cleanroom surfaces: e-paper lot tag on a wafer carrier, lot scanner, sleeved tablet, gowning poster, pass-through intercom.
import importlib.util,os
_s=importlib.util.spec_from_file_location('b',os.path.join(os.path.dirname(__file__),'n16r3_yellowroom.py'));_m=importlib.util.module_from_spec(_s);_s.loader.exec_module(_m)
C=dict(_m.C);C['id']='n16r5';C['name']='Yellow Room (round 5)'
C['world_short']='The amber yellow room of a microfabrication clean room: flush white wall panels with hairline seams, brushed stainless decks, white-panelled tools, a cool grey gowning airlock beyond a glass door.'
C['avoid']=_m.C['avoid']+['a portrait monitor or pillar screen','a hanging sign']
S=[
 {'n':1,'slug':'epaper-tag-wafer-carrier','kind':'tag','noun':'the e-paper lot tag','refs':['wafer_carrier'],'people':'none','comp':'D',
  'moment':'The small e-paper lot tag on the white door of our wafer carrier, sitting on the stainless stocker shelf.',
  'shot':'Straight on, very close, 90mm, f/4. The carrier door faces the camera dead square; the e-paper tag sits on the centre line and fills about 55 percent of the frame width, sharp; the recessed handle sits below it, and the translucent slot stack shows soft at the side. Crisp amber highlights on the edges, deep umber at the corners.',
  'surface':'THE E-PAPER TAG FACE IS PLAIN MATTE LIGHT GREY-WHITE, like paper, not glowing, evenly lit, crisp corners inside its thin white frame, nothing on it.'},
 {'n':2,'slug':'lot-scanner-gloved-over-carrier','kind':'screen','noun':'the scanner screen','refs':['lot_scanner','wafer_carrier'],'people':'glove','edge':'right','comp':'D',
  'moment':'A gloved hand holds our white lot scanner up to the carrier tag, mid-scan, its screen toward the camera.',
  'shot':'Close, 50mm, f/2.8, camera square to the scanner screen. The scanner fills about 60 percent of the frame height, its portrait screen facing the camera dead square, sharp; the carrier door is a soft white shape behind. Amber light, strong contrast.'},
 {'n':3,'slug':'sleeved-tablet-tool-hook','kind':'ipad','noun':'the tablet','refs':['tablet_sleeve'],'people':'none','comp':'A',
  'moment':'A tablet sealed in our clear cleanroom pouch hangs from a steel hook on the white panel of a lithography tool.',
  'shot':'Straight on, camera exactly at the centre of the screen, 50mm, f/2.8, close. The pouch hangs on the centre line from a single steel hook, the tablet facing the camera dead square, filling about 65 percent of the frame height, sharp; the pouch edges and soft corner creases catch thin amber highlights. The white panel with hairline seams runs behind in clean verticals.'},
 {'n':4,'slug':'gowning-poster-through-airlock-door','kind':'print','noun':'the gowning poster','refs':[],'people':'none','comp':'C',
  'moment':'Seen through the open glass door from the amber bay, a gowning procedure poster on the cool grey wall of the airlock.',
  'shot':'Straight on, camera at the centre of the poster, 50mm, f/2.8. The open door frame of brushed steel forms a tall rectangle parallel to the photo edges, amber on the near side; inside it, the portrait poster hangs on the cool pale grey airlock wall facing the camera dead square, filling about 50 percent of the frame height, sharp.',
  'surface':'THE POSTER IS PLAIN BLANK WHITE matte clean-room paper, perfectly flat, crisp corners, nothing printed on it.'},
 {'n':5,'slug':'intercom-screen-passthrough','kind':'screen','noun':'the intercom screen','refs':['passthrough'],'people':'none','comp':'D',
  'moment':'The steel intercom panel beside our pass-through hatch, its small screen lit.',
  'shot':'Straight on, very close, 90mm, f/4. The intercom panel faces the camera dead square, its small landscape screen on the centre line filling about 55 percent of the frame width, sharp; the speaker grille and round button sit below; the edge of the hatch frame shows at one side. Amber light rakes across the brushed steel; deep umber at the corners.'},
]
