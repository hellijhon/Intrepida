# Novo site — Intrépida Engenharia e Projetos

Modernização do site [intrepidaengenharia.com.br](https://intrepidaengenharia.com.br/), feita por uma equipe de agentes do Claude Code (`.claude/agents/`).

## Estrutura
- `CLAUDE.md` — decisões do projeto e fluxo da equipe.
- `equipe/` — entregáveis de cada etapa: contexto (01), wireframe (02), copy (03), design system e guia de migração para Elementor (04), validação UX/UI (05) e QA final (06), além de fotos, marca e screenshots.
- `site/` — protótipo HTML/CSS/JS de alta fidelidade (36 páginas). As páginas são geradas por `site/_build/build.py`.
- `entrega-cliente/` — apresentação e checklist de pendências em PDF.

## Ver o protótipo localmente
```bash
cd site && python3 -m http.server 8000
```
Acesse http://localhost:8000.

## Status
Protótipo aprovado no QA para apresentação ao cliente. A publicação em WordPress + Elementor aguarda as pendências do cliente (CL-01 a CL-06 em `equipe/06-qa-final.md`).
