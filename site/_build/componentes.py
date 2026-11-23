"""Componentes globais (C01–C24) do site da Intrépida.
Cada função devolve o HTML de um componente; no Elementor, cada uma vira um template
global / seção salva com o mesmo código (ver equipe/04-guia-migracao-elementor.md)."""
import html, json, pathlib, re, urllib.parse

B = pathlib.Path(__file__).resolve().parent
SITE = B.parent
IMGS = json.load(open(B / 'data/imagens.json'))
SERV = json.load(open(B / 'data/servicos.json'))
C = json.load(open(B / 'data/conteudo.json'))
PROJ = C['projetos']; BIM = C['bim']; CLIENTES = C['clientes']

DOMINIO = 'https://intrepidaengenharia.com.br'
WA_NUM = '5531996498629'
TEL_TXT, TEL_HREF = '(31) 3070-6568', 'tel:+553130706568'
EMAIL = 'carlos@intrepidaengenharia.com.br'
END_1, END_2, END_3 = 'Rua dos Goitacazes, 103, salas 1604 e 1606', 'Centro, Belo Horizonte/MG', 'CEP 30190-910'
END_LINHA = 'Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910'

# Modo revisão: mostra selos "PLACEHOLDER" nos pontos que aguardam material real. False no build de produção.
REVISAO = True

# Dados que só o cliente pode dar. Enquanto vazios, as seções CONDICIONAIS ficam ocultas
# (o HTML sai com um comentário marcando o lugar). Preencher aqui e rodar build.py de novo.
DADOS = {
    'razao_social': None, 'cnpj': None, 'crea_empresa': None, 'crea_rt': None,
    'horario': None,                 # ex.: 'Segunda a sexta, das 8h às 18h'
    'atendimento_presencial': None,  # ex.: 'Atendimento presencial com hora marcada.' → ativa CT-05
    'linkedin_empresa': None, 'linkedin_rt': None,
    'pdf_portfolio': None,           # ex.: '/assets/docs/portfolio-intrepida.pdf'
    'prazo_resposta_dias': None,     # ex.: 2
    'concessionarias': [],           # ex.: ['COPASA', 'CEMIG', 'Gasmig']
    'foto_rt': None,                 # ex.: 'sobre/carlos-alberto-grope' (chave do manifesto de imagens)
    'depoimentos': [],               # [{'citacao','nome','cargo','empresa'}]
    'equipe': [],                    # [{'nome','funcao','foto'}]
    'linha_do_tempo': [],            # [{'ano','marco'}]
    'disciplinas_por_projeto': {},   # {'mirante-sao-lucas': ['hidrossanitario', 'eletrica']}
    'upload_max_mb': 20,             # limite do formulário (depende do servidor de e-mail)
}

e = lambda s: html.escape(str(s), quote=True)

def ic(name, cls='', label=None):
    a = f' role="img" aria-label="{e(label)}"' if label else ' aria-hidden="true" focusable="false"'
    return f'<svg class="icon{(" " + cls) if cls else ""}"{a}><use href="/assets/img/icons.svg#i-{name}"/></svg>'

ARW = ic('arrow', 'icon--sm arw')

def wa(msg):
    return f'https://wa.me/{WA_NUM}?text=' + urllib.parse.quote(msg)

WA = {
    'padrao': 'Olá! Vim pelo site da Intrépida e quero falar sobre um projeto.',
    'home': 'Olá! Vim pelo site da Intrépida e quero um orçamento de projeto.',
    'hub': 'Olá! Vim pela página de serviços do site da Intrépida e quero ajuda para definir os projetos do meu empreendimento.',
    'bim': 'Olá! Vim pelo site da Intrépida e quero falar sobre projetos em BIM e compatibilização.',
    'projetos': 'Olá! Vi os projetos no site da Intrépida e quero falar sobre o meu empreendimento.',
    'sobre': 'Olá! Vim pela página Sobre do site da Intrépida e quero falar sobre um projeto.',
    'contato': 'Olá! Estou na página de contato do site da Intrépida e prefiro conversar por aqui.',
    'obrigado': 'Olá! Acabei de enviar um pedido de orçamento pelo site da Intrépida e quero mandar os arquivos do projeto.',
    '404': 'Olá! Não encontrei uma página no site da Intrépida. Podem me ajudar?',
}
def wa_servico(nome): return f'Olá! Vim pelo site da Intrépida (página: {nome}) e quero um orçamento.'
def wa_projeto(nome): return f'Olá! Vi o projeto {nome} no site da Intrépida e tenho um empreendimento parecido.'

# ---- Serviços: rótulos (copy 1.4), grupos, ícones e textos curtos (H-05 e SH-04/06) ----
G_PRED, G_INFRA, G_EFIC = 'Instalações prediais', 'Infraestrutura urbana', 'Eficiência e sustentabilidade'
SM = [  # slug, rótulo curto, nome da página, param, grupo, ícone, desc. home (H-05), H3 do hub, desc. hub
 ('projeto-hidrossanitario', 'Hidrossanitário', 'Projeto hidrossanitário', 'hidrossanitario', G_PRED, 'hidro',
  'Água fria e quente, esgoto, águas pluviais e medição individualizada.', 'Projeto hidrossanitário',
  'Água fria e quente, esgoto, ventilação, águas pluviais e medição individualizada por unidade, nos padrões da concessionária de saneamento.'),
 ('projeto-eletrico', 'Elétrica e Sistemas', 'Projeto elétrico e de sistemas', 'eletrica', G_PRED, 'eletrica',
  'Entrada de energia, quadros, iluminação, tomadas e sistemas prediais.', 'Elétrica e Sistemas',
  'Entrada de energia, medição, quadros, iluminação, tomadas e sistemas prediais, calculados para a aprovação na distribuidora.'),
 ('projeto-de-gas', 'Gás', 'Projeto de gás', 'gas', G_PRED, 'gas',
  'Rede interna de gás natural ou GLP, prumadas e medição.', 'Projeto de gás',
  'Rede interna de gás natural ou GLP, medição e ventilação dos ambientes, para ligar o gás com segurança.'),
 ('climatizacao-hvac', 'Climatização (HVAC)', 'Projeto de climatização (HVAC)', 'hvac', G_PRED, 'hvac',
  'Ar-condicionado, ventilação e exaustão dimensionados pela carga térmica.', 'Climatização (HVAC)',
  'Ar-condicionado, ventilação e exaustão mecânica, com espaço para equipamentos e dutos resolvido no projeto.'),
 ('pressurizacao-de-escadas', 'Pressurização de escadas', 'Projeto de pressurização de escadas', 'pressurizacao', G_PRED, 'pressurizacao',
  'Controle de fumaça nas escadas de emergência do edifício.', 'Pressurização de escadas',
  'Sistema que mantém a escada de emergência livre de fumaça, conforme a norma e o Corpo de Bombeiros.'),
 ('projeto-de-piscina', 'Piscina', 'Projeto de piscina', 'piscina', G_PRED, 'piscina',
  'Filtragem, recirculação, casa de máquinas e aquecimento.', 'Projeto de piscina',
  'Filtragem, recirculação, casa de máquinas e aquecimento para piscinas de condomínios e residências.'),
 ('infraestrutura-de-saneamento', 'Infraestrutura de saneamento', 'Projeto de infraestrutura de saneamento', 'saneamento', G_INFRA, 'saneamento',
  'Redes de água, esgoto e drenagem para loteamentos e condomínios, prontas para a análise da concessionária.', 'Infraestrutura de saneamento',
  'Redes de distribuição de água, coleta de esgoto e drenagem pluvial para loteamentos, condomínios e conjuntos com vários blocos. Projetos nos padrões da concessionária e da prefeitura, sob a direção técnica de um engenheiro civil sanitarista.'),
 ('reuso-de-agua-pluvial', 'Reúso de água pluvial', 'Projeto de aproveitamento de água de chuva', 'reuso-pluvial', G_EFIC, 'reuso',
  'Captação e aproveitamento da água de chuva para usos não potáveis.', 'Reúso de água pluvial',
  'Captação da água de chuva para descargas, irrigação e lavagem, com rede separada da água potável.'),
 ('aquecimento-solar', 'Aquecimento solar', 'Projeto de aquecimento solar', 'aquecimento-solar', G_EFIC, 'solar',
  'Coletores, reservatórios térmicos e rede de água quente.', 'Aquecimento solar',
  'Coletores, reservatórios térmicos e rede de água quente dimensionados pelo consumo, individuais ou coletivos.'),
]
SMAP = {s[0]: s for s in SM}
BY_LABEL = {s[1]: s for s in SM}
def surl(slug): return f'/servicos/{slug}/'
def grupo(g): return [s for s in SM if s[4] == g]
GRUPO_LINHA = {G_PRED: 'Sistemas do edifício, do subsolo à cobertura.', G_INFRA: 'Redes de água, esgoto e drenagem.', G_EFIC: 'Menos consumo de água e energia.'}

CLI_LOGO = {  # nome do cliente (projeto) → arquivo do logo monocromático
 'UNENCO': 'unenco', 'RNI': 'rni', 'Vila Construtora': 'vila', 'MRV': 'mrv', 'Quartzo': 'quartzo', 'Erglares': 'erglares',
 'Precon': 'precon', 'Prix Construtora': 'prix', 'VIC': 'vic', 'Direcional Engenharia': 'direcional', 'Vitta': 'vitta'}
LOGO_SLUGS = ['precon', 'mrv', 'direcional', 'tenda', 'riva', 'rni', 'vic', 'patrimar', 'novolar', 'quartzo', 'erglares', 'rrx',
              'prix', 'mello-azevedo', 'vitta', 'mcp', 'cte', 'gabbai', 'unenco', 'brz', 'vila', 'chandon', 'center-norte', 'catagua']
LOGO_TEXTO = {'mello-azevedo'}  # raster ilegível: nome em texto até o cliente enviar o vetor (UX-18)
LOGOS_12 = ['mrv', 'direcional', 'tenda', 'patrimar', 'rni', 'precon', 'vic', 'prix', 'unenco', 'quartzo', 'mello-azevedo', 'vitta']

# ---------------- Imagens ----------------
def picture(key, alt, sizes='100vw', eager=False, cls='', max_default=1200):
    m = IMGS[key]; ws = m['widths']; r = m['ratio']
    srcw = lambda ext: ', '.join(f'/assets/img/{key}-{w}.{ext} {w}w' for w in ws)
    dflt = max([w for w in ws if w <= max_default] or [ws[0]])
    load = 'fetchpriority="high" decoding="async"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ''
    return (f'<picture><source type="image/webp" srcset="{srcw("webp")}" sizes="{sizes}">'
            f'<img{c} src="/assets/img/{key}-{dflt}.jpg" srcset="{srcw("jpg")}" sizes="{sizes}" width="{dflt}" height="{round(dflt / r)}" alt="{e(alt)}" {load}></picture>')

def logo_img(slug, alt):
    m = IMGS[f'clientes/{slug}']
    sq = ' class="sq"' if m['ratio'] < 1.8 else ''
    return (f'<picture><source type="image/webp" srcset="/assets/img/clientes/{slug}.webp">'
            f'<img{sq} src="/assets/img/clientes/{slug}.png" width="{m["w"]}" height="{m["h"]}" alt="{e(alt)}" loading="lazy" decoding="async"></picture>')

def ph(txt):  # selo de placeholder (visível só em modo revisão)
    return f'<span class="ph-flag">{e(txt)}</span>'

def cond(sid, nome, falta):
    return f'\n<!-- CONDICIONAL {sid} {nome}: oculta até chegar {falta} (preencher DADOS em _build/componentes.py). -->\n'

BIM_DISC_OK = {1, 3, 4, 7}  # legendas confirmadas; as demais usam a legenda genérica (copy 13.2)
def bim_cap(n):
    b = BIM[n - 1]; return b['legenda'] if n in BIM_DISC_OK else 'Modelo BIM de instalações prediais'
def bim_alt(n): return BIM[n - 1]['alt']

# ---------------- C01 Header ----------------
def header(ativo=''):
    def mega_col(g, cls):
        lis = ''.join(f'<li><a href="{surl(s[0])}">{ic(s[5])}<span>{e(s[1])}</span></a></li>' for s in grupo(g))
        return f'<div class="{cls}"><h2>{e(g)}</h2><p>{e(GRUPO_LINHA[g])}</p><ul>{lis}</ul></div>'
    cur = lambda k: ' aria-current="page"' if ativo == k else ''
    drawer_grp = ''.join(f'<h3>{e(g)}</h3><ul>' + ''.join(f'<li><a href="{surl(s[0])}">{ic(s[5])}{e(s[1])}</a></li>' for s in grupo(g)) + '</ul>' for g in (G_PRED, G_INFRA, G_EFIC))
    return f'''<header class="c01-header" id="c01" data-componente="C01">
 <div class="container container--wide c01-header__in">
  <a class="c01-logo" href="/" aria-label="Intrépida Engenharia e Projetos, página inicial"><img src="/assets/img/marca/logo-intrepida-azul.svg" width="200" height="46" alt="Intrépida Engenharia e Projetos"></a>
  <nav class="c01-nav" aria-label="Principal"><ul>
   <li class="has-mega{' is-current' if ativo == 'servicos' else ''}"><a class="c01-nav__top" href="/servicos/" aria-expanded="false" aria-controls="mega-servicos"{cur('servicos-hub')}>Serviços {ic('down', 'icon--sm chev')}</a>
    <div class="c01-mega" id="mega-servicos"><div class="container container--wide c01-mega__grid">{mega_col(G_PRED, 'col-1')}{mega_col(G_INFRA, 'col-2')}{mega_col(G_EFIC, 'col-3')}</div>
     <div class="c01-mega__foot"><div class="container container--wide"><a class="link-arrow" href="/servicos/">Ver todos os serviços {ARW}</a><a class="link-arrow" href="/bim-e-compatibilizacao/">BIM e compatibilização {ARW}</a></div></div></div></li>
   <li><a href="/bim-e-compatibilizacao/"{cur('bim')}>BIM</a></li>
   <li><a href="/projetos/"{cur('projetos')}>Projetos</a></li>
   <li><a href="/sobre/"{cur('sobre')}>Sobre</a></li>
   <li><a href="/contato/"{cur('contato')}>Contato</a></li>
  </ul></nav>
  <div class="c01-actions">
   <a class="c01-wa" href="{wa(WA['padrao'])}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp (abre em nova aba)" data-tip="WhatsApp (31) 99649-8629">{ic('whatsapp')}</a>
   <a class="btn btn--sm" href="/contato/">Solicitar orçamento</a>
  </div>
  <button class="c01-burger" type="button" aria-label="Abrir menu" aria-expanded="false" aria-controls="drawer">{ic('menu', 'icon--lg')}</button>
 </div>
</header>
<div class="c01-drawer" id="drawer" aria-hidden="true">
 <div class="c01-drawer__scrim" data-close-drawer></div>
 <div class="c01-drawer__panel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="c01-drawer__head"><img src="/assets/img/marca/logo-intrepida-azul.svg" width="150" height="35" alt="Intrépida Engenharia e Projetos"><button class="c01-drawer__close" type="button" aria-label="Fechar menu" data-close-drawer>{ic('close', 'icon--lg')}</button></div>
  <div class="c01-drawer__body"><nav aria-label="Menu mobile"><ul>
   <li><button class="acc" type="button" aria-expanded="false" aria-controls="dr-serv">Serviços {ic('down', 'chev')}</button>
    <div class="acc-panel" id="dr-serv" hidden>{drawer_grp}<a class="link-arrow" href="/servicos/">Ver todos os serviços {ARW}</a></div></li>
   <li><a href="/bim-e-compatibilizacao/"{cur('bim')}>BIM e compatibilização</a></li>
   <li><a href="/projetos/"{cur('projetos')}>Projetos</a></li>
   <li><a href="/sobre/"{cur('sobre')}>Sobre</a></li>
   <li><a href="/contato/"{cur('contato')}>Contato</a></li>
  </ul></nav>
  <a class="btn btn--block" href="/contato/">Solicitar orçamento</a>
  <div class="c01-drawer__contacts">
   <a href="{wa(WA['padrao'])}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp (abre em nova aba)">{ic('whatsapp')}WhatsApp</a>
   <a href="{TEL_HREF}" aria-label="Ligar para (31) 3070-6568">{ic('phone')}Ligar</a>
   <a href="mailto:{EMAIL}" aria-label="Enviar e-mail para {EMAIL}">{ic('mail')}E-mail</a>
  </div></div>
 </div>
</div>'''

# ---------------- C02 Rodapé ----------------
def footer():
    serv = ''.join(f'<li><a href="{surl(s[0])}">{e(s[1])}</a></li>' for s in SM) + '<li><a href="/bim-e-compatibilizacao/">BIM e compatibilização</a></li>'
    linkedin = (f'<a class="c01-wa" href="{e(DADOS["linkedin_empresa"])}" target="_blank" rel="noopener" aria-label="Intrépida no LinkedIn (abre em nova aba)">{ic("linkedin")}</a>'
                if DADOS['linkedin_empresa'] else cond('C02', 'LinkedIn', 'a URL do LinkedIn'))
    pdf = (f'<a class="btn btn--light btn--sm" href="{e(DADOS["pdf_portfolio"])}" download>{ic("download")}Baixar portfólio (PDF)</a>'
           if DADOS['pdf_portfolio'] else cond('C02', 'Baixar portfólio (PDF)', 'o PDF liberado e atualizado'))
    horario = f'<li>{ic("clock")}<span>{e(DADOS["horario"])}</span></li>' if DADOS['horario'] else cond('C02', 'Horário', 'o horário de atendimento')
    legal = ' · '.join(x for x in [
        f'© <span data-ano>2026</span> ' + e(DADOS['razao_social'] or 'Intrépida Engenharia e Projetos'),
        f'CNPJ {e(DADOS["cnpj"])}' if DADOS['cnpj'] else '', f'CREA {e(DADOS["crea_empresa"])}' if DADOS['crea_empresa'] else ''] if x)
    return f'''<footer class="c02-footer on-dark" id="c02" data-componente="C02">
 <div class="container container--wide">
  <div class="c02-cols">
   <div class="col-marca"><img class="logo" src="/assets/img/marca/logo-intrepida-branco.svg" width="190" height="44" alt="Intrépida Engenharia e Projetos" loading="lazy">
    <p>Projetos de instalações prediais e infraestrutura, em 2D e BIM, para construtoras, incorporadoras e arquitetos.</p>{linkedin}{pdf}</div>
   <details class="c02-acc col-servicos" data-open-desktop><summary><h2>Serviços</h2>{ic('down', 'chev')}</summary><ul>{serv}</ul></details>
   <details class="c02-acc col-inst" data-open-desktop><summary><h2>A Intrépida</h2>{ic('down', 'chev')}</summary><ul>
    <li><a href="/projetos/">Projetos</a></li><li><a href="/projetos/#clientes">Clientes</a></li><li><a href="/sobre/">Sobre</a></li><li><a href="/contato/">Contato</a></li><li><a href="/politica-de-privacidade/">Política de privacidade</a></li></ul></details>
   <div class="col-contato"><h2>Fale com a gente</h2><ul class="c02-contato">
    <li>{ic('whatsapp')}<a href="{wa(WA['padrao'])}" target="_blank" rel="noopener">WhatsApp (31) 99649-8629</a></li>
    <li>{ic('phone')}<a href="{TEL_HREF}">Telefone (31) 3070-6568</a></li>
    <li>{ic('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
    <li>{ic('pin')}<span>{END_1}<br>{END_2}<br>{END_3}</span></li>{horario}
   </ul></div>
  </div>
  <div class="c02-bottom"><p style="margin:0">{legal}</p><nav aria-label="Links legais"><a href="/politica-de-privacidade/">Política de privacidade</a><button type="button" data-cookie-prefs>Preferências de cookies</button></nav></div>
 </div>
</footer>'''

def c19(msg):
    return f'<a class="c19-wa" id="c19" data-componente="C19" href="{wa(msg)}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp (abre em nova aba)">{ic("whatsapp")}<span class="balao" aria-hidden="true">Dúvidas? Fale no WhatsApp</span></a>'

def c20(msg, orc='/contato/'):
    return f'<div class="c20-bar" id="c20" data-componente="C20"><a class="btn" href="{orc}">Solicitar orçamento</a><a class="btn btn--wa" href="{wa(msg)}" target="_blank" rel="noopener" aria-label="Falar no WhatsApp (abre em nova aba)">{ic("whatsapp")}WhatsApp</a></div>'

def c23():
    return f'''<div class="c23-cookies" id="c23" data-componente="C23" role="region" aria-label="Aviso de cookies">
 <p>Usamos cookies para o site funcionar e, com a sua permissão, para medir as visitas e melhorar o conteúdo. Saiba mais na nossa <a href="/politica-de-privacidade/">Política de privacidade</a>.</p>
 <div class="pref"><h2>Preferências de cookies</h2>
  <div class="pref-item"><div><b>Necessários</b>Fazem o site funcionar, como o formulário e a proteção contra spam. Sempre ativos.</div><span class="switch"><input type="checkbox" checked disabled aria-label="Necessários (sempre ativos)"><span></span></span></div>
  <div class="pref-item"><div><b>Medição</b>Contam visitas e cliques de forma agregada (Google Analytics) para sabermos o que funciona no site.</div><span class="switch"><input type="checkbox" id="ck-medicao" aria-label="Medição"><span></span></span></div>
  <button class="btn btn--navy btn--sm" type="button" data-ck="salvar">Salvar preferências</button></div>
 <div class="c23-acoes"><button class="btn btn--navy btn--sm" type="button" data-ck="aceitar">Aceitar todos</button><button class="btn btn--navy btn--sm" type="button" data-ck="recusar">Recusar opcionais</button><button class="c23-config" type="button" data-ck="config">Configurar</button></div>
</div>'''

def lightbox():
    return f'''<div class="lightbox on-dark" role="dialog" aria-modal="true" aria-label="Galeria de imagens" aria-hidden="true">
 <div class="lightbox__bar"><span class="lightbox__count" aria-live="polite"></span><button class="icon-btn" type="button" data-lb-close aria-label="Fechar">{ic('close')}</button></div>
 <div class="lightbox__stage"><figure><img src="data:," alt=""><figcaption></figcaption></figure></div>
 <div class="lightbox__nav"><button class="icon-btn" type="button" data-lb-prev aria-label="Imagem anterior">{ic('arrow-l')}</button><button class="icon-btn" type="button" data-lb-next aria-label="Próxima imagem">{ic('arrow')}</button></div>
</div>'''

# ---------------- C14 Breadcrumb ----------------
def breadcrumb(items):
    """items: [(nome, url|None)] sem o 'Início'."""
    full = [('Início', '/')] + items
    lis = []
    for i, (n, u) in enumerate(full):
        parent = ' class="bc-parent"' if i == len(full) - 2 else ''
        lis.append(f'<li{parent}><span aria-current="page">{e(n)}</span></li>' if i == len(full) - 1 else f'<li{parent}><a href="{u}">{e(n)}</a></li>')
    ld = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, **({'item': DOMINIO + u} if u else {})} for i, (n, u) in enumerate(full)]}
    return f'<nav class="c14-breadcrumb" id="c14" aria-label="Você está em"><div class="container"><ol>{"".join(lis)}</ol></div></nav>', ld

# ---------------- C04 Hero interno ----------------
def hero_interno(sid, eyebrow, h1, sub, btns, img_html='', bc='', wide=False):
    noimg = '' if img_html else ' c04-hero--noimg'
    return f'''<section class="c04-hero{noimg}{' c04-hero--wide' if wide else ''}" id="{sid}" data-componente="C04" data-hero>{bc}
 <div class="container"><div class="c04-hero__grid">
  <div class="c04-hero__txt"><p class="eyebrow">{e(eyebrow)}</p><h1>{e(h1)}</h1><p class="lead">{e(sub)}</p>{btns}</div>
  {f'<div class="c04-hero__img">{img_html}</div>' if img_html else ''}
 </div></div>
</section>'''

def btns(*items, stack=True):
    """items: (texto, href, tipo) tipo ∈ primary|secondary|wa|light|wa-light"""
    out = []
    for t, h, k in items:
        if k.startswith('wa'):
            cls = 'btn btn--wa ' + ('btn--light' if k == 'wa-light' else 'btn--secondary')
            out.append(f'<a class="{cls}" href="{h}" target="_blank" rel="noopener">{ic("whatsapp")}{e(t)}<span class="visually-hidden"> (abre em nova aba)</span></a>')
        else:
            cls = {'primary': 'btn', 'secondary': 'btn btn--secondary', 'light': 'btn btn--light', 'navy': 'btn btn--navy'}[k]
            out.append(f'<a class="{cls}" href="{h}">{e(t)}</a>')
    return f'<div class="btn-row{" btn-row--stack" if stack else ""}">{"".join(out)}</div>'

def fig_bim(n, eager=False, sizes='(min-width: 1025px) 560px, 92vw'):
    return f'<figure class="fig-cota">{picture(f"bim/bim-{n:02d}", bim_alt(n), sizes, eager)}<figcaption><span>{e(bim_cap(n))}</span><span>Modelo BIM · Intrépida</span></figcaption></figure>'

def fig_ia(key, alt, eager=False, sizes='(min-width: 1025px) 560px, 92vw'):
    return f'<figure class="fig-cota">{picture(f"ilustracoes/{key}", alt, sizes, eager)}<figcaption><span class="tag-ia">Imagem ilustrativa</span><span>Gerada por IA · não é projeto da Intrépida</span></figcaption></figure>'

def fig_foto(key, alt, cap=None, eager=False, sizes='(min-width: 1025px) 560px, 92vw'):
    return f'<figure class="fig-photo">{picture(key, alt, sizes, eager)}{f"<figcaption>{e(cap)}</figcaption>" if cap else ""}</figure>'

# ---------------- C05 Números ----------------
NUMEROS = [('24', 'clientes atendidos, entre construtoras e incorporadoras'), ('18', 'empreendimentos no portfólio'),
           ('6', 'estados: MG, DF, SP, RJ, MS e SC'), ('+5.800', 'unidades nos empreendimentos do portfólio')]
def numeros(sid, light=False, h2=None):
    lis = ''.join(f'<li><strong>{n}</strong> <span class="lbl">{e(l)}</span></li>' for n, l in NUMEROS)
    head = f'<h2 class="visually-hidden">Números do portfólio</h2>' if not h2 else ''
    return f'<section class="c05-numeros{" c05-numeros--light" if light else ""}" id="{sid}" data-componente="C05" aria-label="Números do portfólio">{head}<div class="container"><ul>{lis}</ul></div></section>'

# ---------------- C06 Logos ----------------
def logos(sid, h2, sub=None, link=('Ver todos os clientes e projetos →', '/projetos/#clientes'), todos=False, bg='', h2_id=None):
    slugs = LOGO_SLUGS if todos else LOGOS_12
    nome = dict(zip(LOGO_SLUGS, CLIENTES))
    def item(s):
        marca = f'<span class="logo-txt">{e(nome[s])}</span>' if s in LOGO_TEXTO else logo_img(s, nome[s])
        return f'<li>{marca}{f"<span class=cap>{e(nome[s])}</span>" if todos and s not in LOGO_TEXTO else ""}</li>'
    lis = ''.join(item(s) for s in slugs)
    sub_html = f'<p class="lead">{e(sub)}</p>' if sub else ''
    lk = f'<p class="c06-logos__foot"><a class="link-arrow" href="{link[1]}">{e(link[0].replace(" →", ""))} {ARW}</a></p>' if link else ''
    return f'''<section class="sec c06-logos {bg}" id="{sid}" data-componente="C06"><div class="container">
 <div class="sec-head"><h2>{e(h2)}</h2>{sub_html}</div><ul class="reveal">{lis}</ul>{lk}</div></section>'''

# ---------------- C07 Serviços (Home) ----------------
def servicos_grupos(sid='h-05'):
    def li(s):
        return (f'<li><a href="{surl(s[0])}" aria-label="{e(s[1])}: saiba mais sobre o {e(s[2][0].lower() + s[2][1:])}"><span class="ico">{ic(s[5])}</span>'
                f'<span><strong>{e(s[1])}</strong><span class="d">{e(s[6])}</span></span>{ARW}</a></li>')
    g1 = ''.join(li(s) for s in grupo(G_PRED)); g2 = ''.join(li(s) for s in grupo(G_INFRA)); g3 = ''.join(li(s) for s in grupo(G_EFIC))
    return f'''<section class="sec bg-light bg-grid" id="{sid}" data-componente="C07"><div class="container">
 <div class="sec-head sec-head--row"><div><p class="eyebrow">Serviços</p><h2>O que projetamos</h2><p class="lead">Nove disciplinas de instalações e infraestrutura com um só fornecedor, compatibilizadas entre si.</p></div>
  <a class="link-arrow" href="/servicos/">Ver todos os serviços {ARW}</a></div>
 <div class="c07-grupos reveal">
  <div class="c07-grupo grp-1"><h3>Instalações prediais</h3><p>{e(GRUPO_LINHA[G_PRED])}</p><ul class="c07-list">{g1}</ul></div>
  <div class="c07-grupo c07-grupo--destaque grp-2"><h3>Infraestrutura urbana</h3><p><span class="selo">Redes de água, esgoto e drenagem</span></p><ul class="c07-list">{g2}</ul></div>
  <div class="c07-grupo grp-3"><h3>Eficiência e sustentabilidade</h3><p>{e(GRUPO_LINHA[G_EFIC])}</p><ul class="c07-list">{g3}</ul></div>
 </div>
 <a class="faixa-bim" href="/bim-e-compatibilizacao/">{ic('bim', 'icon--lg')}<span>BIM e compatibilização em todas as disciplinas</span>{ARW}</a>
</div></section>'''

def card_servico(s, h='h3', desc=None):
    return (f'<a class="c07-card" href="{surl(s[0])}" aria-label="{e(s[7])}: saiba mais sobre o {e(s[2][0].lower() + s[2][1:])}"><span class="ico">{ic(s[5], "icon--lg")}</span>'
            f'<{h}>{e(s[7])}</{h}><p>{e(desc or s[8])}</p><span class="link-arrow" aria-hidden="true">Saiba mais {ARW}</span></a>')

# ---------------- C08 Projetos ----------------
def proj_by_name(n): return next(p for p in PROJ if p['nome'] == n)
def card_projeto(p, eager=False):
    loc = f'{p["cidade"]}/{p["uf"]}'
    if p['foto']:
        media = picture(f'projetos/{p["slug"]}', p['alt'], '(min-width: 1025px) 380px, (min-width: 768px) 46vw, 92vw', eager, max_default=800)
    else:
        media = f'<div class="semfoto" aria-hidden="true"><img class="simb" src="/assets/img/marca/logo-intrepida-simbolo.svg" alt="" width="26" height="41"><span class="nm">{e(p["nome"])}</span><span class="lc">{e(p["cliente"])} · {e(loc)}</span></div>'
    aria = f'{p["nome"]}, {p["cliente"]}, {loc}, {p["unidades"]} unidades. Ver projeto'
    disc = DADOS['disciplinas_por_projeto'].get(p['slug'])
    tags = (f'<p class="tags">' + ' '.join(f'<span class="selo">{e(d)}</span>' for d in disc) + '</p>') if disc else ''
    return (f'<li data-uf="{p["uf"]}" data-cliente="{e(p["cliente"])}"><article class="c08-card"><div class="c08-card__media">{media}<span class="c08-card__uf">{p["uf"]}</span></div>'
            f'<div class="c08-card__body"><h3><a href="/projetos/{p["slug"]}/" aria-label="{e(aria)}">{e(p["nome"])}</a></h3>'
            f'<p class="c08-card__line">{e(p["cliente"])} · {e(loc)}</p>{tags}<p class="c08-card__units"><span><b>{p["unidades"]}</b> unidades</span>{ARW}</p></div></article></li>')

# ---------------- C10 Processo ----------------
ETAPAS = [('Briefing e análise', 'Você envia a arquitetura e as informações do empreendimento. Avaliamos escopo, disciplinas e exigências locais.'),
          ('Proposta', 'Você recebe escopo, prazo e valor por disciplina, para comparar e aprovar.'),
          ('Cálculo e modelagem', 'Dimensionamos os sistemas e modelamos as instalações em BIM ou desenhamos em 2D.'),
          ('Compatibilização e aprovação', 'Cruzamos as disciplinas com a arquitetura e a estrutura e preparamos o projeto para a análise das concessionárias.'),
          ('Entrega', 'Você recebe pranchas, memoriais e modelo, prontos para a obra.')]
def processo(sid, h2='Como trabalhamos', etapas=ETAPAS, bg='', nota=True):
    lis = ''.join(f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>' for t, d in etapas)
    n = (f'<p class="nota">Resposta ao pedido de orçamento em até {DADOS["prazo_resposta_dias"]} dias úteis.</p>' if DADOS['prazo_resposta_dias']
         else cond(sid, 'nota de prazo', 'o prazo de resposta')) if nota else ''
    return f'<section class="sec c10-processo {bg}" id="{sid}" data-componente="C10"><div class="container"><div class="sec-head"><h2>{e(h2)}</h2></div><ol class="reveal">{lis}</ol>{n}</div></section>'

# ---------------- C11 Galeria ----------------
def bim_full(n):
    """Maior versão JPEG disponível da imagem BIM n (algumas não chegam a 1800 px)."""
    ws = sorted(int(m.group(1)) for f in (B.parent / 'assets' / 'img' / 'bim').glob(f'bim-{n:02d}-*.jpg') if (m := re.search(r'-(\d+)\.jpg$', f.name)))
    return f'/assets/img/bim/bim-{n:02d}-{ws[-1]}.jpg' if ws else ''

def galeria(nums, grupo_lb, scroll=False, big=False):
    lid = f'gal-{grupo_lb}'
    lis = ''.join(
        f'<li><button type="button" data-lb="{grupo_lb}" data-full="{bim_full(n)}" data-alt="{e(bim_alt(n))}" data-cap="{e(bim_cap(n))}" aria-label="Ampliar: {e(bim_cap(n))}">'
        f'{picture(f"bim/bim-{n:02d}", bim_alt(n), "(min-width: 1025px) 280px, 45vw", max_default=480)}<span class="cap">{e(bim_cap(n))}</span></button></li>' for n in nums)
    cls = 'c11-galeria' + (' c11-galeria--scroll' if scroll else '') + (' c11-galeria--8' if big else '')
    dots = f'<div class="dots" data-dots="{lid}" aria-hidden="true"></div>' if scroll else ''
    return f'<ul class="{cls}" id="{lid}" data-componente="C11">{lis}</ul>{dots}'

# ---------------- C12 FAQ ----------------
def faq(sid, h2, items, bg=''):
    """items: [(pergunta, resposta_html)]"""
    det = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}<span class="pm" aria-hidden="true">{ic("plus", "icon--sm")}</span></summary><div class="ans"><p>{a}</p></div></details>' for i, (q, a) in enumerate(items))
    ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': html.unescape(__import__('re').sub('<[^>]+>', '', a))}} for q, a in items]}
    return f'<section class="sec {bg}" id="{sid}" data-componente="C12"><div class="container"><div class="sec-head"><h2>{e(h2)}</h2></div><div class="c12-faq">{det}</div></div></section>', ld

# ---------------- C13 CTA final ----------------
def cta_botoes(sid, h2, txt, wa_msg, orc='/contato/', extra=''):
    return f'''<section class="sec c13-cta bg-texture on-dark" id="{sid}" data-componente="C13"><div class="container"><div class="c13-cta__box c13-cta__box--botoes">
 <div><h2 style="color:#fff">{e(h2)}</h2><p class="lead">{e(txt)}</p>{extra}</div>
 {btns(('Solicitar orçamento', orc, 'primary'), ('Falar no WhatsApp', wa(wa_msg), 'wa-light'))}
</div></div></section>'''

PASSOS = ['Analisamos as informações e os arquivos que você enviar.', 'Entramos em contato para alinhar escopo e disciplinas.', 'Você recebe a proposta com escopo, prazo e valor.']
def passos_lista(itens=PASSOS):
    its = list(itens)
    if DADOS['prazo_resposta_dias']:
        its[1] = f'Entramos em contato em até {DADOS["prazo_resposta_dias"]} dias úteis para alinhar escopo e disciplinas.'
    return '<ol class="passos">' + ''.join(f'<li>{e(x)}</li>' for x in its) + '</ol>'

def cta_form(sid, h2, wa_msg, servico=''):
    pdf = (f'<a class="btn btn--light" href="{e(DADOS["pdf_portfolio"])}" download>{ic("download")}Baixar portfólio (PDF)</a>' if DADOS['pdf_portfolio']
           else cond(sid, 'Baixar portfólio (PDF)', 'o PDF liberado'))
    return f'''<section class="sec c13-cta c13-cta--form bg-texture on-dark" id="{sid}" data-componente="C13+C21b"><div class="container"><div class="c13-cta__box">
 <div class="c13-cta__txt"><h2 style="color:#fff">{e(h2)}</h2>{passos_lista()}
  <p><a class="link-arrow" href="{wa(wa_msg)}" target="_blank" rel="noopener">{ic('whatsapp')}Prefere WhatsApp? Fale com a gente agora<span class="visually-hidden"> (abre em nova aba)</span></a></p>{pdf}</div>
 <div class="c13-cta__form">{form_curto(servico)}</div>
</div></div></section>'''

# ---------------- C21b Formulário curto ----------------
FALHA_ENVIO = ('<div class="alert alert--error form-fail" role="alert" tabindex="-1" hidden>Não conseguimos enviar o seu pedido agora. Seus dados continuam preenchidos. '
               f'Tente de novo em alguns instantes ou fale pelo <a href="{wa(WA["contato"])}" target="_blank" rel="noopener">WhatsApp (31) 99649-8629<span class="visually-hidden"> (abre em nova aba)</span></a>.</div>')
def f_err(): return '<p class="err"><span></span></p>'  # sem role=alert: o resumo da etapa é que anuncia (UX-07)
def form_curto(servico=''):
    pid = 'fc'
    return f'''<form class="form-card form" data-form="orcamento_rapido" action="/obrigado/" method="post" data-componente="C21b" aria-label="Pedido de orçamento rápido">
 <div class="err-summary" tabindex="-1"><h3></h3><ul></ul></div>
 <div class="cols-2">
  <div class="field"><label for="{pid}-nome">Nome</label><input class="input" id="{pid}-nome" name="nome" autocomplete="name" data-req="Informe seu nome.">{f_err()}</div>
  <div class="field"><label for="{pid}-email">E-mail</label><input class="input" id="{pid}-email" name="email" type="email" autocomplete="email" placeholder="nome@empresa.com.br" data-req="Informe seu e-mail." data-fmt="Digite um e-mail válido, como nome@empresa.com.br.">{f_err()}</div>
 </div>
 <div class="cols-2">
  <div class="field"><label for="{pid}-tel">WhatsApp ou telefone</label><input class="input" id="{pid}-tel" name="telefone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(31) 90000-0000" data-req="Informe um telefone para contato." data-fmt="Digite o número com DDD, como (31) 90000-0000.">{f_err()}</div>
  <div class="field"><label for="{pid}-emp">Empresa (opcional)</label><input class="input" id="{pid}-emp" name="empresa" autocomplete="organization"></div>
 </div>
 <div class="field"><label for="{pid}-local">Cidade/UF do empreendimento (opcional)</label><input class="input" id="{pid}-local" name="local" placeholder="Ex.: Belo Horizonte/MG"></div>
 <div class="field"><label for="{pid}-msg">Mensagem (opcional)</label><textarea class="textarea" id="{pid}-msg" name="mensagem" placeholder="Conte o tipo de empreendimento, o número de unidades e os projetos de que você precisa."></textarea></div>
 <div class="field"><label class="check"><input type="checkbox" id="{pid}-lgpd" name="lgpd" data-req="Para enviar, marque que concorda com a Política de privacidade."><span>Concordo com o uso dos meus dados para receber o orçamento, conforme a <a href="/politica-de-privacidade/" target="_blank" rel="noopener">Política de privacidade<span class="visually-hidden"> (abre em nova aba)</span></a>.</span></label>{f_err()}</div>
 <input type="hidden" name="servico" value="{e(servico)}"><input type="hidden" name="origem" value=""><input type="hidden" name="form_label" value="orcamento_rapido">
 <div class="hp" aria-hidden="true"><label>Não preencha<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
 {FALHA_ENVIO}
 <button class="btn btn--block" type="submit">Solicitar orçamento</button>
 <p class="below-btn">Tem arquivos? Depois do envio, mande pelo WhatsApp ou use o formulário completo.</p>
</form>'''

# ---------------- C15 Ficha ----------------
def ficha(rows):
    return '<dl class="c15-ficha" data-componente="C15">' + ''.join(f'<div><dt>{e(k)}</dt><dd>{v}</dd></div>' for k, v in rows if v) + '</dl>'

# ---------------- C17 Responsável técnico ----------------
def rt_foto(full=False):
    if DADOS['foto_rt']:
        return f'<div class="c17-rt__foto">{picture(DADOS["foto_rt"], "Carlos Alberto Grope, diretor técnico da Intrépida Engenharia e Projetos", "200px")}</div>'
    return f'<div class="c17-rt__foto" data-placeholder="foto-rt">{ph("FOTO CARLOS")}<img src="/assets/img/marca/logo-intrepida-simbolo.svg" alt="" width="48" height="76"></div>'

# ---------------- Mapa de UFs (C24) ----------------
TILES = [  # cartograma: (UF, coluna, linha) — posição aproximada no território
 ('RR', 3, 0), ('AP', 5, 0), ('AM', 2, 1), ('PA', 4, 1), ('MA', 5, 1), ('CE', 6, 1), ('AC', 0, 2), ('RO', 1, 2), ('TO', 4, 2), ('PI', 5, 2), ('RN', 6, 2),
 ('MT', 2, 3), ('GO', 3, 3), ('DF', 4, 3), ('BA', 5, 3), ('PB', 6, 3), ('MS', 2, 4), ('MG', 4, 4), ('SE', 5, 4), ('PE', 6, 4),
 ('SP', 3, 5), ('RJ', 4, 5), ('ES', 5, 5), ('AL', 6, 5), ('PR', 3, 6), ('SC', 3, 7), ('RS', 2, 8)]
UF_NOME = {'MG': 'Minas Gerais', 'DF': 'Distrito Federal', 'SP': 'São Paulo', 'RJ': 'Rio de Janeiro', 'MS': 'Mato Grosso do Sul', 'SC': 'Santa Catarina'}
def mapa_ufs(interativo):
    cont = {}
    for p in PROJ: cont[p['uf']] = cont.get(p['uf'], 0) + 1
    cells = {}
    for uf, c, r in TILES: cells[(c, r)] = uf
    out = []
    for r in range(9):
        for c in range(7):
            uf = cells.get((c, r))
            if not uf: out.append('<span class="uf vz"></span>'); continue
            if uf in cont:
                t = f'{UF_NOME[uf]}: {cont[uf]} projeto{"s" if cont[uf] > 1 else ""}'
                out.append(f'<button type="button" class="uf on" data-n="{cont[uf]}" data-uf-go="{uf}" aria-label="{uf}, {e(t)}. Filtrar projetos">{uf}</button>' if interativo
                           else f'<span class="uf on" data-n="{cont[uf]}" title="{e(t)}">{uf}</span>')
            else: out.append(f'<span class="uf" aria-hidden="true">{uf}</span>')
    ordem = ['MG', 'DF', 'SP', 'RJ', 'MS', 'SC']
    def li_uf(u):
        go = f' data-uf-go="{u}"' if interativo else ''
        return f'<li><a href="/projetos/?uf={u.lower()}"{go}>{UF_NOME[u]}</a><span>{cont[u]} projeto{"s" if cont[u] > 1 else ""}</span></li>'
    lista = ''.join(li_uf(u) for u in ordem)
    grid = f'<div class="uf-grid" role="group" aria-label="Mapa do Brasil com os seis estados onde a Intrépida tem projetos: MG, DF, SP, RJ, MS e SC">{"".join(out)}</div>'
    return grid, f'<ul class="uf-lista">{lista}</ul>'

# ---------------- Documento ----------------
def org_ld():
    return {'@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': DOMINIO + '/#empresa', 'name': 'Intrépida Engenharia e Projetos',
            'url': DOMINIO + '/', 'logo': DOMINIO + '/assets/img/marca/logo-intrepida-azul.svg', 'image': DOMINIO + '/assets/img/marca/og-image.jpg',
            'telephone': '+55 31 3070-6568', 'email': EMAIL,
            'address': {'@type': 'PostalAddress', 'streetAddress': 'Rua dos Goitacazes, 103, salas 1604 e 1606', 'addressLocality': 'Belo Horizonte',
                        'addressRegion': 'MG', 'postalCode': '30190-910', 'addressCountry': 'BR'},
            'areaServed': ['MG', 'DF', 'SP', 'RJ', 'MS', 'SC'],
            'contactPoint': {'@type': 'ContactPoint', 'telephone': '+55 31 99649-8629', 'contactType': 'sales', 'availableLanguage': 'pt-BR'}}

def documento(path, title, meta, body, ativo='', wa_msg=WA['padrao'], noindex=False, lds=(), sem_c19=False, sem_c20=False, og_img=None, orc='/contato/'):
    canonical = DOMINIO + path
    ld = [org_ld()] + [x for x in lds if x]
    ldh = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    og = DOMINIO + (og_img or '/assets/img/marca/og-image.jpg')
    robots = '<meta name="robots" content="noindex, nofollow">' if noindex else '<meta name="robots" content="index, follow">'
    desc = f'<meta name="description" content="{e(meta)}"><meta property="og:description" content="{e(meta)}">' if meta else ''
    return f'''<!doctype html>
<html lang="pt-BR" class="no-js{' modo-revisao' if REVISAO else ''}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
{desc}
{robots}
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Intrépida Engenharia e Projetos">
<meta property="og:title" content="{e(title)}"><meta property="og:url" content="{canonical}"><meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B3859">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500;600&amp;family=Montserrat:wght@600;700;800&amp;display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
{ldh}
</head>
<body class="{'has-c20' if not sem_c20 else ''}">
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
{header(ativo)}
<main id="conteudo" tabindex="-1">
{body}
</main>
{footer()}
{'' if sem_c19 else c19(wa_msg)}
{'' if sem_c20 else c20(wa_msg, orc)}
{c23()}
{lightbox() if 'data-lb=' in body else ''}
<div id="live-region" class="visually-hidden" aria-live="polite"></div>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''

def escrever(path, conteudo):
    p = SITE / path.strip('/') / 'index.html' if not path.endswith('.html') else SITE / path.strip('/')
    p.parent.mkdir(parents=True, exist_ok=True); p.write_text(conteudo)
    return p
