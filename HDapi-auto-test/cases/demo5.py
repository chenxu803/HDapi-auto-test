

import requests




host ='http://ws.webxml.com.cn'
endpoint='/WebServices/WeatherWS.asmx/getWeather'
url="".join([host,endpoint])
#form_data
#1，普通上传
files={'files':open('test.txt','rb')}
#2，通过文件上传字符串(自定义)
files={'files':('test.txt','send sssss')}
#3自定义文件名，文件类型，以及请求头，格式如下(请求文件名称，文件路径，文件类型，文件请求头)
files={'files':open('巧吧软件测试.png','rb')}  #这种为默认格式
files={'files':('巧吧软件测试.png',open('巧吧软件测试.png','rb'),'image/jpg')}
#传送多个文件
files=[('field1',('test.txt',open('test.txt','rb'))),('field2',('巧吧软件测试.png',open('巧吧软件测试.png','rb'),'image/png'))]


res= requests.post(url,files=files)

#流式上传

with open('test.txt') as f:
    r= requests.post(url,data=f)


r= requests.post(url)
#打印出是一个jar包
print(r.cookies)
#把jar包转化成字典
dic=requests.utils.dict_from_cookiejar(r.cookies)
print(dic)
#另一种方式
{a.name:a.value  for a in r.cookies}


#发送cookies
cookies={'cookie-name':'qiaoba'}
result=requests.get(url,cookies=cookies)
print(result.text)

#复杂的写法
s = requests.Session()
c = requests.cookies.RequestsCookieJar()
c.set('cookie-name','cookie-value',path='/',domain='.test.com')
s.cookies.update(c)
print(s.cookies)


session=requests.Session() #初始化一个session对象
session.get(url) #cookies的信息存在了session中
rl=session.get(url)
print(rl.text)

#添加headers中信息
header1={'test1':'aa'}
header2={'test2':'bb'}
session1=requests.Session()
session1.headers.update(header1)#已经存在服务器中的信息
r2=session1.get('http://httpbin.org/headers',headers=header2) #发送新的headers信息
r3=session1.get('http://httpbin.org/headers',headers=header2)
print(r3.text)
#删除headers中的信息
session1.headers['test1']=None  #删除会话里面的信息，赋值None即可
r3=session1.get('http://httpbin.org/headers',headers=header2)
print(r3.text)






