# 日期：2022年04月18日
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# new_win='window.open("http://www.mail.163.com")'
# driver.execute_script(new_win)
driver.get("http://www.mail.163.com")
# driver.switch_to.frame(0)
# driver.find_element(By.NAME,'email').send_keys('18675970359')
a=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div[4]/div[1]/div[1]/iframe")
driver.switch_to.frame(a)
driver.find_element(By.NAME,'email').send_keys('18675970359')
driver.switch_to.default_content()
