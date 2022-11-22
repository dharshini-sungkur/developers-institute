# exercise1
my_fav_numbers = set()
my_fav_numbers.add(12)
my_fav_numbers.add(48)
my_fav_numbers.add(3)
my_fav_numbers.add(5)
my_fav_numbers.discard(5)

friend_fav_numbers  = set()
friend_fav_numbers .add(6)
friend_fav_numbers .add(31)
friend_fav_numbers .add(13)
friend_fav_numbers .add(7)

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)


# exercise2
integers = (1,2,3,4)
integers = integers.__add__((5,6))
print(integers)
# tuples are immutable, cannot add more integers, but we can concatenate 2 tuples and save in a new tuple


# exercise3
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


# exercise4
# The float type represents the floating point number. Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts.
sequence = []
x = 1
for i in range(1,8) :
    x += 0.5
    sequence.append(x)
print(sequence)


# exercise5
for i in range(1,21):
    print(i)
for i in range(2,21,2):
    print(i)
    
    
# exercise6
my_name = "dharshini"
your_name = ""
while your_name != my_name :
    your_name = input("\nEnter your name: ").lower()
    
# exercise7
fruits = input("\nEnter your favorite fruits (separate the fruits with a single space): ").split(" ")
fruit = input("Enter the name of any fruit: ")

if fruit in fruits :
    print("You chose one of your favorite fruits! Enjoy!")
else :
    print("You chose a new fruit. I hope you enjoy")
    
    
# exercise8   
topping = ""
toppings = []
while topping != "quit" :
    topping = input("\nEnter a topping for your pizza or enter 'quit' to exit: ").lower()
    if topping != "quit" :
        toppings.append(topping)
print(toppings)
price = 10
for t in toppings :
    price += 2.5 
print("Price of your pizza: $",price)


# exercise9 
person = ""
family = []
while person != "quit" :
    person = input("Enter age of a person or enter 'quit' to exit: ").lower()
    if person != "quit" :
        family.append(int(person))
cost = 0
for p in family :
    if p > 12 :
        cost += 15
    elif p >= 3 :
        cost += 10
print("Total cost of tickets: $",cost)

names = ["shrutee", "dharshini", "ameer", "loubnah"]
to_remove = []
for name in names :
    age = int(input(f"Enter the age of {name}: "))
    if age >= 16 and age <= 21 :
        to_remove.append(name)
for name in to_remove :
    names.remove(name)
print(names)


# exercise10
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while len(sandwich_orders) != 0 :
    finished_sandwiches.append(sandwich_orders.pop(0))
for sandwich in finished_sandwiches :
    print("I made your",sandwich.lower())


# exercise11
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
print("\nThe deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches = []
while len(sandwich_orders) != 0 :
    finished_sandwiches.append(sandwich_orders.pop(0))
for sandwich in finished_sandwiches :
    print("I made your",sandwich.lower())
