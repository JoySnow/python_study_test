

https://my.oschina.net/lionets/blog/268704
https://docs.python.org/2.7/library/unittest.html

unittest 与 doctest 一样也是 Python 发行版自带的包。
PyUnit 是 unittest 的曾用名.


Module doctest:
	Another test-support module with a very different flavor.
Nose and py.test:
	Third-party unittest frameworks with a lighter-weight syntax for writing tests. For example, assert func(10) == 42.


### 使用 unittest 的标准流程为：

从 unittest.TestCase 派生一个子类
在类中定义各种以 “test_” 打头的方法
通过 unittest.main() 函数来启动测试


### 
当类里面定义了 setUp()
方法的时候，测试程序会在执行每条测试项前先调用此方法；同样地，在全部测试项执行完毕后，tearDown()
方法也会被调用。

see `unittest_usecase_1.py`
run by `python unittest_usecase_1.py`



### 
那如果我们想全程只调用一次 setUp/tearDown 该怎么办呢？
就是用 setUpClass() 和
tearDownClass() 类方法啦。注意使用这两个方法的时候一定要用 @classmethod
装饰器装饰起来：


see `unittest_usecase_2.py`
run by `python unittest_usecase_2.py`


### 
再往上一级，我们希望在整个文件级别上只调用一次 setUp/tearDown，这时候就要用
setUpModule() 和 tearDownModule() 这两个函数了，注意是函数，与 TestCase
类同级：


see `unittest_usecase_3.py`
run by `python unittest_usecase_3.py`


### 
Note: tearDown() 仅在 setUp() 成功执行的情况下才会执行，并一定会被执行。



