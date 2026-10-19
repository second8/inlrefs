# n28 Atelier round 19 (Sam 19 Oct): r18 finals 01, 04; 05 crouch 'really nice, make 2 more like this'. Same editorial attitude, bag at her feet, camera low at bag height.
import importlib.util,os
_d=os.path.dirname(__file__)
def _m(n):
    s=importlib.util.spec_from_file_location(n,os.path.join(_d,n+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
r4=_m('n28r4_art');r16=_m('n28r16_chic')
C=dict(r16.C);C['id']='n28r19'
sh,BAG=r4.sh,r4.BAG
S=[
 sh(1,'editorial-sprawl-on-steps-bag-by-hip',['bag_atelier'],
  'She sits sideways on the wide pale stone steps in a high-fashion editorial pose: one leg stretched long down the steps, the other bent, leaning back on one elbow; our bag stands upright on the step beside her hip.',
  'Camera low at the height of the bag, 50mm lens, f/5.6, square to the bag front. The bag stands on the centre line, front square to the camera, filling about 40 percent of the frame width, sharp; behind it her reclined figure in the long black coat makes a long diagonal line down the steps, one pointed boot stretched to the frame edge; hard sun throws strong stepped shadows; frame cropped at her shoulders.',
  'coat','Her body from the shoulders down is in frame in a long, angular, relaxed high-fashion pose, in exactly the outfit from the reference.',BAG),
 sh(2,'editorial-wall-lean-foot-on-wall-bag-at-heel',['bag_atelier'],
  'She leans flat against a sunlit pale stone wall in a high-fashion editorial pose, one knee bent and that foot planted flat against the wall behind her, arms loose at her sides; our bag stands upright on the pavement at her heel.',
  'Camera low at the height of the bag, 50mm lens, f/5.6, square to the bag front. The bag stands on the centre line, front square to the camera, filling about 40 percent of the frame width, sharp; above it her long figure in the satin slip runs up the wall, the bent knee making a sharp angle, the ivory mule pressed flat on the stone; her crisp shadow on the wall beside her; frame cropped at her shoulders.',
  'slip','Her body from the shoulders down is in frame in a strong, angular high-fashion lean, in exactly the outfit from the reference.',BAG),
]
