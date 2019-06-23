import unittest
from HTMLTestReportCN import HTMLTestRunner
def kuaidibaogao(name):
    suit=unittest.TestSuite()
    for i in name:
        discover=unittest.defaultTestLoader.discover(r'C:/Users/xiaozy/PycharmProjects/untitled/接口测试/test',pattern='{}.py'.format(i.strip()))
        print(discover)
        for i in discover:
            suit.addTest(i)
    f=open('a.html','wb')
    runner=HTMLTestRunner(stream=f,title='kuaidi',description='结果如下',)
    runner.run(suit)
    f.close()