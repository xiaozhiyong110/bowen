from HTMLTestReportCN import HTMLTestRunner
import unittest
def baidu_baogao():
    suit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(r'C:/Users/xiaozy/PycharmProjects/untitled/百度输入法/test',pattern='baidu_test.py')
    print(discover)
    suit.addTest(discover)
    f=open('C:/Users/xiaozy/PycharmProjects/untitled/百度输入法/report/baidu_baogao.html','wb')
    runner=HTMLTestRunner(stream=f,title='百度输入法',description='结果如下',verbosity=2)
    runner.run(suit)
    f.close()
baidu_baogao()