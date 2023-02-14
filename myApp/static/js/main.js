// let navigation = document.querySelector('.navigation');
// let nav_bar = document.querySelector('.nav--bar');
// document.querySelector('.toggle').onclick = function() {
//     this.classList.toggle('active');
//     navigation.classList.toggle('active');
// }
// document.querySelectorAll('.nav--bar').onclick = function() {
//     this.classList.toggle('active');
//     navigation.classList.toggle('active');
// }


const text = document.querySelector(".auto-type");
const textload = () => {
    setTimeout(() => {
        text.textContent = "Youtube";
    }, 0)
    setTimeout(() => {
        text.textContent = "Developer";

    }, 4000)
    setTimeout(() => {
        text.textContent = "Frontend";

    }, 8000)
}
textload()
setInterval(textload, 12000);


const menu = document.querySelector(".navigationa").onclick = () => {
    menu.classList.toggle(".navigationap");
}