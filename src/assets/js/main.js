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
