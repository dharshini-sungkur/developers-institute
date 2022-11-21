# exercise3
print(3 <= 3 < 9)
    # True
print(3 == 3 == 3)
    # True    
print(bool(0))
    # False      
print(bool(5 == "5"))
    # False 
print(bool(4 == 4) == bool("4" == "4"))
    # True 
print(bool(bool(None)))
    # False
    
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)    # True
print("y is", y)    # False
print("a:", a)      # 5
print("b:", b)      # 10


# exercise4
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(my_text.__len__())


# exercise5
longest = 0
withoutA = True

while withoutA:
    sentence = input("\nEnter the longest sentence without the character 'A': ")
    
    if sentence.find("A") == -1 :
        if len(sentence) > longest:
            longest = len(sentence)
            print("Congratulations you have entered a new longest sentence without the character 'A'")  
        else:
            print("You have not entered the longest sentence without the character 'A'")  
    else:
        withoutA = False