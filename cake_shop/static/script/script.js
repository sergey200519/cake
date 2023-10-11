import { MoreList } from "./moreList.js"

// const modalWindowBtn = document.querySelector('.hero__form__button')
// modalWindowBtn.addEventListener('click', test)
// function test(event) {
//   event.preventDefault()
//   document.querySelector('.modal-window').classList.toggle('none')
// }
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
new Accordion('.accordion-container')



