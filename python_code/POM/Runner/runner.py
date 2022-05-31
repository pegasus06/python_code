# 日期：2022年04月20日
import unittest
from POM.Utils import HTMLTestRunner3_New
class Run_cms():
    def run(self,report_path,case_path):
        file_name=report_path+"\\"+"aa.html"
        with open(file_name,"wb")as f:
            discover=unittest.TestLoader().discover(case_path,"*")
            runner=HTMLTestRunner3_New.HTMLTestRunner(stream=f,tester='zr',description='测试执行如下',title="测试报告")
            runner.run(discover)
if __name__ == '__main__':
    Run_cms().run(r"E:\python_code\report",r"E:\python_code\POM\Testcase")
