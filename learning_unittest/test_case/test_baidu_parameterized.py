import unittest
from time import sleep
from selenium import webdriver
from parameterized import parameterized


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
        sleep(2)

    # 通过Parameterized实现参数化
    """
    在@parameterized.expand中，每个元组都可以被认为是一条测试用例，元组中的数据为该条测试用例变化的值
    在test_search()中，name对应元组中第一列数据，即case1、case2、case3，用来定义测试用例名称；
    search_key对应元组中第二列数据，即selenium、unittest、parameterized，用来定义搜索的关键词
    """
    @parameterized.expand([
        ("case1", "selenium"),
        ("case2", "unittest"),
        ("case3", "parameterized")
    ])
    def test_search(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)