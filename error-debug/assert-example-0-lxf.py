# http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832284796780f5db7b5744bf9989f8d845ef77712000

# When run with '-O'(OPQ not 012) argument,
# it will treat all asserts as pass sentences,
# like: "$ python -O name.py"
# Much BETTER than print.

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()
