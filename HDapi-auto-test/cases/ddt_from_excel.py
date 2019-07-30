#!/usr/bin/env python
#-*-coding: utf-8-*-
#@Time  : 2019/7/23 15:15
#@Author : Chenxu
#@Site :  
#@File  :  ddt_from_excel.py

import time
import unittest
import xml.etree.ElementTree as ET
import requests
from ddt import ddt,data,unpack
from common import conf
from common.HttpService import MyHTTP

excel_url=conf.get_url('api_data.xlsx','host',0,1,'dataall',1,2)
alldata=conf.get_data('api_data.xlsx','dataall')[0:5]

#print(alldata)
ddt_data=conf.get_data('api_data.xlsx','ddt_data')[0:5]
#print(ddt_data)


#如果写上import ddt，就不用@ddt
@ddt
class DDT_test(unittest.TestCase):
    n = 0
    def setUp(self):
        self.url= excel_url

        # return self.url

    @data(*ddt_data)
    @unpack
    def test_1(self, expected, result, failinfo):
        # n = 0
        for i in range(0,len(ddt_data)+1):
            alldata1 = eval(alldata[i][3])
            #print(self.n)
            res = MyHTTP('get').sendhttp(self.url, **alldata1)
            print(res.text)
            try:
                tree = ET.fromstring(res.text)
                self.assertEqual(200, res.status_code, "服务器异常，请检查服务器")
                self.assertEqual(expected, tree[0].text, failinfo)
                print(result)
               #self.n = self.n + 1
                time.sleep(10)
            except Exception as e:
                self.assertIn(expected, res.text, e)
                #self.n = self.n + 1
                print(result)
                time.sleep(10)
            time.sleep(15)

if __name__=="__main__":
    unittest.main()
