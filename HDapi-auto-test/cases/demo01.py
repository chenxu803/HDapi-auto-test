
import requests
import unittest
import utils
from testcase_py.common import read_conf, read_excel
import xml.etree.ElementTree as ET

class Api_getregion(unittest.TestCase):
    '''测试获取省份ID'''
    def test_api(self):
        flag=True
        url=read_conf.get('getRegionProvince_get','get_url')
        res = requests.get(url=url)
        #print(res.text)
        pre_list=read_excel.readExcel(utils.BASE_DIR+'\\testcase_excel\\api_testcase.xlsx').get_data('getregion',0,1)
        code_list=[]
        #调用parse()方法，返回解析树,加载的为文件，用fromstring的方法加载指定的字符串
        tree = ET.fromstring(res.text)
        print("tree",tree)
        #root = tree.getroot()
        tag_string=tree.findall("./string")
        print(tag_string)
        #print(tree[3].text)
        n=0
        for n in range(0, 100):
            try:
                code_list.append(tree[n].text)
                #print(code_list)
                n = n+1
            except:
                break
        for i in code_list:
            if i in pre_list:
                pass
            else:
                print('异常返回值',i)
                flag=False
        assert flag==True
        print('发送省份ID接口测试通过')





        # for string in tag_string:
        #     print('i为', string)
        #     get_string= string.text
        #     code_list.append(get_string)
        #     print(code_list)





Api_getregion().test_api()