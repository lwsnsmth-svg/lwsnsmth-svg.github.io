/* Marks the page as JS-enabled before first paint. Loaded synchronously in <head> — keep it tiny. */
(function () {
  // Marks that JS is running, so CSS can safely hide scroll-reveal elements.
  // Without this class the content is simply visible — never blank.
  document.documentElement.classList.add('js');
})();
