let imgCont = document.querySelector(".img-container");
let imgLike = document.querySelector(".img-like");
let hrtIcn = document.querySelector(".ri-heart-line");

imgCont.addEventListener("dblclick", () => {
    imgLike.style.display = "block";

    setTimeout(() => {
        imgLike.style.display = "none";
    }, 1500);

    hrtIcn.classList.remove("ri-heart-line");
    hrtIcn.classList.add("ri-heart-fill");
});

