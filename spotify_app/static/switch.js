function showContent(contentId) {

  const windows = document.querySelectorAll('.main-window');
  windows.forEach(window => {
    window.style.display = 'none';
  });


  const selectedContent = document.getElementById(contentId);
  selectedContent.style.display = 'block';
}
showContent('content-1');




document.addEventListener('DOMContentLoaded', function () {
  const homeTab = document.querySelector('.home');
  const searchTab = document.querySelector('.search');
  const upperAdditional = document.querySelector('.upper');
  const lowerAdditional = document.querySelector('.lower');

  homeTab.addEventListener('click', function () {
    homeTab.classList.add('selected');
    homeTab.classList.remove('unselected');
    searchTab.classList.remove('selected');
    searchTab.classList.add('unselected');


    upperAdditional.classList.add('additional1');
    upperAdditional.classList.remove('additional2');
    lowerAdditional.classList.add('additional2');
    lowerAdditional.classList.remove('additional1');
  });

  searchTab.addEventListener('click', function () {
    searchTab.classList.add('selected');
    searchTab.classList.remove('unselected');
    homeTab.classList.remove('selected');
    homeTab.classList.add('unselected');


    upperAdditional.classList.add('additional2');
    upperAdditional.classList.remove('additional1');
    lowerAdditional.classList.add('additional1');
    lowerAdditional.classList.remove('additional2');
  });
});



document.getElementsByClassName("right-arrow").addEventListener("click", function () {
  const container = document.querySelector("#card-grid");
  container.scrollLeft = container.scrollWidth - container.clientWidth;
});