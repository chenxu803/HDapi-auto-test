import unittest

import mock
import modular

from cases.modular import Count

#类里面的方法使用mock server
class test_Count(unittest.TestCase):
    def test_add1(self):
        count=modular.Count()
        count.add1=mock.Mock(return_value=10)
        count.add1=mock.Mock(side_effect=count.add2)
        res=count.add1(3,3)
        self.assertEqual(9,res)
        #装饰器方法
    @mock.patch.object(modular.Count,"add2")
    def test_add2(self,mock_add2):
        count=modular.Count()
        mock_add2.return_value=20
        mock_add2.side_effect=count.add1
        result=modular.Count().add2( 1,2 )
        count.add2.assert_called_once_with(1,2)
        count.add2(0,1)
        count.add2(1,2)
        count.add2.assert_called_with(1,2)
        count.add2.assert_any_call(1,2)
        param1=mock.call(1,2)
        param2=mock.call(0,1)
        count.add2.assert_has_calls([param1,param2],any_order=False)
        count.add2.assert_has_calls([param2,param1],any_order=True)
        print(count.add2.called)
        print(count.add2.call_count)
        print(count.add2.call_args)
        print(count.add2.call_args_list)
        print(count.add2.method_calls)
        print(count.add2.mock_calls)
        count.add2.reset_mock()
        print(count.add2.called)
        print(count.add2.call_count)
        print(count.add2.call_args)
        print(count.add2.call_args_list)
        print(count.add2.method_calls)
        print(count.add2.mock_calls)




        self.assertEqual(3,result)
        print('测试通过')






