# 日期：2022年04月18日
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(By.ID,"kw").send_keys("python")
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.BACK_SPACE)
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,'a')
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,'c')
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.BACK_SPACE)
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.CONTROL,'v')
sleep(1)
driver.find_element(By.ID,"kw").send_keys(Keys.ENTER)
sleep(1)
driver.close()



