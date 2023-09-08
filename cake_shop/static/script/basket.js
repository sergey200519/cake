function add_baskets() {
    
    let products = document.querySelectorAll(".product")
    products.forEach(function (product) {
        let link = product.querySelector(".basket_add");
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const request = new XMLHttpRequest();

            const url = `${window.location.href}${link.getAttribute("data-href")}`;

            request.open("GET", url, true);
            request.send();
        })
    })
}
export { add_baskets };