import random

# exercise1
def display_message():
    print("\nI am learning python")
display_message()
print("\n")


# exercise2
def favorite_book(title):
    print("One of my favorite books is", title)
favorite_book("Alice in Wonderland")
print("\n")


# exercise3
def describe_city(city, country = "Iceland"):
    print(city, "is in", country)
describe_city("Reykjavik ")
print("\n")


# exercise4
def isEqual(number):
    if number >= 1 and number <= 100:
        r = random.randint(1,100)
        if r == number:
            print("Success, numbers match")
        else:
            print(f"Fail, numbers ({number},{r}) do not match")
    else:
        print("Number is not between 1 and 100")
isEqual(12)
print("\n")


# exercise5
def make_shirt(size, text):
    if size.upper() == "L":
        print("The size of the shirt is", size, "and the text is: I love python")
    elif size.upper() == "M":
        print("The size of the shirt is", size, "and the text is: I love java")
    else:        
        print("The size of the shirt is", size, "and the text is", text)
make_shirt(text="hope", size="M")
print("\n")


# exercise6
def show_magicians(magicians):
    for i in magicians:
        print(i)
        
def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] =  "The Great " + magicians[i]   

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)
print("\n")


# exercise7
def get_random_temp(season):
    match(season):
        case "winter":
           return round(random.uniform(-10,16), 1)
        case "autumn":
           return round(random.uniform(16,23), 1)
        case "spring":
           return round(random.uniform(23,32), 1)   
        case "summer":
            return round(random.uniform(32,40), 1)        
           
def get_msg(temp):
    if temp < 0:
        print(f"Temperature: {temp} degrees Celsius. Brrr, that’s freezing! Wear some extra layers today")
    elif temp < 16:
        print(f"Temperature: {temp} degrees Celsius. Quite chilly! Don’t forget your coat")
    else:
        print(f"The temperature right now {temp} degrees Celsius")

def main():
    temp = get_random_temp("winter")
    get_msg(temp)
    
main()
print("\n")