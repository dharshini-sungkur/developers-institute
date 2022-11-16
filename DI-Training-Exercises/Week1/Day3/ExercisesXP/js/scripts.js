//exercise1
let x = 5;
let y = 2;

if (x > y) {
    console.log(x);
}
else {
    console.log(y);
};


//exercise2
let newDog = "Chihuahua";
let letters = newDog.length;

console.log(letters);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());

if (newDog == "Chihuahua"){
    console.log('I love Chihuahuas, it’s my favorite dog breed');
}
else {
    console.log('I dont care, I prefer cats');
};


//exercise3
let num = Number(prompt(`Enter a number`,0));
if (num % 2 == 0) {
    console.log(`${num} is an even number`)
}
else {
    console.log(`${num} is an odd number`)
};


//exercise4
const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numUsers = users.length;

switch (numUsers) {
    case 0:
        console.log(`no one is online`);
        break;
    case 1:
        console.log(`${users[0]} is online`);
        break;
    case 2:
        console.log(`${users[0]} and ${users[1]} are online`);
        break;
    default:
        console.log(`${users[0]}, ${users[1]} and ${numUsers - 2} more are online`);
        break;
}