import os
from openpyxl import load_workbook

os.chdir('../resources')
path = os.getcwd()
workbook = load_workbook(os.path.join(path, "calendare.xlsx"))
sheet = workbook.active

print(sheet.cell(3, 3).value)
