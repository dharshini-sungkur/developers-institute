
//exercise 1
let sentence = ["my","favorite","color","is","blue"];
console.log(sentence.join());


//exercise 2
let str1 = "Hello";
let str2 = "World";

let str3 = str1;
str1 = str2.slice(0,2) + str1.slice(2);
str2 = str3.slice(0,2) + str2.slice(2);

str3 = str1 + " " + str2;
console.log(str3);


//exercise 3
let firstnum = parseInt(prompt("Input your first number",0));
let secondnum = parseInt(prompt("Input your second number",0));
let output = firstnum + secondnum;
let op = prompt("Input your arithmetic operator (+, -, *, /, %)",0);

switch (op) {
    case "+": output = firstnum + secondnum; break;
    case "-": output = firstnum - secondnum; break;
    case "*": output = firstnum * secondnum;break;
    case "%": output = firstnum % secondnum;break;
    case "/": output = firstnum / secondnum;break;
    default: alert("unrecognised operation"); break;
}


alert(`${firstnum} ${op} ${secondnum} = ${output}`);