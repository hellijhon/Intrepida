/* Intrépida — site.js (sem dependências). Cada bloco corresponde a um componente Cxx. */
(function () {
  'use strict';
  var d = document, w = window, html = d.documentElement;
  html.classList.remove('no-js');
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var mqDesk = w.matchMedia('(min-width: 1025px)');
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var store = {
    get: function (k) { try { return w.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { w.localStorage.setItem(k, v); } catch (e) {} },
    sget: function (k) { try { return w.sessionStorage.getItem(k); } catch (e) { return null; } },
    sset: function (k, v) { try { w.sessionStorage.setItem(k, v); } catch (e) {} }
  };
  function track(ev, params) { /* Ponto de integração GA4/GTM (só após consentimento de medição). */
    w.dataLayer = w.dataLayer || []; w.dataLayer.push(Object.assign({ event: ev }, params || {}));
  }
  var live = $('#live-region');
  function announce(msg) { if (!live) return; live.textContent = ''; setTimeout(function () { live.textContent = msg; }, 60); }

  /* Rodapé: colunas abertas a partir do tablet, accordions no mobile */
  var mqTab = w.matchMedia('(min-width: 768px)');
  function syncFooter() { $$('[data-open-desktop]').forEach(function (el) { el.open = mqTab.matches; }); }
  syncFooter(); mqTab.addEventListener('change', syncFooter);
  /* Ano dinâmico no rodapé */
  $$('[data-ano]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- C01 Header: compacto no scroll ---------- */
  var header = $('.c01-header');
  function onScroll() { if (header) header.classList.toggle('is-compact', w.scrollY > 80); }
  w.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Mega-menu: hover + clique/Enter, Esc fecha */
  $$('.has-mega').forEach(function (li) {
    var btn = $('.c01-nav__top', li), t;
    function open(v) { li.classList.toggle('is-open', v); btn.setAttribute('aria-expanded', v ? 'true' : 'false'); }
    li.addEventListener('mouseenter', function () { if (mqDesk.matches) { clearTimeout(t); open(true); } });
    li.addEventListener('mouseleave', function () { if (mqDesk.matches) { t = setTimeout(function () { open(false); }, 160); } });
    btn.addEventListener('click', function (e) {
      if (li.classList.contains('is-open') && e.detail === 0) { open(false); return; }
      if (!li.classList.contains('is-open')) { e.preventDefault(); open(true); var f = $('.c01-mega a', li); if (e.detail === 0 && f) f.focus(); }
      else if (e.detail > 0) { /* segundo clique segue o link do hub */ }
    });
    li.addEventListener('keydown', function (e) { if (e.key === 'Escape') { open(false); btn.focus(); } });
    li.addEventListener('focusout', function (e) { if (!li.contains(e.relatedTarget)) open(false); });
  });

  /* Drawer mobile com foco preso */
  var drawer = $('.c01-drawer'), burger = $('.c01-burger');
  function trap(container, e) {
    var f = $$('a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])', container).filter(function (x) { return x.offsetParent !== null; });
    if (!f.length) return; var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && d.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
  }
  function setDrawer(v) {
    if (!drawer) return;
    drawer.classList.toggle('is-open', v); drawer.setAttribute('aria-hidden', v ? 'false' : 'true');
    burger.setAttribute('aria-expanded', v ? 'true' : 'false'); d.body.classList.toggle('no-scroll', v);
    if (v) { setTimeout(function () { $('.c01-drawer__close', drawer).focus(); }, 50); } else { burger.focus(); }
  }
  if (drawer && burger) {
    burger.addEventListener('click', function () { setDrawer(true); });
    $$('[data-close-drawer]', drawer).forEach(function (b) { b.addEventListener('click', function () { setDrawer(false); }); });
    drawer.addEventListener('keydown', function (e) { if (e.key === 'Escape') setDrawer(false); if (e.key === 'Tab') trap(drawer, e); });
    $$('.acc', drawer).forEach(function (b) {
      b.addEventListener('click', function () {
        var p = d.getElementById(b.getAttribute('aria-controls')); var v = b.getAttribute('aria-expanded') !== 'true';
        b.setAttribute('aria-expanded', v); p.hidden = !v;
      });
    });
    mqDesk.addEventListener('change', function (m) { if (m.matches && drawer.classList.contains('is-open')) setDrawer(false); });
  }

  /* ---------- C19 / C20 ---------- */
  var c20 = $('.c20-bar'), c19 = $('.c19-wa'), hero = $('[data-hero]'), footer = $('.c02-footer');
  if ('IntersectionObserver' in w) {
    if (c20) {
      if (hero) new IntersectionObserver(function (en) { c20.classList.toggle('is-visible', !en[0].isIntersecting); }).observe(hero);
      else c20.classList.add('is-visible');
    }
    if (c19 && footer) new IntersectionObserver(function (en) { c19.classList.toggle('is-hidden', en[0].isIntersecting); }).observe(footer);
  } else if (c20) c20.classList.add('is-visible');
  if (c20) { /* some com teclado aberto (foco em campo) */
    d.addEventListener('focusin', function (e) { if (e.target.matches('input, textarea, select')) c20.style.display = 'none'; });
    d.addEventListener('focusout', function (e) { if (e.target.matches('input, textarea, select')) c20.style.display = ''; });
  }

  /* Eventos de conversão */
  d.addEventListener('click', function (e) {
    var a = e.target.closest('a'); if (!a) return;
    var h = a.getAttribute('href') || '';
    if (h.indexOf('wa.me') > -1) track('whatsapp_click', { pagina: d.title });
    else if (h.indexOf('tel:') === 0) track('tel_click');
    else if (h.indexOf('mailto:') === 0) track('email_click');
  });

  /* ---------- Reveal ---------- */
  if (!reduce && 'IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('is-in'); io.unobserve(x.target); } }); }, { rootMargin: '0px 0px -8% 0px' });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });

  /* ---------- C11 Galeria + lightbox ---------- */
  var lb = $('.lightbox');
  if (lb) {
    var items = [], idx = 0, lastFocus;
    var img = $('img', lb), cap = $('figcaption', lb), cnt = $('.lightbox__count', lb);
    function show(i) {
      idx = (i + items.length) % items.length; var it = items[idx];
      img.src = it.src; img.alt = it.alt; cap.textContent = it.cap;
      cnt.textContent = 'Imagem ' + (idx + 1) + ' de ' + items.length;
    }
    function openLb(group, i) {
      items = $$('[data-lb="' + group + '"]').map(function (b) { return { src: b.dataset.full, alt: b.dataset.alt, cap: b.dataset.cap }; });
      lastFocus = d.activeElement; lb.classList.add('is-open'); lb.setAttribute('aria-hidden', 'false'); d.body.classList.add('no-scroll');
      show(i); $('[data-lb-close]', lb).focus();
    }
    function closeLb() { lb.classList.remove('is-open'); lb.setAttribute('aria-hidden', 'true'); d.body.classList.remove('no-scroll'); if (lastFocus) lastFocus.focus(); }
    $$('[data-lb]').forEach(function (b) {
      b.addEventListener('click', function () { var g = b.dataset.lb; openLb(g, $$('[data-lb="' + g + '"]').indexOf(b)); });
    });
    $('[data-lb-close]', lb).addEventListener('click', closeLb);
    $('[data-lb-prev]', lb).addEventListener('click', function () { show(idx - 1); });
    $('[data-lb-next]', lb).addEventListener('click', function () { show(idx + 1); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeLb(); else if (e.key === 'ArrowLeft') show(idx - 1); else if (e.key === 'ArrowRight') show(idx + 1); else if (e.key === 'Tab') trap(lb, e);
    });
    var sx = null;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { if (sx === null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); sx = null; });
  }
  /* indicador de páginas do carrossel mobile */
  $$('[data-dots]').forEach(function (dots) {
    var list = d.getElementById(dots.dataset.dots); if (!list) return;
    var n = list.children.length; dots.innerHTML = new Array(n + 1).join('<span></span>');
    function upd() { var i = Math.round(list.scrollLeft / (list.children[0].offsetWidth + 12)); $$('span', dots).forEach(function (s, k) { s.classList.toggle('on', k === Math.min(i, n - 1)); }); }
    list.addEventListener('scroll', upd, { passive: true }); upd();
  });

  /* ---------- C22 Filtros de projetos ---------- */
  var grid = $('#pj-grid');
  if (grid) {
    var cards = $$('li[data-uf]', grid), selUf = $('#f-uf'), selCli = $('#f-cliente'), busca = $('#f-busca');
    var countEl = $('#pj-count'), vazio = $('#pj-vazio'), ativos = $('#pj-ativos'), btnF = $('#btn-filtrar');
    var sheet = $('.c22-sheet'), verBtn = $('#pj-ver'), noCli = $('#f-busca-vazio');
    var UFN = { MG: 'Minas Gerais', DF: 'Distrito Federal', SP: 'São Paulo', RJ: 'Rio de Janeiro', MS: 'Mato Grosso do Sul', SC: 'Santa Catarina' };
    function txtN(n) { return n === 0 ? 'Nenhum projeto' : n === 1 ? '1 projeto' : n + ' projetos'; }
    $$('option', selUf).concat($$('option', selCli)).forEach(function (o) { if (o.value) o.dataset.base = o.textContent.replace(/\s*\(\d+\)$/, ''); });
    function contar(uf, cli) { return cards.filter(function (c) { return (!uf || c.dataset.uf === uf) && (!cli || c.dataset.cliente === cli); }).length; }
    function apply(push) {
      var uf = selUf.value, cli = selCli.value, n = 0;
      $$('option', selUf).forEach(function (o) { if (!o.value) return; var k = contar(o.value, cli); o.textContent = o.dataset.base + ' (' + k + ')'; o.disabled = k === 0 && o.value !== uf; });
      $$('option', selCli).forEach(function (o) { if (!o.value) return; var k = contar(uf, o.value); o.textContent = o.dataset.base + ' (' + k + ')'; o.disabled = k === 0 && o.value !== cli; });
      cards.forEach(function (c) { var ok = (!uf || c.dataset.uf === uf) && (!cli || c.dataset.cliente === cli); c.hidden = !ok; if (ok) n++; });
      countEl.textContent = txtN(n); vazio.hidden = n !== 0; grid.hidden = n === 0;
      if (verBtn) verBtn.textContent = n === 1 ? 'Ver 1 projeto' : 'Ver ' + n + ' projetos';
      var act = (uf ? 1 : 0) + (cli ? 1 : 0);
      if (btnF) $('span', btnF).textContent = act ? 'Filtrar (' + act + ')' : 'Filtrar';
      ativos.innerHTML = '';
      [[uf, 'uf', UFN[uf], uf], [cli, 'cliente', cli, cli]].forEach(function (f) {
        if (!f[0]) return; var b = d.createElement('button'); b.type = 'button'; b.className = 'chip';
        b.setAttribute('aria-label', f[3] + ', remover filtro: ' + f[2]); b.innerHTML = f[3] + ' <svg class="icon" aria-hidden="true"><use href="/Intrepida/assets/img/icons.svg#i-close"/></svg>';
        b.addEventListener('click', function () { (f[1] === 'uf' ? selUf : selCli).value = ''; apply(true); countEl.focus(); });
        ativos.appendChild(b);
      });
      if (push) { var p = new URLSearchParams(); if (uf) p.set('uf', uf.toLowerCase()); if (cli) p.set('cliente', cli); history.replaceState(null, '', location.pathname + (p.toString() ? '?' + p : '') + location.hash); }
    }
    var q = new URLSearchParams(location.search);
    if (q.get('uf')) selUf.value = q.get('uf').toUpperCase();
    if (q.get('cliente')) { $$('option', selCli).forEach(function (o) { if (o.value.toLowerCase() === q.get('cliente').toLowerCase()) selCli.value = o.value; }); }
    selUf.addEventListener('change', function () { apply(true); });
    selCli.addEventListener('change', function () { apply(true); });
    if (busca) busca.addEventListener('input', function () {
      var t = busca.value.trim().toLowerCase(), vis = 0;
      $$('option', selCli).forEach(function (o, i) { if (!i) return; var ok = o.textContent.toLowerCase().indexOf(t) > -1; o.hidden = !ok; if (ok) vis++; });
      noCli.hidden = vis !== 0;
    });
    $$('[data-limpar]').forEach(function (b) { b.addEventListener('click', function () { selUf.value = ''; selCli.value = ''; if (busca) { busca.value = ''; busca.dispatchEvent(new Event('input')); } apply(true); }); });
    $$('[data-uf-go]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); selUf.value = b.dataset.ufGo; selCli.value = ''; apply(true); $('#pj-05').scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }); countEl.focus({ preventScroll: true }); }); });
    function setSheet(v) { sheet.classList.toggle('is-open', v); btnF.setAttribute('aria-expanded', v); d.body.classList.toggle('no-scroll', v); if (v) $('#f-uf').focus(); else btnF.focus(); }
    if (btnF) btnF.addEventListener('click', function () { setSheet(true); });
    $$('[data-sheet-close]').forEach(function (b) { b.addEventListener('click', function () { setSheet(false); }); });
    if (sheet) sheet.addEventListener('keydown', function (e) { if (e.key === 'Escape' && sheet.classList.contains('is-open')) setSheet(false); });
    apply(false);
  }

  /* ---------- C21 Formulários ---------- */
  var RX_MAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
  function maskTel(el) {
    el.addEventListener('input', function () {
      var v = el.value.replace(/\D/g, '').slice(0, 11), o = v;
      if (v.length > 2) o = '(' + v.slice(0, 2) + ') ' + v.slice(2);
      if (v.length > 6) o = '(' + v.slice(0, 2) + ') ' + v.slice(2, v.length === 11 ? 7 : 6) + '-' + v.slice(v.length === 11 ? 7 : 6);
      el.value = o;
    });
  }
  $$('input[type="tel"]').forEach(maskTel);
  function fieldOf(el) { return el.closest('.field') || el.closest('fieldset') || el.parentNode; }
  function errOf(el) {
    var e = $('.err', fieldOf(el)); if (!e) return null;
    if (!e.id) e.id = (el.id || el.name) + '-erro';
    return e;
  }
  function describe(el, id, on) {
    var ids = (el.getAttribute('aria-describedby') || '').split(' ').filter(function (x) { return x && x !== id; });
    if (on) ids.push(id);
    if (ids.length) el.setAttribute('aria-describedby', ids.join(' ')); else el.removeAttribute('aria-describedby');
  }
  function setErr(el, msg) {
    var f = fieldOf(el), e = errOf(el);
    var alvos = el.type === 'radio' ? $$('input[name="' + el.name + '"]', el.form) : [el];
    if (msg) { f.classList.add('has-error'); if (e) e.lastChild.textContent = msg; }
    else { f.classList.remove('has-error'); if (e) e.lastChild.textContent = ''; }
    alvos.forEach(function (x) { if (msg) x.setAttribute('aria-invalid', 'true'); else x.removeAttribute('aria-invalid'); if (e) describe(x, e.id, !!msg); });
  }
  function validate(el) {
    if (el.closest('.cond[hidden]') || el.disabled) { setErr(el, ''); return ''; }
    var v = (el.value || '').trim(), m = el.dataset, msg = '';
    if (el.type === 'checkbox' && m.req) msg = el.checked ? '' : m.req;
    else if (el.type === 'radio') { var g = $$('input[name="' + el.name + '"]', el.form); msg = g.some(function (r) { return r.checked; }) ? '' : (m.req || ''); }
    else if (m.req && !v) msg = m.req;
    else if (v && el.type === 'email' && !RX_MAIL.test(v)) msg = m.fmt;
    else if (v && el.type === 'tel' && v.replace(/\D/g, '').length < 10) msg = m.fmt;
    else if (v && m.num && !/^\d+$/.test(v.replace(/\./g, ''))) msg = m.num;
    else if (v && el.type === 'url' && !/^https?:\/\/\S+\.\S+/i.test(v)) msg = m.fmt;
    else if (v && m.maxlen && v.length > +m.maxlen) msg = m.max;
    setErr(el, msg); return msg;
  }
  function fieldsIn(scope) {
    var seen = {};
    return $$('input, select, textarea', scope).filter(function (el) {
      if (el.type === 'hidden' || el.classList.contains('hp') || el.type === 'file') return false;
      if (el.type === 'radio') { if (seen[el.name]) return false; seen[el.name] = 1; }
      return el.dataset.req || el.dataset.fmt || el.dataset.num || el.dataset.max;
    });
  }
  function runValidation(scope, summary) {
    var errs = [];
    fieldsIn(scope).forEach(function (el) {
      var msg;
      if (el.dataset.group) { msg = groupCheck(el); } else msg = validate(el);
      if (msg) errs.push({ el: el, msg: msg });
    });
    if (summary) {
      if (errs.length) {
        $('h3', summary).textContent = errs.length === 1 ? 'Revise 1 campo para continuar:' : 'Revise ' + errs.length + ' campos para continuar:';
        var ul = $('ul', summary); ul.innerHTML = '';
        errs.forEach(function (x) { var li = d.createElement('li'), a = d.createElement('a'); a.href = '#' + x.el.id; a.textContent = x.msg; a.addEventListener('click', function (e) { e.preventDefault(); x.el.focus(); }); li.appendChild(a); ul.appendChild(li); });
        summary.classList.add('is-visible');
      } else summary.classList.remove('is-visible');
    }
    if (errs.length) { errs[0].el.focus(); }
    return errs.length === 0;
  }
  function groupCheck(el) { /* grupo de checkboxes de disciplinas */
    var box = el.closest('[data-checkgroup]'), any = $$('input[type="checkbox"]', box).some(function (c) { return c.checked; });
    var msg = any ? '' : el.dataset.req, err = $(':scope > .err', box);
    box.classList.toggle('has-error', !!msg);
    if (err) { if (!err.id) err.id = 'disciplinas-erro'; err.lastChild.textContent = msg || ''; }
    $$('input[type="checkbox"]', box).forEach(function (c) { if (msg) c.setAttribute('aria-invalid', 'true'); else c.removeAttribute('aria-invalid'); });
    if (msg && err) box.setAttribute('aria-describedby', err.id); else box.removeAttribute('aria-describedby');
    return msg;
  }
  $$('form[data-form]').forEach(function (form) {
    form.setAttribute('novalidate', '');
    $$('[data-req]', form).forEach(function (el) {
      if (el.dataset.group) { var g = el.closest('[data-checkgroup]'); if (g) g.setAttribute('aria-required', 'true'); }
      else if (el.type === 'radio') { $$('input[name="' + el.name + '"]', form).forEach(function (r) { r.required = true; }); }
      else el.required = true;
    });
    $$('input[type="url"]', form).forEach(function (u) {
      u.addEventListener('blur', function () { var v = u.value.trim(); if (v && !/^https?:\/\//i.test(v) && /\S+\.\S+/.test(v)) u.value = 'https://' + v; });
    });
    $$('input, select, textarea', form).forEach(function (el) {
      el.addEventListener('blur', function () { if (fieldOf(el).classList.contains('has-error') || (el.value && el.type !== 'checkbox' && el.type !== 'radio')) { if (!el.dataset.group) validate(el); } });
      el.addEventListener('change', function () { if (fieldOf(el).classList.contains('has-error')) { el.dataset.group ? groupCheck(el) : validate(el); } });
    });
    /* contador de caracteres */
    $$('[data-counter]', form).forEach(function (ta) {
      var c = d.getElementById(ta.dataset.counter), max = +ta.getAttribute('maxlength') || 1000;
      ta.removeAttribute('maxlength'); ta.dataset.maxlen = max;
      ta.addEventListener('input', function () { var n = ta.value.length; c.textContent = n.toLocaleString('pt-BR') + ' de 1.000 caracteres'; if (n > max) setErr(ta, ta.dataset.max); else setErr(ta, ''); });
    });
    /* pré-preenchimento por parâmetro (dados não pessoais) */
    var q = new URLSearchParams(location.search);
    var hs = $('input[name="servico"]', form); if (hs && q.get('servico') && !hs.value) hs.value = q.get('servico');
    var hr = $('input[name="ref"]', form); if (hr && q.get('ref')) hr.value = q.get('ref');
    var ho = $('input[name="origem"]', form); if (ho) ho.value = location.pathname;
    ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) { var h = $('input[name="' + k + '"]', form); if (h && q.get(k)) h.value = q.get(k); });
    if (q.get('servico')) { var cb = $('input[name="disciplinas"][value="' + q.get('servico') + '"]', form); if (cb) { cb.checked = true; cb.dispatchEvent(new Event('change', { bubbles: true })); } }

    var steps = $$('.step', form), cur = 0, prog = $('.progress', form);
    function goStep(i) {
      steps.forEach(function (s, k) { s.classList.toggle('is-active', k === i); });
      cur = i;
      if (prog) { $('.progress__txt', prog).textContent = steps[i].dataset.title; $$('.progress__bar span', prog).forEach(function (s, k) { s.classList.toggle('on', k <= i); }); }
      var h = $('h2', steps[i]); if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
      form.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    }
    $$('[data-next]', form).forEach(function (b) { b.addEventListener('click', function () {
      $$('input[type="url"]', steps[cur]).forEach(function (u) { var v = u.value.trim(); if (v && !/^https?:\/\//i.test(v) && /\S+\.\S+/.test(v)) u.value = 'https://' + v; }); if (runValidation(steps[cur], $('.err-summary', steps[cur]))) goStep(cur + 1); }); });
    $$('[data-prev]', form).forEach(function (b) { b.addEventListener('click', function () { goStep(cur - 1); }); });

    /* Campos condicionais (etapa 1) */
    function syncCond() {
      var t = ($('input[name="tipo"]:checked', form) || {}).value || '';
      $$('[data-show-if]', form).forEach(function (c) { var ok = c.dataset.showIf.split(' ').indexOf(t) > -1; c.hidden = !ok; });
    }
    $$('input[name="tipo"]', form).forEach(function (r) { r.addEventListener('change', function () { syncCond(); validate(r); }); });
    syncCond();
    var und = $('#c-unid-nd', form), unid = $('#c-unidades', form);
    if (und && unid) und.addEventListener('change', function () { unid.disabled = und.checked; if (und.checked) { unid.value = ''; setErr(unid, ''); } });
    /* "Ainda não sei" desmarca as outras */
    var naoSei = $('input[name="disciplinas"][value="nao-sei"]', form);
    if (naoSei) {
      var outras = $$('input[name="disciplinas"]', form).filter(function (c) { return c !== naoSei; });
      naoSei.addEventListener('change', function () { if (naoSei.checked && outras.some(function (c) { return c.checked; })) { outras.forEach(function (c) { c.checked = false; }); announce('As outras opções foram desmarcadas.'); } });
      outras.forEach(function (c) { c.addEventListener('change', function () { if (c.checked) naoSei.checked = false; }); });
    }
    /* Upload (simulado no front; tamanho máximo vem de data-max-mb) */
    var dz = $('.dropzone', form);
    if (dz) {
      var inp = $('input[type="file"]', dz), list = $('.files', form), dzErr = $('#c-arq-err', form), maxMB = +dz.dataset.maxMb || 20, files = [];
      var okExt = /\.(pdf|dwg|rvt|ifc|zip)$/i;
      function render() {
        list.innerHTML = '';
        files.forEach(function (f, i) {
          var li = d.createElement('li');
          li.innerHTML = '<svg class="icon icon--sm" aria-hidden="true"><use href="/Intrepida/assets/img/icons.svg#i-file"/></svg><span class="nm"></span><button type="button"></button>';
          $('.nm', li).textContent = f.name + ' anexado'; var b = $('button', li); b.textContent = 'Remover'; b.setAttribute('aria-label', 'Remover ' + f.name);
          b.addEventListener('click', function () { files.splice(i, 1); render(); announce(f.name + ' removido'); });
          list.appendChild(li);
        });
      }
      function add(fl) {
        var msgs = [];
        Array.prototype.forEach.call(fl, function (f) {
          if (!okExt.test(f.name)) { msgs.push('O arquivo ' + f.name + ' não é aceito. Envie PDF, DWG, RVT, IFC ou ZIP.'); return; }
          var tot = files.reduce(function (s, x) { return s + x.size; }, 0) + f.size;
          if (tot > maxMB * 1048576) { msgs.push('Os arquivos passam de ' + maxMB + ' MB. Envie pelo campo de link acima.'); return; }
          files.push(f); announce(f.name + ' anexado');
        });
        dzErr.hidden = !msgs.length; dzErr.textContent = msgs.join(' '); render();
      }
      inp.addEventListener('change', function () { add(inp.files); inp.value = ''; });
      ['dragenter', 'dragover'].forEach(function (t) { dz.addEventListener(t, function (e) { e.preventDefault(); dz.classList.add('is-over'); }); });
      ['dragleave', 'drop'].forEach(function (t) { dz.addEventListener(t, function () { dz.classList.remove('is-over'); }); });
      dz.addEventListener('drop', function (e) { e.preventDefault(); add(e.dataTransfer.files); });
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      $$('input[type="url"]', form).forEach(function (u) { var v = u.value.trim(); if (v && !/^https?:\/\//i.test(v) && /\S+\.\S+/.test(v)) u.value = 'https://' + v; });
      var scope = steps.length ? steps[cur] : form, sum = $('.err-summary', scope) || $('.err-summary', form);
      if (!runValidation(scope, sum)) return;
      if ($('.hp input', form) && $('.hp input', form).value) return; /* honeypot */
      var btn = $('button[type="submit"]', form), lbl = btn.textContent, fail = $('.form-fail', form);
      btn.disabled = true; btn.textContent = 'Enviando…'; if (fail) fail.hidden = true;
      /* ENVIO SIMULADO: no WordPress este bloco é substituído pelo envio do Elementor Pro Forms. */
      setTimeout(function () {
        if (q.get('simular') === 'falha' && fail) { fail.hidden = false; btn.disabled = false; btn.textContent = lbl; fail.focus(); return; }
        var tipo = form.dataset.form;
        track('form_submit', { form_label: tipo });
        store.sset('intrepida_form', tipo);
        location.href = '/Intrepida/obrigado/?origem=' + tipo;
      }, 900);
    });
  });

  /* /obrigado/: linha extra para quem veio do formulário curto */
  var extra = $('[data-se-rapido]');
  if (extra) { var o = new URLSearchParams(location.search).get('origem') || store.sget('intrepida_form'); extra.hidden = o !== 'orcamento_rapido'; }

  /* ---------- C23 Cookies (LGPD) ---------- */
  var ck = $('.c23-cookies');
  if (ck) {
    var KEY = 'intrepida_consent', med = $('#ck-medicao', ck), voltaFoco = null;
    function save(v) { store.set(KEY, JSON.stringify({ medicao: v, data: new Date().toISOString() })); ck.classList.remove('is-open', 'show-pref');
      var alvo = voltaFoco && d.contains(voltaFoco) ? voltaFoco : $('#conteudo'); if (alvo) alvo.focus({ preventScroll: true }); voltaFoco = null;
      /* Consent Mode v2: gtag('consent','update',{analytics_storage: v ? 'granted' : 'denied'}) */ }
    if (!store.get(KEY)) ck.classList.add('is-open');
    $('[data-ck="aceitar"]', ck).addEventListener('click', function () { save(true); });
    $('[data-ck="recusar"]', ck).addEventListener('click', function () { save(false); });
    $('[data-ck="config"]', ck).addEventListener('click', function () { ck.classList.add('show-pref'); med.focus(); });
    $('[data-ck="salvar"]', ck).addEventListener('click', function () { save(med.checked); });
    $$('[data-cookie-prefs]').forEach(function (b) { b.addEventListener('click', function () {
      voltaFoco = b; var s = store.get(KEY); med.checked = !!(s && JSON.parse(s).medicao); ck.classList.add('is-open', 'show-pref'); med.focus(); }); });
  }
})();
