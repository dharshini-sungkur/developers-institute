// exercise 1
let favouriteFood = "chocolate";
let favouriteMeal = "lunch";

console.log(`I eat ${favouriteFood} at every ${favouriteMeal}.`);


// exercise 2
const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.slice(0,myWatchedSeriesLength - 1).toString() + " and " + myWatchedSeries[myWatchedSeriesLength - 1 ];

console.log(`I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}.`);

myWatchedSeries[2] = "Friends";
myWatchedSeries.push("The boys");
myWatchedSeries.unshift("The originals");
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1][2]);
console.log(myWatchedSeries);


// exercise 3
let tempC = 24;
let tempF = (tempC / 5 * 9) + 32;
console.log(tempC + " degrees celcius is " + tempF + " degrees fahrenheit is " )


// exercise 4
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55 (34+21)
// Actual: 55

a = 2;
console.log(a+b) //second expression
// Prediction: 23 (21+2)
// Actual: 23

//c is undefined

console.log(3 + 4 + '5');
// Prediction: 75
// Actual: 75


//exercise 5
console.log(typeof(15));
// Prediction: integer
// Actual: number

console.log(typeof(5.5));
// Prediction: double
// Actual: number

console.log(typeof(NaN));
// Prediction: number
// Actual: number

console.log(typeof("hello"));
// Prediction: string
// Actual: string

console.log(typeof(true));
// Prediction: boolean
// Actual: boolean

console.log(typeof(1 != 2));
// Prediction: boolean
// Actual: boolean

console.log("hamburger" + "s");
// Prediction: hamburgers
// Actual: hamburgers

console.log("hamburgers" - "s");
// Prediction: NaN
// Actual: NaN

console.log("1" + "3");
// Prediction: 13
// Actual: 13

console.log("1" - "3");
// Prediction: NaN
// Actual: -2

console.log("johnny" + 5);
// Prediction: johnny5
// Actual: johnny5

console.log("johnny" - 5);
// Prediction: NaN
// Actual: NaN

console.log(99 * "hello");
// Prediction: NaN
// Actual: NaN

console.log(1 != 1);
// Prediction: false
// Actual: false

console.log(1 == "1");
// Prediction: true
// Actual: true

console.log(1 === "1");
// Prediction: false
// Actual: false



//exercise 6
console.log("exercise 6");
console.log(5 + "34");
// Prediction: 534
// Actual: 534

console.log(5 - "4");
// Prediction: NaN
// Actual: NaN

console.log(10 % 5);
// Prediction: 0
// Actual: 0

console.log(5 % 10);
// Prediction: 5
// Actual: 5

console.log("Java" + "Script");
// Prediction: JavaScript
// Actual: JavaScript

console.log(" " + " ");
// Prediction:
// Actual:

console.log(" " + 0);
// Prediction: 0
// Actual: 0

console.log(true + true);
// Prediction: 2
// Actual: 2

console.log(true + false);
// Prediction: 1
// Actual: 1

console.log(false + true);
// Prediction: 1
// Actual: 1

console.log(false - true);
// Prediction: NaN
// Actual: -1

console.log(!true);
// Prediction: false
// Actual: false

console.log(3 - 4);
// Prediction: -1
// Actual: -1

console.log("Bob" - "bill");
// Prediction: NaN
// Actual: NaN


