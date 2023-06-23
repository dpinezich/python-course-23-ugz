import csv
csvfile = open('cities.csv', 'r')
cities = csv.reader(csvfile, delimiter=',', quotechar='|')
for row in cities:
     print(row[8], row[9])
