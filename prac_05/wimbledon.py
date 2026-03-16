import csv

FILENAME = 'wimbledon.csv'

with open(FILENAME, "r", encoding="utf-8") as in_file:
    reader = csv.DictReader(in_file)



