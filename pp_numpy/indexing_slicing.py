import numpy as np
'''
Indexing, slicing, and striding for NumPy arrays works the same way as for tuples/lists or nested tuples/lists:

    Indexing:
        Index is an integer number
        Index counting is zero-based
        Negative indices are ok
        Index is specified in square brackets
        Range of index values for the target axis_value:
            positive: np.size (a, axis = axis_value) - 1
            negative: -np.size (a, axis = axis_value)
        For multi-dimensional array: comma-separated indices for each axis
    Slicing and striding:
        [start:stop:step]: square brackets specifying the subarray pattern: start, stop and step of the slice for access along a specific axis
            each element describing the pattern is optional
            negative values are ok
            the rules for range values are the same as for the index
        For multidimensional slice: a comma-separated tuple of subarray access patterns along each axis
            [start,stop): half open interval
    Subarray is a view not a copy
        changes in the subarray, change the main array
        use np.copy() function to explicitly create a copy of the subarray in order to prevent modifying the array when changing the subarray
'''

x1d = np.array([5, 4, 3, 2, 1, 0])
print(x1d[0], x1d[-1], sep='\t')

x2d = np.reshape(x1d, (2, 3))
print(x2d)
print(x2d[0, 0], x2d[-1, -1], sep='\t')

# multi-dimensional indexing
m = np.random.randint(0, 100, (3, 4))
print(m)

print(m[0, 0], m[-3, -4])
row = np.size(m, axis=0)
col = np.size(m, axis=1)
print(m[row-1, col-1])

# multi-dimensional subarray
a = np.arange(12)
ma = np.reshape(a,(3,4))
print(ma)

print(ma[:2,:3])

print(ma[::-1,::-1])

#access rows or columns
print(ma[2,:])
print(ma[:,2])

#subarray vs copy
sma = ma[:2,:2]
sma[0,0]=100
print(sma, ma, sep='\n')

cma = np.copy(ma)
cma[0,0]=200
print(cma, ma, sep='\n')