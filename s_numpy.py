import numpy as np

# Random
arr = np.random.random((5,6))
print(arr)

arr = np.random.randint(1,10,(5,6))
print(arr)

arr = np.random.normal(10,2,(5,6))
print(arr)

# Default 
arr = np.zeros((3,4),dtype=int)
print(arr)

arr = np.eye(5)
print(arr)

arr = np.full((3,2),fill_value=5)
print(arr)

arr = np.arange(1,10,2)
print(arr)

arr = np.linspace(1,10,5)
print(arr)


# from list objects
arr=np.array([1,2,3])
print(arr)

arr=np.array([[2,4],[3,5]])
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(np.size(arr,axis=0))