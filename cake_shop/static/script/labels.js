const inputs = document.querySelectorAll(".form_label input")


class Label {
    constructor(input) {
        this.input = input
        this.label = this.input.nextElementSibling
        if (this.label == null || this.label.tagName.toLowerCase() != "label") return
        if (this.input.getAttribute("type") == "date") {
            this.label.classList.add("form__label-top")
            return
        }

        let self = this
        this.input.addEventListener("focus", () => {
            self.focusEl(self)
        })
        this.input.addEventListener("blur", () => {
            self.blurEl(self)
        })
        this.blurEl(self)
    }

    isEmpty() {
        if (this.input.value == "") return true
        else return false
    }

    focusEl(self) {
        self.label.classList.add("form__label-top")
    }

    blurEl(self) {
        if (self.isEmpty()) {
            self.label.classList.remove("form__label-top")
        } else {
            self.label.classList.add("form__label-top")
        }
    }

}

inputs.forEach(el => {
    new Label(el)
})