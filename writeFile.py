import csv

newRec = ["1005", "GV", "Development", "IT"]

f = open("example.csv", "a")

wtr = csv.writer(f)

wtr.writerow(newRec)

f.close()
