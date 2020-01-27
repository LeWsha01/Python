import json
import openpyxl

wb = openpyxl.load_workbook(filename='students.xlsx')
sheet = wb['Students']
col = sheet.max_column
row = sheet.max_rows
for i in range(1, col + 1):
    sheet['A{}'.format(i)] = sheet['A{}'.format(i)].value + ' ' + sheet['B{}'.format(i)].value
    sheet.merge_cells('A{}:B{}'.format(i, i))

wb.save('table2.xlsx')

# path_excel = 'students.xlsx'
# path_json = 'excel_json.json'
