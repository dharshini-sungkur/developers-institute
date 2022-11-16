let sentence = "This movie is not so bad !";
let wordNot = sentence.indexOf("not");
let wordBad = sentence.indexOf("bad");

let result = sentence;

if ((wordBad > wordNot) && (wordNot != -1) && (wordBad != -1)) { 
    result = result.slice(0,wordNot) + "good" + sentence.slice(wordBad + 3);
}

console.log(result);