from 接口测试.report.kuaidibaogao import kuaidibaogao
f=open(r'C:/Users/xiaozy/PycharmProjects/untitled/接口测试/driver/a.txt','r')
a=f.readlines()
print(a)
if 'all' in a:
    kuaidibaogao(a[3])
else:
    kuaidibaogao(a)