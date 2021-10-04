document.addEventListener('DOMContentLoaded', initHeaderScroll, false)
document.removeEventListener('unload', initHeaderScroll)

function initHeaderScroll () {
  let scrollPosition = window.scrollY
  const header = document.querySelector(".header__nav")
  const stickyOnScroll = () => header.classList.add("header__nav--sticky")
  const removeSticky = () => header.classList.remove("header__nav--sticky")

  window.addEventListener('scroll', function() {
    scrollPosition = window.scrollY;
    if (scrollPosition >= 10 ) { stickyOnScroll() }
    else { removeSticky() }
  })
}
