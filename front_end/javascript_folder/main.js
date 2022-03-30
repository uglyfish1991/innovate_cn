console.log("hello world");

// Data Types
let dataType="This is a string"
dataType=13 // This is now a number

console.log(typeof(dataType))


// Variables
var firstNamme="Katy"; //var is legacy code

let firstName="Katy"; //variable that can be changed
firstName="Katherine"; // not creating a new variable - just changing it

let lastName="Long";

const placeOfBirth="Liverpool";

console.log(placeOfBirth)

if (placeOfBirth === "Liverpool") {
    console.log("I was born in Liverpool")
} else {
    console.log("Where?")
}

// && - and
// || - or

if (firstName=="Katherine" && lastName=="Long"){
    console.log("My full name is Katherine Long");
} else {
    console.log("Who is this");
}

function myFunction() {
    console.log("This is a JS function");
}

myFunction()

// String interpolation - like an f string

console.log(`My name is ${firstName} ${lastName}`);

let genshinTeam=["Rosaria","Xingqiu","Fischl","Zhongli"];

console.log(genshinTeam);
console.log(genshinTeam[2]);

// Loops
let text=""
for (let i=0; i<5; i++) {
    text ="the number is " +i;
    console.log(text)
}

let i=0
while (i <10) {
    text ="the number is " +i
    console.log(text)
    i++;
}

// Switch statements

let fruit = "apple"
switch (fruit) {
    case "grape":
        console.log("grape");
        break;
    case "orange":
        console.log("orange");
        break;
    case "apple":
        console.log("apple");
        break;
    default:
        console.log("No.")
}

// Arrow Functions

hello = () => {
    console.log("Hello World!");
}

hello()