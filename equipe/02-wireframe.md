# 02 — Wireframe e arquitetura de informação: Intrépida Engenharia e Projetos

> Etapa: Wireframe (agente `wireframe`). Data: 21/11/2026.
> Base: `equipe/01-contexto.md` (briefing aprovado) e assets em `equipe/`. O site atual está fora do ar e não foi consultado.
> Wireframes visuais (baixa fidelidade, HTML cinza, responsivos): `equipe/wireframes/index.html`.

**Convenções deste documento**
- `[Título: …]` = placeholder descritivo para o copywriter. Nada aqui é texto final.
- `[A CONFIRMAR: …]` = dado do cliente ainda não confirmado (endereço, números, CREA, CNPJ, equipe, depoimentos, prazos). **Nunca substituir por valor inventado.** Se o dado não chegar até o lançamento, a regra de cada seção diz se ela some ou se o item é omitido.
- **Asset:** arquivo real em `equipe/` a usar. "GERAR" = imagem ilustrativa genérica, sempre sinalizada como ilustrativa, nunca simulando obra, equipe ou cliente real. "FOTOGRAFAR" = sessão de fotos necessária. "PEDIR" = solicitar ao cliente.
- **Cxx** = código do componente reutilizável (seção 4). Cada seção de página indica qual componente usa, para facilitar a montagem como template global no Elementor ou como partial num site estático.
- Plataforma (WordPress + Elementor ou estático) ainda não decidida. Tudo aqui é agnóstico; onde a escolha muda a implementação, há nota "Plataforma".

---

## 1. Sitemap

```
/                                   Home
├── /servicos/                      Serviços (hub, 3 grupos)
│   ├── Instalações prediais
│   │   ├── /servicos/projeto-hidrossanitario/
│   │   ├── /servicos/projeto-eletrico/            (Elétrica e Sistemas)
│   │   ├── /servicos/projeto-de-gas/
│   │   ├── /servicos/climatizacao-hvac/
│   │   ├── /servicos/pressurizacao-de-escadas/
│   │   └── /servicos/projeto-de-piscina/
│   ├── Infraestrutura urbana
│   │   └── /servicos/infraestrutura-de-saneamento/
│   └── Eficiência e sustentabilidade
│       ├── /servicos/reuso-de-agua-pluvial/
│       └── /servicos/aquecimento-solar/
├── /bim-e-compatibilizacao/        BIM e Compatibilização (diferencial transversal)
├── /projetos/                      Projetos (listagem com filtros + #clientes)
│   └── /projetos/[empreendimento]/ Página de projeto (modelo; 18 páginas na fase 1)
├── /sobre/                         Sobre (+ #dados-cadastrais)
├── /contato/                       Contato e orçamento (formulário qualificado)
│   └── /obrigado/                  Confirmação pós-envio (noindex)  ← NOVO
├── /politica-de-privacidade/       Política de privacidade
└── /404                            Página não encontrada
```

**Total fase 1:** 1 home + 1 hub + 9 serviços + 1 BIM + 1 listagem + 18 projetos + sobre + contato + obrigado + política + 404 = **35 páginas**, a partir de **11 modelos** (home, hub, serviço, BIM, listagem, projeto, sobre, contato, obrigado, texto legal, 404).

**Projetos da fase 1 (18)** — 12 com foto real (portfólio 2024) e 6 do site antigo sem foto (ver 7.6):
`mirante-sao-lucas`, `bosque-dos-ipes`, `residencial-pacifico`, `parque-lagoa-dos-principes-e-lagoa-nova`, `residencial-monte-carlo`, `residencial-vila-atlantico`, `residencial-vila-maria`, `residencial-ville-luxemburgo`, `residencial-alta-vista`, `residencial-portal-do-cerrado`, `residencial-scharle`, `residencial-portal-do-engenho`, `alto-boa-vista`, `gran-vic-gama`, `alto-riviera`, `smart-haus`, `alto-sobradinho`, `california-residence`.

**Redirecionamentos 301** (do briefing, mantidos): `/quem-somos/` → `/sobre/`; `/trabalhos-desenvolvidos/` → `/projetos/`; `/nossos-clientes/` → `/projetos/#clientes`; `/servicos/` e `/contato/` mantidos.

---

## 2. Navegação

### 2.1 Header (C01) — todas as páginas
| Desktop (≥ 1024 px) | Mobile (< 1024 px) |
|---|---|
| Logo horizontal (azul em fundo claro) à esquerda, link para `/` | Logo à esquerda (altura ~32 px) |
| Menu: **Serviços ▾** · **BIM** · **Projetos** · **Sobre** · **Contato** | Botão hambúrguer à direita (alvo 48×48 px, rótulo acessível "Abrir menu") |
| À direita: ícone WhatsApp (link `wa.me`, com rótulo acessível) + botão **[Solicitar orçamento]** (CTA primário) | O botão de orçamento sai do header e vai para a barra fixa inferior (C20) |
| **Sticky**: fixo no topo; reduz a altura (de ~88 para ~64 px) após 80 px de rolagem | Sticky, altura fixa ~60 px |

**Submenu "Serviços" (desktop):** mega-menu de 3 colunas, uma por grupo (Instalações prediais · Infraestrutura urbana · Eficiência e sustentabilidade), com os 9 links + rodapé do painel com "Ver todos os serviços →" (`/servicos/`) e "BIM e compatibilização →". Abre no hover **e** no clique/Enter (teclado); fecha com Esc. "Serviços" continua clicável e leva ao hub.

**Menu mobile (drawer em tela cheia, desliza da direita):**
1. Serviços (accordion → 3 grupos com os 9 links + "Ver todos")
2. BIM · Projetos · Sobre · Contato (itens com altura ≥ 48 px)
3. Botão largo **[Solicitar orçamento]**
4. Linha de contato: WhatsApp · Telefone (`tel:`) · E-mail (`mailto:`)
5. Botão fechar (X com ícone, não texto, corrige bug do site antigo). Foco preso no drawer enquanto aberto; Esc fecha.

Item ativo marcado visualmente e com `aria-current="page"`.

### 2.2 Rodapé (C02) — todas as páginas
| Coluna | Conteúdo |
|---|---|
| 1. Marca | Logo horizontal branco · [Texto: posicionamento em 1 frase] · link LinkedIn `[A CONFIRMAR: URL]` (some se não houver) · botão secundário "Baixar portfólio (PDF)" `[A CONFIRMAR: autorização e versão do PDF]` |
| 2. Serviços | 9 links das disciplinas + "BIM e compatibilização" |
| 3. Institucional | Projetos · Clientes (`/projetos/#clientes`) · Sobre · Contato · Política de privacidade |
| 4. Contato | WhatsApp (31) 99649-8629 · Telefone (31) 3070-6568 · E-mail `[A CONFIRMAR: e-mail que recebe leads]` · Endereço `[A CONFIRMAR: Goitacazes 103 ou Espírito Santo 1100]` · Horário `[A CONFIRMAR]` |
| Barra inferior | © 2026 `[A CONFIRMAR: razão social]` · CNPJ `[A CONFIRMAR]` · CREA `[A CONFIRMAR: registro da empresa e do RT]` · Política de privacidade |

**Mobile:** colunas empilhadas na ordem 1 → 4 → 2 → 3 (contato sobe porque é o que o usuário mobile procura). Colunas 2 e 3 viram accordions fechados. Links com alvo ≥ 44 px. A barra inferior fica com padding extra para não ficar escondida atrás da barra fixa C20.

### 2.3 Elementos persistentes de conversão
- **C19 WhatsApp flutuante (só desktop ≥ 1024 px):** botão redondo no canto inferior direito, mensagem pré-preenchida contextual (ver 3.3). Não aparece em `/contato/` (a página já tem o canal) nem cobre o rodapé (sobe quando o rodapé entra na tela).
- **C20 Barra fixa inferior (só mobile < 1024 px):** duas ações lado a lado — **[Solicitar orçamento]** (primária, ~65% da largura) e **[WhatsApp]** (ícone + texto). Aparece depois que o hero sai da tela; some em `/contato/`, `/obrigado/` e com o teclado aberto. Altura ~64 px + safe-area do iOS.
- Decisão: no mobile a barra C20 **substitui** o botão flutuante para não haver dois elementos fixos disputando o polegar.

### 2.4 Breadcrumb (C14)
Em todas as páginas internas de 2º nível ou mais (serviço individual, projeto individual) e no hub/BIM/listagem. Ex.: Início › Serviços › Projeto hidrossanitário. Gera schema `BreadcrumbList`. No mobile: mostra só o nível anterior ("‹ Serviços") para economizar linha.

---

## 3. Fluxos de conversão

### 3.1 Conversões e onde estão
| Conversão | Evento GA4 | Pontos de entrada |
|---|---|---|
| **Formulário qualificado** (principal) | `form_submit` (rótulo `orcamento_completo`) | `/contato/` → `/obrigado/` |
| Formulário curto (CTA final da home e das páginas de serviço) | `form_submit` (rótulo `orcamento_rapido`) | Home H-12, Serviço SV-10 → `/obrigado/` |
| WhatsApp | `whatsapp_click` (parâmetro `pagina`) | Header (desktop), C19, C20, heros, `/contato/`, `/obrigado/`, 404 |
| Telefone / e-mail | `tel_click` / `email_click` | Rodapé, `/contato/`, menu mobile |
| Portfólio PDF | `portfolio_download` | Rodapé, Home H-12, Sobre SB-08, `/obrigado/` `[A CONFIRMAR: PDF liberado]` |

### 3.2 Fluxos principais
**F1. Coordenador de projetos via busca (P1, desktop)** — principal
Google ("projeto hidrossanitário BH") → `/servicos/projeto-hidrossanitario/` → vê escopo, normas, projetos com a disciplina → CTA "Solicitar orçamento de projeto hidrossanitário" → `/contato/?servico=hidrossanitario` (disciplina já marcada no formulário) → `/obrigado/`.

**F2. Coordenador que chega pela marca/indicação (P1)**
Home → Barra de números + logos (prova) → Projetos em destaque → `/projetos/` (filtra pela UF dele) → `/projetos/[empreendimento]/` → CTA "Tem um empreendimento parecido?" → `/contato/` → `/obrigado/`.

**F3. Primeiro contato rápido (P1/P4, mobile)**
Qualquer página → barra fixa C20 → WhatsApp com mensagem contextual. Alternativa: C20 → `/contato/` (formulário em etapas, campos grandes).

**F4. Homologação de fornecedor (P2, desktop)**
Home → Sobre → `#dados-cadastrais` (razão social, CNPJ, CREA, RT) → baixa portfólio PDF ou envia e-mail formal. Também chega por "Clientes"/"Sobre" no rodapé.

**F5. Escritório de arquitetura (P3)**
Home → BIM (ou Serviços hub) → `/bim-e-compatibilizacao/` (galeria, entregáveis, formatos) → CTA → `/contato/` com tipo "Comercial/corporativo" ou "Residência" e disciplina "Compatibilização BIM".

**F6. Proprietário de obra particular (P4, mobile)** `[A CONFIRMAR: se este público interessa]`
Google ("projeto de piscina BH") → `/servicos/projeto-de-piscina/` → FAQ explica o que é e por que precisa → WhatsApp (C20).

**F7. Erro / URL antiga sem 301**
404 → links para Serviços, Projetos, Contato + WhatsApp.

### 3.3 Regras transversais de fluxo
- **Pré-preenchimento por contexto:** links de orçamento em páginas de serviço levam `?servico=[slug]` e marcam a disciplina no formulário; links de páginas de projeto levam `?ref=projeto-[slug]` (campo oculto). Parâmetros só com dados não pessoais.
- **Mensagem de WhatsApp contextual:** "Olá! Vim pelo site da Intrépida (página: [nome da página]) e quero falar sobre um projeto." Texto final com o copywriter.
- **CTA primário acima da dobra** em todas as páginas, em 375 px e em 1440 px.
- **Cada página termina num CTA** (C13); nenhuma página é beco sem saída.
- **Distância máxima de 2 cliques** de qualquer página até o formulário.

---

## 4. Biblioteca de componentes (modular)

Cada componente vira um **template global** no Elementor (seção salva / componente) ou um **partial** no estático. As páginas são montadas empilhando componentes.

| Código | Componente | Variações | Usado em |
|---|---|---|---|
| C01 | Header | normal / compacto (scroll) | todas |
| C02 | Rodapé | — | todas |
| C03 | Hero com foto | foto de fundo com sobreposição / foto ao lado | Home, Projetos, Projeto |
| C04 | Hero interno (texto + imagem lateral) | com/sem imagem, com/sem formulário | Hub, Serviço, BIM, Sobre, Contato |
| C05 | Barra de números | 3, 4 ou 5 itens | Home, Projetos, Sobre |
| C06 | Faixa de logos de clientes | 12 itens + link / 24 itens completos | Home, Projetos (#clientes), Sobre |
| C07 | Grade de cards de serviço | agrupada (3 grupos) / simples (mesmo grupo) | Home, Hub, Serviço |
| C08 | Card + grade de projetos | 3 / 6 / grade completa com filtros | Home, Projetos, Serviço, Projeto |
| C09 | Bloco texto + imagem | imagem à esquerda/direita; com lista de benefícios | Home, Serviço, BIM, Sobre |
| C10 | Processo em etapas | horizontal (desktop) / vertical (mobile) | Home, Hub, BIM, Sobre |
| C11 | Galeria BIM | grade + lightbox | Home (4 imgs), BIM (8), Serviço (1–2) |
| C12 | FAQ (accordion) | 4–8 perguntas; gera schema FAQPage | Home, Serviço, BIM, Contato |
| C13 | CTA final | só botões / com formulário curto (C21b) / com download PDF | todas |
| C14 | Breadcrumb | — | internas |
| C15 | Ficha técnica | lista de pares rótulo/valor | Projeto, Sobre (dados cadastrais) |
| C16 | Depoimentos | 1 destaque / 3 cards — **condicional** | Home, Projeto |
| C17 | Bloco responsável técnico | compacto (home) / completo (sobre) | Home, Sobre |
| C18 | Faixa de destaque (dor → solução) | fundo escuro com CTA | Home, Hub, Serviço |
| C19 | WhatsApp flutuante | só desktop | todas exceto contato |
| C20 | Barra fixa inferior mobile | — | todas exceto contato/obrigado |
| C21 | Formulário qualificado (3 etapas) | C21a completo / C21b curto | Contato / CTA finais |
| C22 | Filtros de projetos | chips (desktop) / bottom sheet (mobile) | Projetos |
| C23 | Banner de cookies (LGPD) | — | todas, se houver analytics |
| C24 | Mapa de atuação (UFs) | SVG do Brasil com UFs destacadas | Sobre, Projetos |

---

## 5. Home (`/`)

**Objetivo:** levar o coordenador de projetos (P1) a pedir orçamento, provando escala e especialização. **CTA primário:** Solicitar orçamento. **Secundário:** WhatsApp.
**Ordem persuasiva:** promessa → prova imediata → solução (serviços) → dor central (concessionárias) → diferencial (BIM) → prova detalhada (projetos) → como funciona → quem assina → objeções (FAQ) → CTA.

| # | Seção | Comp. |
|---|---|---|
| H-01 | Header | C01 |
| H-02 | Hero | C03 |
| H-03 | Barra de números | C05 |
| H-04 | Logos de clientes | C06 |
| H-05 | Serviços (3 grupos) | C07 |
| H-06 | Aprovação em concessionárias | C18 |
| H-07 | BIM e compatibilização | C09 + C11 |
| H-08 | Projetos em destaque | C08 |
| H-09 | Como trabalhamos | C10 |
| H-10 | Responsável técnico | C17 |
| H-11 | Depoimentos (condicional) | C16 |
| H-12 | Perguntas frequentes | C12 |
| H-13 | CTA final com formulário curto | C13 + C21b |
| H-14 | Rodapé | C02 |

**H-02 Hero**
- Objetivo: dizer em 5 segundos o que a Intrépida faz, para quem, e dar o caminho do orçamento.
- Elementos: eyebrow `[Rótulo: categoria — ex. "Projetos de instalações e infraestrutura"]` · **H1** `[Título: promessa principal com serviço + público, até 10 palavras]` · subtítulo `[Subtítulo: benefício — prazo, aprovação em concessionárias, sem retrabalho; até 25 palavras]` · **[Solicitar orçamento]** (primário → `/contato/`) · **[Falar no WhatsApp]** (secundário) · microprova abaixo dos botões `[Linha de prova: "24 construtoras atendidas em 6 estados" — números a confirmar]`.
- Imagem: **Asset** `fotos/obras-empreendimentos/portfolio-2024_p08_mirante-sao-lucas_UNENCO_bh-MG_4096x2304.jpeg` (BH, alta resolução). Alternativa: `…p13_residencial-pacifico…_4000x3000.jpeg`. Crédito discreto "Mirante São Lucas — UNENCO, BH" no canto. `[A CONFIRMAR: direito de uso das fotos]`.
- Desktop: foto de fundo em largura total, sobreposição escura à esquerda para contraste do texto (texto ocupa ~55% da largura); altura ~85vh, máx. 760 px.
- **Mobile:** a foto continua como fundo (altura ~100svh menos o header), com o bloco de texto e sobreposição escura ancorado na base. Foi testado no wireframe: com a foto *acima* do texto, o CTA caía abaixo da dobra em 375 px. H1 em até 4 linhas; botões em largura total, empilhados (orçamento em cima); microprova em 2 linhas. CTA visível sem rolar em 375×667. A barra fixa C20 só aparece depois que o hero sai da tela.
- Interação: nenhuma animação bloqueante; imagem com `fetchpriority="high"` (é o LCP).

**H-03 Barra de números**
- Objetivo: prova de escala imediata.
- Elementos: 4–5 itens (número grande + rótulo): `[N empreendimentos — 18 documentados, A CONFIRMAR total]` · `[~5.870 unidades projetadas — A CONFIRMAR]` · `6 estados (MG, DF, SP, RJ, MS, SC)` · `24 construtoras e incorporadoras` · `[X anos de mercado — A CONFIRMAR ano de fundação]`.
- Regra: item sem confirmação **sai**; mínimo 3 itens. Usar "+" só se o cliente confirmar que é piso.
- Mobile: grade 2×2 (o 5º item ocupa a linha inteira). Sem contador animado obrigatório (se houver, respeitar `prefers-reduced-motion`).

**H-04 Logos de clientes**
- H2 `[Título: "Quem já confia na Intrépida" — curto]`.
- 12 logos (prioridade: MRV, Direcional, Tenda, Patrimar, RNI, Precon, VIC, Prix, UNENCO, Quartzo, Mello Azevedo, Vitta) em escala de cinza uniforme + link "Ver todos os clientes e projetos →" (`/projetos/#clientes`).
- Asset: `marca/logos-clientes/*.jpeg` **só como referência** (JPEG com fundo preto). PEDIR versões PNG/SVG ou redesenhar em monocromático. `[A CONFIRMAR: autorização de uso das marcas]`. `alt` = nome do cliente.
- Desktop: grade 6×2. Mobile: grade 3×4, logos com altura máx. 40 px. **Sem carrossel automático** (acessibilidade e porque escondê-los reduz a prova).

**H-05 Serviços**
- H2 `[Título: o que projetamos]` + intro de 1 linha.
- 3 colunas (grupos), cada uma com H3 do grupo e lista de disciplinas (ícone + nome + 1 linha `[Descrição: 8–12 palavras]` + link para a página). Instalações prediais (6), Infraestrutura urbana (1, card maior com destaque "redes de água, esgoto e drenagem"), Eficiência e sustentabilidade (2).
- Card extra/faixa abaixo: "BIM e compatibilização em todas as disciplinas →" (`/bim-e-compatibilizacao/`).
- CTA da seção: "Ver todos os serviços" (link texto).
- Ícones: REDESENHAR em SVG (os do portfólio são de estilo antigo).
- Mobile: grupos empilhados; dentro de cada grupo, lista vertical compacta (ícone 32 px + nome + seta). Descrição de 1 linha some no mobile para encurtar.

**H-06 Aprovação em concessionárias ("projetista desde o começo")**
- Objetivo: tocar na dor nº 1 (prazo e risco de aprovação) e posicionar a solução.
- Elementos: H2 `[Título: dor — atraso de aprovação em concessionárias]` · parágrafo curto `[Texto: projetista calculista desde o estudo de viabilidade evita reprovações e retrabalho]` · 3 bullets com ícone `[Benefício 1–3: aprovação de primeira, normas atendidas, prazo previsível]` · selos de texto das concessionárias `[A CONFIRMAR: COPASA, CEMIG, Gasmig e de outras UFs em que já aprovaram]` · CTA **[Envie seu projeto para análise]** → `/contato/`.
- Imagem: **Asset** `…p08_bosque-dos-ipes_RNI_campo-grande-MS_4000x2250.jpeg` (foto em obra, reforça "desde o começo").
- Desktop: fundo escuro, texto à esquerda, foto à direita (50/50). Mobile: foto em cima (16:9), texto e CTA largura total abaixo.
- **Corrige** o CTA morto do site antigo (botão apontava para `#`).

**H-07 BIM e compatibilização**
- H2 `[Título: BIM que evita conflito na obra]` · texto `[2–3 frases: modelagem 3D, compatibilização entre disciplinas, menos retrabalho]` · lista de 3–4 benefícios · CTA "Conheça nosso processo BIM →" (`/bim-e-compatibilizacao/`).
- Galeria de 4 imagens (C11 reduzido, clique abre lightbox): **Assets** `fotos/bim-modelos-3d/portfolio-2024_p03_bim-hidrossanitario-a…`, `…p06_bim-quadro-eletrico…`, `…p05_bim-a…`, `…p06_bim-tubulacao-gas-ou-hidraulica…`. Legenda por imagem `[A CONFIRMAR: disciplina exata de cada modelo]`.
- Desktop: texto à esquerda (40%), mosaico 2×2 à direita (60%). Mobile: texto, depois carrossel horizontal com scroll-snap (1,2 imagem visível, indicador de páginas), depois CTA.

**H-08 Projetos em destaque**
- H2 `[Título: empreendimentos que já projetamos]` + link "Ver todos os projetos".
- 6 cards (C08): foto, nome (H3), cliente, cidade/UF, nº de unidades, até 3 tags de disciplina `[A CONFIRMAR: disciplinas por projeto]`. Card inteiro clicável → `/projetos/[slug]/`.
- Seleção sugerida (melhores fotos + diversidade de UF): Mirante São Lucas (BH/MG), Bosque dos Ipês (Campo Grande/MS), Residencial Pacífico (Ribeirão das Neves/MG), Parque Lagoa dos Príncipes (Lagoa Santa/MG), Residencial Alta Vista (Barueri/SP), Residencial Monte Carlo (Cabo Frio/RJ — 1.800 unid., prova de escala, mas foto 960×720: usar em card pequeno).
- Desktop: grade 3×2. Tablet: 2×3. Mobile: 1 coluna com os **3 primeiros** + botão "Ver todos os 18 projetos" (evita rolagem longa).

**H-09 Como trabalhamos**
- H2 `[Título: processo]` · 4–5 etapas numeradas (ícone + título + 1 frase) `[A CONFIRMAR: etapas reais — sugestão: 1. Briefing e análise dos arquivos · 2. Proposta com escopo e prazo · 3. Modelagem BIM e cálculo · 4. Compatibilização e aprovação nas concessionárias · 5. Entrega e acompanhamento de obra]` · nota de prazo de resposta `[A CONFIRMAR: "proposta em até X dias úteis"]`.
- Desktop: linha horizontal com conectores. Mobile: lista vertical com linha à esquerda.

**H-10 Responsável técnico (compacto)**
- Foto + nome **Carlos Alberto Grope** + cargo "Diretor Técnico — Engenheiro Civil Sanitarista" + CREA `[A CONFIRMAR]` + 2 frases `[Texto: experiência e atuação direta nos projetos]` + link "Conheça a Intrépida →" (`/sobre/`).
- Asset: FOTOGRAFAR retrato profissional. **Não gerar por IA.** Enquanto não houver foto: variante sem imagem (só texto, com o símbolo da marca).
- Mobile: foto circular 96 px acima do texto, centralizado.

**H-11 Depoimentos — CONDICIONAL**
- Só entra se o cliente fornecer depoimentos autorizados (nome, cargo, empresa). **Não inventar, não usar texto genérico.** Sem depoimentos → seção removida (a ordem segue de H-10 para H-12).
- 1 a 3 cards: citação, nome, cargo, empresa (+ logo). Mobile: empilhados (não carrossel).

**H-12 Perguntas frequentes (objeções do P1)** — *novo em relação ao briefing*
- H2 `[Título: dúvidas de quem contrata]` · accordion com 5 perguntas, todas respondendo às objeções da persona principal:
  1. `[Pergunta: vocês atendem empreendimentos de grande porte?]` — resposta com o caso de 1.800 unidades.
  2. `[Pergunta: atendem minha cidade/estado?]` — UFs + "atendemos remotamente" `[A CONFIRMAR]`.
  3. `[Pergunta: qual o prazo de um projeto?]` `[A CONFIRMAR: prazos típicos]`.
  4. `[Pergunta: trabalham em Revit / no padrão BIM da minha empresa?]` `[A CONFIRMAR: softwares e formatos]`.
  5. `[Pergunta: o que preciso enviar para receber o orçamento?]`.
- Primeira pergunta aberta por padrão. Schema FAQPage. Mobile: largura total, alvo de toque por pergunta ≥ 48 px.

**H-13 CTA final com formulário curto**
- Desktop 2 colunas: à esquerda H2 `[Título: chamada para orçamento]` + 3 bullets do que acontece depois `[Texto: retorno em X dias úteis — A CONFIRMAR]` + link "Prefere WhatsApp?" + botão secundário "Baixar portfólio (PDF)" `[A CONFIRMAR]`; à direita **C21b** (formulário curto, ver 12.3).
- Fundo: **Asset** `marca/portfolio-2024_fundo-capa_5339x3049.jpeg` (textura azul) ou cor sólida — decisão do designer.
- Mobile: título → formulário → WhatsApp → PDF.

---

## 6. Serviços — hub (`/servicos/`)

**Objetivo:** mostrar o escopo completo e distribuir o tráfego para a página certa; servir quem ainda não sabe quais disciplinas precisa. **CTA primário:** Solicitar orçamento.

| # | Seção | Comp. | Detalhe | Mobile |
|---|---|---|---|---|
| SH-01 | Header + breadcrumb | C01, C14 | Início › Serviços | breadcrumb curto |
| SH-02 | Hero interno | C04 | **H1** `[Título: projetos de instalações prediais e infraestrutura — com serviço + cidade para SEO]` · subtítulo `[9 disciplinas, 2D e BIM, para incorporadoras, construtoras e arquitetos]` · [Solicitar orçamento] · [WhatsApp]. Imagem: **Asset** `bim-modelos-3d/portfolio-2024_p05_bim-a_3660x4096.jpeg` (modelo multidisciplinar). | imagem abaixo do texto, recorte 4:3; botões em largura total |
| SH-03 | Índice rápido | — | 3 âncoras para os grupos (chips). | chips com rolagem horizontal |
| SH-04 | Grupo 1: Instalações prediais | C07 | H2 do grupo + intro de 1 frase + 6 cards (ícone, H3 nome, 2 linhas `[descrição]`, "Saiba mais →"). | 1 coluna, cards compactos |
| SH-05 | Grupo 2: Infraestrutura urbana | C07 | H2 + card largo de Infraestrutura de saneamento (água, esgoto, drenagem, aprovação em concessionárias). Imagem: **Asset** `…p09_parque-lagoa-dos-principes-lagoa-nova_MRV…_1920x1280.jpeg` (vista de implantação). | imagem em cima |
| SH-06 | Grupo 3: Eficiência e sustentabilidade | C07 | H2 + 2 cards (Reuso de água pluvial, Aquecimento solar). | 1 coluna |
| SH-07 | Faixa BIM (transversal) | C18 | "Todas as disciplinas em BIM, compatibilizadas" + CTA → `/bim-e-compatibilizacao/`. | empilhado |
| SH-08 | "Não sabe quais projetos precisa?" | C09 | Texto curto para P3/P4 + CTA "Envie o projeto de arquitetura que indicamos as disciplinas" → `/contato/?servico=nao-sei`. | empilhado |
| SH-09 | Como trabalhamos | C10 | mesmo conteúdo da Home H-09. | vertical |
| SH-10 | Logos (12) | C06 | prova social | 3 colunas |
| SH-11 | CTA final | C13 | só botões | empilhado |
| SH-12 | Rodapé | C02 | | |

---

## 7. Modelo de página de serviço individual (`/servicos/[disciplina]/`)

**Objetivo:** ranquear para "[disciplina] + BH/incorporadoras" e converter quem já sabe o que precisa. **CTA primário:** Solicitar orçamento de [disciplina] (com `?servico=`). Um modelo único para as 9 páginas; o conteúdo varia pela tabela 7.2.

### 7.1 Seções
| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| SV-01 | Header + breadcrumb | C01, C14 | Início › Serviços › [Disciplina] | "‹ Serviços" |
| SV-02 | Hero interno | C04 | Eyebrow com o grupo · **H1** `[Título: "Projeto [disciplina] para [público/cidade]"]` · subtítulo `[benefício específico da disciplina, até 25 palavras]` · **[Solicitar orçamento de [disciplina]]** · [WhatsApp] · imagem (ver 7.2) | imagem depois do texto; botões largura total |
| SV-03 | O que entregamos | C09 | H2 · lista de 5–8 entregáveis com ícone de check `[Entregáveis: plantas, memoriais de cálculo, detalhes, quantitativos, ART, modelo BIM… — A CONFIRMAR por disciplina]` | lista de 1 coluna |
| SV-04 | Para quem / quando contratar | — | H2 · 3 cards por tipo de empreendimento (multifamiliar, loteamento, comercial/residência) `[Texto: quando esse projeto é exigido e em que fase contratar]` | 1 coluna |
| SV-05 | Normas e aprovações | C18 | H2 · normas aplicáveis `[A CONFIRMAR: NBRs da disciplina]` · concessionárias/órgãos `[A CONFIRMAR: COPASA, CEMIG, Gasmig, Corpo de Bombeiros…]` · CTA secundário | empilhado |
| SV-06 | Em BIM | C09 + C11 | 1–2 imagens BIM da disciplina + 2 frases + link "Como usamos BIM →" | imagem em cima |
| SV-07 | Projetos com esta disciplina | C08 | 3 cards filtrados pela disciplina + "Ver todos" → `/projetos/?disciplina=[slug]`. **Condicional:** só aparece quando houver ≥ 2 projetos com a disciplina confirmada `[A CONFIRMAR: disciplinas por projeto]`. Sem dados → substituir por faixa de logos C06. | 1 coluna, 2 cards + botão |
| SV-08 | FAQ da disciplina | C12 | 4–6 perguntas (inclui explicação para leigo — P4) | largura total |
| SV-09 | Outros serviços | C07 | demais disciplinas do mesmo grupo + link para o hub | lista compacta |
| SV-10 | CTA final | C13 + C21b | formulário curto com a disciplina pré-marcada (campo oculto) | empilhado |
| SV-11 | Rodapé | C02 | | |

### 7.2 Variáveis por página (conteúdo e assets)
| Página | Grupo | Imagem do hero / SV-06 | Situação do asset |
|---|---|---|---|
| Projeto hidrossanitário | Instalações prediais | `bim-modelos-3d/…p03_bim-hidrossanitario-a…` (shaft com hidrômetros) + `…p04_bim-b…` (esgoto/ventilação de banheiro) | Real |
| Projeto elétrico (Elétrica e Sistemas) | Instalações prediais | `…p06_bim-quadro-eletrico…` | Real |
| Projeto de gás | Instalações prediais | `…p06_bim-tubulacao-gas-ou-hidraulica…` `[A CONFIRMAR: é gás ou hidráulica?]`; alternativa `…p05_bim-b…` | Real, disciplina a confirmar |
| Climatização HVAC | Instalações prediais | — | **PEDIR** modelo BIM de HVAC ao cliente; senão **GERAR** ilustração genérica de equipamento/duto, sinalizada |
| Pressurização de escadas | Instalações prediais | — | **PEDIR** modelo BIM; senão GERAR ilustrativa genérica |
| Projeto de piscina | Instalações prediais | `…p03_bim-hidrossanitario-b…` (casa de bombas) `[A CONFIRMAR: é de piscina?]` | Real se confirmado; senão GERAR |
| Infraestrutura de saneamento | Infraestrutura urbana | `obras-empreendimentos/…p09_parque-lagoa-dos-principes…_1920x1280` ou `…p08_bosque-dos-ipes…` (obra) | Real (foto do empreendimento, não da rede); ideal PEDIR planta/modelo de rede |
| Reuso de água pluvial | Eficiência | — | PEDIR modelo; senão GERAR ilustrativa |
| Aquecimento solar | Eficiência | `…p04_bim-a…` (ramais de água fria/quente) | Real parcial; complementar com GERAR ilustrativa de coletores |

---

## 8. BIM e Compatibilização (`/bim-e-compatibilizacao/`)

**Objetivo:** provar o diferencial BIM com imagens reais e responder às objeções técnicas (software, formatos, padrão do cliente). Público: P1 e P3. **CTA primário:** Solicitar orçamento (com `?servico=compatibilizacao-bim`).

| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| BM-01 | Header + breadcrumb | C01, C14 | Início › BIM e Compatibilização | — |
| BM-02 | Hero interno | C04 | **H1** `[Título: BIM e compatibilização de projetos de instalações]` · subtítulo `[menos conflito na obra, quantitativos precisos]` · [Solicitar orçamento] · [Ver galeria ↓]. Imagem: **Asset** `bim-modelos-3d/…p05_bim-a_3660x4096.jpeg` sobre fundo branco (já é fundo branco). | imagem abaixo, altura máx. 320 px |
| BM-03 | Benefícios | — | 4 cards (ícone + H3 + 1 frase): `[Detecção de interferências antes da obra]` `[Quantitativos confiáveis]` `[Aprovação e execução sem retrabalho]` `[Modelo para manutenção/gestão]` | grade 1 coluna (2×2 em tablet) |
| BM-04 | Como fazemos a compatibilização | C10 | 4–5 etapas `[A CONFIRMAR: ex. recebimento dos modelos → modelagem das instalações → detecção de conflitos → relatório e reuniões → modelo final]` | vertical |
| BM-05 | Galeria de modelos | C11 | **8 imagens reais** (`equipe/fotos/bim-modelos-3d/`, todas) em grade com legenda `[A CONFIRMAR: disciplina de cada modelo]`; clique abre lightbox com setas e Esc. Slot reservado (fase 2) para **visualizador 3D interativo**. | grade 2 colunas; lightbox em tela cheia com swipe |
| BM-06 | Softwares e formatos de entrega | C15 | Tabela/lista: softwares `[A CONFIRMAR: Revit? AltoQi?]` · formatos `[A CONFIRMAR: RVT, IFC, DWG, PDF, NWC…]` · nível de detalhe `[A CONFIRMAR]` · "Trabalhamos no template/padrão BIM da sua empresa" `[A CONFIRMAR]` | lista empilhada |
| BM-07 | 2D x BIM | — | Comparativo de 2 colunas (o que muda na prática). **Opcional** — copywriter decide se agrega. | vira duas listas empilhadas |
| BM-08 | Projetos | C08 | 3 cards (destaques) | 1 coluna |
| BM-09 | FAQ BIM | C12 | 4–5 perguntas | — |
| BM-10 | CTA final | C13 | botões (orçamento + WhatsApp) | empilhado |
| BM-11 | Rodapé | C02 | | |

---

## 9. Projetos — listagem (`/projetos/`)

**Objetivo:** prova social navegável; o coordenador encontra obras parecidas com a dele (UF, porte, cliente). **CTA primário:** Solicitar orçamento (no fim e na barra fixa).

| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| PJ-01 | Header + breadcrumb | C01, C14 | Início › Projetos | — |
| PJ-02 | Hero | C03 (variação baixa, ~50vh) | **H1** `[Título: projetos de instalações em X empreendimentos]` · subtítulo · sem CTA de formulário aqui (evita competir com a exploração); link "Solicitar orçamento" discreto. Imagem: **Asset** `…p13_residencial-pacifico_VILA…_4000x3000.jpeg`. | hero com altura ~45vh, H1 em até 3 linhas |
| PJ-03 | Barra de números | C05 | mesmos números da Home (regras iguais) | 2×2 |
| PJ-04 | Filtros | C22 | **UF** (MG, DF, SP, RJ, MS, SC) · **Cliente** (select com busca) · **Tipo** (só aparece se houver ≥ 2 tipos — hoje todos parecem residenciais multifamiliares `[A CONFIRMAR]`) · **Disciplina** (só se os dados por projeto forem confirmados) · "Limpar filtros" · contador "X projetos". Filtros refletidos na URL (`?uf=mg&cliente=mrv`) para compartilhar e para links das páginas de serviço. Estado vazio: "Nenhum projeto com esses filtros" + "Limpar filtros" + CTA "Fale com a gente sobre seu projeto". | botão **[Filtrar (n)]** fixo no topo da lista → abre bottom sheet com os filtros e botão "Ver X projetos"; chips dos filtros ativos abaixo do botão |
| PJ-05 | Grade de projetos | C08 | 18 cards: foto, H2 do nome (ou H3 dentro de H2 da seção), cliente, cidade/UF, unidades, tags. Ordem padrão: destaques primeiro, depois por UF. Paginação **não** necessária (18 itens); se passar de 24, "Carregar mais". | 1 coluna (2 em tablet) |
| PJ-06 | Clientes (`#clientes`) | C06 completo | H2 `[Título: construtoras e incorporadoras atendidas]` · **24 logos** com nome em `alt` e legenda opcional. Destino do 301 de `/nossos-clientes/`. | grade 3 colunas |
| PJ-07 | Mapa de atuação | C24 | SVG do Brasil com as 6 UFs destacadas + contagem de projetos por UF (clicar numa UF aplica o filtro). Asset: CRIAR SVG. **Opcional** fase 1. | mapa menor + lista de UFs abaixo |
| PJ-08 | CTA final | C13 | "[Título: seu empreendimento pode ser o próximo]" + botões | empilhado |
| PJ-09 | Rodapé | C02 | | |

**Plataforma:** Elementor → Custom Post Type "Projetos" + taxonomias (UF, cliente, tipo, disciplina) + Loop Grid com filtro (Pro) ou JetSmartFilters. Estático → JSON de projetos + filtro em JS no cliente.

---

## 10. Modelo de página de projeto (`/projetos/[empreendimento]/`)

**Objetivo:** provar capacidade com um caso concreto e converter quem tem empreendimento parecido. **CTA primário:** "Tem um empreendimento parecido? Solicite um orçamento" (`?ref=projeto-[slug]`).

| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| PP-01 | Header + breadcrumb | C01, C14 | Início › Projetos › [Nome] | "‹ Projetos" |
| PP-02 | Hero do projeto | C03 | Foto principal larga · **H1** `[Nome do empreendimento]` · linha "[Cliente] · [Cidade/UF]" · crédito da foto `[A CONFIRMAR: crédito exigido pelo cliente]` | foto 4:3 em cima, H1 abaixo (não sobreposto) |
| PP-03 | Ficha técnica | C15 | Cliente (com logo) · Local · Tipo · Nº de unidades · Área `[A CONFIRMAR]` · Ano `[A CONFIRMAR]` · **Disciplinas projetadas** (tags com link para cada serviço) `[A CONFIRMAR]` · Formato (BIM/2D) `[A CONFIRMAR]`. Campo sem dado = linha oculta (nunca "—" ou "N/D"). | lista de 1 coluna, rótulo acima do valor |
| PP-04 | CTA lateral | — | Desktop: card sticky à direita da ficha com o CTA primário + WhatsApp. | vira botão largura total logo após a ficha |
| PP-05 | Desafio e solução | C09 | **Condicional:** H2 "Desafio" + H2 "Solução" + resultado `[A CONFIRMAR: só se o cliente fornecer o case]`. Sem dados → seção oculta. | empilhado |
| PP-06 | Galeria | C11 | Fotos extras e imagens BIM do projeto (se houver). Hoje: **1 foto por projeto** → seção oculta até haver ≥ 2 imagens. | carrossel com swipe |
| PP-07 | Depoimento do cliente | C16 | **Condicional** (só com depoimento real autorizado). | — |
| PP-08 | Projetos relacionados | C08 | 3 cards (mesma UF ou mesmo cliente) | 1 coluna |
| PP-09 | Navegação anterior/próximo | — | "‹ Projeto anterior · Próximo projeto ›" | dois botões em largura total |
| PP-10 | CTA final | C13 | botões | empilhado |
| PP-11 | Rodapé | C02 | | |

**Fotos por projeto:** 12 projetos com foto real (tabela 10.2 do briefing). 3 em alta para hero; os de baixa resolução (Ville Luxemburgo 640×480, Scharle 800×600, Monte Carlo 960×720, Portal do Cerrado 960×540) usam o hero em **largura de conteúdo** (máx. ~960 px), não em tela cheia, para não ficarem borrados.
**6 projetos sem foto** (Alto Boa Vista, Gran Vic Gama, Alto Riviera, Smart Haus, Alto Sobradinho, California Residence): PEDIR fotos/recuperar backup. Até lá: variante sem foto do card e do hero (fundo neutro com nome, cliente e cidade em destaque). Não gerar imagem que se passe pelo empreendimento. `[A CONFIRMAR: unidades de Alto Boa Vista x Gran Vic Gama — ambos 236]`.

---

## 11. Sobre (`/sobre/`)

**Objetivo:** dar confiança (quem assina os projetos, registro, trajetória) e atender a homologação de fornecedor (P2). **CTA primário:** Solicitar orçamento. **Secundário:** baixar portfólio.

| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| SB-01 | Header + breadcrumb | C01, C14 | | |
| SB-02 | Hero interno | C04 | **H1** `[Título: quem somos — engenharia de projetos com atitude]` · subtítulo `[posicionamento]` · imagem: FOTOGRAFAR escritório/equipe; enquanto isso **Asset** `…p08_bosque-dos-ipes…_4000x2250.jpeg` ou textura `marca/portfolio-2024_fundo-capa…`. | imagem abaixo |
| SB-03 | Nossa história | C09 | H2 · 2–3 parágrafos `[A CONFIRMAR: ano de fundação, marcos]` · linha do tempo curta (opcional, só com datas confirmadas) | linha do tempo vertical |
| SB-04 | Responsável técnico | C17 completo | Foto (FOTOGRAFAR) · **Carlos Alberto Grope** · Diretor Técnico · Engenheiro Civil Sanitarista · CREA `[A CONFIRMAR]` · mini-bio `[A CONFIRMAR]` · LinkedIn pessoal `[A CONFIRMAR]` | foto em cima |
| SB-05 | Equipe | — | **Condicional** `[A CONFIRMAR: quem mais aparece — ex. "André" da assinatura de e-mail; fotos]`. Cards: foto, nome, função. Sem fotos reais → seção oculta (não usar banco de imagens nem IA). | grade 2 colunas |
| SB-06 | Números + área de atuação | C05 + C24 | barra de números + mapa das UFs | 2×2 + mapa |
| SB-07 | Como trabalhamos / valores | C10 | processo (mesmo da Home) ou 3–4 valores `[A CONFIRMAR]` | vertical |
| SB-08 | Dados cadastrais (`#dados-cadastrais`) | C15 | Para suprimentos (P2): Razão social `[A CONFIRMAR]` · CNPJ `[A CONFIRMAR]` · CREA empresa `[A CONFIRMAR]` · RT e CREA `[A CONFIRMAR]` · Endereço `[A CONFIRMAR]` · E-mail comercial `[A CONFIRMAR]` · botão **[Baixar portfólio (PDF)]** `[A CONFIRMAR: PDF liberado e atualizado]` | lista de 1 coluna; botão largura total |
| SB-09 | Clientes | C06 | 12 logos + link para `/projetos/#clientes` | 3 colunas |
| SB-10 | CTA final | C13 | botões | |
| SB-11 | Rodapé | C02 | | |

---

## 12. Contato e orçamento (`/contato/`)

**Objetivo:** receber pedidos de orçamento **qualificados** (com dados suficientes para a proposta) e oferecer canais diretos para quem prefere falar. **CTA primário:** enviar o formulário.

### 12.1 Seções
| # | Seção | Comp. | Elementos | Mobile |
|---|---|---|---|---|
| CT-01 | Header + breadcrumb | C01, C14 | sem C19/C20 nesta página | |
| CT-02 | Cabeçalho curto | C04 (sem imagem) | **H1** `[Título: solicite um orçamento]` · subtítulo `[o que acontece depois + prazo de retorno — A CONFIRMAR]` · 3 selos de texto: `[Retorno em X dias úteis]` `[Atendimento direto com o engenheiro]` `[Seus arquivos tratados com sigilo]` | selos em lista compacta |
| CT-03 | Formulário qualificado + canais | C21a | Desktop: formulário (≈ 65%) à esquerda; à direita, coluna **sticky** "Prefere falar agora?" com WhatsApp, telefone, e-mail, endereço, horário (todos com `[A CONFIRMAR]` onde aplicável). | **formulário primeiro**; canais diretos abaixo dele, em cards largos. Link-âncora no topo "Prefere WhatsApp? ↓" |
| CT-04 | O que enviar para um orçamento rápido | C12 | Accordion curto: arquivos úteis (arquitetura em DWG/PDF/RVT, implantação, nº de unidades/pavimentos, fase), sigilo, prazo. | — |
| CT-05 | Endereço e mapa | — | Endereço `[A CONFIRMAR]` + mapa incorporado **só depois da confirmação**; carregar o mapa sob clique (imagem estática + "Abrir no mapa"), por performance e LGPD. Se o atendimento não for presencial `[A CONFIRMAR]`, a seção sai e o endereço fica só no rodapé. | mapa 16:9 |
| CT-06 | Rodapé | C02 | | |

### 12.2 Formulário qualificado C21a (3 etapas)
Formato em **3 etapas** com barra de progresso ("Etapa 1 de 3 — O empreendimento"). Começa pelas perguntas sobre o projeto (menor esforço percebido) e termina nos dados de contato. Botões "Continuar" / "Voltar"; validação por etapa; dados mantidos ao voltar. **Fallback:** se a plataforma não suportar etapas, o mesmo formulário em uma página com 3 blocos `fieldset` e títulos.

**Etapa 1 — O empreendimento**
| Campo | Tipo | Obrig. | Opções / regras |
|---|---|---|---|
| Tipo de empreendimento | Radio em cards (ícone + rótulo) | Sim | Residencial multifamiliar · Loteamento / condomínio horizontal · Comercial / corporativo · Residência unifamiliar `[A CONFIRMAR: público P4]` · Infraestrutura urbana (redes) · Outro (abre campo de texto) |
| Cidade | Texto com autocomplete opcional | Sim | — |
| UF | Select (27 UFs) | Sim | MG pré-selecionada? Não: deixar "Selecione" |
| Nº de unidades | Número | Condicional | Aparece se tipo = multifamiliar ou loteamento. Checkbox "Ainda não definido" |
| Área construída aproximada (m²) | Número | Não | Aparece para comercial, residência e outro |
| Fase atual | Select | Não | Estudo de viabilidade · Arquitetura em desenvolvimento · Projeto legal aprovado · Projeto executivo · Obra em andamento `[A CONFIRMAR lista com o cliente]` |

**Etapa 2 — Escopo**
| Campo | Tipo | Obrig. | Opções / regras |
|---|---|---|---|
| Disciplinas | Checkboxes (multiseleção) agrupadas nos 3 grupos | Sim (≥ 1) | Hidrossanitário · Elétrica e sistemas · Gás · HVAC · Pressurização de escadas · Piscina · Infraestrutura de saneamento · Reuso pluvial · Aquecimento solar · Compatibilização BIM · **"Ainda não sei — quero orientação"** (desmarca as outras). Pré-marcadas por `?servico=` |
| Formato de entrega | Radio | Não | BIM (Revit/IFC) · 2D (DWG) · Indiferente `[A CONFIRMAR: formatos]` |
| Prazo desejado | Select | Sim | Até 30 dias · 1 a 3 meses · 3 a 6 meses · Sem prazo definido `[A CONFIRMAR faixas]` |
| Link dos arquivos | URL | Não | Ajuda: "Google Drive, WeTransfer, Dropbox…" |
| Envio de arquivos | Upload múltiplo | Não | PDF, DWG, RVT, IFC, ZIP · limite `[A CONFIRMAR: ex. 20 MB por envio — depende da plataforma/e-mail]` · texto de ajuda: "Arquivos grandes? Use o link acima." |
| Mensagem | Textarea | Não | Placeholder com exemplo do que contar |

**Etapa 3 — Seus dados**
| Campo | Tipo | Obrig. | Regras |
|---|---|---|---|
| Nome completo | Texto | Sim | `autocomplete="name"` |
| Empresa | Texto | Não | Ajuda: "Opcional para pessoa física" |
| Cargo | Texto | Não | — |
| E-mail | E-mail | Sim | `autocomplete="email"`, validação de formato |
| WhatsApp / telefone | Tel com máscara (DDD) | Sim | `autocomplete="tel"`, `inputmode="tel"` |
| Como nos conheceu | Select | Não | Google · Indicação · LinkedIn · Já sou cliente · Outro |
| Consentimento LGPD | Checkbox | Sim | "Concordo com o uso dos meus dados para receber o orçamento, conforme a [Política de privacidade]." Desmarcado por padrão |
| Receber novidades | Checkbox | Não | Desmarcado por padrão (só se houver comunicação; senão remover) |

**Campos ocultos:** `servico` (do parâmetro), `ref` (página/projeto de origem), `utm_source/medium/campaign`, página de origem, honeypot anti-spam (+ reCAPTCHA invisível ou Turnstile, a definir pela plataforma).
**Botão final:** "[Enviar pedido de orçamento]" (texto final com o copywriter). Abaixo: "Resposta em até X dias úteis `[A CONFIRMAR]`".
**Erros:** mensagem por campo, abaixo dele, em texto (não só cor); foco vai para o primeiro erro; resumo de erros no topo da etapa.
**Envio:** e-mail para `[A CONFIRMAR: destinatário dos leads]` + cópia de confirmação ao usuário; evento GA4 `form_submit`; redireciona para `/obrigado/`.
**Mobile:** campos em largura total, altura ≥ 48 px, rótulo sempre visível acima do campo (nunca só placeholder), teclado adequado por tipo, botão "Continuar" largura total. Cards de tipo em 1 coluna.

### 12.3 Formulário curto C21b (CTA finais da Home e dos serviços)
Nome* · E-mail* · WhatsApp* · Empresa · Cidade/UF do empreendimento · Mensagem · LGPD* · ocultos (`servico`, origem). Botão "[Solicitar orçamento]". Envia para o mesmo destino com rótulo `orcamento_rapido`; a página `/obrigado/` convida a complementar com arquivos (link para `/contato/`).

### 12.4 `/obrigado/` (novo, noindex)
H1 `[Título: recebemos seu pedido]` · próximos passos (3 itens, com prazo `[A CONFIRMAR]`) · "Quer adiantar? Envie os arquivos pelo WhatsApp" · links Projetos e Portfólio PDF. Sem C20. Ponto de disparo de conversão no GA4/Ads.

---

## 13. 404

**Objetivo:** não perder o visitante (as URLs antigas têm 301; a 404 pega links quebrados de terceiros e do PDF).
| # | Seção | Elementos | Mobile |
|---|---|---|---|
| 404-01 | Header | C01 normal | |
| 404-02 | Mensagem | **H1** `[Título: página não encontrada]` · 1 frase `[Texto: o endereço pode ter mudado com o novo site]` | centralizado |
| 404-03 | Atalhos | 3 cards grandes: **Serviços** · **Projetos** · **Solicitar orçamento** (primário) + link "Voltar para o início" + "Falar no WhatsApp" | cards em 1 coluna, largura total |
| 404-04 | Rodapé | C02 | |

Sem busca interna (o site não terá busca na fase 1). Status HTTP 404 real (não redirecionar para a home).

---

## 14. Política de privacidade (`/politica-de-privacidade/`)
Modelo de texto longo (sem wireframe próprio): breadcrumb · H1 · data de atualização · sumário com âncoras (H2 por tópico: dados coletados, finalidade, base legal, compartilhamento, cookies, direitos do titular, contato do encarregado `[A CONFIRMAR]`) · largura de leitura máx. ~720 px · CTA final só com link de contato. **Texto jurídico:** o copywriter faz uma minuta e o cliente valida; não publicar sem revisão.

---

## 15. Regras globais de layout e acessibilidade (para design e QA)
- **Mobile-first:** projetado a partir de 375 px; breakpoints sugeridos 375 / 768 / 1024 / 1440. Conteúdo com largura máx. ~1200 px.
- **Um H1 por página**; H2 por seção; H3 nos cards. Nenhum título usado só por tamanho visual.
- **Alvos de toque ≥ 44 px** (48 px recomendados nos formulários e menu).
- **Contraste:** o laranja da marca (#F15A29) não serve para texto pequeno nem para botão com texto branco pequeno (ver briefing 7.2) — decisão do designer, mas os wireframes reservam o CTA primário como elemento de maior peso visual de cada tela.
- **Imagens:** `alt` descritivo (logos = nome do cliente; fotos = "Empreendimento X, cidade, vista aérea"); WebP/AVIF responsivo; lazy-load abaixo da dobra; hero com prioridade.
- **Sem carrossel automático** em nenhuma seção. Carrosséis só com swipe/controle manual.
- **Animações** respeitam `prefers-reduced-motion`.
- **Seções condicionais** (depoimentos, equipe, desafio/solução, galeria de projeto, projetos por disciplina, mapa, LinkedIn, PDF): somem por completo quando o dado não existir. Nunca publicar placeholder.

---

## 16. Mudanças e decisões em relação ao briefing

**Acrescentado**
1. **`/obrigado/`** (noindex): confirma o envio, orienta próximos passos e dá um ponto limpo de conversão para GA4/Ads.
2. **FAQ de objeções na Home (H-12)** entre o responsável técnico e o CTA final, respondendo às 4 objeções da persona P1 (escala, cidade, prazo, Revit/BIM) + "o que enviar".
3. **Bloco "Dados cadastrais" em `/sobre/#dados-cadastrais`** para a persona P2 (suprimentos), com download do portfólio.
4. **Formulário em 3 etapas** (empreendimento → escopo → dados), com pré-marcação de disciplina por `?servico=` e origem por `?ref=`. Mais um **formulário curto** nos CTA finais da Home e dos serviços.
5. **Filtro "Disciplina"** em Projetos (condicional aos dados) e regra de esconder o filtro "Tipo" enquanto houver um único tipo.
6. **Seção "Não sabe quais projetos precisa?"** no hub de serviços (P3/P4), com opção "Ainda não sei" no formulário.
7. **Mapa de atuação** (SVG das UFs) em Projetos e Sobre — opcional na fase 1.

**Ajustado**
8. **WhatsApp no mobile:** a barra fixa inferior (Orçamento + WhatsApp) substitui o botão flutuante; o flutuante fica só no desktop. O ícone de WhatsApp do header fica só no desktop (no mobile está no drawer e na barra).
9. **Logos na Home:** 12 em grade estática (não os 24, não carrossel), com link para os 24 em `/projetos/#clientes`.
10. **Projetos em destaque no mobile:** 3 cards + botão, em vez de 6.
11. **Depoimentos, equipe, desafio/solução e galeria do projeto** viraram seções **condicionais** (só entram com dado real).

**Mantido como aprovado:** menu (Serviços · BIM · Projetos · Sobre · Contato + "Solicitar orçamento" + WhatsApp), fim da página Clientes, hub em 3 grupos, slugs, 301s, `/bim-e-compatibilizacao/` na raiz, política de privacidade e 404.

---

## 17. Pendências que afetam a estrutura (para o coordenador levar ao cliente)
| # | Pendência | Afeta | Se não vier até o lançamento |
|---|---|---|---|
| 1 | Endereço correto e se há atendimento presencial | Rodapé, Contato CT-05, Sobre SB-08, schema | Rodapé sem endereço; CT-05 removida |
| 2 | E-mail destino dos leads | Formulários, rodapé | **Bloqueia** o lançamento dos formulários |
| 3 | Números institucionais (ano, empreendimentos, unidades) | H-03, PJ-03, SB-06, microprova do hero | Só itens confirmados (mín. 3: 6 UFs, 24 clientes, 18 empreendimentos documentados) |
| 4 | CNPJ, razão social, CREA (empresa e RT) | Rodapé, SB-04, SB-08 | Linhas ocultas; SB-08 reduzida |
| 5 | Disciplinas por projeto | Tags dos cards, PP-03, SV-07, filtro Disciplina | Tags ocultas; SV-07 vira faixa de logos; filtro sai |
| 6 | Fotos dos 6 projetos do site antigo e direito de uso das 12 fotos | PJ-05, PP-02 | Variante sem foto; se não houver direito de uso, **toda** a estratégia visual de projetos precisa ser revista |
| 7 | Logos em PNG/SVG + autorização | H-04, PJ-06 | Redesenho monocromático, se autorizado |
| 8 | Foto do RT e da equipe | H-10, SB-04, SB-05 | Variante sem foto; SB-05 removida |
| 9 | Etapas do processo e prazo de resposta | H-09, BM-04, CT-02, `/obrigado/` | Copy genérica sem prazo numérico |
| 10 | Softwares, formatos BIM, concessionárias em que aprovaram | BM-06, SV-05, H-06, H-12 | Itens genéricos sem nomes |
| 11 | Disciplina exata de cada imagem BIM (p04/p05/p06 "gás ou hidráulica") | Legendas, SV-06 | Legenda genérica "Modelo BIM de instalações" |
| 12 | Modelos BIM de HVAC, pressurização, piscina, reuso, solar | Hero de 4–5 páginas de serviço | Ilustração GERADA e sinalizada |
| 13 | Portfólio PDF liberado/atualizado | Rodapé, H-13, SB-08, `/obrigado/` | Botões de download removidos |
| 14 | Público P4 (residências particulares) interessa? | Opção do formulário, tom das FAQs de piscina/solar | Opção "Residência unifamiliar" sai do formulário |
| 15 | URL do LinkedIn | Rodapé | Ícone removido |
| 16 | Depoimentos autorizados | H-11, PP-07 | Seções removidas |
| 17 | Plataforma (WP+Elementor x estático) | Implementação de filtros, etapas do formulário, upload | Nenhuma mudança de estrutura; só de implementação |
