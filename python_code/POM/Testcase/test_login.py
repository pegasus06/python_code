# 日期：2022年04月20日
import unittest
from time import sleep

from ddt import ddt, data, unpack

from POM.Base.Page_method import Page_method
from selenium import webdriver
from POM.PageObject.PageObject import Page_Object


@ddt
class Test_login(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.start = Page_Object(self.driver)

    def tearDown(self) -> None:
        sleep(3)
        self.driver.close()

    @data(*Page_Object(None).read_data(Page_Object.path))
    @unpack
    def test_login001(self, user, pwd):
        self.start.login1(user, pwd)

    def test_login002(self):
        self.start.login2()

    def test_login003(self):
        self.start.login3()


if __name__ == '__main__':
    unittest.main()
