#!/usr/bin/env python3

import numpy as np

import sys

def main():
    arr = np.array([[1,0,0], [3,4,5]], dtype=np.int64)

    # print(arr.shape)
    # (2, 3)

    # print(arr.size)
    # 6

    # print(arr.dtype)
    # int64

    # print(arr.itemsize)
    # 8 (bytes)

    # print(arr.data)
    # Memory address of array

    ## Analogous to Python's range function
    arr_2 = np.arange(30).reshape(2,3,5)
    # print(arr_2)

    arr_3 = np.arange(0,12,2).reshape(2,3)
    print(arr_3)

    zeros = np.zeros((3,3,3))
    # print(zeros)

    ones = np.ones((2,5,3))
    # print(ones)

    empties = np.empty((3,5))
    # print(empties)

    """
    Linspace is better for floating point range
    because it is not possible to predict elements obtained because of 
    floating point precision
    """
    # Specifies the number of elements you want instead of step size
    lin_space = np.linspace(0, 2, 9)
    lin_space = lin_space.reshape((3,3))
    # print(lin_space)

    """
    Printing array:

    Last axis is printed from left to right
    Second to last axis is printed top to bottom
    Rest are printed top to bottom, with each slice
        separated by an empty line
    
    NumPy by default skips central part of array if it is
    too large. To disable this behavior, change print options:
    """

    np.set_printoptions(threshold=sys.maxsize)





if __name__ == "__main__":
    main()
