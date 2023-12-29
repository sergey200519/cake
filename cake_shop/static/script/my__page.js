
const droparea = document.querySelector('.mypage__photo__left');
const mypagePhotoI = document.querySelector("#mypage__photoi")

let fileRead = new FileReader()

fileRead.onload = () => {
    document.querySelector(".mypage__photo__link img").src = fileRead.result
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    fileRead.readAsDataURL(files[0])
}

const prevents = (e) => e.preventDefault();

['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evtName => {
    droparea.addEventListener(evtName, prevents);
});

droparea.addEventListener("drop", handleDrop);
mypagePhotoI.addEventListener("input", () => {
    fileRead.readAsDataURL(mypagePhotoI.files[0]);
})

const genderInputs = document.querySelectorAll(".form__style__gender_p input")
const gender = document.querySelector(".profile_gender")
setGender()
setDate()
genderInputs.forEach(input => {
    input.addEventListener("input", getGender)
})

function getGender() {
    console.log("pGender");
    genderInputs.forEach(input => {
        if (input.checked) {
            let label = document.querySelector(`label[for='${input.id}']`)
            let labelText = label.textContent
            if (labelText == "Мужской") gender.value = "M"
            else gender.value = "W"
        }
    });
}

function setGender() {
    if (gender.value == "M") genderInputs[0].checked = true
    else genderInputs[1].checked = true
}

function setDate() {
    const dbDate = document.querySelector(".user_date_of_birth").textContent.split(".")
    let date = new Date(dbDate[2], dbDate[1] - 1, dbDate[0])
    document.querySelector(".date_of_birth_profile").value = date.toISOString().substring(0,10)
}