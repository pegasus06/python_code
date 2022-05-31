# # # # 日期：2022年04月19日
# # # # app_ui自动化
# # # from appium import webdriver
# # # from selenium.webdriver.common.by import By
# # #
# # # desired_caps={"platformName":"Android",#连接的平台名字
# # #               "deviceName":"SM-G977N",#连接设备名称
# # #               "platformVersion":"7.1.2",#平台系统版本
# # #               "appActivity":"com.baidu.yuedu.splash.SplashActivity",#activity
# # #               "appPackage":"com.baidu.yuedu",#需要操作的app包名
# # #               "unicodeKeyboard":True}#输入按键
# # # driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# # # # driver.find_element(By.XPATH,"")
# # # driver.implicitly_wait(60)
# # # print("================")
# # # l1=[[1,2],1]
# # # l2=list(l1)
# # # print(id(l1))   #2536811782912
# # # l1.append(1)
# # # print(l1)       #[[1, 2], 1, 1]
# # # print(l2)       #[[1, 2], 1]
# # # print(id(l1))   #2536811782912
# # # print(id(l2))   #2536810354048
# # # def my_decorator(func):
# # #     def wrapper():
# # #         print('wrapper of decorator')
# # #         func()
# # #
# # #     return wrapper
# # #
# # #
# # # @my_decorator
# # # def greet():
# # #     print('hello world')
# # # def wrap(obj):
# # #     obj.name="python"
# # #     return obj
# # # @wrap #Bar=warp(Bar)
# # # class Bar():
# # #     # def __init__(self):
# # #         pass
# # # print(Bar.name)
# #
# #
# # # def my_decorator(func):
# # #     def wrapper(message):
# # #         print('wrapper of decorator')
# # #         func(message)
# # #
# # #     return wrapper
# # #
# # #
# # # # @my_decorator
# # # def greet(message):
# # #     print(message)
# # #
# # # aa=my_decorator(greet)
# # # aa('hello world')
# # # def my1(func):
# # #     def wap():
# # #         print("hello")
# # #         func()
# # #     return wap
# # # @my1
# # # def greet():
# # #     print("hahah")
# # #
# # # greet=my1(greet)
# # # greet()
# #
# #
# # # def my_decorator(func):    #my_decorator(greet)
# # #     def wrapper(message):
# # #         print('wrapper of decorator')
# # #         func(message)
# # #
# # #     return wrapper          #message="hello world"
# # #
# # #
# # # @my_decorator
# # # def greet(message):
# # #     print(message)
# # #
# # #
# # # greet('hello world')
# # # def repeat(num):      #repeat(greet)
# # #     def my_decorator(func):
# # #         def wrapper(*args, **kwargs):  #wrapper(greet)
# # #             for i in range(num): #4
# # #                 print('wrapper of decorator')
# # #                 func(*args, **kwargs)
# # #
# # #         return wrapper   #wrapper("hello world")
# # #
# # #     return my_decorator
# # #
# # #
# # # @repeat(4)
# # # def greet(message):
# # #     print(message)
# # #
# # #
# # # greet('hello world')
# #
# # # def outer(obj):  # 类方法装饰器
# # #     def inner():
# # #         print('hello inner')
# # #         obj()
# # #
# # #     return inner
# # #
# # #
# # # # class Zoo(object):
# # # #     def __init__(self):
# # # #         pass
# # #
# # # @outer  # => zoo = outer(zoo)
# # # def zoo():
# # #     print('hello zoo')
# # #
# #
# #
# # # import time
# # #
# # # def timeit(itration):
# # #     def inner(f):   #inner(f--double)
# # #         def wrapper(*args,**kwargs): #wrapper(double)
# # #             start=time.time()
# # #             for _ in range(itration):
# # #                 ret=f(*args,**kwargs) #
# # #             print(time.time()-start)
# # #             return ret
# # #         return wrapper
# # #     return inner
# # # @timeit(1000)       #double=timeit(1000)(double)
# # # def double(x):
# # #     return x*2
# # # double(2)
# # # import time
# # #
# # #
# # # class Timer:
# # #     def __init__(self,prefix):
# # #         self.prefix=prefix
# # #     def __call__(self, func):
# # #         def wrapper(*args,**kwargs):
# # #             start=time.time()
# # #             ret=func(*args,**kwargs)
# # #             print(f"{self.prefix}")
# # #             return ret
# # #         return wrapper
# # # @Timer(prefix="current_time")
# # # def add(a,b):
# # #     return a+b
# # # print(add(2,3))
# # # def in_iterable(param):
# # #     try:
# # #         iter(param)
# # #         return True
# # #     except TypeError:
# # #         return False
# # # params=[
# # #     '1234',
# # #     [1, 2, 3, 4],
# # #     set([1, 2, 3, 4]),
# # #     {1:1, 2:2, 3:3, 4:4},
# # #     (1, 2, 3, 4)
# # # ]
# # # def is_iterable(param):
# # #     try:
# # #         iter(param)
# # #         return True
# # #     except TypeError:
# # #         return False
# # # for param in params:
# # #     print(f"{param} is iterable?\t{is_iterable(param)}")
# #
# # # import os
# # # import psutil
# # # def show_memory_info(hint):
# # #     pid=os.getpid()
# # #     p=psutil.Process(pid)
# # #     info=p.memory_full_info()
# # #     memory=info.uss/1024./1024
# # #     print("{}memory used:{}MB".format(hint,memory))
# # #
# # # def test_iterator():
# # #     show_memory_info('initing iterator')
# # #     list_1 = [i for i in range(100000000)]
# # #     show_memory_info('after iterator initiated')
# # #     print(sum(list_1))
# # #     show_memory_info('after sum called')
# # #
# # # def test_generator():
# # #     show_memory_info('initing generator')
# # #     list_2 = (i for i in range(100000000))
# # #     show_memory_info('after generator initiated')
# # #     print(sum(list_2))
# # #     show_memory_info('after sum called')
# # #
# # # test_iterator()
# # # test_generator()
# # from time import sleep
# #
# # from selenium import webdriver
# # from threading import Thread
# #
# # from selenium.webdriver.common.by import By
# #
# #
# # def test_baidu_search(browser,url):
# #     driver=None
# #     if browser=="edge":
# #         driver=webdriver.Edge()
# #     elif browser=="chrome":
# #         driver=webdriver.Chrome()
# #     if driver==None:
# #         exit()
# #     driver.get(url)
# #     driver.find_element(By.ID,"kw").clear()
# #     driver.find_element(By.ID,"kw").send_keys("张真真")
# #     driver.find_element(By.ID,"su").click()
# #     sleep(3)
# #     driver.quit()
# # if __name__ == '__main__':
# #     data={"edge":"http://www.baidu.com",
# #           "chrome":"http://www.baidu.com"}
# #     thread=[]
# #     for b,url in data.items():
# #         t=Thread(target=test_baidu_search,args=(b,url))
# #         thread.append(t)
# #     for i in thread:
# #         i.start()time=2.090287923812866   0.1160280704498291
#
#
# import requests
# import time
# # start_time=time.time()
# # for i in range(100):
# #     request=requests.post("http://www.baidu.com")
# # end_time=time.time()
# # print(f"time={end_time-start_time}")
# from concurrent.futures import ProcessPoolExecutor#进程池
# from threading import Thread
# from concurrent.futures.thread import ThreadPoolExecutor#线程池
# def task(id):
#     request = requests.get("http://www.baidu.com")
#     print(id,request.status_code)
# if __name__ == '__main__':
#     start_time = time.time()
#     users=20
#     with ThreadPoolExecutor(users)as p:#创建10个线程
#         p.map(task,range(users)) #把10个进程提交给线程池执行
#     end_time=time.time()
#     print(f"{end_time-start_time}")
#
# import time
# from gevent import monkey
# monkey.patch_all()#猴子补丁，替换python底层代码，实现协程
#
# from gevent.pool import Pool#导入协程值
# import requests
# def task(id):
#     request = requests.get("http://www.baidu.com")
#     print(id,request.status_code)
# if __name__ == '__main__':
#     start_time = time.time()
#     users=20
#     pool=Pool(users)
#     pool.map(task,range(users))
#     end_time=time.time()
#     print(f"{end_time-start_time}")


