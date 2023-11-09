let articles = []

let articlesList = []


articles.forEach(article => {
    articlesList.push(article)
})

document.querySelector(".generate").addEventListener("click", generate)

function generate() {
    articleFourHundred = document.querySelector("input[name='article_four_hundred']")
    articleSixHundred = document.querySelector("input[name='article_six_hundred']")
    articleEightHundred = document.querySelector("input[name='article_eight_hundred']")
    articleOneThousand = document.querySelector("input[name='article_one_thousand']")
    articleTwoThousand = document.querySelector("input[name='article_two_thousand']")


    max = Math.max(articlesList)

    articleFourHundred.value =  max + 1
    articleSixHundred.value = max + 2
    articleEightHundred.value = max + 3
    articleOneThousand.value = max + 4
    articleTwoThousand.value = max + 5
}