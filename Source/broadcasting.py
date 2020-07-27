#!/usr/bin/env python3

import numpy as np

"""
Broadcasting allows universal functions to deal in a meaningful way with inputs 
who do not have the same shape

If all input arrays do not have the same number of dimensions, the array is '1'
fills until they are all of the same shape

Broadcasting ensures that arrays with a size of 1 along a particular dimension 
act as if they had the size of the array with the largest shape along that 
dimension
"""