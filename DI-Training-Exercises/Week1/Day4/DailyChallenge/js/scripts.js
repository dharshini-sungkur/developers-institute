for (let i = 0; i < 10; i ++) {
    console.log("* ".repeat(i + 1));
}

for (let i = 1; i <= 10; i ++) {
    let sentence = '';
    for (let j = 0; j < i; j++) {
        sentence = sentence + '* ';
    }
    console.log(sentence);
}