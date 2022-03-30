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
    console.log("My full name is Katherine Long")
} else {
    console.log("Who is this")
}

function myFunction() {
    console.log("This is a JS function")
}

myFunction()