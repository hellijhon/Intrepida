# 04 — Design system: Intrépida Engenharia e Projetos

> Etapa: Web design (agente `webdesigner-senior`). Data: 21/11/2026.
> Base: `01-contexto.md`, `02-wireframe.md` e `03-copy.md` (aprovados), manual da marca e portfólio 2024.
> Implementação de referência: `site/` (HTML/CSS/JS gerado por `site/_build/`). CSS com os tokens: `site/assets/css/site.css`.
> Plataforma final: **WordPress + Elementor**. Cada token abaixo traz o nome que ele deve ter no **Kit do Elementor** (Global Colors / Global Fonts) e cada componente traz o **template global** correspondente. O passo a passo está em `04-guia-migracao-elementor.md`.

---

## 1. Direção visual

### 1.1 Referências analisadas
| # | Referência | O que tiramos dela | O que não serve |
|---|---|---|---|
| R1 | **Sites de escritórios de engenharia de projetos internacionais** (padrão Arup / Buro Happold): fotografia grande e real, muito respiro, tipografia sem serifa firme, paleta contida | Hierarquia editorial, fotos de obra como prova, poucos elementos por tela | Tom institucional distante demais para um B2B regional que precisa converter |
| R2 | **Documentação técnica BIM (Revit/Navisworks)**: modelos isométricos sobre fundo branco, linhas finas, marcações de cota | Moldura "técnica" para as imagens BIM, grade de prancha como textura, numeração de itens | Interface de software (densa, cinza) |
| R3 | **A própria marca Intrépida** (manual, portfólio 2024, fundos de reunião, banner LinkedIn): azul-marinho, formas geométricas azuis, símbolo de duas barras laranja/vermelho | Cores, textura `fundo-capa`, etiquetas arredondadas, ícones em quadrados azuis | "Ondas" orgânicas em excesso e a frase genérica do banner |

### 1.2 Conceito escolhido: **"Prancha técnica"**
O site se comporta como uma prancha de projeto bem organizada: **fundo branco e azul-marinho**, **grade fina de desenho técnico** como textura de fundo em seções claras, **molduras com "cantos de cota"** em laranja nas imagens BIM e nas ilustrações, **numeração** (01, 02…) em listas de entregáveis e etapas, e **fotos aéreas reais** como prova em tamanho generoso.

O **símbolo das duas barras** (vermelho + laranja) vira o marcador gráfico do site: aparece antes de cada *eyebrow* (rótulo de seção). O laranja entra só como **acento** (marcadores, cotas, linhas sob números, CTA escurecido), nunca como fundo de texto.

**Por que combina com a marca e o público.** O comprador é engenheiro ou coordenador de projetos (P1) e analista de suprimentos (P2): quer prova, clareza e cara de empresa técnica, não de agência. A linguagem de prancha fala o idioma dele, dá ordem a muito conteúdo técnico (9 disciplinas, normas, entregáveis) e valoriza o maior diferencial visual que a Intrépida tem: os **modelos BIM reais**. Ao mesmo tempo, as fotos aéreas dos 12 empreendimentos provam escala logo na primeira dobra.

### 1.3 Princípios
1. **Prova antes de adjetivo**: foto real, cliente, cidade, unidades.
2. **Um CTA dominante por tela** (laranja escurecido); WhatsApp sempre como secundário.
3. **Respiro e ritmo**: seções alternam branco → cinza claro com grade → azul-marinho.
4. **Nada decorativo sem função**: a grade organiza, a cota emoldura o modelo, a animação só revela conteúdo.

---

## 2. Cores

### 2.1 Tokens (contraste WCAG medido por script)
| Token CSS | Global Color no Elementor | HEX | Uso | Contraste |
|---|---|---|---|---|
| `--c-navy-800` | **Primary** (Azul Intrépida) | `#0B3859` | Títulos, botão secundário, faixas, barra de números | 12,18:1 no branco |
| `--c-navy-900` | Azul profundo | `#082C47` | Fundos escuros (C18, cartões de CTA) | 14,37:1 no branco |
| `--c-navy-950` | Azul rodapé | `#061F33` | Rodapé | 16,78:1 |
| `--c-navy-700` | Azul hover | `#134A72` | Hover de botão azul | 9,33:1 |
| `--c-blue-600` | **Secondary** (Azul apoio) | `#196291` | Links, eyebrows, foco | 6,57:1 no branco · 6,09:1 no blue-50 |
| `--c-blue-200` / `-100` / `-50` | Azul claro 200/100/50 | `#C9DCEB` / `#E4EEF6` / `#F2F7FB` | Bordas, fundos de ícone, fundos de seção | decorativo |
| `--c-orange-500` | **Accent** (Laranja marca) | `#F15A29` | **Só gráfico**: marcador, cotas, linha sob números, borda do CTA em fundo escuro | 3,37:1 no branco → **proibido para texto** |
| `--c-orange-600` | Laranja CTA | `#C8431B` | Fundo do botão primário (texto branco) | **4,91:1** (AA) |
| `--c-orange-700` | Laranja CTA hover | `#A63714` | Hover/active do primário | 6,61:1 |
| `--c-orange-100` | Laranja claro | `#FDE9E1` | Fundo de selo (texto `#8C2E10`, 7,13:1) | — |
| `--c-red-500` | Vermelho marca | `#EF4036` | **Só gráfico** (barra esquerda do marcador) | 3,85:1 → proibido para texto |
| `--c-ink` | **Text** | `#17202B` | Texto principal | 16,43:1 |
| `--c-gray-700` | Texto secundário | `#3A4552` | Parágrafos de apoio | 9,75:1 |
| `--c-gray-600` | Texto auxiliar / logos | `#4A5562` | Legendas, ajuda de campo, logos monocromáticos | 7,59:1 |
| `--c-gray-500` | Texto mínimo | `#5F6A77` | Placeholder, borda de campo | 5,51:1 no branco · 4,95:1 no gray-100 |
| `--c-gray-300` / `-200` / `-100` | Cinzas de borda e fundo | `#C5CCD4` / `#E3E7EC` / `#F1F3F6` | Divisórias, cartões, fundo de seção | decorativo |
| `--c-on-dark-muted` | Texto em azul | `#BFD0DF` | Parágrafos sobre navy | 9,10:1 no navy-900 · 7,72:1 no navy-800 |
| (eyebrow em fundo escuro) | — | `#FFC3AD` / `#FFB59C` | Rótulos e ícones sobre navy | 9,35:1 / 9,86:1 |
| `--c-success` | Sucesso | `#1D7444` (fundo `#E6F4EC`) | Checks, confirmação | 5,78:1 |
| `--c-error` | Erro | `#B42318` (fundo `#FDECEA`) | Mensagens de erro | 6,57:1 · 5,75:1 no fundo |
| `--c-warning` | Aviso | `#8A5300` (fundo `#FFF4E0`) | Placeholders sinalizados (modo revisão) | 6,33:1 |
| `--c-info` | Informação | `#196291` (fundo `#E4EEF6`) | Alertas informativos | 6,57:1 |
| WhatsApp | Verde WhatsApp acessível | `#1F7A4D` / hover `#17633E` | Botão C19 e texto do botão C20 | branco 5,32:1 |

### 2.2 Decisões de cor
- **CTA primário = `#C8431B` com texto branco** (laranja escurecido, mesma matiz da marca). O laranja original `#F15A29` não passa em texto (3,37:1).
- **Texto sobre a textura da marca** (C13): a textura sempre leva uma camada **navy-900 a 82%** (`.bg-texture`). Medido pixel a pixel: `#BFD0DF` fica com pior pixel 5,22:1 e branco com 8,24:1. Em qualquer contexto escuro (`.on-dark`), `.lead` e parágrafos usam `--c-on-dark-muted` (correções UX-02 e UX-04).
- **Eyebrow em fundo escuro ou foto:** `#FFC3AD` (10,9:1 sobre a pílula; 6,26:1 no pior caso). Nunca o azul `#196291` sobre escuro (UX-01).
- Em fundo azul-marinho, o CTA ganha **borda `#F15A29`** (4,27:1 contra o navy-900) para manter o contorno ≥ 3:1 (WCAG 1.4.11), já que o miolo `#C8431B` fica em 2,92:1 contra o navy.
- **Vermelho e laranja da marca só no símbolo e em grafismos.**
- Proporção aproximada por página: 60% branco/cinza claro, 30% azul-marinho, 10% acento laranja.

---

## 3. Tipografia

### 3.1 Fontes
| Papel | Fonte | Pesos | Global Font no Elementor | Por quê |
|---|---|---|---|---|
| Logo | **Harabara** | — | — (só no SVG do logo) | Regra do manual; não é fonte web. O logo foi convertido em SVG a partir do vetor. |
| Títulos, botões, rótulos, números | **Montserrat** (Google Fonts, OFL) | 600, 700, 800 | **Primary** (títulos) e **Accent** (botões/rótulos) | Fonte de apoio oficial do manual. Geométrica, firme, combina com o logotipo. |
| Texto corrido, formulários | **Fira Sans** (Google Fonts, OFL) | 400, 500, 600 | **Text** e **Secondary** | Substitui a Colaborate (ver 3.2). |

### 3.2 Colaborate: por que não usar na web
Os arquivos `ColabThi/Lig/Reg/Med/Bol.otf` trazem nos metadados apenas *"Copyright (c) 2003 … Ralph Oliver du Carrois. All rights reserved."*, **sem licença declarada** (nenhum campo de licença ou URL de licença). Sem a licença de **webfont** confirmada, embutir a fonte no site é risco jurídico. Decisão: **não usar Colaborate no site**.
**Alternativa escolhida: Fira Sans.** Foi desenhada pelo mesmo tipógrafo (Ralph du Carrois, com Erik Spiekermann), tem o mesmo desenho humanista e técnico da Colaborate, é **livre (SIL OFL)**, tem excelente legibilidade em telas pequenas, acentuação completa do português e ótima versão para números tabulares. Montserrat (títulos) + Fira Sans (texto) dá contraste geométrico × humanista sem conflito.
Se o cliente comprovar a licença web da Colaborate, ela pode entrar no lugar da Fira Sans trocando só o token `--f-body` / Global Font "Text".

### 3.3 Escala (fluida com `clamp()`; valores de referência)
| Token | Elementor (Typography global) | Mobile 375 | Desktop 1440 | Line-height | Peso / fonte |
|---|---|---|---|---|---|
| `--fs-display` (H1 da home) | H1 Display | 34 px | 56 px | 1,12 | 800 Montserrat |
| `--fs-h1` / H1 interno | H1 | 30 px | 46 px | 1,12 | 800 Montserrat |
| `--fs-h2` | H2 | 26 px | 40 px | 1,22 | 700 Montserrat |
| `--fs-h3` | H3 | 19 px | 22 px | 1,3 | 700 Montserrat |
| `--fs-h4` | H4 | 17 px | 17 px | 1,35 | 700 Montserrat |
| `--fs-lead` | Texto destaque | 17 px | 20 px | 1,55 | 400 Fira Sans |
| `--fs-body` | Texto | 16 px | 16 px | 1,62 | 400 Fira Sans |
| `--fs-small` | Texto pequeno | 14 px | 14 px | 1,5 | 400/500 Fira Sans |
| `--fs-xs` (eyebrow, legendas) | Rótulo | 13 px | 13 px | 1,3 | 700 Montserrat, caixa alta, `letter-spacing .12em` |
| `--fs-num` (barra de números) | Número | 36 px | 56 px | 1 | 800 Montserrat |
| Botão | Botão | 15 px | 15 px | 1,2 | 700 Montserrat |

No Elementor, definir cada tamanho em **px por breakpoint** (Desktop / Tablet / Mobile) com os valores acima; o valor tablet é a média.

---

## 4. Grid e espaçamento

- **Base 4/8 px.** Tokens: `--s-1` 4 · `--s-2` 8 · `--s-3` 12 · `--s-4` 16 · `--s-5` 24 · `--s-6` 32 · `--s-7` 48 · `--s-8` 64 · `--s-9` 96 · `--s-10` 128.
- **Container:** conteúdo 1200 px (`--container`), header/rodapé 1360 px (`--container-wide`), leitura 720 px (`--read`, política e textos longos).
- **Gutter lateral:** 16 px (375) → 32 px (≥ 1440), fluido.
- **Respiro vertical de seção** (`--sec-y`): 64 px mobile → 112 px desktop. Seções "tight": 40–64 px.
- **Grid:** 4 colunas no mobile, 8 no tablet, 12 no desktop; gap 24 px (mobile) e 32 px (≥ 768).
- **Breakpoints (iguais aos do Elementor):** mobile ≤ 767 · tablet 768–1024 · desktop ≥ 1025 · wide ≥ 1440 (testados em 375, 768, 1280 e 1440).
- **Raios:** 6 (pequeno), 10 (botão, campo), 16 (cartão), 24 (cartão de formulário, bottom sheet), pílula.
- **Sombras:** `--sh-1` (repouso de cartão), `--sh-2` (hover), `--sh-3` (destaque/menu).

**Elementor:** Site Settings → Layout: *Content width* 1200, *Container padding* 0/16 (mobile) e 0/24 (tablet) e 0/32 (desktop), *Widgets space* 24. Todas as seções em **Container (Flexbox)**; as grades de cartões usam **Container Grid** (Elementor ≥ 3.16) com 1/2/3 colunas por breakpoint.

---

## 5. Componentes (C01–C24) e estados

Convenção do código: cada seção tem `id` = ID do wireframe (`h-02`, `sv-03`…) e `data-componente="Cxx"`. Classe CSS = `cxx-nome`. No Elementor, o **nome do template salvo** é `Cxx – Nome` (ex.: `C08 – Card de projeto`).

### 5.1 Botões (global)
| Variação | Classe | Repouso | Hover | Focus | Active | Disabled |
|---|---|---|---|---|---|---|
| Primário | `.btn` | fundo `#C8431B`, texto branco, 48 px de altura, raio 10 | fundo `#A63714` + sombra 2 | anel duplo branco 3 px + azul `#196291` 2 px | desce 1 px, sem sombra | fundo `#E3E7EC`, texto `#5F6A77`, cursor bloqueado |
| Secundário | `.btn--secondary` | borda 2 px navy, texto navy, fundo transparente | fundo navy, texto branco | idem | idem | idem |
| Claro (em fundo escuro) | `.btn--light` | borda branca 85%, texto branco | fundo branco, texto navy | anel navy + laranja claro | idem | — |
| Azul | `.btn--navy` | fundo navy, texto branco | `#134A72` | idem | idem | idem |
| WhatsApp | `.btn--wa` + variação | ícone do WhatsApp 20 px + texto | conforme variação | — | — | — |
| Link com seta | `.link-arrow` | texto `#196291` 700, seta | sublinhado + seta anda 3 px | anel | — | — |
Tamanhos: padrão 48 px; `--sm` 44 px (header, filtros). **Alvo mínimo 44 px em tudo que é clicável.**

### 5.2 Tabela de componentes
| Código | Componente | Template Elementor | Especificação visual | Estados / comportamento |
|---|---|---|---|---|
| **C01** | Header | *Theme Builder → Header* | Branco 97% com blur; logo azul SVG 200 px (168 no mobile); menu Montserrat 600 15 px; ícone WhatsApp em círculo 48 px; CTA primário `--sm`. Altura 88 → 64 px ao rolar 80 px. | Item ativo: sublinhado laranja 2 px + `aria-current`. Mega-menu de 3 colunas (hover **e** clique/Enter; Esc fecha). Mobile: hambúrguer 48 px → drawer da direita, foco preso, Esc fecha, accordion de Serviços, botão largo de orçamento e 3 atalhos (WhatsApp, Ligar, E-mail). |
| **C02** | Rodapé | *Theme Builder → Footer* | Fundo `#061F33`; logo branco; 4 colunas (Marca · Serviços · A Intrépida · Fale com a gente); barra inferior com © dinâmico, Política e "Preferências de cookies". | Mobile: ordem Marca → Contato → Serviços → Institucional; Serviços e Institucional viram accordions. Padding extra embaixo por causa do C20. |
| **C03** | Hero com foto | Seção salva `C03 – Hero foto` | Foto em tela cheia, sobreposição azul em gradiente (esquerda no desktop, de baixo para cima no mobile), H1 display branco, *eyebrow* `#FFC3AD` em pílula escura (seção com classe `on-dark`), 2 botões, microprova com ícones, crédito no canto. Variação **baixa** (Projetos). | Foto com `fetchpriority="high"` e `<picture>` com altura 100% + `object-fit: cover` (cobre o hero em qualquer proporção). Microprova: no mobile um item por linha, sem separador. Mobile: texto ancorado embaixo, botões empilhados em largura total, CTA visível em 375×667. |
| **C04** | Hero interno | `C04 – Hero interno` | Fundo degradê azul-50 → branco com grade técnica à direita; breadcrumb; eyebrow; H1 46 px máx.; lead; botões; imagem em moldura de cota à direita. Variação sem imagem (Contato, Obrigado, 404). | Mobile: imagem abaixo do texto. |
| **C05** | Barra de números | `C05 – Números` | Fundo navy-800, 4 itens (24 · 18 · 6 · +5.800), número 56 px 800 + linha laranja 28×3 px + rótulo. Variação clara (Sobre). | Grade 2×2 no mobile, 4 colunas no desktop. Sem contador animado. |
| **C06** | Logos de clientes | `C06 – Logos (12)` e `C06 – Logos (24)` | Grade com divisórias de 1 px (6×2 desktop, 4 col tablet, 3 col mobile); logos monocromáticos `#4A5562`, altura 48 px (64 px nos quadrados); variação 24 com legenda. Logo raster ilegível (hoje Mello Azevedo) entra como **nome em texto** `.logo-txt` (Montserrat 800, cinza 600) até chegar o vetor. | Sem carrossel. `alt` = nome do cliente. |
| **C07** | Cards de serviço | `C07 – Grupos de serviço` / `C07 – Card serviço` | (a) Home: 3 grupos em cartões, ícone em quadrado azul-50 44 px, nome, descrição de 1 linha (some no mobile), seta laranja; grupo Infraestrutura em destaque navy com selo. (b) Hub: cartão com ícone 52 px, H3, texto, "Saiba mais". (c) Card largo com foto (Infraestrutura). | Hover: ícone inverte para navy, filete laranja de 3 px aparece no topo, sobe 2 px. |
| **C08** | Card de projeto | **Loop Item** `C08 – Card projeto` | Foto 3:2, selo da UF, H3, "Cliente · Cidade/UF", "**n** unidades" + seta. Variação **sem foto**: textura azul da marca + símbolo + nome/cliente/cidade. | Card inteiro clicável (link no H3 com pseudo-elemento), hover sobe 3 px e dá zoom 4% na foto; foco visível no cartão. Home mobile: só 3 + botão. |
| **C09** | Texto + imagem | `C09 – Texto + imagem` | Split 40/60 ou 50/50; checklist com ícone verde; lista numerada "01, 02…" (entregáveis). | Empilha no mobile; em H-06 a imagem vem antes do texto no mobile. |
| **C10** | Processo | `C10 – Processo` | 5 etapas com círculo numerado 48 px (1ª laranja), conector tracejado azul-200, título H3 e frase. Fundo azul-50 com grade. | Horizontal (≥ 1025) / vertical com linha à esquerda (mobile). |
| **C11** | Galeria BIM + lightbox | `C11 – Galeria BIM` (Gallery Pro ou Basic Gallery + Lightbox nativo) | Miniaturas quadradas em fundo branco com borda, legenda 13 px; 4 col (8 imagens) no desktop, 2 col no mobile; na Home, carrossel com scroll-snap e indicador. | Lightbox: Fechar, Anterior, Próxima, contador "Imagem 3 de 8", setas do teclado, Esc, swipe. Foco preso. |
| **C12** | FAQ | Widget **Accordion** (ou *FAQ* com schema do plugin SEO) | `details/summary`, pergunta Montserrat 17 px, botão "+" 32 px que gira para "×", divisórias. 1ª aberta. | Alvo ≥ 64 px por pergunta. Gera schema FAQPage. |
| **C13** | CTA final | `C13 – CTA botões` / `C13 – CTA + formulário` | Fundo com a textura azul da marca (`fundo-azul`) **sob camada navy-900 82%**, lead `#BFD0DF`, H2 branco, lead, botões (primário + WhatsApp claro). Variação com formulário curto em cartão branco à direita e 3 passos numerados à esquerda. | Formulário em largura total no mobile. |
| **C14** | Breadcrumb | Widget *Breadcrumbs* (Yoast/Rank Math) | 14 px, cinza 600, separador "›". | Mobile: só o nível anterior ("‹ Serviços"). Schema BreadcrumbList. |
| **C15** | Ficha técnica | `C15 – Ficha` (Dynamic Tags dos campos) | Lista rótulo (13 px caixa alta) / valor, divisórias. Linhas sem dado **não aparecem**. | Rótulo acima do valor no mobile. |
| **C16** | Depoimentos | `C16 – Depoimentos` | Cartões com citação, nome, cargo, empresa. | **Condicional**: oculto (sem depoimentos). |
| **C17** | Responsável técnico | `C17 – RT compacto` / `C17 – RT completo` | Foto 176 px (raio 24) ou retrato 200×240; nome 22 px 800; cargo; texto; link. | **Placeholder sinalizado**: moldura tracejada com o símbolo da marca e selo "Placeholder · retrato do RT a fotografar" (só no modo revisão). |
| **C18** | Faixa de destaque | `C18 – Faixa escura` | Fundo navy-900, texto branco/azul claro, checklist com ícone verde claro, lista de normas em cartões translúcidos, CTA. | Split no desktop, empilhado no mobile. |
| **C19** | WhatsApp flutuante | *Popup* não, widget fixo no Footer (Container com posição fixa) | Círculo 60 px verde `#1F7A4D`, ícone 30 px, balão "Dúvidas? Fale no WhatsApp" no hover. | Só desktop; some quando o rodapé entra na tela; não existe em /contato/. |
| **C20** | Barra fixa mobile | Container fixo no Footer, visível só Mobile/Tablet | Fundo branco, sombra para cima; "Solicitar orçamento" (62%) + "WhatsApp" (38%, contorno verde). | Aparece depois que o hero sai da tela; some com o teclado aberto; não existe em /contato/ e /obrigado/; respeita a safe-area do iOS. |
| **C21a** | Formulário em 3 etapas | **Elementor Pro Form** com campo *Step* | Cartão branco raio 24; barra de progresso de 3 segmentos laranja; campos 52 px, rótulo sempre visível, borda `#5F6A77` 1,5 px; cartões de rádio com ícone para "Tipo"; checkboxes em caixas; dropzone tracejada; contador de caracteres. | Estados de campo: repouso, hover (borda navy-700), foco (borda azul + anel azul sólido 1,5 px + halo), erro (borda vermelha + mensagem com ícone "!" abaixo, com `id` ligado ao campo por `aria-describedby` e `aria-invalid`), desabilitado (fundo cinza). Obrigatórios com `required` (+ `novalidate`); grupo de checkboxes com `aria-required` e mensagem própria. Só o resumo de erros da etapa é anunciado (sem `role=alert` por campo); foco vai ao 1º erro. Botão "Enviando…" desabilitado. Falha: alerta vermelho com o texto do copy e o WhatsApp como link. Campo de link completa `https://`. |
| **C21b** | Formulário curto | Elementor Pro Form (sem etapas) | Mesmos estilos; 2 colunas no desktop. | Mesmas validações. |
| **C22** | Filtros de projetos | **Taxonomy Filter** (Elementor Pro) ligado ao Loop Grid | Cartão com selects "Estado" e "Cliente" (com busca), cada opção com a contagem "(n)" conforme o outro filtro e opções que zerariam o resultado desabilitadas; "Limpar filtros", chips dos filtros ativos (nome acessível começa pela sigla visível), contador `aria-live`. | Mobile: botão "Filtrar (n)" fixo no topo da lista → bottom sheet com "Ver n projetos". Estado vazio com 2 botões. Filtros refletidos na URL (`?uf=mg&cliente=…`). |
| **C23** | Banner de cookies | Plugin de consentimento (ver guia) | Desktop: cartão branco no canto inferior esquerdo. **Mobile: faixa compacta presa à base** (texto 13 px, ≤ 25% da tela em 375×812). "Aceitar todos" e "Recusar opcionais" com o mesmo peso, lado a lado; "Configurar" como link de texto. Painel com chave liga/desliga. | Consentimento guardado; link "Preferências de cookies" no rodapé reabre o painel. Depois de salvar, o foco volta ao link do rodapé ou ao `<main>`. |
| **C24** | Mapa de atuação | `C24 – Mapa UFs` (SVG/HTML) | **Cartograma em grade**: 27 quadrados na posição aproximada de cada UF; as 6 UFs com projeto em navy com o número de projetos num selo laranja; lista acessível ao lado. | Em Projetos, clicar numa UF aplica o filtro. |

---

## 6. Ícones
- **Conjunto próprio de linha** (24×24, traço 1,75, pontas arredondadas, `currentColor`) em `site/assets/img/icons.svg`: 9 disciplinas (hidro, elétrica, gás, HVAC, pressurização, piscina, saneamento, reúso, solar), BIM (cubo isométrico) e interface (seta, check, telefone, e-mail, pino, relógio, upload, filtro, busca, download, documento, prédio, lotes, loja, casa, escudo, usuário, engrenagem, cálculo, obra, conflito, WhatsApp, LinkedIn).
- Disciplinas sempre dentro de **quadrado arredondado azul-50** (eco dos "ícones brancos em quadrados azuis" do portfólio, invertido para fundo claro).
- Ícones ao lado de texto são decorativos (`aria-hidden`).
- **Elementor:** subir o SVG de cada ícone em *Icon Library → Custom Icons* (ou usar o widget Icon com "Upload SVG").

## 7. Fotografia e imagens
- **Fotos reais** dos 12 empreendimentos (drone): usadas sem filtro, recorte por `object-fit`; sobreposição azul só quando há texto em cima. Crédito/legenda discreta "Nome · Cliente · Cidade/UF".
- **Modelos BIM reais** (8): sempre em fundo branco, dentro da **moldura de cota** (cartão branco + cantos laranja), aparados nas bordas brancas, com legenda. Legendas a confirmar usam o texto genérico "Modelo BIM de instalações prediais" (regra do copy 13.2).
- **Ilustrações geradas por IA** (5): mesmo estilo isométrico de documentação BIM sobre fundo branco, para HVAC, pressurização, piscina, reúso pluvial e aquecimento solar. Sempre com o selo visível **"Imagem ilustrativa"** e a nota "Gerada por IA · não é projeto da Intrépida"; alt termina com "(imagem ilustrativa)". Registro em `site/assets/CREDITOS.md`.
- **Textura da marca** (`fundo-capa` do portfólio) nos CTAs finais (sempre sob camada navy 82%) e nos cartões de projeto sem foto.
- **Fotos em moldura de proporção fixa** (cards, hero): `<picture>` com altura 100% e `object-fit: cover`. Nunca deixar a imagem com altura automática dentro de moldura fixa (gera faixa vazia; UX-03).
- **Proibido:** banco de imagens de pessoas, imagens geradas de obras/equipe/escritório/clientes, foto do RT gerada.
- **Formato:** WebP + JPEG de fallback (`<picture>`), larguras 480/800/1200/1600/2400 conforme a origem, `width`/`height` definidos, `loading="lazy"` abaixo da dobra.

## 8. Animação
- **Revelar ao rolar** (`.reveal`): opacidade 0 → 1 e deslocamento 16 px, 520 ms, `cubic-bezier(.2,.7,.2,1)`, uma vez por elemento. Elementor: *Motion Effects → Entrance Animation "Fade In Up"*, duração "Fast/Normal".
- **Micro-interações:** 150 ms (cor/borda), 240 ms (menu, sheet, cartões). Hover de card: sobe 2–3 px; foto do card dá zoom 4% em 520 ms.
- **Nada em loop, nada automático** (sem carrossel automático, sem contador animado).
- **`prefers-reduced-motion: reduce`** desliga todas as transições e mostra o conteúdo direto.

## 9. Acessibilidade (incorporada ao sistema)
- Contraste AA medido para todos os pares de uso (tabela 2.1).
- Foco visível em tudo: anel duplo (branco 3 px + azul 2 px; em fundo escuro, navy + laranja claro), mais `outline` transparente que aparece no modo de alto contraste (`forced-colors`).
- Títulos com `overflow-wrap: break-word` (sem `hyphens: auto`, que quebrava palavras sem necessidade — REG-01); abaixo de 360 px a escala de títulos reduz (H1 28, H2 24, display 30 px). Sem estouro em 320 px (WCAG 1.4.10).
- Nome acessível de links e botões começa pelo texto visível (WCAG 2.5.3).
- Alvos de 44 px também nos links de contato do rodapé.
- Um H1 por página (verificado nas 36 páginas), H2 por seção, H3 nos cartões.
- Link "Pular para o conteúdo"; menus com `aria-expanded`/`aria-controls`; drawer, lightbox e bottom sheet com foco preso e Esc.
- Formulários com rótulo sempre visível, ajuda associada (`aria-describedby`), erro em texto abaixo do campo + resumo com links, `autocomplete` e `inputmode` corretos.
- Alvos de toque ≥ 44 px (48 px em formulário e menu).

## 10. Modo revisão e placeholders
O build tem `REVISAO = True` (em `site/_build/componentes.py`): mostra selos amarelos **"PLACEHOLDER"** nos pontos que aguardam material real (foto do RT, fotos dos 6 projetos sem imagem, imagem provisória do Sobre) e marca em amarelo os dados pendentes da Política de Privacidade. Para produção: `REVISAO = False`.
As **seções condicionais** (depoimentos, equipe, selos de concessionárias, prazo de resposta, PDF, LinkedIn, horário, CT-05 mapa, SV-07 por disciplina, desafio/solução, galeria do projeto, linha do tempo, CREA/CNPJ) estão prontas no código e ligadas ao dicionário `DADOS`; sem dado, saem como comentário HTML `<!-- CONDICIONAL … -->` no lugar exato.

> Correções da validação UX/UI (rodada 1) registradas em `equipe/04-correcoes-ux.md`.

## 11. Sugestões ao copy/estrutura (registradas, não aplicadas em silêncio)
1. **SV-06 sem modelo BIM real** (HVAC, pressurização, piscina, reúso, saneamento): a seção foi montada como variação do C09 **só com texto** (a ilustração já aparece no hero), para não repetir a mesma imagem nem mostrar modelo de outra disciplina.
2. **Hero de Projetos (PJ-02):** foi mantido o link discreto "Solicitar orçamento →" em branco sobre a foto (o azul de link não teria contraste).
3. **Rótulo "Órgãos"** em SV-05: o copy traz o conteúdo sem rótulo visível; usei o nome do campo ("Órgãos") como rótulo curto. Se o copywriter preferir outro rótulo, trocar em `build.py`.
4. **Logo da Chandon:** o arquivo do portfólio perdeu a transparência e só sobrou o contorno das letras; a versão monocromática ficou vazada. Pedir o logo vetorial.
