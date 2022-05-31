# 日期：2022年04月20日
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import yaml

class Page_method():
    # driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    def login(self, loc):
        return self.driver.find_element(*loc)

    def visit(self, url):
        return self.driver.get(url)

    def send_keys(self, loc, text):
        return self.login(loc).send_keys(text)

    def click(self, loc):
        return self.login(loc).click()

    def switch_alert(self, flag=None, text=None):
        """
        :param flag:输入accept,输入dismiss
        :param text:输入的内容
        :return:
        """
        alter = self.driver.switch_to.alert
        if flag == 'accept':
            alter.accept()
        elif flag == 'dismiss':
            alter.dismiss()
        else:
            alter.send_keys(text)

    def mouse_over(self, loc):
        ele = self.login(loc)
        ActionChains(self.driver).move_to_element(ele).perform()

    def read_data(self, path):
        list1 = []
        with open(path, "r")as f:
            lines = f.readlines()
            for i in lines:
                list1.append(i.strip('\n').split('_'))
        return list1
    def read_yml(self,file_path):
        with open(file_path,"r")as f:
            a=yaml.load(stream=f,Loader=yaml.FullLoader)
            return a



if __name__ == '__main__':
    # path = r"E:\python_code\POM\Data\data"
    # Page_method(None).read_data(path)
    path='E:\python_code\Data\data1.yml'
    b=Page_method("age")
    print(b.read_yml(path))