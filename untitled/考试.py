# from selenium import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('https://www.baidu.com')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u1"]/a[1]').click()
# print(dr.title)
# print(dr.current_url)
# dr.set_window_position(400,400)
# dr.set_window_size(400,400)
# dr.maximize_window()
# dr.minimize_window()
# dr.get('https://www.jd.com')
# sleep(2)
# dr.back()
# sleep(2)
# dr.forward()
# sleep(2)
# dr.find_element_by_id('kw').send_keys('python')
# sleep(2)
# dr.find_element_by_id('su').click()
# dr.find_element_by_name('wd').send_keys('python')
# sleep(2)
# dr.find_element_by_id('su').click()

# dr.find_element_by_class_name('s_ipt').send_keys('python')
# dr.find_element_by_link_text('hao123').click()
# dr.find_element_by_partial_link_text('hao').click()
# print(dr.find_elements_by_tag_name())
# dr.find_element_by_xpath('//*[@id="u_sp"]/a[1]').click()
# dr.find_element_by_css_selector('#u_sp > a:nth-child(1)')


#登录QQ空间
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1287347397')
# sleep(2)
# dr.find_element_by_id('p').click()
# sleep(2)
# dr.find_element_by_id('p').send_keys('')
# sleep(2)
# dr.find_element_by_id('login_button').click()



# from selenium import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com')
# dr.switch_to.frame('login_frame')
# dr.find_element_by_xpath('//*[@id="img_out_1287347397"]').click()
# sleep(5)
# dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys(' 我用程序写了个说说，我成功了')
# dr.find_element_by_xpath('//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]/span').click()

# import unittest
# class Test(unittest.TestCase):
#     def test_1(self):
#         #假设预期结果是1，实际结果是2，判断预期结果是否等于实际结果
#         a=1   #预期结果
#         #断言：
#         self.assertEqual(a,1)
# if __name__=="__main__":
#     unittest.main()


