# 05 — Validação UX/UI: Intrépida Engenharia e Projetos

> Etapa: Validação UX/UI (agente `validador-ux-ui`). Data: 21/11/2026. Rodada 1.
> Objeto: protótipo HTML em `site/`, servido em `http://localhost:8770/` (modo revisão ativo).
> Base: `01-contexto.md`, `02-wireframe.md`, `03-copy.md` e `04-design-system.md`.
> Evidências: `equipe/screenshots-validacao/` (44 arquivos) e medições por script (descritas na seção 5).
> Selos amarelos "PLACEHOLDER" e "Imagem ilustrativa" são intencionais e não contam como problema.

---

> **Atualização (rodada 2, 21/11/2026):** os itens UX-01 a UX-09 foram revalidados e o veredito final está na **seção 7**: **APROVADO COM AJUSTES**, liberado para o `revisor-qa`. Não há Críticos nem Altos em aberto. Há 1 regressão de nível Médio (hifenização dos títulos, REG-01).

## 1. Veredito (rodada 1)

**APROVADO COM AJUSTES**

A estrutura, a navegação, a jornada até o orçamento e o formulário em 3 etapas estão sólidos. A varredura técnica saiu limpa: 37 URLs com status 200, 1 H1 por página, nenhuma imagem sem `alt`, nenhum link interno quebrado e nenhum erro de console.

Há **0 itens Críticos e 3 Altos**. Os três são de CSS e foram confirmados por medição:
- dois são falhas de contraste WCAG em texto visível em muitas páginas;
- um é um defeito visual no cartão de projeto, o principal elemento de prova do site.

Pelo fluxo da equipe, os 3 itens Altos voltam ao `webdesigner-senior` e precisam ser revalidados antes do `revisor-qa`. Os itens Médios podem ser feitos na mesma rodada. Alguns dependem de dados do cliente: disciplinas por projeto, CNPJ/CREA e dados da Política.

---

## 2. Notas por categoria (0–10)

| # | Categoria | Nota | Resumo |
|---|---|---|---|
| 1 | Clareza (teste dos 5 segundos) | **8,5** | Em 375 px e em 1440 px a primeira dobra já diz o que é, para quem e qual é o próximo passo: H1 com o serviço e o público, CTA laranja e WhatsApp. O rótulo do hero, que dá a localização, está quase ilegível (UX-01). |
| 2 | Heurísticas de Nielsen | **8,0** | Bom status do sistema (etapas, contador de filtros, "Enviando…"), prevenção de erro e estados vazios. Pontos fracos: erro de grupo sem texto (UX-06) e mensagem de falha sem atalho clicável (UX-13). |
| 3 | Jornada de conversão | **8,0** | Orçamento a 1 clique de qualquer página. `?servico=` pré-marca a disciplina e o WhatsApp leva mensagem por contexto. A barra C20 e o C19 se comportam como especificado. Perdas: texto de apoio do CTA final invisível em 23 páginas (UX-02), banner de cookies cobrindo o CTA no mobile (UX-08) e cases rasos (UX-10). |
| 4 | Hierarquia visual e UI | **7,0** | Sistema "prancha técnica" consistente, ritmo de seções bom e estados de botão e foco completos. Os cartões de projeto ficam com faixa azul sob a foto (UX-03). O CTA final com textura perde legibilidade (UX-02 e UX-04). |
| 5 | Acessibilidade (WCAG 2.1 AA) | **6,0** | Base boa: skip link, foco visível, drawer, lightbox e bottom sheet com foco preso e Esc, `lang`, H1 único, `alt`. Há 3 falhas de contraste reais (UX-01, UX-02, UX-04), uma de reflow em 320 px (UX-05), uma de Label in Name (UX-09) e erros sem associação programática (UX-07). |
| 6 | Responsividade | **7,5** | Nenhum scroll horizontal em 375, 768, 1024 e 1440. Menu mobile, filtros em bottom sheet e barra fixa funcionam. Em 320 px há H2 cortado (UX-05), e a faixa nos cards aparece em todas as larguras (UX-03). |
| 7 | Formulários | **8,0** | Formulário em 3 etapas bem resolvido:<br>• validação por etapa e resumo de erros com links;<br>• foco no 1º erro e dados mantidos ao voltar;<br>• máscara de telefone e "Ainda não sei" exclusivo;<br>• estados "Enviando…" e falha, com redirecionamento para `/obrigado/`.<br>Ajustes em UX-06, UX-07, UX-13 e UX-14. |
| 8 | Confiança | **7,0** | Prova forte: 24 logos, 18 empreendimentos, números, mapa de UFs e fotos reais. Faltam CNPJ, CREA e PDF para a homologação (UX-11), disciplinas nos cases (UX-10) e a Política tem pendências (UX-12). A foto do RT ainda é placeholder, como já previsto. |
| | **Nota geral** | **7,5** | |

---

## 3. Tabela de problemas

Severidade:
- **Crítica**: impede um objetivo do briefing.
- **Alta**: prejudica de forma relevante conversão, credibilidade ou conformidade AA em escala.
- **Média**: atrito ou falha pontual.
- **Baixa**: polimento.

| ID | Página/Seção | Problema | Evidência | Severidade | Correção recomendada | Responsável |
|---|---|---|---|---|---|---|
| **UX-01** | Home (hero C03, rótulo "ENGENHARIA DE PROJETOS · BELO HORIZONTE/MG") e `/projetos/` (rótulo "PORTFÓLIO") | O *eyebrow* do hero usa `#196291` (azul de link) sobre a pílula escura `rgba(6,31,51,.82)`. O contraste fica em **2,44:1** (pixel medido no screenshot de 375 px) e **2,55:1** (cálculo sobre navy). O mínimo é 4,5:1 (13 px, peso 700). A regra `.on-dark .eyebrow` (`#FFC3AD`) não pega porque o `.c03-hero` não tem a classe `on-dark`. Acontece em 375, 768 e 1440 px. | `02-home-375-dobra.png`, `33-home-1440-dobra.png`, `39-projetos-375-dobra-eyebrow.png`. Script: `color: rgb(25,98,145)`, `bg: rgba(6,31,51,.82)` → 2,55:1. Pixel: texto (25,98,145) × fundo (13,35,54) → 2,44:1. | **Alta** | Acrescentar `.c03-hero .eyebrow { color: #FFC3AD; }`, que dá **10,9:1** sobre a pílula. Outra opção é aplicar `on-dark` no `.c03-hero` e conferir se os outros estilos `on-dark` (foco escuro) servem ali. No Elementor, ajustar o template `C03 – Hero foto`. | webdesigner-senior |
| **UX-02** | CTA final C13 (variação botões) em **23 páginas**: as 18 de projeto, `/projetos/`, `/sobre/`, `/bim-e-compatibilizacao/`, `/servicos/` e o hub | O parágrafo `.lead` do CTA final ("Conte sobre ele e receba uma proposta…", "Conte o porte, a cidade…") fica em `#3A4552` (cinza escuro) sobre a textura azul. O contraste é **1,47:1** contra o navy-900 e 2,54:1 contra as faixas claras. Na prática o texto fica invisível. Causa: `.lead` só é sobrescrito em `.bg-navy`, não em `.on-dark`. | `41-projeto-1440-cta-lead-ilegivel.png`. Também visível no fim de `16-projetos-375-pagina.png` e `21-proj-semfoto-375-pagina.png`. Script nas 5 páginas-modelo: `color=58,69,82`, 1,47:1. | **Alta** | `.on-dark .lead { color: var(--c-on-dark-muted); }` (#BFD0DF, 9,1:1 sobre navy-900), somado ao reforço do UX-04 sobre a textura. Revisar no Kit do Elementor a cor de texto da seção `C13 – CTA botões`. | webdesigner-senior |
| **UX-03** | Card de projeto C08 (Home H-08, `/projetos/`, "Outros projetos" nas páginas de projeto) | A foto não preenche a moldura 3:2. O `<picture>` não tem altura, então o `img { height:100% }` vira `auto`. Resultado: fotos 16:9 deixam uma **faixa azul de 39 px** embaixo e fotos 4:3 ficam cortadas só na base (−31 px). Na Home são 3 de 6 cards com faixa (Mirante São Lucas, Bosque dos Ipês, Alta Vista). A aparência é de imagem quebrada no principal bloco de prova. | `40-projetos-1440-faixa-azul-cards.png`, `16-projetos-375-pagina.png`, `05-home-1440-pagina.png`. Script em 1440: diferença moldura − imagem = `[39, 39, -31, 0, 39, -31]` px. Em 375, `.c08-card__media` 340×227 e img 340×191. | **Alta** | `.c08-card__media picture { display:block; height:100%; }` e `.c08-card__media img { width:100%; height:100%; object-fit:cover; }`. No Elementor (Loop Item), usar *Image Size: custom* com proporção fixa e *object-fit: cover*. Conferir o mesmo padrão nas outras imagens com `<picture>` dentro de moldura de proporção fixa. | webdesigner-senior |
| **UX-04** | CTA final com formulário C13+C21b (Home e as 9 páginas de serviço): coluna de texto à esquerda | Os passos 1-2-3 ("Analisamos as informações…") estão em `#BFD0DF` direto sobre a textura `fundo-azul`, sem sobreposição. No fundo médio o contraste é 5,05:1. Onde o texto cruza as faixas diagonais claras da textura cai para **2,43:1**. | `42-home-1440-cta-textura.png`. Medição por pixel no screenshot 1440: percentil 50 do fundo = 5,05:1, percentil 90 = 2,43:1. | **Média** | Pôr uma camada navy-900 com 75–85% de opacidade atrás da coluna de texto (ou da seção inteira) ou recortar a textura para que as faixas claras não passem sob o texto. Vale também para o lead do UX-02. | webdesigner-senior |
| **UX-05** | `/servicos/infraestrutura-de-saneamento/` (H2 "Redes compatibilizadas com o empreendimento") e `/servicos/pressurizacao-de-escadas/` (H2 "Pressurização em BIM"), em 320 px | Falha de reflow (WCAG 1.4.10, exige 320 px). A palavra longa no H2 (26 px) não cabe na coluna `.sv06-txt` (235 px) e estoura **52 px** e 3 px, respectivamente. O `body { overflow-x:hidden }` mascara o scroll e **corta** o texto. Quando há rolagem programática, a página inteira fica deslocada para a esquerda. Em 375, 768, 1024 e 1440 px não há overflow. | `43-infra-320-h2-cortado.png` (página deslocada e texto cortado à esquerda). Script: `scrollWidth 372 > 320`, culpado `H2 … right 372`. | **Média** | Nos títulos: `overflow-wrap: anywhere; hyphens: auto;` (o `lang="pt-BR"` já está no HTML). Também `min-width:0` nos itens flex/grid e reduzir `--fs-h2` abaixo de 360 px. Não depender de `overflow-x:hidden` no `body` para esconder estouro. | webdesigner-senior |
| **UX-06** | `/contato/`, etapa 2 ("Quais projetos você precisa?") | Sem nenhuma disciplina marcada, o grupo recebe a borda de erro, mas a mensagem abaixo do grupo sai **vazia**: só aparece o ícone "!". A frase existe só no resumo do topo. `groupCheck()` não preenche o `.err`. | `44-contato-375-erro-disciplinas-vazio.png`. Script: `.err` do grupo com `textContent === ""`, `display:flex`, 19 px de altura. | **Média** | Em `groupCheck`, gravar a mensagem `data-req` no `.err` do grupo, como já faz o `setErr`. No Elementor Pro Form, conferir se a mensagem do campo *checkbox* obrigatório aparece. | webdesigner-senior |
| **UX-07** | Formulários C21a e C21b (todas as páginas com formulário) | 1. As mensagens de erro não estão ligadas ao campo: o `.err` não tem `id` e o campo não tem `aria-describedby` apontando para ele.<br>2. Cada `.err` tem `role="alert"`. Com 3 ou 4 erros juntos, o leitor de tela dispara vários alertas ao mesmo tempo, além do foco no 1º campo.<br>3. Os campos obrigatórios não têm `required` nem `aria-required`. A instrução "Todos os campos são obrigatórios, exceto…" é só visual. | Script após "Continuar" vazio: `aria-invalid=true` com `aria-describedby=null` em `tipo`, `cidade` e `uf`. Marcação: `<p class="err" role="alert">`. | **Média** | Dar `id` a cada `.err` e incluí-lo em `aria-describedby` quando houver erro. Tirar o `role="alert"` das mensagens individuais (deixar `aria-live` só no resumo). Adicionar `aria-required="true"` (ou `required` com `novalidate`). | webdesigner-senior |
| **UX-08** | Banner de cookies C23, mobile (todas as páginas, 1ª visita) | No mobile o cartão ocupa **~40% da tela** (y 478 a 795 em 812 px). Ele cobre o lead e os dois CTAs do hero na primeira visita, justamente quando o visitante decide se fica. São 3 botões empilhados de largura total. | `01-home-375-dobra-cookies.png`, `37-hvac-375-dobra.png`. | **Média** | Versão compacta no mobile: texto em até 2 linhas, "Aceitar" e "Recusar" lado a lado com o mesmo peso e "Configurar" como link. Meta: ≤ 25% da altura da tela. Manter o mesmo peso visual entre aceitar e recusar (exigência da LGPD). | webdesigner-senior |
| **UX-09** | Home (grupos de serviço C07), possivelmente o hub `/servicos/` | Falha de *Label in Name* (WCAG 2.5.3, nível A): o nome acessível não contém o texto visível. O card "Elétrica e Sistemas" tem `aria-label="Saiba mais sobre o projeto elétrico e de sistemas"`. O card "Reúso de água pluvial" tem `aria-label="…projeto de aproveitamento de água de chuva"`. Quem usa controle por voz e diz "clicar Reúso de água pluvial" não aciona o link. | Script de varredura dos `aria-label` × texto visível (2 ocorrências na Home). | **Média** | Começar o `aria-label` com o texto visível ("Reúso de água pluvial: saiba mais…") ou remover o `aria-label` e deixar o texto do card como nome. | webdesigner-senior (texto com copywriter) |
| **UX-10** | Páginas de projeto `/projetos/[slug]/` (as 18) | Os cases estão rasos. A ficha técnica traz só Cliente, Local e Unidades, e o texto é genérico ("desenvolveu projetos de engenharia para o empreendimento"). Não diz **quais disciplinas** a Intrépida projetou, que é a pergunta central da P1 ("já fizeram hidrossanitário/infra para obra desse porte?"). Sem isso o case não ajuda a página de serviço (prova por disciplina). | `20-proj-foto-1440-pagina.png`, `22-proj-semfoto-1440-pagina.png`. HTML do C15: `Cliente / Local / Unidades`, em projeto com e sem foto. | **Média** | Levantar com o cliente (ou no portfólio PDF) as disciplinas por empreendimento. Incluir a linha "Disciplinas" no C15, com link para as páginas de serviço, e uma frase específica por projeto. Sem esse dado, ao menos trocar a frase genérica por algo útil (porte, tipologia, concessionária). | copywriter (dado: contexto-site / cliente) |
| **UX-11** | `/sobre/`, "Dados para cadastro de fornecedor" | O texto de abertura promete "os dados da empresa e **o portfólio em PDF**", mas o PDF não existe na página. Também faltam razão social, CNPJ e registro no CREA. O fluxo F4 (P2, homologação) não se completa. | `24-sobre-1440-pagina.png` (bloco "Dados para cadastro de fornecedor"). | **Média** | Tornar a frase condicional ao PDF (tirar a menção enquanto ele não existir). Levar ao cliente o pedido de CNPJ, razão social, CREA e PDF. Até lá, o e-mail para documentação basta. | copywriter (dados: contexto-site / cliente) |
| **UX-12** | `/politica-de-privacidade/` | Há 24 marcações pendentes ([razão social], [CNPJ], [data da publicação], ferramentas de medição, reCAPTCHA/Turnstile, comunicação). Do jeito que está, não pode ser publicada, e o consentimento do formulário remete a ela. | `31-politica-1440-pagina.png`. Script: 24 ocorrências de marcação pendente. | **Média** | Fechar os dados com o cliente e validar o texto jurídico antes do QA final. É bloqueio de publicação, não de layout. | copywriter (dados: contexto-site / cliente) |
| **UX-13** | `/contato/` com falha de envio (`?simular=falha`) | O alerta de falha está correto (`role="alert"`, recebe foco, mantém os dados). Mas cita "WhatsApp (31) 99649-8629" como texto simples, sem link. No momento de frustração, a saída exige copiar o número. | Script: `.form-fail` visível, foco nele, `failLinks: []`. | **Baixa** | Transformar o número em link `wa.me` com mensagem pronta ("Tentei enviar o formulário e deu erro…"). | webdesigner-senior |
| **UX-14** | `/contato/`, etapa 2, campo "Link dos arquivos" | O campo rejeita links colados sem protocolo (ex.: `drive.google.com/...`) com "Cole um link completo, começando com https://". É um atrito evitável num campo opcional. | Script: valor `drive.google.com/x` → erro. | **Baixa** | Acrescentar `https://` automaticamente quando faltar e aceitar `http://`. | webdesigner-senior |
| **UX-15** | Home, microprova do hero, 375 px | O separador "·" quebra sozinho no começo da 2ª linha, desalinhado ("· Empreendimentos em 6 estados"). | `02-home-375-dobra.png`. | **Baixa** | Esconder o separador abaixo de 768 px e usar `gap` e quebra natural (um item por linha). | webdesigner-senior |
| **UX-16** | Global (foco) | O foco é desenhado só com `box-shadow` (`:focus-visible { outline:none; box-shadow: var(--focus) }`). No modo de alto contraste do Windows (forced-colors), sombras são removidas e o foco some. O foco dos campos é um halo de 25% de opacidade, que fica fraco. | `site.css` linhas 96 e 567. Tab real na Home: anel presente em 16 de 16 paradas (modo normal). | **Baixa** | Somar `outline: 2px solid transparent; outline-offset: 2px;` (aparece em forced-colors) ou usar `@media (forced-colors: active)` com `outline`. Halo do campo com ≥ 3:1 contra o fundo. | webdesigner-senior |
| **UX-17** | Rodapé e consentimento LGPD | Há alvos menores que o padrão do próprio DS (≥ 44 px):<br>• links de WhatsApp, telefone e e-mail do rodapé com **24 px** de altura;<br>• link "Política de privacidade" no texto do consentimento com **18 px**.<br>Não falha a 2.1 AA, mas contraria o DS 5.1 e a 2.5.8 (2.2). | Script de altura dos links na Home em 375 px. | **Baixa** | `min-height: 44px` com `display:inline-flex; align-items:center` nos links de contato do rodapé. O link inline do consentimento pode ficar, desde que o checkbox tenha área ≥ 44 px (já tem). | webdesigner-senior |
| **UX-18** | Faixa de logos C06 (Home, Sobre, Projetos) | O logo da Mello Azevedo é um raster pequeno com fundo próprio, ilegível em todas as larguras. Destoa dos demais logos monocromáticos. O caso Chandon já está registrado no DS 11.4. | `05-home-1440-pagina.png`, `24-sobre-1440-pagina.png`. | **Baixa** | Pedir o vetor ao cliente. Até lá, usar o nome em texto no mesmo estilo monocromático. | webdesigner-senior (asset: contexto-site) |
| **UX-19** | `/projetos/`, filtro "Cliente" | "Prix Construtora" e "Prix Engenharia" aparecem como clientes diferentes e dividem os 3 projetos da Prix. A pendência já está registrada no copy. | Opções do `#f-cliente` (14 opções). | **Baixa** | Confirmar o nome com o cliente e unificar. | copywriter |
| **UX-20** | Banner de cookies C23 | Depois de "Aceitar" ou "Recusar", o foco não vai para nenhum lugar (fica no `body`). Quem navega por teclado precisa recomeçar do topo sem referência. | Leitura de `site.js` (função `save()` não move o foco) e teste no navegador. | **Baixa** | Devolver o foco ao elemento que tinha foco antes do banner ou ao link "Pular para o conteúdo". Se o banner foi reaberto pelo rodapé, devolver ao link "Preferências de cookies". | webdesigner-senior |
| **UX-21** | Páginas de projeto | O mesmo CTA "Tem um empreendimento parecido?", com os mesmos dois botões, aparece duas vezes: no card lateral e no C13 final. A repetição enfraquece o fechamento. | `21-proj-semfoto-375-pagina.png`, `22-proj-semfoto-1440-pagina.png`. | **Baixa** | Manter o card lateral (contextual) e trocar o C13 final pela versão com formulário curto (C21b). Outra opção é variar o título final para algo como "Seu empreendimento pode ser o próximo". | wireframe |
| **UX-22** | `/projetos/`, filtros C22 | Os filtros permitem combinações sem resultado (ex.: DF + MRV → "Nenhum projeto"). O estado vazio está bem resolvido (2 saídas), mas o usuário só descobre depois de escolher. | Teste: `?uf=df&cliente=MRV` → 0 cards e estado vazio. | **Baixa** | Mostrar a contagem por opção ("MRV (1)") e desabilitar as opções que zeram o resultado com o filtro atual. | webdesigner-senior |
| **UX-23** | Migração WordPress (404 e `/obrigado/`) | 1. No protótipo, uma URL inexistente devolve a 404 padrão do servidor, não a `404.html`.<br>2. `/obrigado/` afirma "Enviamos uma cópia do pedido para o seu e-mail".<br>No WordPress, os dois pontos precisam ser verdade. | Teste: `/nao-existe/` → 404 genérica. Texto de `/obrigado/`. | **Baixa** | No WP: template 404 do tema com status HTTP 404 real. No Elementor Pro Form, ativar o "Email 2" (cópia ao usuário) ou ajustar o texto. Validar também com `REVISAO = False` (sem selos) antes do QA. | webdesigner-senior |

**Total:** 0 Críticos · 3 Altos · 9 Médios · 11 Baixos.

---

## 4. Pontos fortes

- **Mensagem clara e voltada a B2B:** H1 com serviço e público, prova numérica logo abaixo do hero (24 · 18 · 6 · +5.800) e logos reais. O tom é técnico, de engenheiro para engenheiro.
- **Jornada curta e contextual:**
  - CTA de orçamento a 1 clique em todas as páginas;
  - `?servico=hidrossanitario` pré-marca a disciplina;
  - mensagens de WhatsApp por página ("página: Projeto hidrossanitário", "Vi o projeto Alto Boa Vista…");
  - C20 aparece só depois do hero e some em `/contato/` e `/obrigado/`.
- **Formulário qualificado bem executado:**
  - 3 etapas com progresso anunciado (`aria-live`);
  - foco no H2 da etapa e no 1º erro;
  - resumo de erros com links e dados mantidos ao voltar;
  - campos condicionais por tipo e máscara de telefone;
  - "Ainda não sei" exclusivo, estados de envio e falha;
  - redirecionamento para `/obrigado/` com conteúdo extra para quem veio do formulário curto.
- **Componentes acessíveis no essencial:**
  - drawer mobile com foco preso, Esc e retorno do foco ao gatilho;
  - mega-menu com Enter e Esc;
  - lightbox BIM com `role=dialog`, contador, setas e Esc;
  - bottom sheet de filtros e skip link;
  - `lang="pt-BR"`, H1 único e `alt` descritivos (ilustrações com "(imagem ilustrativa)").
- **Uso honesto de imagem:** as ilustrações de IA trazem selo e nota "Gerada por IA · não é projeto da Intrépida". Modelos BIM reais aparecem em moldura própria.
- **Placeholders bem contidos:** os selos são sobrepostos e não deslocam o layout. A variação "sem foto" do projeto (textura + símbolo + nome) e o bloco do RT funcionam visualmente com e sem os selos.
- **Base técnica limpa:** sem erros de console, sem links ou assets quebrados, sem scroll horizontal nas 4 larguras-alvo, `.reveal` com fallback `no-js` e `prefers-reduced-motion`.

---

## 5. Evidências por script (resumo)

| Verificação | Escopo | Resultado |
|---|---|---|
| Status HTTP | 34 URLs do `sitemap.xml` + `/obrigado/`, `/404.html`, `/contato/?servico=…` | **37/37 = 200** |
| Contagem de H1 | mesmas 37 | **1 H1 em todas**; nenhum salto de nível de título |
| Imagens sem atributo `alt` | mesmas 37 | **0**. Os `alt=""` (decorativos) estão em miniaturas de cards cujo nome já vem no H3 (até 6 por página) |
| Links internos | 34 destinos únicos | **0 quebrados** |
| Assets (CSS, JS, imagens, `srcset`) | 121 únicos | **0 quebrados** |
| Erros de console e requisições com falha | 39 URLs × 375 e 1440 px (Chrome headless, CDP), incluindo `?simular=falha` | **0** (só a 404 esperada em `/nao-existe/`) |
| Scroll horizontal | 37 URLs × 320 / 375 / 768 / 1024 / 1440 px, com `overflow-x` do `body` liberado para não mascarar | **0 em 375, 768, 1024 e 1440**. Em 320 há 2 estouros reais (UX-05); o de `/projetos/` é o bottom sheet fora da tela, sem impacto |
| Contraste (fundos sólidos) | 11 páginas-modelo × 375 e 1440 | Falhas reais: eyebrow do hero (UX-01). Fundos com textura medidos à parte (UX-02 e UX-04). As outras ocorrências eram falsos positivos (fundo translúcido) e foram descartadas |
| CTA acima da dobra em 375×667 | Home | Botão "Solicitar orçamento" em y = 559–607: **visível** |
| Teclado | Home 1440 (16 paradas de Tab), menu mobile, mega-menu, lightbox, radio-cards | Ordem lógica, anel de foco em todas as paradas, trap e Esc corretos |

### Screenshots salvos (`equipe/screenshots-validacao/`)

**Primeira dobra**
- `01` home 375 com banner de cookies
- `02` home 375
- `33` home 1440
- `35` home 375×667
- `37` HVAC 375
- `38` hidrossanitário 375
- `39` projetos 375

**Páginas inteiras**
- Home: `03` (375), `04` (768), `05` (1440)
- `/servicos/`: `06`, `07`, `08`
- Hidrossanitário: `09`, `10`, `11`
- HVAC: `12`, `13`
- BIM: `14`, `15`
- `/projetos/`: `16`, `17`, `18`
- Projeto com foto: `19`, `20`
- Projeto sem foto: `21`, `22`
- `/sobre/`: `23`, `24`
- `/contato/`: `25`, `26`, `27`
- 404: `28`, `29`
- Política: `30`, `31`
- `/obrigado/`: `32`

**Evidências de problemas**
- `36` lightbox BIM aberto
- `40` faixa azul nos cards (UX-03)
- `41` lead ilegível no CTA (UX-02)
- `42` texto sobre textura (UX-04)
- `43` H2 cortado em 320 px (UX-05)
- `44` erro vazio do grupo de disciplinas (UX-06)

> Nota técnica: as capturas de página inteira de `/servicos/`, `/bim/` e das páginas de serviço (06 a 15) foram feitas esticando a janela. Nelas, o header fixo pode aparecer no meio da página. É artefato da captura, não defeito do site.

---

## 6. Encaminhamento

| Responsável | Itens |
|---|---|
| **webdesigner-senior** | **Altos:** UX-01, UX-02, UX-03 · **Médios:** UX-04, UX-05, UX-06, UX-07, UX-08, UX-09 · **Baixos:** UX-13 a UX-18, UX-20, UX-22, UX-23 |
| **copywriter** | UX-10, UX-11, UX-12, UX-19 (texto do UX-09 junto com o webdesigner) |
| **wireframe** | UX-21 |
| **coordenador → cliente** | disciplinas por projeto (UX-10); CNPJ, razão social, CREA e PDF (UX-11); dados da Política (UX-12); nome da Prix (UX-19); vetor da Mello Azevedo (UX-18) |

**Revalidação (rodada 2):** conferir item por item UX-01 a UX-09 em 320, 375, 768 e 1440 px, com contraste remedido por script. Rodar a varredura com o build `REVISAO = False`.

---

## 7. Revalidação (rodada 2): 21/11/2026

**Base da revalidação**
- Registro de correções `equipe/04-correcoes-ux.md` e build novo no preview (recarregado sem cache).
- CSS conferido com `.c03-hero .eyebrow`, `.on-dark .lead` e a sobreposição em `.bg-texture`.
- Evidências novas em `equipe/screenshots-validacao/rodada2/` (R01 a R16).
- Medições por script em iframes nas larguras 320, 375, 768 e 1440, e no Chrome headless via CDP.
- Testes de teclado no navegador integrado.

### 7.1 Status item por item

| ID | Sev. | Status | Evidência |
|---|---|---|---|
| UX-01 | Alta | **Resolvido** | Eyebrow do hero com `rgb(255,195,173)` na Home e em `/projetos/`, em 375, 768 e 1440 px. Contraste 10,92:1 sobre a pílula e navy, e 6,24:1 no pior caso (pílula sobre fundo branco). Antes era 2,44:1. `R03-home-375-hero-eyebrow.png`, `R04-projetos-375-eyebrow.png`. |
| UX-02 | Alta | **Resolvido** | Lead do C13 com contraste mínimo de 9,1:1 contra o navy-900 em `/projetos/`, `/sobre/`, `/bim/`, `/servicos/` e 2 projetos, em 375, 768 e 1440 px. Antes era 1,47:1. `R07-projeto-1440-cta-lead.png`. O alerta de 1,14:1 em Home e serviços é falso positivo: é o `<p>` que envolve o link "Prefere WhatsApp?", sem texto próprio. O link é branco. |
| UX-03 | Alta | **Resolvido** | Diferença entre moldura e foto = **0 px em todos os cards com foto** (Home 6/6 e `/projetos/` 12/12), em 375, 768 e 1440 px. Antes era `[39, 39, −31, 0, 39, −31]`. Os cards sem foto mostram só o símbolo, como previsto. Hero C03: 0 px. |
| UX-04 | Média | **Resolvido** | Sobreposição navy-900 a 82% confirmada no CSS computado de todos os C13. Pixel a pixel sobre `fundo-azul-1600.webp`, `#BFD0DF` fica com mínimo 5,35:1, p10 7,21:1 e mediana 8,12:1. Texto branco: mínimo 8,44:1. Antes, o p90 era 2,43:1. |
| UX-05 | Média | **Resolvido, com regressão (REG-01)** | Varredura de 36 URLs em 320, 375, 768, 1024 e 1440 px com o `overflow-x` do body liberado: **0 estouros**. Em `/servicos/infraestrutura-de-saneamento/` (320 px), `scrollWidth` = 320. A correção, porém, ligou `hyphens:auto` em todos os H1–H4 (ver REG-01). |
| UX-06 | Média | **Resolvido** | Etapa 2 sem disciplina: o erro do grupo mostra "Marque pelo menos um projeto ou a opção "Ainda não sei"." e o grupo tem `aria-describedby="disciplinas-erro"`. A mensagem some quando uma opção é marcada. `R10-contato-375-erro-disciplinas.png`. |
| UX-07 | Média | **Resolvido** | `tipo`, `cidade` e `uf` ficam com `aria-invalid` e `aria-describedby` apontando para `*-erro`, que tem o texto certo. O `aria-describedby` é removido depois de corrigir o campo. `required`/`aria-required` estão nos 9 obrigatórios e no grupo. Sobram só 2 `role="alert"`: o upload (assíncrono) e a falha de envio. Ambos são adequados. |
| UX-08 | Média | **Resolvido em 375 · pendente em 320×568** | Em 375×812, o banner tem 179 px (22% da tela). "Solicitar orçamento" fica livre (base em 632 px, banner começa em 633 px). "Aceitar" e "Recusar" ficam lado a lado com 166×44 px e o mesmo peso. `R01-home-375-cookies-compacto.png`. Em 320×568 o banner ocupa 33% e cobre o CTA do hero (`R02-home-320x568-cookies.png`). Esse caso depende do texto curto proposto ao copywriter. |
| UX-09 | Média | **Resolvido** | Varredura de `a/button[aria-label]` visíveis em 11 páginas e 3 larguras: todos contêm o texto visível. A única exceção é o balão do C19 ("Dúvidas? Fale no WhatsApp"), que só aparece no hover e é `aria-hidden`. O nome "Falar no WhatsApp…" contém "WhatsApp", então é aceitável. |
| UX-10 | Média | **Pendente (cliente)** | A ficha dos projetos continua só com Cliente, Local e Unidades. |
| UX-11 | Média | **Parcial** | A frase que prometia o PDF saiu de `/sobre/`. CNPJ, razão social e CREA continuam pendentes com o cliente. |
| UX-12 | Média | **Pendente (cliente)** | A Política de privacidade continua com marcações pendentes. Bloqueia a publicação. |
| UX-13 | Baixa | **Resolvido** | Com `?simular=falha`, o alerta recebe o foco e traz o link `wa.me` (nova aba) com mensagem pronta. `R12-contato-375-falha-link-whatsapp.png`. |
| UX-14 | Baixa | **Resolvido** | `drive.google.com/pasta` vira `https://drive.google.com/pasta` e o formulário avança sem erro. |
| UX-15 | Baixa | **Resolvido** | `.sep` com `display:none` em 375 px. A microprova fica com um item por linha (`R03`). |
| UX-16 | Baixa | **Resolvido** | `:focus-visible` com `outline: 2px solid transparent` e `@media (forced-colors: active)` com outline sólido. Os campos têm anel sólido de 1,5 px. Com Tab real, o mega-menu abre com Enter e o foco é visível. |
| UX-17 | Baixa | **Resolvido** | Links de contato do rodapé com `[44, 44, 44]` px. |
| UX-18 | Baixa | **Resolvido** | Mello Azevedo aparece como `.logo-txt` (texto monocromático). |
| UX-19 | Baixa | **Pendente (cliente)** | Os filtros continuam mostrando "Prix Construtora" e "Prix Engenharia". |
| UX-20 | Baixa | **Resolvido** | Depois de "Recusar", o foco vai para `main#conteudo` sem rolar a página. Ao reabrir pelo rodapé e salvar, o foco volta a "Preferências de cookies". |
| UX-21 | Baixa | **Pendente (wireframe)** | O CTA duplicado nas páginas de projeto continua. |
| UX-22 | Baixa | **Resolvido** | Com `?uf=df`, os clientes mostram a contagem e as opções sem resultado ficam desabilitadas ("MRV (0)"). Com `cliente=MRV`, os estados se ajustam ("Minas Gerais (1)", os demais desabilitados). A URL reflete o filtro. |
| UX-23 | Baixa | **Pendente (WordPress)** | Continua sendo limitação do servidor de preview. Fica registrado no guia de migração. |

### 7.2 Regressões e achados novos

| ID | Página/Seção | Problema | Evidência | Severidade | Correção recomendada | Responsável |
|---|---|---|---|---|---|---|
| **REG-01** | Global: H1–H4 em todas as páginas e larguras | **Regressão da correção do UX-05.** A regra `h1, h2, h3, h4 { hyphens: auto }` foi aplicada a todos os títulos. O navegador passou a quebrar palavras com hífen mesmo onde não havia estouro: **186 palavras quebradas em títulos** (63 em 320, 55 em 375, 20 em 768 e **48 em 1440 px**). Exemplos:<br>• H1 de Elétrica em 1440 px com 3 quebras: "Projeto elétrico e de sis-temas para edifícios re-sidenciais";<br>• H2 da Home "A aprovação na conces-sionária";<br>• H1 de `/projetos/` "empreendi-mentos";<br>• palavra-chave quebrada no H1 de Hidrossanitário em 375 px: "hidrossani-tário para incorpora-doras";<br>• "Residencial" quebrado nos cards.<br>A leitura dos títulos piora e o acabamento fica com cara de erro. | Script (Range por palavra em H1–H4 de 36 URLs × 4 larguras). `R13-eletrico-1440-h1-hifenizado.png`, `R14-hidro-375-h1-hifenizado.png`, `R15-home-1440-h2-hifenizado.png`. | **Média** | Tirar o `hyphens:auto` global e manter só `overflow-wrap: break-word` (já evita o estouro). Se for preciso hifenizar, restringir a `@media (max-width: 359px)` ou aos títulos do `.sv06-txt`. Outra opção é `hyphens: manual` com `&shy;` nas poucas palavras longas (ex.: "compati&shy;bilizadas"). Revalidar 320 px depois. | webdesigner-senior |
| N-01 | Barra fixa C20, 320 px | O botão "WhatsApp" tem conteúdo de 108 px numa área útil de 101 px. O texto encosta na borda e invade o padding. Em 360 e 375 px está ok. É achado novo, não regressão: 320 px não foi testado com a barra na rodada 1. | Script: `scrollW=108 > clientW=101` em 320 px. `R16-c20-320-whatsapp.png`. | Baixa | Abaixo de 360 px, reduzir o padding lateral e o `gap` do ícone ou mostrar só o ícone, com `aria-label` "WhatsApp". | webdesigner-senior |
| N-02 | Banner de cookies, mobile | O link "Configurar" ficou com 36 px de altura (32 px abaixo de 360 px) e o texto do banner com 12–13 px. Funciona, mas fica abaixo do padrão de 44 px do DS. | CSS `.c23-config` (`min-height: 36px` / `32px`), script em 375 px: `85×36`. | Baixa | `min-height: 44px` no "Configurar" (cabe na faixa). Manter o texto ≥ 13 px. | webdesigner-senior |

### 7.3 Varredura geral (regressão): build novo

| Verificação | Escopo | Resultado |
|---|---|---|
| Status HTTP | 37 URLs (sitemap + `/obrigado/`, `/404.html`, `?servico=`) | **37/37 = 200** |
| H1 por página e saltos de título | 37 | **1 H1 em todas, 0 saltos**, `lang="pt-BR"` em todas, 0 IDs duplicados |
| Imagens sem `alt` | 37 | **0** |
| Links internos / assets | 34 / 119 | **0 quebrados** |
| Console e falhas de rede | 39 URLs × 375 e 1440 px (CDP) | **0 erros** (só a 404 esperada em `/nao-existe/`) |
| Scroll horizontal | 36 URLs × 320, 375, 768, 1024 e 1440 px, sem a máscara do `overflow-x` | **0 estouros** (rodada 1: 2 em 320 px) |
| Fluxos | Formulário completo → `/obrigado/?origem=orcamento_completo` (com `?servico=hidrossanitario` pré-marcado); falha simulada; formulário curto; menu mobile (trap + Esc); mega-menu (Enter); filtros | **Sem regressão** |

### 7.4 Notas atualizadas (rodada 2)

| # | Categoria | R1 | R2 |
|---|---|---|---|
| 1 | Clareza | 8,5 | **9,0** |
| 2 | Heurísticas de Nielsen | 8,0 | **8,5** |
| 3 | Jornada de conversão | 8,0 | **8,5** |
| 4 | Hierarquia visual e UI | 7,0 | **8,0** (descontada a REG-01) |
| 5 | Acessibilidade (WCAG 2.1 AA) | 6,0 | **8,5** |
| 6 | Responsividade | 7,5 | **8,5** |
| 7 | Formulários | 8,0 | **9,0** |
| 8 | Confiança | 7,0 | **7,0** (depende dos dados do cliente) |
| | **Geral** | 7,5 | **8,4** |

### 7.5 Veredito final da revalidação

**APROVADO COM AJUSTES: liberado para o `revisor-qa`.**

Os 3 itens Altos e os 6 Médios do webdesigner (UX-01 a UX-09) foram resolvidos e medidos de novo. A varredura geral não mostrou regressão técnica.

**Ajuste recomendado antes da publicação:** REG-01 (hifenização global nos títulos). É uma mudança de uma linha de CSS e não precisa de nova rodada completa: basta conferir os títulos em 320 e 1440 px.

**Pendências que não são de layout:**
- **Cliente:** UX-10 (disciplinas por projeto), UX-11 (CNPJ, razão social, CREA e PDF), UX-12 (dados da Política, que bloqueiam a publicação) e UX-19 (nome da Prix).
- **Copywriter:** texto curto do banner para fechar o UX-08 em 320×568.
- **Wireframe:** UX-21.
- **Migração para o WordPress:** UX-23.

Os Baixos N-01 e N-02 podem entrar no mesmo ajuste do REG-01.
