//exercise1
let first = Number(prompt("Enter the birth year of the first person",2000));
let second = Number(prompt("Enter the birth year of the second person",2000));
let output;

if (first > second) {
    let age = first - second;
    let year = age + first;
    output = "the youngest was born in " + first + " and the oldest in " + second + " the oldest was/ will be twice the age of the youngest in " + year;
}
else if (first < second) {
    let age = second - first;
    let year = age + second;
    output = "the youngest was born in " + second + " and the oldest in " + first + " the oldest was/ will be twice the age of the youngest in " + year;
}
else {
    output = "they were born in the same year";
}

console.log(output);


//exercise2
//without regex
let zcode = String(prompt("Enter your zip code (should consist of only 5 numbers, no whitespace, no letters)","00000"));

if (zcode.length != 5) {
    console.log("error");
}
else if (zcode.indexOf(" ") != -1) {
    console.log("error");
}
else if (parseInt(zcode) != zcode) {
    console.log("error");
}
else {
    console.log("success");
}

//with regex
const pattern = /\b\d{5}\b/;
let iszcode = pattern.test(zcode);
if (iszcode) {
    console.log("success");
}
else {
    console.log("error");
}


//exercise3
let word = prompt("Enter word:","word");
const reg = /[aeiou]/gi;
//word = word.replace(reg, "");
word = word.replace(/a/gi, 1);
word = word.replace(/e/gi, 2);
word = word.replace(/i/gi, 3);
word = word.replace(/o/gi, 4);
word = word.replace(/u/gi, 5);
console.log(word);