# exercises 1,2,3
birthdays = {
    "meghna": "2000/10/12",
    "adi": "2006/03/31",
    "aditi": "2006/03/31",
    "madan": "1968/08/03",
    "prema": "1976/11/05"    
}

name = input("\nTo add an entry, input the name: ").lower()
birthday = input("Input the birthday (YYYY/MM/DD): ")
birthdays[name] = birthday

print("Names: ", list(birthdays.keys()))
name = input("You can look up the birthdays of the people in the list!\nEnter a name: ").lower()

if name in birthdays:
    print(name,"was born on", birthdays[name])
else:
    print("Sorry, we don’t have the birthday information for", name)
    

# exercises 4
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
for fruit,price in items.items():
    print(fruit, "costs $", price)
    
    
# exercises 5
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}
cost = 0
for fruit,details in items.items():
    cost += details["price"] * details["stock"]
print(cost)