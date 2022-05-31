import re
import csv
result1=[]
with open('xasx.txt','r',encoding='utf-8')as f:
    s=f.read()
username=re.findall('username="(.*?)"',s,flags=re.S)
ip=re.findall('IP属地:(.*?)</span>',s,flags=re.S)
for i in range(len(username)):
    result={'username':username[i],'ip':ip[i]}
    result1.append(result)
with open('aaaa.csv','w',encoding='utf-8')as f:
    writer=csv.DictWriter(f,fieldnames=['username','ip'])
    writer.writeheader()
    writer.writerows(result1)

