# # 日期：2022年05月04日
# import sys
#
# from prompt_toolkit.application import current
#
#
# class SearchEngineBase(object):
#     def __init__(self):
#         pass
#
#     def add_corpus(self, file_path):
#         with open(file_path, 'r') as fin:
#             text = fin.read()
#         self.process_corpus(file_path, text)
#
#     def process_corpus(self, id, text):
#         raise Exception('process_corpus not implemented.')
#
#     def search(self, query):
#         raise Exception('search not implemented.')
#
#
# def main(search_engine):
#     for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
#         search_engine.add_corpus(file_path)
#
#     while True:
#         query = input()
#         results = search_engine.search(query)
#         print('found {} result(s):'.format(len(results)))
#         for result in results:
#             print(result)
# import os
#
# print(os.getcwd())
# print(sum(range(1,1001)))
# import csv
# with open('sss.csv','r')as f:
#     a=csv.DictReader(f)    #生成器
#     print(a)
#     for i in a:
#         print(i['user'])
import csv

data=[{'name':'kingname','age':24,'salary':99999},{'name':'meiji','age':20,'salary':100}]
with open('new.csv','w',encoding='utf-8')as f:
    writer=csv.DictWriter(f,fieldnames=['name','age','salary'])
    writer.writeheader()
    writer.writerows(data)
    writer.writerow({'name':'超人','age':999,'salary':0})
