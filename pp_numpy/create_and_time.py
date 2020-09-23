import numpy as np
from timeit import default_timer as time
from timeit import timeit
from timeit import Timer


'''
How to Create a NumPy Array
There are multiple ways to create a NumPy Array of type ndarray:

    np.empty(): Empty uninitialized array
    np.zeros(), np.ones(), np.full(), np.eye() as well as np.arange(), np.linspace(): arrays from scratch with pre-defined values of zeros, ones, fill values, or identity matrix (1 on the diagonal), respectively, as well as an array filled with a linear sequence in the range of values
    np.array(list_obj): array from a list object or a nested list of lists for a multi-dimensional array
    np.random.random(), np.random.normal(), np.random.randint(): array of random float or integer numbers drawn from a uniform or normal distribution
'''
# Random
arr = np.random.random((5,6))
arr = np.random.randint(1,10,(5,6))
arr = np.random.normal(10,2,(5,6))

# Default 
arr = np.zeros((3,4),dtype=int)
arr = np.eye(5)
arr = np.full((3,2),fill_value=5)
arr = np.arange(1,10,2)
arr = np.linspace(1,10,5)

# from list objects
arr=np.array([1,2,3])
arr=np.array([[2,4],[3,5]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(np.size(arr,axis=0))

arr = np.array([[2,3,4],[5,6]])
print(arr.ndim)
print(arr.shape)
print(arr.size)

'''
Big Arrays: Loops vs. Vectorized Operations
    Vectorized operations:
        The same operation is applied to each element of the array or each subarray
            e.g., the sum of all elements in each row of the 2-d array
        Generally implemented through NumPy's universal functions (ufuncs):
            e.g., np.sum(), np.multiply()
    Loops are slow for such operations:
        Order of magnitude performance degradation
'''
how_big = 1000
fa = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='F')
ca = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='C')

nrow = fa.shape[0]
ncol = fa.shape[1]

# Row sum, using loop
rsum = np.zeros(nrow,dtype=int)
start = time()
for i in range(0,nrow):
    rsum[i] = 0
    for j in range(0,ncol):
        rsum[i]+=fa[i,j]
end = time()
print('Row sum time for F-array:{0:1.2E} sec'.format(end-start))

start = time()
for i in range(0,nrow):
    rsum[i] = 0
    for j in range(0,ncol):
        rsum[i]+=ca[i,j]
end = time()
print('Row sum time for C-array:{0:1.2E} sec'.format(end-start))

# Column Sum : using loops
csum = np.zeros(ncol,dtype=int)
start = time()
for j in range(0,ncol):
    csum[j] = 0
    for i in range(0,nrow):
        csum[j]+=fa[i,j]
end = time()
print('Column sum time for F-array:{0:1.2E} sec'.format(end-start))

csum = np.zeros(ncol,dtype=int)
start = time()
for j in range(0,ncol):
    csum[j] = 0
    for i in range(0,nrow):
        csum[j]+=ca[i,j]
end = time()
print('Column sum time for C-array:{0:1.2E} sec'.format(end-start))

# Vectorized sum for F-Array
def row_sum_for_f_array():
    how_big = 1000
    fa = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='F')
    ca = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='C')
    return np.sum(fa,axis=0)

def column_sum_for_f_array():
    how_big = 1000
    fa = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='F')
    ca = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='C')
    return np.sum(fa,axis=1)

def row_sum_for_c_array():
    how_big = 1000
    ca = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='C')
    return np.sum(ca,axis=0)

def column_sum_for_c_array():
    how_big = 1000
    ca = np.array([range(i,i+how_big) for i in list(range(1,how_big+1))],order='C')
    return np.sum(ca,axis=1)

t1 = Timer('row_sum_for_f_array()','from __main__ import row_sum_for_f_array')
t2 = Timer('column_sum_for_f_array()','from __main__ import column_sum_for_f_array')
t3 = Timer('row_sum_for_c_array()','from __main__ import row_sum_for_c_array')
t4 = Timer('column_sum_for_c_array()','from __main__ import column_sum_for_c_array')
comsuption1 = t1.timeit(1)
comsuption2 = t2.timeit(1)
comsuption3 = t3.timeit(1)
comsuption4 = t4.timeit(1)
print (comsuption1,comsuption2)
print (comsuption3,comsuption4)