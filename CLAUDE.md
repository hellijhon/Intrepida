# Projeto: modernização do site da Intrépida Engenharia

- Site atual: https://intrepidaengenharia.com.br/
- Materiais da marca (Google Drive): https://drive.google.com/drive/folders/0Bw2pG3fN8vN2cWJhcnpZZGhveVE?resourcekey=0-hStuo9oWumBqDt_kmXzlxw&usp=sharing — acessar pelo conector do Google Drive (ferramentas `mcp__8611e02f-...__*`, carregar via ToolSearch).
- Imagens: autorizado gerar imagens no Magnific e em outras ferramentas quando necessário. Prioridade: fotos reais da Intrépida (site/Drive); gerar só quando não houver foto que resolva, e nunca gerar imagem que se passe por obra, equipe ou cliente real da empresa sem sinalizar.
- Não usar o conector Elementor `clt-viaja-elementor` (é de outro cliente).

## Decisões do usuário (21/11/2026)
- Briefing (`equipe/01-contexto.md`) e wireframe (`equipe/02-wireframe.md`) aprovados.
- **Plataforma: WordPress** (com Elementor, como no site antigo).
- **Endereço:** o do site antigo — Rua dos Goitacazes, 103, Salas 1604 e 1606, Centro, Belo Horizonte/MG, CEP 30190-910.
- **Números:** manter os do site antigo (unidades por projeto como estavam). Não inventar números novos (anos de mercado, m², etc.); contagens tiradas do material real (24 clientes, 18 empreendimentos, 6 UFs) podem ser usadas.
- **Números (atualizado em 23/11/2026, substitui a barra anterior):** "+24 construtoras e incorporadoras atendidas", "+18 empreendimentos no portfólio", "8 estados atendidos" (MG, DF, SP, RJ, MS, SC + **RS e PB**, que são atendidos mas não têm projeto no portfólio). O "+5.800 unidades" saiu da barra. O mapa de estados (Projetos e Sobre) é um SVG do Brasil com pins laranja, gerado por `site/_build/mapa_brasil.py` a partir da malha do IBGE. O `equipe/03-copy.md` não foi atualizado com essa mudança: o site é a referência.
- **Fotos de obras e logos de clientes:** uso liberado desde já.
- **Foto do responsável técnico:** deixar marcação/placeholder sinalizado até chegar a foto real (não gerar por IA).
- Status (21/11/2026): ciclo completo (contexto → QA) concluído; protótipo HTML em `site/` aprovado pelo QA para apresentação. Pacote para o cliente em `entrega-cliente/` (apresentação PDF, checklist de pendências PDF, protótipo .zip). Publicação no WordPress aguarda as pendências CL-01 a CL-06 de `equipe/06-qa-final.md`.
- Link de visualização para o cliente (23/11/2026): https://hellijhon.github.io/Intrepida/ — branch `gh-pages` do repositório hellijhon/Intrepida, gerada por `python3 site/_build/gerar_preview.py preview-cliente /Intrepida` (pasta `preview-cliente/` tem o próprio git, com push para `gh-pages`). Bloqueado para o Google (noindex + robots).
- Contatos: telefone (31) 3070-6568, WhatsApp (31) 99649-8629, e-mail carlos@intrepidaengenharia.com.br (com o link `mailto` corrigido).

# Equipe de criação de sites — fluxo de trabalho

Este projeto usa uma equipe de agentes (em `.claude/agents/`). O Claude principal atua como **coordenador**: recebe a tarefa, aciona cada agente na ordem, repassa o contexto e leva as decisões ao usuário.

## Ordem padrão
1. `contexto-site` → `equipe/01-contexto.md` (briefing, diagnóstico, arquitetura de informação)
2. `wireframe` → `equipe/02-wireframe.md` + `equipe/wireframes/`
3. `copywriter` → `equipe/03-copy.md`
4. `webdesigner-senior` → `equipe/04-design-system.md` + `site/` (ou Figma/Elementor)
5. `validador-ux-ui` → `equipe/05-validacao-ux-ui.md`
   - Se houver itens Críticos/Altos: devolver ao agente responsável e revalidar.
6. `revisor-qa` → `equipe/06-qa-final.md` — parecer final (PRONTO / NÃO PRONTO)

## Regras do coordenador
- Pausar para o usuário aprovar ao fim do contexto e do wireframe, antes de seguir.
- Perguntas em aberto dos agentes vão para o usuário; não inventar dados do cliente.
- Tarefas pontuais (ex.: "só reescreva a home") podem acionar apenas o agente necessário + `revisor-qa`.
- Tudo em português do Brasil.
