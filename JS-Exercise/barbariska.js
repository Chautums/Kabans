// const personBoxElementObject = document.querySelector('.js-person-box');
// personBoxElementObject.innerHTML = `<h1 class="js-heading" style="color: gold">Seržs</h1>`
// personBoxElementObject.innerHTML += `<img src="https://thumbs.dreamstime.com/b/pizza-rustic-italian-mozzarella-cheese-basil-leaves-35669930.jpg" width="200" height="200" />`
// const headingElementObject = document.querySelector('.js-heading')
// headingElementObject.classList.add('active')

const boxElementObject = document.querySelector(".js-box")
console.log("boxElementObject", boxElementObject(0));
boxElementObjects[0].style.width = "200px"
boxElementObjects[0].style.height = "200px"
boxElementObjects[0].style.margin = "10px"
boxElementObjects[0].style.backgroundColor = "red"

boxElementObjects[1].style.width = "200px"
boxElementObjects[1].style.height = "200px"
boxElementObjects[1].style.margin = "10px"
boxElementObjects[1].style.backgroundColor = "red"

boxElementObjects[2].style.width = "200px"
boxElementObjects[2].style.height = "200px"
boxElementObjects[2].style.margin = "10px"
boxElementObjects[2].style.backgroundColor = "red"

boxElementObjects.forEach((element) => {
    element.style.width = "200px",
    element.style.height = "200px",
    element.style.margin = "10px",
    element.style.backgroundColor = "red";
  })