import csv, re

count = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x = list(map(int, re.split('-', row[0])))
        y = list(map(int, re.split('-', row[1])))
        z = range(max(x[0], y[0]), min(x[1], y[1])+1)
        if len(z) > 0:
            count += 1
print(count)