(function () {
  document.documentElement.classList.remove('no-js');

  // menu mobilne
  var t = document.querySelector('.nav-toggle'), n = document.getElementById('nav');
  if (t && n) t.addEventListener('click', function () {
    var o = n.classList.toggle('open');
    t.setAttribute('aria-expanded', o ? 'true' : 'false');
  });

  function digits(v) { return v.replace(/[^\d]/g, ''); }
  function val(f, name) { var el = f.querySelector('[name="' + name + '"]'); return el ? el.value.trim() : ''; }
  function checked(f, name) {
    return Array.prototype.map.call(f.querySelectorAll('[name="' + name + '"]:checked'), function (el) { return el.value; });
  }
  function fail(f, msg) { var e = f.querySelector('.form-error'); e.textContent = msg; e.classList.add('show'); }
  function clear(f) { f.querySelector('.form-error').classList.remove('show'); }

  // formularze nie wysyłają nic same: składają wiadomość i otwierają WhatsApp
  function openWhatsApp(f, lines, e) {
    var num = digits(f.getAttribute('data-wa') || ''), text = encodeURIComponent(lines.join('\n'));
    var kanal = e && e.submitter && e.submitter.value;
    if (!kanal) kanal = matchMedia('(pointer: coarse)').matches ? 'sms' : 'wa';
    // SMS: zapis „?&body=” działa i na iPhonie, i na Androidzie
    var url = kanal === 'sms' ? 'sms:+' + num + '?&body=' + text : 'https://wa.me/' + num + '?text=' + text;
    // zwykłe przejście: na telefonie otwiera aplikację WhatsApp (nowa karta w iPhonie zostaje pusta)
    window.location.href = url;
  }

  // animacje: elementy pojawiają się przy przewijaniu
  var reduceMotion = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduceMotion) {
    var sel = '.section-head, .service, .symptoms li, .steps li, .reasons > div, .reviews, .rv, .ticket, .contact-grid > *, .prose > *, .aside';
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { var t = en.target; t.classList.add('in'); io.unobserve(t); setTimeout(function () { t.style.transitionDelay = ''; }, 1200); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll(sel).forEach(function (el) {
      var i = Array.prototype.indexOf.call(el.parentNode.children, el);
      el.style.transition = 'none';          // ukryj od razu, bez mignięcia
      el.classList.add('reveal');
      void el.offsetWidth;
      el.style.transition = '';
      el.style.transitionDelay = Math.min(i, 5) * 70 + 'ms';
      io.observe(el);
    });
  }

  // karuzela opinii: sama przewija co 5 s, staje po dotknięciu
  document.querySelectorAll('[data-rv]').forEach(function (rv) {
    var tr = rv.querySelector('.rv-track'), paused = false, timer;
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    function step() { var c = tr.querySelector('.rv-card'); return c ? c.getBoundingClientRect().width + 18 : 300; }
    function go(dir) {
      var max = tr.scrollWidth - tr.clientWidth - 4;
      if (dir > 0 && tr.scrollLeft >= max) tr.scrollTo({ left: 0 });
      else if (dir < 0 && tr.scrollLeft <= 4) tr.scrollTo({ left: tr.scrollWidth });
      else tr.scrollBy({ left: dir * step() });
    }
    rv.querySelector('[data-rv-next]').addEventListener('click', function () { go(1); });
    rv.querySelector('[data-rv-prev]').addEventListener('click', function () { go(-1); });
    ['pointerenter', 'touchstart', 'focusin'].forEach(function (e) { rv.addEventListener(e, function () { paused = true; }, { passive: true }); });
    ['pointerleave', 'focusout'].forEach(function (e) { rv.addEventListener(e, function () { paused = false; }); });
    if (!reduce) timer = setInterval(function () { if (!paused && !document.hidden) go(1); }, 5000);
  });

  // prośba o telefon
  var cb = document.getElementById('cb-form');
  if (cb) cb.addEventListener('submit', function (e) {
    e.preventDefault();
    var tel = val(cb, 'telefon'), imie = val(cb, 'imie');
    if (digits(tel).length < 9) { fail(cb, 'Wpisz numer telefonu, minimum 9 cyfr.'); return; }
    clear(cb);
    var lines = ['Dzień dobry, proszę o telefon w sprawie auta. Piszę ze strony adozelektryka.pl.'];
    if (imie) lines.push('Imię: ' + imie);
    lines.push('Telefon: ' + tel);
    openWhatsApp(cb, lines, e);
  });

  // zgłoszenie usterki krok po kroku
  var tf = document.getElementById('ticket-form');
  if (tf) {
    var steps = tf.querySelectorAll('.fs'), bars = tf.querySelectorAll('.progress span');
    var back = tf.querySelector('[data-back]'), next = tf.querySelector('[data-next]'), send = tf.querySelector('[data-send]');
    var cur = 0;
    function show(i) {
      steps.forEach(function (s, k) { s.hidden = k !== i; });
      bars.forEach(function (b, k) { b.classList.toggle('on', k <= i); });
      back.style.visibility = i === 0 ? 'hidden' : 'visible';
      next.hidden = i === steps.length - 1;
      send.hidden = i !== steps.length - 1;
      clear(tf);
      cur = i;
    }
    function check(i) {
      if (i === 0 && !val(tf, 'marka')) return 'Wpisz markę i model auta.';
      if (i === 1 && !checked(tf, 'objawy[]').length && !val(tf, 'opis')) return 'Zaznacz objaw albo opisz problem własnymi słowami.';
      if (i === 2 && val(tf, 'telefon') && digits(val(tf, 'telefon')).length < 9) return 'Numer telefonu ma za mało cyfr.';
      return '';
    }
    next.addEventListener('click', function () {
      var m = check(cur);
      if (m) { fail(tf, m); return; }
      show(cur + 1);
      steps[cur].querySelector('input,select,textarea').focus();
    });
    back.addEventListener('click', function () { show(cur - 1); });
    tf.addEventListener('submit', function (e) {
      e.preventDefault();
      for (var i = 0; i < steps.length; i++) {
        var m = check(i);
        if (m) { show(i); fail(tf, m); return; }
      }
      var auto = [val(tf, 'marka'), val(tf, 'rok'), val(tf, 'silnik')].filter(Boolean).join(', ');
      var lines = ['Dzień dobry, zgłoszenie usterki ze strony adozelektryka.pl.', 'Auto: ' + auto];
      var vin = val(tf, 'vin'); if (vin) lines.push('VIN: ' + vin);
      var ob = checked(tf, 'objawy[]'); if (ob.length) lines.push('Objawy: ' + ob.join(', '));
      var kiedy = checked(tf, 'kiedy'); if (kiedy.length) lines.push('Kiedy występuje: ' + kiedy[0]);
      var jezdzi = checked(tf, 'jezdzi'); if (jezdzi.length) lines.push('Czy jeździ: ' + jezdzi[0]);
      var opis = val(tf, 'opis'); if (opis) lines.push('Opis: ' + opis);
      var imie = val(tf, 'imie'); if (imie) lines.push('Imię: ' + imie);
      var tel = val(tf, 'telefon'); if (tel) lines.push('Telefon: ' + tel);
      var pora = checked(tf, 'pora'); if (pora.length) lines.push('Najlepiej dzwonić: ' + pora[0]);
      openWhatsApp(tf, lines, e);
    });
    show(0);
  }
})();
