function initHeaderImage () {
  const parallax = document.querySelector('.hero__parallax')
  parallax.style.backgroundImage = 'url(' + parallax.dataset.headerUrl + ')'
}

document.addEventListener('DOMContentLoaded', initHeaderImage, false)
