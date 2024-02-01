const orderdeliveryListUpdate = [document.querySelector("#order_delivery_input1"), document.querySelector("#order_delivery_input2")]
const orderDelivery = document.querySelectorAll(".orderdel ivery")
const orderStatusUpdate = document.querySelector("#order_delivery_status")

if (orderStatusUpdate.value == "delivery") {
    orderDelivery.forEach(element => {
        element.classList.remove("none")
    })
    orderdeliveryListUpdate[0].checked = true
} else {
    orderDelivery.forEach(element => {
        element.classList.add("none")
    })
    orderdeliveryListUpdate[1].checked = true
}