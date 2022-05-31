# 日期：2022年04月18日
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
handle=driver.current_window_handle#获取当前页面的句柄
new_win="window.open('http://www.jd.com')"            #新开一个窗口打开京东
driver.execute_script(new_win)
new_win1="window.open('http://www.baidu.com')"
driver.execute_script(new_win1)
new_win1="window.open('http://www.taobao.com')"
driver.execute_script(new_win1)
new_wind="window.open('http://www.baidu.com')"
driver.execute_script(new_wind)
handles=driver.window_handles
driver.switch_to.window(handles[3])  #自己的窗口句柄为0，新开的窗口第一个永远是-1，最后一个是1
print(driver.title)
#new_win="window.open("http://www.baidu.com")
# driver.execute_script(new_win)

