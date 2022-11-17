//exercise1
const people = ["Greg", "Mary", "Devon", "James"];
people.shift();
people[2] = "Jason";
people.push("Dharshini");
console.log(people.indexOf("Mary"));
let copypeople = people.slice(1,3);
console.log(copypeople);

console.log(people.indexOf("Foo"));
let last = people.slice(-1);
//index of last = length - 1

console.log(last);

for (let p of people) {
    console.log(p);
}
console.log("");
for (let p of people) {
    if (p == "Jason") {
        console.log(p);
        break;
    }
}


//exercise2
const colors = ["Blue", "Red", "White", "Yellow", "Black"];
const suffix = ["st","nd","th","th","th","th"]
for (let c in colors) {
    console.log(`My ${Number(c)+1}${suffix[c]} choice is ${colors[c]}`);
}


//exercise3
do{
    var num = prompt("Enter a number:",0);
} while (Number(num) != num)

do{
    var num = prompt("Enter a number less than 10:",0);
} while ((Number(num) != num) || num >= 10)


//excercise4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors);
console.log(building.numberOfAptByFloor.firstFloor);
console.log(building.numberOfAptByFloor.thirdFloor);
console.log(building.nameOfTenants[1] + " " + building.numberOfRoomsAndRent.dan[0]);

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
console.log(building);


//exercise5
const family = {
    0: "dharshini", 
    1: "shrutee", 
    2: "ameer"
}
for (let f in family) {
    console.log(f);
}
for (let f in family) {
    console.log(family[f]);
}


//exercise6
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

let text = '';
for (let d in details) {
    text += d + " " + details[d] + " ";
}
console.log(text);


//exercise7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();

let newname = '';
for( let name of names) {
    newname += name[0];
}
console.log(newname);