//exercise 1
const fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

fruits.splice(0,1);
fruits.sort();
fruits.push("Kiwi");
fruits.shift();
fruits.reverse();
console.log(fruits);


//exercise 2
const moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(moreFruits[1][1][0]);