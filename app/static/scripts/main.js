divs = document.querySelectorAll("#long-q>div");
console.log(divs)
divs.forEach(q => {
    console.log(q.nextElementSibling);
    q.addEventListener("input", function(e){
        alter = q.nextElementSibling.querySelectorAll("label, select, option");
        alter.forEach(element => {
            console.log(element);
            element.style.display = "block";
        }
        )
        q.nextElementSibling.style.display = "block";
    })
});