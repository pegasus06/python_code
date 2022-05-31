# 日期：2022年04月18日
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
ele=driver.find_element(By.ID,"s-usersetting-top")
ActionChains(driver).move_to_element(ele).perform()
driver.find_element(By.LINK_TEXT,"搜索设置").click()

