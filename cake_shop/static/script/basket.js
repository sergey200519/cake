function editBasketNum(num) {
    document.querySelector("#basket_num").textContent = num
}

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

            request.addEventListener("readystatechange", () => {
                let ans = request.responseText
                let doc = new DOMParser().parseFromString(ans, "text/html")
                let num = doc.querySelector("#basket_num")
                if (num != null) {
                    editBasketNum(num.textContent)
                }
                
            })
        })
    })
}



export { add_baskets };