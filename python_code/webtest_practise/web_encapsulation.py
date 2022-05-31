# 日期：2022年04月18日
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

class Cms():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://cms.duoceshi.cn/cms/manage/login.do")
    def login(self):
        self.driver.find_element(By.ID,"userAccount").send_keys("admin")
        self.driver.find_element(By.ID,"loginPwd").send_keys('123456')
        self.driver.find_element(By.ID,"loginBtn").click()
        sleep(3)
        value=self.driver.find_element(By.XPATH,"/html/body/div/aside/div/dl[1]/dt").text
        assert value=="用户中心"
    def user_center(self):
        self.driver.find_element(By.XPATH,'/html/body/div/aside/div/dl[1]/dt').click()
        value=self.driver.find_element(By.XPATH,'/html/body/div/aside/div/dl[1]/dd/ul/li[1]/a').text
        assert value=='用户管理'
        self.driver.find_element(By.XPATH, '/html/body/div/aside/div/dl[1]/dd/ul/li[1]/a').click()
        iframe=self.driver.find_element(By.XPATH,"/html/body/div/section/div[2]/div[2]/iframe")
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/span[1]/a[2]").click()
        iframe1 = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/iframe")
        self.driver.switch_to.frame(iframe1)
        self.driver.find_element(By.ID,"userName").send_keys("婷婷宝贝")
        self.driver.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[3]/td/input").send_keys("17765125486")
        self.driver.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[4]/td/input").send_keys("123@163.com")
        self.driver.find_element(By.ID,"userAccount").send_keys("ssssww")
        self.driver.find_element(By.NAME,"loginPwd").send_keys("123456")
        self.driver.find_element(By.XPATH,"/html/body/div/div/form/table/tbody/tr[7]/td/input").send_keys("123456")
        self.driver.find_element(By.ID,"submitBtn").click()
        sleep(3)
        # js=self.driver.switch_to.alert
        # js.accept()
        self.driver.switch_to.default_content()
if __name__ == '__main__':
    c=Cms()
    c.login()
    c.user_center()




