



import requests

import utils
from testcase_py.common import read_conf
from testcase_py.common.read_excel import readExcel
import xml.etree.ElementTree as ET
from unittest import TestCase


class getSupportCityDataset_soap():
    """soap获取城市ID"""
    def test_citycode(self, url, data, headers):
        flag=True
        res=requests.post(url,data,headers)
        tree=ET.fromstring(res.text)
        root=tree.ElementTree.getroot()
        tag = root.findall('string')
        citydata=[]
        for m in tag:
            citydata.append(m)
            print('m:',m)
        citycode = readExcel(utils.BASE_DIR + '\\testcase_excel\\api_testcase.xlsx').get_data('getregion', 1, 1)
        citycode_list=[]
        for i in range(0,100):
            try:
                citycode_list.append(tree[i])
                print(citycode_list)
                print(citycode)
                TestCase.assertEqual(citycode_list[i],citycode[i],'接口测试有问题的值，第一个为响应值，第二个值为预期值')

            except:
                continue
                flag=False
        assert flag==True
        print('接口测试通过')



url=read_conf.get('getSupportCityDataset_soap','soap_url')
data=read_conf.get('getSupportCityDataset_soap','soap_data')
headers=read_conf.get('getSupportCityDataset_soap','soap_headers')

getSupportCityDataset_soap().test_citycode(url,data,headers)

