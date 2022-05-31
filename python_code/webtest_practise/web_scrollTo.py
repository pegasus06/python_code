# 日期：2022年04月18日
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.jd.com")
js="window.scrollTo(0,800)"
driver.execute_script(js)