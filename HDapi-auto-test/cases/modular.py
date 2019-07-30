import mock


class Count():
    def add1(self,a,b):
        return a+b
    def add2(self,a,b):
        return a+b+3

def add3(a,b):
    return a+b

def add4(a,b):
    return a+b+3

class Foo1():
    def plus1(self,a,b):
        return a+b
    def plus2(self,a,b):
        return a+b+1

class Foo2():
    def plus3(self,a,b):
        return a+b+2
    def plus4(self,a,b):
        return a+b+3

class Foo3():
    def plus5(self,a,b):
        return a + b+4

mockFoo1=mock.Mock(spec=Foo1,return_value=Foo2())
mockFoo2=mock.Mock(spec=Foo2,return_value=Foo3())
print(mockFoo1().plus3(2,2))
print(mockFoo2().plus5(2,2))
mockFoo1.attach_mock(mockFoo2,'FooBar')
print(mockFoo1.FooBar().plus5(2,2))

print(mockFoo1.method_calls)
print(mockFoo1.mock_calls)
print(mockFoo2.method_calls)
print(mockFoo2.mock_calls)
print(mockFoo1.call_args_list)

mockFoo3=mock.Mock(spec=Foo3,return_value=Foo1())
#原来的属性被擦除
mockFoo3.mock_add_spec(Foo1)
print(mockFoo3().plus2(3,3))


