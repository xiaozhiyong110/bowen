import xlrd
def shuju():
    num_1=[]
    f=xlrd.open_workbook(r'C:\Users\xiaozy\PycharmProjects\untitled\接口测试\data\bieke.xls')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        num_1.append(sheet.row_values(i))

    return num_1
shuju()