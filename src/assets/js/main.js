(function () {
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem('theme'); } catch (e) { stored = null; }
  if (stored === 'light' || stored === 'dark') root.setAttribute('data-theme', stored);
  var systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  var themeToggles = document.querySelectorAll('[data-theme-toggle]');
  function isDarkTheme() {
    var current = root.getAttribute('data-theme');
    return current ? current === 'dark' : systemTheme.matches;
  }
  function updateThemeLabels() {
    var label = isDarkTheme() ? 'Light mode' : 'Dark mode';
    themeToggles.forEach(function (toggle) {
      toggle.textContent = label;
      toggle.setAttribute('aria-label', 'Switch to ' + label.toLowerCase());
    });
  }
  themeToggles.forEach(function (toggle) {
    toggle.addEventListener('click', function () {
      var next = isDarkTheme() ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      updateThemeLabels();
      try { localStorage.setItem('theme', next); } catch (e) { /* storage blocked; theme still applies for this page */ }
    });
  });
  updateThemeLabels();
  systemTheme.addEventListener('change', updateThemeLabels);

  var navToggle = document.querySelector('[data-nav-toggle]');
  var navLinks = document.querySelector('[data-nav-links]');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      var open = navLinks.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { navLinks.classList.remove('is-open'); });
    });
  }

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    document.querySelectorAll('.reveal').forEach(function (el) {
      el.classList.add('reveal-pending');
      observer.observe(el);
    });
  }

  // plate loops: under reduced motion the still (poster) is the whole experience
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reducedMotion) {
    document.querySelectorAll('.plate video').forEach(function (v) {
      var still = v.querySelector('img');
      if (still) v.replaceWith(still); else { v.removeAttribute('autoplay'); v.pause(); }
    });
  }

  // The first-load type moment (ruled 2026-09-09, prototype variant B "dither"):
  // the display line arrives as a speckle field that thickens into solid type,
  // through one SVG filter per element. The eyebrow and headline get it on load,
  // section heads get a shorter pass when scrolled into view, body copy fades up.
  // Nothing runs under reduced motion, so the static render is untouched.
  if (false && !reducedMotion && window.requestAnimationFrame && document.fonts) {
    var ease = function (t) { return 1 - Math.pow(1 - t, 3); };
    var filterSeq = 0;

    function dither(el, ms, delay) {
      var id = 'dither-' + (filterSeq++);
      var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('width', '0'); svg.setAttribute('height', '0');
      svg.setAttribute('aria-hidden', 'true');
      svg.style.position = 'absolute';
      svg.innerHTML =
        '<filter id="' + id + '" x="-5%" y="-10%" width="110%" height="120%" color-interpolation-filters="sRGB">' +
        '<feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="1" seed="' + filterSeq + '" result="n"/>' +
        '<feColorMatrix in="n" type="luminanceToAlpha" result="la"/>' +
        '<feComponentTransfer in="la" result="lin"><feFuncA type="linear" slope="3" intercept="-1.2"/></feComponentTransfer>' +
        '<feComponentTransfer in="lin" result="mask"><feFuncA type="discrete" tableValues="0 1"/></feComponentTransfer>' +
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="28" xChannelSelector="R" yChannelSelector="G" result="d"/>' +
        '<feComposite in="d" in2="mask" operator="in"/>' +
        '</filter>';
      document.body.appendChild(svg);
      var disp = svg.querySelector('feDisplacementMap');
      var lin = svg.querySelector('feFuncA[type="linear"]');
      var start = null, finished = false;
      function finish() {
        if (finished) return; finished = true;
        el.style.filter = ''; el.style.opacity = ''; el.style.visibility = '';
        svg.remove();
      }
      el.style.filter = 'url(#' + id + ')';
      el.style.opacity = '0';
      el.style.visibility = '';
      function frame(ts) {
        if (finished) return;
        if (start === null) start = ts;
        var raw = (ts - start - delay) / ms, t = Math.max(0, Math.min(1, raw)), e = ease(t);
        disp.setAttribute('scale', String(28 * (1 - e)));
        // the mask threshold sweeps from "almost nothing passes" to "everything passes"
        lin.setAttribute('intercept', String(-1.2 + 2.6 * e));
        el.style.opacity = raw < 0 ? '0' : '1';
        if (t < 1) requestAnimationFrame(frame); else finish();
      }
      requestAnimationFrame(frame);
      // safety net: whatever happens to the filter, the type is never left hidden
      setTimeout(finish, delay + ms + 1500);
    }

    function fadeUp(el, ms, delay) {
      el.style.visibility = '';
      el.style.opacity = '0'; el.style.transform = 'translateY(10px)';
      setTimeout(function () {
        el.style.transition = 'opacity ' + ms + 'ms var(--ease-out), transform ' + ms + 'ms var(--ease-out)';
        el.style.opacity = ''; el.style.transform = '';
        setTimeout(function () { el.style.transition = ''; }, ms + 50);
      }, delay);
    }

    var hero = document.querySelector('.hero, .page-hero');
    var stack = [];
    if (hero) {
      ['.eyebrow', 'h1', '.lede', '.hero-sub'].forEach(function (sel) {
        var el = hero.querySelector(sel); if (el) stack.push(el);
      });
    }
    var heads = [].slice.call(document.querySelectorAll('h2')).filter(function (h) { return !hero || !hero.contains(h); });
    stack.concat(heads).forEach(function (el) { el.style.visibility = 'hidden'; });
    // if fonts never settle, show everything as-is rather than hold the page hostage
    var unhideAll = function () { stack.concat(heads).forEach(function (el) { if (el.style.visibility === 'hidden') el.style.visibility = ''; }); };
    setTimeout(unhideAll, 4000);

    document.fonts.ready.then(function () {
      stack.forEach(function (el, i) {
        if (el.tagName === 'H1' || el.classList.contains('eyebrow')) dither(el, el.tagName === 'H1' ? 1000 : 600, i * 180);
        else fadeUp(el, 600, i * 180 + 250);
      });
    });

    if ('IntersectionObserver' in window && heads.length) {
      var headObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          headObserver.unobserve(entry.target);
          dither(entry.target, 650, 0);
        });
      }, { threshold: 0.3 });
      heads.forEach(function (h) { headObserver.observe(h); });
    } else {
      heads.forEach(function (h) { h.style.visibility = ''; });
    }
  }

  // Vercel 307s to /#now and /gtm-leadership.html#human-data can land
  // with the hash set before layout; jump once the page is ready.
  function scrollToHash() {
    var id = (location.hash || '').replace(/^#/, '');
    if (!id) return;
    var el = document.getElementById(id);
    if (el) el.scrollIntoView();
  }
  if (document.readyState === 'complete') scrollToHash();
  else window.addEventListener('load', scrollToHash);
})();
