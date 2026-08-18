(function () {
  const slides = Array.from(document.querySelectorAll('.slide[data-slide]'));
  const mapLinks = Array.from(document.querySelectorAll('.story-map a[data-go]'));
  const prevBtn = document.getElementById('prev-btn');
  const nextBtn = document.getElementById('next-btn');
  const modeBtn = document.getElementById('mode-btn');
  const counter = document.getElementById('slide-counter');
  let index = 0;

  function clamp(i) {
    return Math.max(0, Math.min(slides.length - 1, i));
  }

  function activate(i, updateHash) {
    index = clamp(i);
    slides.forEach((slide, n) => {
      const on = n === index;
      slide.classList.toggle('active', on);
      slide.setAttribute('aria-hidden', String(!on));
    });
    mapLinks.forEach((link) => {
      const on = Number(link.dataset.go) === index;
      if (on) link.setAttribute('aria-current', 'page');
      else link.removeAttribute('aria-current');
    });
    if (counter) counter.textContent = `${index + 1} / ${slides.length}`;
    if (prevBtn) prevBtn.disabled = index === 0;
    if (nextBtn) nextBtn.disabled = index === slides.length - 1;
    if (updateHash) {
      const id = slides[index].id || `s${index}`;
      history.replaceState(null, '', '#' + id);
    }
    const active = slides[index];
    if (active) active.querySelector('.stage-inner, .slide') || active;
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function go(delta) {
    activate(index + delta, true);
  }

  mapLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();
      activate(Number(link.dataset.go), true);
    });
  });

  if (prevBtn) prevBtn.addEventListener('click', () => go(-1));
  if (nextBtn) nextBtn.addEventListener('click', () => go(1));

  if (modeBtn) {
    modeBtn.addEventListener('click', () => {
      const present = document.body.classList.toggle('present-mode');
      document.body.classList.toggle('review-mode', !present);
      modeBtn.setAttribute('aria-pressed', String(present));
      modeBtn.textContent = present ? 'Exit 16:9' : '16:9 present';
    });
  }

  document.addEventListener('keydown', (event) => {
    if (event.target && ['INPUT', 'TEXTAREA', 'SELECT'].includes(event.target.tagName)) return;
    if (event.key === 'ArrowRight' || event.key === 'PageDown' || event.key === ' ') {
      event.preventDefault();
      go(1);
    } else if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
      event.preventDefault();
      go(-1);
    } else if (event.key === 'p' || event.key === 'P') {
      modeBtn && modeBtn.click();
    } else if (event.key === 'Home') {
      event.preventDefault();
      activate(0, true);
    } else if (event.key === 'End') {
      event.preventDefault();
      activate(slides.length - 1, true);
    }
  });

  const hash = location.hash.slice(1);
  const fromHash = slides.findIndex((slide) => slide.id === hash);
  document.body.classList.add('review-mode');
  activate(fromHash >= 0 ? fromHash : 0, false);
})();
