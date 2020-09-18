import xlrd,xlwt

# Read

book = xlrd.open_workbook(r'.\excel\data_read.xlsx')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
print('Table total row count: ', nrows)

ncols = sheet1.ncols
print('Table total col count: ', ncols)

row3_values = sheet1.row_values(2)
print('Row 3 values: ', row3_values)

col3_values = sheet1.col_values(2)
print('Col 3 values: ', col3_values)

cell_3_3 = sheet1.cell(2,2).value
print('Row 3 Col 3 values: ', cell_3_3)

# Write
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test')
worksheet.write(0,0,'A1data')
workbook.save(r'.\excel\data_write_2.xls')