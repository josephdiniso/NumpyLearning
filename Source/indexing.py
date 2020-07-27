#!/usr/bin/env python3

import numpy as np

import sys

def main():
    # One-dimensional arrays can be indexed and slices like Python lists
    a = np.arange(10)
    # print(a[2:5])

    a[:6:2] = 1000
    # print(a)

    b = np.arange(0,30,2).reshape(3,5)
    # Prints fifth element in axis 1 for all of axis 0
    print(b[:,4])

    # NOTE: When fewer indices than axes are provided, the missing
    # indices are assumed to be complete slices (:)
    # eg: a[-1] is the same as a[-1,:]

    # NumPy allows you to fill in (:) with ...
    c = np.arange(30).reshape(-1,1,1,3)
    print(c[...,0,0])

    d = np.arange(9).reshape(3,3)
    # Iterating will be done wrt the first axis
    for row in d:
        print(row)
        pass
    
    # To perform operation on each element in array
    for element in d.flat:
        print(element)
        pass




if __name__ == "__main__":
    main()