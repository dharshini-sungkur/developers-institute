// exercise1
// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}
// #1.1 - run in the console:
funcOne()  //inside the funcOne function 3
// #1.2 What will happen if the variable is declared with const instead of let ?
// Uncaught TypeError: Assignment to constant variable.


// #2
const a = 0;
function funcTwo() {
    a = 5;
}
function funcThree() {
    alert(`inside the funcThree function ${a}`);
}
// #2.1 - run in the console:
funcThree()  //inside the funcThree function 0
funcTwo()
funcThree()  //inside the funcThree function 5
// #2.2 What will happen if the variable is declared with const instead of let ?
// Uncaught TypeError: Assignment to constant variable.


// #3
function funcFour() {
    window.a = "hello";
}
function funcFive() {
    alert(`inside the funcFive function ${a}`);
}
// #3.1 - run in the console:
funcFour()
funcFive()  //inside the funcFive function hello


// #4
const a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}
// #4.1 - run in the console:
funcSix()  //inside the funcSix function test
// #4.2 What will happen if the variable is declared with const instead of let ?
// Uncaught TypeError: Assignment to constant variable.
// inside the funcSix function test


//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);
// #5.1 - run the code in the console
// in the if block 5
// outside of the if block 2
// #5.2 What will happen if the variable is declared with const instead of let ?
// Uncaught TypeError: Assignment to constant variable.
// in the if block 5
// outside of the if block 2



//exercise2
let winBattle = () =>  true ;
console.log(winBattle ?  10:  1)



//exercise3
let isString = (text) =>  typeof text === 'string'? true : false ;
console.log(isString('hello')); 
//true
console.log(isString([1, 2, 4, 0]));
//false



//exercise4
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach((num, index) => console.log(`${index + 1}# choice is ${num}`))
console.log(colors.some((color) => color === 'Violet') ? "Yeah": "No...")



//exercise5
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];
colors.forEach((num, index) => index > 2 ? console.log(`${index + 1}${ordinal[0]} choice is ${num}`) : console.log(`${index + 1}${ordinal[index + 1]} choice is ${num}`))



//exercise6
let bankAmount = 1200
const vat = 12
const details = ["+200", "-100", "+146", "+167", "-2900"]
details.forEach((amt) => {
        sign = amt[0]
        amount = Number(amt.substring(1))
        sign == "+"? bankAmount = (bankAmount + amount): bankAmount = (bankAmount - amount - (amount * vat / 100))
})
console.log(bankAmount)