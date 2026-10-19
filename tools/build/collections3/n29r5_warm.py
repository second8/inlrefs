# n29 Spatial Awareness round 5 (Sam 19 Oct): new inspo (the Modern Gothic lobby lightbox, Figma 191:1327) 'use this more as look and feel: colour, light, grading',
# take also its composition. Described in words only (hard rule). Keep r4 structure: one hall, a different moodboard installation per shot.
import importlib.util,os
_s=importlib.util.spec_from_file_location('r4',os.path.join(os.path.dirname(__file__),'n29r4_hall.py'));r4=importlib.util.module_from_spec(_s);_s.loader.exec_module(r4)
C=dict(r4.C);C['id']='n29r5'
C['world']=('One and the same museum entrance lobby in every image: low ceiling with a deep soffit lit from above in a soft warm peach-salmon glow, smooth warm cream and beige plaster walls, '
            'a dark doorway or glass door at the left edge, and a dark polished stone floor that holds a soft blurred reflection of the light. Quiet, after hours, nobody working.')
C['light']=('Two lights only: the installation glows a clean, slightly cool white, and the ceiling soffit glows warm peach above; together they light the cream walls in a warm, low, even dimness. '
            'Soft contrast, no hard spotlights; the floor reflection is soft and blurred, not mirror sharp.')
C['palette']=('Warm and soft: peach and salmon at the ceiling, warm cream and sand walls, deep warm brown-black floor; the glowing face is clean white with the faintest cool tint, '
              'so it stands apart from the warm room. Slightly lifted soft blacks. The same grade on every image of the collection.')
C['finish']='Like a quiet documentation photo of a museum lobby taken on a good camera at high ISO: soft natural grain, gentle highlight roll-off, a little softness at the edges, honest dim exposure. Real and unpolished, never a render.'
COMPN=' Framing like a straight, frontal documentation photo: the camera stands square to the work at chest height, the work sits a little left of centre, the warm ceiling band fills the top fifth of the frame and the dark floor the bottom quarter.'
S=[]
for x in r4.S:
    y=dict(x); y['shot']=x['shot']+COMPN; y.pop('comp',None); S.append(y)
S[0]['moment']='A huge backlit wall panel glows across most of one wall of the warm, dim museum lobby; one visitor stands to the side.'
S[0]['shot']='Camera at chest height, 35mm lens, f/4, square to the panel. The glowing panel fills about 60 percent of the frame width; its soft reflection on the dark floor below; the warm peach soffit across the top of the frame; a dark doorway at the left edge; one visitor small at the right.'+COMPN
