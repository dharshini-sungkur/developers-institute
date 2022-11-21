// //exercise1
// function infoAboutMe() {
//     console.log("Hello my name is Dharshini Sungkur. I am 22 years old.");
// }
// infoAboutMe();

// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//     console.log(`Your name is ${personName}, you are ${personAge} years old. your favorite color is ${personFavoriteColor}.`);
// }
// infoAboutPerson("David", 45, "blue");
// infoAboutPerson("Josh", 12, "yellow");


// //exercise2
// function calculateTip(){
//     let bill = Number(prompt("Enter the bill amount:",0));
//     let tip = 0;
//     if (bill < 50) {
//         tip = bill * 0.2;
//     } else if (bill < 200) {
//         tip = bill * 0.15;
//     } else {
//         tip = bill * 0.1;
//     }
//     console.log(tip+bill);
// }
// calculateTip();


// //exercise3
// function isDivisible(divisor){
//     let sum = 0;
//     let outcome = '';
//     for (let i = 0; i <= 500; i++) {
//         if (i % divisor == 0) {
//             outcome += i + " ";
//             sum += i;
//         }
//     }
//     console.log("Outcome: " + outcome);
//     console.log("Sum: " + sum);
// }
// isDivisible(3);
// isDivisible(45);



// //exercise4
// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// }

// const shoppingList = ["banana", "orange", "apple"];

// function myBill() {
//     let bill = "";
//     for(let item of shoppingList){
//         if (stock[item] > 1) {
//             bill +="\n" + item + ": $" + prices[item];
//             stock[item] = stock.item - 1;
//         }
//     }
//     console.log(bill);
// }

// myBill();


// //exercise5
// function changeEnough(itemPrice, amountOfChange) {
//     let sum = 0;
//     let change = [0.25, 0.10, 0.05, 0.01];
//     for (let i in amountOfChange) {
//         sum += change[i] * amountOfChange[i];
//     }
//     if (itemPrice <= sum) {
//         return true;
//     } else {
//         return false;
//     }
// }
// console.log(changeEnough(4.25, [25, 20, 5, 0]));
// console.log(changeEnough(14.11, [2,100,0,0]));
// console.log(changeEnough(0.75, [0,0,20,5]));


//exercise6
function hotelCost(nights) {
    return 140 * nights
}

function planeRideCost(destination) {
    if (destination == "london") {
        return 183
    } else if (destination == "paris") {
        return 220
    } else {
        return 300
    }
}

function rentalCarCost(days) {
    if (days <= 10) {
        return 40 * days
    } else {
        return 40 * days * 0.95
    }   
}

function totalVacationCost() {
    let days = 0
    let destination = ""
    let nights = 0

    do {
        nights = Number(prompt("Enter number of nights you would like to stay in the hotel: ",0))
    } while (isNaN(nights) || nights < 1)

    do {
        days = Number(prompt("Enter number of days you would like to rent the car: ",0))
    } while (isNaN(days) || days < 1)

    do {
        destination = prompt("Enter your destination: ","").toLowerCase()
    } while (!isNaN(destination) || destination.length < 1)

    console.log(`The car cost: $${rentalCarCost(days)}, the hotel cost: $${hotelCost()}, the plane tickets cost: $${planeRideCost()}`)
}

totalVacationCost()

