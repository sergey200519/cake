import { basketWrite } from "./besket_write.js";




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

function setEvents() {
  const btnsDelete = document.querySelectorAll(".basket_delete")
  btnsDelete.forEach(btn => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-basket-id")
      deleteBasketItem(id)
    })
  })
}
setEvents()
export { setEvents }