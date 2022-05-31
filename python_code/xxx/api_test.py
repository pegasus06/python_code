# # # # # 日期：2022年04月22日
# # # # # from appium import webdriver
# # # # # desired_caps={
# # # # #     "platformName":"Android",
# # # # #     "deviceName":"SM-G977N",
# # # # #     "platformVersion":"7.1.2",
# # # # #     "appPackage":"com.baidu.yuedu",
# # # # #     "appActivity":"com.baidu.yuedu.splash.SplashActivity",
# # # # #     "unicodeKeyboard":True
# # # # # }
# # # # # driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
# # # # # driver.
# # # # import json
# # # # from collections import namedtuple
# # # # from functools import reduce
# # # #
# # # # from POM.Utils.HTMLTestRunner3_New import main
# # # #
# # # # """你能否把 NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），而 output.txt 不会很大（意味着重复的单词数量很多）。提示：
# # # # 你可能需要每次读取一定长度的字符串，进行处理，然后再读取下一次的。但是如果单纯按照长度划分，你可能会把一个单词隔断开，所以需要细心处理这种边界情况。"""
# # # # # import re
# # # # #
# # # # #
# # # # # def parse(text):
# # # # #     text = re.sub('r[^\w]', " ", text)
# # # # #     text = text.lower()
# # # # #     word_list = text.split(" ")
# # # # #     word_list = filter(None, word_list)
# # # # #     print(type(word_list))
# # # # #     word_cnt = {}
# # # # #     for word in word_list:
# # # # #         word_cnt.setdefault(word, 0)
# # # # #         word_cnt[word] = word_cnt[word] + 1
# # # # #     sorted_word = sorted(word_cnt.items(), key=lambda x: x[0], reverse=True)
# # # # #     return sorted_word
# # # # #
# # # # #
# # # # # with open("xxx.txt", "r",encoding="utf-8")as f:
# # # # #     text1 = f.read()
# # # # #     print(type(text1))
# # # # #     word=parse(text1)
# # # # #     with open('out.txt',"w")as aa:
# # # # #          for word1,freq in word:
# # # # #             aa.write("{}{}\n".format(word1,freq))
# # # # # def sum(a,b):
# # # # #     return a+b
# # # # # try:
# # # # #     tot=sum([1,2,3],2)
# # # # #     print(tot)
# # # # # except TypeError as err:
# # # # #     print("Err is{}".format(err))
# # # # #     isinstance([1,2,3],list)
# # # # # def nth_powe(exponent):
# # # # #     def exponent_of(base):
# # # # #         return base ** exponent
# # # # #     return exponent_of
# # # # # square=nth_powe(3)
# # # # # print(square(2))
# # # # # squared=map(lambda x:x**2,[1,2,3])
# # # # # print(list(squared))
# # # # # from tkinter import Button,mainloop
# # # # # button=Button(text="this is a button",command=lambda :print('being pressed'))
# # # # # button.pack()
# # # # # mainloop()
# # # # # l=[1,2,3,4]
# # # # # print(reduce(lambda x,y:x * y, l))
# # # # from selenium import webdriver
# # # #
# # # # # class Document(metaclass=):
# # # # #     def __init__(self,name):
# # # # #         self.name=name
# # # # #     def aaa(self):
# # # # #         print(f"{self.name}爱吃鱼")
# # # # # aa=Document("小猫")
# # # # # dict1={"age":2,"name":"zhangsan"}
# # # # # print(dict1.__getitem__("age"))
# # # # # Card=namedtuple('Card',['rank','suit'])
# # # # # str1="sadasd sadasda dadaf asfasf xsua xsud"
# # # # # a=map(str1.split(),str1)
# # # # # print(list(a))
# # # # uncofirmed_users = ['alice', 'brian', 'candace']
# # # # confirmed_users = []
# # # # while uncofirmed_users:
# # # #     current_users = uncofirmed_users.pop()
# # # #     confirmed_users.append(current_users)
# # # # for i in confirmed_users:
# # # #     print(i)
# # # """class Dog():
# # # 	def __init__(self,name,age):
# # # 		self.name=name
# # # 		self.age=age
# # # 	def sit(self):
# # # 		print(self.name.title()+" is now sitting")
# # # 	def roll_back(self):
# # # 		print(self.name+" is "+self.age+" years old rolled over")
# # # dog=Dog("Tom","18")
# # # dog.sit()
# # # print(dog.name)
# # # print(dog.age)
# # # dog.roll_back()
# # # class Restaurant():
# # # 	def __init__(self,restaurant_name,cuisine_type):
# # # 		self.name=restaurant_name
# # # 		self.type=cuisine_type
# # # 	def describe_restaurant(self):
# # # 		print("restaurant"+self.name+"is "+self.type)
# # # 	def open_restaurant(self):
# # # 		print(self.name+"is open")
# # # restaurant=Restaurant("KFC","open")
# # # restaurant.describe_restaurant()"""
# # # class Car():
# # #     """一次模拟汽车的简单尝试"""
# # #     def __init__(self, make, model, year):
# # #         self.make = make
# # #         self.model = model
# # #         self.year = year
# # #         self.odometer_reading = 0
# # #     def get_descriptive_name(self):
# # #         long_name = str(self.year)+' '+self.make+' '+self.model
# # #         return long_name.title()
# # #     def read_odometer(self):
# # #         print("This car has "+str(self.odometer_reading)+" miles on it.")
# # #     def update_odometer(self, mileage):
# # # 		if mileage >= (self.odometer_reading):
# # #             self.odometer_reading = mileage
# # #         else:
# # #             print("You can't roll back an odometer!")
# # #     def increment_odometer(self, miles):
# # #         self.odometer_reading+= miles
# # # class Battery():
# # # 	def __init__(self,battery_size=70):
# # # 	    self.battery_size=battery_size
# # # 	def describe_battery(self):
# # # 		print("this car has a "+str(self.battery_size)+"-kwh battery")
# # # class ElectricCar(Car):
# # # 	def __init__(self,make,model,year):
# # # 		super.__init__(make,model,year)
# # # 		self.battery=Battery()
# # # my_tesla=ElectricCar('tesla','models',2016)
# # # print(my_tesla.get_descriptive_name())
# # # my_tesla.battery.describe_battery()
# # #
# # #
# # # def increment_odometer(self, miles):
# # #     self.odometer_reading += miles
# # #
# # #
# # # class Battery():
# # #     def __init__(self, battery_size=70):
# # #         self.battery_size = battery_size
# # #
# # #     def describe_battery(self):
# # #         print("this car has a " + str(self.battery_size) + "-kwh battery")
# # #
# # #
# # # class ElectricCar(Car):
# # #     def __init__(self, make, model, year):
# # #         super.__init__(make, model, year)
# # #         self.battery = Battery()
# # #
# # #
# # # my_tesla = ElectricCar('tesla', 'models', 2016)
# # # print(my_tesla.get_descriptive_name())
# # # my_tesla.battery.describe_battery()
# # #
# # #
# # import requests
# # import time
# #
# #
# # def download_one(url):
# #     resp = requests.get(url)
# #     print('Read {} from {}'.format(len(resp.content), url))
# #
# #
# # def download_all(sites):
# #     for site in sites:
# #         download_one(site)
# #
# #
# # def main():
# #     sites = [
# #         'https://en.wikipedia.org/wiki/Portal:Arts',
# #         'https://en.wikipedia.org/wiki/Portal:History',
# #         'https://en.wikipedia.org/wiki/Portal:Society',
# #         'https://en.wikipedia.org/wiki/Portal:Biography',
# #         'https://en.wikipedia.org/wiki/Portal:Mathematics',
# #         'https://en.wikipedia.org/wiki/Portal:Technology',
# #         'https://en.wikipedia.org/wiki/Portal:Geography',
# #         'https://en.wikipedia.org/wiki/Portal:Science',
# #         'https://en.wikipedia.org/wiki/Computer_science',
# #         'https://en.wikipedia.org/wiki/Python_(programming_language)',
# #         'https://en.wikipedia.org/wiki/Java_(programming_language)',
# #         'https://en.wikipedia.org/wiki/PHP',
# #         'https://en.wikipedia.org/wiki/Node.js',
# #         'https://en.wikipedia.org/wiki/The_C_Programming_Language',
# #         'https://en.wikipedia.org/wiki/Go_(programming_language)'
# #     ]
# #     start_time = time.perf_counter()
# #     download_all(sites)
# #     end_time = time.perf_counter()
# #     print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
# #
# #
# # if __name__ == '__main__':
# #     main()
# import os
# import psutil
# from derange import derange
#
#
# # 显示当前 python 程序占用的内存大小
# def show_memory_info(hint):
#     pid = os.getpid()
#     p = psutil.Process(pid)
#     info = p.memory_full_info()
#     memory = info.uss / 1024. / 1024
#     print('{} memory used: {} MB'.format(hint, memory))
#
#
# def func():
#     show_memory_info('initial')
#     a = [i for i in derange(10000000)]
#     show_memory_info('after a created')
#     return a
#
#
# a = func()
# show_memory_info('finished')
# from objgraph import show_refs
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# a.append(b)
# b.append(a)
#
import objgraph
a=[1,2,3]
b=[4,5,6]
a.append(b)
b.append(a)
objgraph.show_refs([a], filename='sample-graph.png')