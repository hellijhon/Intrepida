# 04 — Guia de migração para WordPress + Elementor

> Etapa: Web design (agente `webdesigner-senior`). Data: 21/11/2026.
> Fonte da verdade visual: `site/` (protótipo HTML de alta fidelidade) e `equipe/04-design-system.md`.
> Cada seção do protótipo tem `id` = ID do wireframe (`h-02`, `sv-05`…) e `data-componente="Cxx"`: monte no Elementor **na mesma ordem e com o mesmo nome**.
> Não usar o conector `clt-viaja-elementor` (é de outro cliente).

---

## 1. Pré-requisitos e hospedagem
- **Acesso** à hospedagem (VetorialNet hoje, fora do ar), ao DNS (devopers) e ao registro.br. **Não mexer nos registros MX** (e-mail na Penso/Barracuda).
- **Ambiente:** PHP 8.2+, MySQL 8 / MariaDB 10.6+, HTTPS (Let's Encrypt), `memory_limit` ≥ 256 MB, `upload_max_filesize` ≥ o limite do formulário (sugestão 20 MB, a confirmar).
- Montar primeiro em **subdomínio de homologação** (`homolog.intrepidaengenharia.com.br`) com `noindex` e senha; virar o DNS só no fim.
- **Instalação limpa** (não reaproveitar o WP 6.5.5 antigo nem os plugins ElementsKit / Essential Addons / MetForm).

## 2. Plugins (mínimo possível)
| Plugin | Para quê | Obrigatório? |
|---|---|---|
| **Hello Elementor** (tema) | Tema leve, base do Elementor | Sim |
| **Elementor + Elementor Pro** | Theme Builder (header, footer, single, archive), Loop Grid, Taxonomy Filter, Forms (com etapas), Popups, Custom Code | Sim |
| **ACF (Advanced Custom Fields)** – versão gratuita | Campos dos Projetos (cliente, cidade, UF, unidades, foto, relacionados, disciplinas, ano, área…) e opções globais | Sim (alternativa: campos nativos do Elementor Pro não cobrem CPT; o ACF Free resolve) |
| **Rank Math SEO** (ou Yoast) | Title/meta, sitemap, breadcrumbs, schema (Organization, LocalBusiness, BreadcrumbList, FAQPage), **redirecionamentos 301** | Sim |
| **Complianz** (ou CookieYes) | Banner LGPD (C23) com bloqueio prévio e Consent Mode v2. No mobile, usar o layout "barra inferior" compacto: Aceitar e Recusar lado a lado, com o mesmo peso, e "Configurar" como link. Meta: ≤ 25% da altura da tela. | Sim, se houver GA4 |
| **WP Mail SMTP** | Garantir a entrega dos e-mails do formulário pelo servidor da Penso/Google | Sim |
| **Cloudflare Turnstile** (integração nativa do Elementor Pro Forms ≥ 3.20, ou plugin "Simple Cloudflare Turnstile") | Anti-spam invisível no formulário | Sim (reCAPTCHA v3 nativo é alternativa) |
| Cache: **LiteSpeed Cache** (se o servidor for LiteSpeed) ou **WP Super Cache** | Cache de página | Recomendado |
| Backup: **UpdraftPlus** | Backup externo semanal | Recomendado |

**Não instalar:** construtores de terceiros, pacotes de addons, sliders, plugins de ícones extras. Tudo do protótipo é reproduzível com Elementor Pro nativo.

## 3. Configuração do Kit (Site Settings)
### 3.1 Global Colors (nomes exatos)
| Nome no Kit | HEX | Token CSS |
|---|---|---|
| Primary — Azul Intrépida | `#0B3859` | `--c-navy-800` |
| Secondary — Azul apoio | `#196291` | `--c-blue-600` |
| Text — Tinta | `#17202B` | `--c-ink` |
| Accent — Laranja CTA | `#C8431B` | `--c-orange-600` |
| Laranja marca (só gráfico) | `#F15A29` | `--c-orange-500` |
| Laranja hover | `#A63714` | `--c-orange-700` |
| Vermelho marca (só gráfico) | `#EF4036` | `--c-red-500` |
| Azul profundo | `#082C47` | `--c-navy-900` |
| Azul rodapé | `#061F33` | `--c-navy-950` |
| Azul hover | `#134A72` | `--c-navy-700` |
| Azul claro 50 / 100 / 200 | `#F2F7FB` / `#E4EEF6` / `#C9DCEB` | `--c-blue-50/100/200` |
| Cinza texto 700 / 600 / 500 | `#3A4552` / `#4A5562` / `#5F6A77` | `--c-gray-700/600/500` |
| Cinza borda 300 / 200 / fundo 100 | `#C5CCD4` / `#E3E7EC` / `#F1F3F6` | `--c-gray-300/200/100` |
| Texto em azul | `#BFD0DF` | `--c-on-dark-muted` |
| Sucesso / Erro / Aviso | `#1D7444` / `#B42318` / `#8A5300` | feedback |
| WhatsApp | `#1F7A4D` | C19/C20 |
Regra de uso: **Laranja marca e Vermelho marca nunca em texto** (contraste < 4,5:1).

### 3.2 Global Fonts
| Nome | Fonte | Peso | Tamanho D / T / M (px) | Line-height |
|---|---|---|---|---|
| Primary (títulos) | Montserrat | 700 | — (definido por H1–H4 abaixo) | — |
| Secondary | Fira Sans | 500 | 16 | 1,6 |
| Text | Fira Sans | 400 | 16 / 16 / 16 | 1,62 |
| Accent (botões, rótulos) | Montserrat | 700 | 15 | 1,2 |
| H1 Display (home) | Montserrat | 800 | 56 / 44 / 34 | 1,12 |
| H1 | Montserrat | 800 | 46 / 38 / 30 | 1,12 |
| H2 | Montserrat | 700 | 40 / 32 / 26 | 1,22 |
| H3 | Montserrat | 700 | 22 / 20 / 19 | 1,3 |
| Lead | Fira Sans | 400 | 20 / 18 / 17 | 1,55 |
| Eyebrow | Montserrat | 700, caixa alta, espaçamento 0,12em | 13 | 1,3 |
| Número (C05) | Montserrat | 800 | 56 / 44 / 36 | 1 |
- *Site Settings → Typography*: Body = Text; Links = Secondary color.
- **Elementor → Settings → Performance:** ligar **"Load Google Fonts Locally"** (LGPD e desempenho) e **"Improved Asset Loading"**; *Font-display: swap*.
- Harabara: nenhuma configuração; o logo é SVG (`site/assets/img/marca/logo-intrepida-azul.svg` / `-branco.svg`). Habilitar upload de SVG em *Elementor → Settings → Advanced → Enable Unfiltered File Uploads* só para administradores.

### 3.3 Layout, botões, formulários
- *Layout*: Content Width 1200; Container padding Desktop 0/32, Tablet 0/24, Mobile 0/16; Widgets Space 24; **Breakpoints padrão** (Mobile 767, Tablet 1024); ativar *Widescreen* 1440 só se precisar de ajuste fino.
- *Buttons*: Accent font; fundo Accent; texto branco; raio 10; padding 12/24; hover fundo Laranja hover; borda 2 px.
- *Form Fields*: altura 52, borda 1,5 px Cinza 500, raio 10, foco borda Secondary; rótulo Fira Sans 600 15 px.
- *Custom CSS do Kit*: colar os blocos "Tokens" (seção 1 do `site.css`), "Eyebrow", "fig-cota", "c12-faq", "c10-processo", "c24 uf-grid", "reveal" e "prefers-reduced-motion". São os únicos trechos que o painel do Elementor não gera sozinho. Incluir também as regras da rodada de correções UX:
  - `:focus-visible` com `outline` transparente e o bloco `forced-colors`;
  - `h1–h4 { overflow-wrap: break-word }` (NÃO usar `hyphens: auto` — REG-01); barra fixa mobile abaixo de 360 px com padding/fonte menores (N-01); link "Configurar" dos cookies com 44 px de altura (N-02) e a escala reduzida abaixo de 360 px;
  - `.on-dark .lead`;
  - `.c03-hero .eyebrow { color: #FFC3AD }`.
- **Seções com textura** (C13): no Container, *Background* = imagem `fundo-azul` + **Background Overlay** cor `#082C47` com opacidade **0,82**. Texto: título branco, parágrafos `#BFD0DF`.
- **Hero C03 e cards C08:** imagem com *Object Fit: Cover* e altura 100% da moldura (no Loop Item, *Image Size* custom + *Aspect ratio 3:2*). Nunca deixar a imagem com altura automática dentro de moldura de proporção fixa.
- *Background* das seções com grade técnica: imagem de fundo SVG (gerar a partir de `.bg-grid`) ou CSS do Kit.

## 4. Estrutura de conteúdo
### 4.1 Páginas (Pages)
Home, Serviços (hub), as 9 páginas de serviço (filhas de "Serviços", para o slug `/servicos/[slug]/`), BIM e Compatibilização, Sobre, Contato, Obrigado (`noindex`), Política de Privacidade.
> As 9 páginas de serviço podem ser **Pages com um template salvo `Single – Serviço`** (mais simples de editar pelo cliente). Se preferir um CPT "Serviços", seguir o mesmo esquema dos Projetos. Recomendação: **Pages** (são só 9 e mudam pouco).

### 4.2 CPT "Projetos" (ACF Free)
- **Post type** `projeto` (rótulo "Projetos"), slug `projetos`, `has_archive = true` (a listagem `/projetos/` é o archive), suporte a título, imagem destacada e resumo. Registrar com o próprio ACF (*ACF → Post Types*).
- **Taxonomias:** `uf` (MG, DF, SP, RJ, MS, SC) · `cliente` (UNENCO, RNI…) · `tipo` (oculta enquanto houver um só tipo) · `disciplina` (as 9 + Compatibilização BIM; oculta até o cliente confirmar).
- **Campos ACF (grupo "Ficha técnica"):** `cidade` (texto), `unidades` (número), `logo_cliente` (imagem), `area_construida`, `ano`, `formato_entrega` (vazios ficam ocultos via *Display Conditions*), `relacionados` (Relationship, máx. 3), `credito_foto` (texto, condicional), `desafio`, `solucao`, `resultado` (WYSIWYG, condicionais), `galeria` (Gallery — ACF Pro; no Free usar 3 campos de imagem), `depoimento` (grupo, condicional).
- **Importação:** os 18 projetos estão em `site/_build/data/conteudo.json` (nome, slug, cliente, cidade, UF, unidades, title, meta, alt, relacionados). Importar com **WP All Import** (uso único, desinstalar depois) ou cadastrar à mão (18 itens). Imagens: `site/assets/img/projetos/[slug]-2400.jpg` (ou a maior disponível).

### 4.3 Opções globais
ACF → Options page (ACF Pro) **ou** um post privado "Dados da empresa": telefone, WhatsApp, e-mail, endereço, horário, CNPJ, razão social, CREA, LinkedIn, PDF do portfólio, prazo de resposta. Os templates puxam por *Dynamic Tags*; campo vazio → elemento escondido por *Display Conditions* (Elementor Pro 3.19+). É o equivalente do dicionário `DADOS` do protótipo.

## 5. Templates (Theme Builder e seções salvas)
| Template | Tipo | Condição | Conteúdo (IDs do wireframe) |
|---|---|---|---|
| `C01 – Header` | Header | Todo o site | Logo SVG · Nav Menu (menu "Principal") com **mega-menu** (Elementor Pro *Menu* widget ≥ 3.16, conteúdo do dropdown = template `C01 – Mega Serviços`) · ícone WhatsApp · botão. Mobile: *Off-canvas* (widget Off-Canvas ≥ 3.18) com template `C01 – Drawer`. Sticky + "Scroll effects: shrink" (88 → 64 px). |
| `C02 – Footer` | Footer | Todo o site | 4 colunas · accordions no mobile (widget Accordion só no breakpoint mobile; colunas normais no desktop) · © com Dynamic Tag *Current Date (Y)* · link "Preferências de cookies" (shortcode do plugin de consentimento). Inclui **C19** (Container fixo, só desktop) e **C20** (Container fixo, só mobile/tablet), ambos com *Display Conditions* "não mostrar em Contato/Obrigado". |
| `Single – Projeto` | Single (CPT projeto) | Todos os projetos | PP-02 hero (imagem destacada; se vazia, variante "sem foto" via condição) · H1 Post Title · linha cliente · cidade/UF · parágrafo de abertura (texto com Dynamic Tags) · PP-03 ficha (C15) + PP-04 cartão sticky · PP-05/06/07 condicionais · PP-08 Loop Grid de `relacionados` · PP-09 *Post Navigation* (ordem do menu) · PP-10 CTA. |
| `Archive – Projetos` | Archive (CPT projeto) | Arquivo de Projetos | PJ-02 hero baixo · C05 · **Loop Grid** (Loop Item `C08 – Card projeto`, 3/2/1 colunas, 24 itens por página) + **Taxonomy Filter** (UF e Cliente; *multiple selection off*; "Show all" = "Todos os estados"/"Todos os clientes"; ligar "Show number of posts" e esconder termos vazios. A contagem cruzada e o bloqueio de combinações sem resultado do protótipo exigem o script de `site.js` ou JetSmartFilters) · C06 com 24 logos (âncora `#clientes`) · C24 · PJ-08 CTA. Bottom sheet mobile: Off-Canvas com o mesmo Taxonomy Filter. |
| `Single – Serviço` | Seção/Page template | 9 páginas | SV-02 a SV-10. Texto de cada página em `equipe/03-copy.md` §5 e já estruturado em `site/_build/data/servicos.json`. |
| `Loop – C08 Card projeto` | Loop Item | — | Imagem destacada 3:2 · badge UF (termo da taxonomia) · H3 título (link) · cliente · cidade/UF · unidades. Card clicável inteiro (*Link* no Container). |
| Seções salvas | Section/Container | — | `C03 – Hero foto`, `C04 – Hero interno`, `C05 – Números`, `C06 – Logos (12)`, `C06 – Logos (24)`, `C07 – Grupos serviço`, `C07 – Card serviço`, `C09 – Texto + imagem`, `C10 – Processo`, `C11 – Galeria BIM`, `C12 – FAQ`, `C13 – CTA botões`, `C13 – CTA + formulário`, `C15 – Ficha`, `C17 – RT`, `C18 – Faixa escura`, `C21a – Form orçamento`, `C21b – Form curto`, `C24 – Mapa UFs`. Use **Global Widgets / Components** para C05, C06, C10, C13, C17 e C21b, que se repetem e precisam mudar em todas as páginas ao mesmo tempo. |
| `404` | Single 404 | 404 | 404-02/03 (status 404 real; não redirecionar para a home). |
| Popup | — | — | Não há popup no projeto (decisão: nada que interrompa a leitura). |

**C11 Galeria BIM:** widget *Gallery* (Pro) ou *Basic Gallery* com *Lightbox* nativo (Site Settings → Lightbox: fundo `#061F33` 96%, ícones brancos, contador ligado, legenda = "Caption"). Legendas e alt das 8 imagens: copy §13.2.
**C12 FAQ:** widget *Accordion* (nested) + bloco FAQ do Rank Math para o schema (ou ativar "FAQ Schema" no próprio Accordion do Elementor ≥ 3.21).
**C24 Mapa:** colar o HTML do cartograma (`<div class="uf-grid">…`) num widget HTML; os links levam a `/projetos/?uf=mg` (o Taxonomy Filter lê o parâmetro `?e-filter-…`; ajustar o link para o formato de URL do filtro após configurar).

## 6. Formulários
**Recomendado: Elementor Pro Forms** (nativo, sem plugin extra).
- **C21a (Contato):** campo *Step* do Elementor para as 3 etapas ("O empreendimento", "Escopo", "Seus dados"), botões "Continuar"/"Voltar", indicador "Progress bar". Campos e textos exatamente como no copy §10.3 / `site/contato/index.html`.
  - Condicionais (Nº de unidades × Área; "Qual tipo?"): o Elementor Forms não tem lógica condicional nativa → usar o pequeno script de `site/assets/js/site.js` (bloco "Campos condicionais", "Ainda não sei", contador, máscara de telefone e resumo de erros), colado em *Elementor → Custom Code* só na página Contato. Alternativa sem código: **Fluent Forms** (tem etapas e condicionais nativas) — mas é um plugin a mais.
  - Upload: campo *File Upload* (PDF, DWG, RVT, IFC, ZIP; limite em MB a confirmar com o servidor de e-mail). Arquivos grandes → campo "Link dos arquivos".
  - Ocultos: `servico` e `ref` (Dynamic Tag *Request Parameter*), página de origem (*Current URL*), UTMs (*Request Parameter*), `form_label` = `orcamento_completo`.
  - **Pré-marcação por `?servico=`**: o valor do checkbox de cada disciplina deve ser igual ao parâmetro (`hidrossanitario`, `eletrica`, `gas`, `hvac`, `pressurizacao`, `piscina`, `saneamento`, `reuso-pluvial`, `aquecimento-solar`, `compatibilizacao-bim`, `nao-sei`); o script do protótipo marca a opção.
- **C21b (curto):** mesmo widget, sem etapas, `form_label` = `orcamento_rapido`, campo oculto `servico` por página.
- **Ações após envio:** *Email* (para o destinatário dos leads — **a confirmar**; hoje carlos@intrepidaengenharia.com.br), *Email 2* (cópia ao usuário, texto do copy), *Redirect* para `/obrigado/?origem=[form_label]`, *Collect Submissions* (backup no painel). Opcional: *Webhook* para CRM.
- **Anti-spam:** Honeypot (campo nativo) + Cloudflare Turnstile.
- **Mensagens:** sucesso = redirect; erro = "Não conseguimos enviar o seu pedido agora…" (copy §10.3); campo obrigatório com as mensagens por campo do copy.
- **GA4:** evento `form_submit` disparado na página `/obrigado/` (via GTM, gatilho Page View + parâmetro `origem`), com `form_label`.

## 7. Redirecionamentos 301 (Rank Math → Redirections)
| De | Para |
|---|---|
| `/quem-somos/` | `/sobre/` |
| `/trabalhos-desenvolvidos/` | `/projetos/` |
| `/nossos-clientes/` | `/projetos/#clientes` |
| `/servicos/` | (mantido) |
| `/contato/` | (mantido) |
| `/?elementskit_template=header` e qualquer `?elementskit_template=*` | `/` |
| Uploads antigos de imagens (`/wp-content/uploads/2024/07/*`) | não redirecionar (404 é aceitável) |
Arquivo pronto: `site/_redirects-301.txt`. Depois do lançamento, monitorar 404 no Rank Math por 30 dias e criar 301 para o que aparecer.

## 8. SEO
- **Rank Math:** Title e meta de cada página exatamente como no copy §16 (e §8.2 para os 18 projetos). Separador "|".
- **Schema:** Organization + LocalBusiness/ProfessionalService (endereço Goitacazes, telefones, e-mail, `areaServed` MG/DF/SP/RJ/MS/SC) — modelo em JSON-LD no `<head>` do protótipo; BreadcrumbList (automático); FAQPage nas páginas com C12.
- **Breadcrumbs** do Rank Math no widget C14 (rótulo "Início").
- **Open Graph:** imagem padrão `og-image.jpg` (Mirante São Lucas 1200×630); nos projetos, a foto do projeto.
- **Sitemap** do Rank Math (excluir `/obrigado/`); `robots.txt` como `site/robots.txt`.
- **Search Console + GA4 + GTM** com **Consent Mode v2** (o banner só libera `analytics_storage` após "Aceitar").
- **Imagens:** subir as versões de `site/assets/img/` (WebP já otimizado); nome de arquivo descritivo; alt do copy §13.
- **Um H1 por página** (no tema Hello, desativar o título automático da página: *Site Settings → Hello Theme → Disable page title*).

## 9. Performance
- Elementor: *Optimized DOM Output*, *Improved Asset Loading*, *Lazy load background images*, *Inline font icons* ligados; desligar *Font Awesome* e *eicons* no front se não usados (os ícones do site são SVG).
- Imagens: largura máxima 2400 px; hero com *Image Optimization → fetchpriority high* (Elementor ≥ 3.22) e sem lazy-load.
- Cache de página + CDN (Cloudflare grátis, se o DNS migrar).
- Meta: LCP < 2,5 s, CLS < 0,1, INP < 200 ms no mobile (PageSpeed Insights).

## 10. Checklist de publicação
**Conteúdo e dados**
- [ ] Copy colado sem alteração (conferir com `03-copy.md`); seções CONDICIONAIS ocultas enquanto não houver dado.
- [ ] Dados pendentes do cliente preenchidos ou ocultos: razão social, CNPJ, CREA (empresa e RT), horário, LinkedIn, PDF do portfólio, prazo de resposta, concessionárias, disciplinas por projeto, softwares/formatos BIM.
- [ ] Foto do RT (fotografada) no lugar do placeholder; fotos dos 6 projetos sem imagem (ou manter variante sem foto).
- [ ] Imagens geradas por IA com selo "Imagem ilustrativa" e alt "(imagem ilustrativa)"; lista em `site/assets/CREDITOS.md`.
- [ ] Política de Privacidade revisada pelo jurídico (trechos em amarelo no protótipo) e data de atualização.
- [ ] Modo revisão desligado (selos "PLACEHOLDER" não aparecem) e revalidação de contraste, 320 px e foco com `REVISAO = False`.
- [ ] `/obrigado/`: a frase "Enviamos uma cópia do pedido para o seu e-mail" só fica se a ação *Email 2* (cópia ao usuário) estiver ativa no formulário.
- [ ] Erros do formulário: cada mensagem ligada ao campo (`aria-describedby`); o Elementor Pro Forms faz isso nativamente. Conferir a mensagem do grupo de checkboxes obrigatório e o `required` dos campos.

**Formulários e conversão**
- [ ] E-mail destinatário dos leads confirmado; teste de envio real dos 2 formulários (com e sem anexo) chegando na caixa e na cópia ao usuário.
- [ ] WP Mail SMTP testado (SPF/DKIM do domínio ok).
- [ ] Turnstile/honeypot ativos; envio de spam de teste bloqueado.
- [ ] `?servico=` pré-marca a disciplina; `?ref=` chega no e-mail.
- [ ] Redirect para `/obrigado/` e evento `form_submit` no GA4 (DebugView).
- [ ] Links `wa.me` com mensagem por página (copy §2.6), `tel:+553130706568`, `mailto:carlos@intrepidaengenharia.com.br` (**corrigido**).

**Técnico e SEO**
- [ ] 301 configurados e testados; 404 personalizada (template *Single 404* do Theme Builder) com **status HTTP 404 real** (testar `/nao-existe/`).
- [ ] Titles/metas conferidos (≤ 60 / ≤ 155); um H1 por página; sitemap enviado ao Search Console.
- [ ] Banner de cookies: "Recusar" não carrega GA4; "Preferências de cookies" reabre o painel.
- [ ] HTTPS forçado; `www` → sem `www` (ou o inverso) com 301.
- [ ] Homologação com `noindex`; produção com indexação **ligada**.
- [ ] Backup automático configurado; usuários com senhas fortes e 2FA.

**Qualidade**
- [ ] Testes em 375, 768, 1280 e 1440 px (Chrome, Safari iOS, Android); sem scroll horizontal.
- [ ] Teclado: Tab percorre menu, mega-menu, drawer, formulário, lightbox e filtros com foco visível; Esc fecha camadas.
- [ ] Leitor de tela (VoiceOver/NVDA) em Home, Contato e Projetos.
- [ ] PageSpeed mobile ≥ 85 e Core Web Vitals no verde.
- [ ] QA final (`revisor-qa`) com parecer PRONTO.
