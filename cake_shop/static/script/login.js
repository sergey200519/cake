// function noDigits(event) {
//     let re = /^[\d\+][\d\(\)\ -]{4,14}\d$/;
//     let valid = re.test(event.target.value);
//     console.log(valid);
//     let btn = document.querySelector("#login__btn")
//     if (valid) {
//         btn.disabled = false
//     } else {
//         btn.disabled = true
//     }
//     // if ("/^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im".indexOf(event.key) != -1)
//     //   event.preventDefault();
//   }
// document.querySelector("#login__tel").addEventListener("input", noDigits)

document.querySelector("#open__search__form").addEventListener("click", (e) => {
    e.preventDefault();
    document.querySelector(".login").classList.remove("none")
})


document.querySelector(".login__form__close").addEventListener("click", () => {
    document.querySelector(".login").classList.add("none")
})