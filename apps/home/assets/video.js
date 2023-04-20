function showVideo (identifier) {
  const templateTag = document.getElementById('video-template-' + identifier)
  const videoTag = document.getElementById('video-player-' + identifier)
  document.getElementById('accept-video-' + identifier).style.display = 'none'
  const showVideo = templateTag.content.cloneNode(true)
  videoTag.appendChild(showVideo)
}

function initVideos () {
  const videos = document.querySelectorAll('.overlay_video_go')
  videos.forEach(video => {
    video.addEventListener('click', () => showVideo(video.dataset.identifier))
  })
}

document.addEventListener('DOMContentLoaded', initVideos, false)
