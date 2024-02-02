import csv
import os

os.chdir("../resources")
path = os.getcwd()

with open(os.path.join(path, 'csv_test.csv'), 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    print(reader.line_num)

with open(os.path.join(path, 'csv_test.csv'), 'r') as f:
    reader = csv.reader(f)
    print(reader.__next__())
    print(reader.__next__())
