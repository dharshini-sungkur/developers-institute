import random
# exercise1
list1 = [ 1, 2, 3, 4]
list2 = [ 5, 6, 7, 8]
list1.extend(list2)
print(list1)


# exercise2
for i in range (1500, 2501):
    if i % 5 == 0 or i % 7 == 0 :
        print(i, end = "\t")
        

# exercise3
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name = input("\nEnter your name: ")
if name in names :
    print(names.index(name))


# exercise4
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3 :
    print("The greatest number is",num1)
elif num2 > num3 :
    print("The greatest number is",num2)
else :
    print("The greatest number is",num3)


# exercise5
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, len(alphabets)) :
    if alphabets[i] in ["A", "E", "I", "O", "U"] :
        print(alphabets[i],"is a vowel")
    else:
        print(alphabets[i],"is a consonant")
 

# exercise6
words = []
for i in range(0, 7) :
    words.append(input("Enter a word: "))
letter = input("Enter a letter: ")
for i in words :
    if letter in [*i] :
        print([*i].index(letter))
    else:
        print(letter,"does not exist in",i)
        

# exercise7
numbers = range(1,1000001) #Note that range gives you a number UP TO the last number
print(max(numbers))
print(min(numbers))
print(sum(numbers))


# exercise8
numbers = input("Enter some numbers separated by comma:").split(",")
print(numbers)
print(tuple(numbers))


# exercise9
guess = ""
loss = 0
win = 0
while guess != "quit" :
    ran= random.randint(1, 9)
    guess = input("\nEnter your guess (a number from 1 to 9) or enter 'quit' to exit:\n").lower()
    if guess != "quit" :
        if int(guess) == ran :
            win += 1
            print("Winner")
        else:
            loss += 1
            print("Better luck next time")
print("wins:",win," loss:",loss)



    