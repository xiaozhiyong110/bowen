#driver  中主要是控制跑回归测试时只跑哪些模块的用例
from 接口测试.report.baogao import baogao
with open(r'C:/Users/xiaozy/PycharmProjects/untitled/接口测试/driver/a.txt','r') as f:
    a=f.readlines()
    print(a)
    if 'all' in a :
        baogao('*')
    else:
        baogao(a)
