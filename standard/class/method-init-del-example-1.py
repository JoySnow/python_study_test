# encoding:utf8  
  
class NewClass():  
    # 为了方便，这里进行先行声明，但是实际应用中一般没必要  
    #   
    # 共有，私有变量，通过两个下划线区分  
    var_public = 0 # 类型上的共有变量  
    __var_private = 2 # 类型上的私有, 通过_NewClass__var_private 还可以访问  
  
    # python 中的特殊：类变量和成员变量，无法通过语法区分，只有使用时区分  
    var_test_class = 0 # 用于类变量, 类和它的实例都可以访问，类似c++ static, 但又不一样.  
    # 当一个类的对象被构造时，会将当前类变量拷贝一份给这个对象，当前类变量的值是多少，这个对象拷贝得到的类变量的值就是多少；  
    # 通过对象来修改类变量，并不会影响其他对象的类变量的值，因为大家都有各自的副本，更不会影响类本身所拥有的那个类变量的值；  
    # 只有类自己才能改变类本身拥有的类变量的值。  
    var_test_self = 0 # 用于成员变量, 只有类的实例可以访问, 类似c++ 中一般成员变量  
  
    def __init__(self,name):  
        self.name = name  
        self.var_test_self += 1  
        NewClass.var_test_class += 1  
        pass  
    def __del__(self):  
        self.var_test_self -= 1  
        NewClass.var_test_class -= 1  
        pass  
  
    # 一般成员函数  
    def func0(self):  
        pass  
  
    # 静态成员函数，参数可以为空  
    @staticmethod  
    def func1():
        NewClass.var_test_self += 1  
        NewClass.var_test_class += 1  
        print "a5: ", a5
        print "a5",a5.var_test_self, a5.var_test_class, a5.__class__.var_test_class, NewClass.var_test_class, NewClass.var_test_self
        pass  
  
    # 类函数，参数为一个类  
    @classmethod  
    def func2(cls):  
        NewClass.var_test_self += 1  
        NewClass.var_test_class += 1  
        print "a5: ", a5
        print "a5",a5.var_test_self, a5.var_test_class, a5.__class__.var_test_class, NewClass.var_test_class, NewClass.var_test_self
        cls.var_test_self += 1  
        cls.var_test_class += 1  
        print "cls: ", cls
        print "cls: ", cls.var_test_self, cls.var_test_class
        pass  
  
if __name__ == '__main__':  
  
    a1 = NewClass("Hello")
    print "a1: ", a1
    print "NewClass: ", NewClass
    print "type(a1): ", type(a1)
    print "type(NewClass): ", type(NewClass)
    print "a1:", a1.var_test_self, a1.var_test_class, NewClass.var_test_class, NewClass.var_test_self  
    a2 = NewClass("World")  
    print "a2: ", a2
    print "a2:", a2.var_test_self, a2.var_test_class, NewClass.var_test_class, NewClass.var_test_self  
    a3 = NewClass("nihao")  
    print "a3: ", a3
    print "a3:", a3.var_test_self, a3.var_test_class, NewClass.var_test_class, NewClass.var_test_self  
    # change class var  
    a3.var_test_self += 1  
    a3.var_test_class += 10  
    NewClass.var_test_class += 100 # ?? no error  
    NewClass.var_test_self += 1000 # ?? no error  
    print "a3:", a3.var_test_self, a3.var_test_class, NewClass.var_test_class, NewClass.var_test_self  
  
    a4 = NewClass("vartest")  
    print "a4: ", a4
    print "a4",a4.var_test_self, a4.var_test_class, a4.__class__.var_test_class, NewClass.var_test_class, NewClass.var_test_self # a4.__class__ 等价于 NewClass   
  
    ''''' 
    a1:  <__main__.NewClass instance at 0x7f9c3b61e950>
    NewClass:  __main__.NewClass
    type(a1):  <type 'instance'>
    type(NewClass):  <type 'classobj'>
    a1: 1 1 1 0
    a2:  <__main__.NewClass instance at 0x7f9c3b61e998>
    a2: 1 2 2 0
    a3:  <__main__.NewClass instance at 0x7f9c3b61e9e0>
    a3: 1 3 3 0
    a3: 2 13 103 1000
    a4:  <__main__.NewClass instance at 0x7f9c3b61ea28>
    a4 1001 104 104 104 1000
    '''  
    # 说明，类和它的实例 访问成员函数完全是分开的，只有在构造时才有联系  
  
    a5 = NewClass("test") # # Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x01A014B8>> 
    print "a5: ", a5
    print "a5",a5.var_test_self, a5.var_test_class, a5.__class__.var_test_class, NewClass.var_test_class, NewClass.var_test_self # 
    a5.func0()  
    a5.func1()  
    a5.func2()   
#    NewClass.func0() #TypeError: unbound method func0() must be called with NewClass instance as first argument (got nothing instead)  
    NewClass.func1()  
    NewClass.func2()  
    '''
a5:  <__main__.NewClass instance at 0x7f9c3b61ea70>
a5 1001 105 105 105 1000
a5:  <__main__.NewClass instance at 0x7f9c3b61ea70>
a5 1001 106 106 106 1001
a5:  <__main__.NewClass instance at 0x7f9c3b61ea70>
a5 1001 107 107 107 1002
cls:  __main__.NewClass
cls:  1003 108
a5:  <__main__.NewClass instance at 0x7f9c3b61ea70>
a5 1001 109 109 109 1004
a5:  <__main__.NewClass instance at 0x7f9c3b61ea70>
a5 1001 110 110 110 1005
cls:  __main__.NewClass
cls:  1006 111
Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x7f9c3b61e950>> ignored
Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x7f9c3b61e9e0>> ignored
Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x7f9c3b61e998>> ignored
Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x7f9c3b61ea70>> ignored
Exception AttributeError: "'NoneType' object has no attribute 'var_test_class'" in <bound method NewClass.__del__ of <__main__.NewClass instance at 0x7f9c3b61ea28>> ignored
    '''
    # classmethod 与 staticmethod 差异主要在继承等场景时需要明确区分，同时类函数会额外获取自身的类对象，而不是实例对象  
