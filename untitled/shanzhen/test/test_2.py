import unittest
from appium import webdriver
from time import sleep
from shanzhen.config import config_1
from shanzhen.config.config_2 import get_logger
log=get_logger('test_1')
class shanzhen(unittest.TestCase):
    def setUp(self):
        self.des={
                    "platformName": "Android",
                    "platformVersion": "5.1.1",
                    "deviceName": "emulator-5554",
                    "appPackage": "com.wayyue.shanzhen",
                    "appActivity": ".view.main.SZMainActivity",
                    "noReset": "true"
                    }

        self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(10)
        log.info('连接服务器成功')
    def test_1(self):
        self.dr.find_elements_by_class_name('android.widget.RelativeLayout')[2].click()
        sleep(10)
        log.info('点击体检成功')
        self.dr.find_elements_by_class_name('android.view.View')[3].click()
        sleep(10)
        log.info('点击下一步成功')
        self.dr.find_element_by_accessibility_id('下一步').click()
        sleep(10)
        log.info('点击下一步成功')
        self.dr.find_element_by_accessibility_id('下一步').click()
        sleep(10)
        log.info('购买成功的处理')
        a=self.dr.find_element_by_id('com.wayyue.shanzhen:id/toolbar_title').text
        print(a)
        self.assertEqual(a,'订单信息',msg='购买套餐成功')

    def tearDown(self):
        self.dr.quit()
        log.info('断开服务器成功')
if __name__=='__main__':
    # unittest.main()
    config_1.report(test_name=shanzhen('test_1'),report_path=r'C:\Users\xiaozy\PycharmProjects\untitled\shanzhen\report\a.html')