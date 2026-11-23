"""Converte o stream vetorial do logo (PDF/AI exportado do Illustrator) em SVG.
Uso: python3 pdf2svg_logo.py <arquivo.pdf> <saida-base>
Gera <saida-base>-azul.svg, <saida-base>-branco.svg e <saida-base>-simbolo.svg.
Suporta o subconjunto de operadores usado pelo arquivo (q/Q/cm/m/l/c/v/y/h/re/f/f*/scn/rg)."""
import re, sys, zlib

NAVY, WHITE = '#0B3859', '#FFFFFF'

def load_content(fn):
    d = open(fn, 'rb').read()
    page = re.search(rb'/Contents (\d+) 0 R', d).group(1)
    mb = [float(x) for x in re.search(rb'/MediaBox\[([^\]]*)\]', d).group(1).split()]
    m = re.search(rb'\b' + page + rb' 0 obj\s*<<(.*?)>>\s*stream\r?\n', d, re.S)
    ln = int(re.search(rb'/Length (\d+)', m.group(1)).group(1))
    return zlib.decompress(d[m.end():m.end() + ln]).decode('latin1'), mb

def mul(a, b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3], a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3],
            a[4]*b[0]+a[5]*b[2]+b[4], a[4]*b[1]+a[5]*b[3]+b[5]]

def hexcol(vals):
    return '#%02X%02X%02X' % tuple(round(max(0, min(1, v))*255) for v in vals)

def parse(content, H):
    toks = re.findall(r'/[^\s/\[\]<>()]+|[-+]?\d*\.?\d+|[A-Za-z*]+', content)
    stack, ctm, gstack, fill = [], [1, 0, 0, 1, 0, 0], [], (0, 0, 0)
    path, fills, clip_skip = [], [], False
    def P(x, y):
        X = ctm[0]*x + ctm[2]*y + ctm[4]; Y = ctm[1]*x + ctm[3]*y + ctm[5]
        return '%.3f %.3f' % (X, H - Y)
    for t in toks:
        if re.match(r'^[-+]?\d*\.?\d+$', t): stack.append(float(t)); continue
        if t.startswith('/'): stack.append(t); continue
        a = stack
        if t == 'q': gstack.append((ctm[:], fill))
        elif t == 'Q': ctm, fill = gstack.pop()
        elif t == 'cm': ctm = mul(a[-6:], ctm)
        elif t in ('scn', 'sc', 'rg'): fill = tuple(a[-3:])
        elif t == 'k':
            c, m_, y, k = a[-4:]; fill = ((1-c)*(1-k), (1-m_)*(1-k), (1-y)*(1-k))
        elif t == 'm': path.append('M' + P(a[-2], a[-1]))
        elif t == 'l': path.append('L' + P(a[-2], a[-1]))
        elif t == 'c': path.append('C' + P(a[-6], a[-5]) + ' ' + P(a[-4], a[-3]) + ' ' + P(a[-2], a[-1]))
        elif t == 'v': path.append('C' + P(*last) + ' ' + P(a[-4], a[-3]) + ' ' + P(a[-2], a[-1])) if False else path.append('S' + P(a[-4], a[-3]) + ' ' + P(a[-2], a[-1]))
        elif t == 'y': path.append('C' + P(a[-4], a[-3]) + ' ' + P(a[-2], a[-1]) + ' ' + P(a[-2], a[-1]))
        elif t == 'h': path.append('Z')
        elif t == 're':
            x, y, w, h = a[-4:]
            path.append('M%sL%sL%sL%sZ' % (P(x, y), P(x+w, y), P(x+w, y+h), P(x, y+h)))
        elif t in ('f', 'f*', 'F'):
            fills.append((''.join(path), hexcol(fill), 'evenodd' if t == 'f*' else 'nonzero')); path = []
        elif t == 'n': path = []
        stack = [] if t not in () else stack
    return fills

def bbox(fills):
    xs, ys = [], []
    for d, _, _ in fills:
        nums = [float(n) for n in re.findall(r'-?\d+\.\d+', d)]
        xs += nums[0::2]; ys += nums[1::2]
    return min(xs), min(ys), max(xs), max(ys)

def write(fn, fills, recolor, title):
    x0, y0, x1, y1 = bbox(fills)
    pad = 0.5
    vb = '%.2f %.2f %.2f %.2f' % (x0-pad, y0-pad, x1-x0+2*pad, y1-y0+2*pad)
    out = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-labelledby="t"><title id="t">%s</title>' % (vb, title)]
    for d, col, rule in fills:
        out.append('<path fill="%s"%s d="%s"/>' % (recolor(col), ' fill-rule="evenodd"' if rule == 'evenodd' else '', d))
    out.append('</svg>')
    open(fn, 'w').write(''.join(out))
    return vb

def brand(col):
    r, g, b = int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16)
    if b > r: return NAVY            # azul do logotipo
    if g < 0x50: return '#EF4036'    # vermelho
    return '#F15A29'                 # laranja

if __name__ == '__main__':
    src, base = sys.argv[1], sys.argv[2]
    content, mb = load_content(src)
    fills = parse(content, mb[3])
    print('fills:', len(fills), sorted(set(c for _, c, _ in fills)))
    print('azul', write(base + '-azul.svg', fills, brand, 'Intrépida Engenharia e Projetos'))
    print('branco', write(base + '-branco.svg', fills, lambda c: WHITE if brand(c) == NAVY else brand(c), 'Intrépida Engenharia e Projetos'))
    sym = [f for f in fills if brand(f[1]) != NAVY]
    print('simbolo', write(base + '-simbolo.svg', sym, brand, 'Intrépida'))
