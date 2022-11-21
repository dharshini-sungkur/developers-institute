import random

string = input("\nEnter a string of 10 characters: ")
numCharacters = len(string.replace(" ", ""))
if numCharacters > 10 :
    print("string too long")
elif numCharacters < 10 :
    print("string not long enough")    
else:
    print("First character:",string[0])
    print("Last character:",string[-1])
    
    output = ""
    for i in range(len(string)):
        
        if string[i] != " " :
            output += string[i]
            print(output)
        else:
            output += string[i]
    
    shuffled = list(string.replace(" ", ""))
    random.shuffle(shuffled)
    print("Shuffled word:",''.join(shuffled))