document.addEventListener("DOMContentLoaded", function (event) {

    let elem = document.querySelector('#navbar-collapsible')
    elem.style.display = "none";
 
    let backToTopButton = document.querySelector(".top");
    if(backToTopButton)
      backToTopButton.className = "top hide-top"

    elem = document.querySelector('button.navbar-toggler')

    elem.addEventListener("click", myFunction);

    function myFunction() {
        let elem = document.querySelector('#navbar-collapsible')
        if (elem.style.display === "none") {
            elem.style.display = "block";
        } else {
            elem.style.display = "none";
        }
    }

    backToTopButton = document.querySelector(".top");

    var myScrollFunc = function () {
        var y = window.scrollY;
        if (y >= 600) {
            backToTopButton.className = "top show-top"
        } else {
            backToTopButton.className = "top hide-top"
        }
    };

    window.addEventListener("scroll", myScrollFunc);
});

