function initMatomo () {
  const matomo = document.getElementById('matomo')
  const _paq = window._paq = window._paq || []
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  if (matomo.dataset.cookieDisabed) {
    _paq.push(['disableCookies'])
  }
  _paq.push(['trackPageView'])
  _paq.push(['enableLinkTracking'])
  insertMatomo(_paq, matomo.dataset.url, matomo.dataset.id)
}

function insertMatomo (_paq, url, id) {
  _paq.push(['setTrackerUrl', url + 'matomo.php'])
  _paq.push(['setSiteId', id])
  const d = document; const g = d.createElement('script'); const s = d.getElementsByTagName('script')[0]
  g.type = 'text/javascript'; g.async = true; g.src = url + 'matomo.js'; s.parentNode.insertBefore(g, s)
}

initMatomo()
