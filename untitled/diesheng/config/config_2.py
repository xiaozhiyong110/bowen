from HTMLTestReportCN import HTMLTestRunner
import unittest
def report(test_name,report_path):
    suite=unittest.TestSuite()
#第二步：向测试套件里面添加测试用例，理解成玩具枪弹夹添加子弹
    suite.addTest(test_name)
#将生成的测试结果写入html文件里，理解成玩具枪上档
    with open(report_path,'wb') as fb:
        runner=HTMLTestRunner(stream=fb,
                          title='报告名称',
                          description='报告的描述',
                          verbosity=2)
                 #输出内容的详细等级，默认是0,2代表最详细
        runner.run(suite)