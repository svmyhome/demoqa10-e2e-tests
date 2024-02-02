import csv
import os

# with open(os.path.join(PROJECT_ROOT_PATH, "resources/csv_test.csv")) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#     print(reader.line_num)
with open(os.path.join(os.getcwd(), "resources", "csv_test.csv")) as f:
    reader = csv.reader(f)
    reader.__next__()
    reader.__next__()