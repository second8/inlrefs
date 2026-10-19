"""builder3: builder2 plus a realism layer (Sam, 16 Oct: night 2 batch read 'too perfect', people too much in frame).
Changes vs builder2:
- No look image by default (the look tests were the too-perfect frames; feeding them back copied the finish).
- 'Real' block on every prompt: a real place in use, small signs of age on the place only, a working photographer's
  framing, honest exposure, screens at room brightness.
- People are foreshadowed, never the subject:
    'edge'  only a hand / forearm / sleeve entering from a frame edge, slightly soft
    'far'   one figure small and out of focus deep in the background, back turned
    'trace' nobody in frame; a sign someone was just here (described in the shot text)
  Legacy 'his'/'her'/'both' are treated as 'edge' for that person.
- Screens no longer 'evenly bright edge to edge'; they sit at the brightness of the room.
Shot keys as builder2, plus: who ('his'|'her') for edge/far, edge ('left'|'right'|'bottom').
Usage: python3 builder3.py collections3/<file>.py
"""
import sys, json, os
sys.path.insert(0, os.path.dirname(__file__))
from assets import URL, JOB
from builder2 import CHAR, DEV, SCREEN_KINDS, load

REAL = ("Real: this is a product mockup photograph, so the design surface is the hero: it fills most of the frame and the "
        "camera is close to it, the way a photographer frames a product, never an establishing shot of the room. The place is only "
        "context, glimpsed in fragments at the edges and falling into deep shadow; large parts of the frame are allowed to go "
        "nearly black. It is an unstaged photograph of a real place in use, not a set and not a showroom, with small honest signs "
        "of age on the place only (fine scuffs, a slightly mismatched replacement panel, lines very slightly uneven); the design "
        "surface itself is new and clean. The design surface faces the camera almost square-on, within about 15 degrees, so it reads flat and undistorted; its four edges run parallel to the edges of the photograph, a true rectangle, never a trapezoid or keystone; flat things on a table are shot from nearly straight above. Only the objects named in the shot are in frame. Framing is deliberate and geometric: the design surface's edges line up with the frame and with the strong lines of the place. "
        "Exposure is honest and nothing looks retouched or edited, but any lit screen is bright and clean, clearly the brightest "
        "surface in the frame, without blowing out: its edges and corners stay crisp. No halation or glow around lights.")

COMP = {
 'A': "Composition A, centred and symmetric: the design surface sits on the centre line, square to the camera, with even space on both sides; strong verticals and horizontals run parallel to the frame.",
 'B': "Composition B, top-down grid: the camera looks straight down; the design surface's edges run exactly parallel to the frame edges; one clean diagonal of light or shadow crosses the frame beside it, never over it.",
 'C': "Composition C, frame within a frame: the design surface sits inside a real opening or shape of the place, whose edges run parallel to the photo edges and frame it with an even margin.",
 'D': "Composition D, tight crop: the camera is very close; the design surface fills most of the frame, its edges nearly touching the photo edges; only a sliver of what holds it shows.",
}

SQ = ("The design surface faces the camera almost square-on, within about 15 degrees, so it reads flat and undistorted; its four edges run parallel to the edges of the photograph, a true rectangle, never a trapezoid or keystone; flat things on a table are shot from nearly straight above.")

def surface_default(kind, noun):
    if kind in SCREEN_KINDS:
        return (f"THE {noun.upper()} SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly brighter than "
                f"everything else in the frame, evenly lit edge to edge yet not blown out, with crisp corners meeting its thin black "
                f"border; nothing crosses the screen.")
    return (f"THE {noun.upper()} DESIGN AREA IS PLAIN BLANK WHITE, lit by the room's own light, cleanly bounded with crisp "
            f"edges, lying flat where it rests, with nothing printed on it and nothing crossing it.")

def mode(C, s):
    p = s.get('people', 'none')
    if p in ('his', 'her'): return 'edge', p
    if p == 'both': return 'edge', 'her'
    return p, s.get('who', 'her')

def char_for(C, who):
    return C.get('cast', {}).get(who)

def refs_for(C, s):
    out = []
    if C.get('look_url') and s.get('use_look'):
        out.append((C['look_url'], 'the look of this place: take its materials, colour and light only; ignore its composition, camera position and props'))
    for u, take in s.get('looks', []):
        out.append((u, f'an inspiration photograph: take only its {take}; do not copy its objects, room, furniture, props or layout'))
    m, who = mode(C, s)
    if m in ('edge','back'):
        ch = char_for(C, who); g, _ = CHAR[ch]
        out.append((URL[ch], f'the {g}: take only {"his" if g=="man" else "her"} skin tone and hands; ignore the clothes and the face on the sheet'))
    for k in s.get('refs', []):
        if k in DEV:
            noun, take = DEV[k]; out.append((URL[k], f'{noun}: take {take}'))
        else:
            out.append((URL[k], JOB[k].rstrip('.')))
    return out[:5]

def people_line(C, s):
    if s.get('people_line'): return s['people_line']
    m, who = mode(C, s)
    wear = (s.get('wear', {}) or {}).get(who) or C.get('wear', {}).get(who, '')
    if m == 'edge':
        ch = char_for(C, who); g, d = CHAR[ch]
        side = s.get('edge', 'right')
        sleeve = f", in the sleeve of {wear}," if wear else ''
        return (f"Only {'his' if g=='man' else 'her'} hand and part of the forearm{sleeve} enter from the {side} edge of the frame, "
                f"relaxed and slightly soft; the rest of the person is out of frame, and no head, face, shoulder or hair is visible.")
    if m == 'far':
        ch = char_for(C, who); g, d = CHAR[ch]
        w = f", in {wear}," if wear else ''
        where = (' ' + s['far_where']) if s.get('far_where') else ''
        return (f"Far behind, deep in the background and well out of focus, one {g}{w}{where}, small in the frame and seen from behind, "
                f"turned away and half in shadow, just a soft shape that tells you someone is here.")
    if m == 'back':
        ch = char_for(C, who); g, d = CHAR[ch]
        return (f"The back of the {g}'s head and one shoulder ({d}) fill the {s.get('edge','left')} edge of the frame, large, dark and "
                f"well out of focus in the foreground, turned fully away from the camera; no face, cheek, ear, profile or chin is visible.")
    if m == 'tip':
        return (f"Only one gloved fingertip, {s.get('tipwear','in a violet-black nitrile glove')}, enters from the {s.get('edge','right')} edge "
                f"and rests lightly on the {s.get('tipon','screen edge')}; nothing else of the person is in frame.")
    if m == 'glove':
        return (f"Only one gloved hand, {s.get('tipwear','in a violet-black nitrile glove with a white coverall cuff')}, enters from the {s.get('edge','right')} edge "
                f"and holds it in a relaxed, natural working grip; nothing else of the person is in frame.")
    if m == 'trace':
        return 'Nobody is in frame, but someone was here a moment ago.'
    return 'Nobody is in frame.'

def build_prompt(C, s):
    refs = refs_for(C, s)
    ref_txt = ' '.join(f'Image {i+1} is {r}.' for i, (_, r) in enumerate(refs))
    noun = s.get('noun') or DEV.get(s['kind'], (s['kind'],))[0]
    surf = s.get('surface') or surface_default(s['kind'], noun.replace('the ', ''))
    ca = C.get('avoid', [])
    ca = ca if len(ca) <= 7 else ca[:2] + ca[-5:]
    avoid = list(dict.fromkeys(ca + s.get('avoid', [])[:3]))
    lines = [
        f"{C['register']}: {s['moment']}",
        (f"References: {ref_txt} " if refs else '') + f"The output is one single photograph, {C['format_words']}.",
        (f"{COMP[s['comp']]} " if s.get('comp') else '') + f"Shot: {s['shot']} {people_line(C, s)}".strip(),
        f"Place: {C.get('world_short') or C['world']}",
        f"Light: {C['light']}",
        f"Palette and grade: {C['palette']}",
        (C.get('real') or (REAL.replace(SQ, C['real_angle']) if C.get('real_angle') else REAL)),
        f"Design surface: {surf}",
        f"Finish: {C['finish']}",
    ]
    if avoid: lines.append('Avoid: ' + ', '.join(avoid) + '.')
    return '\n\n'.join(lines), [u for u, _ in refs]

if __name__ == '__main__':
    m = load(sys.argv[1]); C, S = m.C, m.S
    only = None
    if '--only' in sys.argv: only = {int(x) for x in sys.argv[sys.argv.index('--only') + 1].split(',')}
    out = []
    for s in S:
        if only and s['n'] not in only: continue
        p, imgs = build_prompt(C, s)
        out.append({'id': f"{C['id']}-{s['n']:02d}", 'name': s['slug'],
                    'input': {'prompt': p, 'images': imgs, 'resolution': '2K', 'aspect_ratio': C.get('aspect', '4:5')}})
    os.makedirs('out3', exist_ok=True)
    tag = '_t' if only else ''
    json.dump(out, open(f"out3/{C['id']}{tag}.json", 'w'), indent=1, ensure_ascii=False)
    print(C['id'], len(out), 'words(first)=', len(out[0]['input']['prompt'].split()) if out else 0)
