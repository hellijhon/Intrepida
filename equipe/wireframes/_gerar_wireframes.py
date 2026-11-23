#!/usr/bin/env python3
"""Gera os wireframes HTML de baixa fidelidade da Intrépida em equipe/wireframes/."""
import os, sys

OUT = sys.argv[1]
OB = "obras-empreendimentos/portfolio-2024_"
BIM = "bim-modelos-3d/portfolio-2024_"

PAGES = [
    ("index.html", "Índice"),
    ("home.html", "Home"),
    ("servicos.html", "Serviços (hub)"),
    ("servico-modelo.html", "Serviço individual (modelo)"),
    ("bim.html", "BIM e Compatibilização"),
    ("projetos.html", "Projetos (listagem)"),
    ("projeto-modelo.html", "Projeto individual (modelo)"),
    ("sobre.html", "Sobre"),
    ("contato.html", "Contato e orçamento"),
    ("obrigado.html", "Obrigado (pós-envio)"),
    ("404.html", "404"),
]

SERV = {
    "Instalações prediais": ["Hidrossanitário", "Elétrica e Sistemas", "Gás", "Climatização HVAC", "Pressurização de escadas", "Piscina"],
    "Infraestrutura urbana": ["Infraestrutura de saneamento"],
    "Eficiência e sustentabilidade": ["Reuso de água pluvial", "Aquecimento solar"],
}

PROJ = [
    ("Mirante São Lucas", "UNENCO", "Belo Horizonte/MG", "152", OB + "p08_mirante-sao-lucas_UNENCO_bh-MG_4096x2304.jpeg"),
    ("Bosque dos Ipês", "RNI", "Campo Grande/MS", "142", OB + "p08_bosque-dos-ipes_RNI_campo-grande-MS_4000x2250.jpeg"),
    ("Residencial Pacífico", "Vila Construtora", "Ribeirão das Neves/MG", "160", OB + "p13_residencial-pacifico_VILA_ribeirao-das-neves-MG_4000x3000.jpeg"),
    ("Parque Lagoa dos Príncipes e Lagoa Nova", "MRV", "Lagoa Santa/MG", "256", OB + "p09_parque-lagoa-dos-principes-lagoa-nova_MRV_lagoa-santa-MG_1920x1280.jpeg"),
    ("Residencial Alta Vista", "Quartzo", "Barueri/SP", "240", OB + "p11_residencial-alta-vista_QUARTZO_barueri-SP_1920x1080.jpeg"),
    ("Residencial Monte Carlo", "Habit Construtora", "Cabo Frio/RJ", "1.800", OB + "p09_residencial-monte-carlo_HABIT_cabo-frio-RJ_960x720.jpeg"),
    ("Residencial Vila Atlântico", "Erglares", "Sabará/MG", "240", OB + "p10_residencial-vila-atlantico_ERGLARES_sabara-MG_1034x704.jpeg"),
    ("Residencial Vila Maria", "Mello Azevedo", "Lagoa Santa/MG", "356", OB + "p10_residencial-vila-maria_MELLO-AZEVEDO_lagoa-santa-MG_1280x718.jpeg"),
    ("Residencial Ville Luxemburgo", "Precon", "Lagoa Santa/MG", "368", OB + "p11_residencial-ville-luxemburgo_PRECON_lagoa-santa-MG_640x480.jpeg"),
    ("Residencial Portal do Cerrado", "Quartzo", "Uberlândia/MG", "192", OB + "p12_residencial-portal-do-cerrado_QUARTZO_uberlandia-MG_960x540.jpeg"),
    ("Residencial Scharle", "UNENCO", "Sabará/MG", "240", OB + "p12_residencial-scharle_UNENCO_sabara-MG_800x600.jpeg"),
    ("Residencial Portal do Engenho", "Prix Construtora", "Itaúna/MG", "208", OB + "p13_residencial-portal-do-engenho_PRIX_itauna-MG_1334x1000.jpeg"),
    ("Alto Boa Vista", "Prix Engenharia", "Belo Horizonte/MG", "236 [conferir]", None),
    ("Gran Vic Gama", "VIC", "Brasília/DF", "236 [conferir]", None),
    ("Alto Riviera", "Prix Engenharia", "Belo Horizonte/MG", "157", None),
    ("Smart Haus", "RNI", "Blumenau/SC", "333", None),
    ("Alto Sobradinho", "Direcional Engenharia", "Sobradinho/DF", "344", None),
    ("California Residence", "Vitta", "Marília/SP", "214", None),
]

LOGOS12 = ["MRV", "Direcional", "Tenda", "Patrimar", "RNI", "Precon", "VIC", "Prix", "UNENCO", "Quartzo", "Mello Azevedo", "Vitta"]
LOGOS24 = ["Precon", "MRV", "Direcional", "Tenda", "Riva", "RNI", "VIC", "Patrimar", "Novolar", "Quartzo", "Erglares", "RRX",
           "Prix", "Mello Azevedo", "Vitta", "MCP", "CTE", "Gabbai", "Unenco", "BRZ", "Vila", "Chandon", "Center Norte", "Catagua"]


# ---------- helpers ----------
def img(cap, r="r169", extra=""):
    return f'<div class="img {r} {extra}" role="img" aria-label="Imagem: {cap}"><span>{cap}</span></div>'

def note(mobile=None, asset=None, other=None):
    p = []
    if mobile: p.append(f"<b>Mobile:</b> {mobile}")
    if asset: p.append(f"<b>Asset:</b> {asset}")
    if other: p.append(other)
    return '<div class="note">' + "<br>".join(p) + "</div>"

def sec(code, name, inner, cls="", cond=False, sid=""):
    if 'class="hero-bg' in inner:
        cls = (cls + " hero-s").strip()
    c = " cond" if cond else ""
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="s {cls}"{idattr}><div class="wrap"><span class="tag{c}">{code} · {name}</span>{inner}</div></section>\n'

def h(level, text, ph=True):
    cls = ' class="ph"' if False else ""
    return f'<h{level}><span class="hl">H{level}</span>{text}</h{level}>'

def btns(*items):
    out = []
    for kind, label, href in items:
        out.append(f'<a class="btn {kind}" href="{href}">{label}</a>')
    return '<div class="btns">' + "".join(out) + "</div>"

def lines(n=3):
    return '<div class="lines" aria-hidden="true">' + "<span></span>" * n + "</div>"

def logos(names, cls="g6"):
    return f'<div class="{cls}">' + "".join(f'<div class="logo">[logo] {n}</div>' for n in names) + "</div>"

def pcard(p, level=3, tags=True, hide=False):
    name, cli, loc, un, asset = p
    cap = ("ASSET: " + asset.split("/")[-1]) if asset else "SEM FOTO — variante sem imagem (PEDIR foto ao cliente)"
    hcls = ' hide-m' if hide else ''
    t = '<div class="tags"><span class="chip">[disciplina]</span><span class="chip">[disciplina]</span><span class="chip">[+1]</span></div>' if tags else ''
    return (f'<a class="card link-card{hcls}" href="projeto-modelo.html">{img(cap, "r43")}'
            f'<h{level}><span class="hl">H{level}</span>{name}</h{level}>'
            f'<p class="meta">{cli} · {loc} · {un} unidades</p>{t}</a>')

def steps():
    s = ["Briefing e análise dos arquivos", "Proposta com escopo e prazo", "Modelagem BIM e cálculo",
         "Compatibilização e aprovação nas concessionárias", "Entrega e acompanhamento de obra"]
    return '<div class="steps">' + "".join(f'<div class="step"><h3>[Etapa: {x}]</h3><p class="ph small">[1 frase] [A CONFIRMAR]</p></div>' for x in s) + "</div>"

def faq(qs, open_first=True):
    out = []
    for i, q in enumerate(qs):
        o = " open" if (i == 0 and open_first) else ""
        out.append(f'<details{o}><summary>{q}</summary><div><p class="ph">[Resposta curta, 2–4 frases]</p></div></details>')
    return "".join(out)

def stats():
    items = [("[18+]", "empreendimentos [A CONFIRMAR total]"), ("[~5.870]", "unidades projetadas [A CONFIRMAR]"),
             ("6", "estados atendidos"), ("24", "construtoras e incorporadoras"), ("[X]", "anos de mercado [A CONFIRMAR]")]
    return '<div class="stats">' + "".join(
        f'<div class="stat"><div class="num">{n}</div><div class="small">{l}</div></div>' for n, l in items) + "</div>"

def cta_final(code, title, with_form=False, pdf=False, form_title="C21b formulário curto"):
    left = (f'{h(2, title)}<p class="ph">[Subtítulo: o que acontece depois do contato; retorno em X dias úteis — A CONFIRMAR]</p>'
            + btns(("pri", "[Solicitar orçamento]", "contato.html"), ("", "[Falar no WhatsApp]", "#")))
    if pdf:
        left += '<p><a class="link" href="#">[Baixar portfólio (PDF)] — A CONFIRMAR</a></p>'
    if with_form:
        left = (f'{h(2, title)}<ul class="plain ph"><li>[O que acontece depois 1]</li><li>[2 — retorno em X dias úteis, A CONFIRMAR]</li><li>[3]</li></ul>'
                '<p><a class="link" href="#">Prefere WhatsApp? [Falar agora]</a></p>'
                + ('<p><a class="btn sm" href="#">[Baixar portfólio (PDF)] — A CONFIRMAR</a></p>' if pdf else ''))
        form = short_form()
        inner = f'<div class="g55" style="align-items:start"><div>{left}</div>{form}</div>'
    else:
        centered = left.replace('class="btns"', 'class="btns" style="justify-content:center"')
        inner = '<div class="center" style="max-width:720px;margin:0 auto">' + centered + '</div>'
    return inner

def field(label, req=True, kind="input", help=None, ph=""):
    r = '<span class="req"> *</span>' if req else ' <span class="opt">(opcional)</span>'
    hp = f'<span class="help">{help}</span>' if help else ''
    if kind == "textarea":
        ctl = f'<textarea class="input" disabled placeholder="{ph}"></textarea>'
    elif kind == "select":
        ctl = f'<div class="input">{ph or "Selecione ▾"}</div>'
    else:
        ctl = f'<div class="input">{ph}</div>'
    return f'<div class="field"><span class="lbl">{label}{r}</span>{ctl}{hp}</div>'

def short_form():
    return ('<div class="form" aria-label="Formulário curto"><p class="small"><b>C21b · Formulário curto</b></p>'
            + field("Nome") + '<div class="row2 eq">' + field("E-mail") + field("WhatsApp", ph="(31) 9____-____") + '</div>'
            + '<div class="row2 eq">' + field("Empresa", req=False) + field("Cidade/UF do empreendimento", req=False) + '</div>'
            + field("Mensagem", req=False, kind="textarea")
            + '<div class="cb">Concordo com a [Política de privacidade] *</div>'
            + '<div class="btns"><span class="btn pri" style="width:100%">[Solicitar orçamento]</span></div>'
            + '<p class="small ph" style="margin-top:8px">Ocultos: servico, origem, honeypot. Envia para /obrigado/.</p></div>')


# ---------- moldura ----------
NAV = [("Serviços", "servicos.html"), ("BIM", "bim.html"), ("Projetos", "projetos.html"), ("Sobre", "sobre.html"), ("Contato", "contato.html")]

def header(active):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if label == active else ''
        if label == "Serviços":
            cols = "".join(f'<div><b>{g}</b>' + "".join(f'<a href="servico-modelo.html">{s}</a>' for s in ss) + "</div>" for g, ss in SERV.items())
            items.append(f'<li class="has-sub"><a href="{href}"{cur} aria-haspopup="true">Serviços ▾</a><div class="mega">{cols}'
                         '<div class="foot"><a href="servicos.html">Ver todos os serviços →</a><a href="bim.html">BIM e compatibilização →</a></div></div></li>')
        else:
            items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    drawer_serv = "".join(f'<div><p class="small" style="margin:8px 0 0 16px"><b>{g}</b></p>' + "".join(f'<a href="servico-modelo.html">{s}</a>' for s in ss) + "</div>" for g, ss in SERV.items())
    drawer_links = "".join(f'<a class="item" href="{href}">{l}</a>' for l, href in NAV[1:])
    return f'''<header class="hdr"><div class="wrap">
<a class="logo-ph" href="home.html">[LOGO INTRÉPIDA horizontal]</a>
<nav class="nav" aria-label="Menu principal"><ul>{"".join(items)}</ul></nav>
<div class="hdr-cta"><a class="wa-ico" href="#" aria-label="WhatsApp">WA</a><a class="btn pri sm" href="contato.html">[Solicitar orçamento]</a></div>
<button class="burger" id="open-menu" aria-expanded="false" aria-controls="drawer" aria-label="Abrir menu">☰</button>
</div></header>
<div class="drawer" id="drawer" aria-hidden="true" role="dialog" aria-label="Menu">
<div class="top"><span class="logo-ph">[LOGO]</span><button class="burger" id="close-menu" aria-label="Fechar menu">✕</button></div>
<details><summary>Serviços ▾</summary>{drawer_serv}<a href="servicos.html"><b>Ver todos os serviços →</b></a></details>
{drawer_links}
<a class="btn pri" href="contato.html">[Solicitar orçamento]</a>
<div class="contacts"><a href="#">WhatsApp</a><a href="#">Ligar</a><a href="#">E-mail</a></div>
<div class="note"><b>C01 mobile:</b> drawer em tela cheia; foco preso; Esc fecha; itens ≥ 48 px; fechar com ícone (não texto).</div>
</div>
'''

def crumb(parts):
    full = " › ".join(parts)
    short = "‹ " + parts[-2] if len(parts) > 1 else parts[0]
    return f'<nav class="crumb" aria-label="Breadcrumb"><div class="wrap"><span class="tag" style="margin:0 8px 0 0">C14</span><span class="full">{full}</span><span class="short">{short}</span></div></nav>'

def footer():
    serv = "".join(f'<a href="servico-modelo.html">{s}</a>' for ss in SERV.values() for s in ss) + '<a href="bim.html">BIM e compatibilização</a>'
    return f'''<footer class="ftr"><div class="wrap"><span class="tag" style="background:#fff;color:#222">C02 · Rodapé</span>
<div class="cols">
<div class="o1"><span class="logo-ph" style="border-color:#eee">[LOGO branco]</span><p class="small" style="margin-top:12px">[Texto: posicionamento em 1 frase]</p><a href="#">[LinkedIn — A CONFIRMAR URL]</a><a class="btn sm" style="color:#eee;border-color:#eee;background:transparent;display:inline-flex;line-height:1.2" href="#">[Baixar portfólio (PDF)]</a></div>
<details class="f-acc o3" open><summary>Serviços</summary><div>{serv}</div></details>
<details class="f-acc o4" open><summary>Institucional</summary><div><a href="projetos.html">Projetos</a><a href="projetos.html#clientes">Clientes</a><a href="sobre.html">Sobre</a><a href="contato.html">Contato</a><a href="#">Política de privacidade</a></div></details>
<div class="o2"><b>Contato</b><a href="#">WhatsApp (31) 99649-8629</a><a href="#">Tel. (31) 3070-6568</a><a href="#">[E-mail — A CONFIRMAR]</a><p class="small">[Endereço — A CONFIRMAR: Goitacazes 103 ou Espírito Santo 1100]<br>[Horário — A CONFIRMAR]</p></div>
</div>
<div class="bottom">© 2026 [Razão social — A CONFIRMAR] · CNPJ [A CONFIRMAR] · CREA [A CONFIRMAR] · Política de privacidade</div>
<div class="note"><b>Mobile:</b> ordem Marca → Contato → Serviços → Institucional; Serviços e Institucional viram accordions fechados; padding inferior extra por causa da barra fixa C20.</div>
</div></footer>
'''

def page(fn, title, active, body, crumbs=None, fl=True, mb=True, desc=""):
    nav = " · ".join(f'<a href="{f}">{t}</a>' for f, t in PAGES[1:])
    fixed = ""
    if fl:
        fixed += '<a class="wa-float" href="#" aria-label="WhatsApp">C19 WA</a>'
    if mb:
        fixed += '<div class="mbar hidden" aria-label="Ações fixas"><span class="mbar-tag">C20 barra fixa mobile</span><a class="btn pri" href="contato.html">[Solicitar orçamento]</a><a class="btn" href="#">WhatsApp</a></div>'
    cr = crumb(crumbs) if crumbs else ""
    html = f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wireframe · {title} · Intrépida</title><link rel="stylesheet" href="wf.css"></head>
<body><a class="skip" href="#main">Pular para o conteúdo</a>
<div class="wfbar"><span><b>WIREFRAME</b> baixa fidelidade · {title}{(" · " + desc) if desc else ""}</span><span><a href="index.html">← Índice</a> &nbsp; <button id="toggle-notes" type="button">Ocultar notas</button></span></div>
{header(active)}{cr}
<main id="main">
{body}
</main>
{footer()}{fixed}
<script src="wf.js"></script></body></html>
'''
    with open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)


# ---------- HOME ----------
def home():
    b = ""
    hero = (f'<div class="hero-bg">{img("ASSET: " + OB + "p08_mirante-sao-lucas_UNENCO_bh-MG_4096x2304.jpeg (hero, LCP)", "r169")}'
            f'<div class="overlay"><p class="eyebrow">[Rótulo: projetos de instalações e infraestrutura]</p>'
            f'{h(1, "[Título: promessa principal — serviço + público, até 10 palavras]")}'
            f'<p class="ph">[Subtítulo: benefício — prazo, aprovação em concessionárias, sem retrabalho; até 25 palavras]</p>'
            + btns(("pri", "[Solicitar orçamento]", "contato.html"), ("", "[Falar no WhatsApp]", "#"))
            + '<p class="small ph" style="margin-top:12px">[Microprova: 24 construtoras atendidas em 6 estados — números A CONFIRMAR]</p></div></div>')
    b += sec("H-02", "Hero · C03", hero + note(
        "foto como fundo, bloco de texto com sobreposição escura na base; H1 em até 4 linhas; botões largura total, orçamento em cima; CTA visível sem rolar em 375×667. Barra C20 só aparece depois que o hero sai da tela.",
        "Mirante São Lucas (BH). Alternativa: " + OB + "p13_residencial-pacifico_…_4000x3000.jpeg. Crédito discreto da foto. [A CONFIRMAR direito de uso]",
        "<b>Desktop:</b> foto em largura total, bloco de texto com sobreposição escura à esquerda, ~85vh (máx. 760 px)."))
    b += sec("H-03", "Barra de números · C05", stats() + note(
        "grade 2×2 (5º item em linha inteira). Contador animado opcional, respeitando prefers-reduced-motion.", None,
        "<b>Regra:</b> item sem confirmação sai; mínimo 3 itens."), cls="alt")
    b += sec("H-04", "Logos de clientes · C06 (12)", h(2, "[Título: quem já confia na Intrépida]") + logos(LOGOS12)
             + '<p style="margin-top:12px"><a class="link" href="projetos.html#clientes">Ver todos os clientes e projetos →</a></p>' + note(
        "grade 3×4, logos com altura máx. 40 px. Sem carrossel automático.",
        "marca/logos-clientes/*.jpeg só como referência (fundo preto). PEDIR PNG/SVG ou redesenhar monocromático. alt = nome do cliente. [A CONFIRMAR autorização]"))
    groups = ""
    for g, ss in SERV.items():
        items = "".join(f'<li><span class="icon"></span><div><b>{s}</b><div class="small ph hide-m">[Descrição 8–12 palavras]</div><a class="small" href="servico-modelo.html">Saiba mais →</a></div></li>' for s in ss)
        groups += f'<div class="card">{h(3, g)}<ul class="ilist">{items}</ul></div>'
    b += sec("H-05", "Serviços · C07 agrupado", h(2, "[Título: o que projetamos]") + '<p class="ph">[Intro de 1 linha]</p>'
             + f'<div class="g3">{groups}</div>'
             + '<div class="card" style="margin-top:16px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between"><b>[Faixa: BIM e compatibilização em todas as disciplinas]</b><a class="btn sm" href="bim.html">Conheça →</a></div>'
             + '<p><a class="link" href="servicos.html">Ver todos os serviços</a></p>'
             + note("grupos empilhados; lista compacta (ícone 32 px + nome + seta); descrição some.", "Ícones: REDESENHAR em SVG (os do portfólio são de estilo antigo)."), cls="alt")
    conc = (f'<div class="g55"><div>{h(2, "[Título: dor — atraso de aprovação em concessionárias]")}'
            '<p class="ph">[Texto: projetista calculista desde o estudo de viabilidade evita reprovações e retrabalho]</p>'
            '<ul class="ilist"><li><span class="icon"></span><div class="ph">[Benefício 1: aprovação de primeira]</div></li><li><span class="icon"></span><div class="ph">[Benefício 2: normas atendidas]</div></li><li><span class="icon"></span><div class="ph">[Benefício 3: prazo previsível]</div></li></ul>'
            '<div class="tags" style="margin-top:16px"><span class="chip">[COPASA]</span><span class="chip">[CEMIG]</span><span class="chip">[Gasmig]</span><span class="chip">[outras — A CONFIRMAR]</span></div>'
            + btns(("pri", "[Envie seu projeto para análise]", "contato.html")) + f'</div>{img("ASSET: " + OB + "p08_bosque-dos-ipes_RNI_campo-grande-MS_4000x2250.jpeg (em obra)", "r43")}</div>')
    b += sec("H-06", "Aprovação em concessionárias · C18", conc + note(
        "foto 16:9 em cima, texto e CTA em largura total abaixo.", None, "Corrige o CTA morto do site antigo (apontava para #)."), cls="dark")
    gal = '<div class="scroller">' + "".join(img(f"ASSET: {BIM}{x}", "r11") for x in [
        "p03_bim-hidrossanitario-a_2438x3128.jpeg", "p06_bim-quadro-eletrico_4096x3068.jpeg", "p05_bim-a_3660x4096.jpeg", "p06_bim-tubulacao-gas-ou-hidraulica_4096x3291.jpeg"]) + "</div>"
    bim = (f'<div class="g46"><div>{h(2, "[Título: BIM que evita conflito na obra]")}<p class="ph">[2–3 frases: modelagem 3D, compatibilização, menos retrabalho]</p>'
           '<ul class="plain ph"><li>[Benefício 1]</li><li>[Benefício 2]</li><li>[Benefício 3]</li></ul>'
           '<a class="link" href="bim.html">Conheça nosso processo BIM →</a></div><div>' + gal + '<p class="lightbox-note">Clique abre lightbox (C11). Legenda por imagem: [A CONFIRMAR disciplina].</p></div></div>')
    b += sec("H-07", "BIM e compatibilização · C09 + C11", bim + note(
        "texto → carrossel horizontal com scroll-snap (1,2 imagem visível, controle manual) → CTA.", "4 das 8 imagens reais de equipe/fotos/bim-modelos-3d/ (fundo branco)."))
    cards = "".join(pcard(p, hide=(i >= 3)) for i, p in enumerate(PROJ[:6]))
    b += sec("H-08", "Projetos em destaque · C08 (6)", '<div style="display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;align-items:baseline">' + h(2, "[Título: empreendimentos que já projetamos]") + '<a class="link" href="projetos.html">Ver todos os projetos</a></div>'
             + f'<div class="g3">{cards}</div><div class="only-m">' + btns(("", "Ver todos os 18 projetos", "projetos.html")) + "</div>"
             + note("1 coluna com os 3 primeiros + botão “Ver todos os 18 projetos”. Card inteiro clicável.",
                    "12 fotos reais; Monte Carlo (960×720) só em card pequeno.", "<b>Tags de disciplina:</b> [A CONFIRMAR por projeto]; sem dado → tags ocultas."), cls="alt")
    b += sec("H-09", "Como trabalhamos · C10", h(2, "[Título: processo]") + steps()
             + '<p class="small ph" style="margin-top:16px">[Nota de prazo: proposta em até X dias úteis — A CONFIRMAR]</p>'
             + note("lista vertical com linha/numeração à esquerda.", None, "<b>Etapas:</b> sugestão; validar com o cliente."))
    rt = (f'<div class="g46"><div>{img("FOTOGRAFAR: retrato do RT (não gerar por IA). Sem foto → variante só texto com símbolo da marca", "r34 circle", "")}</div>'
          f'<div>{h(2, "[Título: quem assina os projetos]")}<p><b>Carlos Alberto Grope</b><br>Diretor Técnico · Engenheiro Civil Sanitarista<br>CREA [A CONFIRMAR]</p>'
          '<p class="ph">[2 frases: experiência e atuação direta nos projetos]</p><a class="link" href="sobre.html">Conheça a Intrépida →</a></div></div>')
    b += sec("H-10", "Responsável técnico · C17 compacto", rt.replace('class="img r34 circle "', 'class="img r11 circle" style="max-width:220px;border-radius:50%;margin:0 auto"')
             + note("foto circular 96 px acima do texto, centralizado."), cls="alt")
    dep = '<div class="g3">' + "".join(f'<div class="card"><p class="ph">“[Citação real autorizada]”</p><p class="small"><b>[Nome]</b><br>[Cargo] · [Empresa]</p></div>' for _ in range(3)) + "</div>"
    b += sec("H-11", "Depoimentos · C16 — CONDICIONAL", dep + note("cards empilhados (sem carrossel).", None,
             "<b>Só entra com depoimentos reais autorizados.</b> Sem dado → seção removida inteira. Não inventar."), cond=True)
    b += sec("H-12", "Perguntas frequentes · C12 (objeções P1)", h(2, "[Título: dúvidas de quem contrata]") + faq([
        "[Vocês atendem empreendimentos de grande porte?]", "[Atendem minha cidade/estado?]", "[Qual o prazo de um projeto?] [A CONFIRMAR]",
        "[Trabalham em Revit / no padrão BIM da minha empresa?] [A CONFIRMAR]", "[O que preciso enviar para receber o orçamento?]"])
             + note("largura total; cada pergunta ≥ 48 px de altura.", None, "Schema FAQPage. Primeira aberta por padrão. NOVO em relação ao briefing."), cls="alt")
    b += sec("H-13", "CTA final · C13 + C21b", cta_final("H-13", "[Título: chamada para orçamento]", with_form=True, pdf=True)
             + note("título → formulário → WhatsApp → PDF.", "Fundo: marca/portfolio-2024_fundo-capa_5339x3049.jpeg (textura) ou cor sólida — decisão do designer."), cls="dark")
    page("home.html", "Home", None, b, desc="/")


# ---------- SERVIÇOS HUB ----------
def hub():
    b = ""
    hero = (f'<div class="g55"><div><p class="eyebrow">Serviços</p>{h(1, "[Título: projetos de instalações prediais e infraestrutura — serviço + cidade]")}'
            '<p class="ph">[Subtítulo: 9 disciplinas, 2D e BIM, para incorporadoras, construtoras e arquitetos]</p>'
            + btns(("pri", "[Solicitar orçamento]", "contato.html"), ("", "[WhatsApp]", "#")) + f'</div>{img("ASSET: " + BIM + "p05_bim-a_3660x4096.jpeg (modelo multidisciplinar)", "r43")}</div>')
    b += sec("SH-02", "Hero interno · C04", hero + note("imagem abaixo do texto, recorte 4:3; botões largura total."))
    b += sec("SH-03", "Índice rápido (âncoras)", '<div class="chips">' + "".join(f'<a class="chip" href="#g{i}">{g}</a>' for i, g in enumerate(SERV)) + "</div>"
             + note("chips com rolagem horizontal dentro do bloco (sem rolagem da página)."), cls="alt")
    for i, (g, ss) in enumerate(SERV.items()):
        if i == 1:
            inner = (f'{h(2, g)}<p class="ph">[Intro de 1 frase do grupo]</p><div class="card"><div class="g55">'
                     f'{img("ASSET: " + OB + "p09_parque-lagoa-dos-principes-lagoa-nova_MRV_lagoa-santa-MG_1920x1280.jpeg", "r169")}'
                     f'<div>{h(3, "Infraestrutura de saneamento")}<p class="ph">[Redes de água, esgoto e drenagem; aprovação em concessionárias]</p><a class="link" href="servico-modelo.html">Saiba mais →</a></div></div></div>')
            nt = note("imagem em cima, texto abaixo.", None, "Card largo: grupo com 1 disciplina ganha destaque (diferencial pouco explorado pelos concorrentes).")
        else:
            cards = "".join(f'<a class="card link-card" href="servico-modelo.html"><span class="icon"></span>{h(3, s)}<p class="ph small">[Descrição 2 linhas]</p><span class="small">Saiba mais →</span></a>' for s in ss)
            inner = f'{h(2, g)}<p class="ph">[Intro de 1 frase do grupo]</p><div class="g3">{cards}</div>'
            nt = note("1 coluna, cards compactos (ícone + nome + seta).")
        b += sec(f"SH-0{4 + i}", f"Grupo {i + 1}: {g} · C07", inner + nt, cls="" if i % 2 == 0 else "alt", sid=f"g{i}")
    b += sec("SH-07", "Faixa BIM transversal · C18", f'<div class="g55"><div>{h(2, "[Título: todas as disciplinas em BIM, compatibilizadas]")}<p class="ph">[1–2 frases]</p></div><div>' + btns(("pri", "[Conheça o BIM da Intrépida]", "bim.html")) + "</div></div>" + note("empilhado."), cls="dark")
    b += sec("SH-08", "Não sabe quais projetos precisa? · C09", f'{h(2, "[Título: não sabe quais projetos seu empreendimento precisa?]")}<p class="ph">[Texto curto para arquitetos e proprietários]</p>'
             + btns(("pri", "[Envie a arquitetura que indicamos as disciplinas]", "contato.html?servico=nao-sei")) + note("empilhado; botão largura total.", None, "Leva a /contato/?servico=nao-sei (marca “Ainda não sei”)."), cls="alt")
    b += sec("SH-09", "Como trabalhamos · C10", h(2, "[Título: processo]") + steps() + note("vertical."))
    b += sec("SH-10", "Logos · C06 (12)", logos(LOGOS12) + note("grade 3 colunas."), cls="alt")
    b += sec("SH-11", "CTA final · C13", cta_final("SH-11", "[Título: chamada para orçamento]") + note("botões empilhados."), cls="dark")
    page("servicos.html", "Serviços (hub)", "Serviços", b, ["Início", "Serviços"], desc="/servicos/")


# ---------- SERVIÇO MODELO ----------
def servico():
    b = ""
    hero = (f'<div class="g55"><div><p class="eyebrow">[Grupo: Instalações prediais]</p>{h(1, "[Título: Projeto [disciplina] para [público/cidade]]")}'
            '<p class="ph">[Subtítulo: benefício específico da disciplina, até 25 palavras]</p>'
            + btns(("pri", "[Solicitar orçamento de [disciplina]]", "contato.html?servico=hidrossanitario"), ("", "[WhatsApp]", "#"))
            + f'</div>{img("ASSET por disciplina (ver tabela 7.2). Ex. hidrossanitário: " + BIM + "p03_bim-hidrossanitario-a_2438x3128.jpeg", "r43")}</div>')
    b += sec("SV-02", "Hero interno · C04", hero + note("imagem depois do texto; botões largura total.",
             "Real: hidrossanitário, elétrica, gás [confirmar], aquecimento solar (parcial), saneamento (foto de empreendimento). HVAC, pressurização, piscina [confirmar], reuso: PEDIR modelo BIM ou GERAR ilustração genérica sinalizada.",
             "<b>Link do CTA:</b> /contato/?servico=[slug] — disciplina já marcada no formulário."))
    ent = '<ul class="ilist">' + "".join(f'<li class="check">[Entregável {i}: ex. plantas, memorial de cálculo, detalhes, quantitativos, ART, modelo BIM]</li>' for i in range(1, 7)) + "</ul>"
    b += sec("SV-03", "O que entregamos · C09", f'<div class="g46"><div>{h(2, "[Título: o que entregamos]")}<p class="ph">[1 frase]</p></div>{ent}</div>' + note("lista de 1 coluna.", None, "[A CONFIRMAR entregáveis por disciplina]"), cls="alt")
    cards = "".join(f'<div class="card"><span class="icon"></span>{h(3, t)}<p class="ph small">[Quando esse projeto é exigido e em que fase contratar]</p></div>' for t in ["[Residencial multifamiliar]", "[Loteamento / condomínio]", "[Comercial / residência]"])
    b += sec("SV-04", "Para quem / quando contratar", h(2, "[Título: para quem é / quando contratar]") + f'<div class="g3">{cards}</div>' + note("1 coluna."))
    b += sec("SV-05", "Normas e aprovações · C18", f'<div class="g55"><div>{h(2, "[Título: normas e aprovações]")}<p class="ph">[Texto curto]</p></div><div><p><b>Normas:</b> <span class="ph">[NBRs da disciplina — A CONFIRMAR]</span></p><p><b>Concessionárias/órgãos:</b> <span class="ph">[COPASA, CEMIG, Gasmig, Bombeiros… — A CONFIRMAR]</span></p>' + btns(("", "[Fale com o engenheiro]", "contato.html")) + "</div></div>" + note("empilhado."), cls="dark")
    b += sec("SV-06", "Em BIM · C09 + C11", f'<div class="g55">{img("ASSET: 1–2 imagens BIM da disciplina (ex. " + BIM + "p04_bim-b_3801x4096.jpeg)", "r43")}<div>{h(2, "[Título: projeto em BIM]")}<p class="ph">[2 frases]</p><a class="link" href="bim.html">Como usamos BIM →</a></div></div>' + note("imagem em cima."))
    cards = "".join(pcard(p) for p in PROJ[:3])
    b += sec("SV-07", "Projetos com esta disciplina · C08 — CONDICIONAL", h(2, "[Título: projetos com [disciplina]]") + f'<div class="g3">{cards}</div><p><a class="link" href="projetos.html">Ver todos → /projetos/?disciplina=[slug]</a></p>'
             + note("2 cards + botão.", None, "<b>Condição:</b> ≥ 2 projetos com a disciplina confirmada. Sem dado → trocar por faixa de logos C06."), cls="alt", cond=True)
    b += sec("SV-08", "FAQ da disciplina · C12", h(2, "[Título: perguntas sobre [disciplina]]") + faq(["[O que é um projeto [disciplina] e quando é obrigatório?] (leigo — P4)", "[Quanto tempo leva?]", "[O que preciso enviar?]", "[Vocês acompanham a aprovação?]"]) + note("largura total."))
    others = "".join(f'<a class="chip" href="servico-modelo.html">{s}</a>' for s in SERV["Instalações prediais"][1:])
    b += sec("SV-09", "Outros serviços · C07 simples", h(2, "[Título: outros projetos de instalações prediais]") + f'<div class="tags">{others}</div><p><a class="link" href="servicos.html">Ver todos os serviços</a></p>' + note("lista compacta."), cls="alt")
    b += sec("SV-10", "CTA final · C13 + C21b", cta_final("SV-10", "[Título: orçamento de projeto [disciplina]]", with_form=True) + note("empilhado.", None, "Campo oculto servico=[slug]."), cls="dark")
    page("servico-modelo.html", "Serviço individual (modelo)", "Serviços", b, ["Início", "Serviços", "[Disciplina]"], desc="/servicos/[disciplina]/")


# ---------- BIM ----------
def bimpage():
    b = ""
    hero = (f'<div class="g55"><div><p class="eyebrow">Diferencial</p>{h(1, "[Título: BIM e compatibilização de projetos de instalações]")}'
            '<p class="ph">[Subtítulo: menos conflito na obra, quantitativos precisos]</p>'
            + btns(("pri", "[Solicitar orçamento]", "contato.html?servico=compatibilizacao-bim"), ("", "[Ver galeria ↓]", "#galeria"))
            + f'</div>{img("ASSET: " + BIM + "p05_bim-a_3660x4096.jpeg (fundo branco)", "r43")}</div>')
    b += sec("BM-02", "Hero interno · C04", hero + note("imagem abaixo, altura máx. 320 px."))
    cards = "".join(f'<div class="card"><span class="icon"></span>{h(3, t)}<p class="ph small">[1 frase]</p></div>' for t in ["[Detecção de interferências antes da obra]", "[Quantitativos confiáveis]", "[Aprovação e execução sem retrabalho]", "[Modelo para manutenção e gestão]"])
    b += sec("BM-03", "Benefícios", h(2, "[Título: o que o BIM muda no seu empreendimento]") + f'<div class="g4">{cards}</div>' + note("1 coluna (2×2 em tablet)."), cls="alt")
    b += sec("BM-04", "Como fazemos a compatibilização · C10", h(2, "[Título: como fazemos]") + steps() + note("vertical.", None, "[A CONFIRMAR etapas reais: recebimento dos modelos → modelagem → detecção de conflitos → relatório/reuniões → modelo final]"))
    files = ["p03_bim-hidrossanitario-a_2438x3128.jpeg", "p03_bim-hidrossanitario-b_3349x4096.jpeg", "p04_bim-a_3801x4096.jpeg", "p04_bim-b_3801x4096.jpeg",
             "p05_bim-a_3660x4096.jpeg", "p05_bim-b_2196x3502.jpeg", "p06_bim-quadro-eletrico_4096x3068.jpeg", "p06_bim-tubulacao-gas-ou-hidraulica_4096x3291.jpeg"]
    gal = '<div class="g4 m2">' + "".join(f'<figure style="margin:0">{img("ASSET: " + BIM + f, "r11")}<figcaption class="small ph">[Legenda: disciplina — A CONFIRMAR]</figcaption></figure>' for f in files) + "</div>"
    gal += '<div class="card" style="margin-top:16px;text-align:center"><b>[Slot fase 2: visualizador 3D interativo]</b></div>'
    b += sec("BM-05", "Galeria de modelos · C11 (8 imagens reais)", h(2, "[Título: modelos reais]") + gal + note("grade 2 colunas; lightbox em tela cheia com swipe.", "todas as 8 imagens de equipe/fotos/bim-modelos-3d/.", "Clique abre lightbox com setas e Esc."), cls="alt", sid="galeria")
    tbl = "".join(f'<div class="card"><p class="meta">{k}</p><p class="ph">{v}</p></div>' for k, v in [("Softwares", "[Revit? AltoQi? — A CONFIRMAR]"), ("Formatos de entrega", "[RVT, IFC, DWG, PDF, NWC — A CONFIRMAR]"), ("Nível de detalhe", "[A CONFIRMAR]"), ("Padrão do cliente", "[Trabalhamos no template BIM da sua empresa — A CONFIRMAR]")])
    b += sec("BM-06", "Softwares e formatos · C15", h(2, "[Título: softwares e formatos]") + f'<div class="g4">{tbl}</div>' + note("lista empilhada."))
    b += sec("BM-07", "2D x BIM — OPCIONAL", h(2, "[Título: 2D x BIM na prática]") + '<div class="g2"><div class="card"><h3>2D</h3>' + lines(4) + '</div><div class="card"><h3>BIM</h3>' + lines(4) + "</div></div>" + note("duas listas empilhadas.", None, "Copywriter decide se agrega."), cls="alt", cond=True)
    b += sec("BM-08", "Projetos · C08 (3)", h(2, "[Título: projetos]") + '<div class="g3">' + "".join(pcard(p) for p in PROJ[:3]) + "</div>" + note("1 coluna."))
    b += sec("BM-09", "FAQ BIM · C12", h(2, "[Título: perguntas sobre BIM]") + faq(["[Preciso ter o projeto de arquitetura em BIM?]", "[Vocês compatibilizam com projetos de terceiros?]", "[Quais arquivos recebo?]", "[BIM encarece o projeto?]"]) + note("largura total."), cls="alt")
    b += sec("BM-10", "CTA final · C13", cta_final("BM-10", "[Título: chamada para orçamento BIM]") + note("empilhado."), cls="dark")
    page("bim.html", "BIM e Compatibilização", "BIM", b, ["Início", "BIM e Compatibilização"], desc="/bim-e-compatibilizacao/")


# ---------- PROJETOS ----------
def projetos():
    b = ""
    hero = (f'<div class="hero-bg low">{img("ASSET: " + OB + "p13_residencial-pacifico_VILA_ribeirao-das-neves-MG_4000x3000.jpeg", "r169")}'
            f'<div class="overlay">{h(1, "[Título: projetos de instalações em X empreendimentos]")}<p class="ph">[Subtítulo]</p><a class="link" href="contato.html">Solicitar orçamento</a></div></div>')
    b += sec("PJ-02", "Hero (baixo, ~50vh) · C03", hero.replace("min-height:620px", "") + note("altura ~45vh; H1 em até 3 linhas.", None, "Sem formulário no hero, para não competir com a exploração."))
    b += sec("PJ-03", "Barra de números · C05", stats() + note("2×2."), cls="alt")
    filters = ('<div class="hide-m"><div class="g" style="grid-template-columns:repeat(4,minmax(0,1fr));align-items:end">'
               + field("UF", req=False, kind="select", ph="Todas ▾") + field("Cliente", req=False, kind="select", ph="Todos (com busca) ▾")
               + field("Tipo", req=False, kind="select", ph="Todos ▾ [só se ≥ 2 tipos]") + field("Disciplina", req=False, kind="select", ph="Todas ▾ [se houver dado]")
               + '</div><div class="chips"><span class="chip on">MG ✕</span><span class="chip on">MRV ✕</span><a class="chip" href="#">Limpar filtros</a></div><p class="small"><b>[18] projetos</b></p></div>'
               '<div class="only-m"><button class="btn" id="open-filters" aria-expanded="false" aria-controls="filter-sheet" style="width:100%">[Filtrar (2)]</button>'
               '<div class="chips" style="margin-top:8px"><span class="chip on">MG ✕</span><span class="chip on">MRV ✕</span></div>'
               '<div class="sheet" id="filter-sheet" hidden><b>Bottom sheet de filtros</b>' + field("UF", req=False, kind="select", ph="Todas ▾") + field("Cliente", req=False, kind="select", ph="Todos ▾")
               + '<div class="btns"><span class="btn pri">Ver [X] projetos</span><span class="btn">Limpar</span></div></div><p class="small"><b>[18] projetos</b></p></div>')
    b += sec("PJ-04", "Filtros · C22", filters + note("botão [Filtrar (n)] abre bottom sheet; chips dos filtros ativos abaixo (toque no botão para ver).", None,
             "Filtros refletidos na URL (?uf=mg&amp;cliente=mrv). Estado vazio: “Nenhum projeto com esses filtros” + Limpar + CTA."))
    cards = "".join(pcard(p, level=3) for p in PROJ)
    b += sec("PJ-05", "Grade de projetos · C08 (18)", '<h2 class="skip">Lista de projetos</h2><div class="g3">' + cards + "</div>" + note("1 coluna (2 em tablet).",
             "12 com foto real + 6 sem foto (variante sem imagem até o cliente enviar).", "Sem paginação (18 itens). Destaques primeiro, depois por UF."), cls="alt")
    b += sec("PJ-06", "Clientes (#clientes) · C06 completo (24)", h(2, "[Título: construtoras e incorporadoras atendidas]") + logos(LOGOS24) + note("grade 3 colunas.", "logos de referência; PEDIR PNG/SVG.", "Destino do 301 de /nossos-clientes/."), sid="clientes")
    mapa = f'<div class="g55">{img("CRIAR: SVG do mapa do Brasil com MG, DF, SP, RJ, MS, SC destacados", "r43")}<div><ul class="plain"><li>MG — [n] projetos</li><li>DF — [n]</li><li>SP — [n]</li><li>RJ — [n]</li><li>MS — [n]</li><li>SC — [n]</li></ul><p class="small ph">Clicar numa UF aplica o filtro.</p></div></div>'
    b += sec("PJ-07", "Mapa de atuação · C24 — OPCIONAL", mapa + note("mapa menor + lista de UFs abaixo."), cls="alt", cond=True)
    b += sec("PJ-08", "CTA final · C13", cta_final("PJ-08", "[Título: seu empreendimento pode ser o próximo]") + note("empilhado."), cls="dark")
    page("projetos.html", "Projetos (listagem)", "Projetos", b, ["Início", "Projetos"], desc="/projetos/")


# ---------- PROJETO MODELO ----------
def projeto():
    b = ""
    hero = img("ASSET: foto principal do projeto. Ex.: " + PROJ[0][4] + " (baixa resolução → largura de conteúdo, não tela cheia)", "r169")
    hero += f'<div style="margin-top:16px">{h(1, "[Nome do empreendimento]")}<p class="meta">[Cliente] · [Cidade/UF]</p><p class="small ph">[Crédito da foto — A CONFIRMAR]</p></div>'
    b += sec("PP-02", "Hero do projeto · C03", hero + note("foto 4:3 em cima, H1 abaixo (não sobreposto).", None, "6 projetos sem foto: variante com fundo neutro + nome/cliente/cidade em destaque. Não gerar imagem do empreendimento."))
    ficha = "".join(f'<div style="border-bottom:1px solid #ddd;padding:10px 0"><p class="meta" style="margin:0">{k}</p><p style="margin:0" class="ph">{v}</p></div>' for k, v in [
        ("Cliente", "[logo] [Nome do cliente]"), ("Local", "[Cidade/UF]"), ("Tipo", "[Residencial multifamiliar]"), ("Unidades", "[nº]"),
        ("Área", "[A CONFIRMAR]"), ("Ano", "[A CONFIRMAR]"), ("Formato", "[BIM / 2D — A CONFIRMAR]")])
    ficha += '<div style="padding:10px 0"><p class="meta" style="margin:0 0 6px">Disciplinas projetadas [A CONFIRMAR]</p><div class="tags"><a class="chip" href="servico-modelo.html">[Hidrossanitário]</a><a class="chip" href="servico-modelo.html">[Elétrica]</a><a class="chip" href="servico-modelo.html">[Gás]</a></div></div>'
    side = ('<div class="card sticky-col"><span class="tag">PP-04 · CTA lateral</span>' + h(3, "[Tem um empreendimento parecido?]")
            + '<p class="ph small">[1 frase]</p>' + btns(("pri", "[Solicitar orçamento]", "contato.html?ref=projeto-slug"), ("", "[WhatsApp]", "#")) + "</div>")
    b += sec("PP-03", "Ficha técnica · C15 + PP-04 CTA lateral", f'<div class="g64"><div>{h(2, "[Ficha técnica]")}{ficha}</div>{side}</div>'
             + note("lista de 1 coluna (rótulo acima do valor); o CTA vira botão largura total logo após a ficha.", None, "Campo sem dado = linha oculta (nunca “—” ou “N/D”). Link do CTA: /contato/?ref=projeto-[slug]."), cls="alt")
    b += sec("PP-05", "Desafio e solução · C09 — CONDICIONAL", '<div class="g2"><div>' + h(2, "Desafio") + lines(4) + "</div><div>" + h(2, "Solução") + lines(4) + "</div></div>"
             + note("empilhado.", None, "Só se o cliente fornecer o case. Sem dado → seção oculta."), cond=True)
    b += sec("PP-06", "Galeria · C11 — CONDICIONAL", '<div class="scroller">' + "".join(img(f"[foto/imagem BIM extra {i}]", "r43") for i in range(1, 5)) + "</div>"
             + note("carrossel com swipe.", None, "Hoje há 1 foto por projeto → seção oculta até haver ≥ 2 imagens."), cls="alt", cond=True)
    b += sec("PP-07", "Depoimento do cliente · C16 — CONDICIONAL", '<div class="card"><p class="ph">“[Citação real autorizada]”</p><p class="small"><b>[Nome]</b> · [Cargo] · [Empresa]</p></div>' + note(None, None, "Só com depoimento real autorizado."), cond=True)
    b += sec("PP-08", "Projetos relacionados · C08 (3)", h(2, "[Título: outros projetos em [UF] / de [cliente]]") + '<div class="g3">' + "".join(pcard(p) for p in PROJ[1:4]) + "</div>" + note("1 coluna."), cls="alt")
    b += sec("PP-09", "Anterior / próximo", '<div class="btns" style="justify-content:space-between"><a class="btn" href="#">‹ Projeto anterior</a><a class="btn" href="#">Próximo projeto ›</a></div>' + note("dois botões em largura total."))
    b += sec("PP-10", "CTA final · C13", cta_final("PP-10", "[Título: tem um empreendimento parecido?]") + note("empilhado."), cls="dark")
    page("projeto-modelo.html", "Projeto individual (modelo)", "Projetos", b, ["Início", "Projetos", "[Nome do empreendimento]"], desc="/projetos/[empreendimento]/")


# ---------- SOBRE ----------
def sobre():
    b = ""
    hero = (f'<div class="g55"><div><p class="eyebrow">Sobre</p>{h(1, "[Título: quem somos — engenharia de projetos com atitude]")}<p class="ph">[Subtítulo: posicionamento]</p>'
            + btns(("pri", "[Solicitar orçamento]", "contato.html"), ("", "[Baixar portfólio (PDF)]", "#")) + f'</div>{img("FOTOGRAFAR escritório/equipe. Provisório: " + OB + "p08_bosque-dos-ipes_…_4000x2250.jpeg ou textura marca/portfolio-2024_fundo-capa", "r43")}</div>')
    b += sec("SB-02", "Hero interno · C04", hero + note("imagem abaixo."))
    b += sec("SB-03", "Nossa história · C09", f'<div class="g46"><div>{h(2, "[Título: nossa história]")}</div><div>{lines(5)}<p class="ph small">[A CONFIRMAR: ano de fundação e marcos]</p><div class="steps" style="margin-top:16px"><div class="step"><b>[Ano]</b><p class="ph small">[Marco]</p></div><div class="step"><b>[Ano]</b><p class="ph small">[Marco]</p></div><div class="step"><b>[Ano]</b><p class="ph small">[Marco]</p></div></div></div></div>'
             + note("linha do tempo vertical.", None, "Linha do tempo opcional — só com datas confirmadas."), cls="alt")
    rt = (f'<div class="g46"><div style="max-width:320px">{img("FOTOGRAFAR retrato do RT — não gerar por IA", "r34")}</div><div>{h(2, "[Título: responsável técnico]")}'
          '<p><b>Carlos Alberto Grope</b><br>Diretor Técnico · Engenheiro Civil Sanitarista<br>CREA [A CONFIRMAR]</p>' + lines(4) + '<a class="link" href="#">[LinkedIn pessoal — A CONFIRMAR]</a></div></div>')
    b += sec("SB-04", "Responsável técnico · C17 completo", rt + note("foto em cima."))
    team = '<div class="g4 m2">' + "".join(f'<div class="card">{img("FOTOGRAFAR", "r11")}<b>[Nome]</b><p class="small ph">[Função]</p></div>' for _ in range(4)) + "</div>"
    b += sec("SB-05", "Equipe — CONDICIONAL", h(2, "[Título: equipe]") + team + note("grade 2 colunas.", None, "[A CONFIRMAR quem aparece — ex. “André”]. Sem fotos reais → seção oculta (sem banco de imagens, sem IA)."), cls="alt", cond=True)
    mapa = img("CRIAR: SVG mapa do Brasil com as 6 UFs", "r43")
    b += sec("SB-06", "Números + área de atuação · C05 + C24", stats() + f'<div style="margin-top:24px" class="g55">{mapa}<div>{h(3, "[Título: onde atuamos]")}<p class="ph">MG, DF, SP, RJ, MS, SC · [atendimento remoto — A CONFIRMAR]</p></div></div>' + note("2×2 + mapa."))
    b += sec("SB-07", "Como trabalhamos / valores · C10", h(2, "[Título: como trabalhamos]") + steps() + note("vertical.", None, "Processo (igual à Home) ou 3–4 valores [A CONFIRMAR]."), cls="alt")
    dados = "".join(f'<div style="border-bottom:1px solid #ddd;padding:10px 0"><p class="meta" style="margin:0">{k}</p><p style="margin:0" class="ph">[A CONFIRMAR]</p></div>' for k in ["Razão social", "CNPJ", "CREA da empresa", "Responsável técnico e CREA", "Endereço", "E-mail comercial"])
    b += sec("SB-08", "Dados cadastrais (#dados-cadastrais) · C15", f'<div class="g64"><div>{h(2, "[Título: dados para cadastro de fornecedor]")}{dados}</div><div class="card">{h(3, "[Portfólio]")}<p class="ph small">[1 frase]</p>' + btns(("pri", "[Baixar portfólio (PDF)]", "#")) + '<p class="small ph">[A CONFIRMAR: PDF liberado e atualizado]</p></div></div>'
             + note("lista de 1 coluna; botão largura total.", None, "Para persona P2 (suprimentos). NOVO em relação ao briefing."), sid="dados-cadastrais")
    b += sec("SB-09", "Clientes · C06 (12)", logos(LOGOS12) + '<p><a class="link" href="projetos.html#clientes">Ver todos →</a></p>' + note("3 colunas."), cls="alt")
    b += sec("SB-10", "CTA final · C13", cta_final("SB-10", "[Título: chamada para orçamento]") + note("empilhado."), cls="dark")
    page("sobre.html", "Sobre", "Sobre", b, ["Início", "Sobre"], desc="/sobre/")


# ---------- CONTATO ----------
def contato():
    b = ""
    selos = '<div class="tags"><span class="chip">[Retorno em X dias úteis — A CONFIRMAR]</span><span class="chip">[Atendimento direto com o engenheiro]</span><span class="chip">[Arquivos tratados com sigilo]</span></div>'
    b += sec("CT-02", "Cabeçalho curto · C04 sem imagem", f'{h(1, "[Título: solicite um orçamento]")}<p class="ph">[Subtítulo: o que acontece depois + prazo — A CONFIRMAR]</p>{selos}'
             + '<p class="only-m"><a class="link" href="#canais">Prefere WhatsApp? ↓</a></p>' + note("selos em lista compacta; link-âncora “Prefere WhatsApp? ↓” para os canais.", None, "Sem C19 e sem C20 nesta página."))
    tipos = "".join(f'<div class="rc">{t}</div>' for t in ["Residencial multifamiliar", "Loteamento / condomínio horizontal", "Comercial / corporativo", "Residência unifamiliar [A CONFIRMAR P4]", "Infraestrutura urbana (redes)", "Outro (abre campo)"])
    disc = ""
    for g, ss in SERV.items():
        disc += f'<div><p class="small" style="margin:8px 0 0"><b>{g}</b></p>' + "".join(f'<div class="cb{" on" if s == "Hidrossanitário" else ""}">{s}</div>' for s in ss) + "</div>"
    disc += '<div><p class="small" style="margin:8px 0 0"><b>Transversal</b></p><div class="cb">Compatibilização BIM</div><div class="cb">Ainda não sei — quero orientação</div></div>'
    form = ('<div class="form"><p class="small"><b>C21a · Formulário qualificado em 3 etapas</b> — no wireframe as 3 etapas aparecem empilhadas; no site, uma por vez.</p>'
            '<div class="stepbox"><p class="small"><b>Etapa 1 de 3 — O empreendimento</b></p><div class="progress"><span class="on"></span><span></span><span></span></div>'
            f'<div class="field"><span class="lbl">Tipo de empreendimento<span class="req"> *</span></span><div class="radio-cards">{tipos}</div></div>'
            '<div class="row2">' + field("Cidade") + field("UF", kind="select") + '</div>'
            '<div class="row2 eq">' + field("Nº de unidades", req=False, help="Condicional: multifamiliar/loteamento. ☐ Ainda não definido") + field("Área construída aprox. (m²)", req=False, help="Condicional: comercial, residência, outro") + '</div>'
            + field("Fase atual", req=False, kind="select", ph="Viabilidade · Arquitetura em desenvolvimento · Legal aprovado · Executivo · Obra ▾")
            + '<div class="btns"><span class="btn pri">[Continuar]</span></div></div>'
            '<div class="stepbox"><p class="small"><b>Etapa 2 de 3 — Escopo</b></p><div class="progress"><span class="on"></span><span class="on"></span><span></span></div>'
            f'<div class="field"><span class="lbl">Disciplinas<span class="req"> *</span> <span class="opt">(marque uma ou mais; pré-marcada por ?servico=)</span></span><div class="cbgrid">{disc}</div></div>'
            '<div class="row2 eq">' + field("Formato de entrega", req=False, kind="select", ph="BIM (Revit/IFC) · 2D (DWG) · Indiferente ▾") + field("Prazo desejado", kind="select", ph="Até 30 dias · 1–3 meses · 3–6 meses · Sem prazo ▾") + '</div>'
            + field("Link dos arquivos", req=False, ph="https://", help="Google Drive, WeTransfer, Dropbox…")
            + '<div class="field"><span class="lbl">Envio de arquivos <span class="opt">(opcional)</span></span><div class="input" style="border-style:dashed;text-align:center;min-height:80px;display:flex;align-items:center;justify-content:center">[Arraste ou selecione · PDF, DWG, RVT, IFC, ZIP · limite A CONFIRMAR]</div><span class="help">Arquivos grandes? Use o link acima.</span></div>'
            + field("Mensagem", req=False, kind="textarea", ph="Conte o que for útil: pavimentos, prazo de aprovação, particularidades…")
            + '<div class="btns"><span class="btn">[Voltar]</span><span class="btn pri">[Continuar]</span></div></div>'
            '<div class="stepbox"><p class="small"><b>Etapa 3 de 3 — Seus dados</b></p><div class="progress"><span class="on"></span><span class="on"></span><span class="on"></span></div>'
            + field("Nome completo") + '<div class="row2 eq">' + field("Empresa", req=False, help="Opcional para pessoa física") + field("Cargo", req=False) + '</div>'
            + '<div class="row2 eq">' + field("E-mail") + field("WhatsApp / telefone", ph="(31) 9____-____") + '</div>'
            + field("Como nos conheceu", req=False, kind="select", ph="Google · Indicação · LinkedIn · Já sou cliente · Outro ▾")
            + '<div class="cb">Concordo com o uso dos meus dados para receber o orçamento, conforme a [Política de privacidade]. *</div>'
            + '<div class="cb">Quero receber novidades (opcional; desmarcado)</div>'
            + '<div class="btns"><span class="btn">[Voltar]</span><span class="btn pri">[Enviar pedido de orçamento]</span></div>'
            + '<p class="small ph" style="margin-top:8px">Resposta em até X dias úteis [A CONFIRMAR]. Ocultos: servico, ref, UTMs, página de origem, honeypot + anti-spam invisível.</p></div></div>')
    canais = ('<div class="card sticky-col" id="canais"><span class="tag">Canais diretos</span>' + h(2, "[Prefere falar agora?]")
              + '<div class="btns" style="flex-direction:column"><a class="btn pri" href="#">WhatsApp (31) 99649-8629</a><a class="btn" href="#">Ligar (31) 3070-6568</a><a class="btn" href="#">[E-mail — A CONFIRMAR]</a></div>'
              + '<p class="small" style="margin-top:16px"><b>Endereço</b><br><span class="ph">[A CONFIRMAR: Goitacazes 103 ou Espírito Santo 1100]</span></p><p class="small"><b>Horário</b><br><span class="ph">[A CONFIRMAR]</span></p></div>')
    b += sec("CT-03", "Formulário qualificado C21a + canais", f'<div class="g64">{form}{canais}</div>'
             + note("formulário primeiro, canais diretos abaixo em cards largos. Campos ≥ 48 px, rótulo sempre acima, teclado por tipo (email/tel/url), botões largura total.", None,
                    "<b>Erros:</b> mensagem por campo em texto + resumo no topo da etapa; foco no 1º erro. <b>Envio:</b> e-mail [A CONFIRMAR destinatário] + cópia ao usuário + GA4 form_submit → /obrigado/. <b>Fallback</b> sem etapas: mesmo conteúdo em 3 fieldsets numa página."), cls="alt")
    b += sec("CT-04", "O que enviar · C12", h(2, "[Título: o que enviar para um orçamento rápido]") + faq(["[Quais arquivos ajudam?] (arquitetura DWG/PDF/RVT, implantação, nº de unidades/pavimentos, fase)", "[Meus arquivos ficam em sigilo?]", "[Em quanto tempo recebo a proposta?] [A CONFIRMAR]"]) + note("largura total."))
    b += sec("CT-05", "Endereço e mapa — CONDICIONAL", f'<div class="g55">{img("Mapa: imagem estática + “Abrir no mapa” (carrega sob clique)", "r169")}<div><p class="ph">[Endereço — A CONFIRMAR]</p><a class="link" href="#">Abrir no mapa</a></div></div>'
             + note("mapa 16:9.", None, "Só depois de confirmar endereço; se o atendimento não for presencial, a seção sai."), cls="alt", cond=True)
    page("contato.html", "Contato e orçamento", "Contato", b, ["Início", "Contato"], fl=False, mb=False, desc="/contato/")


def obrigado():
    b = sec("OB-01", "Confirmação (noindex)", f'<div style="max-width:720px">{h(1, "[Título: recebemos seu pedido]")}<p class="ph">[1 frase de confirmação]</p>'
            '<ol><li class="ph">[Próximo passo 1 — análise]</li><li class="ph">[Próximo passo 2 — contato em X dias úteis, A CONFIRMAR]</li><li class="ph">[Próximo passo 3 — proposta]</li></ol>'
            + btns(("pri", "[Enviar arquivos pelo WhatsApp]", "#"), ("", "[Ver projetos]", "projetos.html"), ("", "[Baixar portfólio (PDF)]", "#")) + "</div>"
            + note("botões largura total empilhados.", None, "Disparo de conversão GA4/Ads. Sem C20. NOVO em relação ao briefing."))
    page("obrigado.html", "Obrigado (pós-envio)", None, b, None, fl=False, mb=False, desc="/obrigado/")


def notfound():
    cards = "".join(f'<a class="card link-card" href="{href}">{h(2, t)}<p class="ph small">[1 frase]</p><span class="btn {k} sm" style="margin-top:8px">{c}</span></a>' for t, href, k, c in [
        ("Serviços", "servicos.html", "", "Ver serviços"), ("Projetos", "projetos.html", "", "Ver projetos"), ("Solicitar orçamento", "contato.html", "pri", "Pedir orçamento")])
    b = sec("404-02", "Mensagem", f'<div class="center">{h(1, "[Título: página não encontrada]")}<p class="ph">[Texto: o endereço pode ter mudado com o novo site]</p></div>' + note("centralizado."))
    b += sec("404-03", "Atalhos", f'<div class="g3">{cards}</div><p class="center"><a class="link" href="home.html">Voltar para o início</a> · <a class="link" href="#">Falar no WhatsApp</a></p>'
             + note("cards em 1 coluna, largura total.", None, "Status HTTP 404 real (não redirecionar para a home). Sem busca na fase 1."), cls="alt")
    page("404.html", "404", None, b, None, desc="página não encontrada")


def index():
    rows = [
        ("home.html", "Home", "/", "14 seções · hero com foto real, prova, serviços, concessionárias, BIM, projetos, processo, RT, depoimentos (cond.), FAQ, CTA com formulário curto"),
        ("servicos.html", "Serviços (hub)", "/servicos/", "3 grupos + faixa BIM + “não sei o que preciso”"),
        ("servico-modelo.html", "Serviço individual (modelo)", "/servicos/[disciplina]/", "Modelo único para as 9 disciplinas"),
        ("bim.html", "BIM e Compatibilização", "/bim-e-compatibilizacao/", "Galeria com as 8 imagens BIM reais"),
        ("projetos.html", "Projetos (listagem)", "/projetos/", "Filtros (UF, cliente, tipo*, disciplina*), 18 cards, #clientes com 24 logos"),
        ("projeto-modelo.html", "Projeto individual (modelo)", "/projetos/[empreendimento]/", "Ficha técnica, CTA lateral, seções condicionais"),
        ("sobre.html", "Sobre", "/sobre/", "RT, equipe (cond.), atuação, #dados-cadastrais"),
        ("contato.html", "Contato e orçamento", "/contato/", "Formulário qualificado em 3 etapas + canais diretos"),
        ("obrigado.html", "Obrigado (pós-envio)", "/obrigado/", "Novo · noindex · conversão"),
        ("404.html", "404", "—", "Atalhos para Serviços, Projetos e Orçamento"),
    ]
    cards = "".join(f'<a class="card" href="{f}">{h(2, t)}<p class="meta">{u}</p><p class="small">{d}</p></a>' for f, t, u, d in rows)
    legend = ('<ul class="plain small"><li><b>Etiqueta preta</b> = código da seção (ex. H-02) + componente reutilizável (Cxx, ver 02-wireframe.md §4).</li>'
              '<li><b>Etiqueta tracejada</b> = seção condicional/opcional: só entra com dado real.</li>'
              '<li><b>[Colchetes]</b> = placeholder para o copywriter; <b>[A CONFIRMAR]</b> = dado do cliente pendente, nunca inventar.</li>'
              '<li><b>Caixa cinza com nota</b> = comportamento mobile, asset real a usar (ASSET), ou FOTOGRAFAR / PEDIR / GERAR / CRIAR.</li>'
              '<li>Botão “Ocultar notas” na barra preta mostra o wireframe limpo.</li>'
              '<li>Fixos: C19 WhatsApp flutuante (desktop) e C20 barra Orçamento + WhatsApp (mobile).</li></ul>')
    html = f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wireframes · Intrépida Engenharia</title><link rel="stylesheet" href="wf.css"></head><body class="idx">
<div class="wfbar"><span><b>WIREFRAMES</b> baixa fidelidade · Intrépida Engenharia e Projetos · 21/11/2026</span><span>Especificação: equipe/02-wireframe.md</span></div>
<main><section class="s"><div class="wrap"><h1>Wireframes do novo site</h1><p class="ph">Cinza, sem estilo de marca. Estrutura, hierarquia e comportamento responsivo (375 px e 1440 px). Agnóstico de plataforma (WordPress + Elementor ou estático).</p>
<div class="g3" style="margin-top:24px">{cards}</div></div></section>
<section class="s alt"><div class="wrap"><h2>Legenda</h2>{legend}</div></section></main></body></html>'''
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


home(); hub(); servico(); bimpage(); projetos(); projeto(); sobre(); contato(); obrigado(); notfound(); index()
print("ok")
