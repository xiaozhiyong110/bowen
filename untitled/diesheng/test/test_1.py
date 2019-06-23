from HTMLTestReportCN import HTMLTestRunner
import unittest
from time import sleep
from appium import webdriver
from diesheng.config import config_1
from diesheng.config import config_2
from diesheng.config.config_3 import get_logger
#创建变量接收日志的句柄
log=get_logger('test_1')


#写测试用例的类，单元测试
class DS(unittest.TestCase):
    #每个用例执行之前运行一次，作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):
        self.des = {
                    "platformName": "Android",
                    "platformVersion": "5.1.1",
                    "deviceName": "emulator-5554",
                    "appPackage": "com.qk.butterfly",
                    "appActivity": ".main.LauncherActivity",
                    "noReset": "true",
                    "unicodeKeyboard": "true",
                    "resetKeyboard": "true",

                    }
        self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5)
        log.info('手机与appium服务器建立连接完成')
    def test_1(self):
    #使用账号密码登录碟声
        sleep(5)
        log.info('点击密码按键，进入账号密码登录页面')
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        for i in config_1.read_data():
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(i[0])
            log.info(f'输入的手机是:{i[0]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(i[1])
            log.info(f'输入的密码是:{i[1]}')
            self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
            log.info('点击登录按钮')
        #断言
            try:
                sleep(5)
                log.info('登录失败的处理')
                b = self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').text
                print('登录失败')
                self.assertEqual(b, '登录', msg='登录失败')
            except:
                sleep(2)
                log.info('登录成功的处理')
                a = self.dr.find_elements_by_id('com.qk.butterfly:id/tv_tab')[-1].text
                print('登录成功')
                self.assertEqual(a, '我的', msg='我已登录成功')
    #每个测试用例执行完毕之后，运行teardown一次，作用：测试用例运行完，清理测试环境
    def tearDown(self):
        log.info('手机与appium断开连接')
        self.dr.quit()
if __name__=='__main__':
    # unittest.main()
    config_2.report(test_name=DS('test_1'),report_path='C:/Users/xiaozy/PycharmProjects/untitled/diesheng/report/a.html')

