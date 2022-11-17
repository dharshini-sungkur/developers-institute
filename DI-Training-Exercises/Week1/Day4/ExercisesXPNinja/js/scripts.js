//exercise1
function calculateBMI ( mass, height ) {
    return mass / (height * height / 10000);
}

const person1 = {
    FullName: "Dharshini Sungkur",
    Mass: 55,
    Height: 159,
    BMI: calculateBMI(this.Mass, this.Height)
};
const person2 = {
    FullName: "Shrutee Balgobhind",
    Mass: 62,
    Height: 153,
    BMI: calculateBMI(this.Mass, this.Height)
};

if (person1.BMI > person2.BMI) {
    console.log(person1.FullName);
} else {
    console.log(person2.FullName);
}


//exercise2
function findAvg(gradesList) {
    let avg = 0;
    for (let grade of gradesList) {
        avg += grade;
    }
    avg = avg/gradesList.length;

    if (greaterThan(avg, 65)) {
        console.log("You have passed");
    } else {
        console.log("You have failed");
    }
}

function greaterThan (num1, num2) {
    return num1 > num2;
}

let gradesList = [77,12];
findAvg(gradesList);

