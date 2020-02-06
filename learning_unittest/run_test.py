import unittest

# 定义测试用例的目录为当前目录中得test_case/目录
test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(suits)