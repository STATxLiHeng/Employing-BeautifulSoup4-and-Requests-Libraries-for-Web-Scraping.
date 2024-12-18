from openpyxl import Workbook

wb = Workbook()
# ws = wb.active
ws1 = wb.create_sheet('訊息.xlsx',0)
ws2 = wb.create_sheet('訊息2.xlsx')

# 絕對位置
ws1['A1'] = 'aaa'
ws1['B1'] = 'bbbb'
ws1['W2'] = 'ccc'
#CELL
ws1.cell(row = 5,column = 1).value='我'

# 追加
rows = (
    ('andy','男',18),
    ('andy','男',18),
    ('andy','男',18)
)

for row in rows:
    ws2.append(row)

wb.save('訊息.xlsx')