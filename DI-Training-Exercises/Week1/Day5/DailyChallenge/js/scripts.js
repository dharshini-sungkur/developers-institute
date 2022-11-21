words = prompt("Enter several words separated by commas","Hello, World, in, a, frame").replace(/\s+/g, '').split(",")

longest = 0;
for (i of words) {
    if (i.length > longest) {
        longest = Number(i.length)
    }
}

console.log("*".repeat(longest+4));
for (i of words) {
    console.log("* " + i + " ".repeat(longest - i.length) + " *")
}
console.log("*".repeat(longest+4));