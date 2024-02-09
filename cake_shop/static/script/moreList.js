class MoreList {
    constructor(list, n, clouse_item) {
        this.wrapper = list;
        this.list = this.wrapper.querySelectorAll(`:scope > li`)
        console.log(this.list.length, n - 1, );
        if (this.list.length < n) {
            return
        }
        this.list[n - 1].classList.add("list__more")
        this.on = this.wrapper.querySelector(`:scope > .list__more`)

        this.create_close(list, clouse_item)
        this.clouse_item(n)

        this.on.addEventListener("click", () => {
            this.on.classList.add("onclick")
            let i = 1
            this.list.forEach(element => {
                if (i > n) {
                    element.classList.remove("none")
                }
                i++
            });
        })

        this.clouse.addEventListener("click", () => {
            this.on.classList.remove("onclick")
            let i = 1
            this.list.forEach(element => {
                if (i > n) {
                    element.classList.add("none")
                }
                i++
            });
        })
    }

    create_close(list, clouse_item) {
        let div = document.createElement("li")
        div.className = "list__close"
        div.innerHTML = clouse_item
        this.wrapper.append(div)
        this.list = this.wrapper.querySelectorAll(`:scope > li`)
        this.clouse = this.wrapper.querySelector(`:scope > .list__close`)
    }

    clouse_item(n) {
        let i = 1
        this.list.forEach(element => {
            if (i > n) {
                element.classList.add("none")
            }
            i++
        });
    }
}
export { MoreList }