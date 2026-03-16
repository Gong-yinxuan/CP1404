import csv

FILENAME = 'wimbledon.csv'

data = {}
with open(FILENAME, "r", encoding="utf-8") as in_file:
    reader = csv.DictReader(in_file)
    countries = set()
    for row in reader:
        champion = row["Champion"]
        country = row["Country"]
        countries.add(country)

        if champion not in data:
            data[champion] = 1
        else:
            data[champion] += 1

