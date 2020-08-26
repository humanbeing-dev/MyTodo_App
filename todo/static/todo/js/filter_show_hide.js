function element_show(names) {

    console.log(names)
    for (let name in names) {
        let element = document.getElementById(names[name])
        if (element.style.display === "block") {
            element.style.display = "none";
        } else {
            element.style.display = "block";
        }
    }
}