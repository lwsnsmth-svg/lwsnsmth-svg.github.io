/* ==========================================================================
   Ascent — site behaviour
   Vanilla JS, no dependencies. Every block guards for missing elements so
   the same file can be included on every page.
   ========================================================================== */
(function () {
  'use strict';

  /* ---- Mobile navigation --------------------------------------------- */
  var navToggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      var open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
    });

    // Close on outside click, on Escape, and after following a link.
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeNav();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeNav();
    });
    document.addEventListener('click', function (e) {
      if (!nav.classList.contains('is-open')) return;
      if (e.target.closest('#primary-nav') || e.target.closest('.nav-toggle')) return;
      closeNav();
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) closeNav();
    });
  }

  function closeNav() {
    if (!nav || !navToggle) return;
    nav.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
  }

  /* ---- Sticky header shadow ------------------------------------------ */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Scroll reveal -------------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal');

  function revealAll() {
    revealables.forEach(function (el) { el.classList.add('is-visible'); });
  }

  if (revealables.length) {
    if (!('IntersectionObserver' in window)) {
      revealAll();
    } else {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        });
      }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
      revealables.forEach(function (el) { observer.observe(el); });

      // Failsafe. If the observer never reports an intersection — a page laid
      // out in a zero-height viewport, a hidden container, an embedded frame —
      // every .reveal would stay at opacity 0 forever and the page would look
      // blank. Decoration must never be able to hide content permanently, so
      // if nothing at all has been revealed shortly after load, show it all.
      // In a normal viewport the first element resolves immediately and this
      // never runs.
      setTimeout(function () {
        if (!document.querySelector('.reveal.is-visible')) revealAll();
      }, 3000);
    }
  }

  /* ---- Animated stat counters ---------------------------------------- */
  var counters = document.querySelectorAll('[data-count-to]');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function formatNumber(value, el) {
    var prefix = el.dataset.prefix || '';
    var suffix = el.dataset.suffix || '';
    return prefix + Math.round(value).toLocaleString() + suffix;
  }

  function runCounter(el) {
    var target = parseFloat(el.dataset.countTo);
    if (isNaN(target)) return;
    if (reduceMotion) { el.textContent = formatNumber(target, el); return; }

    var duration = 1400;
    var start = null;
    function step(timestamp) {
      if (start === null) start = timestamp;
      var progress = Math.min((timestamp - start) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
      el.textContent = formatNumber(target * eased, el);
      if (progress < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  if (counters.length) {
    if (!('IntersectionObserver' in window)) {
      counters.forEach(runCounter);
    } else {
      var countObserver = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          runCounter(entry.target);
          countObserver.unobserve(entry.target);
        });
      }, { threshold: 0.5 });
      counters.forEach(function (el) { countObserver.observe(el); });
    }
  }

  /* ---- Accordion (FAQ) ------------------------------------------------ */
  document.querySelectorAll('.accordion__trigger').forEach(function (trigger) {
    trigger.addEventListener('click', function () {
      var panel = document.getElementById(trigger.getAttribute('aria-controls'));
      var open = trigger.getAttribute('aria-expanded') === 'true';
      trigger.setAttribute('aria-expanded', String(!open));
      if (panel) panel.classList.toggle('is-open', !open);
    });
  });

  /* ---- Tool cards (home): click to expand a short description ----------- */
  document.querySelectorAll('.tool-card__toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!open));
      btn.closest('.tool-card').classList.toggle('is-open', !open);
    });
  });

  /* ---- Download page: buttons fetch the newest release ------------------ */
  // The markup links one release's files, so the buttons work without this.
  // GitHub's /releases/latest/download/ skips pre-releases and the file names
  // carry the version, so ask the API instead: take the newest release that has
  // every installer (one still uploading is passed over) and point each button
  // at its file. If the request fails — offline, or past the API's limit of 60
  // requests an hour per visitor — the links in the markup stay.
  var installers = document.querySelectorAll('[data-installer]');
  if (installers.length && window.fetch) {
    var fileFor = function (release, suffix) {
      return release.assets.filter(function (asset) {
        return asset.state === 'uploaded' && asset.name.slice(-suffix.length) === suffix;
      })[0];
    };
    fetch('https://api.github.com/repos/Ascent-Evaluation/ascent-mapper/releases?per_page=10')
      .then(function (res) {
        if (!res.ok) throw new Error('GitHub API ' + res.status);
        return res.json();
      })
      .then(function (releases) {
        var newest = releases
          .filter(function (release) {
            return !release.draft && Array.prototype.every.call(installers, function (btn) {
              return fileFor(release, btn.getAttribute('data-installer'));
            });
          })
          .sort(function (a, b) { return (b.published_at || '').localeCompare(a.published_at || ''); })[0];
        if (!newest) return;
        installers.forEach(function (btn) {
          btn.href = fileFor(newest, btn.getAttribute('data-installer')).browser_download_url;
        });
        document.querySelectorAll('[data-release-version]').forEach(function (el) {
          el.textContent = newest.tag_name.replace(/^v/, '');
        });
      })
      .catch(function () { /* keep the links in the markup */ });
  }

  /* ---- Embedded apps that report their own height ---------------------- */
  // The Evaluation Pipeline app (Evaluation Process) posts
  // { type: 'evaluation-timeline:resize', height } whenever its content changes
  // size, including when a step's card opens. Match the frame to it so the app
  // never scrolls inside itself. Without JS the frame keeps the CSS height.
  var autoFrames = document.querySelectorAll('iframe[data-autoheight]');
  if (autoFrames.length) {
    window.addEventListener('message', function (e) {
      var data = e.data;
      if (!data || data.type !== 'evaluation-timeline:resize' || !(data.height > 0)) return;
      autoFrames.forEach(function (frame) {
        if (frame.contentWindow === e.source && new URL(frame.src).origin === e.origin) {
          frame.style.height = Math.ceil(data.height) + 'px';
        }
      });
    });
  }

  /* ---- Embedded apps fade in once loaded ------------------------------- */
  // Each iframe.frame-fade adds .is-loaded from its own onload attribute (see
  // styles.css). Failsafe, as for the scroll reveal: if load never fires, an
  // app must not stay hidden, so show every frame after 5 seconds regardless.
  var fadeFrames = document.querySelectorAll('iframe.frame-fade');
  if (fadeFrames.length) {
    setTimeout(function () {
      fadeFrames.forEach(function (frame) { frame.classList.add('is-loaded'); });
    }, 5000);
  }

  /* ---- Current year in footer ------------------------------------------ */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
