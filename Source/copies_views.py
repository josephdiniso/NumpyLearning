#!/usr/bin/env python3

import numpy as np

a = np.floor(np.random.rand(5,5))

# Makes no new array, b is just a reference to a
b = a
# print(b is a)

def f(x):
    print(id(x))

# Will be the same, because function calls don't make a copy
# print(id(a))
# print(f(a))

"""
View or Shallow Copy:

The .view() method creates a new array object that looks at the same data but
is not the same as the original

if c = a.view()
then c is not a but c.base IS a
c.flags.owndata is false and changes to c do not affect a

You can change the data of a from c but not the shape

Slicing an array returns a view of it
"""

# Deep copy creates an entirely new array
d = a.copy()
# print(d is a)
# False

"""
If slicing an array and you don't need the original, you can copy is and delete
the original
"""

a = np.arange(int(1e8))
b = a[:100].copy()
del a

