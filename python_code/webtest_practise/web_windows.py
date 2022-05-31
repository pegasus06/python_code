# 日期：2022年04月18日
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http:\\www.baidu.com")
driver.maximize_window()
driver.get_window_size()
driver.refresh()
assert driver.title=='百度一下，你就知道'
driver.close()
driver.quit()
