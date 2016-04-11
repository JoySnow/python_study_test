# Test getopt.getopt
# from:
#   http://www.linuxidc.com/Linux/2012-02/53764.htm
# run it like this:
#   python getopt_getopt.py -o ndjk -i iii --version --file=hhh -h what?

import sys, getopt

# getopt.getopt(args, options[, long_options])
# arguments:
#         h is for "-h"
#         i is for "-i value"
#   version is for "--version"
#     file= is for "--file=value"
# return value:
#   opts is a list for matched arguments.
#       [('-o', 'ndjk'), ('-i', 'iii'), ('--version', ''),
#        ('--file', 'hhh'), ('-h', '')]
#   args is a list for unmatched arguments.
#       ['what?']
opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["version", "file="])

print opts
print args

for op, value in opts:
    if op == "-i":
        print "input = ", value
    elif op == "-o":
        print "output = ", value
    elif op == "--version": #no value for version
        print "version = 0.0.1, miao", value
    elif op == "--file":
        print "file= is ", value
    elif op == "-h":    # no value for -h
        print "help = ", value
        print ":) ...././.-../.--. (:"
        sys.exit()
