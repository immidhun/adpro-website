/* Ad Pro Advertising, motion + interaction layer (v4, Nov 2026) */
(function () {
  var d = document, root = d.documentElement, w = window;
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = w.matchMedia('(hover: hover) and (pointer: fine)').matches;
  function $(s, c) { return (c || d).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); }

  /* ---------- menu, dropdown ---------- */
  var mb = $('.menu'), nav = $('#nav');
  if (mb) mb.addEventListener('click', function () { var o = nav.classList.toggle('open'); mb.setAttribute('aria-expanded', o); });
  $$('.dd>button').forEach(function (x) {
    x.addEventListener('click', function () { var o = x.parentNode.classList.toggle('open'); x.setAttribute('aria-expanded', o); });
  });
  d.addEventListener('click', function (e) { $$('.dd.open').forEach(function (dd) { if (!dd.contains(e.target)) { dd.classList.remove('open'); $('button', dd).setAttribute('aria-expanded', false); } }); });

  /* ---------- WhatsApp form ---------- */
  var f = d.getElementById('qf');
  if (f) f.addEventListener('submit', function (e) {
    e.preventDefault();
    var g = function (i) { var x = d.getElementById(i); return x ? x.value.trim() : ''; };
    var m = 'Hello Ad Pro,\n\nName: ' + g('n') + '\nBusiness: ' + g('b') + '\nPlace: ' + g('p') + '\nNeed: ' + g('s') + '\n\n' + g('m');
    w.open('https://wa.me/917560921593?text=' + encodeURIComponent(m), '_blank', 'noopener');
  });

  /* ---------- page wipe (two bands at 45deg, like the logo's hands) ---------- */
  var wipe = $('.wipe');
  function flag(v) { try { v ? sessionStorage.setItem('apw', '1') : sessionStorage.removeItem('apw'); } catch (e) {} }
  flag(false);                                   // the arrival wipe plays once, only after an in-site click
  w.addEventListener('pageshow', function (e) { if (wipe) wipe.classList.remove('go'); if (e.persisted) root.classList.remove('arrive'); });
  /* prefetch the next page as soon as a link is hovered or touched, so it is ready before the wipe ends */
  var pre = {};
  function prefetch(e) {
    var a = e.target.closest && e.target.closest('a'); if (!a) return;
    var href = a.getAttribute('href') || '';
    if (a.target === '_blank' || !/^[\w-]+\.html$/.test(href) || pre[href]) return;
    pre[href] = 1; var l = d.createElement('link'); l.rel = 'prefetch'; l.href = href; d.head.appendChild(l);
  }
  d.addEventListener('mouseover', prefetch, { passive: true });
  d.addEventListener('touchstart', prefetch, { passive: true });
  if (wipe && !reduce) {
    d.addEventListener('click', function (e) {
      var a = e.target.closest('a'); if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
      var href = a.getAttribute('href') || '';
      if (a.target === '_blank' || /^(#|tel:|mailto:|https?:)/.test(href) || !/\.html(#.*)?$/.test(href)) return;
      if (href.split('#')[0] === location.pathname.split('/').pop()) return;
      e.preventDefault(); flag(true); root.classList.remove('arrive'); void wipe.offsetWidth; wipe.classList.add('go');
      setTimeout(function () { location.href = href; }, 300);
    });
  }

  /* ---------- smooth scroll (desktop) ---------- */
  var lenis = null;
  if (fine && !reduce && w.Lenis) {
    lenis = new w.Lenis({ duration: 1.1, smoothWheel: true });
    d.addEventListener('click', function (e) {
      var a = e.target.closest('a[href^="#"]'); if (!a) return; var t = $(a.getAttribute('href')); if (!t) return;
      e.preventDefault(); lenis.scrollTo(t, { offset: -90 });
    });
  }

  /* ---------- header hide/show + progress bar ---------- */
  var hd = $('.hd'), bar = $('.prog i'), lastY = 0;
  function onScroll(y) {
    if (hd) {
      hd.classList.toggle('scrolled', y > 8);
      var open = nav && nav.classList.contains('open');
      hd.classList.toggle('hide', !open && y > 320 && y > lastY + 2);
      if (y < lastY - 2) hd.classList.remove('hide');
    }
    if (bar) { var max = d.documentElement.scrollHeight - innerHeight; bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')'; }
    lastY = y;
  }

  /* ---------- scroll reveals (position check each frame; clip-path hides elements from IntersectionObserver) ---------- */
  var io = 'IntersectionObserver' in w;
  var pending = $$('[data-r]');
  pending.forEach(function (el) {
    var sib = el.parentNode ? Array.prototype.indexOf.call(el.parentNode.children, el) : 0;
    el.style.setProperty('--d', Math.min(sib, 6) * 70 + 'ms');
    if (reduce) el.classList.add('in');
  });
  if (reduce) pending = [];
  function reveal() {
    if (!pending.length) return;
    var lim = innerHeight * 0.92;
    pending = pending.filter(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < lim && r.bottom > -50) { el.classList.add('in'); setTimeout(function () { el.classList.add('done'); }, 1800); return false; }
      if (r.bottom <= -50) { el.classList.add('in'); return false; }
      return true;
    });
  }
  /* ---------- scroll-lit paragraphs ---------- */
  var lits = [];
  if (!reduce) $$('[data-lit]').forEach(function (el) {
    if (el.children.length) return;           // plain-text paragraphs only
    el.innerHTML = el.textContent.trim().split(/\s+/).map(function (t) { return '<span class="lw">' + t + '</span>'; }).join(' ');
    lits.push({ el: el, ws: $$('.lw', el), n: -1 });
  });
  function lightUp() {
    var vh = innerHeight;
    lits.forEach(function (o) {
      var r = o.el.getBoundingClientRect();
      var p = (vh * 0.88 - r.top) / (vh * 0.5);          // starts lighting at 88% of screen, done by 38%
      p = Math.max(0, Math.min(1, p));
      var n = Math.round(p * o.ws.length);
      if (n !== o.n) { o.ws.forEach(function (w, i) { w.classList.toggle('l', i < n); }); o.n = n; }
    });
  }

  /* ---------- counters ---------- */
  $$('[data-count]').forEach(function (el) {
    var to = +el.getAttribute('data-count');
    if (reduce || !io) { el.textContent = to; return; }
    el.textContent = '0';
    var o = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting) return; o.disconnect();
      var t0 = performance.now(), dur = 1400;
      (function tick(t) { var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3); el.textContent = Math.round(to * e); if (p < 1) requestAnimationFrame(tick); })(t0);
    }, { threshold: 0.5 });
    o.observe(el);
  });

  /* ---------- parallax: hero hands follow the mouse, screenshots drift on scroll ---------- */
  var hands = $('.hero .hands svg'), mx = 0, my = 0, cx = 0, cy = 0;
  if (hands && fine && !reduce) {
    w.addEventListener('mousemove', function (e) { mx = (e.clientX / innerWidth - .5); my = (e.clientY / innerHeight - .5); }, { passive: true });
  }
  var shots = $$('.shot img');
  function parallax() {
    if (reduce) return;
    shots.forEach(function (img) {
      var r = img.parentNode.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return;
      var p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight;
      img.style.transform = 'translateY(' + (p * -28).toFixed(1) + 'px) scale(1.08)';
    });
    if (hands) {
      cx += (mx - cx) * .06; cy += (my - cy) * .06;
      var hb = $('.hb', hands), hr = $('.hr', hands);
      if (hb && hands.classList.contains('ready')) {
        hb.style.transform = 'translate(' + (cx * -26).toFixed(2) + 'px,' + (cy * -18).toFixed(2) + 'px)';
        hr.style.transform = 'translate(' + (cx * 26).toFixed(2) + 'px,' + (cy * 18).toFixed(2) + 'px)';
      }
    }
  }
  if (hands) setTimeout(function () { hands.classList.add('ready'); }, 1400);

  /* ---------- custom cursor + magnetic buttons (desktop) ---------- */
  var cur = $('.cur');
  if (cur && fine && !reduce) {
    root.classList.add('has-cur');
    var tx = -100, ty = -100, ux = -100, uy = -100, lab = $('span', cur);
    w.addEventListener('mousemove', function (e) { tx = e.clientX; ty = e.clientY; }, { passive: true });
    d.addEventListener('mouseover', function (e) {
      var s = e.target.closest('.shot'), a = e.target.closest('a,button,summary,label,input,select,textarea');
      cur.classList.toggle('big', !!s); cur.classList.toggle('hov', !s && !!a);
      lab.textContent = s ? 'Open site' : '';
    });
    d.addEventListener('mouseleave', function () { cur.style.opacity = 0; });
    d.addEventListener('mouseenter', function () { cur.style.opacity = 1; });
    (function loop() { ux += (tx - ux) * .22; uy += (ty - uy) * .22; cur.style.transform = 'translate(' + ux + 'px,' + uy + 'px)'; requestAnimationFrame(loop); })();
    $$('.mag').forEach(function (b) {
      b.addEventListener('mousemove', function (e) { var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .22).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .3).toFixed(1) + 'px)'; });
      b.addEventListener('mouseleave', function () { b.style.transform = ''; });
    });
  }

  /* ---------- BatchBoard TV: students check in live ---------- */
  var tv = $('.tv[data-live]');
  if (tv && !reduce) {
    var tiles = $$('.g span', tv), stat = $('.t span', tv), clock = $('.t b', tv), i = 0, started = false;
    var states = tiles.map(function (t) { return t.className; });
    function render() {
      var inN = 0, lv = 0;
      tiles.forEach(function (t) { if (t.className === '') inN++; else if (t.className === 'l') lv++; });
      stat.textContent = inN + ' in, ' + lv + ' on leave, ' + (tiles.length - inN - lv) + ' to arrive';
    }
    var tvo = new IntersectionObserver(function (es) {
      if (!es[0].isIntersecting || started) return; started = true;
      tiles.forEach(function (t) { if (t.className !== 'l') t.className = 'w'; }); render();
      var order = tiles.filter(function (t) { return t.className === 'w'; });
      var min = 52;
      var iv = setInterval(function () {
        if (i < order.length - 3) { order[i].className = 'pop'; void order[i].offsetWidth; order[i].className = ''; i++; render(); }
        clock.textContent = 'Batch C, 9:' + (min < 59 ? ++min : 59);
        if (i >= order.length - 3) clearInterval(iv);
      }, 650);
    }, { threshold: .5 });
    tvo.observe(tv);
  }

  /* ---------- FAQ: smooth open ---------- */
  $$('.faq details').forEach(function (det) {
    var s = $('summary', det), p = $('p', det);
    s.addEventListener('click', function (e) {
      if (reduce) return; e.preventDefault();
      if (det.open) { var h = p.offsetHeight; p.animate([{ height: h + 'px', opacity: 1 }, { height: '0px', opacity: 0 }], { duration: 260, easing: 'ease' }).onfinish = function () { det.open = false; }; det.classList.remove('on'); }
      else { det.open = true; det.classList.add('on'); var h2 = p.offsetHeight; p.animate([{ height: '0px', opacity: 0 }, { height: h2 + 'px', opacity: 1 }], { duration: 320, easing: 'cubic-bezier(.2,.8,.2,1)' }); }
    });
  });

  /* ---------- main loop ---------- */
  function raf(t) {
    if (lenis) lenis.raf(t);
    var y = lenis ? lenis.scroll : w.scrollY;
    if (y !== lastY) onScroll(y);
    parallax(); reveal(); lightUp();
    requestAnimationFrame(raf);
  }
  onScroll(w.scrollY); requestAnimationFrame(raf);
})();
