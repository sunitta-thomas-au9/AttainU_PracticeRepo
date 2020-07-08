text = "heavy rain in international gate,in cheinn"
x = "in" in text    # this checks whether in is there in text or not
print(x)
a = "hello"
b = "world"
c = a + b
print(c)
place = "chennai"
txt = "I am staying in {}"
print(txt.format(place))

num1 = 100
num2 = 112
if num1 > num2:
    txt = "{0} is greater than {1}"
    print(txt.format(num1, num2))
else:
    txt = "{1} is greater than {0}"
    print(txt.format(num1, num2))
