

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [Diff (doctest, unittest, nose, pytest)](#diff-doctest-unittest-nose-pytest)
	* [doctest](#doctest)
		* [Use-case-1:](#use-case-1)
		* [Use-case-2:](#use-case-2)
		* [Test Output:](#test-output)
	* [unittest](#unittest)
		* [使用 unittest 的标准流程为：](#使用-unittest-的标准流程为)
		* [类里 每个test_函数都执行一次 setUp()](#类里-每个test_函数都执行一次-setup)
		* [类里 多个test_函数， 但只执行一次 setUp()](#类里-多个test_函数-但只执行一次-setup)
		* [在整个文件级别上只调用一次 setUp/tearDown](#在整个文件级别上只调用一次-setupteardown)
		* [Note](#note)
	* [nose](#nose)
		* [usecase 四种功能](#usecase-四种功能)
		* [Output](#output)
		* [nose 的 discovery 规则为：](#nose-的-discovery-规则为)
		* [调用 discovery 的语法](#调用-discovery-的语法)
	* [pytest](#pytest)
		* [pytest 的 setup/teardown 使用方式](#pytest-的-setupteardown-使用方式)
		* [Output](#output-1)
	* [pytest 与 nose 二选一](#pytest-与-nose-二选一)

<!-- /code_chunk_output -->


# Diff (doctest, unittest, nose, pytest)

Module doctest:
	Python 发行版自带的包. Another test-support module with a very different flavor.

Module unittest:
	Python 发行版自带的包, Unit testing framework

Nose and py.test:
	Third-party unittest frameworks with a lighter-weight syntax for writing tests. For example, assert func(10) == 42.


## doctest

https://my.oschina.net/lionets/blog/268542


### Use-case-1:

put the doctest lines as docsting into code, see `doctest_usecase_1.py`.

```python
def multiply(a,b):
    """
    >>> multiply(2,3)
    6
    >>> multiply('baka~',3)
    'baka~baka~baka~'
    """
    return a*b

if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose=True)
```
Run with `$ python doctest_usecase_1.py`.


### Use-case-2:

如果不想（或不能）把测试用例写进源代码里，则还可以使用一个独立的文本文件来保存测试用例。

See `doctest_example.txt`:

```
>>> from doctest_usecase_1 import multiply
>>> multiply(2,3)
6
>>> multiply('baka~',3)
'baka~baka~baka~'

```

Run with: In command line, call:
```
python -m doctest -v doctest_example.txt
```


### Test Output:
```
Trying:
	multiply(2,3)
Expecting:
	6
ok
Trying:
	multiply('baka~',3)
Expecting:
	'baka~baka~baka~'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.multiply
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```


## unittest

https://my.oschina.net/lionets/blog/268704
https://docs.python.org/2.7/library/unittest.html

PyUnit 是 unittest 的曾用名.

### 使用 unittest 的标准流程为：

从 unittest.TestCase 派生一个子类,
在类中定义各种以 “test_” 打头的方法,
通过 unittest.main() 函数来启动测试.


### 类里 每个test_函数都执行一次 setUp()
当类里面定义了 setUp()方法的时候，测试程序会在执行每条测试项前先调用此方法；
同样地，在全部测试项执行完毕后，tearDown()方法也会被调用。

see `unittest_usecase_1.py`
run by `python unittest_usecase_1.py`

```python
import unittest
from doctest_usecase_1 import multiply

class TestUM(unittest.TestCase):
	def setUp(self):
                print "--- DEBUG: Setup"

	def test_number_3_4(self):
                print "test_number_3_4"
		self.assertEqual(multiply(3,4),12)

	def test_string_a_3(self):
                print "test_string_a_3"
		self.assertEqual(multiply('a',3),'aaa')

if __name__ == '__main__':
	unittest.main()
```



### 类里 多个test_函数， 但只执行一次 setUp()
那如果我们想全程只调用一次 setUp/tearDown 该怎么办呢？
就是用 `setUpClass()` 和 `tearDownClass()` 类方法啦。注意使用这两个方法的时候一定要用 @classmethod 装饰器装饰起来：


see `unittest_usecase_2.py`
run by `python unittest_usecase_2.py`

```python
import unittest
from doctest_usecase_1 import multiply

class simple_test(unittest.TestCase):

	@classmethod
	def setUpClass(self):
                print "--- DEBUG: Setup"

	def test_number_3_4(self):
                print "test_number_3_4"
		self.assertEqual(multiply(3,4),12)

	def test_string_a_3(self):
                print "test_string_a_3"
		self.assertEqual(multiply('a',3),'aaa')


if __name__ == '__main__':
	unittest.main()
```

### 在整个文件级别上只调用一次 setUp/tearDown
要用 setUpModule() 和 tearDownModule() 这两个`函数`了，注意是函数，与 TestCase 类同级：


see `unittest_usecase_3.py`
run by `python unittest_usecase_3.py`

```python
import unittest
from doctest_usecase_1 import multiply

def setUpModule():
        print "--- DEBUG: Setup"


class simple_test(unittest.TestCase):

	def test_number_3_4(self):
                print "test_number_3_4"
		self.assertEqual(multiply(3,4),12)

	def test_string_a_3(self):
                print "test_string_a_3"


class simple_test2(unittest.TestCase):

	def test_number(self):
                print "test_number"
		self.assertEqual(multiply(3,4),12)


if __name__ == '__main__':
	unittest.main()
```

### Note
tearDown() 仅在 setUp() 成功执行的情况下才会执行，并`一定`会被执行。


## nose

https://my.oschina.net/lionets/blog/269174

Third-party module.
nose 的口号就是：
    扩展 unittest，nose 让测试更简单。

另外非常棒的一点是，nosetests 兼容对 doctest 和 unittest
测试脚本的解析运行。


扩展自 unittest，
nose 也支持类似于 setUp() setUpClass() setUpModule() 的测试环境创建方式，只不过函数命名规则最好改一改，我们可以使用更符合 Python
规范的命名规则。
另外因为 nose支持上例中所展示的函数式测试用例，所以还有一种为单个函数创建运行环境的装饰器可用。

### usecase 四种功能

See `nose_usecase_1.py`
run with `nosetests -v -s nose_usecase_1.py`

```python
# -*- coding: UTF-8

from nose import with_setup

from doctest_usecase_1 import multiply

def setup_module(module):    # <-- module/file level setup
	print('setup_module 函数执行于一切开始之前')

def setup_deco():     # <-- function level setup
	print('setup_deco 将用于 with_setup')

def teardown_deco():  # <-- function level teardown
	print('teardown_deco 也将用于 with_setup')

@with_setup(setup_deco,teardown_deco)
def test_2b_decorated():
	print "Run for test_2b_decorated"
	assert multiply(3,4)==12

class TestUM():
	def setup(self):		# <-- class's function level setup
		print('setup 方法执行于本类中每条用例之前')

	@classmethod
	def setup_class(cls):     # <-- class level setup
		print('setup_class 类方法执行于本类中任何用例开始之前,且仅执行一次')

	def test_strings(self):
                print "Run for test_strings"
		assert multiply('a',3)=='aaa'
```

### Output
Run for 2 test case,
 - first nose_usecase_1.TestUM.test_strings,
 - then nose_usecase_1.test_2b_decorated.
``` shell
╰> nosetests nose_usecase_1.py -s -v
setup_module 函数执行于一切开始之前
setup_class 类方法执行于本类中任何用例开始之前,且仅执行一次
nose_usecase_1.TestUM.test_strings ... setup 方法执行于本类中每条用例之前
Run for test_strings
ok
nose_usecase_1.test_2b_decorated ... setup_deco 将用于 with_setup
Run for test_2b_decorated
teardown_deco 也将用于 with_setup
ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```

### nose 的 discovery 规则为：

1. 长得像测试用例，那就是测试用例。
路径、模块（文件）、类、函数的名字如果能和
testMatch 正则表达式匹配上，那就会被认为是一个用例。另外所有 unittest.TestCase
的子类也都会被当做测试用例。（这里的 testMatch
可能是个环境变量之类的东西，我没有去查，因为反正你只要以 test_
开头的格式来命名就可以保证能被发现）

2. 如果一个文件夹既长得不像测试用例，又不是一个包（路径下没有
__init__.py）的话，那么 nose 就会略过对这个路径的检查。

3. 但只要一个文件夹是一个包，那么 nose 就一定会去检查这个路径。

4. 显式避免某个对象被当做测试用例的方法为：给其或其容器添加一个 __test__ 属性，并且运算结果不为 True。
并不需要直接指定为 False，只要 bool(__test__) ==False即可。
另外，这个属性的添加方式比较特别，确认自己已经掌握使用方法前最好都试试。
例如在类里面需要添加为类属性而非实例属性（即不能写在__inti__(self) 里），否则不起作用。这里因为只是简介，就不挨个试了。（官方文档里就没解释清楚...）


### 调用 discovery 的语法
cd 到目录后直接调用 $nosetests，后面不跟具体的文件名。
另外这种方法其实对 unittest 也适用.



## pytest


https://my.oschina.net/lionets/blog/269892

module name: pytest
run command: py.test

pytest 与 nose 的基本用法极其相似。

### pytest 的 setup/teardown 使用方式

see `pytest_usecase_1.py`

```python
import pytest

@pytest.fixture(scope='function')
def setup_function(request):
    def teardown_function():
        print("teardown_function called.")
    request.addfinalizer(teardown_function)
    print('setup_function called.')

@pytest.fixture(scope='module')
def setup_module(request):
    def teardown_module():
        print("teardown_module called.")
    request.addfinalizer(teardown_module)
    print('setup_module called.')

def test_1(setup_function):
    print('Test_1 called.')

def test_2(setup_module):
    print('Test_2 called.')

def test_3(setup_module):
    print('Test_3 called.')
```

pytest 创建测试环境（fixture）的方式如上例所示，通过显式指定 scope='' 参数来选择需要使用的 pytest.fixture 装饰器。
即一个 fixture 函数的类型从你定义它的时候就确定了，这与使用 @nose.with_setup() 十分不同。
对于 scope='function' 的 fixture 函数，它就是会在测试用例的前后分别调用 setup/teardown。
测试用例的参数如 def test_1(setup_function) 只负责引用具体的对象，它并不关心对方的作用域是函数级的还是模块级的。

有效的 scope 参数限于：'function','module','class','session'，默认为 function。

运行上例：$ py.test some_test.py -s。 -s 用于显示 print() 函数


### Output
from the running result ,
py.test cmd will discover all testable items, here, is `test1 ~ 3`.

Run for `test_1` first, this envolved `setup_function`.
When run for `test_2` and `test_3`, envolved `setup_module` only once, its `teardown_module` is run when no `test_*` need it anymore.

```
collected 3 items
pytest_usecase_1.py define setup_function
setup_function called.
Test_1 called.
.teardown_function called.   <-- the first . means test_1 is passed
define setup_moudle
setup_module called.
Test_2 called.
.Test_3 called.              <-- the first . means test_2 is passed
.teardown_module called.     <-- the first . means test_3 is passed
```


## pytest 与 nose 二选一

https://my.oschina.net/lionets/blog/269892

首先，单是从不需要使用特定类模板的角度上，nose 和 pytest 就较于 unittest 好出太多了。

pythontesting.net 的作者非常喜欢 pytest，并表示 “如果你挑不出 pytest 的毛病，就用这个吧”。

>于是下面我们就来挑挑 pytest 的毛病：
它的 setup/teardown 语法与 unittest 的兼容性不如 nose 高，实现方式也不如 nose 直观.
第一条足矣.
毕竟 unittest 还是 Python 自带的单元测试框架，肯定有很多怕麻烦的人在用，所以与其语法保持一定兼容性能避免很多麻烦。即使 pytest 在命令行中有彩色输出让我很喜欢，但这还是不如第一条重要。
实际上，PyPI 中 nose 的下载量也是 pytest 的 8 倍多。
所以假如再继续写某一个框架的详解的话，大概我会选 nose 吧。
