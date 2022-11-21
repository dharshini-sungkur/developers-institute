# exercise1
print("Hello world\n"*4)

# exercise2
print(pow(99,3) * 8)

# exercise3
print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
# print("3" > 3) #Typeerror
print("Hello" == "hello") #False

# exercise4
computer_brand = "hp"
print("I have a",computer_brand,"computer")

# exercise5
name = "Dharshini"
age = 22
shoe_size = 38
info = f"{name} aged {age} years old, wears a shoe size of {shoe_size}"
print(info)

# exercise6
a = 30
b = 20
if a < b :
    print("Hello World")

# exercise 7
number = int(input("\nEnter a number: "))
if number % 2 == 0 :
    print("even")
else:
    print("odd")
        
# exercise 8
my_name = "dharshini"
your_name = input("\nWhat is you name? ").lower()
if my_name == your_name :
    print("We have the same name")
else:
    print("We don't have the same name")
    
# exercise 9
height = int(input("\nEnter your height in cms: "))
if height > 145 :
    print("You are tall enough to ride")
else:
    print("You need to grow some more to ride")
    