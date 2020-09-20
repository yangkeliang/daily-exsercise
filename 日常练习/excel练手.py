import xlrd
import xlwt
# wb = xlrd.open_workbook("daily-exsercise\日常练习\data.xlsx")
# sheet = wb.sheet_by_name("学生表")
# print(sheet.row_values(0,0,10)) 

wb1 = xlwt.Workbook()#工作薄
sheet1 = wb1.add_sheet("info")#工作表

tall_style = xlwt.easyxf('font:height 1')#设置行高及列宽
num = int(input("请输入需要改变的数量："))
for i in range(num):
    sheet1.col(i).width=256*3
for j in range(num):
    sheet1.row(j).set_style(tall_style)

mflist = []
for i in range(num):#设置样式
    mf = xlwt.XFStyle()#样式
    pattern = xlwt.Pattern()#背景颜色
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN#设置背景颜色模式
    pattern.pattern_fore_colour = i#设置背景颜色
    mf.pattern = pattern
    mflist.append(mf)

for i in range(num):
    for j in range(num):
        change = 0
        for k in range(num):
            if i == j+k:
                sheet1.write(i,j,"",mflist[k])
                change = 1
                continue
        if change == 0:
            sheet1.write(i,j,"",mflist[j])
wb1.save("date1.xls")
