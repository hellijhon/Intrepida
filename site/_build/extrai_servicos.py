"""Extrai as 9 páginas de serviço de equipe/03-copy.md para data/servicos.json.
Regra: texto exato entre crases; trechos [INSERIR DADO REAL] são omitidos e o 'Fallback' é usado."""
import re, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
md = (ROOT / 'equipe/03-copy.md').read_text()
start = md.index('### 5.1 Projeto hidrossanitário'); end = md.index('## 6. BIM e Compatibilização')
blocks = re.split(r'\n### 5\.\d ', md[start:end])
bt = lambda s: re.findall(r'`([^`]*)`', s)

def section(txt, key):
    m = re.search(r'\*\*' + key + r'[^\n]*\*\*[^\n]*\n(.*?)(?=\n\*\*SV-|\n\*\*SEO|\Z)', txt, re.S)
    return m.group(1) if m else ''

out = []
for b in blocks:
    b = b if b.startswith('### ') else b
    slug = re.search(r'\(`/servicos/([^/]+)/`\)', b).group(1)
    seo = section(b, 'SEO')
    d = {'slug': slug,
         'title': re.search(r'\*\*Title:\*\* (.+)', seo).group(1).strip(),
         'meta': re.search(r'\*\*Meta description:\*\* (.+)', seo).group(1).strip(),
         'param': re.search(r'\?servico=([a-z-]+)', seo).group(1)}
    hero = section(b, 'SV-02 Hero')
    d['eyebrow'] = bt(re.search(r'Eyebrow: (.+)', hero).group(1))[0]
    d['h1'] = bt(re.search(r'\*\*H1:\*\* (.+)', hero).group(1))[0]
    d['sub'] = bt(re.search(r'Subtítulo: (.+)', hero).group(1))[0]
    d['cta'] = bt(re.search(r'CTA: (.+)', hero).group(1))[0]
    m = re.search(r'imagem (\d)', hero); d['hero_img'] = int(m.group(1)) if m else None
    al = re.search(r'Alt[^`]*`([^`]+)`', hero); d['hero_alt_ilustr'] = al.group(1) if al else None
    s3 = section(b, 'SV-03')
    d['entregas_h2'] = bt(re.search(r'H2: (.+)', s3).group(1))[0]
    d['entregas_intro'] = bt(re.search(r'Intro: (.+)', s3).group(1))[0]
    d['entregas'] = [bt(l)[0] for l in s3.split('\n') if re.match(r'^- `', l)]
    s4 = section(b, 'SV-04')
    d['quem_h2'] = bt(re.search(r'H2: (.+)', s4).group(1))[0]
    d['quem'] = [{'t': bt(l)[0], 'd': bt(l)[1]} for l in s4.split('\n') if re.match(r'^- `', l)]
    s5 = section(b, 'SV-05')
    d['normas_h2'] = bt(re.search(r'H2: (.+)', s5).group(1))[0]
    d['normas_txt'] = bt(re.search(r'Texto: (.+)', s5).group(1))[0]
    nm = re.search(r'- Normas:\n((?:  .*\n?)*)', s5)
    d['normas'] = [bt(l)[0] for l in (nm.group(1).split('\n') if nm else []) if re.match(r'^  - `', l)]
    one = re.search(r'- Normas: `([^`]+)`', s5)
    if one: d['normas'] = [one.group(1)]
    om = re.search(r'- Órgãos: (.+)', s5); d['orgaos'] = bt(om.group(1))[0] if om else None
    integ = re.search(r'- Integração: (.+)', s5); d['integracao'] = bt(integ.group(1))[0] if integ else None
    s6 = section(b, 'SV-06')
    d['bim_h2'] = bt(re.search(r'H2: (.+)', s6).group(1))[0]
    d['bim_txt'] = bt(re.search(r'Texto: (.+)', s6).group(1))[0]
    im = re.search(r'Image[mn]s?: (.+)', s6); d['bim_imgs'] = [int(x) for x in re.findall(r'\b(\d)\b', im.group(1).split('13.2')[-1])] if im else []
    d['bim_raw'] = im.group(1) if im else ''
    s8 = section(b, 'SV-08')
    d['faq_h2'] = bt(re.search(r'H2: (.+)', s8).group(1))[0]
    faqs = []
    for q in re.finditer(r'^\d\. \*\*(.+?)\*\*[^\n]*\n((?:   .*\n?)+)', s8, re.M):
        body = q.group(2)
        fb = re.search(r'Fallback: `([^`]*)`', body)
        ans = fb.group(1) if fb else bt(body)[0]
        link = re.search(r'\(link para `([^`]+)`\)', body)
        faqs.append({'q': q.group(1), 'a': ans, 'link': link.group(1) if link else None})
    d['faq'] = faqs
    s9 = re.search(r'\*\*SV-09\*\* — H2: `([^`]+)` \((.*)\)\s*$', b, re.M)
    d['outros_h2'] = s9.group(1); d['outros_raw'] = s9.group(2)
    d['cta_h2'] = bt(re.search(r'\*\*SV-10\*\* — H2: (.+)', b).group(1))[0]
    out.append(d)
json.dump(out, open(pathlib.Path(__file__).parent / 'data/servicos.json', 'w'), ensure_ascii=False, indent=1)
for d in out:
    print(d['slug'], '| hero', d['hero_img'], '| bim', d['bim_imgs'], d['bim_raw'][:60], '| ent', len(d['entregas']), '| quem', len(d['quem']), '| normas', len(d['normas']), '| faq', len(d['faq']), '| org', bool(d['orgaos']), '| int', bool(d['integracao']))
    print('   outros:', d['outros_raw'])
