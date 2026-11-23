"""Gera todas as páginas do site em site/ a partir de data/*.json + componentes.py.
Uso: python3 _build/build.py   (rodar extrai_servicos.py / extrai_dados.py antes se o copy mudar)
Textos: equipe/03-copy.md (aprovado). Estrutura: IDs de seção do wireframe (H-02, SV-03…)."""
import json, re
from componentes import *

PAGINAS = []
def pub(path, html_):
    escrever(path, html_); PAGINAS.append(path)

def sec(sid, comp, inner, cls='sec', extra=''):
    return f'<section class="{cls}" id="{sid}" data-componente="{comp}"{extra}><div class="container">{inner}</div></section>'

# =====================================================================
# HOME
# =====================================================================
def home():
    mir = proj_by_name('Mirante São Lucas')
    hero = f'''<section class="c03-hero on-dark" id="h-02" data-componente="C03" data-hero>
 <div class="c03-hero__media">{picture('projetos/mirante-sao-lucas', 'Vista aérea do Mirante São Lucas, torre residencial da UNENCO em Belo Horizonte/MG', '100vw', eager=True, max_default=1600)}</div>
 <div class="container c03-hero__in"><div class="c03-hero__txt">
  <p class="eyebrow">Engenharia de projetos · Belo Horizonte/MG</p>
  <h1>Projetos de instalações e infraestrutura para incorporadoras e construtoras</h1>
  <p class="lead">Hidrossanitário, elétrica, gás e mais seis disciplinas, em 2D ou BIM, compatibilizadas para reduzir retrabalho e pensadas para aprovar nas concessionárias.</p>
  {btns(('Solicitar orçamento', '/contato/', 'primary'), ('Falar no WhatsApp', wa(WA['home']), 'wa-light'))}
  <p class="c03-hero__proof"><span>{ic('check')}+24 construtoras e incorporadoras atendidas</span><span class="sep" aria-hidden="true">·</span><span>{ic('pin')}Presença em 8 estados</span></p>
 </div></div>
 <p class="c03-hero__credit">Mirante São Lucas · UNENCO · Belo Horizonte/MG</p>
</section>'''
    selos = (f'<p class="eyebrow" style="margin-top:1.5rem">Projetos aprovados em:</p><p>' + ' '.join(f'<span class="selo">{e(c)}</span>' for c in DADOS['concessionarias']) + '</p>'
             if DADOS['concessionarias'] else cond('H-06', 'selos das concessionárias', 'a lista de concessionárias em que já aprovaram'))
    h06 = f'''<section class="sec c18-faixa bg-navy on-dark" id="h-06" data-componente="C18"><div class="container"><div class="split split--img-first-m">
 <div class="reveal"><p class="eyebrow">Aprovação em concessionárias</p><h2>A aprovação na concessionária está travando o seu cronograma?</h2>
  <p class="lead">Projeto que chega à concessionária fora do padrão volta com exigências, e cada reanálise empurra a obra. Com o projetista calculista desde o estudo de viabilidade, as normas e as exigências das concessionárias de energia, água, gás e telecomunicações entram no projeto desde a primeira versão.</p>
  <ul class="checklist">{''.join(f'<li>{ic("check")}<span>{x}</span></li>' for x in ['Normas técnicas e padrões da concessionária considerados desde o início', 'Projeto preparado para reduzir exigências e reanálises', 'Cronograma de aprovação mais previsível para a obra'])}</ul>
  {selos}{btns(('Enviar meu projeto para análise', '/contato/', 'primary'))}</div>
 <div class="reveal">{fig_foto('projetos/bosque-dos-ipes', 'Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS', 'Bosque dos Ipês · RNI · Campo Grande/MS')}</div>
</div></div></section>'''
    h07 = f'''<section class="sec" id="h-07" data-componente="C09+C11"><div class="container"><div class="split split--40-60">
 <div class="reveal"><p class="eyebrow">BIM e compatibilização</p><h2>BIM para achar o conflito no modelo, e não na obra</h2>
  <p>Modelamos as instalações em 3D e cruzamos todas as disciplinas antes de liberar o projeto. Tubulação que bate em viga, shaft sem espaço, quadro no lugar errado: o problema aparece na tela, quando corrigir ainda custa pouco.</p>
  <ul class="checklist">{''.join(f'<li>{ic("check")}<span>{x}</span></li>' for x in ['Interferências entre disciplinas resolvidas antes da obra', 'Quantitativos de materiais extraídos do modelo', 'Informação útil para execução, manutenção e gestão do empreendimento', 'Entrega em 2D quando o seu processo pedir'])}</ul>
  <a class="link-arrow" href="/bim-e-compatibilizacao/">Conheça nosso processo BIM {ARW}</a></div>
 <div class="reveal">{galeria([1, 7, 5, 8], 'home', scroll=True)}</div>
</div></div></section>'''
    destaques = ['Mirante São Lucas', 'Bosque dos Ipês', 'Residencial Pacífico', 'Parque Lagoa dos Príncipes e Lagoa Nova', 'Residencial Alta Vista', 'Residencial Monte Carlo']
    h08 = f'''<section class="sec bg-light" id="h-08" data-componente="C08"><div class="container">
 <div class="sec-head sec-head--row"><div><p class="eyebrow">Portfólio</p><h2>Empreendimentos com projetos da Intrépida</h2></div><a class="link-arrow only-desktop" href="/projetos/">Ver todos os projetos {ARW}</a></div>
 <ul class="c08-grid c08-grid--home">{''.join(card_projeto(proj_by_name(n)) for n in destaques)}</ul>
 <p class="only-mobile" style="margin-top:1.5rem"><a class="btn btn--secondary btn--block" href="/projetos/">Ver todos os 18 projetos</a></p>
</div></section>'''
    crea = f'<p>CREA-MG {e(DADOS["crea_rt"])}</p>' if DADOS['crea_rt'] else cond('H-10', 'CREA do RT', 'o nº do CREA')
    h10 = f'''<section class="sec" id="h-10" data-componente="C17"><div class="container"><div class="c17-rt reveal">
 {rt_foto()}
 <div><h2>Quem responde pelos seus projetos</h2><p class="c17-rt__nome">Carlos Alberto Grope</p><p class="c17-rt__cargo">Diretor técnico · Engenheiro civil sanitarista</p>{crea}
  <p style="max-width:62ch">Os projetos da Intrépida são conduzidos pelo engenheiro civil sanitarista Carlos Alberto Grope, diretor técnico da empresa. No orçamento e durante o projeto, você fala com quem entende do cálculo.</p>
  <a class="link-arrow" href="/sobre/">Conheça a Intrépida {ARW}</a></div>
</div></div></section>'''
    h11 = depoimentos('h-11', 'O que dizem os clientes')
    faqs = [
        ('Vocês atendem empreendimentos de grande porte?', 'Sim. O maior empreendimento do nosso portfólio tem 1.800 unidades: o Residencial Monte Carlo, da Habit Construtora, em Cabo Frio/RJ. Os demais vão de 142 a 368 unidades, para construtoras e incorporadoras como MRV, Direcional, RNI e Precon.'),
        ('Vocês atendem a minha cidade?', 'Já atendemos oito estados: MG, DF, SP, RJ, MS, SC, RS e PB. Para outras localidades, envie o pedido de orçamento com a cidade do empreendimento e confirmamos o atendimento.'),
        ('Qual é o prazo de um projeto?', 'Depende do porte, das disciplinas contratadas e da fase em que a arquitetura está. Por isso o prazo de cada etapa vem descrito na proposta, antes de você contratar.'),
        ('Vocês trabalham no padrão BIM da minha empresa?', 'Entregamos em BIM (modelo 3D) ou em 2D. Se a sua empresa tem template, padrão de nomenclatura ou formato próprio, envie junto com o pedido de orçamento: a compatibilidade fica definida na proposta.'),
        ('O que preciso enviar para receber o orçamento?', 'O projeto de arquitetura (DWG, PDF ou RVT), a implantação, o número de unidades ou a área construída, a cidade e as disciplinas de que você precisa. Ainda não tem tudo? Envie o que tiver e completamos juntos.'),
        ('A Intrépida executa a obra?', 'Não. A Intrépida faz projetos de engenharia: instalações prediais e infraestrutura. A execução fica com a sua construtora, que recebe um projeto completo e compatibilizado.')]
    h12, ld12 = faq('h-12', 'Dúvidas de quem contrata projetos', faqs, 'bg-light')
    body = (hero + numeros('h-03') + logos('h-04', 'Quem já contratou nossos projetos', '+24 construtoras e incorporadoras atendidas. Algumas delas:') + servicos_grupos('h-05')
            + h06 + h07 + h08 + processo('h-09', bg='bg-blue-50 bg-grid') + h10 + h11 + h12
            + cta_form('h-13', 'Conte sobre o seu empreendimento e receba uma proposta', WA['home']))
    pub('/', documento('/', 'Projetos de instalações prediais e BIM em BH | Intrépida',
        'Projetos hidrossanitários, elétricos, de gás e de infraestrutura, em 2D e BIM, para incorporadoras. +24 clientes em 8 estados. Solicite orçamento.',
        body, wa_msg=WA['padrao'], lds=[ld12, {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'Intrépida Engenharia e Projetos', 'url': DOMINIO + '/'}]))

def depoimentos(sid, h2):
    if not DADOS['depoimentos']:
        return cond(sid, 'Depoimentos (C16)', 'depoimentos reais autorizados (nome, cargo, empresa)')
    cards = ''.join(f'<figure class="c07-card"><blockquote><p>“{e(d["citacao"])}”</p></blockquote><figcaption><b>{e(d["nome"])}</b><br>{e(d["cargo"])} · {e(d["empresa"])}</figcaption></figure>' for d in DADOS['depoimentos'])
    return sec(sid, 'C16', f'<div class="sec-head"><h2>{e(h2)}</h2></div><div class="grid grid--3">{cards}</div>')

# =====================================================================
# SERVIÇOS — HUB
# =====================================================================
def hub():
    bc, ldbc = breadcrumb([('Serviços', None)])
    hero = hero_interno('sh-02', 'Serviços', 'Projetos de instalações prediais e infraestrutura em Belo Horizonte',
        'Nove disciplinas em 2D e BIM para incorporadoras, construtoras e arquitetos, com atuação em oito estados.',
        btns(('Solicitar orçamento', '/contato/', 'primary'), ('Falar no WhatsApp', wa(WA['hub']), 'wa')), fig_bim(5, eager=True), bc=bc, wide=True)
    chips = f'''<nav class="sec--tight" id="sh-03" aria-label="Ir para o grupo de serviços" style="padding-block:0 1rem"><div class="container"><div class="chips">
 <a class="chip" href="#sh-04">{ic('building', 'icon--sm')}Instalações prediais</a><a class="chip" href="#sh-05">{ic('saneamento', 'icon--sm')}Infraestrutura urbana</a><a class="chip" href="#sh-06">{ic('reuso', 'icon--sm')}Eficiência e sustentabilidade</a></div></div></nav>'''
    g1 = ''.join(card_servico(s) for s in grupo(G_PRED))
    sh04 = sec('sh-04', 'C07', f'<div class="sec-head"><h2>Instalações prediais</h2><p class="lead">Os sistemas que fazem o edifício funcionar, do subsolo à cobertura.</p></div><div class="grid grid--3 reveal">{g1}</div>', 'sec sec--flush-top')
    san = SMAP['infraestrutura-de-saneamento']
    sh05 = sec('sh-05', 'C07', f'''<div class="sec-head"><h2>Infraestrutura urbana</h2><p class="lead">Redes que ligam o empreendimento ao sistema público.</p></div>
 <a class="c07-card c07-card--wide reveal" href="{surl(san[0])}">{fig_foto('projetos/bosque-dos-ipes', 'Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS', None, sizes='(min-width: 1025px) 600px, 92vw')}
  <span class="txt"><span class="ico">{ic('saneamento', 'icon--lg')}</span><h3>Infraestrutura de saneamento</h3><p>{e(san[8])}</p><span class="link-arrow">Conheça o projeto de infraestrutura {ARW}</span></span></a>''', 'sec bg-light')
    g3 = ''.join(card_servico(s) for s in grupo(G_EFIC))
    sh06 = sec('sh-06', 'C07', f'<div class="sec-head"><h2>Eficiência e sustentabilidade</h2><p class="lead">Menos água potável e menos energia gastas pelo empreendimento.</p></div><div class="grid grid--2 reveal">{g3}</div>')
    sh07 = f'''<section class="sec c18-faixa bg-navy on-dark" id="sh-07" data-componente="C18"><div class="container"><div class="split">
 <div><p class="eyebrow">BIM</p><h2>Todas as disciplinas em BIM, compatibilizadas</h2><p class="lead">Cada sistema é modelado em 3D e cruzado com a arquitetura, a estrutura e as demais instalações. Os conflitos são resolvidos no modelo, antes de chegar à obra.</p>
  <a class="link-arrow" href="/bim-e-compatibilizacao/">Conheça nosso processo BIM {ARW}</a></div>
 <div>{fig_bim(4)}</div></div></div></section>'''
    sh08 = sec('sh-08', 'C09', f'''<div class="split split--top"><div><h2>Não sabe quais projetos o seu empreendimento precisa?</h2></div>
 <div><p class="lead">Normal. A lista muda com o tipo de empreendimento, a cidade e as exigências de cada concessionária. Envie o projeto de arquitetura e indicamos as disciplinas necessárias e a melhor fase para contratar cada uma.</p>
  <ul class="checklist"><li>{ic('check')}<span>Arquiteto: um parceiro para os complementares, compatibilizados com o seu projeto.</span></li><li>{ic('check')}<span>Dono de obra: orientação em linguagem clara, antes de gastar com a disciplina errada.</span></li></ul>
  {btns(('Enviar a arquitetura para indicação das disciplinas', '/contato/?servico=nao-sei', 'navy'))}</div></div>''')
    body = (hero + chips + sh04 + sh05 + sh06 + sh07 + sh08 + processo('sh-09', bg='bg-blue-50 bg-grid')
            + logos('sh-10', 'Quem já contratou nossos projetos')
            + cta_botoes('sh-11', 'Vamos orçar os projetos do seu empreendimento?', 'Conte o que você precisa. Se ainda não souber todas as disciplinas, a gente ajuda a definir.', WA['hub']))
    pub('/servicos/', documento('/servicos/', 'Projetos de instalações prediais em BH | Intrépida',
        'Hidrossanitário, elétrica, gás, HVAC, pressurização, piscina, saneamento, reúso pluvial e aquecimento solar, em 2D e BIM. Veja e solicite orçamento.',
        body, ativo='servicos', wa_msg=WA['hub'], lds=[ldbc]))

# =====================================================================
# SERVIÇO INDIVIDUAL (modelo único para as 9)
# =====================================================================
IA_SERV = {'climatizacao-hvac': 'ia-hvac', 'pressurizacao-de-escadas': 'ia-pressurizacao', 'projeto-de-piscina': 'ia-piscina',
           'reuso-de-agua-pluvial': 'ia-reuso-pluvial', 'aquecimento-solar': 'ia-aquecimento-solar'}
SV06_IMG = {'projeto-hidrossanitario': [4], 'projeto-eletrico': [5], 'projeto-de-gas': [6], 'aquecimento-solar': [3]}
def outros_de(d):
    raw = d['outros_raw']
    if d['slug'] == 'infraestrutura-de-saneamento': labels = ['Reúso de água pluvial', 'Aquecimento solar', 'Hidrossanitário']
    else: labels = [x.strip() for x in re.split(r'·|\+', raw)]
    return [BY_LABEL[l] for l in labels]

def servico(d):
    s = SMAP[d['slug']]; nome = s[2]; wmsg = wa_servico(nome); orc = f'/contato/?servico={d["param"]}'
    bc, ldbc = breadcrumb([('Serviços', '/servicos/'), (nome, None)])
    if d['slug'] in IA_SERV: img = fig_ia(IA_SERV[d['slug']], d['hero_alt_ilustr'], eager=True)
    elif d['slug'] == 'infraestrutura-de-saneamento': img = fig_foto('projetos/bosque-dos-ipes', d['hero_alt_ilustr'], 'Bosque dos Ipês · RNI · Campo Grande/MS', eager=True)
    else: img = fig_bim(d['hero_img'], eager=True)
    hero = hero_interno('sv-02', d['eyebrow'], d['h1'], d['sub'], btns((d['cta'], orc, 'primary'), ('Falar no WhatsApp', wa(wmsg), 'wa')), img, bc=bc, wide=True)
    sv03 = sec('sv-03', 'C09', f'''<div class="sec-head"><p class="eyebrow">Escopo</p><h2>{e(d['entregas_h2'])}</h2><p class="lead">{e(d['entregas_intro'])}</p></div>
 <ol class="entregas reveal">{''.join(f'<li>{e(x)}</li>' for x in d['entregas'])}</ol>''')
    sv04 = sec('sv-04', '—', f'''<div class="sec-head"><h2>{e(d['quem_h2'])}</h2></div><div class="grid grid--3 cards-quem reveal">{''.join(f'<div class="c-quem"><h3>{e(q["t"])}</h3><p>{e(q["d"])}</p></div>' for q in d['quem'])}</div>''', 'sec bg-light')
    org = f'<p class="orgao">{ic("building")}<span><b>Órgãos</b>{e(d["orgaos"])}</span></p>' if d['orgaos'] else ''
    aprov = (f'<p class="orgao">{ic("check")}<span>Já aprovamos projetos em: {e(", ".join(DADOS["concessionarias"]))}</span></p>' if DADOS['concessionarias'] and d['orgaos']
             else cond('SV-05', 'Já aprovamos projetos em', 'as concessionárias confirmadas') if d['orgaos'] else '')
    sv05 = f'''<section class="sec c18-faixa bg-navy on-dark" id="sv-05" data-componente="C18"><div class="container"><div class="split split--top">
 <div><p class="eyebrow">Normas</p><h2>{e(d['normas_h2'])}</h2><p class="lead">{e(d['normas_txt'])}</p>{btns(('Fale com o engenheiro', wa(wmsg), 'wa-light'))}</div>
 <div><ul class="c18-normas">{''.join(f'<li>{ic("doc")}<span>{e(n)}</span></li>' for n in d['normas'])}</ul>{org}{aprov}</div>
</div></div></section>'''
    imgs = SV06_IMG.get(d['slug'], [])
    link_bim = f'<a class="link-arrow" href="/bim-e-compatibilizacao/">Como usamos BIM {ARW}</a>'
    if imgs:
        sv06 = sec('sv-06', 'C09+C11', f'''<div class="split split--40-60"><div><p class="eyebrow">BIM</p><h2>{e(d['bim_h2'])}</h2><p>{e(d['bim_txt'])}</p>{link_bim}</div><div class="reveal">{fig_bim(imgs[0])}</div></div>''')
    else:  # sem modelo BIM real da disciplina: variação do C09 só com texto (a ilustração já está no hero)
        sv06 = sec('sv-06', 'C09', f'''<div class="sv06-txt reveal"><span class="ico">{ic(s[5], "icon--lg")}</span><div><h2>{e(d['bim_h2'])}</h2><p class="lead">{e(d['bim_txt'])}</p>{link_bim}</div></div>'''
                   + cond('SV-06', 'imagem BIM da disciplina', 'um modelo BIM real desta disciplina'))
    # SV-07: condicional (projetos com a disciplina) → sem dado vira faixa de logos C06
    com = [p for p in PROJ if d['param'] in DADOS['disciplinas_por_projeto'].get(p['slug'], [])]
    if len(com) >= 2:
        sv07 = sec('sv-07', 'C08', f'<div class="sec-head sec-head--row"><h2>Empreendimentos com projeto {e(nome.split(" ", 1)[1] if nome.startswith("Projeto") else nome)}</h2><a class="link-arrow" href="/projetos/?disciplina={d["param"]}">Ver todos {ARW}</a></div><ul class="c08-grid">{"".join(card_projeto(p) for p in com[:3])}</ul>', 'sec bg-light')
    else:
        sv07 = cond('SV-07', 'Projetos com esta disciplina', 'as disciplinas por projeto') + logos('sv-07', 'Quem já contratou nossos projetos', link=('Ver clientes e projetos →', '/projetos/#clientes'), bg='bg-light')
    fq = []
    for f in d['faq']:
        a = e(f['a'])
        if f['link']: a = a.replace('Veja também o projeto de piscina.', f'Veja também o <a href="{f["link"]}">projeto de piscina</a>.')
        fq.append((f['q'], a))
    sv08, ldfaq = faq('sv-08', d['faq_h2'], fq)
    outros = outros_de(d)
    sv09 = sec('sv-09', 'C07', f'''<div class="sec-head sec-head--row"><h2>{e(d['outros_h2'])}</h2><a class="link-arrow" href="/servicos/">Ver todos os serviços {ARW}</a></div>
 <div class="grid grid--3">{''.join(card_servico(o, desc=o[6]) for o in outros)}</div>''', 'sec bg-light bg-grid')
    sv10 = cta_form('sv-10', d['cta_h2'], wmsg, servico=d['param'])
    body = hero + sv03 + sv04 + sv05 + sv06 + sv07 + sv08 + sv09 + sv10
    og = None
    pub(f'/servicos/{d["slug"]}/', documento(f'/servicos/{d["slug"]}/', d['title'], d['meta'], body, ativo='servicos', wa_msg=wmsg, lds=[ldbc, ldfaq], orc=orc))

# =====================================================================
# BIM E COMPATIBILIZAÇÃO
# =====================================================================
def bim():
    bc, ldbc = breadcrumb([('BIM e compatibilização', None)])
    hero = hero_interno('bm-02', 'Em todas as disciplinas', 'BIM e compatibilização de projetos de instalações',
        'Instalações modeladas em 3D e cruzadas com a arquitetura e a estrutura: menos conflito na obra e quantitativos que saem do modelo.',
        btns(('Solicitar orçamento', '/contato/?servico=compatibilizacao-bim', 'primary'), ('Ver modelos reais ↓', '#bm-05', 'secondary')), fig_bim(5, eager=True), bc=bc, wide=True)
    ben = [('conflito', 'Interferências resolvidas antes da obra', 'Tubulação contra viga, duto contra eletrocalha: o conflito aparece no modelo, quando corrigir custa uma revisão, e não uma demolição.'),
           ('calc', 'Quantitativos confiáveis', 'Tubos, conexões, cabos e equipamentos são contados a partir do modelo, o que dá uma base mais sólida ao orçamento da obra.'),
           ('obra', 'Execução com menos dúvida', 'Vistas 3D e detalhes mostram à equipe de campo como cada sistema deve ficar.'),
           ('gear', 'Informação para manutenção e gestão', 'O modelo reúne dados úteis para operar e manter o empreendimento depois da entrega.')]
    bm03 = sec('bm-03', '—', f'<div class="sec-head"><h2>O que muda com o BIM</h2></div><div class="grid grid--4 beneficios reveal">' + ''.join(f'<div class="b"><span class="ico">{ic(i)}</span><h3>{e(t)}</h3><p>{e(x)}</p></div>' for i, t, x in ben) + '</div>', 'sec sec--flush-top')
    etapas = [('Recebimento dos modelos', 'Recebemos a arquitetura e a estrutura, em BIM ou em 2D, e definimos o padrão de entrega.'),
              ('Modelagem das instalações', 'Cada disciplina é modelada com as informações do cálculo.'),
              ('Detecção de conflitos', 'Cruzamos todas as disciplinas e listamos as interferências encontradas.'),
              ('Relatório e ajustes', 'Apresentamos os conflitos com as soluções propostas e ajustamos os projetos.'),
              ('Modelo final', 'Você recebe o modelo compatibilizado e as pranchas para a obra.')]
    bm04 = processo('bm-04', 'Como fazemos a compatibilização', etapas, 'bg-blue-50 bg-grid', nota=False)
    bm05 = sec('bm-05', 'C11', f'<div class="sec-head"><h2>Modelos reais de projetos da Intrépida</h2><p class="lead">Recortes de modelos BIM desenvolvidos pela Intrépida. Clique para ampliar.</p></div>{galeria(range(1, 9), "bim", big=True)}'
               + cond('BM-05', 'Explore um modelo em 3D (fase 2)', 'o visualizador 3D'))
    if DADOS.get('softwares'):
        bm06_in = ficha([('Softwares:', e(DADOS['softwares']))])
    else:
        bm06_in = cond('BM-06', 'ficha de softwares/formatos', 'softwares, formatos, nível de detalhe e padrão do cliente') + '<p class="lead">Entregamos em BIM (modelo 3D) ou em 2D. Envie o padrão BIM da sua empresa com o pedido de orçamento: formato, nível de detalhe e template ficam definidos na proposta.</p>'
    bm06 = sec('bm-06', 'C15', f'<div class="split split--top"><div><h2>Softwares e formatos de entrega</h2></div><div>{bm06_in}</div></div>', 'sec bg-light')
    c2d = ['Cada disciplina em pranchas separadas', 'Conflitos entre sistemas aparecem na sobreposição das pranchas ou na obra', 'Quantitativos levantados a partir dos desenhos', 'Uma revisão precisa ser repetida em cada prancha', 'Boa opção para empreendimentos simples ou processos 2D']
    cbim = ['Todas as disciplinas no mesmo modelo 3D', 'Conflitos detectados no modelo, antes da obra', 'Quantitativos extraídos do modelo', 'Pranchas geradas do modelo: mudou o modelo, mudam as vistas', 'Informação útil também para manutenção e gestão']
    bm07 = sec('bm-07', '—', f'''<div class="sec-head"><h2>2D ou BIM: o que muda na prática</h2></div><div class="comparativo reveal">
 <div class="col"><h3>{ic('doc')}Projeto em 2D</h3><ul>{''.join(f'<li>{e(x)}</li>' for x in c2d)}</ul></div>
 <div class="col col--bim"><h3>{ic('bim')}Projeto em BIM</h3><ul>{''.join(f'<li>{e(x)}</li>' for x in cbim)}</ul></div></div>
 <p class="nota">Fazemos os dois. A escolha depende do empreendimento e do processo da sua empresa, e pode ser discutida no orçamento.</p>''')
    bm08 = sec('bm-08', 'C08', f'<div class="sec-head sec-head--row"><h2>Empreendimentos com projetos da Intrépida</h2><a class="link-arrow" href="/projetos/">Ver todos os projetos {ARW}</a></div><ul class="c08-grid">{"".join(card_projeto(proj_by_name(n)) for n in ["Mirante São Lucas", "Bosque dos Ipês", "Residencial Pacífico"])}</ul>', 'sec bg-light')
    fq = [('O que é BIM?', 'É a sigla de Building Information Modeling, ou modelagem da informação da construção. Em vez de desenhos soltos, o projeto vira um modelo 3D com informação de cada elemento, como diâmetro, material e circuito.'),
          ('Preciso que a arquitetura esteja em BIM?', 'Não necessariamente. As instalações podem ser modeladas sobre uma arquitetura em 2D. Com a arquitetura e a estrutura em BIM, a compatibilização fica mais completa.'),
          ('Em que software vocês trabalham?', 'Entregamos em BIM ou em 2D. Envie o padrão da sua empresa com o pedido de orçamento, e o formato de entrega fica definido na proposta.'),
          ('Vocês compatibilizam projetos de outros escritórios?', 'Envie os projetos que você já tem e o escopo desejado. Na proposta, definimos o que será compatibilizado e como.'),
          ('Projeto em BIM custa mais?', 'O valor depende do escopo e vem detalhado na proposta. Ao comparar, considere quanto custaria resolver na obra um conflito que o modelo mostraria antes.')]
    bm09, ldf = faq('bm-09', 'Perguntas sobre BIM e compatibilização', fq)
    bm10 = cta_botoes('bm-10', 'Quer o seu próximo empreendimento compatibilizado em BIM?', 'Envie a arquitetura e as disciplinas de que você precisa. A proposta vem com escopo, prazo e valor.', WA['bim'], orc='/contato/?servico=compatibilizacao-bim')
    body = hero + bm03 + bm04 + bm05 + bm06 + bm07 + bm08 + bm09 + bm10
    pub('/bim-e-compatibilizacao/', documento('/bim-e-compatibilizacao/', 'BIM e compatibilização de projetos | Intrépida',
        'Projetos de instalações em BIM e compatibilização entre disciplinas: interferências resolvidas no modelo e quantitativos confiáveis. Veja modelos reais.',
        body, ativo='bim', wa_msg=WA['bim'], lds=[ldbc, ldf], orc='/contato/?servico=compatibilizacao-bim'))

# =====================================================================
# PROJETOS — LISTAGEM
# =====================================================================
def projetos():
    bc, ldbc = breadcrumb([('Projetos', None)])
    hero = f'''<section class="c03-hero c03-hero--low on-dark" id="pj-02" data-componente="C03" data-hero>
 <div class="c03-hero__media">{picture('projetos/residencial-pacifico', 'Vista aérea dos blocos do Residencial Pacífico, da Vila Construtora, em Ribeirão das Neves/MG', '100vw', eager=True, max_default=1600)}</div>
 <div class="on-dark">{bc}</div>
 <div class="container c03-hero__in"><div class="c03-hero__txt"><p class="eyebrow">Portfólio</p><h1>Projetos de instalações em 18 empreendimentos de 6 estados</h1>
  <p class="lead">De 142 a 1.800 unidades, para construtoras e incorporadoras como MRV, Direcional, RNI e Precon.</p>
  <a class="link-arrow" href="/contato/">Solicitar orçamento {ARW}</a></div></div>
 <p class="c03-hero__credit">Residencial Pacífico · Vila Construtora · Ribeirão das Neves/MG</p>
</section>'''
    ufs = [('MG', 'Minas Gerais', 11), ('DF', 'Distrito Federal', 2), ('SP', 'São Paulo', 2), ('RJ', 'Rio de Janeiro', 1), ('MS', 'Mato Grosso do Sul', 1), ('SC', 'Santa Catarina', 1)]
    clientes = sorted({p['cliente'] for p in PROJ}, key=lambda x: x.lower())
    opt_uf = ''.join(f'<option value="{u}">{n} ({c})</option>' for u, n, c in ufs)
    opt_cli = ''.join(f'<option value="{e(c)}">{e(c)}</option>' for c in clientes)
    filtros = f'''<div class="c22-mobilebar"><button class="btn btn--secondary btn--sm" type="button" id="btn-filtrar" aria-expanded="false" aria-controls="pj-sheet">{ic('filter', 'icon--sm')}<span>Filtrar</span></button></div>
 <div class="c22-sheet" id="pj-sheet"><div class="c22-sheet__scrim" data-sheet-close></div>
 <div class="c22-sheet__panel" role="group" aria-labelledby="pj-filtrar-t">
  <div class="c22-sheet__head"><h2 id="pj-filtrar-t-m">Filtrar projetos</h2><button class="icon-btn icon-btn--dark" type="button" data-sheet-close aria-label="Fechar filtros">{ic('close')}</button></div>
  <form class="c22-filtros" id="pj-04" data-componente="C22" onsubmit="return false">
   <h2 class="visually-hidden" id="pj-filtrar-t">Filtrar projetos</h2>
   <div class="field"><label for="f-uf">Estado</label><select class="select" id="f-uf"><option value="">Todos os estados</option>{opt_uf}</select></div>
   <div class="field"><label for="f-cliente">Cliente</label>
    <div class="busca"><label class="visually-hidden" for="f-busca">Buscar cliente</label>{ic('search')}<input class="input" id="f-busca" type="search" placeholder="Buscar cliente" autocomplete="off"></div>
    <p class="help" id="f-busca-vazio" hidden>Nenhum cliente com esse nome</p>
    <select class="select" id="f-cliente"><option value="">Todos os clientes</option>{opt_cli}</select></div>
   <!-- CONDICIONAL Filtro "Tipo de empreendimento": só com ≥ 2 tipos confirmados. Filtro "Disciplina": só com disciplinas por projeto. -->
   <div class="c22-filtros__acoes"><button class="btn btn--secondary btn--sm" type="button" data-limpar>Limpar filtros</button></div>
  </form>
  <div class="c22-sheet__foot btn-row btn-row--stack"><button class="btn" type="button" id="pj-ver" data-sheet-close>Ver 18 projetos</button><button class="btn btn--secondary" type="button" data-limpar>Limpar filtros</button></div>
 </div></div>'''
    grade = ''.join(card_projeto(p) for p in PROJ)
    pj05 = f'''<section class="sec" id="pj-05" data-componente="C22+C08" style="padding-top:2.5rem"><div class="container">
 {filtros}
 <div class="c22-ativos" id="pj-ativos"></div>
 <h2 class="visually-hidden">Todos os projetos</h2>
 <p class="c22-count" id="pj-count" aria-live="polite" tabindex="-1">18 projetos</p>
 <ul class="c08-grid" id="pj-grid">{grade}</ul>
 <div class="vazio" id="pj-vazio" hidden><h3>Nenhum projeto com esses filtros</h3><p>Tente outro estado ou cliente. Ou conte sobre o seu empreendimento: a experiência que você procura pode não estar no site.</p>
  <div class="btn-row"><button class="btn btn--secondary" type="button" data-limpar>Limpar filtros</button><a class="btn" href="/contato/">Falar sobre meu projeto</a></div></div>
</div></section>'''
    grid, lista = mapa_ufs(True)
    pj07 = sec('pj-07', 'C24', f'<div class="c24-mapa"><div><h2>Onde já atuamos</h2><p class="lead">Clique em um estado para ver os projetos.</p>{lista}</div><div>{grid}</div></div>', 'sec bg-blue-50')
    body = (hero + numeros('pj-03') + pj05 + logos('clientes', 'Clientes atendidos', '24 empresas, entre construtoras e incorporadoras, já contrataram projetos da Intrépida.', link=None, todos=True, bg='bg-light')
            + pj07 + cta_botoes('pj-08', 'Seu empreendimento pode ser o próximo desta lista', 'Conte o porte, a cidade e as disciplinas de que você precisa. A proposta vem com escopo, prazo e valor.', WA['projetos']))
    body = body.replace('id="clientes" data-componente="C06"', 'id="clientes" data-componente="C06" data-secao="PJ-06"')
    pub('/projetos/', documento('/projetos/', 'Projetos em 18 empreendimentos de 6 estados | Intrépida',
        'Veja 18 empreendimentos em 6 estados com projetos da Intrépida, para clientes como MRV, Direcional, RNI e Precon. Filtre por estado e cliente.',
        body, ativo='projetos', wa_msg=WA['projetos'], lds=[ldbc]))

# =====================================================================
# PROJETO INDIVIDUAL (modelo único para os 18)
# =====================================================================
def projeto(i, p):
    loc = f'{p["cidade"]}/{p["uf"]}'; wmsg = wa_projeto(p['nome'])
    bc, ldbc = breadcrumb([('Projetos', '/projetos/'), (p['nome'], None)])
    if p['foto']:
        cls = ' pp-hero__media--content' if p['baixa_res'] else ''
        media = f'<div class="pp-hero__media{cls}">{picture("projetos/" + p["slug"], p["alt"], "(min-width: 1025px) 1200px, 100vw", eager=True, max_default=1600)}</div>'
    else:
        media = (f'<div class="pp-hero__media"><div class="semfoto" data-placeholder="foto-projeto">{ph("Placeholder · foto do empreendimento a receber")}<img class="simb" src="/assets/img/marca/logo-intrepida-simbolo.svg" alt="" width="26" height="41">'
                 f'<span class="nm" aria-hidden="true">{e(p["nome"])}</span><span class="lc" aria-hidden="true">{e(p["cliente"])} · {e(loc)}</span></div></div>')
    verbo = 'é um empreendimento'
    abertura = f'O {p["nome"]} {verbo} da {p["cliente"]} com {p["unidades"]} unidades em {loc}. A Intrépida Engenharia e Projetos desenvolveu projetos de engenharia para o empreendimento.'
    disc = DADOS['disciplinas_por_projeto'].get(p['slug'])
    if disc:
        nomes = [next(s[1].lower() for s in SM if s[3] == x) for x in disc]
        abertura = abertura.rsplit('. ', 1)[0] + '. A Intrépida desenvolveu os projetos de ' + (', '.join(nomes[:-1]) + ' e ' + nomes[-1] if len(nomes) > 1 else nomes[0]) + '.'
    logo = CLI_LOGO.get(p['cliente'])
    cliente_dd = (logo_img(logo, '') .replace('alt=""', 'alt="" aria-hidden="true"') if logo else '') + f'<span>{e(p["cliente"])}</span>'
    rows = [('Cliente', cliente_dd), ('Local', e(loc)), ('Unidades', e(p['unidades'])), ('Tipo', None), ('Área construída', None), ('Ano', None),
            ('Disciplinas projetadas', ' '.join(f'<a class="selo" href="/servicos/{next(s[0] for s in SM if s[3] == x)}/">{e(next(s[1] for s in SM if s[3] == x))}</a>' for x in disc) if disc else None),
            ('Formato de entrega', None)]
    orc = f'/contato/?ref=projeto-{p["slug"]}'
    aside = f'''<aside class="cta-card on-dark" id="pp-04" data-componente="PP-04"><h2>Tem um empreendimento parecido?</h2><p>Conte sobre ele e receba uma proposta com escopo, prazo e valor.</p>
 {btns(('Solicitar orçamento', orc, 'primary'), ('Falar no WhatsApp', wa(wmsg), 'wa-light'))}</aside>'''
    corpo = f'''<section class="sec" id="pp-03" data-componente="C15" style="padding-top:0"><div class="container"><div class="pp-body">
 <div class="main"><h2>Ficha técnica</h2>{ficha(rows)}
  {cond('PP-03', 'linhas Tipo, Área construída, Ano, Disciplinas projetadas e Formato de entrega', 'os dados do cliente')}</div>
 {aside}</div></div></section>'''
    pp05 = cond('PP-05', 'Desafio e solução', 'o case fornecido pelo cliente')
    pp06 = cond('PP-06', 'Galeria', '≥ 2 imagens do projeto')
    pp07 = cond('PP-07', 'Depoimento do cliente', 'depoimento real autorizado')
    rel = [proj_by_name(n) for n in p['relacionados']]
    if all(r['cliente'] == p['cliente'] for r in rel): h2r = f'Outros projetos para {p["cliente"]}'
    elif all(r['uf'] == p['uf'] for r in rel): h2r = f'Outros projetos em {p["estado"]}'
    else: h2r = 'Outros projetos'
    pp08 = sec('pp-08', 'C08', f'<div class="sec-head sec-head--row"><h2>{e(h2r)}</h2><a class="link-arrow" href="/projetos/">Ver todos os projetos {ARW}</a></div><ul class="c08-grid">{"".join(card_projeto(r) for r in rel)}</ul>', 'sec bg-light')
    ant, prox = PROJ[i - 1], PROJ[(i + 1) % len(PROJ)]
    pp09 = f'''<nav class="sec sec--tight" id="pp-09" aria-label="Navegação entre projetos"><div class="container"><div class="pp-nav">
 <a href="/projetos/{ant['slug']}/" rel="prev"><span class="k">‹ Projeto anterior</span><span class="n">{e(ant['nome'])}</span></a>
 <a class="next" href="/projetos/{prox['slug']}/" rel="next"><span class="k">Próximo projeto ›</span><span class="n">{e(prox['nome'])}</span></a></div></div></nav>'''
    pp10 = cta_botoes('pp-10', 'Tem um empreendimento parecido?', 'Conte sobre ele e receba uma proposta com escopo, prazo e valor.', wmsg, orc=orc)
    hero = f'''<section class="pp-hero" id="pp-02" data-componente="C03" data-hero>{bc}<div class="container">{media}
 <div class="pp-hero__head"><h1>{e(p['nome'])}</h1><p class="linha">{e(p['cliente'])} · {e(loc)}</p></div>
 {cond('PP-02', 'crédito da foto', 'o crédito exigido pelo cliente')}
 <p class="lead" style="max-width:70ch;margin-top:1.25rem">{e(abertura)}</p></div></section>'''
    body = hero + corpo + pp05 + pp06 + pp07 + pp08 + pp09 + pp10
    og = None
    if p['foto']:
        import glob as _g
        _ws = sorted(int(m.group(1)) for f in _g.glob(str(B.parent / 'assets' / 'img' / 'projetos' / f'{p["slug"]}-*.jpg')) if (m := re.search(r'-(\d+)\.jpg$', f)))
        _ok = [w for w in _ws if w <= 1200] or _ws
        og = f'/assets/img/projetos/{p["slug"]}-{_ok[-1]}.jpg' if _ok else None
    pub(f'/projetos/{p["slug"]}/', documento(f'/projetos/{p["slug"]}/', p['title'], p['meta'], body, ativo='projetos', wa_msg=wmsg, lds=[ldbc], og_img=og, orc=orc))

# =====================================================================
# SOBRE
# =====================================================================
def sobre():
    bc, ldbc = breadcrumb([('Sobre', None)])
    pdf = btns(('Baixar portfólio (PDF)', DADOS['pdf_portfolio'], 'secondary')) if DADOS['pdf_portfolio'] else ''
    hero = hero_interno('sb-02', 'Sobre a Intrépida', 'Uma empresa de projetos, feita para quem constrói',
        'A Intrépida Engenharia e Projetos desenvolve projetos de instalações prediais e infraestrutura, em 2D e BIM, para construtoras, incorporadoras e arquitetos. Não executamos obras: entregamos o projeto de que a sua obra precisa.',
        btns(('Solicitar orçamento', '/contato/', 'primary')) + (pdf or cond('SB-02', 'Baixar portfólio (PDF)', 'o PDF liberado')),
        f'<div style="position:relative">{ph("Imagem provisória · fotografar escritório/equipe")}{fig_foto("projetos/bosque-dos-ipes", "Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS", "Bosque dos Ipês · RNI · Campo Grande/MS", eager=True)}</div>', bc=bc)
    txt = ['Somos uma empresa técnica de Belo Horizonte dedicada a projetos de instalações residenciais, comerciais e de redes de infraestrutura urbana.',
           'Trabalhamos em 2D e em BIM, com informação para a execução, a implantação, a manutenção e a gestão do empreendimento. O objetivo é que a obra receba um projeto compatível entre as disciplinas e pronto para a análise das concessionárias.',
           'Nosso portfólio reúne 18 empreendimentos, de 142 a 1.800 unidades, e já atendemos oito estados. Mais de 24 construtoras e incorporadoras já contrataram nossos projetos.',
           'Intrépida quer dizer corajosa. Para nós, isso significa assumir empreendimentos grandes e complexos com método, cálculo e responsabilidade técnica.']
    tl = cond('SB-03', 'Linha do tempo', 'ano de fundação e marcos com data')
    sb03 = sec('sb-03', 'C09', f'<div class="split split--top"><div><h2>Quem é a Intrépida</h2></div><div class="reveal">{"".join(f"<p class=lead>{e(t)}</p>" if k == 0 else f"<p>{e(t)}</p>" for k, t in enumerate(txt))}{tl}</div></div>')
    crea = f'<p>CREA {e(DADOS["crea_rt"])}</p>' if DADOS['crea_rt'] else cond('SB-04', 'CREA', 'o nº do CREA')
    lk = f'<a class="link-arrow" href="{e(DADOS["linkedin_rt"])}" target="_blank" rel="noopener">Ver perfil no LinkedIn {ARW}</a>' if DADOS['linkedin_rt'] else cond('SB-04', 'LinkedIn pessoal', 'a URL')
    sb04 = sec('sb-04', 'C17', f'''<div class="c17-rt c17-rt--full">{rt_foto(True)}<div><h2>Responsável técnico</h2><p class="c17-rt__nome">Carlos Alberto Grope</p><p class="c17-rt__cargo">Diretor técnico · Engenheiro civil sanitarista</p>{crea}
 <p style="max-width:62ch">Carlos Alberto Grope é engenheiro civil sanitarista e diretor técnico da Intrépida. Ele conduz os projetos da empresa e é o seu contato técnico do orçamento à entrega.</p>
 {cond('SB-04', 'Mini-bio ampliada', 'formação, trajetória e especialidades')}{lk}</div></div>''', 'sec bg-light')
    sb05 = cond('SB-05', 'Equipe', 'nomes, funções e fotos reais')
    grid, lista = mapa_ufs(False)
    sb06 = f'''<section class="sec" id="sb-06" data-componente="C05+C24"><div class="container"><div class="sec-head"><h2>Onde já atuamos</h2></div></div>
 {numeros('sb-06-numeros', light=True).replace('class="c05-numeros', 'class="c05-numeros').replace('<section', '<div').replace('</section>', '</div>')}
 <div class="container" style="margin-top:3rem"><div class="c24-mapa"><div>{lista}</div><div>{grid}</div></div></div></section>'''
    dados = [('Razão social:', e(DADOS['razao_social']) if DADOS['razao_social'] else None), ('Nome fantasia:', 'Intrépida Engenharia e Projetos'),
             ('CNPJ:', e(DADOS['cnpj']) if DADOS['cnpj'] else None), ('Registro da empresa no CREA:', e(DADOS['crea_empresa']) if DADOS['crea_empresa'] else None),
             ('Responsável técnico:', 'Carlos Alberto Grope, engenheiro civil sanitarista' + (f' · CREA {e(DADOS["crea_rt"])}' if DADOS['crea_rt'] else '')),
             ('Endereço:', END_LINHA), ('E-mail:', f'<a href="mailto:{EMAIL}">{EMAIL}</a>'), ('Telefone:', f'<a href="{TEL_HREF}">(31) 3070-6568</a>')]
    pdf8 = (f'<p>{btns(("Baixar portfólio (PDF)", DADOS["pdf_portfolio"], "navy"))}</p><p class="nota">Clientes, empreendimentos e modelos BIM em um arquivo.</p>' if DADOS['pdf_portfolio']
            else f'<p class="nota">Precisa de mais documentos para o cadastro? Escreva para <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>')
    # UX-11: a frase de abertura promete o PDF; só aparece quando o arquivo existir (DADOS['pdf_portfolio']).
    intro8 = ('<p class="lead">Para o setor de suprimentos: os dados da empresa e o portfólio em PDF.</p>' if DADOS['pdf_portfolio']
              else cond('SB-08', 'frase de abertura que cita o portfólio em PDF', 'o PDF liberado'))
    sb08 = f'''<section class="sec" id="dados-cadastrais" data-componente="C15" data-secao="SB-08"><div class="container"><div class="split split--top">
 <div><h2>Dados para cadastro de fornecedor</h2>{intro8}</div>
 <div>{ficha(dados)}{cond('SB-08', 'Razão social, CNPJ e CREA', 'os dados cadastrais')}{pdf8}</div></div></div></section>'''
    body = (hero + sb03 + sb04 + sb05 + sb06 + processo('sb-07', bg='bg-blue-50 bg-grid') + sb08 + logos('sb-09', 'Quem já contratou nossos projetos', bg='bg-light')
            + cta_botoes('sb-10', 'Vamos conversar sobre o seu empreendimento?', 'Envie as informações do projeto e receba uma proposta com escopo, prazo e valor.', WA['sobre']))
    pub('/sobre/', documento('/sobre/', 'Sobre a Intrépida Engenharia e Projetos | BH',
        'Empresa de Belo Horizonte de projetos de instalações prediais e infraestrutura, em 2D e BIM. Conheça o responsável técnico e os dados para cadastro.',
        body, ativo='sobre', wa_msg=WA['sobre'], lds=[ldbc]))

# =====================================================================
# CONTATO (C21a — 3 etapas)
# =====================================================================
REQ_TIPO = ' data-req="Escolha o tipo de empreendimento."'
REQ_DISC = ' data-req="Marque pelo menos um projeto ou a opção &quot;Ainda não sei&quot;." data-group="1"'
UFS27 = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
def contato():
    bc, ldbc = breadcrumb([('Contato', None)])
    selo1 = f'Retorno em até {DADOS["prazo_resposta_dias"]} dias úteis' if DADOS['prazo_resposta_dias'] else 'Proposta com escopo, prazo e valor'
    sub = 'Conte sobre o empreendimento em três etapas rápidas. Com a arquitetura em mãos, a proposta sai mais precisa.' + (f' Retornamos em até {DADOS["prazo_resposta_dias"]} dias úteis.' if DADOS['prazo_resposta_dias'] else '')
    selos = f'<ul class="selos">{"".join(f"<li>{ic(i)}{e(t)}</li>" for i, t in [("check", selo1), ("user", "Atendimento direto com o engenheiro"), ("shield", "Seus arquivos tratados com sigilo")])}</ul>'
    hero = hero_interno('ct-02', 'Contato e orçamento', 'Solicite um orçamento de projeto', sub, selos + '<p class="only-mobile" style="margin-top:1rem"><a class="link-arrow" href="#canais">Prefere WhatsApp? ↓</a></p>', bc=bc)
    tipos = [('multifamiliar', 'building', 'Residencial multifamiliar', 'Prédios e conjuntos de apartamentos'), ('loteamento', 'lotes', 'Loteamento ou condomínio horizontal', 'Casas e lotes'),
             ('comercial', 'loja', 'Comercial ou corporativo', 'Lojas, salas, galpões, hotéis'), ('residencia', 'casa', 'Residência unifamiliar', 'Casa própria'),
             ('infraestrutura', 'saneamento', 'Infraestrutura urbana', 'Redes de água, esgoto e drenagem'), ('outro', 'mais', 'Outro', '')]
    rad = ''.join(f'<label class="opt-card"><input type="radio" name="tipo" value="{v}" id="c-tipo-{v}"{REQ_TIPO if k == 0 else ""}><span class="ico">{ic(i)}</span><span><b>{e(t)}</b>{f"<small>{e(h)}</small>" if h else ""}</span></label>' for k, (v, i, t, h) in enumerate(tipos))
    fases = ['Estudo de viabilidade', 'Arquitetura em desenvolvimento', 'Projeto legal aprovado', 'Projeto executivo', 'Obra em andamento']
    disc_grp = lambda g: ''.join(f'<label class="check check--box"><input type="checkbox" name="disciplinas" value="{s[3]}" id="c-d-{s[3]}"{REQ_DISC if s[3] == "hidrossanitario" else ""}><span>{e(s[1])}</span></label>' for s in grupo(g))
    errsum = '<div class="err-summary" tabindex="-1"><h3></h3><ul></ul></div>'
    maxmb = DADOS['upload_max_mb']
    step1 = f'''<div class="step is-active" data-title="Etapa 1 de 3 — O empreendimento"><h2>O empreendimento</h2><p class="step-intro">Comece pelo projeto. Seus dados de contato ficam para o fim.</p>{errsum}
 <fieldset class="field" style="border:0;padding:0;margin:0"><legend class="fs-legend">Tipo de empreendimento</legend><div class="opts-tipo">{rad}</div>{f_err()}</fieldset>
 <!-- Opção "Residência unifamiliar" é CONDICIONAL ao público P4 (pendência 14 do wireframe). -->
 <div class="field cond" data-show-if="outro" hidden><label for="c-tipo-outro-txt">Qual tipo?</label><input class="input" id="c-tipo-outro-txt" name="tipo_outro" placeholder="Ex.: clínica, escola, indústria" data-req="Conte qual é o tipo de empreendimento.">{f_err()}</div>
 <div class="cols-2 cols-2--uf">
  <div class="field"><label for="c-cidade">Cidade do empreendimento</label><input class="input" id="c-cidade" name="cidade" placeholder="Ex.: Belo Horizonte" autocomplete="address-level2" data-req="Informe a cidade do empreendimento.">{f_err()}</div>
  <div class="field"><label for="c-uf">Estado</label><select class="select" id="c-uf" name="uf" data-req="Selecione o estado."><option value="">Selecione</option>{''.join(f'<option>{u}</option>' for u in UFS27)}</select>{f_err()}</div></div>
 <div class="field cond" data-show-if="multifamiliar loteamento" hidden><label for="c-unidades">Número de unidades</label><p class="help" id="c-unid-h">Apartamentos, casas ou lotes.</p>
  <input class="input" id="c-unidades" name="unidades" inputmode="numeric" placeholder="Ex.: 240" aria-describedby="c-unid-h" data-req="Informe o número de unidades ou marque &quot;Ainda não definido&quot;." data-num="Use só números, por exemplo 240.">{f_err()}
  <label class="check"><input type="checkbox" id="c-unid-nd" name="unidades_nd"><span>Ainda não definido</span></label></div>
 <div class="field cond" data-show-if="comercial residencia outro" hidden><label for="c-area">Área construída aproximada, em m² (opcional)</label><input class="input" id="c-area" name="area" inputmode="numeric" placeholder="Ex.: 1500" data-num="Use só números, por exemplo 1500.">{f_err()}</div>
 <div class="field"><label for="c-fase">Fase do projeto (opcional)</label><p class="help" id="c-fase-h">Ajuda a definir o que entra na proposta.</p><select class="select" id="c-fase" name="fase" aria-describedby="c-fase-h"><option value="">Selecione</option>{''.join(f'<option>{f}</option>' for f in fases)}</select></div>
 <div class="step-nav"><span></span><button class="btn" type="button" data-next>Continuar {ARW}</button></div></div>'''
    step2 = f'''<div class="step" data-title="Etapa 2 de 3 — Escopo"><h2>Escopo</h2><p class="step-intro">Marque o que você precisa. Se não souber, a gente orienta.</p>{errsum}
 <fieldset class="field" data-checkgroup style="border:0;padding:0;margin:0"><legend class="fs-legend">Quais projetos você precisa?</legend><p class="help">Marque um ou mais.</p>
  <fieldset class="disc-grupo"><legend>Instalações prediais</legend><div class="disc-checks">{disc_grp(G_PRED)}</div></fieldset>
  <fieldset class="disc-grupo"><legend>Infraestrutura urbana</legend><div class="disc-checks">{disc_grp(G_INFRA)}</div></fieldset>
  <fieldset class="disc-grupo"><legend>Eficiência e sustentabilidade</legend><div class="disc-checks">{disc_grp(G_EFIC)}</div></fieldset>
  <div class="disc-checks"><label class="check check--box"><input type="checkbox" name="disciplinas" value="compatibilizacao-bim" id="c-d-bim"><span>Compatibilização BIM</span></label>
   <label class="check check--box"><input type="checkbox" name="disciplinas" value="nao-sei" id="c-d-nao-sei" aria-describedby="c-naosei-h"><span>Ainda não sei — quero orientação<small class="help" id="c-naosei-h" style="display:block">Indicamos as disciplinas a partir da arquitetura.</small></span></label></div>
  {f_err()}</fieldset>
 <fieldset class="field" style="border:0;padding:0;margin:0"><legend class="fs-legend">Formato de entrega (opcional)</legend><div class="radios-inline">{''.join(f'<label class="check"><input type="radio" name="formato" value="{v}"><span>{t}</span></label>' for v, t in [('bim', 'BIM (modelo 3D)'), ('2d', '2D (DWG)'), ('indiferente', 'Sem preferência')])}</div></fieldset>
 <div class="field"><label for="c-prazo">Prazo desejado para o projeto</label><select class="select" id="c-prazo" name="prazo" data-req="Escolha um prazo."><option value="">Selecione</option>{''.join(f'<option>{x}</option>' for x in ['Até 30 dias', 'De 1 a 3 meses', 'De 3 a 6 meses', 'Sem prazo definido'])}</select>{f_err()}</div>
 <div class="field"><label for="c-link">Link dos arquivos (opcional)</label><p class="help" id="c-link-h">Google Drive, WeTransfer, Dropbox ou outro. Confira se o link está liberado para visualização.</p><input class="input" id="c-link" name="link" type="url" placeholder="https://" aria-describedby="c-link-h" data-fmt="Cole um link completo, começando com https://">{f_err()}</div>
 <div class="field"><span class="fs-legend" id="c-arq-l">Anexar arquivos (opcional)</span>
  <div class="dropzone" data-max-mb="{maxmb}">{ic('upload')}<span>Arraste os arquivos aqui ou clique para selecionar</span><input type="file" id="c-arq" name="arquivos" multiple accept=".pdf,.dwg,.rvt,.ifc,.zip" aria-labelledby="c-arq-l" aria-describedby="c-arq-h"></div>
  <p class="help" id="c-arq-h">PDF, DWG, RVT, IFC ou ZIP, até {maxmb} MB no total. Arquivos grandes? Use o campo de link acima.</p>
  <p class="err" id="c-arq-err" role="alert" hidden style="display:flex"></p><ul class="files" aria-live="polite"></ul></div>
 <div class="field"><label for="c-msg">Conte mais sobre o projeto (opcional)</label><textarea class="textarea" id="c-msg" name="mensagem" maxlength="1000" data-counter="c-msg-n" data-max="A mensagem passou de 1.000 caracteres." aria-describedby="c-msg-n" placeholder="Ex.: 3 torres de 12 pavimentos, arquitetura em desenvolvimento, precisamos aprovar o projeto na concessionária até março."></textarea><p class="counter" id="c-msg-n">Até 1.000 caracteres</p>{f_err()}</div>
 <div class="step-nav"><button class="btn btn--secondary" type="button" data-prev>Voltar</button><button class="btn" type="button" data-next>Continuar {ARW}</button></div></div>'''
    step3 = f'''<div class="step" data-title="Etapa 3 de 3 — Seus dados"><h2>Seus dados</h2><p class="step-intro">Para onde enviamos a proposta?</p>{errsum}
 <div class="field"><label for="c-nome">Nome completo</label><input class="input" id="c-nome" name="nome" autocomplete="name" data-req="Informe seu nome.">{f_err()}</div>
 <div class="cols-2"><div class="field"><label for="c-emp">Empresa (opcional)</label><p class="help" id="c-emp-h">Deixe em branco se for pessoa física.</p><input class="input" id="c-emp" name="empresa" autocomplete="organization" aria-describedby="c-emp-h"></div>
  <div class="field"><label for="c-cargo">Cargo (opcional)</label><p class="help">&nbsp;</p><input class="input" id="c-cargo" name="cargo" autocomplete="organization-title" placeholder="Ex.: Coordenador de projetos"></div></div>
 <div class="cols-2"><div class="field"><label for="c-email">E-mail</label><input class="input" id="c-email" name="email" type="email" autocomplete="email" placeholder="nome@empresa.com.br" data-req="Informe seu e-mail." data-fmt="Digite um e-mail válido, como nome@empresa.com.br.">{f_err()}</div>
  <div class="field"><label for="c-tel">WhatsApp ou telefone</label><input class="input" id="c-tel" name="telefone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(31) 90000-0000" aria-describedby="c-tel-h" data-req="Informe um telefone para contato." data-fmt="Digite o número com DDD, como (31) 90000-0000."><p class="help" id="c-tel-h">Com DDD.</p>{f_err()}</div></div>
 <div class="field"><label for="c-origem">Como conheceu a Intrépida? (opcional)</label><select class="select" id="c-origem" name="como_conheceu"><option value="">Selecione</option>{''.join(f'<option>{x}</option>' for x in ['Busca no Google', 'Indicação', 'LinkedIn', 'Já sou cliente', 'Outro'])}</select></div>
 <div class="field"><label class="check"><input type="checkbox" id="c-lgpd" name="lgpd" data-req="Para enviar, marque que concorda com a Política de privacidade."><span>Concordo com o uso dos meus dados para receber o orçamento, conforme a <a href="/politica-de-privacidade/" target="_blank" rel="noopener">Política de privacidade<span class="visually-hidden"> (abre em nova aba)</span></a>.</span></label>{f_err()}</div>
 <!-- CONDICIONAL "Quero receber novidades da Intrépida por e-mail (opcional).": só se houver comunicação por e-mail. -->
 {FALHA_ENVIO}
 <div class="step-nav"><button class="btn btn--secondary" type="button" data-prev>Voltar</button><button class="btn" type="submit">Enviar pedido de orçamento</button></div>
 <p class="below-btn">{'Resposta em até ' + str(DADOS['prazo_resposta_dias']) + ' dias úteis. ' if DADOS['prazo_resposta_dias'] else ''}Você recebe uma cópia do pedido no seu e-mail.</p></div>'''
    hidden = ''.join(f'<input type="hidden" name="{n}" value="">' for n in ['servico', 'ref', 'origem', 'utm_source', 'utm_medium', 'utm_campaign']) + '<input type="hidden" name="form_label" value="orcamento_completo">'
    form = f'''<form class="form-card form" id="ct-03-form" data-form="orcamento_completo" action="/obrigado/" method="post" enctype="multipart/form-data" data-componente="C21a" aria-label="Pedido de orçamento">
 <p class="form-legend">Todos os campos são obrigatórios, exceto os marcados como opcionais.</p>
 <div class="progress" aria-live="polite"><p class="progress__txt">Etapa 1 de 3 — O empreendimento</p><div class="progress__bar" aria-hidden="true"><span class="on"></span><span></span><span></span></div></div>
 {step1}{step2}{step3}{hidden}
 <div class="hp" aria-hidden="true"><label>Não preencha<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
</form>'''
    hor = f'<div class="canal"><span class="k">{ic("clock")}Horário</span><span class="v">{e(DADOS["horario"])}</span></div>' if DADOS['horario'] else cond('CT-03', 'Horário', 'o horário de atendimento')
    aside = f'''<aside id="canais" aria-labelledby="canais-t"><h2 id="canais-t" style="font-size:1.375rem">Prefere falar agora?</h2><div class="canais">
 <div class="canal"><span class="k">{ic('whatsapp')}WhatsApp</span><span class="v">(31) 99649-8629</span>{btns(('Falar no WhatsApp', wa(WA['contato']), 'wa'), stack=False)}</div>
 <div class="canal"><span class="k">{ic('phone')}Telefone</span><span class="v">(31) 3070-6568</span><a class="btn btn--secondary btn--sm" href="{TEL_HREF}">Ligar</a></div>
 <div class="canal"><span class="k">{ic('mail')}E-mail</span><span class="v">{EMAIL}</span><a class="btn btn--secondary btn--sm" href="mailto:{EMAIL}">Enviar e-mail</a></div>
 <div class="canal"><span class="k">{ic('pin')}Endereço</span><span class="v">{END_LINHA}</span></div>{hor}</div></aside>'''
    ct03 = f'<section class="sec sec--flush-top" id="ct-03" data-componente="C21a"><div class="container"><div class="contato-grid">{form}{aside}</div></div></section>'
    fq = [('Quais arquivos ajudam?', 'A arquitetura (plantas, cortes, fachadas e implantação) em DWG, PDF ou RVT, o número de unidades e de pavimentos e a fase do projeto. Se tiver, envie também a estrutura e as diretrizes das concessionárias.'),
          ('Meus arquivos ficam em sigilo?', 'Sim. Usamos os arquivos só para preparar o orçamento e o projeto, e não os repassamos a terceiros.'),
          ('Em quanto tempo recebo a proposta?', f'Em até {DADOS["prazo_resposta_dias"]} dias úteis depois de recebermos as informações completas.' if DADOS['prazo_resposta_dias'] else 'Depende do porte e das disciplinas. Assim que analisarmos o pedido, informamos quando a proposta fica pronta.'),
          ('Ainda não tenho a arquitetura pronta. Posso pedir orçamento?', 'Pode. Quanto antes o projetista entra, mais fácil prever shafts, reservatórios e as exigências das concessionárias. Envie o estudo que tiver.')]
    ct04, ldf = faq('ct-04', 'O que enviar para um orçamento rápido', fq, 'bg-light')
    if DADOS['atendimento_presencial']:
        maps = 'https://www.google.com/maps/search/?api=1&query=' + urllib.parse.quote(END_LINHA)
        ct05 = sec('ct-05', '—', f'<h2>Onde estamos</h2><p>Rua dos Goitacazes, 103, salas 1604 e 1606 · Centro, Belo Horizonte/MG · CEP 30190-910</p><p>{e(DADOS["atendimento_presencial"])}</p><a class="btn btn--secondary" href="{maps}" target="_blank" rel="noopener" aria-label="Abrir endereço no Google Maps (abre em nova aba)">Abrir no mapa</a>')
    else:
        ct05 = cond('CT-05', 'Endereço e mapa', 'a confirmação de atendimento presencial')
    body = hero + ct03 + ct04 + ct05
    pub('/contato/', documento('/contato/', 'Solicite orçamento de projeto de instalações | Intrépida',
        'Peça orçamento de projetos hidrossanitário, elétrico, de gás, BIM e infraestrutura. Envie a arquitetura pelo formulário ou fale no WhatsApp.',
        body, ativo='contato', wa_msg=WA['contato'], lds=[ldbc, ldf], sem_c19=True, sem_c20=True))

# =====================================================================
# OBRIGADO, 404, POLÍTICA
# =====================================================================
def obrigado():
    pdf = f'<a class="btn btn--secondary" href="{e(DADOS["pdf_portfolio"])}" download>Baixar portfólio (PDF)</a>' if DADOS['pdf_portfolio'] else cond('OB', 'Baixar portfólio (PDF)', 'o PDF liberado')
    passos = ['Analisamos as informações e os arquivos do seu empreendimento.', 'Entramos em contato para alinhar escopo e disciplinas.', 'Você recebe a proposta com escopo, prazo e valor.']
    body = f'''<section class="c04-hero c04-hero--noimg" id="ob-01" data-componente="C04"><div class="container"><div class="c04-hero__grid"><div class="c04-hero__txt">
 <span class="ico" style="display:inline-grid;place-items:center;width:64px;height:64px;border-radius:50%;background:var(--c-success-bg);color:var(--c-success);margin-bottom:1rem">{ic('tick', 'icon--lg')}</span>
 <h1>Recebemos seu pedido de orçamento</h1><p class="lead">Obrigado pelo contato. Enviamos uma cópia do pedido para o seu e-mail.</p>
 <p class="alert alert--info" data-se-rapido hidden>Quer detalhar mais? Complete seu pedido no formulário completo. <a href="/contato/">Completar meu pedido</a></p></div></div></div></section>
<section class="sec sec--flush-top" id="ob-02"><div class="container"><div class="split split--top">
 <div class="light"><h2>O que acontece agora</h2>{passos_lista(passos)}</div>
 <div class="cta-card on-dark"><h2>Quer adiantar? Envie os arquivos pelo WhatsApp</h2><p>Plantas, implantação ou o link da pasta: mande pelo WhatsApp e juntamos ao seu pedido.</p>{btns(('Enviar arquivos pelo WhatsApp', wa(WA['obrigado']), 'wa-light'))}</div>
</div>
<div class="btn-row" style="margin-top:3rem"><a class="btn btn--secondary" href="/projetos/">Ver projetos</a>{pdf}<a class="link-arrow" href="/">Voltar para o início {ARW}</a></div></div></section>'''
    pub('/obrigado/', documento('/obrigado/', 'Pedido recebido | Intrépida Engenharia',
        'Recebemos seu pedido de orçamento. Veja os próximos passos e, se quiser, adiante o envio dos arquivos do projeto pelo WhatsApp.',
        body, wa_msg=WA['obrigado'], noindex=True, sem_c20=True))

def erro404():
    cards = [('Serviços', 'As nove disciplinas que projetamos.', '/servicos/', 'bim', ''), ('Projetos', 'Os 18 empreendimentos do nosso portfólio.', '/projetos/', 'building', ''),
             ('Solicitar orçamento', 'Conte sobre o seu empreendimento.', '/contato/', 'doc', ' c07-card--primary')]
    body = f'''<section class="c04-hero c04-hero--noimg" id="404-02"><div class="container"><div class="c04-hero__grid"><div class="c04-hero__txt">
 <p class="erro-num" aria-hidden="true">404</p><h1>Página não encontrada</h1><p class="lead">O endereço pode ter mudado com o novo site da Intrépida. Escolha um dos caminhos abaixo.</p></div></div></div></section>
<section class="sec sec--flush-top atalhos" id="404-03"><div class="container"><div class="grid grid--3">
 {''.join(f'<a class="c07-card{c}" href="{u}"><span class="ico">{ic(i, "icon--lg")}</span><h2>{e(t)}</h2><p>{e(x)}</p><span class="link-arrow" aria-hidden="true">Acessar {ARW}</span></a>' for t, x, u, i, c in cards)}</div>
 <div class="btn-row" style="margin-top:2rem"><a class="link-arrow" href="/">Voltar para o início {ARW}</a>{btns(('Falar no WhatsApp', wa(WA['404']), 'wa'), stack=False)}</div></div></section>'''
    escrever('404.html', documento('/404', 'Página não encontrada | Intrépida Engenharia', '', body, wa_msg=WA['404'], noindex=True)); PAGINAS.append('/404.html')

def pend(t): return f'<mark class="pendente" title="Dado a confirmar com o cliente">[{e(t)}]</mark>'
def politica():
    bc, ldbc = breadcrumb([('Política de privacidade', None)])
    rs = e(DADOS['razao_social']) if DADOS['razao_social'] else pend('razão social')
    cnpj = e(DADOS['cnpj']) if DADOS['cnpj'] else pend('CNPJ')
    sumario = ['Quem somos', 'Quais dados coletamos', 'Para que usamos os dados', 'Bases legais', 'Com quem compartilhamos', 'Cookies', 'Por quanto tempo guardamos', 'Como protegemos', 'Seus direitos', 'Contato do encarregado', 'Alterações']
    ul = lambda xs: '<ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>'
    S = [
     f'<p>Esta política explica como a {rs}, inscrita no CNPJ {cnpj}, com sede na Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910 ("Intrépida", "nós"), trata os dados pessoais de quem usa o site intrepidaengenharia.com.br, conforme a Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018, LGPD). A Intrépida é a controladora desses dados.</p>',
     ul(['<strong>Dados que você nos envia pelos formulários:</strong> nome, e-mail, telefone ou WhatsApp, empresa, cargo, cidade e estado do empreendimento, informações sobre o projeto e, se você quiser, arquivos ou links de arquivos.',
         '<strong>Dados de contato direto:</strong> o que você nos enviar por WhatsApp, telefone ou e-mail.',
         f'<strong>Dados de navegação:</strong> com o seu consentimento, informações como páginas visitadas, tempo de visita, tipo de dispositivo, navegador, cidade aproximada e origem do acesso, coletadas por cookies de medição. {pend("confirmar as ferramentas: Google Analytics 4, Google Tag Manager, outras")}',
         f'<strong>Dados técnicos de segurança:</strong> endereço IP e dados do navegador usados pela proteção contra spam dos formulários. {pend("reCAPTCHA ou Turnstile")}'])
     + '<p>Não pedimos dados sensíveis. Pedimos que os arquivos de projeto não contenham dados pessoais de terceiros além do necessário.</p>',
     ul(['Responder ao seu pedido e preparar o orçamento e a proposta.', 'Falar com você sobre o projeto, por e-mail, telefone ou WhatsApp.', 'Cumprir obrigações legais e regulatórias.',
         'Medir o uso do site e melhorar o conteúdo, de forma agregada, se você aceitar os cookies de medição.', 'Proteger o site contra spam e uso indevido.',
         f'Enviar novidades por e-mail, só se você marcar essa opção. {pend("manter só se houver comunicação")}']),
     ul(['<strong>Procedimentos preliminares a um contrato, a seu pedido</strong> (art. 7º, V, da LGPD): orçamento e proposta.',
         '<strong>Consentimento</strong> (art. 7º, I): cookies de medição e envio de novidades. Você pode retirar o consentimento quando quiser.',
         '<strong>Legítimo interesse</strong> (art. 7º, IX): segurança do site e prevenção de fraude e spam.',
         '<strong>Cumprimento de obrigação legal ou regulatória</strong> (art. 7º, II), quando aplicável.']),
     '<p>Não vendemos nem alugamos dados pessoais. Compartilhamos apenas com fornecedores que nos ajudam a operar o site e o atendimento, e só no necessário:</p>'
     + ul([f'hospedagem do site e serviço de e-mail {pend("fornecedores")};', f'ferramentas de medição e de proteção contra spam {pend("Google e outros")};', 'WhatsApp (Meta), quando você escolhe falar conosco por lá;', 'autoridades públicas, quando a lei exigir.'])
     + '<p>Alguns desses fornecedores podem armazenar dados fora do Brasil. Nesses casos, a transferência segue as regras do art. 33 da LGPD.</p>',
     ul(['<strong>Necessários:</strong> fazem o site e os formulários funcionarem. Não dependem de consentimento.', '<strong>Medição:</strong> contam visitas e cliques de forma agregada. Só são ativados se você aceitar no aviso de cookies.'])
     + '<p>Você pode mudar a sua escolha a qualquer momento em "Preferências de cookies", no rodapé do site, ou nas configurações do seu navegador.</p>',
     ul([f'Pedidos de orçamento que não viram contrato: {pend("prazo, ex. até 2 anos")} após o último contato.', 'Dados de clientes: pelo tempo do contrato e pelos prazos exigidos em lei.',
         f'Dados de navegação: pelo prazo configurado na ferramenta de medição {pend("ex. 14 meses")}.']) + '<p>Depois disso, os dados são apagados ou tornados anônimos.</p>',
     '<p>Usamos conexão segura (HTTPS), acesso restrito aos dados e fornecedores com práticas de segurança reconhecidas. Nenhum sistema é totalmente imune a falhas; se houver um incidente que traga risco a você, avisaremos você e a Autoridade Nacional de Proteção de Dados (ANPD), como manda a lei.</p>',
     '<p>Pela LGPD (art. 18), você pode pedir, a qualquer momento:</p>' + ul(['confirmação de que tratamos seus dados e acesso a eles;', 'correção de dados incompletos ou desatualizados;', 'anonimização, bloqueio ou eliminação de dados desnecessários;', 'portabilidade;', 'informação sobre com quem compartilhamos;', 'revogação do consentimento e eliminação dos dados tratados com base nele.'])
     + f'<p>Para isso, escreva para o contato da seção 10. Respondemos {pend("prazo, ex. em até 15 dias")}. Você também pode reclamar à ANPD.</p>',
     f'<p>Encarregado pelo tratamento de dados: {pend("nome")}<br>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a><br>Endereço: Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910.</p>',
     '<p>Podemos atualizar esta política. A data da última versão fica sempre no topo da página.</p>']
    secs = ''.join(f'<h2 id="p{k + 1}">{k + 1}. {t}</h2>{S[k]}' for k, t in enumerate(sumario))
    body = f'''{bc}<section class="sec" id="pp-politica" style="padding-top:2rem"><div class="container"><article class="legal">
 <!-- MINUTA — VALIDAR COM O CLIENTE/JURÍDICO antes de publicar. Trechos marcados em amarelo dependem do cliente. -->
 <h1>Política de privacidade</h1><p class="nota">Última atualização: {pend('data da publicação')}</p>
 <nav class="sumario" aria-label="Sumário"><ol>{''.join(f'<li><a href="#p{k + 1}">{t}</a></li>' for k, t in enumerate(sumario))}</ol></nav>
 {secs}
 <p style="margin-top:3rem"><a class="link-arrow" href="/contato/">Dúvidas sobre seus dados? Fale com a gente. {ARW}</a></p></article></div></section>'''
    pub('/politica-de-privacidade/', documento('/politica-de-privacidade/', 'Política de privacidade | Intrépida Engenharia',
        'Como a Intrépida Engenharia e Projetos coleta, usa e protege os dados enviados pelo site, e como exercer os seus direitos pela LGPD.', body, lds=[ldbc]))

# =====================================================================
def extras():
    (SITE / 'site.webmanifest').write_text(json.dumps({'name': 'Intrépida Engenharia e Projetos', 'short_name': 'Intrépida', 'lang': 'pt-BR',
        'icons': [{'src': '/assets/img/marca/icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/assets/img/marca/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}],
        'theme_color': '#0B3859', 'background_color': '#ffffff', 'display': 'browser'}, ensure_ascii=False, indent=1))
    (SITE / 'robots.txt').write_text(f'User-agent: *\nDisallow: /obrigado/\nDisallow: /_build/\nSitemap: {DOMINIO}/sitemap.xml\n')
    urls = [p for p in PAGINAS if p not in ('/obrigado/', '/404.html')]
    (SITE / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{DOMINIO}{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    (SITE / '_redirects-301.txt').write_text('/quem-somos/ /sobre/ 301\n/trabalhos-desenvolvidos/ /projetos/ 301\n/nossos-clientes/ /projetos/#clientes 301\n')

if __name__ == '__main__':
    home(); hub()
    for d in SERV: servico(d)
    bim(); projetos()
    for i, p in enumerate(PROJ): projeto(i, p)
    sobre(); contato(); obrigado(); erro404(); politica(); extras()
    print(len(PAGINAS), 'páginas geradas')
