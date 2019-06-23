import xlrd
def shuju():
    f=xlrd.open_workbook(r'C:/Users/xiaozy/PycharmProjects/untitled/接口测试/data/bieke.xls','r')
    sheet=f.sheets()[0]
    num=[]
    for i in range(sheet.nrows):
        num.append(sheet.row_values(i))
    return num