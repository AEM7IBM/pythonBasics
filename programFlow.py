import random

a = 7
b = 7

# if statements
if a > b:
    print("a is larger than b")
elif a < b:
    print("b is larger than a")
else:
    print("idk")

# while loops
i = 1

while i<=10:
    ranNum = random.randint(0,20)
    print(ranNum)
    if ranNum == 6:
        print("Break")
        break
    print(i)
    i+=1

# For Loops
usernames = ["Aaron", "Gene", "Mac", "Blessed"]
for x in usernames:
    print(x)

name = "Aaron McNeal"

for x in name:
    print(x)
