function deleteExtraZero() {
    const extraZeroNums = document.querySelectorAll(".extra_zero");
    extraZeroNums.forEach(num => {
        const data = parseFloat(num.textContent.replace(",", ".")).toString().replace(".", ",")
        num.textContent = data
    })
}

deleteExtraZero()


export { deleteExtraZero }