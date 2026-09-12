(function () {
  var reduceMq = window.matchMedia('(prefers-reduced-motion: reduce)');

  function reduced() {
    return reduceMq.matches;
  }

  function tabVisible() {
    return document.visibilityState === 'visible';
  }

  function stillFor(video) {
    var still = video.querySelector('img');
    if (still) video.replaceWith(still);
    else { video.removeAttribute('autoplay'); video.pause(); }
  }

  function showComplete(video) {
    if (video.readyState >= 1 && video.duration && isFinite(video.duration)) {
      try { video.currentTime = Math.max(0, video.duration - 0.05); } catch (e) { /* seek ignored before metadata */ }
    }
  }

  function sync(video, onScreen) {
    if (reduced()) return;
    if (onScreen && tabVisible()) {
      var play = video.play();
      if (play && play.catch) play.catch(function () { showComplete(video); });
    } else {
      video.pause();
      showComplete(video);
    }
  }

  function boot() {
    var videos = [].slice.call(document.querySelectorAll('.loop video'));
    if (!videos.length) return;

    if (reduced()) {
      videos.forEach(stillFor);
      return;
    }

    var visible = typeof WeakMap === 'function' ? new WeakMap() : null;

    function allSync() {
      videos.forEach(function (video) {
        if (video.tagName !== 'VIDEO') return;
        sync(video, visible ? !!visible.get(video) : true);
      });
    }

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (visible) visible.set(entry.target, entry.isIntersecting);
          sync(entry.target, entry.isIntersecting);
        });
      }, { threshold: 0.15 });
      videos.forEach(function (video) {
        if (visible) visible.set(video, false);
        io.observe(video);
      });
    } else {
      videos.forEach(function (video) { sync(video, true); });
    }

    document.addEventListener('visibilitychange', allSync);
    if (reduceMq.addEventListener) reduceMq.addEventListener('change', function () {
      if (reduced()) videos.forEach(function (video) {
        if (video.tagName === 'VIDEO') stillFor(video);
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
