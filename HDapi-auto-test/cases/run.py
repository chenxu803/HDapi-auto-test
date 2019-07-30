
import unittest

import HTMLTestRunner
import unittest
from time import strftime, localtime, time
from cases.demo01 import Api_getregion
from cases.demo2 import getSupportCityDataset

suite=unittest.TestSuite()

suite.addTest(Api_getregion("test_api"))
suite.addTest(getSupportCityDataset("test_data"))

now = strftime("%Y-%m-%d-%H_%M_%S", localtime(time()))

filepath='D:\\HDapi-auto-test\\report\\'+now+"_接口测试报告_.html"

fp=open(filepath,"wb")


runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    verbosity=2,
    title=u"接口自动化测试结果",
    description=u"测试结果详情")

runner.run(suite)

fp.close()



