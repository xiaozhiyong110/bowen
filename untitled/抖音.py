# from appium import webdriver
# from time import sleep
#建立与appium
# des={
#     "platformName": "Android",
#     "platformVersion": "5.1.1",
#     "deviceName": "emulator-5554",
#     "appPackage": "com.tencent.tim",
#     "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#     "noReset": "true",
#     "unicodeKeyboard":"true",
#     "resetKeyboard":"true",
#
# }
#http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
#测试脚本与appium服务器建立一个session连接
# dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# sleep(10)
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').clear()
# sleep(5)
# dr.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('1136682078') #安卓独有的定位方法
# dr.find_element_by_id('com.tencent.tim:id/password').clear()
# sleep(2)
# dr.find_element_by_id('com.tencent.tim:id/password').send_keys('xiao123456')
# dr.find_element_by_id('com.tencent.tim:id/login').click()
# sleep(10)

#滑动操作
#第一步：获取窗口大小
# s=dr.get_window_size()
# print(s)
# #第二步：放缩x，y轴
# x1=s['width']*0.5
# x2=s['height']*0.25
# y2=s['height']*0.75
# #第三步：使用swipe方法，进行滑动操作
# dr.swipe(x1,y2,x1,y2)
# sleep(0)

# item=dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')
# item[1].click()
# sleep(10)
# b=dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
# sleep(5)
# x=dr.get_window_size()
# x1=x['width']*0.5
# y1=x['width']*0.1
# y2=x['height']*0.3
# dr.swipe(x1,y2,x1,y1)
# sleep(10)
# a=dr.find_elements_by_class_name('android.widget.ImageView')
# sleep(10)
# a[1].click()
# sleep(2)



# from appium import webdriver
# from time import sleep
# class Tim(object):
#     def __init__(self):
#         self.des = {
#             "platformName": "Android",
#             "platformVersion": "5.1.1",
#             "deviceName": "emulator-5554",
#             "appPackage": "com.tencent.tim",
#             "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
#             "noReset": "true",
#             "unicodeKeyboard": "true",
#             "resetKeyboard": "true",
#
#         }
#         self.dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
#         sleep(10)
#     def dianzan(self):
#             self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.FrameLayout')[1].click()
#             self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name('android.widget.RelativeLayout')[-1].click()
#             sleep(5)
#             x = self.dr.get_window_size()
#             x1=x['width']*0.5
#             y1=x['width']*0.1
#             y2=x['height']*0.3
#             self.dr.swipe(x1,y2,x1,y1)
#             sleep(10)
#             a = self.dr.find_elements_by_class_name('android.widget.ImageView')
#             sleep(10)
#             a[1].click()
#     def wenzi(self):
#         aa=self.dr.find_element_by_id('com.tencent.tim:id/ivTitleName').text
#         print(aa)
#     def anjian(self):
#         # self.dr.keyevent(3)     #模拟人点击物理按键home键
#         self.dr.keyevent(4)
# if __name__=='__main__':
#     yasuo=Tim()
    # yasuo.dianzan()
    # yasuo.wenzi()
    # yasuo.anjian()

#unittest 单元测试模块
# import HTMLTestReportCN  #生成测试报告的
# import unittest   #用于单元测试，验证预期与实际结果是否一致，一致代表通过，不一致代表失败
# class T(unittest.TestCase):
#     def test_1(self):   #测试用例方法必须以test开头
#         x='宝马'   #预期结果
#         y='宝马'  #实际结果
#         self.assertEqual(x,y,msg='msg作用填写备注信息')
#     def test_2(self):
#         x='宝马'
#         y='劳斯莱斯'
#         self.assertEqual(x,y,msg='a')
# if __name__=='__main__': #使用unittest类的main方法，自动加载当前脚本中的类，并自动运行测试用例
#     #unittest.main()
#     #第一步：创一个测试套件，理解成玩具枪的弹夹
#     suite=unittest.TestSuite()
#     #第二步：向测试套件里面添加测试用例，理解成玩具枪弹夹添加子弹
#     suite.addTest(T('test_1'))
#     suite.addTest(T('test_2'))
#     #将生成的测试结果写入html文件里，理解成玩具枪上档
#     with open('a.html','wb') as fb:
#         runner=HTMLTestReportCN.HTMLTestRunner(stream=fb,
#                                                title='报告名称',
#                                                description='报告的描述',
#                                                verbosity=2)
#                                             #输出内容的详细等级，默认是0,2代表最详细
#         runner.run(suite)