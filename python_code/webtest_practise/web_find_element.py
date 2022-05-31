# 日期：2022年04月18日
from time import sleep

import document
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()#实例化浏览器对象
#WebDriverWait(driver,10,0.5).until(EC.presence_of_all_elements_located(By.ID,"userAccount"))
driver.implicitly_wait(20)
driver.get("http://localhost:8080/cms/manage/login.do")
driver.get_window_size()
#s=driver.find_element(By.TAG_NAME,"input")
# for i in s:
#     if i.get_attribute('id')=="userAccount":
#         i.send_keys("admin")
JS='var a=document.getElementById("userAccount").value="admin"'
driver.execute_script(JS)
"""var a 为用java定义一个变量"""
# driver.find_element(By.ID,"userAccount").send_keys("admin")
driver.find_element(By.NAME,"loginPwd").send_keys(u"123456")
driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div[3]/label/input").click()
driver.find_element(By.ID,"loginBtn").click()
driver.find_element(By.XPATH,"/html/body/div/aside/div/dl[1]/dt").click()
sleep(2)
s=driver.find_element(By.TAG_NAME,"input")
print(s)
driver.close()
