import csv
mylist =[]
with open ("pokemon.csv", "r", encoding='utf-8') as csv_file: #utf-8 to avoid strange symbols, reads the CSV
    reader = csv.reader(csv_file, delimiter=',') 
    for lines in reader:
        if lines[1] == mystring
            type = line[2]

