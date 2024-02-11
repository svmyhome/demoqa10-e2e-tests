import os
from xlrd import open_workbook

os.chdir('../resources')
path = os.getcwd()


reader = open_workbook(os.path.join(path, "template.xls"))
print(reader.sheets())
print(reader.sheet_names())
print(reader.sheet_by_index(1))
print(reader.sheet_by_index(0).ncols)
print(reader.sheet_by_index(0).nrows)
print(reader.sheet_by_index(0).cell_value(5, 2))
print(reader.sheets())
for nx in range(reader.sheet_by_index(0).nrows):
    print(reader.sheet_by_index(0).row(nx))
