let slideIndex = 0;

showSlides();

function showSlides() {
  let i;
  let slides = document.querySelectorAll(".mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  // slides[slideIndex-1].style.display = "block";
  slides[slideIndex-1].style.display = 'block';
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}

let navbarList = document.querySelector('.navbar-list');
let menu = document.querySelector('.navbar-menu-button');
let close = document.querySelector('.navbar-close-button');
menu.addEventListener('click', openMenu);
close.addEventListener('click', closeMenu);
function openMenu(e){
  navbarList.classList.replace('navbar-list','navbar-list-visible');
}
function closeMenu(){
  navbarList.classList.replace('navbar-list-visible','navbar-list')
}

 