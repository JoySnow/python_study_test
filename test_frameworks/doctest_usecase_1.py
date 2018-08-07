"""
https://my.oschina.net/lionets/blog/268542

"""

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
