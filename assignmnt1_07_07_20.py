num1 = int(input("Input number 1 : "))
num2 = int(input("Input number 2 : "))
print("Please press 1 for Addition, 2 for Subtraction, 3 for Multiplication , 4 for Division: ")
selection = int(input())

if (selection == 1):
    sum = num1 + num2
    print( "The sum of the numbers is :", sum)
elif (selection == 2):
    sub = num1 - num2
    print("The subtraction of numbers is :", sub)
elif (selection == 3):
    mult = num1 * num2
    print("The multiplication of numbers is :", mult)
elif (selection == 4):
    div = num1 / num2
    print("The division of numbers is :", div)
else:
    print("Invalid Selection, Select a number between 1-4")