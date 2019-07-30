import requests


class SendHttp():
    def __init__(self,url,data,method):
        self.url=url
        self.data=data
        self.method=method
        #self.headers=headers
    def Sendmethod(self):
        if self.method=='post':
            result=requests.post(self.url,self.data)
        else:
            result=requests.get(self.url,self.data)

        return result
url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getWeather'
data={'theCityCode':'3408','theUserID':""}
method='get'


getweather=SendHttp(url,data,method)
res=getweather.Sendmethod()
print(res.text)

print(res.url)
print(res.request.url)
