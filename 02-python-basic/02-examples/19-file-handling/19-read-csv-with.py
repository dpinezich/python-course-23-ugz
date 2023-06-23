import csv

with open("cities.csv", "r") as csvfile:
    cities = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in cities:
        print(row[8], row[9])
