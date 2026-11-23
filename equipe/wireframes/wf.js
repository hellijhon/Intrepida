// Interações mínimas do wireframe (notas, menu mobile, filtros).
(function () {
  var body = document.body;
  try { if (localStorage.getItem('wf-notes') === 'off') body.classList.add('no-notes'); } catch (e) {}
  var t = document.getElementById('toggle-notes');
  function label() { if (t) t.textContent = body.classList.contains('no-notes') ? 'Mostrar notas' : 'Ocultar notas'; }
  label();
  if (t) t.addEventListener('click', function () {
    body.classList.toggle('no-notes'); label();
    try { localStorage.setItem('wf-notes', body.classList.contains('no-notes') ? 'off' : 'on'); } catch (e) {}
  });

  var drawer = document.getElementById('drawer');
  var openBtn = document.getElementById('open-menu');
  var closeBtn = document.getElementById('close-menu');
  function setMenu(open) {
    if (!drawer) return;
    drawer.classList.toggle('open', open);
    drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
    if (openBtn) openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open && closeBtn) closeBtn.focus(); else if (openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener('click', function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener('click', function () { setMenu(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) setMenu(false); });

  var fBtn = document.getElementById('open-filters');
  var sheet = document.getElementById('filter-sheet');
  if (fBtn && sheet) fBtn.addEventListener('click', function () {
    var open = sheet.hasAttribute('hidden');
    if (open) sheet.removeAttribute('hidden'); else sheet.setAttribute('hidden', '');
    fBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  // C20: aparece depois que o hero sai da tela
  var mbar = document.querySelector('.mbar');
  var hero = document.querySelector('main section');
  if (mbar && hero) {
    var upd = function () { mbar.classList.toggle('hidden', window.scrollY < hero.offsetTop + hero.offsetHeight - 200); };
    upd(); window.addEventListener('scroll', upd, { passive: true });
  }
})();
