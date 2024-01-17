import { basketWrite } from "./besket_write.js";

const btnsDelete = document.querySelectorAll(".basket_delete")


function deleteBasketItem(basketId) {
    fetch(`/basket/delete_basket_product/${basketId}/`, {
        method: "GET",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "basketId": basketId
        }
      })
      .then(response => response.json())
      .then(data => {
        if (data.status == "success") {
          basketWrite(data.basket_products, data.count)
        }
      });
}


btnsDelete.forEach(btn => {
    btn.addEventListener("click", () => {
      console.log("ok");
        const id = btn.getAttribute("data-basket-id")
        deleteBasketItem(id)
    })
})