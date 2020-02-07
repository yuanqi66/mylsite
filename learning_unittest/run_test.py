import unittest
from HTMLTestRunner import HTMLTestRunner

# 定义测试用例的目录为当前目录中得test_case/目录
test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
	# 生成HTML格式的报告
	# 使用open方法打开result.html文件（无该文件会自动创建）
	fp = open('./test_report/result.html', 'wb')
	"""
	stream：指定生成HTML测试报告的文件，必填
	verbosity：指定日志级别，012
	title：指定测试用例的标题，默认为None
	description：指定测试用例的描述，默认为None
	"""
	runner = HTMLTestRunner(stream=fp,
							verbosity=2,
							title="百度搜索测试报告",
							description="运行环境：Windows 10，Firefox浏览器"
							)
	runner.run(suits, rerun=0, save_last_run=False)
	fp.close()