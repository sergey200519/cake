
new Accordion('.accordion-container')

import { MoreList } from "./moreList.js"

let clouse_it = ""

const lists = document.querySelectorAll(".list__cakes")

lists.forEach(list => {
    console.log(list);
    new MoreList(list, 8, clouse_it)
})


// new MoreList(".list__cakes", 8, clouse_it)
// второй блок
// new MoreList(".list__cakes__two", 8, clouse_it)
