import requests
url="http://cms.duoceshi.cn/cms/manage/loginJump.do"
data={"userAccount":"admin","loginPwd":"123456"}
resp=requests.post(url,params=data)
print(resp.json())
