function basketWrite(html, count) {
    // count передаю на случай если потребуется выводить число товаров в корзине
    const parser = new DOMParser();
    const htmlElement = parser.parseFromString(html, "text/html");
    const table = htmlElement.querySelector("#order .order__parent .order__table")
    document.querySelector("#order .order__parent .order__table").innerHTML = table.innerHTML
}

export { basketWrite }