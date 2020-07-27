#!/usr/src/env python3

import numpy as np

a = np.array([[1.,2.], [3.,4.]])

a.transpose()

# Takes inverse of a square matrix
np.linalg.inv(a)

# eye represents "I" and is a unit matrix
u = np.eye(3)
# print(u)

j = np.array([[0., -1.], [1., 0.]])
k = np.array([[1., 3.], [2., 0.]])
# print(j@k)

# The trace of a matrix is the sum of the diagonal
print(np.trace(u))

y = np.array([[5.],[7.]])
print(np.linalg.solve(a,y))

print(np.linalg.eig(j))
