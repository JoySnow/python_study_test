

nose 不是 Python 官方发行版的标准包.

nose 的口号就是：
    扩展 unittest，nose 让测试更简单。


另外非常棒的一点是，nosetests 兼容对 doctest 和 unittest
测试脚本的解析运行。如果你认为 nose 比那两个都好用的话，完全可以放弃 doctest 和
unittest 的使用。


由于扩展自 unittest，nose 也支持类似于 setUp() setUpClass() setUpModule()
的测试环境创建方式，只不过函数命名规则最好改一改，我们可以使用更符合 Python
规范的命名规则。另外因为 nose
支持上例中所展示的函数式测试用例，所以还有一种为单个函数创建运行环境的装饰器可用。下面我们将使用一个例子来展示这四种功能的用法。




See `nose_usecase_1.py`
run with `nosetests -v -s nose_usecase_1.py`


#### nose 的 discovery 规则为：

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


#### 调用 discovery 的语法为，
cd 到目录后直接调用 $nosetests，后面不跟具体的文件名。另外这种方法其实对 unittest 也适用.
