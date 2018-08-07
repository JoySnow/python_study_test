
https://my.oschina.net/lionets/blog/268542

doctest 是一个 Python 发行版自带的标准模块.


#### Use-case-1:

put the doctest lines as docsting into code, see `doctest_usecase_1.py`.



#### Use-case-2:

如果不想（或不能）把测试用例写进源代码里，则还可以使用一个独立的文本文件来保存测试用例。

See `doctest_example.txt`:

```
$cat example.txt
>>> from doctest_usecase_1 import multiply
>>> multiply(2,3)
6
>>> multiply('baka~',3)
'baka~baka~baka~'

```

In command line, call:
```
python -m doctest -v doctest_example.txt
```


#### Test Output:
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
