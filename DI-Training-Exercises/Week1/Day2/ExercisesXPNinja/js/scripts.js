//exercise 1

console.log(5 >= 1);
// Prediction: true
// Actual: true

console.log(0 === 1);
// Prediction: false
// Actual: false

console.log(4 <= 1);
// Prediction: false
// Actual: false

console.log(1 != 1);
// Prediction: false
// Actual: false

console.log("A" > "B");
// Prediction: false
// Actual: false

console.log("B" < "C");
// Prediction: true
// Actual: true

console.log("a" > "A");
// Prediction: true
// Actual: true

console.log("b" < "A");
// Prediction: false
// Actual: false

console.log(true === false);
// Prediction: false
// Actual: false

console.log(true != true);
// Prediction: false
// Actual: false


//exercise 2
let input = prompt("Enter a list of numbers separated by commas", "2,3");
let inputArray = input.split(",");

let sum = 0;

for(let i = 0; i < inputArray.length; i++)
{
    sum += parseInt(inputArray[i]);
}
console.log(sum);


//exercise 3
let text = prompt("Enter a sentence containing the word 'Nemo'", "Nemo is a cute fish.");
let found = text.indexOf("Nemo");
if ( found >= 0 )
{
    let position = text.split("Nemo")[0].split(" ").length - 1 ;
    console.log(`I found Nemo at ${position}`);
}
else
{
    console.log("I can't find Nemo");
}


//exercise 4
let num = parseInt(prompt("Enter a number",10));
let output;
if (num < 2) 
{
    output = "boom";
}
else if (num > 2)
{
    output = "b" + "o".repeat(num) + "m";
}
if (num % 2 == 0)
{
    output += "!";
}
if (num % 5 == 0)
{
    output = output.toUpperCase();
}

console.log(output)