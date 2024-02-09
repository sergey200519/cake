import { setEvents  } from "./basket_delete.js";
import { deleteExtraZero } from "./deleteExtraZero.js";

function basketWrite(html, count) {
    // count передаю на случай если потребуется выводить число товаров в корзине
    const parser = new DOMParser();
    const htmlElement = parser.parseFromString(html, "text/html");
    // console.log(htmlElement, htmlElement.querySelector(".order__table"));
    // const table = htmlElement.querySelector("#order .order__parent .order__table")
    const table = htmlElement.querySelector(".order__table")
    document.querySelector("#order .order__parent .order__table").innerHTML = table.innerHTML

    const totalPrice = htmlElement.querySelector("#order_total_price")
    console.log(document.querySelector("#order_total_price"));
    document.querySelector("#order_total_price").innerHTML = totalPrice.innerHTML

    document.querySelector("#basketcout").innerHTML = count
    setEvents()
    deleteExtraZero()
}

export { basketWrite }