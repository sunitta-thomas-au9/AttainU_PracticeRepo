# To print out first n no . this will give the out put 1 to n

n = int(input("Please Enter the no: "))

for i in range(n):
    print(i+1)
    i += 1
    if i == n:
        break

# program to check the number is odd or even

n = int(input("Enter the no: "))
if n % 2 == 0:
    print("Number is even")
else:
    print("Number is ODD")

