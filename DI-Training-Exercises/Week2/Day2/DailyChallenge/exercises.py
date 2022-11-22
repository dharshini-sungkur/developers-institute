# exercise1
number = int(input("Enter a number: "))
length = int(input("Enter length: "))
multiples = []
for i in range (1,length+1) :
    multiples.append(number * i)
print(multiples)


# exercise2
word = input("Enter a word: ")
newword = ""
character = ""
for i in range (0,len(word)) :
    if i != 0 :
        character = word[i-1]
    if character != word[i] :
        newword += word[i]
print(newword)
