# 06 — QA final: Intrépida Engenharia e Projetos

> Etapa: QA final (agente `revisor-qa`). Data: 21/11/2026.
> Objeto: protótipo HTML de alta fidelidade em `site/` (36 páginas, gerado por `site/_build/build.py`), servido em `http://localhost:8770/` em modo revisão (`REVISAO = True`), e o guia `04-guia-migracao-elementor.md` para WordPress + Elementor.
> Base: `CLAUDE.md` (decisões do usuário), `01-contexto.md`, `02-wireframe.md`, `03-copy.md`, `04-design-system.md`, `04-guia-migracao-elementor.md`, `04-correcoes-ux.md` (rodadas 1 e 2) e `05-validacao-ux-ui.md` (aprovado com ajustes).
> Selos "PLACEHOLDER" e "Imagem ilustrativa" são intencionais e não contam como defeito. O envio dos formulários é simulado.

**Como testei:** tudo foi feito no build atual (o `build.py`, rodado numa cópia, gera arquivos idênticos aos de `site/`, e a cópia do preview está sincronizada).
- **Scripts sobre o HTML gerado:**
  - comparação do copy aprovado com o texto publicado;
  - varredura de resíduos;
  - contatos e números;
  - SEO: title, meta, canonical, OG, JSON-LD, sitemap e robots.
- **Navegador integrado:**
  - status de 36 páginas, 34 links internos e 256 assets;
  - 180 medições (36 páginas × 320, 375, 768, 1280 e 1440 px): overflow, H1, ordem de títulos, IDs, `alt`, labels e `hyphens`;
  - contraste em 6 páginas;
  - fluxos completos dos 2 formulários (validação, máscara, pré-marcação, sucesso e falha);
  - simulação de `REVISAO = False`.
- **Chrome headless (CDP):** 144 carregamentos sem cache (36 páginas × 375, 768, 1280 e 1440 px) para medir peso, LCP e erros de console, com screenshots de página inteira em `equipe/screenshots-qa/{375,768,1280,1440}/`.
- **Simulação de produção:** build com `REVISAO = False` numa cópia, comparado com o build atual.

---

## 1. Checklist

| # | Item | Status | Observação (o que foi testado) |
|---|---|---|---|
| 1 | **Aderência ao briefing** | ✅ | **Páginas:** as do mapa do site 9.1 estão todas lá (Home, hub + 9 serviços, BIM, Projetos + 18 cases, Sobre, Contato, Obrigado, 404, Política).<br>**Menu:** 5 itens + botão "Solicitar orçamento" + WhatsApp.<br>**Problemas do site antigo:** os 7 ALTOS do diagnóstico 5.2 foram resolvidos no protótipo:<br>• `mailto` correto;<br>• H1 em toda página;<br>• meta description;<br>• serviços com página própria;<br>• CTA de orçamento no hero;<br>• CTA do bloco das concessionárias funcionando;<br>• "projetos, não obras" (FAQ e Sobre).<br>**Personas:** P1 tem prova (números, logos, cases) e formulário qualificado. P2 tem `#dados-cadastrais`, ainda sem dados (pendência do cliente). P3/P4 têm o bloco "Não sabe quais projetos precisa?" e o WhatsApp. |
| 2 | **Consistência entre etapas** | ✅ | **Wireframe:** os IDs de seção batem com o wireframe em Home, hub, serviço, BIM, Projetos, case, Sobre e Contato. As seções CONDICIONAIS ficam ocultas, como manda a regra.<br>**Copy:** comparação automática das strings do copy (Home inteira, globais, hub, Hidrossanitário, Saneamento, BIM, Projetos, 18 cases, Sobre, Contato, Obrigado, 404):<br>• **0 divergências de texto**;<br>• 18/18 cases com H1, linha, unidades, relacionados, title, meta e alt idênticos à tabela 8.1/8.2;<br>• 18/18 titles e metas idênticos ao quadro §16.<br>As únicas diferenças são previstas: setas viraram ícone, conteúdo condicional oculto, link `wa.me` na falha (UX-13) e foto do SH-05 trocada (proposta 9 do copy).<br>**Design system:** tokens do CSS iguais à tabela 2.1 do DS e ao Kit do guia.<br>**Documentação:** 2 desalinhamentos (QA-02). |
| 3 | **Validação UX/UI** | ✅ | **Críticos/Altos:** os 0 Críticos e 3 Altos (UX-01 a 03) foram resolvidos e revalidados pelo validador.<br>**REG-01, N-01, N-02:** confirmei no CSS e por script:<br>• `hyphens` computado ≠ `auto` em todos os H1–H4 das 36 páginas × 5 larguras (0 ocorrências);<br>• 0 estouros em 320 px;<br>• barra C20 em 320 px com `scrollWidth − clientWidth = 0` nos 2 botões (N-01);<br>• "Configurar" com `min-height: 44px` (N-02).<br>**Médios/Baixos em aberto:** só os que dependem do cliente (UX-10, 11, 12, 19), UX-21 (wireframe), UX-23 (WordPress) e UX-08 em 320×568 (texto curto do banner). |
| 4 | **Texto** | ✅ | **Resíduos no HTML publicado:** 0 de `lorem`, `ipsum`, `[INSERIR`, `[VALIDAR`, `[DERIVADO`, `TODO`, `XXX` e `FIXME`. "TODO" só aparece dentro de "todos".<br>**Marcações intencionais:**<br>• 12 `<mark class="pendente">` na Política;<br>• comentários HTML `<!-- CONDICIONAL … -->` e `<!-- MINUTA — VALIDAR… -->`, que não aparecem na tela.<br>**Glossário:** "reúso", "Intrépida", "Elétrica e Sistemas", "Cidade/UF" e "Solicitar orçamento" estão consistentes. 1 desvio herdado do copy: "companhia de saneamento" (QA-08).<br>**Ortografia e acentuação:** sem erros nas amostras. 2 microajustes em QA-05 e QA-06. |
| 5 | **Funcional** | ⚠️ | **OK:**<br>• 36/36 páginas com status 200;<br>• 34 links internos e 256 assets testados;<br>• 0 âncoras quebradas (`#…` e `/página/#…`, incluindo os 20 ícones do `icons.svg`);<br>• `mailto:carlos@intrepidaengenharia.com.br` (76×, **nenhum gmail**), `tel:+553130706568` (74×), `wa.me/5531996498629` (261×) com a mensagem certa por página;<br>• C21a: validação por etapa, resumo de erros, foco no 1º erro, `aria-describedby`, máscara "(31) 90000-0000", `https://` automático, `?servico=hidrossanitario` pré-marcado, ocultos `servico`/`origem`/`form_label` preenchidos, "Enviando…" e redirecionamento para `/obrigado/?origem=orcamento_completo`;<br>• C21b: falha simulada com foco no alerta, dados mantidos e link de WhatsApp;<br>• 0 erros de console (CDP).<br>**Falha:** **5 imagens `og:image` em 404** (QA-01). |
| 6 | **Responsivo** | ✅ | **Medições:** 36 páginas × 320, 375, 768, 1280 e 1440 px com o `overflow-x` do body liberado: **0 estouros horizontais**.<br>**Screenshots:** de página inteira das 36 páginas em 375, 768, 1280 e 1440 px (144 arquivos) em `equipe/screenshots-qa/`.<br>Nas capturas, o header e a barra fixa podem aparecer no meio da página. É artefato da captura de página inteira, não defeito. |
| 7 | **Acessibilidade básica** | ✅ | **Varredura das 36 páginas × 5 larguras:**<br>• 1 H1 por página e 0 saltos de nível;<br>• 0 `img` sem `alt` e 0 IDs duplicados;<br>• 0 campos sem label;<br>• `lang="pt-BR"` em todas.<br>**Contraste:** 0 falhas em fundos sólidos (Home, Hidrossanitário, Projetos, Sobre, Contato, Política, em 1440 px). Os fundos com textura já tinham sido medidos pelo validador.<br>**Teclado:** skip link é o 1º foco e o CSS tem `:focus-visible` + `forced-colors`. O teste de Tab completo já tinha sido feito pelo validador (16/16 paradas); não refiz.<br>**Microajuste:** QA-05 (espaço entre número e rótulo no C05). |
| 8 | **SEO técnico** | ⚠️ | **OK:**<br>• title e meta **únicos** em todas as 36 páginas (0 duplicatas), ≤ 60 e ≤ 155 caracteres;<br>• `canonical` absoluto, igual ao `og:url`;<br>• OG com 7 tags (6 na 404);<br>• `noindex` em `/obrigado/` e na 404;<br>• JSON-LD válido: ProfessionalService com endereço, telefones e e-mail certos e `areaServed` = 6 UFs; FAQPage nas 12 páginas com FAQ; BreadcrumbList; WebSite na Home;<br>• `sitemap.xml` com as 34 URLs indexáveis, todas existentes (sem `/obrigado/`);<br>• `robots.txt` com o sitemap;<br>• favicon ICO/SVG/PNG, `apple-touch-icon` e `webmanifest`;<br>• URLs amigáveis e iguais às do briefing;<br>• `_redirects-301.txt` coerente com o mapa 301 do briefing.<br>**Ajustes:** `og:image` quebrada (QA-01); detalhes menores em QA-09, QA-10 e QA-11. |
| 9 | **Performance** | ✅ | Ver a seção 2. Imagens em WebP com `srcset`/`sizes`, `width`/`height` (sem CLS), `loading="lazy"` abaixo da dobra, `fetchpriority="high"` no hero, Google Fonts com `display=swap`, 1 CSS (75 KB) e 1 JS `defer` (27 KB), sem bibliotecas. |
| 10 | **Legal e confiança** | ❌ (para publicação) · ✅ (para o protótipo) | **OK:**<br>• contatos e endereço exatamente como no `CLAUDE.md`, sem o endereço da Rua Espírito Santo;<br>• © 2026;<br>• banner LGPD com Aceitar e Recusar de mesmo peso e "Preferências de cookies" no rodapé;<br>• consentimento obrigatório nos 2 formulários;<br>• números só os autorizados (24 · 18 · 6 · +5.800; unidades por projeto como no site antigo). Nenhum "anos de mercado", m², % ou número inventado. Os únicos números extras são normas, leis, faixas de prazo do formulário e exemplos de placeholder;<br>• as 5 imagens de IA têm selo, nota "Gerada por IA · não é projeto da Intrépida" e alt "(imagem ilustrativa)", e estão listadas em `CREDITOS.md`. Nenhuma simula obra, equipe ou cliente;<br>• a foto do Carlos é placeholder (símbolo da marca), sem IA.<br>**Bloqueia a publicação:** Política com 12 dados pendentes, CNPJ/razão social/CREA, validação técnica do RT e e-mail de leads (seção 4). |

---

## 2. Performance (Chrome headless, sem cache, rolando a página até o fim)

Medição: servidor local, DPR 1, cache desligado e página rolada até o fim para disparar o lazy-load. "Inicial" é o peso até o evento `load`.

| Página | 375 px: inicial / total | 1440 px: inicial / total | LCP (elemento) |
|---|---|---|---|
| Home | 463 / 597 KB | 736 / 1.073 KB | foto do hero (`mirante-sao-lucas-480/1600.webp`) |
| `/projetos/` (a mais pesada) | 389 / 982 KB | 889 / 1.303 KB | foto do hero (Residencial Pacífico) |
| Hidrossanitário | 272 / 429 KB | 309 / 478 KB | modelo BIM 01 |
| BIM | 270 / 500 KB | 302 / 543 KB | modelo BIM 05 |
| Mirante São Lucas | 354 / 370 KB | 502 / 519 KB | foto do hero |
| Sobre | 303 / 451 KB | 353 / 501 KB | foto do hero |
| Contato | 251 / 268 KB | 251 / 268 KB | H1 / lead (texto) |
| **Mediana das 36 páginas** | **413 KB total** | **473 KB total** | |

**Resultado**
- **Peso:** todas as páginas ficam abaixo de 1,4 MB no desktop e de 1 MB no mobile.
- **Requisições:** 18 a 52 por página.
- **Base fixa:** CSS 76 KB, JS 27 KB, fontes 69–87 KB (Google Fonts, 6 arquivos woff2) e HTML 18–59 KB.
- **LCP:** fica entre 136 e 592 ms em todas as medições com o navegador aquecido. A única leitura alta (4,6 s na Home em 375 px) foi a 1ª navegação do Chrome a frio. Refeita, deu 148 ms.

**Maiores imagens servidas**
- `mirante-sao-lucas-1600.webp` (311 KB) e `residencial-pacifico-1600.webp` (304 KB), nos heros em 1440 px;
- `residencial-portal-do-engenho-1200.webp` (254 KB).

As versões de 2400 px (até 625 KB em WebP) só entram em telas retina largas. O `srcset`/`sizes` escolhe corretamente: 480w no mobile DPR 1, 1600w no hero desktop.

**Lazy loading, fontes e scripts**
- **Lazy loading:** `loading="lazy"` em tudo abaixo da dobra; hero com `fetchpriority="high"` e sem lazy.
- **Fontes:** Fira Sans e Montserrat com `display=swap`. No WordPress, carregar localmente (guia §3.2, LGPD).
- **Scripts:** nenhum script de terceiros e nada desnecessário.
- **Console:** 0 erros e 0 avisos nas 144 cargas.

Estimativa realista em 4G: Home com LCP < 2,5 s. Confirmar com PageSpeed no ambiente WordPress, que terá o peso do Elementor.

---

## 3. Pendências

Severidade: **Crítica** (impede objetivo do briefing ou expõe erro grave) · **Alta** (prejuízo relevante a conversão, credibilidade ou conformidade) · **Média** (falha pontual que deve ser corrigida) · **Baixa** (polimento).

| ID | Item | Onde | Severidade | Responsável | Ação |
|---|---|---|---|---|---|
| **QA-01** | `og:image` aponta para arquivo inexistente (404). Ao compartilhar no WhatsApp ou no LinkedIn, sai sem imagem. | `og:image` de 5 cases: `residencial-monte-carlo`, `residencial-vila-atlantico`, `residencial-ville-luxemburgo`, `residencial-portal-do-cerrado`, `residencial-scharle`. Essas fotos não têm versão de 1200 px (a maior é 960, 1034, 640, 960 e 800). | Média | webdesigner-senior | Em `build.py`, linha 315, usar a maior largura ≤ 1200 disponível no manifesto: `w = max([x for x in IMGS[f'projetos/{p["slug"]}']['widths'] if x <= 1200]); og = f'/assets/img/projetos/{p["slug"]}-{w}.jpg'`. Ou usar `og-image.jpg` quando `baixa_res`. Rodar o build e repetir o HEAD dos `og:image`. A falha escapou da varredura do validador, que não lia as metatags. |
| **QA-02** | O guia de migração e o DS ainda mandam aplicar `hyphens: auto` nos títulos, a regra removida no REG-01. Quem montar o Kit pelo guia reintroduz a regressão. | `04-guia-migracao-elementor.md` §3.3 (linha 77) e `04-design-system.md` §9 (linha 191) | Média | webdesigner-senior | Trocar por: `` `h1–h4 { overflow-wrap: break-word }` (sem `hyphens: auto`, ver REG-01) e a escala reduzida abaixo de 360 px``. No DS: "Títulos com `overflow-wrap: break-word` (sem hifenização automática)". Incluir também no guia as regras N-01 (C20 < 360 px) e N-02 ("Configurar" com 44 px no banner do Complianz). |
| QA-03 | Os blocos técnicos marcados no copy como **[VALIDAR COM O RT]** saem publicados sem nenhuma sinalização, nem no modo revisão: entregáveis, normas (NBR) e respostas técnicas das FAQs das 9 páginas de serviço. O cliente pode aprovar sem perceber que precisa conferir. | 9 páginas de serviço (SV-03, SV-05, SV-08) | Média | coordenador → cliente (RT); webdesigner-senior (opcional: selo no modo revisão) | Enviar ao Carlos a lista de entregáveis e normas por disciplina para cortar ou confirmar, como parte da aprovação. Se possível, pôr um `ph()` "Conteúdo técnico · validar com o RT" nesses blocos enquanto `REVISAO = True`. |
| QA-04 | Promessas sem confirmação do cliente aparecem como fato no hero do Contato: "Atendimento direto com o engenheiro" e "Seus arquivos tratados com sigilo" (copy 18.2, item 20). "Proposta com escopo, prazo e valor" também aparece em vários CTAs. | `/contato/` (CT-02) | Média | coordenador → cliente | Confirmar com o cliente antes de publicar. Se não confirmar, o copywriter troca os selos. |
| QA-05 | No C05, o número e o rótulo não têm espaço entre si (`<strong>24</strong><span>clientes…`). O texto lido fica "24clientes atendidos…", e o copy H-03 pede leitura corrida. | C05 em Home, `/projetos/` e `/sobre/` | Baixa | webdesigner-senior | Em `componentes.py` (C05), inserir um espaço: `<strong>24</strong> <span class="lbl">…`. |
| QA-06 | A mensagem de falha do formulário curto usa a mensagem de WhatsApp "Estou na página de contato…" também na Home e nas 9 páginas de serviço, onde ela não é verdade. | `FALHA_ENVIO` (C21b), em `componentes.py`, linha 392 | Baixa | copywriter + webdesigner-senior | Mensagem própria para a falha, como sugeriu o validador. Correção exata: `Olá! Tentei enviar o pedido de orçamento pelo site da Intrépida e deu erro. Podem me ajudar?` (incluir no copy §2.6). |
| QA-07 | `+5.800` depende das 236 unidades do Gran Vic Gama, número repetido do Alto Boa Vista. A soma atual é 5.874; se o Gran Vic Gama tiver < 162 unidades, o número cai. No protótipo, o número não tem marca de conferência visível. | C05 (Home, Projetos, Sobre) e o case Gran Vic Gama | Média | coordenador → cliente | Pôr na lista de confirmação do cliente. Se ele não confirmar até a publicação, usar o item alternativo do copy: `1.800` · `unidades no maior empreendimento do portfólio`. |
| QA-08 | Desvio do glossário (copy §1.3: "concessionária", não "companhia"). O texto veio assim do próprio copy aprovado. | `/servicos/projeto-hidrossanitario/`, SV-05 (`servicos.json`, linha 41) | Baixa | copywriter | Correção exata: "os padrões da **concessionária de saneamento** do município". |
| QA-09 | O `robots.txt` bloqueia `/obrigado/` e a página também tem `noindex`. Com o bloqueio, o robô não lê o `noindex`. | `site/robots.txt` e guia §8 | Baixa | webdesigner-senior | No WordPress, tirar o `Disallow: /obrigado/` e deixar só o `noindex` (Rank Math). `/_build/` não existe no WP. |
| QA-10 | A 404 tem `canonical` para `/404`, uma URL que não existe. | `site/404.html` | Baixa | webdesigner-senior | Remover o canonical da 404 (no WP, o Rank Math já não emite). |
| QA-11 | `_redirects-301.txt` não traz a regra `?elementskit_template=*` → `/`, que está no guia §7, e o guia o chama de "arquivo pronto". | `site/_redirects-301.txt` | Baixa | webdesigner-senior | Acrescentar a regra, ou anotar no guia que ela é configurada à parte no Rank Math (regex por query string). |
| QA-12 | Cores usadas sobre fundo escuro (`#FFC3AD`, `#FFB59C`) não estão nas Global Colors do Kit (guia §3.1). Aparecem só no DS 2.1 e no Custom CSS. | guia §3.1 | Baixa | webdesigner-senior | Acrescentar "Eyebrow em fundo escuro `#FFC3AD`" e "Ícone/rótulo em fundo escuro `#FFB59C`" ao Kit. |
| QA-13 | O CTA "Tem um empreendimento parecido?" aparece duplicado nas páginas de projeto (UX-21). | 18 cases | Baixa | wireframe | Decidir: trocar o título do C13 final ou usar o formulário curto. |
| QA-14 | O banner de cookies cobre o CTA do hero em 320×568 (UX-08 residual). | todas as páginas, 1ª visita | Baixa | copywriter | Aprovar o texto curto para mobile proposto em `04-correcoes-ux.md`. No WP, aplicar no Complianz. |
| QA-15 | O HTML do protótipo traz comentários internos (`<!-- CONDICIONAL … -->`, `<!-- MINUTA — VALIDAR… -->`) e spans `.ph-flag` ocultos. Não aparecem na tela e não vão para o WordPress, mas ficariam visíveis no código-fonte se o protótipo estático fosse publicado como está. | 36 páginas | Baixa | webdesigner-senior | Só se o HTML estático for usado em produção: remover os comentários e `ph()` no build com `REVISAO = False`. |

### Pendências que dependem do cliente

**Bloqueiam a publicação**
| ID | Dado / decisão | Impacto |
|---|---|---|
| CL-01 | Dados da Política de privacidade. São 12 marcações pendentes: razão social, CNPJ, encarregado, ferramentas (GA4/GTM), anti-spam (Turnstile ou reCAPTCHA), fornecedores, prazos de guarda e de resposta, "novidades", data. Revisão jurídica. | A Política não pode ir ao ar como minuta, e o consentimento dos formulários remete a ela (UX-12). |
| CL-02 | E-mail que recebe os leads (hoje carlos@intrepidaengenharia.com.br), cópia ao usuário (Email 2), limite de upload em MB, e SPF/DKIM para o WP Mail SMTP. | Sem isso não há captação. `/obrigado/` afirma "Enviamos uma cópia do pedido para o seu e-mail" (UX-23). |
| CL-03 | Validação técnica do RT dos blocos [VALIDAR COM O RT]: entregáveis, normas e FAQs das 9 disciplinas, e o escopo de "Sistemas" (QA-03). | Hoje o site afirmaria entregáveis que podem não ser feitos. |
| CL-04 | Confirmar "atendimento direto com o engenheiro" e "sigilo dos arquivos" (QA-04). | São promessas publicadas no Contato. |
| CL-05 | Unidades do Gran Vic Gama (236?), que condicionam o `+5.800` (QA-07). | É um número público no C05 de 3 páginas. |
| CL-06 | Acessos: hospedagem, DNS (devopers), registro.br e contas GA4/GTM/Search Console. | Pré-requisitos do guia §1. |

**Não bloqueiam (o site tem fallback), mas fortalecem**
- CNPJ, razão social e CREA (empresa e RT): rodapé e `#dados-cadastrais` (UX-11). Para a P2 (homologação de fornecedor), é muito recomendável antes do lançamento.
- Disciplinas por projeto (UX-10).
- Nome da Prix (Construtora × Engenharia, UX-19).
- Rótulo do "24" (Center Norte, CTE, Chandon).
- "Lagoa dos Príncipes e Lagoa Nova": um ou dois empreendimentos?
- Prazo de resposta, concessionárias, softwares e formatos BIM, horário, atendimento presencial.
- LinkedIn, PDF do portfólio.
- Foto do Carlos (fotografar), fotos dos 6 projetos sem imagem, crédito exigido nas fotos, vetores da Mello Azevedo e da Chandon.
- Depoimentos, equipe e linha do tempo.

---

## 4. Separação pedida pelo coordenador

### (a) Impedem a entrega do protótipo para aprovação do cliente
**Nenhum item bloqueante.** Não há Crítico nem Alto em aberto.

Recomendo corrigir **antes do envio**, junto (minutos de trabalho, sem nova rodada de validação):
- **QA-01:** `og:image` quebrada em 5 cases (1 linha no `build.py`).
- **QA-02:** guia e DS ainda pedem `hyphens: auto` (2 linhas de documentação).
- **QA-05:** espaço no C05 (1 caractere).

Ao enviar, levar junto a lista CL-01 a CL-06 e o pedido de validação técnica do RT (QA-03), porque a aprovação do cliente precisa cobrir esses conteúdos.

### (b) Impedem a PUBLICAÇÃO no WordPress
1. **CL-01** Política de privacidade completa e revisada (LGPD).
2. **CL-02** E-mail de leads, SMTP e teste real de envio dos 2 formulários; texto do `/obrigado/` coerente com o Email 2.
3. **CL-03 / QA-03** Validação técnica do RT.
4. **CL-04 / QA-04** Promessas do Contato confirmadas.
5. **CL-05 / QA-07** `+5.800` confirmado, ou troca pelo item alternativo.
6. **CL-06** Acessos de hospedagem, DNS e analytics. Consent Mode v2 com "Recusar" sem GA4.
7. **QA-02** Guia corrigido antes de montar o Kit (senão a REG-01 volta).
8. Checklist do guia §10, inteiro:
   - 301 testados;
   - 404 com status real (UX-23);
   - `REVISAO = False` (ver seção 5);
   - fontes locais (LGPD);
   - Turnstile/honeypot;
   - `noindex` só na homologação;
   - novo QA no ambiente WordPress (os formulários reais e o Complianz não existem no protótipo e precisam ser testados lá).

### (c) Melhorias opcionais
QA-06, QA-08, QA-09, QA-10, QA-11, QA-12, QA-13, QA-14 e QA-15. Também:
- `lastmod` no sitemap e `twitter:card` (o Rank Math gera);
- recortes 1200×630 próprios para o `og:image` dos cases.

---

## 5. Troca para `REVISAO = False` (verificado)

Fiz um build numa cópia com `REVISAO = False` e comparei com o atual.
- **A única diferença nas 36 páginas** é a classe `modo-revisao` sair do `<html>`. O CSS `.ph-flag { display:none }` esconde os selos, e o JS não depende da classe.
- **No navegador:** removi a classe em `/sobre/` e `/projetos/smart-haus/`. Os selos somem, o layout não se desloca, a variante "sem foto" do case fica íntegra e o bloco do RT mostra o símbolo da marca.
- **O que NÃO muda com `REVISAO = False`:**
  - as 12 marcações amarelas da Política (`pend()`), que só somem com os dados preenchidos (correto: bloqueiam a publicação);
  - os selos "Imagem ilustrativa" das imagens de IA, que **devem continuar** em produção;
  - o hero do `/sobre/`, que continua com a foto do Bosque dos Ipês e a legenda dela. É aceitável: a foto é identificada e não se passa por escritório ou equipe.
- **Nada quebra.**

## 6. Prontidão do guia de migração

**Completo e executável.** O guia cobre:
- pré-requisitos e homologação;
- plugins mínimos e Kit (cores, fontes, botões, campos, Custom CSS);
- páginas, CPT "Projetos" com ACF e importação a partir de `conteudo.json` (o arquivo existe e tem os 18 projetos com todos os campos);
- opções globais equivalentes ao `DADOS`;
- os templates do Theme Builder por ID do wireframe;
- formulários (etapas, ocultos, `?servico=`, ações, anti-spam, GA4);
- 301, SEO e schema, performance;
- checklist de publicação.

**Ajustes antes de usar:**
- **QA-02** (obrigatório): `hyphens: auto` e regras N-01/N-02.
- **QA-09** e **QA-11**: robots e regra do ElementsKit.
- **QA-12**: cores do Kit.

**Riscos conhecidos e já registrados no guia:**
- Campos condicionais e contagem cruzada de filtros dependem de colar trechos do `site.js` em Custom Code, ou de plugin extra.
- O link do mapa C24 precisa ser ajustado ao formato de URL do Taxonomy Filter.
- O ACF Free não tem Options Page nem Gallery. O guia já dá a alternativa (post privado / 3 campos).

---

## 7. Contagem por severidade

| Severidade | Qtde | IDs |
|---|---|---|
| Crítica | 0 | — |
| Alta | 0 | — |
| Média | 5 | QA-01, QA-02, QA-03, QA-04, QA-07 |
| Baixa | 10 | QA-05, QA-06, QA-08 a QA-15 |
| Dependem do cliente | 6 bloqueantes (CL-01 a CL-06) + itens com fallback | seção 3 |

---

## 8. Parecer final

### Protótipo para aprovação do cliente: **PRONTO PARA ENTREGA**
Não há pendência Crítica nem Alta.
- **Briefing, wireframe, copy e DS:** estão alinhados. O texto publicado é o copy aprovado, sem divergências nas amostras.
- **Dados:** contatos, endereço e números estão corretos e só os autorizados.
- **Imagens:** as geradas por IA estão sinalizadas.
- **Técnico:** sem erros de console, sem links quebrados e sem estouro em 320–1440 px.

Condição de envio (minutos): corrigir **QA-01**, **QA-02** e **QA-05**. Ao enviar, incluir a lista CL-01 a CL-06 e o pedido de validação técnica ao RT.

### Publicação no WordPress: **NÃO PRONTO**
Mínimo para ficar pronto:
1. Política de privacidade completa e revisada (CL-01).
2. E-mail de leads, SMTP e teste real dos 2 formulários (CL-02).
3. Validação do RT e das promessas do Contato (CL-03, CL-04).
4. `+5.800` confirmado ou trocado (CL-05).
5. Acessos de hospedagem, DNS e analytics (CL-06).
6. Montagem seguindo o guia corrigido (QA-02).
7. Nova rodada de QA no ambiente WordPress de homologação, com `REVISAO = False` e o checklist do guia §10.

## Correções aplicadas após o QA (coordenador, 21/11/2026)
| ID | Correção | Verificação |
|---|---|---|
| QA-01 | `og:image` dos projetos usa a maior largura disponível ≤ 1200 px (`build.py`) | Todas as `og:image` das 36 páginas apontam para arquivos existentes |
| QA-02 | Guia de migração e design system sem `hyphens: auto`; N-01 e N-02 incluídos no guia | Texto revisado |
| QA-05 | Espaço entre número e rótulo na barra de números (`componentes.py`) | HTML gerado: `<strong>24</strong> <span …>` |
| QA-08 | "companhia de saneamento" → "concessionária de saneamento" (copy e `servicos.json`) | Página Hidrossanitário regenerada |
| QA-09 | `/obrigado/` removido do `robots.txt` (a página já tem `noindex`) | Arquivo revisado |
