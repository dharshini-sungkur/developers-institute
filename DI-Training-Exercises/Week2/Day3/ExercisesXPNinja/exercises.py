# exercise
cars = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(",")
print("Number of companies/manufacturers: ", len(cars))
cars.sort(reverse=True)
print(cars)
with_o = 0
without_i = 0
for c in cars:
    if "o" in c:
        with_o += 1
    if "i" not in c:
        without_i += 1
print(without_i, "car names do not contain the letter i")     
print(with_o, "car names contain the letter o")  

cars = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
filtered_cars = list(dict.fromkeys(cars))
print(len(filtered_cars), "companies in the list:",", ".join(filtered_cars))

for i in range(0, len(filtered_cars)):
    name = [i for a,i in enumerate(filtered_cars[i])]
    name.reverse()
    filtered_cars[i] = "".join(name)
filtered_cars.sort()    
print(filtered_cars)