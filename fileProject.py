import csv

print(dir(csv))

# open file in read mode
f = open("example.csv", 'r')

rdr = csv.reader(f, delimiter=",")

for x in rdr:
    print(x)

f.close()