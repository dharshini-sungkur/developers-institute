//exercise1
function isBlank (text) {
    if (text == "") {
        console.log("String '" + text + "' is blank");
    } else {
        console.log("String '" + text + "' is not blank");
    }
}
isBlank("");
isBlank("abc");
isBlank(``);


//exercise2
function abbrevName (text) {
   console.log(text.split(" ")[0] + " " + text.split(" ")[1][0] + ".")
}
abbrevName("Robin Singh");
abbrevName("Dharshini Sungkur");
abbrevName(`Shrutee Balgobhind`);


//exercise3
function swapcase (text) {
    let newtext = "";
    for (i in text) {
        if (text[i] == text[i].toUpperCase()) {
            newtext += text[i].toLowerCase();
        } else {
            newtext += text[i].toUpperCase();
        }
    }
    console.log(newtext)
}
swapcase("The Quick Brown Fox");


//exercise5
function isOmnipresent (array, element) {
    present = true;
    for ( i in array) {
        if ( !array[i].includes(element) ) {
            present = false
            break;
        }
    }
    console.log(present)
}
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1)
isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)
