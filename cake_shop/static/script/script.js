import { MoreList } from "./moreList.js"
import { add_baskets } from "./basket.js"

// const modalWindowBtn = document.querySelector('.hero__form__button')
// modalWindowBtn.addEventListener('click', test)
// function test(event) {
//   event.preventDefault()
//   document.querySelector('.modal-window').classList.toggle('none')
// }
console.log("mmmmmmmm");

const swiper = new Swiper('.swiper', {
  // Optional parameters
  //direction: 'vertical',
  loop: true,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickable: true
  }
});
// new Accordion('.accordion-container')



// let clouse_it = "<p>Закрыть</p>"

// new MoreList(".list__cakes", 8, clouse_it)
// // второй блок
// new MoreList(".list__cakes__two", 8, clouse_it)

add_baskets()

