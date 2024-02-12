firstName = "aaron"
lastName = "mcneal"
age = 30
print(type(firstName))
print(type(age))
print(firstName.upper())

properFirstName = firstName.capitalize()
properLastName = lastName.capitalize()

varToSplit = "Aaron, McNeal"
print(varToSplit.split(','))

year = "2024"
print(type(year))
print(type(int(year)))

x = 7
# x = x + 1 Same as the code below
x += 1
x *= 2
print(x == 16)

myList = ["Black", "Blue", "Grey"]
newList = list((firstName, lastName, age))
myList.append("Green")
newList.append("Eugene")
print(newList)
print(myList)
print(len(newList))
myList.reverse()

# Tuples are static, can't add or remove elements
myTuple = ("Black", "Blue", "Grey")

# Differenes of Tuple and Lists
print(dir(myList))
print("Tuple Methods")
print(dir(myTuple))
