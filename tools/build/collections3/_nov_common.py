# Shared helper for the Nov 2026 collections (n35 Nature, n36 Terminal, n37 Night Square). Same shot dict shape as n31r1.
def sh(n,slug,moment,shot,surface,noun,comp='A',people=None,aspect='4:5',refs=None):
    fw={'4:5':'portrait 4:5','16:9':'landscape 16:9','4:3':'landscape 4:3','3:4':'portrait 3:4'}[aspect]
    d={'n':n,'slug':slug,'kind':'print','noun':noun,'refs':refs or [],'moment':moment,'shot':shot,'surface':surface,'comp':comp,'aspect':aspect,'format_words':fw}
    if people: d['people']='line';d['people_line']=people
    else: d['people']='none'
    return d
PRINT=lambda what: f'{what} IS PLAIN MATTE PAPER-WHITE, flat and taut edge to edge with crisp corners, nothing printed on it and nothing crossing it.'
SCREEN=lambda what: f'{what} SHOWS A PLAIN WHITE FULL-SCREEN IMAGE, glowing bright and clean, clearly the brightest thing in the frame, evenly lit edge to edge yet not blown out, with crisp corners meeting its thin dark frame; nothing crosses it.'
