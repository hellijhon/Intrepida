"""Extrai de equipe/03-copy.md: 18 projetos (8.1 + 8.2), legendas BIM (13.2) e nomes dos clientes (13.3)."""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
md = (ROOT / 'equipe/03-copy.md').read_text()
sec = lambda a, b: md[md.index(a):md.index(b)]
rows = lambda t: [[c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', l.strip().strip('|'))] for l in t.split('\n') if re.match(r'^\| *\d', l)]
UF = {'MG': 'Minas Gerais', 'DF': 'Distrito Federal', 'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MS': 'Mato Grosso do Sul', 'SC': 'Santa Catarina'}
p81 = rows(sec('### 8.1 Os 18 projetos', 'Pontos para o QA'))
p82 = {int(r[0]): r for r in rows(sec('### 8.2 SEO e alt por projeto', 'Quando chegarem as fotos'))}
projs = []
for r in p81:
    n = int(r[0]); cli, loc = [x.strip() for x in r[3].split('·')]
    cidade, uf = loc.rsplit('/', 1)
    seo = p82[n]
    projs.append({'n': n, 'slug': r[1].strip('`'), 'nome': r[2], 'cliente': cli, 'cidade': cidade, 'uf': uf, 'estado': UF[uf],
                  'unidades': r[4].replace(' unidades', ''), 'foto': r[5].startswith('Sim'), 'baixa_res': 'baixa' in r[5],
                  'relacionados': [x.strip() for x in r[6].split('·')],
                  'title': seo[1].replace('\\|', '|'), 'meta': seo[2], 'alt': None if seo[3].startswith('—') else seo[3]})
bim = []
for r in rows(sec('### 13.2 Imagens BIM', 'Galeria da Home')):
    leg = re.findall(r'`([^`]+)`', r[2])[0]
    bim.append({'n': int(r[0]), 'legenda': leg, 'confirmar': 'A CONFIRMAR' in r[2], 'alt': r[3].strip('`')})
cli = {}
for r in rows(sec('### 13.3 Logos de clientes', '(Grafias conferidas')):
    cli[int(r[0])] = r[1].strip('`'); cli[int(r[2])] = r[3].strip('`')
json.dump({'projetos': projs, 'bim': bim, 'clientes': [cli[i] for i in range(1, 25)]},
          open(pathlib.Path(__file__).parent / 'data/conteudo.json', 'w'), ensure_ascii=False, indent=1)
for p in projs: print(p['n'], p['slug'], p['cliente'], p['cidade'], p['uf'], p['unidades'], p['foto'], len(p['title']), p['relacionados'][0])
print([b['legenda'] for b in bim]); print([cli[i] for i in range(1, 25)])
