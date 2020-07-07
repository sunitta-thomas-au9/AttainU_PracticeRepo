# To Check a number is even or odd
n = 20
if n % 2 == 0: 
    print("Number is even")
elif n % 2 == 1:
    print("Number is odd")
else:
    print("Number is invalid")

# Number entered by user
num = int(input("Please enter the number"))
if num % 2 == 0:
    print("The number is even")
elif num % 2 != 0:
    print("The number is odd")
else:
    print("The number is invalid")

# How to check a number is divisible by 7 or not
num1 = int(input("Enter the number to be checked : "))
if num1 % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7 ")    



