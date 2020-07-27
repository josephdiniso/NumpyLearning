#!/usr/src/env python3

import numpy as np

"""
NumPy allows you to index with an array of indices
"""

a = np.arange(12)**2

b = np.array([1,4,8])
# print(a[b])


"""
When the indexed array is multidimensional, a single array of indices refers 
to the first dimension of a.
"""

palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white
image = np.array([[0, 1, 2, 0],        # each value corresponds to a color in the palette
                  [0, 3, 4, 0]])
# (2, 4, 3) color image
# print(palette[image])

"""
Can also give indices for multiple dimensions, however the arrays of indices
must have the same shape
"""

a = np.arange(12).reshape(3,4)
"""
[[0,1,2,3],
[4,5,6,7],
[8,9,10,11]]
"""
# Vertical dimension, axis 0
i = np.array([[0,1],[1,2]])
# Horizontal dimension, axis 1
j = np.array([[2,1],[3,3]])

# print(a[i,j])

"""
Indexing with arrays can be used to find the maximum value of time dependent
series
"""

time = np.linspace(20,145,5)
# Gives four time dependent series
data = np.sin(np.arange(20)).reshape(5,4)

# Returns indices of max in each row
ind = data.argmax(axis=0)

time_max = time[ind]

# Gives max data point in each row
data_max = data[ind, range(data.shape[1])]

"""
Indexing with boolean arrays

Most natural usage of indexing with boolean arrays is with an array of the same
shape as the target array
"""

a = np.arange(6).reshape(3,2)
# Returns an array of all indices where elements of a are greater than 4
b = a > 4
# print(a[b])
a[b] = 0
# print(a)

"""
Second method of boolean indexing is to give an array of which indices on an 
axis we wish to use
"""

a = np.arange(6).reshape(3,2)
b1 = np.array([False, False, True])
b2 = np.array([True, False])
# print(a)
# print(a[b1,b2])