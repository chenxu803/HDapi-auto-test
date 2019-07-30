import HTMLTestRunner
import unittest
from time import strftime, localtime, time



all_cases=unittest.defaultTestLoader.discover('D:/HDapi-auto-test/cases','demo*.py')
suite=unittest.TestSuite()

for case in all_cases:
    suite.addTest(case)
now = strftime("%Y-%m-%d-%H_%M_%S", localtime(time()))
filepath='D:\\HDapi-auto-test\\report\\'+now+'_接口测试报告_.html'
fp=open(filepath,'wb')

runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'接口测试报告',description=u"测试详情",verbosity=2)
runner.run(suite)
fp.close()