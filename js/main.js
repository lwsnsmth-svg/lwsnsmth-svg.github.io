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

  /* ---- Current year in footer ------------------------------------------ */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();
