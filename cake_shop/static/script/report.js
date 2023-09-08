function add_report() {
    let report_form = document.querySelector("#report_form")
    report_form.addEventListener("submit", (e) => {
        e.preventDefault();

        console.log("fghjkl");
        const request = new XMLHttpRequest();

        const url = `${window.location.href}${report_form.getAttribute("action")}`;
        console.log(url);

        request.open("POST", url, true);
        request.send();
    })
}
export { add_report };