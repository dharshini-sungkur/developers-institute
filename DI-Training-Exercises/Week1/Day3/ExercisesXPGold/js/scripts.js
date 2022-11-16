//exercise1
let language = prompt("Enter which language do you speak:","English/ French/ Hebrew");
language = language.toLowerCase();

switch (language) {
    case "french":
        console.log(`Bonjour`);
        break;
    case "english":
        console.log(`Hello`);
        break;
    case "hebrew":
        console.log(`Shalom`);
        break;
    default:
        console.log(`01110011 01101111 01110010 01110010 01111001`);
        break;
}


//exercise2
let grade = Number(prompt("Enter your grade:","0"));

if(grade > 100 || grade < 0) {
    console.log('Invalid');
}
else if(grade > 90) {
    console.log('A');
}
else if(grade > 80) {
    console.log('B');
}
else if(grade >= 70) {
    console.log('C');
}
else {
    console.log('D');
}


//exercise3
let verb = prompt("Enter a verb:","swimming");

if (verb.length < 3){
    console.log(verb);
}
else if (verb.endsWith("ing")) {
    console.log(verb+`ly`);
}
else {
    console.log(verb+`ing`);
};