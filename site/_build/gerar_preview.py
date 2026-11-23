"""Gera uma cópia do site para visualização do cliente em um subcaminho
(ex.: GitHub Pages em https://usuario.github.io/intrepida-prototipo/).

- Reescreve caminhos absolutos ("/assets/...", "/contato/") para o subcaminho.
- Bloqueia indexação (meta robots noindex + robots.txt Disallow: /).
- Não altera o site/ original.

Uso: python3 gerar_preview.py <pasta-de-saida> /intrepida-prototipo
"""
import pathlib, re, shutil, sys

SITE = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]).resolve()
BASE = '/' + sys.argv[2].strip('/')

# Limpa a saída, preservando o .git do repositório de preview
OUT.mkdir(parents=True, exist_ok=True)
for item in OUT.iterdir():
    if item.name == '.git':
        continue
    shutil.rmtree(item) if item.is_dir() else item.unlink()

for src in SITE.rglob('*'):
    rel = src.relative_to(SITE)
    if rel.parts[0] == '_build' or src.name == '.DS_Store':
        continue
    dst = OUT / rel
    if src.is_dir():
        dst.mkdir(parents=True, exist_ok=True)
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.suffix in ('.html', '.js', '.css', '.webmanifest'):
        t = src.read_text(encoding='utf-8')
        if src.suffix == '.html':
            t = re.sub(r'(=")/(?!/)', r'\1' + BASE + '/', t)               # atributos href/src/action/data-*
            t = re.sub(r'(,\s*)/(?=assets/)', r'\1' + BASE + '/', t)       # demais itens de srcset
            t = re.sub(r'url\((["\']?)/(?!/)', r'url(\1' + BASE + '/', t)  # estilos inline
            t = t.replace('<head>', '<head>\n<meta name="robots" content="noindex, nofollow">', 1)
        elif src.suffix == '.js':
            t = re.sub(r'(["\'`])/(?=(assets|obrigado|contato|servicos|projetos|sobre|bim-e-compatibilizacao)/)', r'\1' + BASE + '/', t)
        elif src.suffix == '.css':
            t = re.sub(r'url\((["\']?)/(?!/)', r'url(\1' + BASE + '/', t)
        else:
            t = t.replace('"/assets/', '"' + BASE + '/assets/')
        dst.write_text(t, encoding='utf-8')
    else:
        shutil.copy2(src, dst)

(OUT / 'robots.txt').write_text('User-agent: *\nDisallow: /\n', encoding='utf-8')
(OUT / '.nojekyll').write_text('', encoding='utf-8')
(OUT / 'README.md').write_text(
    '# Intrépida Engenharia — protótipo do novo site\n\n'
    'Versão de visualização para aprovação. Não é o site oficial: os formulários não enviam '
    'mensagens e os selos amarelos marcam informações pendentes.\n', encoding='utf-8')
print('preview gerado em', OUT, 'com base', BASE)
