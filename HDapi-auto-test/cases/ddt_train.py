#!/usr/bin/env python
#-*-coding: utf-8-*-
#@Time  : 2019/7/23 12:10
#@Author : Chenxu
#@Site :  
#@File  :  ddt_train.py
#@Software :
import time
import unittest
import xml.etree.ElementTree as ET

import requests
from ddt import ddt,data,unpack
from common import conf
from common.HttpService import MyHTTP

excel_url=conf.get_url('api_data.xlsx','host',0,1,'dataall',1,2)
#如果写上import ddt，就不用@ddt
@ddt
class DDT_test(unittest.TestCase):
    def setUp(self):
        self.url= excel_url
        return self.url
    #,多参数时，data() 是一个大元祖，元祖里面可以是列表，可以是元祖，也可以是字典
    # @data([{"theCityCode":120,"theUserID":""},200,'黑龙江 哈尔滨'],[{"theCityCode":88,"theUserID":""},200,'黑龙江 绥化'])
    @data(({"theCityCode":120,"theUserID":""},200,'黑龙江 哈尔滨'),({"theCityCode":88,"theUserID":""},200,'黑龙江 绥化'))
    @unpack
    def test_1(self,params,result,result1):
        res=requests.get(self.url,params)
        tree = ET.fromstring(res.text)
        self.assertEqual(result,res.status_code,"服务器不正常")
        self.assertEqual(result1,tree[0].text,"城市ID和城市名称对应不上")
        print('\n天气预报接口测试成功')
        time.sleep(5)
    #一个参数的时候
    @data(200,300,400)
    def test_2(self,result):
        res = requests.get(self.url, params={"theCityCode":120,"theUserID":""})
        tree = ET.fromstring(res.text)
        self.assertEqual(result, res.status_code, "服务器不正常")
        print("天气预报接口测试成功")
        time.sleep(3)

    def tearDown(self):
        pass

#ddt运行报错AttributeError: type object 'DDT_test' has no attribute 'test_2'
#原因：运行的时候光标的位置放在 test_login 方法里面了，加了ddt后，运行时要先识别装饰的类，将光标放在某一个方法后面的话，测试用例只会执行当前的方法，ddt识别不到类，就会报错，
# 将光标放到外面，则运行通过，或者加main方法，再运行，也不会报错
#
# 其他可能原因，setUp 或者 tearDown 拼写错误也可能报此错误