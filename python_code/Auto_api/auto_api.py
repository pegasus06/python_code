# 日期：2022年04月19日
import requests
class App_api():
    def login(self):
        login_url="http://app.duoceshi.com/api/login"
        headers={"application":"json"}
        login_json={"username":"18675970359","password":"123456","spread":""}
        response=requests.post(url=login_url,headers=headers,json=login_json)
        token=response.json()["data"]["token"]
        return token
    def edit_user(self):
        token=self.login()
        url="http://app.duoceshi.com/api/user/edit"
        headers={"Content-Type":"application/json","Authorization":"Bearer %s"%token}
        login_json={"nickname":"奥力给","avatar":"https://image.dayouqiantu.cn/5e79f6cfd33b6.png"}
        response=requests.post(url=url,headers=headers,json=login_json)
        result=response.json()
        print(result)
if __name__ == '__main__':
   a=App_api()
   a.login()
   a.edit_user()




