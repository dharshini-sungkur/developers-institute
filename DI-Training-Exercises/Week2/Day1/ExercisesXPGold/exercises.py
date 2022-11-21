# exercise1
print("Hello world\n"*4 + "I love python\n"*4)

# exercise2
month = int(input("\nEnter month(1 to 12): "))
match month:
    case 12|1|2:
        print("Winter runs from December (12) to February (2)")
    case 3|4|5:
        print("Spring runs from March (3) to May (5)")
    case 6|7|8:
        print("Summer runs from June (6) to August (8)")
    case 9|10|11:
        print("Autumn runs from September (9) to November (11)")
    case _:
        print("invalid month")
        
