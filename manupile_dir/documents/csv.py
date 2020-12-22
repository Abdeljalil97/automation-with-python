import csv
with open('top_films.csv', newline='') as file:
    dialect = csv.Sniffer()
    print(dialect)

with open('top_films.csv', newline='') as file:
    reader = csv.reader(file, dialect)
    for row in reader:
        print(row)