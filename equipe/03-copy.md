# 03 — Copy do site: Intrépida Engenharia e Projetos

> Etapa: Copy (agente `copywriter`). Data: 21/11/2026.
> Base: `equipe/01-contexto.md` (briefing aprovado), `equipe/02-wireframe.md` + `equipe/wireframes/` (wireframe aprovado) e decisões do usuário registradas no `CLAUDE.md` (21/11/2026).
> Plataforma: WordPress + Elementor. Os IDs de seção (H-02, SV-03, CT-03…) e de componente (C01…C24) são os do wireframe. O web designer encaixa cada bloco pelo ID.

## 0. Como ler este documento

**Marcações**
| Marcação | Significado | O que fazer |
|---|---|---|
| **[INSERIR DADO REAL: …]** | Dado que só o cliente pode dar (CNPJ, CREA, prazo, softwares…). | Não publicar o trecho até o dado chegar. Cada bloco traz a **versão sem o dado** (fallback), pronta para uso. |
| **[DERIVADO DO PORTFÓLIO — conferir]** | Número calculado a partir do material real, não declarado pelo cliente. | O QA confere a conta antes de publicar. |
| **[VALIDAR COM O RT]** | Conteúdo técnico de referência (normas, entregáveis típicos) escrito a partir do conhecimento da disciplina, não de uma declaração da empresa. | O responsável técnico confirma ou corta itens. Nada nesses blocos afirma experiência ou número da empresa. |
| **CONDICIONAL** | Seção que só entra com dado real (regra do wireframe). | Sem o dado, a seção some inteira. Nunca publicar placeholder. |
| `texto em código` | Texto exato de interface (botão, label, mensagem). | Copiar como está. |

**Fonte de cada fato usado na copy** (nada fora desta lista foi afirmado):
- Disciplinas, 2D e BIM, mensagem "projetista desde o começo / concessionárias de energia, água, gás e telecom", BIM para "execução, implantação, manutenção e gerenciamento": site antigo [SITE-2025].
- 24 clientes, 18 empreendimentos, 6 UFs, dados de cada empreendimento (nome, cliente, cidade/UF, unidades): portfólio 2024 + site antigo, mantidos como estavam (decisão do usuário).
- Carlos Alberto Grope, Diretor Técnico, engenheiro civil sanitarista: manual da marca + decisão do usuário.
- Contatos e endereço: decisão do usuário (21/11/2026).

---

## 1. Posicionamento, tom de voz e glossário

### 1.1 Posicionamento escolhido
**Frase-mãe (uso interno e base do rodapé):** Projetos de instalações prediais e infraestrutura, em 2D e BIM, para construtoras, incorporadoras e arquitetos.

**H1 da Home:** `Projetos de instalações e infraestrutura para incorporadoras e construtoras` (9 palavras).

Por que este H1:
- Diz **o que é** (projetos, e não obras, que era a confusão do site antigo) e **para quem é** em uma linha. Passa no teste dos 5 segundos.
- Traz as palavras que o coordenador de projetos busca ("projetos de instalações", "incorporadoras").
- Não promete o que não dá para provar ("aprovação garantida", "zero retrabalho"). O benefício (compatibilização, aprovação nas concessionárias) fica no subtítulo, com formulação defensável.

Alternativas para teste A/B depois do lançamento (mesmo subtítulo):
- B: `Projetos de instalações em BIM para empreendimentos residenciais em escala`
- C: `Instalações prediais e infraestrutura projetadas desde o estudo de viabilidade`

### 1.2 Tom de voz
**Técnico, seguro e objetivo: de engenheiro para engenheiro.**
- Frases curtas. Parágrafos de até 3 linhas. Uma ideia por frase.
- Benefício antes da característica: primeiro o que muda para o cronograma e a obra, depois a técnica.
- Trata o leitor por "você" e, quando cabe, "sua incorporadora", "seu empreendimento".
- Prova em vez de adjetivo: cliente, cidade, número de unidades. Proibido: "excelência", "qualidade", "soluções inovadoras", "construindo o futuro", "soluções inteligentes", superlativos.
- Termos técnicos corretos (ART, NBR, BIM, concessionária, compatibilização), explicados em uma frase nas FAQs de cada serviço para o leigo (P4).
- O nome "Intrépida" (corajosa) aparece uma vez, na página Sobre. Sem trocadilhos no resto do site.

### 1.3 Glossário de consistência (usar sempre igual)
| Use | Não use | Observação |
|---|---|---|
| Solicitar orçamento | Pedir orçamento, Fale conosco, Saiba mais (em CTA de conversão) | CTA primário em todo o site. |
| Falar no WhatsApp | Chamar no zap, Fale conosco | CTA secundário. |
| empreendimento | obra (para o produto do cliente) | "Obra" só para a fase de execução ("retrabalho na obra"). |
| projeto | trabalho, job | O que a Intrépida entrega. |
| construtoras e incorporadoras | construtoras/incorporadoras, players | Nessa ordem. |
| disciplina | especialidade, modalidade | Hidrossanitário, elétrica etc. |
| concessionária | companhia, operadora | Energia, água/esgoto, gás, telecom. |
| compatibilização | compatibilidade (como serviço) | |
| BIM (modelo 3D) na 1ª menção da página; depois só BIM | 3D BIM, Bim | |
| Cidade/UF | Cidade - UF, Cidade (UF) | Ex.: `Belo Horizonte/MG`. |
| unidades | apartamentos, casas, UH | Número com ponto de milhar: `1.800 unidades`. |
| reúso | reuso | Grafia correta no texto. O slug segue `reuso-de-agua-pluvial` (sem acento, como aprovado). |
| Climatização (HVAC) | Ar-condicionado e ventilação (como nome do serviço) | Nome do serviço. |
| Elétrica e Sistemas | Elétrico e Sistemas | Nome do serviço, como no site antigo. |
| Intrépida | Intrepida | Sempre com acento no texto. Razão social: [INSERIR DADO REAL]. |

### 1.4 Nomes dos serviços (rótulos curtos, usados em menu, cards, formulário e tags)
| Slug | Rótulo curto (menu/tags) | Nome da página (H1 base) |
|---|---|---|
| `projeto-hidrossanitario` | Hidrossanitário | Projeto hidrossanitário |
| `projeto-eletrico` | Elétrica e Sistemas | Projeto elétrico e de sistemas |
| `projeto-de-gas` | Gás | Projeto de gás |
| `climatizacao-hvac` | Climatização (HVAC) | Projeto de climatização (HVAC) |
| `pressurizacao-de-escadas` | Pressurização de escadas | Projeto de pressurização de escadas |
| `projeto-de-piscina` | Piscina | Projeto de piscina |
| `infraestrutura-de-saneamento` | Infraestrutura de saneamento | Projeto de infraestrutura de saneamento |
| `reuso-de-agua-pluvial` | Reúso de água pluvial | Projeto de aproveitamento de água de chuva |
| `aquecimento-solar` | Aquecimento solar | Projeto de aquecimento solar |
| `/bim-e-compatibilizacao/` | BIM e compatibilização | BIM e compatibilização de projetos |

Valores do parâmetro `?servico=` (para pré-marcar o formulário): `hidrossanitario`, `eletrica`, `gas`, `hvac`, `pressurizacao`, `piscina`, `saneamento`, `reuso-pluvial`, `aquecimento-solar`, `compatibilizacao-bim`, `nao-sei`.

---

## 2. Componentes globais

### 2.1 C01 Header (todas as páginas)
- Logo (link para `/`): `alt="Intrépida Engenharia e Projetos"`; rótulo acessível do link: `Intrépida Engenharia e Projetos, página inicial`.
- Menu desktop: `Serviços` · `BIM` · `Projetos` · `Sobre` · `Contato`
- Ícone WhatsApp (desktop): `aria-label="Falar no WhatsApp (abre em nova aba)"`; tooltip: `WhatsApp (31) 99649-8629`.
- Botão: `Solicitar orçamento` → `/contato/`
- Link "pular para o conteúdo" (primeiro foco da página): `Pular para o conteúdo`

**Mega-menu "Serviços" (desktop)**
| Coluna | Título | Links |
|---|---|---|
| 1 | Instalações prediais | Hidrossanitário · Elétrica e Sistemas · Gás · Climatização (HVAC) · Pressurização de escadas · Piscina |
| 2 | Infraestrutura urbana | Infraestrutura de saneamento |
| 3 | Eficiência e sustentabilidade | Reúso de água pluvial · Aquecimento solar |
| Rodapé do painel | — | `Ver todos os serviços →` (`/servicos/`) · `BIM e compatibilização →` (`/bim-e-compatibilizacao/`) |

Linha de apoio opcional abaixo do título de cada coluna (desktop, 1 linha):
- Instalações prediais: `Sistemas do edifício, do subsolo à cobertura.`
- Infraestrutura urbana: `Redes de água, esgoto e drenagem.`
- Eficiência e sustentabilidade: `Menos consumo de água e energia.`

**Menu mobile (drawer)**
- Botão de abrir: `aria-label="Abrir menu"`. Botão de fechar (ícone X): `aria-label="Fechar menu"`.
- Accordion: `Serviços` → 3 grupos com os 9 links + `Ver todos os serviços`
- Itens: `BIM e compatibilização` · `Projetos` · `Sobre` · `Contato`
  (No drawer, "BIM" ganha o nome completo, porque há espaço e fica mais claro.)
- Botão largo: `Solicitar orçamento`
- Linha de contato (3 ícones com texto): `WhatsApp` · `Ligar` · `E-mail`
  - `aria-label`: `Falar no WhatsApp (abre em nova aba)` · `Ligar para (31) 3070-6568` · `Enviar e-mail para carlos@intrepidaengenharia.com.br`

### 2.2 C14 Breadcrumb
- Rótulo do primeiro nível: `Início`. Separador visual "›" (oculto para leitor de tela; usar `<nav aria-label="Você está em">`).
- Mobile: `‹ Serviços`, `‹ Projetos` (só o nível anterior).
- Exemplos: `Início › Serviços › Projeto hidrossanitário` · `Início › Projetos › Mirante São Lucas` · `Início › BIM e compatibilização`.

### 2.3 C02 Rodapé (todas as páginas)
**Coluna 1 — Marca**
- Logo branco: `alt="Intrépida Engenharia e Projetos"`
- Texto: `Projetos de instalações prediais e infraestrutura, em 2D e BIM, para construtoras, incorporadoras e arquitetos.`
- LinkedIn: `aria-label="Intrépida no LinkedIn (abre em nova aba)"` — **CONDICIONAL** [INSERIR DADO REAL: URL do LinkedIn]. Sem URL → ícone sai.
- Botão secundário: `Baixar portfólio (PDF)` — **CONDICIONAL** [INSERIR DADO REAL: PDF liberado e atualizado]. Sem PDF → botão sai.

**Coluna 2 — Serviços** (título `Serviços`)
Hidrossanitário · Elétrica e Sistemas · Gás · Climatização (HVAC) · Pressurização de escadas · Piscina · Infraestrutura de saneamento · Reúso de água pluvial · Aquecimento solar · BIM e compatibilização

**Coluna 3 — Institucional** (título `A Intrépida`)
Projetos · Clientes · Sobre · Contato · Política de privacidade

**Coluna 4 — Contato** (título `Fale com a gente`)
- `WhatsApp (31) 99649-8629` → `https://wa.me/5531996498629?text=…` (mensagem da seção 2.6)
- `Telefone (31) 3070-6568` → `tel:+553130706568`
- `carlos@intrepidaengenharia.com.br` → `mailto:carlos@intrepidaengenharia.com.br` (**corrige** o link antigo, que apontava para outro endereço)
- Endereço:
  `Rua dos Goitacazes, 103, salas 1604 e 1606`
  `Centro, Belo Horizonte/MG`
  `CEP 30190-910`
- Horário: **CONDICIONAL** [INSERIR DADO REAL: horário de atendimento]. Formato quando chegar: `Segunda a sexta, das [h] às [h]`.

**Barra inferior**
`© 2026 [INSERIR DADO REAL: razão social] · CNPJ [INSERIR DADO REAL] · CREA [INSERIR DADO REAL: registro da empresa] · Política de privacidade`
Fallback (sem os dados): `© 2026 Intrépida Engenharia e Projetos · Política de privacidade`

> Nota para o designer: o ano do © deve ser dinâmico (shortcode de ano no WordPress), para não repetir o "© 2024" desatualizado do site antigo.

### 2.4 C19 WhatsApp flutuante (desktop) e C20 barra fixa (mobile)
- C19: `aria-label="Falar no WhatsApp (abre em nova aba)"`; balão opcional ao passar o mouse: `Dúvidas? Fale no WhatsApp`.
- C20: botão primário `Solicitar orçamento` · botão secundário `WhatsApp` (ícone + texto).
  - Em páginas de serviço, o primário continua `Solicitar orçamento` (o texto longo não cabe), mas o link leva `?servico=[valor]`.

### 2.5 C23 Banner de cookies (LGPD)
- Texto: `Usamos cookies para o site funcionar e, com a sua permissão, para medir as visitas e melhorar o conteúdo. Saiba mais na nossa Política de privacidade.`
- Botões (mesmo peso visual entre "Aceitar" e "Recusar"): `Aceitar todos` · `Recusar opcionais` · `Configurar`
- Painel "Configurar":
  - Título: `Preferências de cookies`
  - `Necessários` — `Fazem o site funcionar, como o formulário e a proteção contra spam. Sempre ativos.`
  - `Medição` — `Contam visitas e cliques de forma agregada (Google Analytics) para sabermos o que funciona no site.` (chave liga/desliga, desligada por padrão)
  - Botão: `Salvar preferências`
- Link permanente no rodapé (opcional, recomendado): `Preferências de cookies`

### 2.6 Mensagens pré-preenchidas do WhatsApp
Base do link: `https://wa.me/5531996498629?text=` + mensagem codificada em URL. Nenhuma mensagem leva dado pessoal.

| Onde | Mensagem |
|---|---|
| Header, C19, C20, rodapé (padrão) | `Olá! Vim pelo site da Intrépida e quero falar sobre um projeto.` |
| Home (hero e CTA final) | `Olá! Vim pelo site da Intrépida e quero um orçamento de projeto.` |
| Hub de serviços | `Olá! Vim pela página de serviços do site da Intrépida e quero ajuda para definir os projetos do meu empreendimento.` |
| Página de serviço | `Olá! Vim pelo site da Intrépida (página: [nome do serviço]) e quero um orçamento.` — ex.: `(página: Projeto hidrossanitário)` |
| BIM e compatibilização | `Olá! Vim pelo site da Intrépida e quero falar sobre projetos em BIM e compatibilização.` |
| Projetos (listagem) | `Olá! Vi os projetos no site da Intrépida e quero falar sobre o meu empreendimento.` |
| Página de projeto | `Olá! Vi o projeto [nome do empreendimento] no site da Intrépida e tenho um empreendimento parecido.` |
| Sobre | `Olá! Vim pela página Sobre do site da Intrépida e quero falar sobre um projeto.` |
| Contato | `Olá! Estou na página de contato do site da Intrépida e prefiro conversar por aqui.` |
| Obrigado | `Olá! Acabei de enviar um pedido de orçamento pelo site da Intrépida e quero mandar os arquivos do projeto.` |
| 404 | `Olá! Não encontrei uma página no site da Intrépida. Podem me ajudar?` |

---

## 3. Home (`/`)

### SEO — Home
- **Title:** Projetos de instalações prediais e BIM em BH | Intrépida
- **Meta description:** Projetos hidrossanitários, elétricos, de gás e de infraestrutura, em 2D e BIM, para incorporadoras. 24 clientes em 6 estados. Solicite orçamento.
- **Palavra-chave principal:** projetos de instalações prediais
- **Secundárias:** projeto hidrossanitário BH; projetos complementares para incorporadoras; projeto BIM de instalações; projeto de infraestrutura de saneamento; engenharia de projetos Belo Horizonte
- **Slug:** `/`
- **H1:** ver H-02

### H-02 Hero (C03)
- **Eyebrow:** `Engenharia de projetos · Belo Horizonte/MG`
- **H1:** `Projetos de instalações e infraestrutura para incorporadoras e construtoras`
- **Subtítulo:** `Hidrossanitário, elétrica, gás e mais seis disciplinas, em 2D ou BIM, compatibilizadas para reduzir retrabalho e pensadas para aprovar nas concessionárias.`
- **CTA primário:** `Solicitar orçamento` → `/contato/`
- **CTA secundário:** `Falar no WhatsApp` → mensagem "Home" (2.6)
- **Microprova:** `24 clientes, entre construtoras e incorporadoras · Empreendimentos em 6 estados`
- **Crédito da foto (canto):** `Mirante São Lucas · UNENCO · Belo Horizonte/MG`
- **Alt da imagem:** `Vista aérea do Mirante São Lucas, torre residencial da UNENCO em Belo Horizonte/MG`

### H-03 Barra de números (C05) — 4 itens
| Número | Rótulo | Nota |
|---|---|---|
| `24` | `clientes atendidos, entre construtoras e incorporadoras` | Contagem real (24 logos do portfólio). Ver nota abaixo da tabela sobre o rótulo. |
| `18` | `empreendimentos no portfólio` | Contagem real (12 do portfólio 2024 + 6 do site antigo). |
| `6` | `estados: MG, DF, SP, RJ, MS e SC` | Contagem real. |
| `+5.800` | `unidades nos empreendimentos do portfólio` | **[DERIVADO DO PORTFÓLIO — conferir]** Soma das unidades dos 18 empreendimentos = 5.874. Inclui os 236 de Gran Vic Gama, que repetem o número de Alto Boa Vista. Se o número correto de Gran Vic Gama for menor que 162, a soma cai abaixo de 5.800 e o item precisa ser refeito. |

- **Nota sobre o rótulo do "24":** a decisão do usuário fala em "24 construtoras/incorporadoras". Ao conferir os 24 logos, três não parecem ser construtoras ou incorporadoras: **Center Norte** (assinatura "O shopping da família"), **CTE – Centro de Tecnologia de Edificações** (consultoria) e **Chandon** (atividade não identificada). Para não afirmar algo impreciso, a copy usa `24 clientes, entre construtoras e incorporadoras`. Se o cliente confirmar que as 24 atuaram como construtoras ou incorporadoras, trocar por `24 construtoras e incorporadoras atendidas` (H-02, H-03, H-04, PJ-06, SB-03).
- Sem "anos de mercado", m² ou qualquer outro número (decisão do usuário).
- Item opcional para substituir o 4º, se o QA não validar a soma: `1.800` · `unidades no maior empreendimento do portfólio` (Residencial Monte Carlo, dado real).
- Leitura acessível: cada item como texto corrido para leitor de tela (ex.: "24 clientes atendidos, entre construtoras e incorporadoras"), sem depender da separação visual.

### H-04 Logos de clientes (C06, 12 logos)
- **H2:** `Quem já contratou nossos projetos`
- **Linha de apoio:** `24 clientes atendidos. Alguns deles:`
- **Link:** `Ver todos os clientes e projetos →` (`/projetos/#clientes`)
- **Alt de cada logo:** só o nome do cliente (lista completa na seção 13.3).

### H-05 Serviços (C07, 3 grupos)
- **H2:** `O que projetamos`
- **Intro:** `Nove disciplinas de instalações e infraestrutura com um só fornecedor, compatibilizadas entre si.`

**H3 `Instalações prediais`**
| Serviço | Descrição (some no mobile) |
|---|---|
| Hidrossanitário | `Água fria e quente, esgoto, águas pluviais e medição individualizada.` |
| Elétrica e Sistemas | `Entrada de energia, quadros, iluminação, tomadas e sistemas prediais.` |
| Gás | `Rede interna de gás natural ou GLP, prumadas e medição.` |
| Climatização (HVAC) | `Ar-condicionado, ventilação e exaustão dimensionados pela carga térmica.` |
| Pressurização de escadas | `Controle de fumaça nas escadas de emergência do edifício.` |
| Piscina | `Filtragem, recirculação, casa de máquinas e aquecimento.` |

**H3 `Infraestrutura urbana`** (card maior)
| Serviço | Descrição |
|---|---|
| Infraestrutura de saneamento | `Redes de água, esgoto e drenagem para loteamentos e condomínios, prontas para a análise da concessionária.` |
Selo do card: `Redes de água, esgoto e drenagem`

**H3 `Eficiência e sustentabilidade`**
| Serviço | Descrição |
|---|---|
| Reúso de água pluvial | `Captação e aproveitamento da água de chuva para usos não potáveis.` |
| Aquecimento solar | `Coletores, reservatórios térmicos e rede de água quente.` |

- Link de cada card: `Saiba mais →` (rótulo acessível: `Saiba mais sobre o projeto [nome]`)
- **Faixa abaixo dos grupos:** `BIM e compatibilização em todas as disciplinas →` (`/bim-e-compatibilizacao/`)
- **Link da seção:** `Ver todos os serviços`

### H-06 Aprovação em concessionárias (C18)
- **H2:** `A aprovação na concessionária está travando o seu cronograma?`
- **Texto:** `Projeto que chega à concessionária fora do padrão volta com exigências, e cada reanálise empurra a obra. Com o projetista calculista desde o estudo de viabilidade, as normas e as exigências das concessionárias de energia, água, gás e telecomunicações entram no projeto desde a primeira versão.`
- **Bullets (ícone + texto):**
  1. `Normas técnicas e padrões da concessionária considerados desde o início`
  2. `Projeto preparado para reduzir exigências e reanálises`
  3. `Cronograma de aprovação mais previsível para a obra`
- **Selos das concessionárias:** **CONDICIONAL** [INSERIR DADO REAL: concessionárias em que a Intrépida já aprovou projetos, ex.: COPASA, CEMIG, Gasmig e de outras UFs]. Título dos selos quando houver: `Projetos aprovados em:`. Sem dado → selos saem; o texto acima funciona sozinho.
- **CTA:** `Enviar meu projeto para análise` → `/contato/`
- **Alt da imagem:** `Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS`

### H-07 BIM e compatibilização (C09 + C11)
- **H2:** `BIM para achar o conflito no modelo, e não na obra`
- **Texto:** `Modelamos as instalações em 3D e cruzamos todas as disciplinas antes de liberar o projeto. Tubulação que bate em viga, shaft sem espaço, quadro no lugar errado: o problema aparece na tela, quando corrigir ainda custa pouco.`
- **Benefícios (lista com check):**
  - `Interferências entre disciplinas resolvidas antes da obra`
  - `Quantitativos de materiais extraídos do modelo`
  - `Informação útil para execução, manutenção e gestão do empreendimento`
  - `Entrega em 2D quando o seu processo pedir`
- **CTA:** `Conheça nosso processo BIM →` (`/bim-e-compatibilizacao/`)
- **Galeria (4 imagens):** legendas e alt na seção 13.2 (imagens 1, 7, 5 e 8).

### H-08 Projetos em destaque (C08, 6 cards)
- **H2:** `Empreendimentos com projetos da Intrépida`
- **Link da seção:** `Ver todos os projetos →`
- **Botão no mobile (após 3 cards):** `Ver todos os 18 projetos`
- **Cards** (H3 = nome; linha = cliente · cidade/UF; destaque = unidades):

| Ordem | H3 | Linha | Destaque |
|---|---|---|---|
| 1 | `Mirante São Lucas` | `UNENCO · Belo Horizonte/MG` | `152 unidades` |
| 2 | `Bosque dos Ipês` | `RNI · Campo Grande/MS` | `142 unidades` |
| 3 | `Residencial Pacífico` | `Vila Construtora · Ribeirão das Neves/MG` | `160 unidades` |
| 4 | `Parque Lagoa dos Príncipes e Lagoa Nova` | `MRV · Lagoa Santa/MG` | `256 unidades` |
| 5 | `Residencial Alta Vista` | `Quartzo · Barueri/SP` | `240 unidades` |
| 6 | `Residencial Monte Carlo` | `Habit Construtora · Cabo Frio/RJ` | `1.800 unidades` |

- Tags de disciplina: **CONDICIONAL** [INSERIR DADO REAL: disciplinas projetadas em cada empreendimento]. Sem dado → tags ocultas.
- Rótulo acessível do card: `[Nome], [cliente], [cidade/UF], [n] unidades. Ver projeto`.

### H-09 Como trabalhamos (C10)
- **H2:** `Como trabalhamos`
- **Etapas** [INSERIR DADO REAL: confirmar etapas e nomes com o cliente. Texto abaixo segue a sugestão aprovada no wireframe, sem prazos e sem promessas novas]:
  1. `Briefing e análise` — `Você envia a arquitetura e as informações do empreendimento. Avaliamos escopo, disciplinas e exigências locais.`
  2. `Proposta` — `Você recebe escopo, prazo e valor por disciplina, para comparar e aprovar.`
  3. `Cálculo e modelagem` — `Dimensionamos os sistemas e modelamos as instalações em BIM ou desenhamos em 2D.`
  4. `Compatibilização e aprovação` — `Cruzamos as disciplinas com a arquitetura e a estrutura e preparamos o projeto para a análise das concessionárias.`
  5. `Entrega` — `Você recebe pranchas, memoriais e modelo, prontos para a obra.` [INSERIR DADO REAL: se há acompanhamento/assistência à obra, acrescentar: `e conta com o nosso suporte durante a execução.`]
- **Nota de prazo:** **CONDICIONAL** [INSERIR DADO REAL: prazo de resposta]. Com dado: `Resposta ao pedido de orçamento em até [X] dias úteis.` Sem dado → linha sai.

### H-10 Responsável técnico (C17 compacto)
- **H2:** `Quem responde pelos seus projetos`
- **Nome:** `Carlos Alberto Grope`
- **Cargo:** `Diretor técnico · Engenheiro civil sanitarista`
- **CREA:** **CONDICIONAL** [INSERIR DADO REAL: nº do CREA]. Formato: `CREA-MG [nº]`.
- **Texto:** `Os projetos da Intrépida são conduzidos pelo engenheiro civil sanitarista Carlos Alberto Grope, diretor técnico da empresa. No orçamento e durante o projeto, você fala com quem entende do cálculo.`
- **Link:** `Conheça a Intrépida →` (`/sobre/`)
- **Foto:** [INSERIR DADO REAL: retrato profissional — FOTOGRAFAR; não gerar por IA]. Enquanto não houver, variante sem foto (símbolo da marca). Alt quando houver: `Carlos Alberto Grope, diretor técnico da Intrépida Engenharia e Projetos`.

### H-11 Depoimentos (C16) — CONDICIONAL
- Só entra com depoimento real autorizado. **Nenhum texto foi escrito.**
- Estrutura quando houver: **H2** `O que dizem os clientes` · por card: citação (até 40 palavras) · `[INSERIR DADO REAL: nome]` · `[INSERIR DADO REAL: cargo]` · `[INSERIR DADO REAL: empresa]` · logo da empresa (alt = nome da empresa).
- Sem depoimentos → seção removida; a página segue de H-10 para H-12.

### H-12 Perguntas frequentes (C12, schema FAQPage)
- **H2:** `Dúvidas de quem contrata projetos`

**1. Vocês atendem empreendimentos de grande porte?** (aberta por padrão)
`Sim. O maior empreendimento do nosso portfólio tem 1.800 unidades: o Residencial Monte Carlo, da Habit Construtora, em Cabo Frio/RJ. Os demais vão de 142 a 368 unidades, para construtoras e incorporadoras como MRV, Direcional, RNI e Precon.`

**2. Vocês atendem a minha cidade?**
`Temos empreendimentos em seis estados: MG, DF, SP, RJ, MS e SC. Para outras localidades, envie o pedido de orçamento com a cidade do empreendimento e confirmamos o atendimento.`
[INSERIR DADO REAL: se o atendimento é remoto/nacional, trocar a segunda frase por: `Atendemos empreendimentos em todo o Brasil, com reuniões online.`]

**3. Qual é o prazo de um projeto?**
`Depende do porte, das disciplinas contratadas e da fase em que a arquitetura está. Por isso o prazo de cada etapa vem descrito na proposta, antes de você contratar.`
[INSERIR DADO REAL: se houver prazo típico, acrescentar: `Como referência, [exemplo de prazo real].`]

**4. Vocês trabalham no padrão BIM da minha empresa?**
Fallback (publicável hoje): `Entregamos em BIM (modelo 3D) ou em 2D. Se a sua empresa tem template, padrão de nomenclatura ou formato próprio, envie junto com o pedido de orçamento: a compatibilidade fica definida na proposta.`
Versão completa (com dado): `Sim. Modelamos em [INSERIR DADO REAL: software] e entregamos em [INSERIR DADO REAL: formatos, ex. RVT, IFC, DWG e PDF]. Se a sua empresa tem template ou padrão próprio, seguimos o seu padrão.`

**5. O que preciso enviar para receber o orçamento?**
`O projeto de arquitetura (DWG, PDF ou RVT), a implantação, o número de unidades ou a área construída, a cidade e as disciplinas de que você precisa. Ainda não tem tudo? Envie o que tiver e completamos juntos.`

**6. (proposta) A Intrépida executa a obra?**
`Não. A Intrépida faz projetos de engenharia: instalações prediais e infraestrutura. A execução fica com a sua construtora, que recebe um projeto completo e compatibilizado.`
> Proposta do copywriter: acrescentar esta 6ª pergunta (o C12 aceita até 8). O site antigo dizia "construção civil, do planejamento à execução", e a dúvida pode reaparecer em quem conheceu a empresa por ele. Se o coordenador preferir 5 perguntas, esta sai sem prejuízo.

### H-13 CTA final com formulário curto (C13 + C21b)
- **H2:** `Conte sobre o seu empreendimento e receba uma proposta`
- **O que acontece depois (3 itens numerados):**
  1. `Analisamos as informações e os arquivos que você enviar.`
  2. `Entramos em contato para alinhar escopo e disciplinas.` [INSERIR DADO REAL: prazo; com dado → `Entramos em contato em até [X] dias úteis para alinhar escopo e disciplinas.`]
  3. `Você recebe a proposta com escopo, prazo e valor.`
- **Link:** `Prefere WhatsApp? Fale com a gente agora` (mensagem "Home")
- **Botão secundário:** `Baixar portfólio (PDF)` — **CONDICIONAL** [INSERIR DADO REAL: PDF liberado]
- **Formulário curto:** microcopy completa na seção 10.4 (C21b).

---

## 4. Serviços — hub (`/servicos/`)

### SEO — Serviços
- **Title:** Projetos de instalações prediais em BH | Intrépida
- **Meta description:** Hidrossanitário, elétrica, gás, HVAC, pressurização, piscina, saneamento, reúso pluvial e aquecimento solar, em 2D e BIM. Veja e solicite orçamento.
- **Palavra-chave principal:** projetos de instalações prediais BH
- **Secundárias:** projetos complementares de engenharia; projeto de instalações hidráulicas e elétricas; projetos de infraestrutura urbana; projetos para incorporadoras
- **Slug:** `/servicos/`

### SH-01 Breadcrumb
`Início › Serviços`

### SH-02 Hero interno (C04)
- **Eyebrow:** `Serviços`
- **H1:** `Projetos de instalações prediais e infraestrutura em Belo Horizonte`
- **Subtítulo:** `Nove disciplinas em 2D e BIM para incorporadoras, construtoras e arquitetos, com empreendimentos em seis estados.`
- **CTA primário:** `Solicitar orçamento` → `/contato/`
- **CTA secundário:** `Falar no WhatsApp` (mensagem "Hub de serviços")
- **Alt da imagem:** ver 13.2, imagem 5.

### SH-03 Índice rápido (chips)
`Instalações prediais` · `Infraestrutura urbana` · `Eficiência e sustentabilidade`
(`aria-label` do grupo de chips: `Ir para o grupo de serviços`)

### SH-04 Grupo 1 (C07)
- **H2:** `Instalações prediais`
- **Intro:** `Os sistemas que fazem o edifício funcionar, do subsolo à cobertura.`

| H3 | Descrição (2 linhas) | Link |
|---|---|---|
| `Projeto hidrossanitário` | `Água fria e quente, esgoto, ventilação, águas pluviais e medição individualizada por unidade, nos padrões da concessionária de saneamento.` | `Saiba mais →` |
| `Elétrica e Sistemas` | `Entrada de energia, medição, quadros, iluminação, tomadas e sistemas prediais, calculados para a aprovação na distribuidora.` | `Saiba mais →` |
| `Projeto de gás` | `Rede interna de gás natural ou GLP, medição e ventilação dos ambientes, para ligar o gás com segurança.` | `Saiba mais →` |
| `Climatização (HVAC)` | `Ar-condicionado, ventilação e exaustão mecânica, com espaço para equipamentos e dutos resolvido no projeto.` | `Saiba mais →` |
| `Pressurização de escadas` | `Sistema que mantém a escada de emergência livre de fumaça, conforme a norma e o Corpo de Bombeiros.` | `Saiba mais →` |
| `Projeto de piscina` | `Filtragem, recirculação, casa de máquinas e aquecimento para piscinas de condomínios e residências.` | `Saiba mais →` |

### SH-05 Grupo 2 (C07, card largo)
- **H2:** `Infraestrutura urbana`
- **Intro:** `Redes que ligam o empreendimento ao sistema público.`
- **Card — H3:** `Infraestrutura de saneamento`
- **Texto do card:** `Redes de distribuição de água, coleta de esgoto e drenagem pluvial para loteamentos, condomínios e conjuntos com vários blocos. Projetos nos padrões da concessionária e da prefeitura, sob a direção técnica de um engenheiro civil sanitarista.`
- **Link:** `Conheça o projeto de infraestrutura →`
- **Alt da imagem:** `Blocos residenciais e estacionamento do Parque Lagoa dos Príncipes, da MRV, em Lagoa Santa/MG`
  > Sugestão ao designer: a foto do Bosque dos Ipês em obra (vista aérea com arruamento e lotes) comunica "infraestrutura" melhor que a do Parque Lagoa dos Príncipes (vista ao nível do chão). Se trocar, alt: `Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS`.

### SH-06 Grupo 3 (C07)
- **H2:** `Eficiência e sustentabilidade`
- **Intro:** `Menos água potável e menos energia gastas pelo empreendimento.`

| H3 | Descrição | Link |
|---|---|---|
| `Reúso de água pluvial` | `Captação da água de chuva para descargas, irrigação e lavagem, com rede separada da água potável.` | `Saiba mais →` |
| `Aquecimento solar` | `Coletores, reservatórios térmicos e rede de água quente dimensionados pelo consumo, individuais ou coletivos.` | `Saiba mais →` |

### SH-07 Faixa BIM (C18)
- **H2:** `Todas as disciplinas em BIM, compatibilizadas`
- **Texto:** `Cada sistema é modelado em 3D e cruzado com a arquitetura, a estrutura e as demais instalações. Os conflitos são resolvidos no modelo, antes de chegar à obra.`
- **CTA:** `Conheça nosso processo BIM →` (`/bim-e-compatibilizacao/`)

### SH-08 "Não sabe quais projetos precisa?" (C09)
- **H2:** `Não sabe quais projetos o seu empreendimento precisa?`
- **Texto:** `Normal. A lista muda com o tipo de empreendimento, a cidade e as exigências de cada concessionária. Envie o projeto de arquitetura e indicamos as disciplinas necessárias e a melhor fase para contratar cada uma.`
- **Lista curta (opcional):**
  - `Arquiteto: um parceiro para os complementares, compatibilizados com o seu projeto.`
  - `Dono de obra: orientação em linguagem clara, antes de gastar com a disciplina errada.`
- **CTA:** `Enviar a arquitetura para indicação das disciplinas` → `/contato/?servico=nao-sei`

### SH-09 Como trabalhamos (C10)
Mesmo conteúdo da Home H-09 (H2 `Como trabalhamos` + 5 etapas + nota de prazo condicional).

### SH-10 Logos (C06, 12)
- **H2:** `Quem já contratou nossos projetos`
- **Link:** `Ver todos os clientes e projetos →`

### SH-11 CTA final (C13, só botões)
- **H2:** `Vamos orçar os projetos do seu empreendimento?`
- **Texto:** `Conte o que você precisa. Se ainda não souber todas as disciplinas, a gente ajuda a definir.`
- **Botões:** `Solicitar orçamento` · `Falar no WhatsApp`

---

## 5. Páginas de serviço (`/servicos/[disciplina]/`)

### 5.0 Partes fixas do modelo (iguais nas 9 páginas)
- **SV-01 Breadcrumb:** `Início › Serviços › [Nome da página]` · mobile `‹ Serviços`
- **SV-02 CTAs:** primário `Solicitar orçamento de [nome em minúsculas]` → `/contato/?servico=[valor]` · secundário `Falar no WhatsApp` (mensagem "Página de serviço", 2.6)
- **SV-05 CTA secundário:** `Fale com o engenheiro` → WhatsApp (mesma mensagem da página)
- **SV-06 link:** `Como usamos BIM →` (`/bim-e-compatibilizacao/`)
- **SV-07 Projetos com esta disciplina — CONDICIONAL:** só com ≥ 2 empreendimentos com a disciplina confirmada [INSERIR DADO REAL: disciplinas por projeto]. H2 `Empreendimentos com projeto [nome]` · link `Ver todos →` (`/projetos/?disciplina=[valor]`). **Sem dado (situação atual):** a seção vira a faixa de logos C06 com H2 `Quem já contratou nossos projetos` e link `Ver clientes e projetos →`.
- **SV-09 Outros serviços:** H2 conforme a página · lista das outras disciplinas do grupo (rótulos de 1.4) · link `Ver todos os serviços →`
- **SV-10 CTA final (C13 + C21b):** H2 `Orçamento de projeto [nome]` · os 3 itens "o que acontece depois" da Home H-13 · link `Prefere WhatsApp? Fale com a gente agora` · formulário curto com o campo oculto `servico=[valor]` (microcopy em 10.4)
- **Entregáveis (SV-03), normas (SV-05) e respostas técnicas das FAQs estão marcados [VALIDAR COM O RT].** São o escopo típico de cada disciplina e as normas de referência; o responsável técnico corta o que a Intrépida não entrega. A linha `ART do projeto` vale para todas as páginas (a ART é obrigatória por lei para projetos de engenharia).
- **Normas:** citar só número e assunto, sem ano de edição, para não desatualizar.

---

### 5.1 Projeto hidrossanitário (`/servicos/projeto-hidrossanitario/`)

**SEO**
- **Title:** Projeto hidrossanitário em BH | Intrépida Engenharia
- **Meta description:** Projeto hidrossanitário para incorporadoras: água fria e quente, esgoto, pluviais e medição individualizada, em 2D ou BIM. Solicite orçamento.
- **Palavra-chave principal:** projeto hidrossanitário
- **Secundárias:** projeto hidrossanitário BH; projeto de instalações hidráulicas prediais; medição individualizada de água; projeto hidrossanitário em BIM
- **Slug:** `/servicos/projeto-hidrossanitario/` · `?servico=hidrossanitario`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto hidrossanitário para incorporadoras e construtoras`
- Subtítulo: `Água fria e quente, esgoto, ventilação, águas pluviais e medição individualizada, dimensionados e compatibilizados para a análise da concessionária e para a obra.`
- CTA: `Solicitar orçamento de projeto hidrossanitário`
- Alt da imagem: ver 13.2, imagem 1.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `O projeto completo dos sistemas hidráulicos e sanitários do edifício:`
- `Água fria e água quente: alimentação, reservatórios, barrilete, prumadas e ramais`
- `Medição individualizada de água por unidade`
- `Esgoto sanitário e ventilação`
- `Águas pluviais: calhas, condutores e destinação`
- `Sistemas de recalque e pressurização de água, quando necessários`
- `Memorial descritivo e de cálculo, plantas, cortes, isométricos e detalhes`
- `Lista de materiais e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Indispensável para construir e para pedir as ligações de água e esgoto. Contrate junto com a arquitetura: shafts, reservatórios e casa de bombas mudam área e fachada.`
- `Loteamento e condomínio` — `Casas e áreas comuns precisam de projeto próprio, integrado às redes de infraestrutura do condomínio. Contrate junto com o projeto das redes.`
- `Comercial e residência` — `Lojas, clínicas e casas também precisam de projeto, principalmente com água quente, piscina ou reúso. Quanto antes, menos parede quebrada na obra.`

**SV-05 Normas e aprovações (C18)** [VALIDAR COM O RT]
- H2: `Normas e aprovações`
- Texto: `O projeto segue as normas da ABNT e os padrões da concessionária de saneamento do município, que analisa as ligações de água e esgoto e a medição individualizada.`
- Normas:
  - `ABNT NBR 5626 — sistemas prediais de água fria e água quente`
  - `ABNT NBR 8160 — sistemas prediais de esgoto sanitário`
  - `ABNT NBR 10844 — instalações prediais de águas pluviais`
  - `Lei federal 13.312/2016 — medição individualizada de água em novas edificações em condomínio`
- Órgãos: `Companhia de saneamento do município (em Minas Gerais, a COPASA, na maior parte das cidades)`
  [INSERIR DADO REAL: concessionárias em que a Intrépida já aprovou projetos. Com dado, acrescentar a linha `Já aprovamos projetos em: [lista]`.]
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM (C09 + C11)**
- H2: `Projeto hidrossanitário em BIM`
- Texto: `No modelo 3D, cada prumada, ramal e caixa é posicionado junto com a estrutura e as outras disciplinas. Os conflitos aparecem antes da obra, e os quantitativos saem do próprio modelo.`
- Imagens: 13.2, imagens 1 e 4.

**SV-07** — ver 5.0 (H2 condicional `Empreendimentos com projeto hidrossanitário`).

**SV-08 FAQ (C12)**
- H2: `Perguntas sobre projeto hidrossanitário`
1. **O que é um projeto hidrossanitário e quando ele é necessário?**
   `É o projeto que define como a água chega a cada ponto de uso e como o esgoto e a água de chuva saem do edifício. Ele é necessário para executar a obra com segurança e para pedir as ligações de água e esgoto à concessionária.`
2. **O que é medição individualizada de água?** [VALIDAR COM O RT]
   `É um hidrômetro por unidade, para que cada morador pague o próprio consumo. Em novas edificações em condomínio, a medição individualizada é exigida pela Lei 13.312/2016 e precisa estar prevista no projeto.`
3. **Quanto tempo leva o projeto?**
   `Depende do número de unidades, dos pavimentos e da fase em que está a arquitetura. O prazo de cada etapa vem descrito na proposta.`
4. **O que preciso enviar para o orçamento?**
   `A arquitetura (plantas, cortes e implantação) em DWG, PDF ou RVT, o número de unidades e de pavimentos e, se já tiver, a estrutura e a carta de viabilidade da concessionária.`
5. **Vocês acompanham a aprovação na concessionária?**
   Fallback: `O projeto é preparado nos padrões exigidos pela concessionária. Como funcionam o protocolo e o acompanhamento da análise no seu caso fica definido na proposta.`
   [INSERIR DADO REAL: se a Intrépida protocola e acompanha a aprovação, trocar por: `Sim. Protocolamos o projeto e acompanhamos a análise até a aprovação.`]

**SV-09** — H2: `Outros projetos de instalações prediais` (Elétrica e Sistemas · Gás · Climatização (HVAC) · Pressurização de escadas · Piscina)
**SV-10** — H2: `Orçamento de projeto hidrossanitário`

---

### 5.2 Elétrica e Sistemas (`/servicos/projeto-eletrico/`)

**SEO**
- **Title:** Projeto elétrico e de sistemas em BH | Intrépida
- **Meta description:** Projeto elétrico para edifícios: entrada de energia, medição, quadros, iluminação e sistemas prediais, em 2D ou BIM, para incorporadoras. Peça orçamento.
- **Palavra-chave principal:** projeto elétrico predial
- **Secundárias:** projeto elétrico BH; projeto de entrada de energia; projeto elétrico para incorporadoras; projeto elétrico em BIM
- **Slug:** `/servicos/projeto-eletrico/` · `?servico=eletrica`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto elétrico e de sistemas para edifícios residenciais e comerciais`
- Subtítulo: `Da entrada de energia à última tomada: medição, quadros, iluminação e sistemas prediais, calculados para a aprovação na distribuidora de energia.`
- CTA: `Solicitar orçamento de projeto elétrico`
- Alt da imagem: ver 13.2, imagem 7.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `Do ponto de ligação da distribuidora até cada circuito das unidades e das áreas comuns:`
- `Entrada de energia e padrão de medição, com agrupamento de medidores`
- `Cálculo de demanda e dimensionamento de alimentadores`
- `Quadros de distribuição com diagramas unifilares`
- `Iluminação e tomadas das unidades e das áreas comuns`
- `Aterramento`
- `Sistemas prediais` [INSERIR DADO REAL: quais sistemas a Intrépida projeta, ex. telefonia e dados, interfone, CFTV, antena coletiva, SPDA. Listar um por linha.]
- `Memorial descritivo e de cálculo, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Exigido para a ligação de energia pela distribuidora. Define a área do quadro de medidores e dos shafts, por isso deve começar junto com a arquitetura.`
- `Loteamento e condomínio` — `Projeto das casas e das áreas comuns, coordenado com a infraestrutura do condomínio.`
- `Comercial e residência` — `Lojas, salas e clínicas têm cargas específicas, como equipamentos e ar-condicionado. O projeto evita disjuntor desarmando e reforma depois da inauguração.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e aprovações`
- Texto: `A distribuidora de energia analisa a entrada, a medição e a demanda do empreendimento conforme as normas técnicas dela. O restante da instalação segue as normas da ABNT.`
- Normas:
  - `ABNT NBR 5410 — instalações elétricas de baixa tensão`
  - `Normas de fornecimento da distribuidora de energia (em Minas Gerais, as normas da CEMIG)`
  - [INSERIR DADO REAL: se SPDA estiver no escopo → `ABNT NBR 5419 — proteção contra descargas atmosféricas`; se cabeamento estruturado estiver no escopo → `ABNT NBR 14565 — cabeamento estruturado`]
- Órgãos: `Distribuidora de energia (em Minas Gerais, a CEMIG) e concessionárias de telecomunicações`
  [INSERIR DADO REAL: concessionárias em que já aprovaram projetos.]
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Projeto elétrico em BIM`
- Texto: `Quadros, eletrocalhas e eletrodutos entram no modelo 3D junto com a estrutura, a hidráulica e o forro. Passagens e espaços técnicos ficam definidos antes da obra.`
- Imagem: 13.2, imagem 7.

**SV-08 FAQ**
- H2: `Perguntas sobre projeto elétrico`
1. **O que é o projeto elétrico e de sistemas?**
   `É o projeto que define como a energia chega ao edifício e se distribui até cada ponto de luz e tomada. Quando contratado, inclui também os sistemas prediais. A distribuidora exige o projeto para fazer a ligação.`
2. **O que a distribuidora de energia analisa?**
   `A entrada de energia, o padrão de medição e a demanda calculada do empreendimento, conforme as normas dela. Um erro nessa parte atrasa a ligação.`
3. **Quais sistemas entram em "Sistemas"?**
   Fallback: `O escopo de sistemas prediais é definido na proposta, conforme o empreendimento.` [INSERIR DADO REAL: lista de sistemas → `Projetamos [lista]. O escopo de cada empreendimento fica definido na proposta.`]
4. **O que preciso enviar para o orçamento?**
   `A arquitetura em DWG, PDF ou RVT, o número de unidades e a lista de equipamentos especiais, se houver: elevadores, bombas, ar-condicionado, carregadores de veículos.`

**SV-09** — H2: `Outros projetos de instalações prediais` (Hidrossanitário · Gás · Climatização (HVAC) · Pressurização de escadas · Piscina)
**SV-10** — H2: `Orçamento de projeto elétrico e de sistemas`

---

### 5.3 Projeto de gás (`/servicos/projeto-de-gas/`)

**SEO**
- **Title:** Projeto de gás natural e GLP em BH | Intrépida
- **Meta description:** Projeto de gás para edifícios e condomínios: rede interna de gás natural ou GLP, medição e ventilação dos ambientes, em 2D ou BIM. Solicite orçamento.
- **Palavra-chave principal:** projeto de gás
- **Secundárias:** projeto de gás natural BH; projeto de gás GLP para condomínio; projeto de rede de gás predial; projeto de gás para incorporadoras
- **Slug:** `/servicos/projeto-de-gas/` · `?servico=gas`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto de gás para edifícios residenciais e comerciais`
- Subtítulo: `Rede interna de gás natural ou GLP, com prumadas, medição e ventilação dos ambientes calculadas para a aprovação na distribuidora e o uso seguro.`
- CTA: `Solicitar orçamento de projeto de gás`
- Alt da imagem: ver 13.2, imagem 8 (ou 6) — **[A CONFIRMAR: disciplina da imagem]**.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `Do ponto de entrega do gás até cada aparelho:`
- `Rede de distribuição interna: prumadas e ramais`
- `Medição individual e abrigo de medidores`
- `Central de GLP, quando não há gás canalizado na rua`
- `Dimensionamento pela potência dos aparelhos previstos`
- `Verificação da ventilação dos ambientes com aparelhos a gás`
- `Memorial, plantas, isométricos, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Necessário para ligar o gás canalizado ou instalar a central de GLP. Define abrigos, prumadas e shafts ventilados, que precisam estar na arquitetura.`
- `Loteamento e condomínio` — `Ramais das casas e, quando houver, a rede interna do condomínio até o ponto de entrega da distribuidora.`
- `Comercial e residência` — `Restaurantes, cozinhas profissionais e casas com aquecedor ou fogão a gás precisam de projeto para instalar com segurança.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e aprovações`
- Texto: `A distribuidora de gás canalizado analisa o projeto antes da ligação. Centrais de GLP seguem também as regras do Corpo de Bombeiros do estado.`
- Normas:
  - `ABNT NBR 15526 — redes de distribuição interna para gases combustíveis`
  - `ABNT NBR 13103 — instalação de aparelhos a gás e adequação dos ambientes`
  - `ABNT NBR 13523 — central de gás liquefeito de petróleo (GLP)`
- Órgãos: `Distribuidora de gás canalizado (em Minas Gerais, a Gasmig) e Corpo de Bombeiros, no caso de centrais de GLP`
  [INSERIR DADO REAL: distribuidoras em que já aprovaram projetos.]
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Projeto de gás em BIM`
- Texto: `Prumadas e ramais de gás modelados com as demais disciplinas. Os afastamentos de segurança em relação à elétrica e a outras tubulações ficam visíveis e conferidos no modelo.`

**SV-08 FAQ**
- H2: `Perguntas sobre projeto de gás`
1. **O que é um projeto de gás e quando ele é necessário?**
   `É o projeto da rede que leva o gás do medidor ou da central até cada aparelho. A distribuidora exige o projeto para ligar o gás canalizado, e ele é a base de uma instalação segura.`
2. **Gás natural ou GLP: qual escolher?** [VALIDAR COM O RT]
   `Depende de haver rede de gás canalizado na rua do empreendimento. Sem rede, a solução usual é a central de GLP. O projeto pode deixar a instalação pronta para uma conversão futura.`
3. **Por que a ventilação dos ambientes entra no projeto?**
   `Aparelhos a gás precisam de ar para queimar com segurança e de saída para os gases da combustão. A norma define aberturas mínimas, e isso afeta a arquitetura.`
4. **O que preciso enviar para o orçamento?**
   `A arquitetura em DWG, PDF ou RVT, o número de unidades e os aparelhos previstos (fogão, aquecedor, churrasqueira a gás), além da informação de se há gás canalizado na rua.`

**SV-09** — H2: `Outros projetos de instalações prediais` (Hidrossanitário · Elétrica e Sistemas · Climatização (HVAC) · Pressurização de escadas · Piscina)
**SV-10** — H2: `Orçamento de projeto de gás`

---

### 5.4 Climatização HVAC (`/servicos/climatizacao-hvac/`)

**SEO**
- **Title:** Projeto de climatização HVAC em BH | Intrépida
- **Meta description:** Projeto de ar-condicionado, ventilação e exaustão para edifícios residenciais e comerciais, com carga térmica calculada, em 2D ou BIM. Peça orçamento.
- **Palavra-chave principal:** projeto de climatização
- **Secundárias:** projeto HVAC BH; projeto de ar-condicionado predial; projeto de ventilação e exaustão; projeto de exaustão de garagem
- **Slug:** `/servicos/climatizacao-hvac/` · `?servico=hvac`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto de climatização (HVAC) para edifícios residenciais e comerciais`
- Subtítulo: `Ar-condicionado, ventilação e exaustão dimensionados pela carga térmica de cada ambiente, com o espaço de equipamentos e dutos resolvido antes da obra.`
- CTA: `Solicitar orçamento de projeto de climatização`
- Imagem: [INSERIR DADO REAL: modelo BIM de HVAC do cliente]. Sem modelo → ilustração GERADA de equipamento/duto, com legenda `Imagem ilustrativa`. Alt da ilustração: `Ilustração de dutos e equipamento de ar-condicionado (imagem ilustrativa)`.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `Conforto térmico e qualidade do ar, com o espaço técnico previsto:`
- `Cálculo de carga térmica por ambiente`
- `Definição do sistema: split, multi-split, VRF ou central`
- `Ventilação e renovação de ar`
- `Exaustão mecânica de banheiros sem janela, cozinhas e garagens`
- `Infraestrutura para ar-condicionado nas unidades: drenos, pontos de força e posição das condensadoras`
- `Memorial, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Prever drenos, pontos de força e o lugar das condensadoras evita fachada improvisada e reforma depois da entrega. Contrate junto com a arquitetura.`
- `Áreas comuns de condomínios` — `Salão de festas, academia e espaços de convivência, com conforto e renovação de ar adequados ao uso.`
- `Comercial e corporativo` — `Lojas, escritórios, clínicas e restaurantes, em que o conforto e a renovação do ar fazem parte do funcionamento.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e integração com outras disciplinas`
- Texto: `Climatização não passa por concessionária, mas pesa no projeto elétrico: a carga dos equipamentos entra no cálculo de demanda do edifício. Por isso as duas disciplinas andam juntas.`
- Normas:
  - `ABNT NBR 16401 — instalações de ar-condicionado: sistemas centrais e unitários`
  - `ABNT NBR 14518 — sistemas de ventilação para cozinhas industriais`
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Climatização em BIM`
- Texto: `Dutos ocupam o forro e cruzam com todas as outras disciplinas. No modelo, a altura do forro e as passagens em vigas ficam definidas antes da obra.`

**SV-08 FAQ**
- H2: `Perguntas sobre projeto de climatização`
1. **O que significa HVAC?**
   `É a sigla em inglês para aquecimento, ventilação e ar-condicionado. O projeto define os equipamentos, a ventilação e a exaustão de cada ambiente.`
2. **Preciso de projeto só para instalar aparelhos split?**
   `Em um edifício, sim. O projeto define a posição das condensadoras, os drenos e a carga elétrica de todas as unidades, e evita improviso na fachada e nos quadros.`
3. **Garagem em subsolo precisa de exaustão mecânica?** [VALIDAR COM O RT]
   `Depende da ventilação natural disponível e da legislação local. O projeto verifica a necessidade e dimensiona o sistema quando ele for exigido.`
4. **O que preciso enviar para o orçamento?**
   `A arquitetura em DWG, PDF ou RVT, o uso de cada ambiente e o padrão de climatização desejado (unidades preparadas para split, sistema central, só áreas comuns).`

**SV-09** — H2: `Outros projetos de instalações prediais` (Hidrossanitário · Elétrica e Sistemas · Gás · Pressurização de escadas · Piscina)
**SV-10** — H2: `Orçamento de projeto de climatização`

---

### 5.5 Pressurização de escadas (`/servicos/pressurizacao-de-escadas/`)

**SEO**
- **Title:** Projeto de pressurização de escadas | Intrépida
- **Meta description:** Projeto de pressurização de escadas de emergência: cálculo de vazão, ventiladores e dutos, conforme a NBR 14880 e o Corpo de Bombeiros. Peça orçamento.
- **Palavra-chave principal:** projeto de pressurização de escadas
- **Secundárias:** pressurização de escada de emergência; escada pressurizada; NBR 14880; controle de fumaça em escadas
- **Slug:** `/servicos/pressurizacao-de-escadas/` · `?servico=pressurizacao`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto de pressurização de escadas de emergência`
- Subtítulo: `Sistema que mantém a escada livre de fumaça durante um incêndio, dimensionado conforme a norma e as exigências do Corpo de Bombeiros.`
- CTA: `Solicitar orçamento de pressurização de escadas`
- Imagem: [INSERIR DADO REAL: modelo BIM do cliente]. Sem modelo → ilustração GERADA de ventilador/duto, com legenda `Imagem ilustrativa`. Alt: `Ilustração de ventilador e dutos de um sistema de pressurização (imagem ilustrativa)`.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `O sistema completo, da tomada de ar à escada:`
- `Cálculo de vazão e pressão da escada`
- `Seleção do ventilador e do grupo de pressurização`
- `Dutos, grelhas e dampers`
- `Tomada de ar externo protegida contra fumaça`
- `Lógica de acionamento integrada ao sistema de alarme de incêndio`
- `Interface com a elétrica: alimentação de emergência do ventilador`
- `Memorial, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Em edifícios mais altos, a escada pressurizada costuma ser exigida pela regulamentação do Corpo de Bombeiros do estado.`
- `Comercial e uso misto` — `A exigência depende da altura e da ocupação do edifício. O projeto confirma o enquadramento antes de dimensionar.`
- `Fase certa` — `No início da arquitetura. A casa do ventilador e o trajeto dos dutos ocupam área e precisam de espaço em todos os pavimentos.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e aprovações`
- Texto: `A pressurização faz parte do processo de segurança contra incêndio do edifício, analisado pelo Corpo de Bombeiros do estado.`
- Normas:
  - `ABNT NBR 14880 — saídas de emergência em edifícios: escadas de segurança, controle de fumaça por pressurização`
  - `Instruções técnicas do Corpo de Bombeiros do estado`
- Órgãos: `Corpo de Bombeiros Militar do estado (em Minas Gerais, o CBMMG)`
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Pressurização em BIM`
- Texto: `Os dutos de pressurização são grandes e atravessam vários pavimentos. No modelo, o trajeto é compatibilizado com a estrutura e as demais instalações antes da obra.`

**SV-08 FAQ**
- H2: `Perguntas sobre pressurização de escadas`
1. **O que é pressurização de escadas?**
   `É um sistema de ventiladores que injeta ar na escada de emergência e mantém nela uma pressão maior que a dos andares. Assim a fumaça não entra, e a escada continua segura para a saída das pessoas.`
2. **Meu edifício precisa de escada pressurizada?**
   `Depende da altura, da ocupação e da regulamentação do Corpo de Bombeiros do estado. Envie a arquitetura e verificamos a exigência.`
3. **Quem aprova o sistema?**
   `O Corpo de Bombeiros, dentro do processo de segurança contra incêndio do edifício.`
4. **O que preciso enviar para o orçamento?**
   `A arquitetura com plantas de todos os pavimentos e cortes, em DWG, PDF ou RVT, e a classificação de ocupação do edifício, se já houver.`

**SV-09** — H2: `Outros projetos de instalações prediais` (Hidrossanitário · Elétrica e Sistemas · Gás · Climatização (HVAC) · Piscina)
**SV-10** — H2: `Orçamento de projeto de pressurização`

---

### 5.6 Projeto de piscina (`/servicos/projeto-de-piscina/`)

**SEO**
- **Title:** Projeto de piscina para condomínios e casas | Intrépida
- **Meta description:** Projeto hidráulico de piscina: filtragem, recirculação, casa de máquinas e aquecimento, para condomínios e residências. Solicite orçamento.
- **Palavra-chave principal:** projeto hidráulico de piscina
- **Secundárias:** projeto de piscina BH; projeto de casa de máquinas de piscina; projeto de piscina para condomínio; aquecimento de piscina
- **Slug:** `/servicos/projeto-de-piscina/` · `?servico=piscina`

**SV-02 Hero**
- Eyebrow: `Instalações prediais`
- **H1:** `Projeto de piscina: filtragem, recirculação e aquecimento`
- Subtítulo: `Casa de máquinas, bombas, filtros e tubulações dimensionados para água limpa, uso seguro e manutenção simples, em condomínios e residências.`
- CTA: `Solicitar orçamento de projeto de piscina`
- Imagem: 13.2, imagem 2 — **[A CONFIRMAR: o modelo é de piscina?]**. Se não for, ilustração GERADA sinalizada. Alt da ilustração: `Ilustração de casa de máquinas de piscina com bomba e filtro (imagem ilustrativa)`.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `O sistema hidráulico completo da piscina:`
- `Dimensionamento do filtro e do conjunto motobomba`
- `Tubulações de sucção, retorno e dreno`
- `Dispositivos de sucção com proteção contra aprisionamento`
- `Layout da casa de máquinas`
- `Aquecimento: solar, bomba de calor ou trocador de calor`
- `Interface com os projetos elétrico e hidrossanitário`
- `Memorial, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Piscinas das áreas de lazer, com uso intenso e manutenção pelo condomínio. Contrate junto com a arquitetura do lazer.`
- `Loteamento e clube` — `Piscinas de clubes e áreas comuns de condomínios horizontais.`
- `Residência` — `Casas com piscina, aquecimento e hidromassagem.` [INSERIR DADO REAL: confirmar se o público de residências particulares interessa. Se não, trocar este card por `Comercial`: `Hotéis, academias e clubes.`]

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e segurança`
- Texto: `Piscina não passa por concessionária, mas segue norma própria, com regras de circulação da água e de segurança nos pontos de sucção.`
- Normas: `ABNT NBR 10339 — piscina: projeto, execução e manutenção`
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Piscina em BIM`
- Texto: `Bombas, filtros e tubulações modelados na casa de máquinas, com espaço de acesso para manutenção conferido no modelo.`

**SV-08 FAQ**
- H2: `Perguntas sobre projeto de piscina`
1. **Por que a piscina precisa de projeto próprio?**
   `Porque a água precisa passar pelo filtro no tempo certo para continuar limpa, e os pontos de sucção precisam de proteção para evitar acidentes. Sem projeto, é comum bomba mal dimensionada, água turva e manutenção cara.`
2. **Dá para aquecer a piscina com energia solar?**
   `Sim. O aquecimento solar pode ser ligado ao sistema de filtragem. O projeto compara as opções de aquecimento e dimensiona os coletores.`
3. **Quando devo contratar?**
   `Junto com a arquitetura da área de lazer. A casa de máquinas precisa de espaço, acesso e ventilação.`
4. **O que preciso enviar para o orçamento?**
   `A planta da área de lazer com as dimensões da piscina, em DWG, PDF ou RVT, e se haverá aquecimento, hidromassagem ou cascata.`

**SV-09** — H2: `Outros projetos de instalações prediais` (Hidrossanitário · Elétrica e Sistemas · Gás · Climatização (HVAC) · Pressurização de escadas)
**SV-10** — H2: `Orçamento de projeto de piscina`

---

### 5.7 Infraestrutura de saneamento (`/servicos/infraestrutura-de-saneamento/`)

**SEO**
- **Title:** Projeto de infraestrutura de saneamento | Intrépida
- **Meta description:** Projetos de redes de água, esgoto e drenagem pluvial para loteamentos e condomínios, nos padrões da concessionária e da prefeitura. Peça orçamento.
- **Palavra-chave principal:** projeto de infraestrutura de saneamento
- **Secundárias:** projeto de rede de água e esgoto; projeto de drenagem pluvial para loteamento; projeto de saneamento para loteamento; projeto de infraestrutura urbana BH
- **Slug:** `/servicos/infraestrutura-de-saneamento/` · `?servico=saneamento`

**SV-02 Hero**
- Eyebrow: `Infraestrutura urbana`
- **H1:** `Projeto de infraestrutura de saneamento para loteamentos e condomínios`
- Subtítulo: `Redes de água, esgoto e drenagem pluvial nos padrões da concessionária e da prefeitura, sob a direção técnica de um engenheiro civil sanitarista.`
- CTA: `Solicitar orçamento de infraestrutura de saneamento`
- Alt da imagem (foto sugerida): `Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS`

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `As redes que ligam o empreendimento ao sistema público:`
- `Rede de distribuição de água e ligações prediais`
- `Rede coletora de esgoto e ligações prediais`
- `Drenagem pluvial: sarjetas, bocas de lobo, galerias e lançamento`
- `Interligação com as redes públicas existentes`
- `Elevatórias e reservatórios, quando necessários`
- `Plantas, perfis longitudinais, detalhes, memorial e quantitativos`
- `ART do projeto`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Loteamento` — `As redes de água, esgoto e drenagem fazem parte da aprovação do loteamento na prefeitura e na concessionária. Contrate logo após o projeto urbanístico.`
- `Condomínios e conjuntos com vários blocos` — `As redes internas levam água, esgoto e chuva de cada bloco até o ponto de ligação com a rede pública.`
- `Extensão da rede pública` — `Quando a rede da rua não atende o empreendimento, a concessionária pode exigir projeto de extensão ou reforço. Melhor saber disso na viabilidade.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e aprovações`
- Texto: `A concessionária de saneamento analisa as redes de água e esgoto. A drenagem costuma ser analisada pela prefeitura, com diretrizes próprias de cada município.`
- Normas:
  - `ABNT NBR 12218 — projeto de rede de distribuição de água para abastecimento público`
  - `ABNT NBR 9649 — projeto de redes coletoras de esgoto sanitário`
  - `Diretrizes e cadernos de encargos da concessionária e da prefeitura`
- Órgãos: `Concessionária de saneamento (em Minas Gerais, a COPASA, na maior parte das cidades) e prefeitura municipal`
  [INSERIR DADO REAL: concessionárias e prefeituras em que já aprovaram projetos.]
- CTA: `Fale com o engenheiro`

**SV-06 Projeto e compatibilização (variação do C09)**
- H2: `Redes compatibilizadas com o empreendimento`
- Texto: `As redes são traçadas com a topografia, o projeto urbanístico e as instalações das edificações. Cotas, interferências e sequência de obra ficam resolvidas no projeto.`
  [INSERIR DADO REAL: se a Intrépida modela infraestrutura em BIM, trocar o H2 por `Infraestrutura em BIM` e acrescentar: `As redes também podem ser entregues em modelo BIM.`]

**SV-08 FAQ**
- H2: `Perguntas sobre infraestrutura de saneamento`
1. **O que é um projeto de infraestrutura de saneamento?**
   `É o projeto das redes que abastecem de água, coletam o esgoto e escoam a chuva de um loteamento ou conjunto de edifícios, até a ligação com o sistema público.`
2. **Quem aprova o projeto?**
   `A concessionária de saneamento analisa as redes de água e esgoto. A drenagem costuma ser analisada pela prefeitura. Cada município tem as suas diretrizes.`
3. **O que é a viabilidade técnica da concessionária?** [VALIDAR COM O RT]
   `É a resposta da concessionária sobre a capacidade de atender o empreendimento e as condições para a ligação. Ela orienta o projeto e deve ser pedida no início.`
4. **Por que contratar um engenheiro sanitarista para as redes?**
   `Porque saneamento é a especialidade da engenharia sanitária. O diretor técnico da Intrépida, Carlos Alberto Grope, é engenheiro civil sanitarista.`
5. **O que preciso enviar para o orçamento?**
   `O levantamento topográfico, o projeto urbanístico ou a implantação, o número de lotes ou unidades e as diretrizes da concessionária e da prefeitura, se já tiver.`

**SV-09** — H2: `Outros serviços` (aqui o grupo tem 1 item; listar os 2 de Eficiência e sustentabilidade + Hidrossanitário)
**SV-10** — H2: `Orçamento de projeto de infraestrutura de saneamento`

---

### 5.8 Reúso de água pluvial (`/servicos/reuso-de-agua-pluvial/`)

**SEO**
- **Title:** Projeto de aproveitamento de água de chuva | Intrépida
- **Meta description:** Projeto de reúso de água pluvial: captação, filtragem, reservatório e rede não potável para descargas e irrigação, conforme a NBR 15527. Peça orçamento.
- **Palavra-chave principal:** projeto de aproveitamento de água de chuva
- **Secundárias:** projeto de reúso de água pluvial; reuso de água de chuva em condomínio; NBR 15527; captação de água de chuva predial
- **Slug:** `/servicos/reuso-de-agua-pluvial/` · `?servico=reuso-pluvial`

**SV-02 Hero**
- Eyebrow: `Eficiência e sustentabilidade`
- **H1:** `Projeto de aproveitamento de água de chuva (reúso pluvial)`
- Subtítulo: `Captação, filtragem, reservação e distribuição da água de chuva para descargas, irrigação e lavagem, com rede separada da água potável.`
- CTA: `Solicitar orçamento de reúso de água pluvial`
- Imagem: [INSERIR DADO REAL: modelo BIM do cliente]. Sem modelo → ilustração GERADA sinalizada. Alt: `Ilustração de sistema de captação de água de chuva com calha, filtro e reservatório (imagem ilustrativa)`.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `O sistema completo, do telhado ao ponto de uso:`
- `Estudo de chuva e de demanda não potável para dimensionar o reservatório`
- `Captação em coberturas, calhas e condutores`
- `Filtro e descarte das primeiras águas`
- `Reservatório, bombeamento e rede não potável`
- `Identificação e sinalização da rede não potável`
- `Integração com o projeto hidrossanitário`
- `Memorial, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Água de chuva nas descargas e na irrigação das áreas comuns diminui o consumo de água tratada do condomínio.`
- `Loteamento e condomínio` — `Em muitos municípios, a captação ou a retenção de água de chuva é exigência para aprovar o empreendimento. O projeto atende à regra local.`
- `Comercial e galpões` — `Prédios com grande área de cobertura têm muita água para captar e uso não potável alto.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e legislação`
- Texto: `O sistema segue as normas da ABNT e a legislação do município, que em muitos casos define volumes mínimos de captação ou de retenção.`
- Normas:
  - `ABNT NBR 15527 — aproveitamento de água de chuva de coberturas para fins não potáveis`
  - `ABNT NBR 16783 — uso de fontes alternativas de água não potável em edificações`
  - `ABNT NBR 5626 — separação entre água potável e não potável`
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Reúso pluvial em BIM`
- Texto: `No modelo, a rede não potável fica separada e identificada desde o reservatório até cada ponto de uso. Isso evita ligação cruzada com a água potável na obra.`

**SV-08 FAQ**
- H2: `Perguntas sobre aproveitamento de água de chuva`
1. **Qual é a diferença entre reúso e aproveitamento de água de chuva?**
   `Aproveitamento usa a água de chuva captada nas coberturas. Reúso, em sentido estrito, é tratar e usar de novo águas já utilizadas no edifício. Este serviço trata da água de chuva.`
   [INSERIR DADO REAL: se a Intrépida projeta reúso de águas cinzas, acrescentar: `Também projetamos reúso de águas cinzas.`]
2. **A água de chuva pode ser usada para beber?**
   `Não. O uso é não potável: descargas, irrigação e lavagem de pisos e veículos. Por isso a rede é separada e sinalizada.`
3. **Vale a pena no meu empreendimento?**
   `Depende das chuvas da cidade, da área de cobertura e do consumo não potável. O projeto calcula o volume aproveitável antes de você decidir.`
4. **O que preciso enviar para o orçamento?**
   `A arquitetura com a planta de cobertura e a implantação, em DWG, PDF ou RVT, o número de unidades e os usos previstos para a água.`

**SV-09** — H2: `Outros projetos de eficiência e sustentabilidade` (Aquecimento solar + Hidrossanitário)
**SV-10** — H2: `Orçamento de projeto de reúso de água pluvial`

---

### 5.9 Aquecimento solar (`/servicos/aquecimento-solar/`)

**SEO**
- **Title:** Projeto de aquecimento solar de água | Intrépida
- **Meta description:** Projeto de aquecimento solar para edifícios, casas e piscinas: coletores, reservatórios térmicos e rede de água quente, em 2D ou BIM. Solicite orçamento.
- **Palavra-chave principal:** projeto de aquecimento solar
- **Secundárias:** projeto de aquecimento solar para prédio; aquecimento solar coletivo; NBR 15569; projeto de água quente predial
- **Slug:** `/servicos/aquecimento-solar/` · `?servico=aquecimento-solar`

**SV-02 Hero**
- Eyebrow: `Eficiência e sustentabilidade`
- **H1:** `Projeto de aquecimento solar de água`
- Subtítulo: `Coletores, reservatórios térmicos, aquecimento auxiliar e rede de água quente dimensionados pelo consumo, em sistemas individuais ou coletivos.`
- CTA: `Solicitar orçamento de aquecimento solar`
- Imagem: 13.2, imagem 3 (ramais de água quente) + ilustração GERADA de coletores, sinalizada. Alt da ilustração: `Ilustração de coletores solares na cobertura de um edifício (imagem ilustrativa)`.

**SV-03 O que entregamos** [VALIDAR COM O RT]
- H2: `O que entregamos`
- Intro: `Do coletor ao chuveiro:`
- `Cálculo da demanda de água quente`
- `Dimensionamento da área de coletores e do volume dos reservatórios térmicos`
- `Aquecimento auxiliar elétrico ou a gás`
- `Posição dos coletores na cobertura: orientação, inclinação e sombreamento`
- `Rede de água quente e isolamento térmico`
- `Integração com os projetos hidrossanitário e de piscina`
- `Memorial, plantas, detalhes e quantitativos`
- `ART do projeto e, quando contratado, modelo BIM`

**SV-04 Para quem e quando contratar**
- H2: `Para quem é e quando contratar`
- `Residencial multifamiliar` — `Sistema coletivo ou individual por unidade. A escolha muda cobertura, shafts e medição, por isso deve ser feita cedo.`
- `Loteamento e casas em série` — `Sistemas individuais por casa, padronizados para a obra em série.`
- `Comercial e residência` — `Casas, hotéis, academias e clínicas com consumo alto de água quente.`

**SV-05 Normas e aprovações** [VALIDAR COM O RT]
- H2: `Normas e exigências`
- Texto: `O projeto segue as normas da ABNT e atende às exigências de aquecimento solar do seu programa habitacional ou contrato de financiamento, quando houver.`
- Normas:
  - `ABNT NBR 15569 — sistema de aquecimento solar de água em circuito direto: projeto e instalação`
  - `ABNT NBR 5626 — sistemas prediais de água fria e água quente`
- CTA: `Fale com o engenheiro`

**SV-06 Em BIM**
- H2: `Aquecimento solar em BIM`
- Texto: `Reservatórios e coletores pesam e ocupam a cobertura. No modelo, posição, estrutura e rede de água quente são compatibilizadas antes da obra.`
- Imagem: 13.2, imagem 3.

**SV-08 FAQ**
- H2: `Perguntas sobre aquecimento solar`
1. **Como funciona o aquecimento solar de água?**
   `Coletores na cobertura aquecem a água com a energia do sol, e reservatórios térmicos guardam a água quente. Em dias nublados, um sistema auxiliar elétrico ou a gás completa o aquecimento.`
2. **Individual ou coletivo: qual é melhor no meu prédio?**
   `Depende da área de cobertura, do número de unidades e de como o condomínio vai medir o consumo. O projeto compara as opções antes da decisão.`
3. **Dá para aquecer a piscina também?**
   `Sim, com coletores próprios ligados ao sistema de filtragem. Veja também o projeto de piscina.` (link para `/servicos/projeto-de-piscina/`)
4. **O que preciso enviar para o orçamento?**
   `A arquitetura com a planta de cobertura, em DWG, PDF ou RVT, o número de unidades e de banheiros por unidade e se haverá piscina aquecida.`

**SV-09** — H2: `Outros projetos de eficiência e sustentabilidade` (Reúso de água pluvial + Hidrossanitário + Piscina)
**SV-10** — H2: `Orçamento de projeto de aquecimento solar`

---

## 6. BIM e Compatibilização (`/bim-e-compatibilizacao/`)

### SEO — BIM
- **Title:** BIM e compatibilização de projetos | Intrépida
- **Meta description:** Projetos de instalações em BIM e compatibilização entre disciplinas: interferências resolvidas no modelo e quantitativos confiáveis. Veja modelos reais.
- **Palavra-chave principal:** compatibilização de projetos BIM
- **Secundárias:** projeto BIM de instalações; modelagem BIM hidrossanitário; projetos complementares em BIM; compatibilização de projetos BH
- **Slug:** `/bim-e-compatibilizacao/` · `?servico=compatibilizacao-bim`

### BM-01 Breadcrumb
`Início › BIM e compatibilização`

### BM-02 Hero interno (C04)
- **Eyebrow:** `Em todas as disciplinas`
- **H1:** `BIM e compatibilização de projetos de instalações`
- **Subtítulo:** `Instalações modeladas em 3D e cruzadas com a arquitetura e a estrutura: menos conflito na obra e quantitativos que saem do modelo.`
- **CTA primário:** `Solicitar orçamento` → `/contato/?servico=compatibilizacao-bim`
- **CTA secundário:** `Ver modelos reais ↓` (âncora para BM-05)
- **Alt da imagem:** ver 13.2, imagem 5.

### BM-03 Benefícios (4 cards)
- **H2:** `O que muda com o BIM`
| H3 | Texto |
|---|---|
| `Interferências resolvidas antes da obra` | `Tubulação contra viga, duto contra eletrocalha: o conflito aparece no modelo, quando corrigir custa uma revisão, e não uma demolição.` |
| `Quantitativos confiáveis` | `Tubos, conexões, cabos e equipamentos são contados a partir do modelo, o que dá uma base mais sólida ao orçamento da obra.` |
| `Execução com menos dúvida` | `Vistas 3D e detalhes mostram à equipe de campo como cada sistema deve ficar.` |
| `Informação para manutenção e gestão` | `O modelo reúne dados úteis para operar e manter o empreendimento depois da entrega.` |

### BM-04 Como fazemos a compatibilização (C10)
- **H2:** `Como fazemos a compatibilização`
- [INSERIR DADO REAL: confirmar etapas com o cliente. Texto segue a sugestão aprovada no wireframe.]
  1. `Recebimento dos modelos` — `Recebemos a arquitetura e a estrutura, em BIM ou em 2D, e definimos o padrão de entrega.`
  2. `Modelagem das instalações` — `Cada disciplina é modelada com as informações do cálculo.`
  3. `Detecção de conflitos` — `Cruzamos todas as disciplinas e listamos as interferências encontradas.`
  4. `Relatório e ajustes` — `Apresentamos os conflitos com as soluções propostas e ajustamos os projetos.`
  5. `Modelo final` — `Você recebe o modelo compatibilizado e as pranchas para a obra.`

### BM-05 Galeria de modelos (C11, 8 imagens)
- **H2:** `Modelos reais de projetos da Intrépida`
- **Intro:** `Recortes de modelos BIM desenvolvidos pela Intrépida. Clique para ampliar.`
- **Legendas e alt:** seção 13.2 (imagens 1 a 8).
- **Microcopy do lightbox:** `Fechar` · `Imagem anterior` · `Próxima imagem` · contador `Imagem 3 de 8`
- **Slot fase 2 (oculto):** `Explore um modelo em 3D` — só quando houver o visualizador.

### BM-06 Softwares e formatos de entrega (C15)
- **H2:** `Softwares e formatos de entrega`
- **Ficha (CONDICIONAL, cada linha só com dado):**
  - `Softwares:` [INSERIR DADO REAL: ex. Revit, AltoQi]
  - `Formatos de entrega:` [INSERIR DADO REAL: ex. RVT, IFC, DWG, PDF, NWC]
  - `Nível de detalhe:` [INSERIR DADO REAL]
  - `Padrão do cliente:` [INSERIR DADO REAL: confirmar se trabalham no template BIM do cliente → `Trabalhamos no template e no padrão BIM da sua empresa.`]
- **Fallback (publicável hoje, no lugar da ficha):** `Entregamos em BIM (modelo 3D) ou em 2D. Envie o padrão BIM da sua empresa com o pedido de orçamento: formato, nível de detalhe e template ficam definidos na proposta.`

### BM-07 2D x BIM — **decisão: entra**
**Por que entra:** responde à objeção "por que pagar por BIM?" (P1) e explica a diferença para quem não conhece (P3, P4) sem prometer número nenhum. Mostra também que a Intrépida faz os dois, o que é verdade e evita afastar quem ainda contrata em 2D. Reforça a palavra-chave "projeto 2D ou BIM" sem texto genérico. Se o RT discordar de algum item, o item sai; a seção continua de pé com 3 linhas por coluna.

- **H2:** `2D ou BIM: o que muda na prática`
| Projeto em 2D | Projeto em BIM |
|---|---|
| `Cada disciplina em pranchas separadas` | `Todas as disciplinas no mesmo modelo 3D` |
| `Conflitos entre sistemas aparecem na sobreposição das pranchas ou na obra` | `Conflitos detectados no modelo, antes da obra` |
| `Quantitativos levantados a partir dos desenhos` | `Quantitativos extraídos do modelo` |
| `Uma revisão precisa ser repetida em cada prancha` | `Pranchas geradas do modelo: mudou o modelo, mudam as vistas` |
| `Boa opção para empreendimentos simples ou processos 2D` | `Informação útil também para manutenção e gestão` |
- **Nota abaixo:** `Fazemos os dois. A escolha depende do empreendimento e do processo da sua empresa, e pode ser discutida no orçamento.`

### BM-08 Projetos (C08, 3 cards)
- **H2:** `Empreendimentos com projetos da Intrépida`
- Cards: Mirante São Lucas · Bosque dos Ipês · Residencial Pacífico (dados na seção 8).
- Link: `Ver todos os projetos →`
- Nota: não chamar de "projetos em BIM" até o cliente confirmar quais foram entregues em BIM [INSERIR DADO REAL].

### BM-09 FAQ BIM (C12)
- **H2:** `Perguntas sobre BIM e compatibilização`
1. **O que é BIM?**
   `É a sigla de Building Information Modeling, ou modelagem da informação da construção. Em vez de desenhos soltos, o projeto vira um modelo 3D com informação de cada elemento, como diâmetro, material e circuito.`
2. **Preciso que a arquitetura esteja em BIM?** [VALIDAR COM O RT]
   `Não necessariamente. As instalações podem ser modeladas sobre uma arquitetura em 2D. Com a arquitetura e a estrutura em BIM, a compatibilização fica mais completa.`
3. **Em que software vocês trabalham?**
   Fallback: `Entregamos em BIM ou em 2D. Envie o padrão da sua empresa com o pedido de orçamento, e o formato de entrega fica definido na proposta.`
   Com dado: `Modelamos em [INSERIR DADO REAL: software] e entregamos em [INSERIR DADO REAL: formatos].`
4. **Vocês compatibilizam projetos de outros escritórios?**
   Fallback: `Envie os projetos que você já tem e o escopo desejado. Na proposta, definimos o que será compatibilizado e como.`
   [INSERIR DADO REAL: se fazem compatibilização de terceiros como serviço avulso, trocar por: `Sim. Compatibilizamos projetos de outros escritórios com as instalações e a arquitetura.`]
5. **Projeto em BIM custa mais?**
   `O valor depende do escopo e vem detalhado na proposta. Ao comparar, considere quanto custaria resolver na obra um conflito que o modelo mostraria antes.`

### BM-10 CTA final (C13)
- **H2:** `Quer o seu próximo empreendimento compatibilizado em BIM?`
- **Texto:** `Envie a arquitetura e as disciplinas de que você precisa. A proposta vem com escopo, prazo e valor.`
- **Botões:** `Solicitar orçamento` · `Falar no WhatsApp` (mensagem "BIM e compatibilização")

---

## 7. Projetos — listagem (`/projetos/`)

### SEO — Projetos
- **Title:** Projetos em 18 empreendimentos de 6 estados | Intrépida
- **Meta description:** Veja 18 empreendimentos em 6 estados com projetos da Intrépida, para clientes como MRV, Direcional, RNI e Precon. Filtre por estado e cliente.
- **Palavra-chave principal:** portfólio de projetos de instalações
- **Secundárias:** projetos para MRV; projetos complementares de empreendimentos residenciais; clientes Intrépida Engenharia; projetos de instalações em Minas Gerais
- **Slug:** `/projetos/` (301 de `/trabalhos-desenvolvidos/`; `#clientes` recebe o 301 de `/nossos-clientes/`)

### PJ-01 Breadcrumb
`Início › Projetos`

### PJ-02 Hero (C03, baixo)
- **Eyebrow:** `Portfólio`
- **H1:** `Projetos de instalações em 18 empreendimentos de 6 estados`
- **Subtítulo:** `De 142 a 1.800 unidades, para construtoras e incorporadoras como MRV, Direcional, RNI e Precon.`
- **Link discreto:** `Solicitar orçamento →`
- **Alt da imagem:** `Vista aérea dos blocos do Residencial Pacífico, da Vila Construtora, em Ribeirão das Neves/MG`

### PJ-03 Barra de números (C05)
Igual à Home H-03 (mesmas regras e a mesma nota [DERIVADO DO PORTFÓLIO — conferir]).

### PJ-04 Filtros (C22)
| Elemento | Texto |
|---|---|
| Título do bloco (oculto visualmente no desktop) | `Filtrar projetos` |
| Filtro UF — rótulo | `Estado` |
| Opção padrão | `Todos os estados` |
| Opções (com contagem) | `Minas Gerais (11)` · `Distrito Federal (2)` · `São Paulo (2)` · `Rio de Janeiro (1)` · `Mato Grosso do Sul (1)` · `Santa Catarina (1)` |
| Filtro Cliente — rótulo | `Cliente` |
| Opção padrão | `Todos os clientes` |
| Busca no select | placeholder `Buscar cliente` · sem resultado: `Nenhum cliente com esse nome` |
| Filtro Tipo | **CONDICIONAL** (só com ≥ 2 tipos confirmados). Rótulo `Tipo de empreendimento` · `Todos os tipos` |
| Filtro Disciplina | **CONDICIONAL** (só com disciplinas por projeto confirmadas). Rótulo `Disciplina` · `Todas as disciplinas` |
| Limpar | `Limpar filtros` |
| Contador | `18 projetos` · `1 projeto` · `Nenhum projeto` (anunciar com `aria-live="polite"`) |
| Mobile — botão | `Filtrar` / `Filtrar (2)` (número = filtros ativos) |
| Mobile — bottom sheet | título `Filtrar projetos` · botão `Ver 5 projetos` (dinâmico) · `Limpar filtros` · fechar `aria-label="Fechar filtros"` |
| Chip de filtro ativo | texto `MG` / `MRV` · `aria-label="Remover filtro: Minas Gerais"` |

**Estado vazio**
- **H3:** `Nenhum projeto com esses filtros`
- **Texto:** `Tente outro estado ou cliente. Ou conte sobre o seu empreendimento: a experiência que você procura pode não estar no site.`
- **Botões:** `Limpar filtros` · `Falar sobre meu projeto` → `/contato/`

### PJ-05 Grade de projetos (C08, 18 cards)
- **H2 da seção (pode ser visualmente oculto):** `Todos os projetos`
- **Estrutura do card:** foto · H3 nome · linha `[Cliente] · [Cidade/UF]` · destaque `[n] unidades` · tags (CONDICIONAL) · card inteiro clicável.
- **Card sem foto (6 projetos do site antigo):** fundo neutro com nome, cliente e cidade em destaque. Nenhum texto do tipo "foto em breve".
- **Dados dos 18 cards:** tabela da seção 8.1 (mesma ordem).

### PJ-06 Clientes (`#clientes`, C06 completo)
- **H2:** `Clientes atendidos`
- **Texto:** `24 empresas, entre construtoras e incorporadoras, já contrataram projetos da Intrépida.`
- **Logos:** 24, com alt = nome (lista na seção 13.3). Legenda opcional abaixo de cada logo: o mesmo nome.

### PJ-07 Mapa de atuação (C24) — opcional na fase 1
- **H2:** `Onde já projetamos`
- **Instrução:** `Clique em um estado para ver os projetos.`
- **Lista acessível (sempre visível no mobile e para leitor de tela):** `Minas Gerais: 11 projetos` · `Distrito Federal: 2 projetos` · `São Paulo: 2 projetos` · `Rio de Janeiro: 1 projeto` · `Mato Grosso do Sul: 1 projeto` · `Santa Catarina: 1 projeto`
- Título acessível do SVG: `Mapa do Brasil com os seis estados onde a Intrépida tem projetos: MG, DF, SP, RJ, MS e SC`

### PJ-08 CTA final (C13)
- **H2:** `Seu empreendimento pode ser o próximo desta lista`
- **Texto:** `Conte o porte, a cidade e as disciplinas de que você precisa. A proposta vem com escopo, prazo e valor.`
- **Botões:** `Solicitar orçamento` · `Falar no WhatsApp` (mensagem "Projetos")

---

## 8. Páginas de projeto (`/projetos/[empreendimento]/`)

### 8.0 Partes fixas do modelo
- **PP-01 Breadcrumb:** `Início › Projetos › [Nome]` · mobile `‹ Projetos`
- **PP-02 Hero:** H1 `[Nome]` · linha `[Cliente] · [Cidade/UF]` · crédito da foto **CONDICIONAL** [INSERIR DADO REAL: crédito exigido pelo cliente; formato `Foto: [crédito]`].
- **Parágrafo de abertura (proposta do copywriter, logo abaixo da linha do H1):** evita páginas com conteúdo raso para o Google e usa só dados reais.
  Modelo: `O [Nome] é um empreendimento da [Cliente] com [n] unidades em [Cidade/UF]. A Intrépida Engenharia e Projetos desenvolveu projetos de engenharia para o empreendimento.`
  Com disciplinas confirmadas, a 2ª frase vira: `A Intrépida desenvolveu os projetos de [disciplinas, em minúsculas, separadas por vírgula e "e"].`
- **PP-03 Ficha técnica (C15)** — H2 `Ficha técnica`. Rótulos fixos; linha sem dado fica oculta (nunca "—" ou "N/D"):
  `Cliente` · `Local` · `Unidades` · `Tipo` [INSERIR DADO REAL] · `Área construída` [INSERIR DADO REAL] · `Ano` [INSERIR DADO REAL] · `Disciplinas projetadas` [INSERIR DADO REAL] · `Formato de entrega` [INSERIR DADO REAL: BIM ou 2D]
- **PP-04 CTA lateral:** título `Tem um empreendimento parecido?` · texto `Conte sobre ele e receba uma proposta com escopo, prazo e valor.` · botões `Solicitar orçamento` (→ `/contato/?ref=projeto-[slug]`) e `Falar no WhatsApp` (mensagem "Página de projeto").
- **PP-05 Desafio e solução — CONDICIONAL.** Só com case fornecido pelo cliente. H2 `O desafio` · H2 `A solução` · H2 `O resultado`. Nenhum texto escrito.
- **PP-06 Galeria — CONDICIONAL** (≥ 2 imagens). H2 `Imagens do projeto`.
- **PP-07 Depoimento — CONDICIONAL.** H2 `O que diz o cliente`. Nenhum texto escrito.
- **PP-08 Relacionados:** H2 conforme a regra — mesmo cliente: `Outros projetos para [Cliente]`; mesma UF: `Outros projetos em [Estado por extenso]`; misto: `Outros projetos`. Lista na coluna "Relacionados" da tabela 8.1.
- **PP-09 Navegação:** `‹ Projeto anterior` · `Próximo projeto ›` (com o nome do projeto abaixo, em texto menor). A ordem segue a tabela 8.1 e é circular (o 18º leva ao 1º).
- **PP-10 CTA final:** H2 `Tem um empreendimento parecido?` · texto `Conte sobre ele e receba uma proposta com escopo, prazo e valor.` · botões `Solicitar orçamento` · `Falar no WhatsApp`.
- **SEO (modelo):** palavra-chave principal = `[Nome] [Cidade]`; secundárias = `[Cliente] [Cidade]` e `projeto de instalações [Cidade]`. Title e meta por projeto na tabela 8.2.

### 8.1 Os 18 projetos (ordem da listagem, dados como no material real)
| # | Slug | H1 | Linha (cliente · local) | Unidades | Foto | Relacionados (PP-08) |
|---|---|---|---|---|---|---|
| 1 | `mirante-sao-lucas` | Mirante São Lucas | UNENCO · Belo Horizonte/MG | 152 unidades | Sim | Residencial Scharle · Alto Boa Vista · Alto Riviera |
| 2 | `bosque-dos-ipes` | Bosque dos Ipês | RNI · Campo Grande/MS | 142 unidades | Sim | Smart Haus · Mirante São Lucas · Residencial Monte Carlo |
| 3 | `residencial-pacifico` | Residencial Pacífico | Vila Construtora · Ribeirão das Neves/MG | 160 unidades | Sim | Mirante São Lucas · Parque Lagoa dos Príncipes e Lagoa Nova · Residencial Vila Atlântico |
| 4 | `parque-lagoa-dos-principes-e-lagoa-nova` | Parque Lagoa dos Príncipes e Lagoa Nova | MRV · Lagoa Santa/MG | 256 unidades | Sim | Residencial Vila Maria · Residencial Ville Luxemburgo · Residencial Pacífico |
| 5 | `residencial-alta-vista` | Residencial Alta Vista | Quartzo · Barueri/SP | 240 unidades | Sim | Residencial Portal do Cerrado · California Residence · Mirante São Lucas |
| 6 | `residencial-monte-carlo` | Residencial Monte Carlo | Habit Construtora · Cabo Frio/RJ | 1.800 unidades | Sim (baixa resolução) | Bosque dos Ipês · Residencial Alta Vista · Mirante São Lucas |
| 7 | `residencial-vila-atlantico` | Residencial Vila Atlântico | Erglares · Sabará/MG | 240 unidades | Sim | Residencial Scharle · Residencial Pacífico · Mirante São Lucas |
| 8 | `residencial-vila-maria` | Residencial Vila Maria | Mello Azevedo · Lagoa Santa/MG | 356 unidades | Sim | Parque Lagoa dos Príncipes e Lagoa Nova · Residencial Ville Luxemburgo · Residencial Vila Atlântico |
| 9 | `residencial-ville-luxemburgo` | Residencial Ville Luxemburgo | Precon · Lagoa Santa/MG | 368 unidades | Sim (baixa resolução) | Parque Lagoa dos Príncipes e Lagoa Nova · Residencial Vila Maria · Residencial Portal do Engenho |
| 10 | `residencial-portal-do-cerrado` | Residencial Portal do Cerrado | Quartzo · Uberlândia/MG | 192 unidades | Sim (baixa resolução) | Residencial Alta Vista · Residencial Portal do Engenho · Mirante São Lucas |
| 11 | `residencial-scharle` | Residencial Scharle | UNENCO · Sabará/MG | 240 unidades | Sim (baixa resolução) | Mirante São Lucas · Residencial Vila Atlântico · Residencial Pacífico |
| 12 | `residencial-portal-do-engenho` | Residencial Portal do Engenho | Prix Construtora · Itaúna/MG | 208 unidades | Sim | Alto Boa Vista · Alto Riviera · Residencial Portal do Cerrado |
| 13 | `alto-boa-vista` | Alto Boa Vista | Prix Engenharia · Belo Horizonte/MG | 236 unidades | Não | Alto Riviera · Residencial Portal do Engenho · Mirante São Lucas |
| 14 | `alto-riviera` | Alto Riviera | Prix Engenharia · Belo Horizonte/MG | 157 unidades | Não | Alto Boa Vista · Residencial Portal do Engenho · Mirante São Lucas |
| 15 | `gran-vic-gama` | Gran Vic Gama | VIC · Brasília/DF | 236 unidades | Não | Alto Sobradinho · Mirante São Lucas · Residencial Monte Carlo |
| 16 | `alto-sobradinho` | Alto Sobradinho | Direcional Engenharia · Sobradinho/DF | 344 unidades | Não | Gran Vic Gama · Mirante São Lucas · Bosque dos Ipês |
| 17 | `smart-haus` | Smart Haus | RNI · Blumenau/SC | 333 unidades | Não | Bosque dos Ipês · Residencial Monte Carlo · Residencial Alta Vista |
| 18 | `california-residence` | California Residence | Vitta · Marília/SP | 214 unidades | Não | Residencial Alta Vista · Mirante São Lucas · Bosque dos Ipês |

Pontos para o QA (dados mantidos como estavam, por decisão do usuário):
- **Alto Boa Vista e Gran Vic Gama** têm o mesmo número (236 unidades) no site antigo. Mantido; conferir com o cliente.
- **Prix Construtora** (portfólio 2024, Portal do Engenho) x **Prix Engenharia** (site antigo, Alto Boa Vista e Alto Riviera): confirmar se é a mesma empresa e qual nome usar. Até lá, mantido como em cada fonte. Se for a mesma, os 3 projetos aparecem juntos no filtro "Cliente".
- "Belo Horizonte" foi corrigido (no site antigo estava "elo Horizonte").
- O parágrafo de abertura de cada página usa a frase-modelo de 8.0 com os dados desta tabela. Ex. (projeto 1): `O Mirante São Lucas é um empreendimento da UNENCO com 152 unidades em Belo Horizonte/MG. A Intrépida Engenharia e Projetos desenvolveu projetos de engenharia para o empreendimento.`
  Atenção à concordância nos nomes sem "Residencial": `O Bosque dos Ipês`, `O Alto Boa Vista`, `O Smart Haus`, `O California Residence`, `O Gran Vic Gama`, `O Parque Lagoa dos Príncipes e Lagoa Nova` (neste, trocar "é um empreendimento" por `reúne empreendimentos`, se o cliente confirmar que são dois) [INSERIR DADO REAL].

### 8.2 SEO e alt por projeto
| # | Title | Meta description | Alt da foto principal |
|---|---|---|---|
| 1 | Mirante São Lucas – UNENCO, Belo Horizonte \| Intrépida | Mirante São Lucas, da UNENCO, com 152 unidades em Belo Horizonte/MG. Veja o empreendimento e solicite orçamento para o seu projeto. | Vista aérea do Mirante São Lucas, torre residencial da UNENCO em Belo Horizonte/MG |
| 2 | Bosque dos Ipês – RNI, Campo Grande/MS \| Intrépida | Bosque dos Ipês, da RNI, com 142 unidades em Campo Grande/MS. Veja o empreendimento e solicite orçamento para o seu projeto. | Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS |
| 3 | Residencial Pacífico – Ribeirão das Neves \| Intrépida | Residencial Pacífico, da Vila Construtora, com 160 unidades em Ribeirão das Neves/MG. Veja o empreendimento e solicite orçamento. | Vista aérea dos blocos do Residencial Pacífico, da Vila Construtora, em Ribeirão das Neves/MG |
| 4 | Parque Lagoa dos Príncipes e Lagoa Nova – MRV \| Intrépida | Parque Lagoa dos Príncipes e Lagoa Nova, da MRV, com 256 unidades em Lagoa Santa/MG. Veja o empreendimento e solicite orçamento. | Blocos residenciais e estacionamento do Parque Lagoa dos Príncipes, da MRV, em Lagoa Santa/MG |
| 5 | Residencial Alta Vista – Quartzo, Barueri \| Intrépida | Residencial Alta Vista, da Quartzo, com 240 unidades em Barueri/SP. Veja o empreendimento e solicite orçamento para o seu projeto. | Vista aérea das torres do Residencial Alta Vista, da Quartzo, em Barueri/SP |
| 6 | Residencial Monte Carlo – Cabo Frio/RJ \| Intrépida | Residencial Monte Carlo, da Habit Construtora, com 1.800 unidades em Cabo Frio/RJ. Veja o empreendimento e solicite orçamento. | Vista aérea do Residencial Monte Carlo, da Habit Construtora, em Cabo Frio/RJ |
| 7 | Residencial Vila Atlântico – Erglares, Sabará \| Intrépida | Residencial Vila Atlântico, da Erglares, com 240 unidades em Sabará/MG. Veja o empreendimento e solicite orçamento para o seu projeto. | Vista aérea dos blocos do Residencial Vila Atlântico, da Erglares, em Sabará/MG |
| 8 | Residencial Vila Maria – Lagoa Santa/MG \| Intrépida | Residencial Vila Maria, da Mello Azevedo, com 356 unidades em Lagoa Santa/MG. Veja o empreendimento e solicite orçamento. | Vista aérea do Residencial Vila Maria, da Mello Azevedo, com área de lazer e piscina, em Lagoa Santa/MG |
| 9 | Residencial Ville Luxemburgo – Precon \| Intrépida | Residencial Ville Luxemburgo, da Precon, com 368 unidades em Lagoa Santa/MG. Veja o empreendimento e solicite orçamento. | Blocos e área de lazer do Residencial Ville Luxemburgo, da Precon, em Lagoa Santa/MG |
| 10 | Residencial Portal do Cerrado – Uberlândia \| Intrépida | Residencial Portal do Cerrado, da Quartzo, com 192 unidades em Uberlândia/MG. Veja o empreendimento e solicite orçamento. | Blocos do Residencial Portal do Cerrado, da Quartzo, com reservatório elevado, em Uberlândia/MG |
| 11 | Residencial Scharle – UNENCO, Sabará \| Intrépida | Residencial Scharle, da UNENCO, com 240 unidades em Sabará/MG. Veja o empreendimento e solicite orçamento para o seu projeto. | Vista aérea do Residencial Scharle, da UNENCO, com blocos, estacionamento e quadra, em Sabará/MG |
| 12 | Residencial Portal do Engenho – Itaúna/MG \| Intrépida | Residencial Portal do Engenho, da Prix Construtora, com 208 unidades em Itaúna/MG. Veja o empreendimento e solicite orçamento. | Vista aérea do Residencial Portal do Engenho, da Prix Construtora, em Itaúna/MG |
| 13 | Alto Boa Vista – Belo Horizonte/MG \| Intrépida | Alto Boa Vista, da Prix Engenharia, com 236 unidades em Belo Horizonte/MG. Veja o empreendimento e solicite orçamento. | — (sem foto) |
| 14 | Alto Riviera – Belo Horizonte/MG \| Intrépida | Alto Riviera, da Prix Engenharia, com 157 unidades em Belo Horizonte/MG. Veja o empreendimento e solicite orçamento. | — (sem foto) |
| 15 | Gran Vic Gama – VIC, Brasília/DF \| Intrépida | Gran Vic Gama, da VIC, com 236 unidades em Brasília/DF. Veja o empreendimento e solicite orçamento para o seu projeto de instalações. | — (sem foto) |
| 16 | Alto Sobradinho – Direcional, Sobradinho/DF \| Intrépida | Alto Sobradinho, da Direcional Engenharia, com 344 unidades em Sobradinho/DF. Veja o empreendimento e solicite orçamento. | — (sem foto) |
| 17 | Smart Haus – RNI, Blumenau/SC \| Intrépida | Smart Haus, da RNI, com 333 unidades em Blumenau/SC. Veja o empreendimento e solicite orçamento para o seu projeto de instalações. | — (sem foto) |
| 18 | California Residence – Vitta, Marília/SP \| Intrépida | California Residence, da Vitta, com 214 unidades em Marília/SP. Veja o empreendimento e solicite orçamento para o seu projeto. | — (sem foto) |

Quando chegarem as fotos dos projetos 13 a 18, o alt segue o padrão: `Vista aérea do [Nome], da [Cliente], em [Cidade/UF]` (ajustar "vista aérea" ao que a foto mostra).

---

## 9. Sobre (`/sobre/`)

### SEO — Sobre
- **Title:** Sobre a Intrépida Engenharia e Projetos | BH
- **Meta description:** Empresa de Belo Horizonte de projetos de instalações prediais e infraestrutura, em 2D e BIM. Conheça o responsável técnico e os dados para cadastro.
- **Palavra-chave principal:** Intrépida Engenharia e Projetos
- **Secundárias:** empresa de projetos de instalações BH; engenharia de projetos Belo Horizonte; Carlos Alberto Grope engenheiro
- **Slug:** `/sobre/` (301 de `/quem-somos/`)

### SB-01 Breadcrumb
`Início › Sobre`

### SB-02 Hero interno (C04)
- **Eyebrow:** `Sobre a Intrépida`
- **H1:** `Uma empresa de projetos, feita para quem constrói`
- **Subtítulo:** `A Intrépida Engenharia e Projetos desenvolve projetos de instalações prediais e infraestrutura, em 2D e BIM, para construtoras, incorporadoras e arquitetos. Não executamos obras: entregamos o projeto de que a sua obra precisa.`
- **CTA primário:** `Solicitar orçamento`
- **CTA secundário:** `Baixar portfólio (PDF)` — **CONDICIONAL** [INSERIR DADO REAL: PDF liberado]
- **Alt da imagem (provisória):** `Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS`

### SB-03 Quem somos (C09)
- **H2:** `Quem é a Intrépida`
  (Quando chegarem ano de fundação e marcos, o H2 vira `Nossa história` e entra a linha do tempo.)
- **Texto:**
  `Somos uma empresa técnica de Belo Horizonte dedicada a projetos de instalações residenciais, comerciais e de redes de infraestrutura urbana.`
  `Trabalhamos em 2D e em BIM, com informação para a execução, a implantação, a manutenção e a gestão do empreendimento. O objetivo é que a obra receba um projeto compatível entre as disciplinas e pronto para a análise das concessionárias.`
  `Nosso portfólio reúne 18 empreendimentos em seis estados, de 142 a 1.800 unidades. Ao todo, 24 empresas, entre construtoras e incorporadoras, já contrataram nossos projetos.`
  `Intrépida quer dizer corajosa. Para nós, isso significa assumir empreendimentos grandes e complexos com método, cálculo e responsabilidade técnica.`
- **Linha do tempo — CONDICIONAL** [INSERIR DADO REAL: ano de fundação e marcos com data]. Formato por item: `[Ano]` · `[Marco em até 12 palavras]`.

### SB-04 Responsável técnico (C17 completo)
- **H2:** `Responsável técnico`
- **Nome:** `Carlos Alberto Grope`
- **Cargo:** `Diretor técnico · Engenheiro civil sanitarista`
- **CREA:** **CONDICIONAL** [INSERIR DADO REAL: nº do CREA]
- **Texto (publicável hoje):** `Carlos Alberto Grope é engenheiro civil sanitarista e diretor técnico da Intrépida. Ele conduz os projetos da empresa e é o seu contato técnico do orçamento à entrega.`
- **Mini-bio ampliada — CONDICIONAL** [INSERIR DADO REAL: formação, trajetória, especialidades. Não escrever sem dado.]
- **LinkedIn pessoal — CONDICIONAL** [INSERIR DADO REAL: URL]. Texto do link: `Ver perfil no LinkedIn`.
- **Foto:** [INSERIR DADO REAL: FOTOGRAFAR]. Alt: `Carlos Alberto Grope, diretor técnico da Intrépida Engenharia e Projetos`.

### SB-05 Equipe — CONDICIONAL
- Só com nomes, funções e fotos reais [INSERIR DADO REAL]. **H2:** `Equipe` · cards `[Nome]` · `[Função]`. Alt da foto: `[Nome], [função] na Intrépida`. Sem dados → seção oculta.

### SB-06 Números e área de atuação (C05 + C24)
- **H2:** `Onde já projetamos`
- Barra de números: igual à Home H-03.
- Mapa: igual a PJ-07 (título acessível e lista de estados).

### SB-07 Como trabalhamos (C10)
- **H2:** `Como trabalhamos`
- Mesmas 5 etapas da Home H-09. Valores da empresa: não escritos (não há dado) [INSERIR DADO REAL, se o cliente quiser].

### SB-08 Dados cadastrais (`#dados-cadastrais`, C15)
- **H2:** `Dados para cadastro de fornecedor`
- **Intro:** `Para o setor de suprimentos: os dados da empresa e o portfólio em PDF.`
- **Ficha** (linha sem dado fica oculta):
  - `Razão social:` [INSERIR DADO REAL]
  - `Nome fantasia:` `Intrépida Engenharia e Projetos`
  - `CNPJ:` [INSERIR DADO REAL]
  - `Registro da empresa no CREA:` [INSERIR DADO REAL]
  - `Responsável técnico:` `Carlos Alberto Grope, engenheiro civil sanitarista` + ` · CREA [INSERIR DADO REAL]`
  - `Endereço:` `Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910`
  - `E-mail:` `carlos@intrepidaengenharia.com.br`
  - `Telefone:` `(31) 3070-6568`
- **Botão:** `Baixar portfólio (PDF)` — **CONDICIONAL** [INSERIR DADO REAL: PDF liberado e atualizado]. Texto de apoio: `Clientes, empreendimentos e modelos BIM em um arquivo.`
- **Sem PDF:** `Precisa de mais documentos para o cadastro? Escreva para carlos@intrepidaengenharia.com.br.`

### SB-09 Clientes (C06, 12)
- **H2:** `Quem já contratou nossos projetos`
- **Link:** `Ver todos os clientes e projetos →`

### SB-10 CTA final (C13)
- **H2:** `Vamos conversar sobre o seu empreendimento?`
- **Texto:** `Envie as informações do projeto e receba uma proposta com escopo, prazo e valor.`
- **Botões:** `Solicitar orçamento` · `Falar no WhatsApp` (mensagem "Sobre")

---

## 10. Contato e orçamento (`/contato/`)

### SEO — Contato
- **Title:** Solicite orçamento de projeto de instalações | Intrépida
- **Meta description:** Peça orçamento de projetos hidrossanitário, elétrico, de gás, BIM e infraestrutura. Envie a arquitetura pelo formulário ou fale no WhatsApp.
- **Palavra-chave principal:** orçamento de projeto de instalações
- **Secundárias:** orçamento projeto hidrossanitário; orçamento projeto elétrico predial; contato Intrépida Engenharia; projetista de instalações BH
- **Slug:** `/contato/`

### CT-01 Breadcrumb
`Início › Contato`

### CT-02 Cabeçalho curto (C04 sem imagem)
- **Eyebrow:** `Contato e orçamento`
- **H1:** `Solicite um orçamento de projeto`
- **Subtítulo:** `Conte sobre o empreendimento em três etapas rápidas. Com a arquitetura em mãos, a proposta sai mais precisa.`
  [INSERIR DADO REAL: prazo de retorno → acrescentar `Retornamos em até [X] dias úteis.`]
- **Selos (3):**
  1. Com dado: `Retorno em até [X] dias úteis` · Sem dado (publicável hoje): `Proposta com escopo, prazo e valor`
  2. `Atendimento direto com o engenheiro`
  3. `Seus arquivos tratados com sigilo`
- **Link-âncora (mobile, acima do formulário):** `Prefere WhatsApp? ↓`

### CT-03 Formulário qualificado C21a (3 etapas)

**Regras gerais de microcopy**
- Legenda no topo do formulário: `Todos os campos são obrigatórios, exceto os marcados como opcionais.`
- Campo opcional: rótulo + ` (opcional)`. Nada de asterisco.
- Barra de progresso (texto visível e lido por leitor de tela): `Etapa 1 de 3 — O empreendimento` · `Etapa 2 de 3 — Escopo` · `Etapa 3 de 3 — Seus dados`
- Botões: `Continuar` · `Voltar` · final `Enviar pedido de orçamento`
- Os dados ficam preenchidos ao voltar de etapa.

**Etapa 1 — O empreendimento**
- Linha de apoio: `Comece pelo projeto. Seus dados de contato ficam para o fim.`

| Campo | Rótulo | Placeholder | Ajuda | Mensagens de erro |
|---|---|---|---|---|
| Tipo (cards) | `Tipo de empreendimento` | — | — | `Escolha o tipo de empreendimento.` |
| ↳ opção | `Residencial multifamiliar` | — | `Prédios e conjuntos de apartamentos` | — |
| ↳ opção | `Loteamento ou condomínio horizontal` | — | `Casas e lotes` | — |
| ↳ opção | `Comercial ou corporativo` | — | `Lojas, salas, galpões, hotéis` | — |
| ↳ opção (CONDICIONAL, público P4) | `Residência unifamiliar` | — | `Casa própria` | — |
| ↳ opção | `Infraestrutura urbana` | — | `Redes de água, esgoto e drenagem` | — |
| ↳ opção | `Outro` | — | — | — |
| ↳ "Outro" aberto | `Qual tipo?` | `Ex.: clínica, escola, indústria` | — | `Conte qual é o tipo de empreendimento.` |
| Cidade | `Cidade do empreendimento` | `Ex.: Belo Horizonte` | — | `Informe a cidade do empreendimento.` |
| UF | `Estado` | opção inicial `Selecione` | — | `Selecione o estado.` |
| Unidades (multifamiliar/loteamento) | `Número de unidades` | `Ex.: 240` | `Apartamentos, casas ou lotes.` | `Informe o número de unidades ou marque "Ainda não definido".` · `Use só números, por exemplo 240.` |
| ↳ checkbox | `Ainda não definido` | — | — | — |
| Área (comercial/residência/outro) | `Área construída aproximada, em m² (opcional)` | `Ex.: 1500` | — | `Use só números, por exemplo 1500.` |
| Fase | `Fase do projeto (opcional)` | opção inicial `Selecione` | `Ajuda a definir o que entra na proposta.` | — |
| ↳ opções [INSERIR DADO REAL: validar lista] | `Estudo de viabilidade` · `Arquitetura em desenvolvimento` · `Projeto legal aprovado` · `Projeto executivo` · `Obra em andamento` | | | |

**Etapa 2 — Escopo**
- Linha de apoio: `Marque o que você precisa. Se não souber, a gente orienta.`

| Campo | Rótulo | Placeholder | Ajuda | Mensagens de erro |
|---|---|---|---|---|
| Disciplinas (checkboxes em 3 grupos) | `Quais projetos você precisa?` | — | `Marque um ou mais.` | `Marque pelo menos um projeto ou a opção "Ainda não sei".` |
| ↳ grupo | `Instalações prediais`: `Hidrossanitário` · `Elétrica e Sistemas` · `Gás` · `Climatização (HVAC)` · `Pressurização de escadas` · `Piscina` | | | |
| ↳ grupo | `Infraestrutura urbana`: `Infraestrutura de saneamento` | | | |
| ↳ grupo | `Eficiência e sustentabilidade`: `Reúso de água pluvial` · `Aquecimento solar` | | | |
| ↳ avulso | `Compatibilização BIM` | | | |
| ↳ avulso | `Ainda não sei — quero orientação` | — | `Indicamos as disciplinas a partir da arquitetura.` | Ao marcar, anunciar (aria-live): `As outras opções foram desmarcadas.` |
| Formato | `Formato de entrega (opcional)` | — | — | — |
| ↳ opções | `BIM (modelo 3D)` · `2D (DWG)` · `Sem preferência` | | | |
| Prazo | `Prazo desejado para o projeto` | opção inicial `Selecione` | — | `Escolha um prazo.` |
| ↳ opções [INSERIR DADO REAL: validar faixas] | `Até 30 dias` · `De 1 a 3 meses` · `De 3 a 6 meses` · `Sem prazo definido` | | | |
| Link | `Link dos arquivos (opcional)` | `https://` | `Google Drive, WeTransfer, Dropbox ou outro. Confira se o link está liberado para visualização.` | `Cole um link completo, começando com https://` |
| Upload | `Anexar arquivos (opcional)` | área: `Arraste os arquivos aqui ou clique para selecionar` | `PDF, DWG, RVT, IFC ou ZIP, até [INSERIR DADO REAL: X] MB no total. Arquivos grandes? Use o campo de link acima.` | Formato: `O arquivo [nome] não é aceito. Envie PDF, DWG, RVT, IFC ou ZIP.` · Tamanho: `Os arquivos passam de [X] MB. Envie pelo campo de link acima.` · Falha: `Não foi possível anexar [nome]. Tente de novo ou use o campo de link.` |
| ↳ estados do upload | progresso `Enviando [nome]… 45%` · concluído `[nome] anexado` · remover `Remover [nome]` | | | |
| Mensagem | `Conte mais sobre o projeto (opcional)` | `Ex.: 3 torres de 12 pavimentos, arquitetura em desenvolvimento, precisamos aprovar o projeto na concessionária até março.` | contador `Até 1.000 caracteres` | `A mensagem passou de 1.000 caracteres.` |

**Etapa 3 — Seus dados**
- Linha de apoio: `Para onde enviamos a proposta?`

| Campo | Rótulo | Placeholder | Ajuda | Mensagens de erro |
|---|---|---|---|---|
| Nome | `Nome completo` | — | — | `Informe seu nome.` |
| Empresa | `Empresa (opcional)` | — | `Deixe em branco se for pessoa física.` | — |
| Cargo | `Cargo (opcional)` | `Ex.: Coordenador de projetos` | — | — |
| E-mail | `E-mail` | `nome@empresa.com.br` | — | `Informe seu e-mail.` · `Digite um e-mail válido, como nome@empresa.com.br.` |
| Telefone | `WhatsApp ou telefone` | `(31) 90000-0000` | `Com DDD.` | `Informe um telefone para contato.` · `Digite o número com DDD, como (31) 90000-0000.` |
| Origem | `Como conheceu a Intrépida? (opcional)` | opção inicial `Selecione` | — | — |
| ↳ opções | `Busca no Google` · `Indicação` · `LinkedIn` · `Já sou cliente` · `Outro` | | | |
| LGPD (desmarcado) | `Concordo com o uso dos meus dados para receber o orçamento, conforme a Política de privacidade.` ("Política de privacidade" é link, abre em nova aba) | — | — | `Para enviar, marque que concorda com a Política de privacidade.` |
| Novidades — CONDICIONAL (só se houver comunicação por e-mail) | `Quero receber novidades da Intrépida por e-mail (opcional).` | — | — | — |

**Abaixo do botão final**
- Com prazo: `Resposta em até [X] dias úteis. Você recebe uma cópia do pedido no seu e-mail.`
- Sem prazo (publicável hoje): `Você recebe uma cópia do pedido no seu e-mail.`

**Estados e mensagens do formulário**
| Situação | Texto |
|---|---|
| Resumo de erros no topo da etapa | `Revise 1 campo para continuar:` / `Revise [n] campos para continuar:` + lista com link para cada campo (usar o texto do erro) |
| Enviando (botão desativado) | `Enviando…` |
| Falha no envio | `Não conseguimos enviar o seu pedido agora. Seus dados continuam preenchidos. Tente de novo em alguns instantes ou fale pelo WhatsApp (31) 99649-8629.` |
| Anti-spam bloqueou (verificação falhou) | `Não conseguimos confirmar o envio. Atualize a página e tente de novo, ou fale pelo WhatsApp (31) 99649-8629.` |
| Sucesso | Redireciona para `/obrigado/` (ver seção 11). |
| Fallback sem etapas (uma página, 3 `fieldset`) | Títulos dos blocos: `1. O empreendimento` · `2. Escopo` · `3. Seus dados` |

**Coluna lateral "Prefere falar agora?" (desktop sticky; mobile abaixo do formulário)**
- **H2:** `Prefere falar agora?`
- `WhatsApp` · `(31) 99649-8629` · botão `Falar no WhatsApp` (mensagem "Contato")
- `Telefone` · `(31) 3070-6568` · botão `Ligar`
- `E-mail` · `carlos@intrepidaengenharia.com.br` · botão `Enviar e-mail`
- `Endereço` · `Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910`
- `Horário` — **CONDICIONAL** [INSERIR DADO REAL]

### CT-04 O que enviar (C12)
- **H2:** `O que enviar para um orçamento rápido`
1. **Quais arquivos ajudam?**
   `A arquitetura (plantas, cortes, fachadas e implantação) em DWG, PDF ou RVT, o número de unidades e de pavimentos e a fase do projeto. Se tiver, envie também a estrutura e as diretrizes das concessionárias.`
2. **Meus arquivos ficam em sigilo?** [VALIDAR COM O CLIENTE: é um compromisso que a empresa precisa cumprir]
   `Sim. Usamos os arquivos só para preparar o orçamento e o projeto, e não os repassamos a terceiros.`
3. **Em quanto tempo recebo a proposta?**
   Fallback: `Depende do porte e das disciplinas. Assim que analisarmos o pedido, informamos quando a proposta fica pronta.`
   Com dado: `Em até [INSERIR DADO REAL: X] dias úteis depois de recebermos as informações completas.`
4. **Ainda não tenho a arquitetura pronta. Posso pedir orçamento?**
   `Pode. Quanto antes o projetista entra, mais fácil prever shafts, reservatórios e as exigências das concessionárias. Envie o estudo que tiver.`

### CT-05 Endereço e mapa — CONDICIONAL (só com atendimento presencial confirmado)
- **H2:** `Onde estamos`
- **Endereço:** `Rua dos Goitacazes, 103, salas 1604 e 1606 · Centro, Belo Horizonte/MG · CEP 30190-910`
- **Linha de atendimento:** [INSERIR DADO REAL: ex. `Atendimento presencial com hora marcada.`]
- **Mapa (carrega sob clique):** imagem estática + botão `Abrir no mapa` (`aria-label="Abrir endereço no Google Maps (abre em nova aba)"`)
- Sem confirmação de atendimento presencial → seção removida; o endereço fica no rodapé e na coluna lateral.

### 10.4 Formulário curto C21b (CTA final da Home e das páginas de serviço)
| Campo | Rótulo | Placeholder | Erros |
|---|---|---|---|
| Nome | `Nome` | — | `Informe seu nome.` |
| E-mail | `E-mail` | `nome@empresa.com.br` | `Informe seu e-mail.` · `Digite um e-mail válido, como nome@empresa.com.br.` |
| Telefone | `WhatsApp ou telefone` | `(31) 90000-0000` | `Informe um telefone para contato.` · `Digite o número com DDD, como (31) 90000-0000.` |
| Empresa | `Empresa (opcional)` | — | — |
| Local | `Cidade/UF do empreendimento (opcional)` | `Ex.: Belo Horizonte/MG` | — |
| Mensagem | `Mensagem (opcional)` | `Conte o tipo de empreendimento, o número de unidades e os projetos de que você precisa.` | — |
| LGPD | `Concordo com o uso dos meus dados para receber o orçamento, conforme a Política de privacidade.` | — | `Para enviar, marque que concorda com a Política de privacidade.` |
- **Botão:** `Solicitar orçamento` (estado `Enviando…`)
- **Abaixo do botão:** `Tem arquivos? Depois do envio, mande pelo WhatsApp ou use o formulário completo.`
- Falha de envio e resumo de erros: mesmos textos do C21a.

---

## 11. Obrigado (`/obrigado/`, noindex)

### SEO — Obrigado
- **Title:** Pedido recebido | Intrépida Engenharia
- **Meta description:** Recebemos seu pedido de orçamento. Veja os próximos passos e, se quiser, adiante o envio dos arquivos do projeto pelo WhatsApp.
- **Indexação:** `noindex, nofollow`. Sem palavra-chave.
- **Slug:** `/obrigado/`

### Conteúdo
- **H1:** `Recebemos seu pedido de orçamento`
- **Frase de confirmação:** `Obrigado pelo contato. Enviamos uma cópia do pedido para o seu e-mail.`
  (Se a cópia ao usuário não for implementada, a 2ª frase sai.)
- **H2:** `O que acontece agora`
  1. `Analisamos as informações e os arquivos do seu empreendimento.`
  2. `Entramos em contato para alinhar escopo e disciplinas.` [INSERIR DADO REAL: com prazo → `Entramos em contato em até [X] dias úteis para alinhar escopo e disciplinas.`]
  3. `Você recebe a proposta com escopo, prazo e valor.`
- **Bloco de destaque — H2:** `Quer adiantar? Envie os arquivos pelo WhatsApp`
  - Texto: `Plantas, implantação ou o link da pasta: mande pelo WhatsApp e juntamos ao seu pedido.`
  - Botão: `Enviar arquivos pelo WhatsApp` (mensagem "Obrigado")
- **Para quem veio do formulário curto (rótulo `orcamento_rapido`):** linha extra `Quer detalhar mais? Complete seu pedido no formulário completo.` → link `Completar meu pedido` (`/contato/`)
- **Links:** `Ver projetos` · `Baixar portfólio (PDF)` (CONDICIONAL) · `Voltar para o início`

---

## 12. Página 404

### SEO — 404
- **Title:** Página não encontrada | Intrépida Engenharia
- **Meta description:** (não necessária; página com status 404 e `noindex`)

### Conteúdo
- **H1:** `Página não encontrada`
- **Texto:** `O endereço pode ter mudado com o novo site da Intrépida. Escolha um dos caminhos abaixo.`
- **Cards:**
  - `Serviços` — `As nove disciplinas que projetamos.` → `/servicos/`
  - `Projetos` — `Os 18 empreendimentos do nosso portfólio.` → `/projetos/`
  - `Solicitar orçamento` (primário) — `Conte sobre o seu empreendimento.` → `/contato/`
- **Links:** `Voltar para o início` · `Falar no WhatsApp` (mensagem "404")

---

## 13. Imagens: legendas e textos alternativos

Regras: alt descreve o que a imagem mostra e onde, sem "imagem de" ou "foto de"; até ~125 caracteres. Ícones decorativos ao lado de texto usam `alt=""` (o texto já informa). Imagens geradas por IA levam a legenda visível `Imagem ilustrativa` e a indicação no alt.

### 13.1 Fotos de empreendimentos (`equipe/fotos/obras-empreendimentos/`)
| Arquivo | Alt | Crédito/legenda curta |
|---|---|---|
| `…p08_mirante-sao-lucas_UNENCO_bh-MG…` | `Vista aérea do Mirante São Lucas, torre residencial da UNENCO em Belo Horizonte/MG` | `Mirante São Lucas · UNENCO · Belo Horizonte/MG` |
| `…p08_bosque-dos-ipes_RNI_campo-grande-MS…` | `Vista aérea do Bosque dos Ipês em construção, empreendimento da RNI em Campo Grande/MS` | `Bosque dos Ipês · RNI · Campo Grande/MS` |
| `…p09_parque-lagoa-dos-principes-lagoa-nova_MRV_lagoa-santa-MG…` | `Blocos residenciais e estacionamento do Parque Lagoa dos Príncipes, da MRV, em Lagoa Santa/MG` | `Parque Lagoa dos Príncipes e Lagoa Nova · MRV · Lagoa Santa/MG` |
| `…p09_residencial-monte-carlo_HABIT_cabo-frio-RJ…` | `Vista aérea do Residencial Monte Carlo, da Habit Construtora, em Cabo Frio/RJ` | `Residencial Monte Carlo · Habit Construtora · Cabo Frio/RJ` |
| `…p10_residencial-vila-atlantico_ERGLARES_sabara-MG…` | `Vista aérea dos blocos do Residencial Vila Atlântico, da Erglares, em Sabará/MG` | `Residencial Vila Atlântico · Erglares · Sabará/MG` |
| `…p10_residencial-vila-maria_MELLO-AZEVEDO_lagoa-santa-MG…` | `Vista aérea do Residencial Vila Maria, da Mello Azevedo, com área de lazer e piscina, em Lagoa Santa/MG` | `Residencial Vila Maria · Mello Azevedo · Lagoa Santa/MG` |
| `…p11_residencial-alta-vista_QUARTZO_barueri-SP…` | `Vista aérea das torres do Residencial Alta Vista, da Quartzo, em Barueri/SP` | `Residencial Alta Vista · Quartzo · Barueri/SP` |
| `…p11_residencial-ville-luxemburgo_PRECON_lagoa-santa-MG…` | `Blocos e área de lazer do Residencial Ville Luxemburgo, da Precon, em Lagoa Santa/MG` | `Residencial Ville Luxemburgo · Precon · Lagoa Santa/MG` |
| `…p12_residencial-portal-do-cerrado_QUARTZO_uberlandia-MG…` | `Blocos do Residencial Portal do Cerrado, da Quartzo, com reservatório elevado, em Uberlândia/MG` | `Residencial Portal do Cerrado · Quartzo · Uberlândia/MG` |
| `…p12_residencial-scharle_UNENCO_sabara-MG…` | `Vista aérea do Residencial Scharle, da UNENCO, com blocos, estacionamento e quadra, em Sabará/MG` | `Residencial Scharle · UNENCO · Sabará/MG` |
| `…p13_residencial-pacifico_VILA_ribeirao-das-neves-MG…` | `Vista aérea dos blocos do Residencial Pacífico, da Vila Construtora, em Ribeirão das Neves/MG` | `Residencial Pacífico · Vila Construtora · Ribeirão das Neves/MG` |
| `…p13_residencial-portal-do-engenho_PRIX_itauna-MG…` | `Vista aérea do Residencial Portal do Engenho, da Prix Construtora, em Itaúna/MG` | `Residencial Portal do Engenho · Prix Construtora · Itaúna/MG` |

Sugestão de nome de arquivo para a web (SEO de imagem): `mirante-sao-lucas-unenco-belo-horizonte.webp`, `bosque-dos-ipes-rni-campo-grande.webp` etc. (nome do empreendimento + cliente + cidade, sem acento).

### 13.2 Imagens BIM (`equipe/fotos/bim-modelos-3d/`)
Os números abaixo são os usados nas referências das páginas. Legendas marcadas [A CONFIRMAR] dependem da confirmação da disciplina; sem ela, usar a legenda genérica `Modelo BIM de instalações prediais` e manter o alt.

| # | Arquivo | Legenda visível | Alt |
|---|---|---|---|
| 1 | `…p03_bim-hidrossanitario-a…` | `Shaft hidráulico com hidrômetros individuais` | `Modelo BIM 3D de shaft hidráulico com prumadas de água e hidrômetros individuais por unidade` |
| 2 | `…p03_bim-hidrossanitario-b…` | `Casa de bombas com conjunto motobomba` [A CONFIRMAR: piscina ou recalque de água] | `Modelo BIM 3D de casa de bombas com duas motobombas e tubulações de sucção e recalque` |
| 3 | `…p04_bim-a…` | `Ramais de água fria e água quente` | `Modelo BIM 3D de ramais de água fria e água quente em banheiro, com diâmetros indicados` |
| 4 | `…p04_bim-b…` | `Esgoto sanitário e ventilação de banheiro` | `Modelo BIM 3D das tubulações de esgoto sanitário e ventilação de um banheiro` |
| 5 | `…p05_bim-a…` | `Instalações de uma unidade, por sistema` [A CONFIRMAR: disciplinas] | `Modelo BIM 3D com tubulações de esgoto, ventilação e água de uma unidade residencial, em cores por sistema` |
| 6 | `…p05_bim-b…` | `Prumada e abrigo de medidores em shaft` [A CONFIRMAR: gás?] | `Modelo BIM 3D de shaft com prumada de tubulação e abrigo de medidores` |
| 7 | `…p06_bim-quadro-eletrico…` | `Quadro de distribuição elétrica` | `Modelo BIM 3D de quadro de distribuição elétrica com disjuntores identificados` |
| 8 | `…p06_bim-tubulacao-gas-ou-hidraulica…` | `Rede de distribuição no pavimento` [A CONFIRMAR: gás ou hidráulica] | `Modelo BIM 3D de rede de tubulações distribuída pelo pavimento, com pontos de consumo numerados` |

Galeria da Home (H-07): imagens 1, 7, 5 e 8.

### 13.3 Logos de clientes (`equipe/marca/logos-clientes/`) — alt = nome
| # | Alt | # | Alt |
|---|---|---|---|
| 01 | `Precon Engenharia` | 13 | `Prix Construtora` |
| 02 | `MRV` | 14 | `Mello Azevedo` |
| 03 | `Direcional` | 15 | `Vitta Residencial` |
| 04 | `Tenda` | 16 | `MCP Realty` |
| 05 | `Riva Incorporadora` | 17 | `CTE – Centro de Tecnologia de Edificações` |
| 06 | `RNI` | 18 | `Gabbai Empreendimentos` |
| 07 | `VIC Engenharia` | 19 | `UNENCO` |
| 08 | `Patrimar` | 20 | `BRZ Empreendimentos` |
| 09 | `Novolar` | 21 | `Vila Construtora` |
| 10 | `Quartzo Incorporadora` | 22 | `Chandon` |
| 11 | `Erglares Engenharia` | 23 | `Center Norte` |
| 12 | `RRX Incorporações` | 24 | `Cataguá Construtora` |

(Grafias conferidas nos próprios logos. Se o logo for link, o rótulo acessível é o mesmo nome.)

### 13.4 Marca e outros
- Logo no header: `Intrépida Engenharia e Projetos` · no rodapé: idem.
- Favicon/ícone: sem alt (metadado).
- Textura azul de fundo (`portfolio-2024_fundo-capa…`): decorativa, `alt=""`.
- Ícones das disciplinas e dos benefícios: decorativos, `alt=""`.
- Retrato do RT (quando houver): `Carlos Alberto Grope, diretor técnico da Intrépida Engenharia e Projetos`.

---

## 14. Política de privacidade (`/politica-de-privacidade/`)

> **MINUTA — VALIDAR COM O CLIENTE/JURÍDICO.** Texto-base escrito pelo copywriter a partir do que o site vai coletar segundo o wireframe. Não publicar sem revisão jurídica. Itens entre colchetes dependem do cliente.

### SEO — Política
- **Title:** Política de privacidade | Intrépida Engenharia
- **Meta description:** Como a Intrépida Engenharia e Projetos coleta, usa e protege os dados enviados pelo site, e como exercer os seus direitos pela LGPD.
- **Slug:** `/politica-de-privacidade/` · indexável, sem palavra-chave-alvo.

### Texto da minuta

**H1:** `Política de privacidade`
`Última atualização: [INSERIR DATA DA PUBLICAÇÃO]`

**Sumário:** 1. Quem somos · 2. Quais dados coletamos · 3. Para que usamos os dados · 4. Bases legais · 5. Com quem compartilhamos · 6. Cookies · 7. Por quanto tempo guardamos · 8. Como protegemos · 9. Seus direitos · 10. Contato do encarregado · 11. Alterações

**H2 1. Quem somos**
Esta política explica como a [INSERIR DADO REAL: razão social], inscrita no CNPJ [INSERIR DADO REAL], com sede na Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910 ("Intrépida", "nós"), trata os dados pessoais de quem usa o site intrepidaengenharia.com.br, conforme a Lei Geral de Proteção de Dados Pessoais (Lei 13.709/2018, LGPD). A Intrépida é a controladora desses dados.

**H2 2. Quais dados coletamos**
- **Dados que você nos envia pelos formulários:** nome, e-mail, telefone ou WhatsApp, empresa, cargo, cidade e estado do empreendimento, informações sobre o projeto e, se você quiser, arquivos ou links de arquivos.
- **Dados de contato direto:** o que você nos enviar por WhatsApp, telefone ou e-mail.
- **Dados de navegação:** com o seu consentimento, informações como páginas visitadas, tempo de visita, tipo de dispositivo, navegador, cidade aproximada e origem do acesso, coletadas por cookies de medição. [INSERIR DADO REAL: confirmar as ferramentas: Google Analytics 4, Google Tag Manager, outras]
- **Dados técnicos de segurança:** endereço IP e dados do navegador usados pela proteção contra spam dos formulários. [INSERIR DADO REAL: reCAPTCHA ou Turnstile]

Não pedimos dados sensíveis. Pedimos que os arquivos de projeto não contenham dados pessoais de terceiros além do necessário.

**H2 3. Para que usamos os dados**
- Responder ao seu pedido e preparar o orçamento e a proposta.
- Falar com você sobre o projeto, por e-mail, telefone ou WhatsApp.
- Cumprir obrigações legais e regulatórias.
- Medir o uso do site e melhorar o conteúdo, de forma agregada, se você aceitar os cookies de medição.
- Proteger o site contra spam e uso indevido.
- Enviar novidades por e-mail, só se você marcar essa opção. [INSERIR DADO REAL: manter só se houver comunicação]

**H2 4. Bases legais**
- **Procedimentos preliminares a um contrato, a seu pedido** (art. 7º, V, da LGPD): orçamento e proposta.
- **Consentimento** (art. 7º, I): cookies de medição e envio de novidades. Você pode retirar o consentimento quando quiser.
- **Legítimo interesse** (art. 7º, IX): segurança do site e prevenção de fraude e spam.
- **Cumprimento de obrigação legal ou regulatória** (art. 7º, II), quando aplicável.

**H2 5. Com quem compartilhamos**
Não vendemos nem alugamos dados pessoais. Compartilhamos apenas com fornecedores que nos ajudam a operar o site e o atendimento, e só no necessário:
- hospedagem do site e serviço de e-mail [INSERIR DADO REAL: fornecedores];
- ferramentas de medição e de proteção contra spam [INSERIR DADO REAL: Google e outros];
- WhatsApp (Meta), quando você escolhe falar conosco por lá;
- autoridades públicas, quando a lei exigir.
Alguns desses fornecedores podem armazenar dados fora do Brasil. Nesses casos, a transferência segue as regras do art. 33 da LGPD.

**H2 6. Cookies**
- **Necessários:** fazem o site e os formulários funcionarem. Não dependem de consentimento.
- **Medição:** contam visitas e cliques de forma agregada. Só são ativados se você aceitar no aviso de cookies.
Você pode mudar a sua escolha a qualquer momento em "Preferências de cookies", no rodapé do site, ou nas configurações do seu navegador.

**H2 7. Por quanto tempo guardamos**
- Pedidos de orçamento que não viram contrato: [INSERIR DADO REAL: prazo, ex. até 2 anos] após o último contato.
- Dados de clientes: pelo tempo do contrato e pelos prazos exigidos em lei.
- Dados de navegação: pelo prazo configurado na ferramenta de medição [INSERIR DADO REAL: ex. 14 meses].
Depois disso, os dados são apagados ou tornados anônimos.

**H2 8. Como protegemos**
Usamos conexão segura (HTTPS), acesso restrito aos dados e fornecedores com práticas de segurança reconhecidas. Nenhum sistema é totalmente imune a falhas; se houver um incidente que traga risco a você, avisaremos você e a Autoridade Nacional de Proteção de Dados (ANPD), como manda a lei.

**H2 9. Seus direitos**
Pela LGPD (art. 18), você pode pedir, a qualquer momento:
- confirmação de que tratamos seus dados e acesso a eles;
- correção de dados incompletos ou desatualizados;
- anonimização, bloqueio ou eliminação de dados desnecessários;
- portabilidade;
- informação sobre com quem compartilhamos;
- revogação do consentimento e eliminação dos dados tratados com base nele.
Para isso, escreva para o contato da seção 10. Respondemos [INSERIR DADO REAL: prazo, ex. em até 15 dias]. Você também pode reclamar à ANPD.

**H2 10. Contato do encarregado**
Encarregado pelo tratamento de dados: [INSERIR DADO REAL: nome]
E-mail: [INSERIR DADO REAL: e-mail para privacidade; se não houver, `carlos@intrepidaengenharia.com.br`]
Endereço: Rua dos Goitacazes, 103, salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910.

**H2 11. Alterações**
Podemos atualizar esta política. A data da última versão fica sempre no topo da página.

**CTA final:** `Dúvidas sobre seus dados? Fale com a gente.` → `/contato/`

---

## 15. Antes → depois (principais mudanças em relação ao site antigo)

Textos do site antigo conforme registrados no briefing [SITE-2025]. O site está fora do ar; algumas frases antigas estão resumidas, porque o briefing registrou o sentido, não a frase completa.

| # | Antes (site antigo) | Depois (novo site) | Por quê |
|---|---|---|---|
| 1 | `<title>` "Intrépida Engenharia – Intrepida Engenharia" | `Projetos de instalações prediais e BIM em BH \| Intrépida` | Título redundante, sem serviço nem cidade. O novo traz a palavra-chave e a cidade. |
| 2 | Hero com texto longo em H2 e botão "Saiba mais" (→ Serviços); página sem H1 | H1 `Projetos de instalações e infraestrutura para incorporadoras e construtoras` + subtítulo de benefício + `Solicitar orçamento` e `Falar no WhatsApp` | O visitante entende em 5 segundos o que é e para quem é, e o CTA principal leva à conversão, não a outra página. |
| 3 | "Excelência em construção civil" / "Soluções completas em construção civil, do planejamento à execução" | `Uma empresa de projetos, feita para quem constrói` + `Não executamos obras: entregamos o projeto de que a sua obra precisa.` + FAQ `A Intrépida executa a obra?` | A empresa faz projetos. O texto antigo sugeria construtora e atraía o contato errado. "Excelência" é adjetivo sem prova. |
| 4 | Menu: Home · Serviços · Quem Somos · Projetos Executados · Clientes · Contato | `Serviços` · `BIM` · `Projetos` · `Sobre` · `Contato` + `Solicitar orçamento` | "Projetos Executados" era ambíguo (parecia obra executada). BIM ganha destaque como diferencial; Clientes vira prova dentro de Projetos. |
| 5 | Mensagem das concessionárias no meio da home, com botão "Saiba Mais" apontando para `#` | H2 `A aprovação na concessionária está travando o seu cronograma?` + bullets + `Enviar meu projeto para análise` (→ `/contato/`) | A mensagem de maior valor vira seção própria, com a dor no título e um CTA que funciona. |
| 6 | 9 ícones de serviço com link para pastas do Google Drive (404) | 9 páginas próprias com H1, entregáveis, normas, FAQ e CTA `Solicitar orçamento de [disciplina]` | O usuário não sai do site nem cai em erro, e cada serviço passa a ranquear no Google. |
| 7 | "Fale conosco" (WhatsApp sem mensagem) | `Falar no WhatsApp` com mensagem pré-preenchida por página | Verbo de ação claro e contexto na primeira mensagem, o que poupa uma troca de perguntas. |
| 8 | Cards "Empreendimento: X" em H2, "Proprietário :" | Card com H3 `[Nome]`, linha `[Cliente] · [Cidade/UF]` e `[n] unidades`; rótulo `Cliente` | Hierarquia correta (um H1, H2 por seção) e leitura rápida. "Cliente" é o termo do mercado. |
| 9 | "construindo o futuro", "soluções inteligentes" | Benefícios verificáveis: `Interferências entre disciplinas resolvidas antes da obra`, `Quantitativos de materiais extraídos do modelo` | Jargão genérico não diferencia. O mecanismo concreto convence o engenheiro. |
| 10 | "Projeto entregue no prazo", "redução de custos" (promessas soltas) | Prazo tratado com honestidade: `O prazo de cada etapa vem descrito na proposta`; custo explicado pelo mecanismo (conflito resolvido no modelo) | Promessa sem prova gera desconfiança. Prazos numéricos só entram quando o cliente confirmar. |
| 11 | "Nossos Clientes" com 24 logos sem nome e com `alt=""` | H2 `Quem já contratou nossos projetos` + `alt` com o nome de cada cliente | Prova social legível para o Google e para leitores de tela. |
| 12 | Sem números de impacto | Barra: `24` clientes · `18` empreendimentos · `6` estados · `+5.800` unidades [DERIVADO DO PORTFÓLIO — conferir] | Prova de escala acima da dobra, só com contagens reais do material. |
| 13 | Link de e-mail com `mailto:` errado; texto exibia carlos@intrepidaengenharia.com.br | `mailto:carlos@intrepidaengenharia.com.br` em todo o site | Leads iam para um endereço de terceiros. |
| 14 | "elo Horizonte", "Garantimos  o" (espaço duplo), "Proprietário :" | `Belo Horizonte`, revisão completa | Erros de digitação tiram credibilidade de quem vende precisão técnica. |
| 15 | "© 2024" fixo | `© 2026` dinâmico | Evita parecer site abandonado. |
| 16 | Sem formulário estruturado nem política de privacidade | Formulário em 3 etapas com microcopy completa + consentimento LGPD + minuta de política | Pedido qualificado (dados suficientes para a proposta) e conformidade com a LGPD. |
| 17 | Todas as imagens com `alt=""` | Alt descritivo com empreendimento, cliente e cidade | Acessibilidade e SEO de imagem. |

---

## 16. Quadro de SEO (conferência rápida para o QA)

Limites: title ≤ 60 caracteres; meta description ≤ 155. Contagem feita por script sobre o texto final deste documento (com espaços). Os 18 projetos estão na tabela 8.2: titles de 41 a 57 caracteres e metas de 116 a 134.

| Slug | Title | Caract. title | Caract. meta | Palavra-chave principal |
|---|---|---|---|---|
| `/` | Projetos de instalações prediais e BIM em BH \| Intrépida | 56 | 145 | projetos de instalações prediais |
| `/servicos/` | Projetos de instalações prediais em BH \| Intrépida | 50 | 148 | projetos de instalações prediais BH |
| `/servicos/projeto-hidrossanitario/` | Projeto hidrossanitário em BH \| Intrépida Engenharia | 52 | 142 | projeto hidrossanitário |
| `/servicos/projeto-eletrico/` | Projeto elétrico e de sistemas em BH \| Intrépida | 48 | 153 | projeto elétrico predial |
| `/servicos/projeto-de-gas/` | Projeto de gás natural e GLP em BH \| Intrépida | 46 | 150 | projeto de gás |
| `/servicos/climatizacao-hvac/` | Projeto de climatização HVAC em BH \| Intrépida | 46 | 150 | projeto de climatização |
| `/servicos/pressurizacao-de-escadas/` | Projeto de pressurização de escadas \| Intrépida | 47 | 151 | projeto de pressurização de escadas |
| `/servicos/projeto-de-piscina/` | Projeto de piscina para condomínios e casas \| Intrépida | 55 | 139 | projeto hidráulico de piscina |
| `/servicos/infraestrutura-de-saneamento/` | Projeto de infraestrutura de saneamento \| Intrépida | 51 | 147 | projeto de infraestrutura de saneamento |
| `/servicos/reuso-de-agua-pluvial/` | Projeto de aproveitamento de água de chuva \| Intrépida | 54 | 152 | projeto de aproveitamento de água de chuva |
| `/servicos/aquecimento-solar/` | Projeto de aquecimento solar de água \| Intrépida | 48 | 153 | projeto de aquecimento solar |
| `/bim-e-compatibilizacao/` | BIM e compatibilização de projetos \| Intrépida | 46 | 152 | compatibilização de projetos BIM |
| `/projetos/` | Projetos em 18 empreendimentos de 6 estados \| Intrépida | 55 | 142 | portfólio de projetos de instalações |
| `/sobre/` | Sobre a Intrépida Engenharia e Projetos \| BH | 44 | 148 | Intrépida Engenharia e Projetos |
| `/contato/` | Solicite orçamento de projeto de instalações \| Intrépida | 56 | 140 | orçamento de projeto de instalações |
| `/obrigado/` | Pedido recebido \| Intrépida Engenharia | 38 | 127 | — |
| `/404` | Página não encontrada \| Intrépida Engenharia | 44 | — | — |
| `/politica-de-privacidade/` | Política de privacidade \| Intrépida Engenharia | 46 | 132 | — |

Notas de SEO técnico para o designer/QA:
- Open Graph: `og:title` = title da página; `og:description` = meta description; `og:image` = foto do hero (projetos) ou foto do Mirante São Lucas (demais páginas).
- Schema: FAQPage nas FAQs (H-12, SV-08, BM-09, CT-04); BreadcrumbList; ProfessionalService/LocalBusiness com o endereço e os telefones deste documento.
- Um H1 por página, exatamente como escrito aqui.

---

## 17. Propostas de ajuste à estrutura (para o coordenador aprovar; nada foi imposto)

| # | Onde | Proposta | Motivo |
|---|---|---|---|
| 1 | Home H-12 | 6ª pergunta: `A Intrépida executa a obra?` | O site antigo falava em "execução"; a FAQ desfaz a confusão. Sai sem prejuízo se preferirem 5. |
| 2 | Projeto PP-02/PP-03 | Parágrafo de abertura de 2 frases com os dados reais (modelo em 8.0) | Sem ele, as 18 páginas teriam só uma ficha, conteúdo raso para o Google. |
| 3 | Rótulo do "24" (H-02, H-03, H-04, PJ-06, SB-03) | `24 clientes, entre construtoras e incorporadoras` | Center Norte, CTE e Chandon não parecem construtoras/incorporadoras. Volta ao rótulo original se o cliente confirmar. |
| 4 | Barra de números (C05) | 4 itens (24 · 18 · 6 · +5.800), sem "anos de mercado" | Decisão do usuário; 4 itens fecham a grade 2×2 do mobile. |
| 5 | SV-05 em HVAC, piscina e pressurização | H2 adaptado (`Normas e integração com outras disciplinas`, `Normas e segurança`) | Essas disciplinas não passam por concessionária; o título genérico prometeria algo que não existe. |
| 6 | SV-04 em pressurização | 3º card `Fase certa` no lugar de "Loteamento" | Pressurização não se aplica a loteamento. |
| 7 | SV-06 em saneamento | `Redes compatibilizadas com o empreendimento` em vez de "em BIM" | Não está confirmado que a infraestrutura é modelada em BIM. |
| 8 | SV-09 em saneamento | Listar disciplinas de outros grupos | O grupo Infraestrutura urbana tem um só serviço. |
| 9 | SH-05 | Foto do Bosque dos Ipês (em obra) em vez do Parque Lagoa dos Príncipes | Comunica infraestrutura melhor. Decisão do designer. |
| 10 | Formulário C21a, Formato | `BIM (modelo 3D)` em vez de `BIM (Revit/IFC)` | Softwares e formatos ainda não confirmados. |
| 11 | Drawer mobile | Item `BIM e compatibilização` (nome completo) | Há espaço e fica mais claro que só "BIM". |
| 12 | Rodapé e banner C23 | Link `Preferências de cookies` | Permite revogar o consentimento, como pede a LGPD. |
| 13 | BM-07 | Comparativo 2D x BIM **entra** | Ver justificativa em BM-07. |

---

## 18. Resumo e pendências

### 18.1 O que foi escrito
- **Globais:** header, mega-menu, drawer mobile, breadcrumb, rodapé, C19, C20, banner de cookies e 11 mensagens de WhatsApp pré-preenchidas.
- **Home:** 12 seções (H-02 a H-13), com FAQ de 6 perguntas e formulário curto.
- **Serviços:** hub completo (SH-02 a SH-11, com o bloco "Não sabe quais projetos precisa?") e **9 páginas de serviço com texto completo**: hero, entregáveis, para quem/quando, normas e aprovações, BIM, FAQ de 4 ou 5 perguntas, outros serviços e CTA final.
- **BIM e compatibilização:** página completa, com comparativo 2D x BIM, galeria das 8 imagens e FAQ.
- **Projetos:** listagem com filtros, estados vazios e clientes; **18 projetos** com H1, linha, parágrafo de abertura, ficha, relacionados, title, meta e alt.
- **Sobre**, **Contato** (formulário em 3 etapas e formulário curto, com labels, placeholders, ajudas, opções, erros, estados de envio, sucesso e falha), **Obrigado**, **404** e **minuta de Política de Privacidade** (validar com o cliente/jurídico).
- **SEO** de todas as páginas, alt de 12 fotos, 8 imagens BIM, 24 logos e da marca; tabela antes → depois.

### 18.2 Depende do cliente (por impacto)
**Bloqueiam texto publicado hoje com fallback (o site sai sem eles, mas mais fraco):**
1. **Prazo de resposta ao orçamento** — H-09, H-13, CT-02, CT-04, `/obrigado/`.
2. **Concessionárias em que já aprovaram projetos** e se a Intrépida protocola e acompanha a aprovação — H-06 (selos), SV-05 e SV-08 de cada serviço.
3. **Softwares, formatos BIM e uso do template do cliente** — H-12 (pergunta 4), BM-06, BM-09.
4. **Etapas reais do processo** e se há acompanhamento de obra — H-09, BM-04, SB-07.
5. **Disciplinas projetadas em cada empreendimento** — tags dos cards, PP-03, SV-07, filtro "Disciplina".
6. **Validação técnica do RT** dos blocos [VALIDAR COM O RT]: entregáveis, normas e respostas técnicas das 9 páginas; escopo de "Sistemas" (e se SPDA e cabeamento entram).

**Dados institucionais:**
7. Razão social, CNPJ, CREA da empresa e do RT — rodapé, H-10, SB-04, SB-08, política.
8. Horário de atendimento e se há atendimento presencial — rodapé, CT-03, CT-05.
9. URL do LinkedIn da empresa e do Carlos.
10. Portfólio PDF liberado e atualizado — rodapé, H-13, SB-02, SB-08, `/obrigado/`.
11. Ano de fundação e marcos (linha do tempo), equipe com fotos, depoimentos autorizados, cases com desafio e solução — todos CONDICIONAIS, nenhum texto inventado.

**Dados a conferir (mantidos como estavam, por decisão do usuário):**
12. **Gran Vic Gama x Alto Boa Vista (236 unidades cada).** Se Gran Vic Gama tiver menos de 162 unidades, o `+5.800` deixa de valer [DERIVADO DO PORTFÓLIO — conferir].
13. **Prix Construtora x Prix Engenharia**: a mesma empresa?
14. **Center Norte, CTE e Chandon**: atuaram como construtoras/incorporadoras? (define o rótulo do "24").
15. **Parque Lagoa dos Príncipes e Lagoa Nova**: um ou dois empreendimentos?
16. Disciplina das imagens BIM 2, 5, 6 e 8 (legendas) e se há modelos de HVAC, pressurização, piscina, reúso e solar (senão, ilustrações geradas e sinalizadas).
17. Fotos dos 6 projetos do site antigo, foto do Carlos e crédito exigido nas fotos.

**Formulário e LGPD:**
18. E-mail que recebe os leads (a copy usa carlos@intrepidaengenharia.com.br), envio de cópia ao usuário e limite de upload em MB.
19. Faixas de prazo e lista de fases do formulário; se o público de residências particulares (P4) interessa.
20. Compromisso de sigilo dos arquivos e prática de "atendimento direto com o engenheiro".
21. Política: encarregado, prazos de guarda, fornecedores e ferramentas (GA4, reCAPTCHA/Turnstile), envio de novidades.
22. Atendimento fora dos 6 estados; compatibilização de projetos de terceiros; reúso de águas cinzas.
