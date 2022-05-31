# 日期：2022年04月21日
"""
python+requests库
安装：pip install +库名
pycharm中解释器里面安装
接口请求的三种方式：
r=requests.post(url=url,data=data,json=json)
    将每种请求方式封装成一个方法，使用requests模块调用方法
r=requests.request(method=get,url=url,data=data)
     将所有请求做了二次封装，封装在方法request中，通过传参的形式选择请求方式
r=requests.Session()
    表示在同一个会话当中，保持上下文，使所有的接口请求你在同一会话当中

post请求参数有两种类型，data和json
    data：如果请求头中内容类型为Content-Type": "application/x-www-form-urlencoded 使用data参数
    json：如果请求头中内容类型为Content-Type": "application/json 使用json参数
get请求参数为params

对于cookie的处理：
        postman：有cookie code自动记录登录的cookie 给到登录之后的其它接口
        python：通过在同一会话，Session
"""
import requests
login_url="http://cms.duoceshi.cn/cms/manage/loginJump.do"
hearers={"Content-Type": "application/x-www-form-urlencoded"}
data={"userAccount": "admin",
        "loginPwd": "123456"}
# response=requests.post(url=login_url,headers=hearers,data=data)
# result=response.json()#.text
# # assert result["msg"]=="登录成功！"
# #get请求
# response=requests.get(params=data,url=login_url,headers=hearers)
# login_response=response.json()
# print(login_response)


#组建cms平台查询接口
#使用session保持同一会话，获取登录的cookie
s=requests.Session()
login_response=s.post(url=login_url,data=data,headers=hearers)
query_url='http://cms.duoceshi.cn/cms/manage/queryUserList.do'
query_data={"startCreateDate": "",
            "endCreateDate": "",
            "searchValue": "ys28jst9",
            "page": 1}
query_headers={"Content-Type": "application/x-www-form-urlencoded"}
query_response=s.post(query_url,data=query_data,headers=query_headers)  #发送一个查询接口
result=query_response.text
print(result)

