m1 = int(input("Enter the mark of subject 1 : "))
m2 = int(input("Enter the mark of subject 2 : "))
m3 = int(input("Enter the mark of subject 3 : "))
m4 = int(input("Enter the mark of subject 4 : "))
m5 = int(input("Enter the mark if subject 5 : "))

perc = (m1 + m2+ m3 + m4 + m5)/5

if (perc >= 90):
    grade = "A"
    print("You have scored grade - A")
elif (perc < 90 and perc >= 70):
    grade = "B"
    print("You have scored grade - B")
elif (perc < 70 and perc >= 50):
    grade = "C"
    print("You have scored grade - C")
elif (perc < 50 and perc >= 30):
    grade = "D"
    print("You have scored grade - D")
elif (perc < 30):
    grade = "E"
    print("You have scored grade - E")
else:
    print("Invalid Entry")


