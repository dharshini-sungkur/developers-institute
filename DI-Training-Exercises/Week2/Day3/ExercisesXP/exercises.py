# exercise1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys, values)))


# exercise2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
name = input("Enter name: ")
age = int(input("Enter age: "))
family[name] = age
cost = 0
for name,age in family.items():
    if age > 12:
        cost += 15
    elif age >= 3:
        cost += 10
print("Total cost:", cost)


# exercise3
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": {"men", "women", "children", "home" },
    "international_competitors": {"Gap", "H&M", "Benetton"}, 
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": {"pink", "green"}
    }
}  
brand["number_stores"] = 2
print(brand["type_of_clothes"])
brand["country_creation "] = "spain"
if "international_competitors" in brand:
    brand["international_competitors"].add("Desigual")
del brand["creation_date"]
print(list(brand["international_competitors"])[-1])
print(brand["major_color"]["US"])
print(len(brand))
print(brand.keys())
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}
brand.update(more_on_zara)
print(brand["number_stores"])


# exercise4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
print({key: value for value, key in enumerate(users)})
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

print({value: key for value, key in enumerate(users)})
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

users.sort()
print({key: value for value, key in enumerate(users)})

print({key: value for value, key in enumerate(users) if "i" in key })

print({key: value for value, key in enumerate(users) if key[0].lower() in ["m","p"] })
