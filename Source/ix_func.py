#!/usr/src/env python3

import numpy as np

"""
ix_() function is used to combine different vectors to obtain th eresult for
each n-uplet

For example, if you wished to compute all the a+b*c for all the triplets taken
from each of the vectors a, b, and c:
"""

a = np.array([2,3,4,5])
b = np.array([8,5,4])
c = np.array([5,4,6,8,3])

ax, bx, cx = np.ix_(a,b,c)

result = ax+bx*cx
result_i = result[3,2,4]
result_i_2 = a[3]+b[2]*c[4]
print(result_i, result_i_2)

"""
A function to give all combinations of a specified function
"""
def ufunc_reduce(ufct, *vectors):
   vs = np.ix_(*vectors)
   r = ufct.identity
   for v in vs:
       r = ufct(r,v)
   return r

results = ufunc_reduce(np.add, a,b,c)
# print(results[1,2,3])
# print(a[1]+b[2]+c[3])