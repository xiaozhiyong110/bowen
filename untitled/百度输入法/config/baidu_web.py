from selenium import webdriver
from time import sleep
def baidu_web(name):
    dr=webdriver.Firefox()
    dr.get('https://shurufa.baidu.com/')
    sleep(2)
    dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[2]/a').click()
    sleep(2)
    dr.find_element_by_xpath('//*[@id="keyword"]').send_keys('{}'.format(name))
    sleep(2)
    dr.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[1]/form/div/div[2]/button').click()
    sleep(2)
    try:
        b=dr.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[2]').text
        print(b)
    except:
        b=dr.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/a[2]').text
        print(b)
    return b