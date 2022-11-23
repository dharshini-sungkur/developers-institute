import math
import random

# exercise1
C = 50
H = 30
numbers = input("Enter list of numbers each separated by comma: ").split(",")
results=[]
for i in numbers :
    results.append(int(math.sqrt(2 * C * int(i)/ H)))
print(results)


# exercise2
list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 

list2.clear()
count = 0
while count < 10:
    number = int(input("Enter a numbers from -100 to 100: "))
    if number >= -100 and number <= 100 :
        list2.append(number)
        count += 1
    
list2.clear()
numbers = random.randint(50, 100)
for i in range(0, numbers):
    list2.append(random.randint(-100, 100))

print("\nnumbers:", *list2)

print("\nnumbers in descending order:", sorted(list2,reverse=True))

print("\nsum:", sum(list2))

outputList = []

outputList.append(list2[0])
outputList.append(list2[-1])
print("\nfirst and last numbers:", outputList)

outputList.clear()
for i in list2:
    if i > 50:
        outputList.append(i)
print("\nnumbers > 50:", outputList)

outputList.clear()
for i in list2:
    if i < 10:
        outputList.append(i)
print("\nnumbers < 10:", outputList)

outputList.clear()
for i in range(0, len(list2)):
    outputList.append(pow(list2[i], 2))
print("\nsquared numbers:", outputList)

outputList.clear()
outputList = list(dict.fromkeys(list2))
print("\nList without duplicates:", outputList)

print("\naverage:", int(sum(list2)/ len(list2)))

print("\nsmallest:", min(list2))

print("\nlargest:", max(list2))


# exercise3
paragraph = "A while back I needed to count the amount of letters that a piece of text in an email template had (to avoid passing any character limits). Unfortunately, I could not think of a quick way to do so on my macbook and I therefore turned to the Internet. There were a couple of tools out there, but none of them met my standards and since I am a web designer I thought: why not do it myself and help others along the way? And... here is the result, hope it helps out!"
characters = len(paragraph)
print("Number of characters:", characters)
words = paragraph.split(" ")
print("Number of words:", len(words))
print("Number of non-whitespace characters:", len(paragraph.replace(" ","")))
print("Number of unique words:", len(list(dict.fromkeys(words))))
print("Number of non-unique words:", len(words) - len(list(dict.fromkeys(words))))
sentence = 0
previous_character = ""
for i in paragraph:
    if i in [".", "!", "?"] :
        if i != previous_character :
            sentence += 1
        previous_character = i
print("Number of sentences:", sentence)
print("Average number of words in sentences:", len(words)/sentence)



# exercise4
sentence = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
sentence = input("\nEnter a sentence: ")
words = list(dict.fromkeys(sentence.split(" ")))
for i in words:
    print(i, ":", sentence.count(i))
