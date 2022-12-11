import csv, re

count = 0
with open('input4.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x = list(map(int, re.split('-', row[0])))
        y = list(map(int, re.split('-', row[1])))
        if (x[0] <= y[0] and x[1] >= y[1]) or (x[0] >= y[0] and x[1] <= y[1]):
            count += 1
print(count)