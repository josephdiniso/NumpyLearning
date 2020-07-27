#!/usr/bin/env python3

import numpy as np

def main():
    # The shape of an array is the number of elements along each
    # axis

    # NOTE: The following three methods will return a modified
    # array but not change the original

    a = np.arange(15).reshape(-1, 5)

    # Returns the array, flattened
    # print(a.ravel())

    # Returns reshaped array
    # print(a.reshape(-1,5))

    # Returns array, transposed
    # print(a.T)

    # Resize method changes the original array
    a.resize((5,3))

    # Returns reshaped array
    b = a.reshape(-1,5)

    # Stacking arrays
    c = np.random.rand(3,3)
    c = np.floor(10*np.random.rand(3,3))
    print(c)

if __name__=="__main__":
    main()