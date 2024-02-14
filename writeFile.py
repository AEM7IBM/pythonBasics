import csv

newRec = ["1005", "GV", "Development", "Technology"]

f = open("example.csv", "a")

wtr = csv.writer(f)

wtr.writerow(newRec)

f.close()
