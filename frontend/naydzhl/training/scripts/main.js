/*
осторожно нацысты следят за вами!
*/
var myImage = document.querySelector("img");

myImage.onclick = function () {
    var mySrc = myImage.getAttribute("src");
    if (mySrc === "images/img2.png") {
        myImage.setAttribute("src", "images/img2.png");
    } else {
        myImage.setAttribute("src", "images/fon.png");
    }
};
var myButton = document.querySelector("button");
var myHeading = document.querySelector("h1");
function setUserName() {
    var myName = prompt("Please enter your name.");
    localStorage.setItem("name", myName);
    myHeading.textContent = "СРОЧНО ПИВА БЛЯТЬ, " + myName;
}
if (!localStorage.getItem("name")) {
    setUserName();
} else {
    var storedName = localStorage.getItem("name");
    myHeading.textContent = "СРОЧНО ПИВА БЛЯТЬ, " + storedName;
}
myButton.onclick = function () {
    setUserName();
  };
myImage.onclick = function () {
    
}