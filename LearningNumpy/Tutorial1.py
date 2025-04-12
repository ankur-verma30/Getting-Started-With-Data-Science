"""Numpy is used for scientific computing"""
#It's most useful feature is n dimensional array object (a.k.a nd array)

import numpy as np

a=np.array([1,2,3])

print(a)

"""
Benifits of numpy array over a python list
1. Less memory
2. Fast
3. Convinent
"""
import sys

l=range(1000)
print("This is the length of the conventional list in python",sys.getsizeof(5)*len(l))

array = np.arange(1000)
print("This is the size of the numpy array ",array.size*array.itemsize)

#checking the speed difference between numpy and list
size=1000
l1=range(size)
l2=range(size)

a1=np.arange(size)
a2=np.arange(size)

import time
start=time.time()

result=[(x+y) for x,y in zip(l1,l2)]
print("Python list took: ",(time.time()-start)*1000)

start=time.time()
result=a1+a2
print("Numpy Array took: ", (time.time()-start)*1000)


