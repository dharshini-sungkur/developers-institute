def perfectNumber(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        return True
    else:
        return False

number = int(input("Enter a number (to check if it is a perfect number): "))
print(perfectNumber(number))