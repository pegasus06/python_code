# 日期：2022年04月18日
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
ele=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[4]/span")
ActionChains(driver).move_to_element(ele).perform()
driver.find_element(By.LINK_TEXT,"搜索设置").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT,'保存设置').click()
time.sleep(1)
t=driver.switch_to.alert
t.accept()

