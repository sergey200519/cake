
class FooterForm {
    constructor(form) {
        this.isValidState = false;

        this.form = form;


        this.captchaInput = this.form.querySelector("#captcha-footer")
        this.updateCaptcha = this.form.querySelector(".update__icon")
        this.captcha = this.form.querySelector(".footer__captcha__text")
        this.uniquechar = ""


        this.submitBtn = this.form.querySelector(".footer-button")

        this.submitBtn.classList.add("form__button-disabled")

        this.generateCaptcha()
        let self = this;
        this.updateCaptcha.addEventListener("click", () => {
            this.generateCaptcha()
        })

        this.captchaInput.addEventListener("input", () => {
            if (this.captchaInput.value == this.uniquechar) this.submitBtn.classList.remove("form__button-disabled")
            else this.submitBtn.classList.add("form__button-disabled")
        })


    }
    generateCaptcha() {
        this.uniquechar = ""
        const randomchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        for (let i = 1; i < 5; i++) {
            this.uniquechar += randomchar.charAt(
                Math.random() * randomchar.length)
        }
        this.captcha.innerHTML = this.uniquechar;
    }
}

let form = document.querySelector(".footer__form")



let a = new FooterForm(form);  