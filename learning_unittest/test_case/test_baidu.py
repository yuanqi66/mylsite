import unittest
from time import sleep
from selenium import webdriver


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

    def test_search_key_selenium(self):
        """搜索关键字：selenium"""
        search_key = "selenium"
        self.baidu_search(search_key)
        title = self.driver.title
        self.assertEqual(title, search_key + "_百度搜索")

    def test_search_key_unittest(self):
        """搜索关键字：unittest"""
        search_key = "unittest"
        self.baidu_search(search_key)
        title = self.driver.title
        self.assertEqual(title, search_key + "_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)