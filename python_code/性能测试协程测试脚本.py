# 日期：2022年05月07日
from statistics import mean

from gevent import monkey
from gevent.pool import Pool
import requests
import time
err_list=[]
ok_list=[]
def task(id):
    for i in range(query_count):
        try:
            res=requests.get(url)
            print(f"用户：{id}发送第{i},响应状态码为{res.status_code}")
            ok_list.append(res.elapsed.total_seconds())
        except Exception as e:
            err_list.append((f"{id},{i},{url},{time.time()},{e}"))
if __name__ == '__main__':
    users=int(input("请输入模拟用户的数量")) #接口收到的请求数量=用户数量*循环次数
    query_count=int(input("请输入循环的次数"))
    url=input("请输入被测的接口")
    pool=Pool(users)
    start_time=time.time()
    pool.map(task,range(users))
    end_time=time.time()
    print("=="*40)
    print("接口地址：",url)
    print(f"用户数：{users},循环次数:{query_count}")
    print(f"耗时{end_time-start_time}")
    print("最快响应:",max(ok_list))
    print("最慢响应:",min(ok_list))
    print("RPS:",len(ok_list)/mean(ok_list))