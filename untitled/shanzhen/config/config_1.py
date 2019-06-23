from HTMLTestReportCN import HTMLTestRunner
import unittest
def report(test_name,report_path):
    suite=unittest.TestSuite()
    suite.addTest(test_name)
    with open(report_path,'wb') as fb:
        runner=HTMLTestRunner(stream=fb,
                              title='善珍',
                              description='报告的描述',
                              verbosity=2)
        runner.run(suite)