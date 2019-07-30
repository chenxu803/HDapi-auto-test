#!/usr/bin/env python
#-*-coding: utf-8-*-
#@Time  : 2019/7/19 15:49
#@Author : Chenxu
#@Site :  
#@File  :  HttpService.py
#@Software :



# python 2.x 没有父类，要写上object，Python3.0 可以写，可以不写
import requests


class MyHTTP(object):
    def __init__(self,method):
        self.method=method
  #封装所有的请求  ，alldata传入字典类型
    def sendhttp(self,url,**alldata):
        if self.method =='get':
            params=alldata.get('params')
            headers=alldata.get('headers')
            try:
                #result=requests.get(url,params=params,headers=headers,timeout=3)
                result = requests.get(url, params=params, headers=headers)
                return result
            except Exception as e:
                print('GET错误，%s'%e)
        if self.method=='post':
            params = alldata.get('params')
            headers = alldata.get('headers')
            data= alldata.get('data')
            json=alldata.get('json')
            files=alldata.get('files')
            try:

                #result=requests.post(url,params=params,headers=headers,data=data,json=json,files=files,timeout=3)
                result = requests.post(url, params=params, headers=headers, data=data, json=json, files=files)
                return result
            except Exception as e:
                print('POST错误，%s'%e)
        if self.method=='delete':
            params = alldata.get('params')
            headers = alldata.get('headers')
            data = alldata.get('data')
            json = alldata.get('json')
            files = alldata.get('files')
            try:

                #result=requests.post(url,params=params,headers=headers,data=data,json=json,files=files,timeout=3)
                result = requests.delete(url, params=params, headers=headers, data=data, json=json, files=files)
                return result
            except Exception as e:
                print('delete错误，%s' %e)


#调试
# url="http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather"
# headers = {'Content-Type': "application/x-www-form-urlencoded"}
# params = {'theCityCode': 120, 'theUserID': ''}
# alldata = {'params': params, 'headers': headers}
# print(alldata)
# print(MyHTTP('post').sendhttp(url, **alldata))

