console.log("Hello World")

function displayDate(id) {
    document.getElementById("date").innerHTML = Date();
}

function checkCookies() {
    let text = "";
    if (navigator.cookieEnabled === true) {
        text = "Cookies are enabled";
    } else {
        text = "Cookies are not enabled";
    } document.getElementById("cookie").innerHTML = text;
}

function sendAlert() {
    alert(location.hostname);
}

function mOver(){
    document.getElementById("title").style.color="pink";
}

function mOut(){
    document.getElementById("title").style.color="black";
}

function darkMode() {
    let page = document.getElementById("swap")
    page.classList.toggle("dark-mode");
}