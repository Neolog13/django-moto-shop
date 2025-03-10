  // adaptive
  const menuBtn = document.querySelector('.menu__btn');
  const menu = document.querySelector('.menu__list');


menuBtn.addEventListener('click', () => {
  menu.classList.toggle('menu__list--active');
});



const swiper = new Swiper(".swiper", {
    effect: "fade",
    pagination: {
      el: ".swiper-pagination",
    },
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
  });

