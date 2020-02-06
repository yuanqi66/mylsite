import unittest
from time import sleep
from selenium import webdriver


class TestBaiDu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()

    def test_search_key_selenium(self):
        self.baidu_search("selenium")
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_search_key_unittest(self):
        self.baidu_search("unittest")
        sleep(2)
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()