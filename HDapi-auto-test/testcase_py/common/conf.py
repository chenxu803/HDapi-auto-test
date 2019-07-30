#!/usr/bin/env python
#-*-coding: utf-8-*-
#@Time  : 2019/7/19 12:57
#@Author : Chenxu
#@Site :  
#@File  :  conf.py
#@Software :
import configparser

import utils
#from common.read_excel import readExcel

#host 从ini文件调用，endpoint都是从Excel中调用,此方法不好，在于一个链接就是一个接口，不需要测试多个链接的情况
# def get_url(session,key,excel,sheet_name,col,row):
#     conf=configparser.ConfigParser()
#     conf.read(utils.BASE_DIR+'\\config\\ConfigParser.ini',encoding='utf-8')
#     host=conf.get(session,key)
#     #print(host)
#     excel_path=utils.BASE_DIR+'\\data\\'+excel
#     EndPoint=readExcel(excel_path).get_data(sheet_name,col,row)
#     #print(EndPoint)
#     url_list=[]
#     for endpoint in EndPoint:
#         url="".join([host,endpoint])
#         #print(url_list)
#         url_list.append(url)
#     return url_list
from testcase_py.common.excel_data import XLdata


def get_url(session1,key1,session2,key2):
    conf = configparser.ConfigParser()
    conf.read(utils.BASE_DIR+'\\config\\ConfigParser.ini',encoding='utf-8')
    host=conf.get(session1,key1)
    endpoint=conf.get(session2,key2)
    url = "".join([host, endpoint])
    return url


#print(get_url('getRegionProvince_get','host','getRegionProvince_get','get_url'))

#数据库连接串
sql_conn_dict = {
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "db":"chenxu",
    "charset":"utf8",

}


def get_data(filename,sheetname):
    data=XLdata(filename).get_sheetinfo_by_name(sheetname)
    return data










#老师用的方法
def url():
    url ='http://httpbin.org/'
    return url

#调用函数
# excel_path=utils.BASE_DIR+'\\data\\api_data.xlsx'
#print(get_url('host','url_getregioncode','api_data.xlsx','endpoint',1,1))