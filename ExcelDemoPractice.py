import openpyxl

book = openpyxl.load_workbook("C:\\Users\\USER\\Downloads\\download (9).xlsx")
sheet = book.active
print(sheet.cell(row = 3, column = 2).value)