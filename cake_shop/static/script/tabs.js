class Tabs {
    constructor(card) {
        this.card = card;
        this.tabsBtn = this.card.querySelectorAll(".list__weight__link");
        this.tabsItem = this.card.querySelectorAll(".list__weight__container");
        this.basketBtn = this.card.querySelector(".list__righ__button")
        this.firstArticle = this.card.querySelector(".tabs-item--active span")
        this.basketBtn.setAttribute("data-product-article", this.firstArticle.textContent)

        let self = this;
        this.tabsBtn.forEach(function (element) {
            element.addEventListener("click", (e) => {
                self.render(e)
            });
        });

    }

    render(e) {
        const path = e.target.dataset.path;

        this.tabsBtn.forEach(function (btn) { btn.classList.remove("tabs-nav__btn--active") });
        e.currentTarget.classList.add("tabs-nav__btn--active");

        this.tabsItem.forEach(function (element) { element.classList.remove("tabs-item--active") });


        this.card.querySelector(`[data-target="${path}"]`).classList.add("tabs-item--active");
        let article = this.card.querySelector(`[data-target="${path}"] .list__right__articletext span`).textContent;
        this.basketBtn.setAttribute("data-product-article", article)
    }
}

document.querySelectorAll(".product").forEach((product) => {
    new Tabs(product)
})