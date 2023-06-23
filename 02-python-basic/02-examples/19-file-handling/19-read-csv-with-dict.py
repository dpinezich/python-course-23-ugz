import csv

with open("onboarding.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        print(row["Login email"], row["First name"])