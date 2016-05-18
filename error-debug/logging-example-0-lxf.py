# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832284796780f5db7b5744bf9989f8d845ef77712000

import logging
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename="./logging-example-0-lxf.log")

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
