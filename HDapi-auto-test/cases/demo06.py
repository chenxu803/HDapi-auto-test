from testcase_py.common.HttpService import MyHTTP
from testcase_py.common.conf import get_url


class Api_test():
     def setUp(self):
         url=get_url('getSupportCityString_get','host','getSupportCityString_get','get_url')
         #print(url)
         return url


     def test_get(self):
         url=self.setUp()
         params={'theRegionCode': 3113}
         alldata={'params': params}
         print(alldata)
         res = MyHTTP('get').sendhttp(url,**alldata)
         print(res.text)

Api_test().test_get()

class Api_test1():
    def setUp(self):
        url = get_url('getweather_post', 'host', 'getweather_post', 'endpoint')
        print(url)
        return url
    def test_post(self):
        url =self.setUp()

        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        data = {'theCityCode': 120, 'theUserID': ''}
        alldata={'data': data, 'headers': headers}
        print(alldata)
        res=MyHTTP('post').sendhttp(url, **alldata)

        print(res.text)
Api_test1().test_post()

