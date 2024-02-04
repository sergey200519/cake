import { basketWrite } from "./besket_write.js";

function addBasketProduct(productId, productArticle) {
    fetch("/basket/product_add_basket/", {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "productArticle": productArticle,
          "productId": productId
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.status == "userNotAuthenticated") {
          document.querySelector("#login_popup").classList.remove("none");
        }
        if (data.status == "success") {
          basketWrite(data.basket_products, data.count)
        }
      })
}


const basketBtns = document.querySelectorAll(".list__righ__button")
const basketBtns2 = document.querySelectorAll(".list__righ__buttontwo")

basketBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault()
        addBasketProduct(btn.getAttribute("data-product-id"), btn.getAttribute("data-product-article"))
    })
})

basketBtns2.forEach(btn => {
  btn.addEventListener("click", (e) => {
      e.preventDefault()
      addBasketProduct(btn.getAttribute("data-product-id"), btn.getAttribute("data-product-article"))
      document.querySelector("#order").classList.remove("none")
  })
})