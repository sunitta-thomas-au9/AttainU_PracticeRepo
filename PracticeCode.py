# TO check whether n is divisible by d or not
n = int(input("Enter no:"))
d = int(input("Enter no to divide:"))
if n % d == 0:
    print(n, "is divisible by", d)
else:
    print(n, "is not divisible by", d)

# To check the number is greater than or less than

n = int(input("Enter the first no: "))
m = int(input("Enter the second no: "))

if n > m:
    print(n, "is greater than ", m)
elif n < m:
    print(n, "is less than", m)
else:
    print(n, "is equal to ", m)

 # To print out first n no this will give the out put from 0 to n

n = int(input("Please Enter the no: "))
m = n + 1
for i in range(m):
    print(i)
    i += i
    if i == m:
        break



