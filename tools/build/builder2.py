"""builder2: short labelled-prose prompts for Nano Banana 2.1 (night 2 rules, see plan/night2/r_craft.md).
Usage: python3 builder2.py collections2/<file>.py [--look URL]
Collection C keys: id, name, aspect, format_words, register, world, light, palette, finish,
  cast {his,her}, wear {his: text, her: text}, avoid [<=4], look_url, look_note
Shot keys: n, slug, kind, refs [asset keys], moment (one sentence, hero first), shot (camera, hero size, hands, supporting objects),
  surface (optional override), people ('none' | 'his' | 'her' | 'both'), chars (override), avoid [<=4], look_test (bool)
"""
import sys, json, importlib.util, re, os
sys.path.insert(0, os.path.dirname(__file__))
from assets import URL, JOB

# one-line identity descriptors, reused verbatim
CHAR = {
 'ch01': ('man', 'a man of about 32 with dark textured hair, lean build'),
 'ch04': ('woman', 'a woman of about 30 with dark brown hair, slim build'),
 'ch06': ('woman', 'a woman of about 29 with long straight black hair in a high ponytail, slim build'),
 'ch07': ('woman', 'a woman of about 32 with dark curly hair tied back and olive skin'),
 'ch09': ('woman', 'a woman of about 30, East Asian, with a black blunt bob and slim hands'),
 'ch10': ('man', 'a man of about 30, Southern Italian, light olive skin, thick dark brown wavy hair pushed back, lean athletic build'),
 'ch11': ('man', 'a man of about 28, Danish, fair skin, short ash-blond hair, tall and slim'),
 'ch12': ('man', 'a man of about 32, Korean, light skin, neat thick black hair, slim build'),
 'ch13': ('woman', 'a woman of about 28, Irish, fair freckled skin, straight auburn shoulder-length hair, slim build'),
 'ch14': ('woman', 'a woman of about 30, Black British, medium-dark skin, short natural tight curls, slim build'),
 'ch15': ('woman', 'a woman of about 26, Spanish, warm light-tan skin, long dark brown wavy hair in a low ponytail'),
}
DEV = {  # ref key -> (noun, take sentence)
 'phone': ('the phone', 'its exact shape, proportions, thin even black border and dark titanium frame'),
 'air': ('the phone', 'its very thin body, exact proportions and light frame'),
 'ipad': ('the tablet', 'its exact shape, thin even black border and dark aluminium body'),
 'laptop': ('the laptop', 'its exact shape, thin bezels and dark body; no logo on the lid'),
 'keys': ('the keyboard layout', 'plain blank keycaps with even gaps, no letters'),
 'watch': ('the watch', 'its exact titanium case, crown guard and side button'),
 'display': ('the display', 'its exact thin bezel, stand and proportions; no logo'),
 'vision': ('the headset', 'its exact shape; no logo'),
 'airmax': ('the headphones', 'their exact over-ear shape; no logo'),
 'airpods': ('the earbuds case', 'its exact shape and size'),
}
SCREEN_KINDS = {'phone','air','ipad','laptop','display','watch','tv','kiosk','screen','vision','monitor','led'}

def surface_default(kind, noun):
    if kind in SCREEN_KINDS:
        return (f"THE {noun.upper()} SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, evenly bright from edge to edge, not blown out, "
                f"with crisp corners meeting its thin black border. The glass is clean, and nothing crosses the screen.")
    return (f"THE {noun.upper()} DESIGN AREA IS PLAIN BLANK WHITE, evenly lit, cleanly bounded with crisp edges, "
            f"lying flat where it rests, with nothing printed on it and nothing crossing it.")

def pick_chars(C, s):
    if 'chars' in s: return s['chars']
    p = s.get('people', 'none')
    cast = C.get('cast', {})
    if p == 'none': return []
    if p == 'both': return [cast['his'], cast['her']]
    return [cast[p]]

def refs_for(C, s):
    out = []  # (url, role sentence)
    if C.get('look_url') and not s.get('no_look'):
        out.append((C['look_url'], 'the look of this set: take its materials, light, colour and grade; ignore its camera position, composition and props'))
    for ch in pick_chars(C, s):
        g, d = CHAR[ch]
        out.append((URL[ch], f'the {g}: take only {"his" if g=="man" else "her"} skin tone, hair and build; ignore the clothes on the sheet; the face is never shown'))
    for k in s.get('refs', []):
        if k in DEV:
            noun, take = DEV[k]; out.append((URL[k], f'{noun}: take {take}'))
        else:
            out.append((URL[k], JOB[k].rstrip('.')))
    return out[:5]

def people_line(C, s):
    chs = pick_chars(C, s)
    if not chs: return ''
    parts = []
    for ch in chs:
        g, d = CHAR[ch]
        cast = C.get('cast', {})
        who = 'his' if cast.get('his') == ch else ('her' if cast.get('her') == ch else ('his' if g == 'man' else 'her'))
        wear = s.get('wear', {}).get(who) or C.get('wear', {}).get(who, '')
        parts.append(f"The person is {d}, wearing {wear}." if wear else f"The person is {d}.")
    parts.append('Crop the head out of frame, or show only the back of the head turned fully away from the camera; no profile, cheek, ear, jaw or chin is visible.')
    return ' '.join(parts)

def build_prompt(C, s):
    refs = refs_for(C, s)
    ref_txt = ' '.join(f'Image {i+1} is {r}.' for i, (_, r) in enumerate(refs))
    noun = s.get('noun') or DEV.get(s['kind'], (s['kind'],))[0]
    surf = s.get('surface') or surface_default(s['kind'], noun.replace('the ', ''))
    avoid = (C.get('avoid', [])[:4] + s.get('avoid', [])[:4])
    lines = [
        f"{C['register']}: {s['moment']}",
        f"References: {ref_txt} The output is one single photograph, {C['format_words']}." if refs else f"The output is one single photograph, {C['format_words']}.",
        f"Shot: {s['shot']} {people_line(C, s)}".strip(),
        f"Set: {C['world']}",
        f"Light: {C['light']}",
        f"Palette and grade: {C['palette']}",
        f"Design surface: {surf}",
        f"Finish: {C['finish']}",
    ]
    if avoid: lines.append('Avoid: ' + ', '.join(avoid) + '.')
    return '\n\n'.join(lines), [u for u, _ in refs]

def load(path):
    spec = importlib.util.spec_from_file_location('col', path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

if __name__ == '__main__':
    m = load(sys.argv[1]); C, S = m.C, m.S
    if '--look' in sys.argv: C['look_url'] = sys.argv[sys.argv.index('--look') + 1]
    only_tests = '--tests' in sys.argv
    out = []
    for s in S:
        if only_tests and not s.get('look_test'): continue
        if C.get('look_url') and s.get('look_test') and not only_tests: continue
        p, imgs = build_prompt(C, s)
        out.append({'id': f"{C['id']}-{s['n']:02d}", 'name': s['slug'], 'look_test': bool(s.get('look_test')),
                    'input': {'prompt': p, 'images': imgs, 'resolution': '2K', 'aspect_ratio': C.get('aspect', '4:5')}})
    os.makedirs('out2', exist_ok=True)
    json.dump(out, open(f"out2/{C['id']}{'_tests' if only_tests else ''}.json", 'w'), indent=1, ensure_ascii=False)
    print(C['id'], len(out), 'words(first)=', len(out[0]['input']['prompt'].split()) if out else 0)
