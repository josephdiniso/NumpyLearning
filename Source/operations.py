#!/usr/bin/env python3

import numpy as np

import sys


def main():
    a = np.array([20,30,40,50])
    b = np.arange(4)
    # Can perform all element-wise operations

    b**2

    np.sin(a)

    # print(a<35)

    ## Array Multiplication

    """
    In NumPy the * operator operates elementwise

    To calculate the matrix product use the @ operator
    or the dot function/method
    """

    A = np.array( [[1,1], [0,1]])
    B = np.array( [[2,0], [3,4]])

    # Elementwise product
    # print(A*B)
    """
    [[2 0]
      [0 4]]
    """

    # print(A @ B)
    # print(A.dot(B))
    """
    [[5 4]
    [3 4]]
    """

    """
    NumPy's unary operations are methods of arrays
    .sum(), .min(), .max()
    By default these operations apply to the array as a whole, but
    axis can be specified
    """

    b = np.arange(12).reshape(3,4)

    # print(b)
    # print(b.max())
    # 11
    # print(b.max(axis=1))
    #  [3 7 11]

    # Sums first axis which is vertical
    # print(b.sum(axis=0))
    
    # Cumulative sum along each row
    """
    NOTE: Cumulative sum is a sequence of sums
    cumsum([1,2,3,4]) is:
    [1,1+2,1+2+3,...]
    """
    print(b.cumsum(axis=1))

    """
    NumPy provides support for mathematical functions
    np.-
    exp()
    sqrt()
    add(A,B)
    
    """
    

if __name__ == "__main__":
    main()