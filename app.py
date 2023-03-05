print("Hello World")

# birth_year: int = input("Enter your DOB ")
#age = 2023 - int(birth_year)
#print(age)#

#first = input("First: ")
#second = input("Second: ")
#sum = float(first) + float(second)
#print("Sum " + str(sum))

#third = float(input("Third: "))
#fourth = float(input("Fourth: "))
#sum = third + fourth
#print(sum)

"""
course = "Python for Beginners"
print(course)
print(course.upper())
print(course.lower())
print(course.find("y"))
print(course.find("Y"))
print(course.replace("for", "4"))

print(10/13) #creates a float
print(10//13) #creates an integer
print(10%13) #modular
print(10**3) #power

x = 10
x +=3
print(x)

x = 3>2
print(x)
y = 3!=2
print(y)

price = 25
print(price>10 and price<30)
price2 = 5
print(price2>10 or price2<30)
print(price2>10 and price2<30)
price3 = 5
print(not price3 > 10)

temperature = 85
if temperature > 30:
    print("It's hot")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")

"""

"""
Weight: 170
(K)g or (L)bs: l
Weight in Kg: 76.5
"""
"""
WEIGHT CONVERSION
weight = int(input("Weight: "))
unit = input("K or L: ")
if unit.upper() == "K":
    converted = weight/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))
"""

"""
COUNTING
i = 1
while i <=5:
    print(i)
    i = i + 1
"""
"""
COUNTING WITH STRINGS
i = 1
while i <=10:
    print(i * "x")
    i = i + 1
"""
"""
#LISTS

names = ["John", "Bob", "Bill", "Mary", "Bam"]
print(names)
print(names[0])
print(names[-1])
names[0] = "Jon"
print(names[0])
print(names)
print(names[0:3])
"""

names = ["Jon", "Mary", "David"]
names.insert(3, "Neve")
print(names)
"""
names.remove([0])
print(names)
"""
#INSERT
numbers = [1,2,3,4,5]
numbers.insert(3, "-7")
print(numbers)
"""
REMOVE
numbers.remove(0) this function is not working
"""
print(numbers)

"""
#CLEAR. DOES NOT REQUIRE ANY VALUES. WILL SIMPLY CLEAR THE LIST
numbers.clear()
print(numbers)
"""
"""
#FIND A NAME OR NUMBER IN LIST. RETURNS A BOOLEAN - TRUE OR FALSE
print("Pete" in names)
print(1 in numbers)
print(len(names))
print(len(numbers))
"""
#FOR LOOP
numbers = [1,2,3,4,5]
for i in numbers:
    print(i)
#WHILE LOOP
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
#FOR LOOP IS EASIER TO UNDERSTAND


#RANGE FUNCTION
i = range(5)
for i in i:
    print(i)

t = range(7,19) #includes 7 but not 19
for t in t:
    print(t)

#SKIP 2
y = range(7,19,2) #includes 7 but not 19
for y in y:
    print(y)

print("X" * 10)






