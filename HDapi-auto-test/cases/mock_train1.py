import unittest

import mock

from cases import modular

#函数使用mock server
from cases.modular import Count


class test_def(unittest.TestCase):
    def test_add3(self):
        modular.add3=mock.Mock(return_value=40)
        modular.add3 = mock.Mock()
        #设置属性为mock
        modular.add3.configure_mock(side_effect=modular.add4)

        res=modular.add3(1,2)
        self.assertEqual(6,res)
    @mock.patch('modular.add4')
    def test_add4(self,mock_add4):
        mock_add4.return_value=modular.add3(5,6)
        mock_add4.side_effect=modular.add3
        #和老师不一样
        result=mock_add4(5,2)
        res=modular.add4(5,2)
        print("老师的方法",res)  # res =10
        self.assertEqual(7,result)
    @mock.patch.object(modular.Count,"add2")
    @mock.patch('modular.add4')
    def test_add3_add4(self,mock_add4,mock_add2): #注意这个传参的顺序，和装饰器里面是反着的

        mock_add4.return_value=modular.add3(1,1)
        mock_add2.side_effect=Count().add1
        result1=Count().add2(10,10)
        #这步和老师的不一样***********************************
        result2=mock_add4(10,20)
        mock_add4.assert_called_once_with(10,20)
        Count().add2.assert_called_with(10,10)
        self.assertEqual(20,result1)
        self.assertEqual(2,result2)
        print('mock测试通过，就是使用的方法不同')

