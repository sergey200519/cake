//  ---------Табы---------

let tabsBtn = document.querySelectorAll('.main__weight__link');
let tabsItem = document.querySelectorAll('.main__weight__container');
const buyBtns = document.querySelectorAll(".buy_btn") 

let article = 0;

tabsBtn.forEach(function (element) {
  element.addEventListener('click', function (e) {
    const path = e.currentTarget.dataset.path;


    tabsBtn.forEach(function (btn) { btn.classList.remove('tabs-nav__btn--active') });
    e.currentTarget.classList.add('tabs-nav__btn--active');

    tabsItem.forEach(function (element) { element.classList.remove('tabs-item--active') });

    let activeTab = document.querySelector(`[data-target="${path}"]`);
    activeTab.classList.add('tabs-item--active');
    article = parseInt(activeTab.querySelector(".main__right__article span").textContent)
    setArticle();
  });
});
article = parseInt(document.querySelector(".tabs-item--active .main__right__article span.article").textContent);
function setArticle() {
  buyBtns.forEach(btn => {
    btn.setAttribute("data-product-article", article);
  });
}
setArticle();