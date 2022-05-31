# 日期：2022年04月20日
from selenium import webdriver
from selenium.webdriver.common.by import By

from Base.Page_method import Page_method


class Page_Object(Page_method):
    path=r"E:\python_code\POM\Data\data"
    url = 'http://cms.duoceshi.cn/cms/manage/login.do'
    username = (By.ID, "userAccount")
    password = (By.ID, "loginPwd")
    login_btn = (By.ID, "loginBtn")

    def login1(self,user,pwd):
        self.visit(self.url)
        self.send_keys(self.username,user)
        self.send_keys(self.password,pwd)
        self.click(self.login_btn)
    def login2(self):
        pass
    def login3(self):
        pass
if __name__ == '__main__':
    driver=webdriver.Chrome()
    Page_Object(driver).login1("admin",123456)
