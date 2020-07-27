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
    c = np.floor(10*np.random.rand(3,3))
    d = np.floor(10*np.random.rand(3,3))

    e = np.vstack((c,d))
    # print(e.shape)
    # (6, 3)

    f = np.hstack((c,d))
    # print(f.shape)
    # (3, 6)

    """
    np.column_stack is used to stack 1D arrays as columns intoa  2D array
    it is equivalent to hstack but only for 2D arrays

    np.row_stack is equivalent to vstack for 2D arrasy
    """


    # Viewing a as a 2D column vector:
    # print(a[:,np.newaxis])

    ## Splitting an array into smaller ones:

    a = np.floor(10*np.random.rand(2,12))
    # print(a)
    split_a = np.hsplit(a,3)
    # print(split_a)

    # Splits a after the third and fourth column
    split_a_2 = np.hsplit(a, (3,4))
    # print(split_a_2)

    


if __name__=="__main__":
    main()