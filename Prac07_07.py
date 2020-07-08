# To Check an year is leap year
a = input("Enter an year: ") 

if (a.isdigit() == True):
    a = int(a) 
    if (a <= 0 or a >= 5000):
        print("Please enter a valid year")
    else:
        if (a % 4 == 0):
            print("Year is leap Year")
        else:
            print("Year is not leap year")
else:
    print("Please enter a valid year out")

print("Calculation Over")  
 
  
















