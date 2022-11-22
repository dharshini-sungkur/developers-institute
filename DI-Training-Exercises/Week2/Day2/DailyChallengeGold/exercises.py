# exercise1
birthday = input("Enter your birthdate (DD/MM/YYYY): ").split("/")[2]
age = 2022 - int(birthday)
candles = age % 10

cake = "     _" + "_" * (int((10 - candles) / 2))
cake += "i"*candles
cake += "_"*(int((10-candles-1)/2)) + "_"

leap = int(birthday) % 4

if (leap == 0) :
    print("\n")
    print(cake)
    print("    |:H:a:p:p:y:|   ")
    print("  __|___________|__ ")
    print(" |^^^^^^^^^^^^^^^^^|")
    print(" |:B:i:r:t:h:d:a:y:|")
    print(" |                 |")
    print(" ~~~~~~~~~~~~~~~~~~~")
print("\n")
print(cake)
print("    |:H:a:p:p:y:|   ")
print("  __|___________|__ ")
print(" |^^^^^^^^^^^^^^^^^|")
print(" |:B:i:r:t:h:d:a:y:|")
print(" |                 |")
print(" ~~~~~~~~~~~~~~~~~~~")
print("\n")