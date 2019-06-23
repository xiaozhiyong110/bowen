from HTMLTestReportCN import HTMLTestRunner
import unittest
def baogao(name):
    suit=unittest.TestSuite()
    #第一个参数存放脚本路径，第二参数匹配测试文件的通配符
    #函数的意思是可以自动去发现写的通配符语句中符合通配符的文件中以.test开头的函数，提取出来放在discover中
    for i in name:
        print(i)
        discover=unittest.defaultTestLoader.discover(r'C:/Users/xiaozy/PycharmProjects/untitled/接口测试/test',pattern='{}.py'.format(i.strip()))
        print(discover)
        for i in discover:
            suit.addTest(i)
    f=open('abc.html','wb')
    runner=HTMLTestRunner(stream=f,tester='xiazy',description='结果如下',title='别克测试报告',verbosity=2)
    runner.run(suit)
    f.close()