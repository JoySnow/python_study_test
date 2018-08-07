
https://my.oschina.net/lionets/blog/269892

pytest 有时也被称为 py.test，是因为它使用的执行命令是 $ py.test。

pytest 与 nose 的基本用法极其相似。
因此只做一个比较就好了。

他俩的区别仅在于:
 - 调用测试的命令不同，pytest 用的是 $ py.test
 - 创建测试环境（setup/teardown）的 api 不同

 pytest 的 setup/teardown 使用方式。


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




#### pytest 与 nose 二选一

首先，单是从不需要使用特定类模板的角度上，nose 和 pytest 就较于 unittest 好出太多了。doctest 比较奇葩我们在这里不比。因此对于 “选一个自己喜欢的测试框架来用” 的问题，就变成了 nose 和 pytest 二选一的问题。

pythontesting.net 的作者非常喜欢 pytest，并表示

 “如果你挑不出 pytest 的毛病，就用这个吧”。

于是下面我们就来挑挑 pytest 的毛病：

它的 setup/teardown 语法与 unittest 的兼容性不如 nose 高，实现方式也不如 nose 直观.

第一条足矣
毕竟 unittest 还是 Python 自带的单元测试框架，肯定有很多怕麻烦的人在用，所以与其语法保持一定兼容性能避免很多麻烦。即使 pytest 在命令行中有彩色输出让我很喜欢，但这还是不如第一条重要。

实际上，PyPI 中 nose 的下载量也是 pytest 的 8 倍多。

所以假如再继续写某一个框架的详解的话，大概我会选 nose 吧。
