import { basketWrite } from "./besket_write.js";

function addBasketExclusive(productId, productArticle) {
  let res = "not code" 
    fetch("/basket/exclusive_add_basket/", {
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
      });
      return res
}


const basketBtns = document.querySelectorAll(".list__cakes .card .list__righ__button")

basketBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
        e.preventDefault()
        addBasketExclusive(btn.getAttribute("data-product-id"), btn.getAttribute("data-product-article"))
    })
})