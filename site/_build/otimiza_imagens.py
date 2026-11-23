"""Gera os assets web a partir das fontes em equipe/ (fotos, BIM, marca) e de _build/src-ia/.
Saída: site/assets/img/** + _build/data/imagens.json (dimensões de cada variante).
Requer só Pillow (WebP). Uso: python3 otimiza_imagens.py"""
import json, pathlib, re, statistics
from PIL import Image, ImageChops, ImageDraw, ImageOps

B = pathlib.Path(__file__).resolve().parent
SITE = B.parent; EQ = SITE.parent / 'equipe'; IMG = SITE / 'assets/img'
man = {}

def save_set(im, outdir, name, widths, q=78, crop=None):
    import os
    if os.environ.get('SO_LOGOS') and (outdir / f'{name}-{min(widths)}.webp').exists():
        W, H = ImageOps.exif_transpose(im).size; vs = sorted(set(min(w, W) for w in widths))
        man[f'{outdir.relative_to(IMG)}/{name}'] = {'w': W, 'h': H, 'widths': vs, 'ratio': round(W / H, 4)}; return
    outdir.mkdir(parents=True, exist_ok=True)
    im = ImageOps.exif_transpose(im).convert('RGB')
    W, H = im.size; vs = []
    for w in sorted(set(min(w, W) for w in widths)):
        h = round(H * w / W); r = im.resize((w, h), Image.LANCZOS)
        r.save(outdir / f'{name}-{w}.webp', 'WEBP', quality=q, method=6)
        r.save(outdir / f'{name}-{w}.jpg', 'JPEG', quality=q + 4, optimize=True, progressive=True)
        vs.append(w)
    man[f'{outdir.relative_to(IMG)}/{name}'] = {'w': W, 'h': H, 'widths': vs, 'ratio': round(W / H, 4)}

def trim_white(im, pad=0.05, thr=245):
    g = im.convert('L').point(lambda v: 255 if v < thr else 0)
    bb = g.getbbox()
    if not bb: return im
    x0, y0, x1, y1 = bb; p = int(max(x1 - x0, y1 - y0) * pad)
    W, H = im.size
    return im.crop((max(0, x0 - p), max(0, y0 - p), min(W, x1 + p), min(H, y1 + p)))

PROJ = {'mirante-sao-lucas': 'mirante-sao-lucas', 'bosque-dos-ipes': 'bosque-dos-ipes',
        'parque-lagoa-dos-principes': 'parque-lagoa-dos-principes-e-lagoa-nova', 'residencial-monte-carlo': 'residencial-monte-carlo',
        'residencial-vila-atlantico': 'residencial-vila-atlantico', 'residencial-vila-maria': 'residencial-vila-maria',
        'residencial-alta-vista': 'residencial-alta-vista', 'residencial-ville-luxemburgo': 'residencial-ville-luxemburgo',
        'residencial-portal-do-cerrado': 'residencial-portal-do-cerrado', 'residencial-scharle': 'residencial-scharle',
        'residencial-pacifico': 'residencial-pacifico', 'residencial-portal-do-engenho': 'residencial-portal-do-engenho'}
for f in sorted((EQ / 'fotos/obras-empreendimentos').glob('*.jpeg')):
    slug = next(v for k, v in PROJ.items() if k in f.name)
    save_set(Image.open(f), IMG / 'projetos', slug, [480, 800, 1200, 1600, 2400], q=74)

for i, f in enumerate(sorted((EQ / 'fotos/bim-modelos-3d').glob('*.jpeg')), 1):
    save_set(trim_white(Image.open(f).convert('RGB')), IMG / 'bim', f'bim-{i:02d}', [480, 800, 1200, 1800], q=80)

for f in sorted((B / 'src-ia').glob('*.png')):
    save_set(trim_white(Image.open(f).convert('RGB'), pad=0.04), IMG / 'ilustracoes', f.stem, [480, 800, 1200, 1800], q=80)

save_set(Image.open(EQ / 'marca/portfolio-2024_fundo-capa_5339x3049.jpeg'), IMG / 'marca', 'fundo-azul', [800, 1600, 2400], q=64)

# ---- logos de clientes: versão monocromática (mesma forma, cor única) ----
NOMES = ['precon', 'mrv', 'direcional', 'tenda', 'riva', 'rni', 'vic', 'patrimar', 'novolar', 'quartzo', 'erglares', 'rrx',
         'prix', 'mello-azevedo', 'vitta', 'mcp', 'cte', 'gabbai', 'unenco', 'brz', 'vila', 'chandon', 'center-norte', 'catagua']
INK = (74, 85, 98)  # neutral-600 #4A5562
(IMG / 'clientes').mkdir(parents=True, exist_ok=True)
for f in sorted((EQ / 'marca/logos-clientes').glob('*.jpeg')):
    n = int(re.search(r'cliente-(\d+)', f.name).group(1)); slug = NOMES[n - 1]
    im = Image.open(f).convert('RGB')
    if slug == 'mello-azevedo':  # logo original é um retângulo branco sobre fundo preto: usa só o retângulo
        im = im.crop(im.convert('L').point(lambda v: 255 if v > 200 else 0).getbbox())
    W, H = im.size
    kc = {'brz': 0.0}.get(slug, 0.55)
    px = im.load()
    border = [px[x, y] for x in range(0, W, max(1, W // 60)) for y in (0, H - 1)] + [px[x, y] for y in range(0, H, max(1, H // 30)) for x in (0, W - 1)]
    bg = tuple(statistics.median(c[i] for c in border) for i in range(3))
    lum = lambda c: (0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]) / 255
    Lb = lum(bg)
    a = Image.new('L', (W, H)); ap = a.load(); vals = []
    for y in range(H):
        for x in range(W):
            c = px[x, y]
            d = (((c[0] - bg[0]) ** 2 + (c[1] - bg[1]) ** 2 + (c[2] - bg[2]) ** 2) ** .5) / 441
            ink = max(abs(lum(c) - Lb), kc * d)
            ap[x, y] = int(ink * 255)
            if ink > 0.03: vals.append(ink)
    vals.sort(); top = vals[int(len(vals) * 0.98)] if vals else 1
    if slug == 'brz':  # quadrado amarelo vira cinza claro proporcional; texto escuro fica cheio
        a = a.point(lambda v: min(255, int(v / (top * 255) * 255)))
    else:              # binário com borda suave: qualquer traço acima do ruído do JPEG vira tinta
        lo, hi = 0.045 * 255, 0.13 * 255
        a = a.point(lambda v: 0 if v <= lo else 255 if v >= hi else int((v - lo) / (hi - lo) * 255))
    if slug == 'chandon':  # traço muito fino no original: engrossa levemente para continuar legível reduzido
        from PIL import ImageFilter; a = a.filter(ImageFilter.MaxFilter(7))
    bb = a.point(lambda v: 255 if v > 40 else 0).getbbox(); a = a.crop(bb)
    out = Image.new('RGBA', a.size, INK + (0,)); out.putalpha(a)
    th = 120
    if out.size[1] > th: out = out.resize((round(out.size[0] * th / out.size[1]), th), Image.LANCZOS)
    out.save(IMG / f'clientes/{slug}.png', optimize=True)
    out.save(IMG / f'clientes/{slug}.webp', 'WEBP', quality=90, method=6)
    man[f'clientes/{slug}'] = {'w': out.size[0], 'h': out.size[1], 'ratio': round(out.size[0] / out.size[1], 4)}

# ---- favicon a partir do símbolo vetorial (polígonos retos) ----
svg = (IMG / 'marca/logo-intrepida-simbolo.svg').read_text()
polys = [(fill, [tuple(map(float, p.split())) for p in re.findall(r'[ML]([\d.]+ [\d.]+)', d)])
         for fill, d in re.findall(r'fill="(#\w+)" d="([^"]+)"', svg)]
def icon(size, bg=None, pad=0.14):
    S = size * 4; im = Image.new('RGBA', (S, S), bg or (0, 0, 0, 0)); dr = ImageDraw.Draw(im)
    w, h = 74.765, 118.128; sc = S * (1 - 2 * pad) / h; ox = (S - w * sc) / 2; oy = S * pad
    for fill, pts in polys: dr.polygon([(ox + x * sc, oy + y * sc) for x, y in pts], fill=fill)
    return im.resize((size, size), Image.LANCZOS)
icon(32, pad=0.04).save(SITE / 'favicon-32.png'); icon(180, (255, 255, 255, 255)).save(SITE / 'apple-touch-icon.png')
icon(192, (255, 255, 255, 255)).save(IMG / 'marca/icon-192.png'); icon(512, (255, 255, 255, 255)).save(IMG / 'marca/icon-512.png')
icon(48, pad=0.04).save(SITE / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
(SITE / 'favicon.svg').write_text(svg.replace('viewBox="-0.50 -0.50 75.77 119.13"', 'viewBox="-22 -0.5 119.77 119.13"'))
# og-image 1200x630
og = Image.open(EQ / 'fotos/obras-empreendimentos/portfolio-2024_p08_mirante-sao-lucas_UNENCO_bh-MG_4096x2304.jpeg').convert('RGB')
og = ImageOps.fit(og, (1200, 630), Image.LANCZOS); og.save(IMG / 'marca/og-image.jpg', quality=82, optimize=True)

json.dump(man, open(B / 'data/imagens.json', 'w'), indent=1)
print(len(man), 'conjuntos')
