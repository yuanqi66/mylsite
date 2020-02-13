import unittest
from time import sleep
from selenium import webdriver
from ddt import ddt, data, file_data, unpack


@ddt
class TestBaiDu(unittest.TestCase):
    """百度搜索测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        """百度搜索关键字方法"""
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)
    """
    # 参数化使用方式一，使用列表
    @data(["case1", "selenium"], ["case2", "ddt"], ["case3", "python"])
    @unpack
    def test_search1(self, case, search_key):
        print("第一组测试用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "百度搜索")

    # 参数化使用方式二，使用元组
    @data(("case1", "selenium"), ("case2", "ddt"), ("case3", "python"))
    @unpack
    def test_search1(self, case, search_key):
        print("第二组测试用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "百度搜索")

    # 参数化使用方式三，使用字典
    @data({"case1", "selenium"}, {"case2", "ddt"}, {"case3", "python"})
    @unpack
    def test_search1(self, case, search_key):
        print("第三组测试用例：", case)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "百度搜索")
    """
    # 参数化读取JSON文件
    @file_data('ddt_data_file.json')
    def test_search4(self, search_key):
        print("第四组测试用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # 参数化读取yaml文件
    @file_data('ddt_data_file.yaml')
    def test_search5(self, case):
        search_key = case[0]["search_key"]
        print("第五组测试用例：", search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
