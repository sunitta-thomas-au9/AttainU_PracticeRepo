list1 = ["apple", "orange", "banana", "apple", "jackfruit", "grape"]
print(list1)  # print all
print(list1[2])  # print only one
list1[3] = "pear"   # replace one item
print(list1)
for x in list1:  # list out using for loop
    print(x)
if "apple" in list1:  # checks whether apple is there or not
    print("yes,exists")
print(len(list1))  # length of the list
list1.append("blueberry")  # add to last
print(list1[5:])  # list from 5th to last
print(list1[-2:])  # list from last to backwards
list1.insert(3, "pineapple")  # insert at specific point
print(list1)
list2 = ["tomato", "passionfruit", "duriyan"]
list3 = list1 + list2  # add two lists together
list4 = list2.copy()  # copy of a list
print(list4)
list1.extend(list2)  # append list2 to list1
print(list1)
# list1.remove("grape") # removed one item
# list1.pop()#remove from last,since index is not given
# list1.pop(2)#removed from index 2
# print(list1)
# del list1[1] #delete from index1
# list1.clear()#delete all items
# print(list1)


#  ###############TUPLES##############
mytuples = ("apple", "banana", "cherry")
print(mytuples)
