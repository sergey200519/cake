let dels = document.querySelectorAll(".del_item")

dels.forEach(el => {
    el.addEventListener("click", (e) => {
        let res = confirm("Удалить элемент?")
        if (!res) {
            e.preventDefault()
        }
    })
})