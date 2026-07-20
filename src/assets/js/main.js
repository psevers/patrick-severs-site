(function () {
  var root = document.documentElement;
  var stored = localStorage.getItem('theme');
  if (stored) root.setAttribute('data-theme', stored);

  var toggle = document.querySelector('[data-theme-toggle]');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var current = root.getAttribute('data-theme');
      var isDark = current
        ? current === 'dark'
        : window.matchMedia('(prefers-color-scheme: dark)').matches;
      var next = isDark ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    });
  }

  var navToggle = document.querySelector('[data-nav-toggle]');
  var navLinks = document.querySelector('[data-nav-links]');
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', function () {
      navLinks.classList.toggle('is-open');
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

  var typedCmd = document.getElementById('hero-typed-cmd');
  if (typedCmd) {
    var HERO_COMMAND = '$ agents --status';
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion) {
      typedCmd.textContent = HERO_COMMAND;
    } else {
      var charIndex = 0;
      var typeInterval = setInterval(function () {
        charIndex++;
        var caret = charIndex < HERO_COMMAND.length ? '█' : '';
        typedCmd.textContent = HERO_COMMAND.slice(0, charIndex) + caret;
        if (charIndex >= HERO_COMMAND.length) clearInterval(typeInterval);
      }, 55);
    }
  }
})();
