import csv
from bs4 import UnicodeDammit
with open('movies.csv','rb') as file:
    content = file.read()
    suggestion = UnicodeDammit(content)
    print(f'encoding for the file{suggestion.original_encoding}')
    print(f'encoding for the file{suggestion.unicode_markup}')
with open('movies.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)