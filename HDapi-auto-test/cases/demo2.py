import requests

import utils
from testcase_py.common import read_conf
from testcase_py.common.read_excel import readExcel
import xml.etree.ElementTree as ET
import unittest
from xml.etree.ElementTree import fromstring, ElementTree



class getSupportCityDataset(unittest.TestCase):
    """获取城市ID"""
    def test_data(self):
        flag= True
        citycode= readExcel(utils.BASE_DIR+'\\testcase_excel\\api_testcase.xlsx').get_data('getregion',1,1)


        get_url = 'http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getSupportCityString?theRegionCode=3113'
        res= requests.get(url=get_url)
        print(res.text)
        tree=ElementTree(fromstring(res.text))
        root=tree.getroot()
        print('root为：',root)
        tag= root.findall('.//string')
        code_list = []
        for m in tag:
            code_list.append(m.text)

        print(code_list)
        citycode_list=[]
        for n in range(0,100):
            try:
                citycode_list.append(tree[n])
                if citycode_list[n]==citycode[n]:
                    pass
                else:
                    print('返回数据为：',citycode_list[n],'预期的值为：',citycode[n])
                    flag=False
            except:
                break
        assert flag==True
        print('取城市ID接口测试成功')









getSupportCityDataset().test_data()