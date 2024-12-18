import openpyxl

# 導入
wb = openpyxl.load_workbook('訊息.xlsx')

# 選擇worksheet
# print(wb.sheetnames)

ws = wb['訊息.xlsx']
# print(ws)

# 獲取數據
# print(ws['A1'].value)
#
# for row in ws.rows:
#     # for cell in row:
#         # print(cell.value)
#     data = [ cell.value for cell in row]
#
# print(data)

# 獲取行列數
# print(ws.max_row)
# print(ws.max_column)

for row in ws.iter_rows(min_row =2, min_col=1,max_row=5,max_col=23):
    data = [cell.value for cell in row]
    print(data)