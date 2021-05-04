# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = int(input('Please input an number for calculate Factorial:'))

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print("The factorial of", num, "is", factorial)

count = 0
temp = factorial
for n in range(len(str(factorial)), 0, -1):
    if(temp % 10 == 0):
        temp /= 10
        count += 1

print('count of Zero:', count)
