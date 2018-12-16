# the order will be changed;
# Time: O(n); Space: O(n)

old_lst = ['1', 'asd', 2, 4.5]
d = {}
NUL = None

for k in old_lst:
    d[k] = NUL

new_lst = d.keys()

for k in d:
    print id(k)


# the order won't be changed;
# Time: O(n*n), Space: O(n)
#output = []
#for x in trends:
#    if x not in output:  # O(n), https://wiki.python.org/moin/TimeComplexity
#        output.append(x)
#print output


# Will sort first. can also keep output in order.

import numpy as np
#>>> a = np.array(['a', 'b', 'b', 'c', 'a'])
#>>> u, indices = np.unique(a, return_index=True)
#>>> u
#array(['a', 'b', 'c'],
#>>> indices
#array([0, 1, 3])
#>>> a[indices]
#array(['a', 'b', 'c'],
#

old_lst = ['1', 'asd', 2, 4.5, 2]
a = np.array(old_lst)
u, indexs = np.unique(a, return_index=True)
print u
print indexs
print type(u)
rs = u.tolist()
print type(rs), rs

print a[indexs]
print type(a[indexs])
print type(a[indexs].tolist())

u, indexs = np.unique(a)
