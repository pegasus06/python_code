# from ddt import ddt,file_data
# import unittest
# @ddt
# class Demo(unittest.TestCase):
#     @file_data("E:\python_code\Data\data1.yml")
#     def test01(self,*args,**kwargs):
#         print(args,kwargs)
# if __name__ == '__main__':
#     unittest.main()
import yaml
from ddt import ddt,file_data
with open("/Data/data1.yml", "r", encoding="utf-8")as f:
    a=yaml.load(stream=f,Loader=yaml.FullLoader)
    print(a)