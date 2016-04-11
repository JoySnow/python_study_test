# Test sys.argv[]
# from:
#   http://www.linuxidc.com/Linux/2012-02/53764.htm
# run it like this:
#   python sys_argv.py a b c d and what ?? \> 1

import sys

print "script file name: ", sys.argv[0]

for i in range(1, len(sys.argv)):
    print "argment ", i, ": ", sys.argv[i]
