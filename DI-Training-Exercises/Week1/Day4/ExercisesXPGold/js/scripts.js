//exercise1
let numbers = [123, 8409, 100053, 333333333, 7];
for (let number of numbers) {
    console.log( (number % 3) == 0)
}


//exercise2
let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

let student = prompt("Enter your name",'karla').toLowerCase();
if (guestList[student] != undefined) {
    console.log("Hi! I'm " + student + ", and I'm from "+ guestList[student]);
} else {
    console.log("Hi! I'm a guest.");
}


//exercise3
let age = [20,5,12,43,98,55];

let highest = 0;
let sum = 0;
for ( let a of age) {
    sum = sum + a;
    if (a > highest) {
        highest = a;
    }
}

console.log(sum);
console.log(highest);
