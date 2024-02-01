let orderdelivery = document.querySelectorAll(".orderdelivery")

let orderdeliveryList = [document.querySelector("#order_delivery_input1"), document.querySelector("#order_delivery_input2")]

orderdeliveryList.forEach(element => {
    element.addEventListener("input", hideInputs)
});

// document.querySelector("#checkbox").addEventListener("input", () => {
//     if (document.querySelector("#checkbox").checked) {
//         orderdelivery.forEach(element => {
//             element.classList.remove("none")
//         })
//     } else {
//         orderdelivery.forEach(element => {
//             element.classList.add("none")
//         })
//     }
// })
const orderStatus = document.querySelector("#order_delivery_status")
function hideInputs() {
    if (orderdeliveryList[0].checked) {
        orderdelivery.forEach(element => {
            orderStatus.value = "delivery"
            element.classList.remove("none")
        })   
    } else {
        orderdelivery.forEach(element => {
            orderStatus.value = "pickup"
            element.classList.add("none")
        })
    }
}
hideInputs()