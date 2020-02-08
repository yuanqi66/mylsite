"""
数据驱动
"""
import csv
import codecs
import unittest
from time import sleep
from itertools import islice
from selenium import webdriver


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.base_url = "https://www.baidu.com"
        cls.test_data = []
        # 将文件中的数据存储到test_data数组中
        with codecs.open('baidu_data.csv', 'r', 'utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                cls.test_data.append(line)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        """搜索关键字"""
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(3)


    """
    def test_search(self):
        with codecs.open('baidu_data.csv', 'r', 'utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data, 1, None):
                search_key = line[1]
                self.baidu_search(search_key)
    """

    def test_search_selenium(self):
        """搜索关键字：selenium"""
        self.baidu_search(self.test_data[0][1])
        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_search_unittest(self):
        """搜索关键字：unittest"""
        self.baidu_search(self.test_data[1][1])
        title = self.driver.title
        self.assertEqual(title, "unittest_百度搜索")

    def test_search_parameterized(self):
        """搜索关键字：parameterized"""
        self.baidu_search(self.test_data[2][1])
        title = self.driver.title
        self.assertEqual(title, "parameterized_百度搜索")

if __name__ == '__main__':
    unittest.main(verbosity=2)