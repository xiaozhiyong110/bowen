#web自动化
#selenium：web自动化测试工具集
#以下3点是selenium 1.0的组成
#1.selenium IDE 是火狐浏览器的一个插件  作用：录制和回放
#2.selenium Grid 是自动化测试的一个辅助工具  作用：可以实现在不同的测试环境中同时执行测试
#3. selenium Rc 是selenium 1.0 里面自动化测试的核心  作用：控制浏览器行为  rc通过将测试代码转换成javascript能够识别的动作从而间接的控制浏览器

#selenium 2.0 的组成
#selenium1.0（selenium ide/ grid/rc）+ webdriver    webdriver是selenium2.0的核心  作用：控制浏览器的行为
   # webdriver通过将浏览器所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制浏览器
from selenium import webdriver
from time import sleep
import selenium.webdriver.support.ui as ui


from selenium.webdriver.common.action_chains import ActionChains
#登录qq空间
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(5)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1136682078')
# sleep(5)
# dr.find_element_by_id('p').click()
# dr.find_element_by_id('p').send_keys('xiao123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
# dr.quit()

#定位一组对象
# dr=webdriver.Chrome()
# dr.switch_to_default_content()
# dr.get("https://qzone.qq.com/")
# sleep(5)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('113668294')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('xiao123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# dr.switch_to.frame('tcaptcha_iframe')
# wd=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# sleep(5)
# ActionChains(dr).drag_and_drop_by_offset(wd,170,0).perform()    #drag_and_drop_by_offset  函数有三个参数（起始位置，x轴坐标，y轴坐标）
# print(len(ww))
# for i in ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
# dr.quit()
#     b=i.get_attribute('text')    #获取某个属性的值
#     print(b)
#
# #层级定位
#模拟鼠标移动


#切换弹出框
# dr=webdriver.Chrome()
# dr.get('file:///C:/Users/xiaozy/Desktop/abc.html')
# sleep(5)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(3)
# ww=dr.switch_to_alert()
# print(ww.text)
# ww.accept()   #点击确定
# ww.dismiss() #点击取消
# ww.send_keys('')  #输入数据



#拉动浏览器滚动条
# qq='var q=document.documentElement.scrollTop=5000'
# dr.execute_script(qq)
# sleep(3)

#获取当前窗口的标识
# print(dr.current_window_handle)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# print(dr.title)
# sleep(5)
# aa=dr.window_handles  #获取所有窗口
# dr.switch_to.window(aa[1])
# print(dr.title)
# dr.quit()

dr=webdriver.Chrome()
dr.get('https://www.baidu.com')
# sleep(3)  #强制等待
unitl=ui.WebDriverWait(dr,10)   #创建的一个智能等待的控制器  10是最大等待时间
unitl.until(lambda dr:dr.find_element_by_link_text('hao123').is_displayed())    #检测hao123这个文本是否出现如果定位元素出现了，就不用再等待了，如果没有出现就一直等待最大等待10秒

dr.find_element_by_link_text('新闻').click()
dr.quit()