#!/usr/bin/env python
#-*-coding: utf-8-*-
#@Time  : 2019/7/24 11:02
#@Author : Chenxu
#@Site :  
#@File  :  ddt_train1.py
#@Software :
import time

import time
import unittest
import xml.etree.ElementTree as ET
from ddt import ddt,data,unpack

import utils
from testcase_py.common import conf
from testcase_py.common.HttpService import MyHTTP

excel_url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString'
dir=utils.BASE_DIR+"\\testcase_excel\\api_data.xlsx"
alldata=conf.get_data(dir,'dataall')[7:10]

#print(alldata)
ddt_data=conf.get_data('D:\\HDapi-auto-test\\testcase_excel\\api_data.xlsx','ddt_data')[7:10]
#print(ddt_data)


#如果写上import ddt，就不用@ddt
@ddt
class DDT_test(unittest.TestCase):
    #n = 0
    def setUp(self):
        self.url= excel_url

        # return self.url

    @data(*ddt_data)
    @unpack
    def test_1(self, *ddt_data):  #传入ddt_data
        # n = 0


            alldata = eval(ddt_data[3])

            res = MyHTTP('get').sendhttp(self.url, **alldata)
            print(res.text)
            try:
                tree = ET.fromstring(res.text)
                self.assertEqual(200, res.status_code, "服务器异常，请检查服务器")
                self.assertEqual(ddt_data[0], tree[0].text, ddt_data[2])
                print(ddt_data[1])


                time.sleep(10)
            except Exception as e:
                self.assertIn(ddt_data[0], res.text, e)

                #self.n = self.n + 1
                print(ddt_data[1])
                time.sleep(10)
            time.sleep(15)


