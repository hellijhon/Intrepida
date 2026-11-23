"""Mapa do Brasil em SVG (contornos oficiais do IBGE, data/br-ufs.geojson) com pins
nos estados onde a Intrépida atua.

Fonte dos contornos: API de Malhas do IBGE
https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=minima&intrarregiao=UF
"""
import html, json, math, pathlib

B = pathlib.Path(__file__).resolve().parent
COD = {'11': 'RO', '12': 'AC', '13': 'AM', '14': 'RR', '15': 'PA', '16': 'AP', '17': 'TO', '21': 'MA', '22': 'PI', '23': 'CE',
       '24': 'RN', '25': 'PB', '26': 'PE', '27': 'AL', '28': 'SE', '29': 'BA', '31': 'MG', '32': 'ES', '33': 'RJ', '35': 'SP',
       '41': 'PR', '42': 'SC', '43': 'RS', '50': 'MS', '51': 'MT', '52': 'GO', '53': 'DF'}
W = 600  # largura do viewBox
LAT0 = math.radians(-15)
# Ajustes finos de posição do pin (em unidades do viewBox) onde o centroide fica ruim visualmente
AJUSTE = {'RJ': (2, 2), 'SC': (2, 0), 'PB': (4, 0), 'DF': (0, 0)}


def _carregar():
    d = json.load(open(B / 'data' / 'br-ufs.geojson', encoding='utf-8'))
    ufs = {}
    for f in d['features']:
        g = f['geometry']
        polys = g['coordinates'] if g['type'] == 'MultiPolygon' else [g['coordinates']]
        ufs[COD[f['properties']['codarea']]] = polys
    return ufs


def _proj(lon, lat):
    return lon * math.cos(LAT0), -lat


def _area_centroide(ring):
    a = cx = cy = 0.0
    for (x1, y1), (x2, y2) in zip(ring, ring[1:] + ring[:1]):
        k = x1 * y2 - x2 * y1
        a += k; cx += (x1 + x2) * k; cy += (y1 + y2) * k
    a /= 2
    return abs(a), (cx / (6 * a), cy / (6 * a)) if a else ring[0]


def gerar_svg(ativos, links=None, titulo=''):
    """ativos: {UF: texto do tooltip}; links: {UF: href} para estados clicáveis."""
    links = links or {}
    ufs = _carregar()
    pts = [_proj(x, y) for polys in ufs.values() for poly in polys for ring in poly for x, y in ring]
    minx, maxx = min(p[0] for p in pts), max(p[0] for p in pts)
    miny, maxy = min(p[1] for p in pts), max(p[1] for p in pts)
    s = W / (maxx - minx)
    H = round((maxy - miny) * s)
    tr = lambda x, y: ((_proj(x, y)[0] - minx) * s, (_proj(x, y)[1] - miny) * s)

    formas, pins = [], []
    for uf in sorted(ufs, key=lambda u: u in ativos):  # estados ativos por cima
        d, maior = [], (0, None)
        for poly in ufs[uf]:
            for i, ring in enumerate(poly):
                r = [tr(x, y) for x, y in ring]
                d.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in r) + 'Z')
                if i == 0:
                    a, c = _area_centroide(r)
                    if a > maior[0]: maior = (a, c)
        on = uf in ativos
        attrs = f' data-uf-go="{uf}"' if uf in links else ''
        tit = f'<title>{html.escape(ativos[uf])}</title>' if on else ''
        formas.append(f'<path class="mb-uf{" is-on" if on else ""}{" is-link" if uf in links else ""}" d="{"".join(d)}"{attrs}>{tit}</path>')
        if on:
            cx, cy = maior[1]
            dx, dy = AJUSTE.get(uf, (0, 0))
            cx, cy = cx + dx, cy + dy
            pins.append(f'<g class="mb-pin{" is-link" if uf in links else ""}" transform="translate({cx:.1f} {cy:.1f})"{attrs}>{tit}'
                        f'<g class="mb-pin__s"><circle class="mb-pin__pulse" r="8"/>'
                        f'<path class="mb-pin__body" d="M0,0 C-3,-7 -11,-12 -11,-21 A11,11 0 1 1 11,-21 C11,-12 3,-7 0,0Z"/>'
                        f'<circle class="mb-pin__dot" cy="-21" r="4.2"/>'
                        f'<text class="mb-pin__uf" y="-36" text-anchor="middle">{uf}</text></g></g>')
    return (f'<svg class="mapa-br" viewBox="-20 -56 {W + 40} {H + 70}" role="img" aria-label="{html.escape(titulo)}" '
            f'xmlns="http://www.w3.org/2000/svg"><g class="mb-ufs">{"".join(formas)}</g><g class="mb-pins">{"".join(pins)}</g></svg>')
