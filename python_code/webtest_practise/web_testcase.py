# # # 日期：2022年04月19日
# # """python+requests库
# # 安装：pip install +库名
# # pycharm中解释器里面安装
# # 接口请求的三种方式：
# # r=requests.post(url=url,data=data,json=json)
# #     将每种请求方式封装成一个方法，使用requests模块调用方法
# # r=requests.request(method=get,url=url,data=data)
# #      将所有请求做了二次封装，封装在方法request中，通过传参的形式选择请求方式
# # r=requests.Session()
# #     表示在同一个会话当中，保持上下文，使所有的接口请求你在同一会话当中
# #
# # post请求参数有两种类型，data和json
# #     data：如果请求头中内容类型为Content-Type": "application/x-www-form-urlencoded 使用data参数
# #     json：如果请求头中内容类型为Content-Type": "application/json 使用json参数
# # get请求参数为params
# #
# # 对于cookie的处理：
# #         postman：有cookie code自动记录登录的cookie 给到登录之后的其它接口
# #         python：通过在同一会话，Session
# # """
# # #组建一个post请求接口  ：组建接口请求==》接口url地址，请求头，请求方式，请求参数
# # import requests
# # url="http://cms.duoceshi.cn/cms/manage/loginJump.do"
# # data={"userAccount": "admin","loginPwd": "123456"}#请求参数
# # #请求头
# # headers={"Content-Type": "application/x-www-form-urlencoded"}
# # response=requests.post(url=url,data=data,headers=headers)#将接口的响应报文赋值给变量respons
# # result=response.json()#{'code': '200', 'msg': '登录成功！', 'model': {}}
# # result1=response.text
# # print(response.cookies)
# # print(response.headers)
# # print(response.status_code)
# # # import re
# # response1=requests.get(url=url,params=data,headers=headers)
# # result2=response1.json()
# # print(result2)
#
# #组建一个cms平台查询接口
# #使用Session保持在同一会话，获取登录的cookie
# import requests
# # s=requests.Session()
# # login_response=s.post(url=url,data=data,headers=headers)
# # query_url="http://cms.duoceshi.cn/cms/manage/queryUserList.do"
# # query_data={"startCreateDate": "","endCreateDate": "","searchValue": "ys28jst9","page": 1}
# # query_headers={"Content-Type": "application/x-www-form-urlencoded"}
# # query_response=s.post(url=query_url,data=query_data,headers=query_headers)
# # result=query_response.text
# # print(result)
#
# #使用unittest进行管理
# """
# unittest核心：
# 1.TestCase:封装的类中集成TestCase，将每条实例方法变成测试用例，用例以test开头
# 2.Fixture:setup,teardown(每条用例前执行一次)  setupClass,teardownclass（所有用例只执行一次）
# 3.Suite:测试套件，将需要执行的测试用例通过TestLoader加载到套件中
# 4.Runner：执行器，执行套件中的测试用例
# 5.report：测试报告，结合第三方模块（HtmlTestRunner）
# """
# import unittest
# class Cms_api(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.s=requests.Session()
#     def test_cms_login(self):
#         login_url = 'http://cms.duoceshi.cn/cms/manage/loginJump.do'
#         headers = {"Content-Type": "application/x-www-form-urlencoded"}
#         data = {"userAccount": "admin","loginPwd": "123456"}
#         response=self.s.post(url=login_url,headers=headers,data=data)
#         result=response.json()['msg']
#         self.assertEqual(result,'登录成功！')
#     def test_cms_queryUserlist(self):
#         query_url="http://cms.duoceshi.cn/cms/manage/queryUserList.do"
#         query_data={"startCreateDate": "","endCreateDate": "","searchValue": "ys28jst9","page": 1}
#         query_headers={"Content-Type": "application/x-www-form-urlencoded"}
#         response = self.s.post(url=query_url, data=query_data, headers=query_headers)
#         result=response.json()['msg']
#         self.assertIn('查询用户成功',result)
# if __name__ == '__main__':
#     # unittest.main()#通过main函数执行所有测试用例
#     # suite=unittest.TestSuite()
#     # suite.addTest(Cms_api('test_cms_login'))
#     # suite.addTest(Cms_api('test_cms_queryUserlist'))
#     # 使用discover的方法到指定路径加载测试用例到套件中
#     path=r'E:\python_code\report'
#     file_name=path+"\\"+"testcase.html"
#     startpath="E:\python_code\webtest_practise"
#     with open(file_name,"wb")as f:
#         discover=unittest.TestLoader().discover(startpath,"web_testcase.py")
#         # runner=unittest.TextTestRunner()
#         # runner.run(discover)
#         from webtest_practise import HTMLTestRunner3_New
#         runner=HTMLTestRunner3_New.HTMLTestRunner(stream=f,tester='zr',description="测试执行如下",title="测试执行报告")
#         runner.run(discover)


#关联接口一：省份和城市
import random

import requests
import re
# class Test_1():
#     def get_province(self):
#         province_url="http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportProvince"
#         response=requests.post(url=province_url)
#         result=response.text
#         provinces=re.findall('<string>(.+)</string>',result)
#         return provinces
#     def get_city(self):
#         city_url="http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity"
#         province=random.choices(self.get_province())
#         city_params = {'byProvinceName': province}
#         response=requests.get(params=city_params,url=city_url)
#         result=response.text
#         result1=re.findall('<string>(.*?)</string>', result)
#         print(result1)
class Y_shop():
    def code(self):
        code_url="http://manage.duoceshi.com/auth/code"
        response=requests.get(code_url)
        result=response.json()['uuid']
        return result
    def login(self):
        uuid=self.code()
        login_url="http://manage.duoceshi.com/auth/login"
        login_json={"username":"admin","password":"jp4GtyKy0FuQw3AljeqAoD70hItiHNZo97ZeE/0FZZXl2tTGYjI67swGiyzWdmKWeXj+y1rimNVUQ6Rol2bGHA==","code":"8888","uuid":uuid}
        login_headers={'Content-Type':'application/json'}
        response=requests.post(url=login_url,headers=login_headers,json=login_json)
        result=re.findall('"token":"(.*?)"',response.text)[0]
        return result
    def build(self):
        token=self.login()
        build_url='http://manage.duoceshi.com/api/menus/build'
        build_headers = {'Authorization':token}
        response=requests.get(url=build_url,headers=build_headers)
        result=response.json()
        print(result)

if __name__ == '__main__':
    # province=Test_1()
    # province.get_province()
    # province.get_city()
    y=Y_shop()
    y.code()
    y.login()
    y.build()

