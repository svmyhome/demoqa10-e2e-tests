import os
from xlrd import open_workbook

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# with open(os.path.join(PROJECT_ROOT_PATH, "resources/template.xls"), 'r') as xls:
#     reader = open_workbook(xls)
#     print(reader.sheet_names())

reader = open_workbook(os.path.join(PROJECT_ROOT_PATH, "resources/template.xls"))
print(reader.sheets())
print(reader.sheet_names())
print(reader.sheet_by_index(1))
print(reader.sheet_by_index(0).ncols)
print(reader.sheet_by_index(0).nrows)
print(reader.sheet_by_index(0).cell_value(5, 2))
print(reader.sheets())
for nx in range(reader.sheet_by_index(0).nrows):
    print(reader.sheet_by_index(0).row(nx))
