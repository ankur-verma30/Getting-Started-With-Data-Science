import numpy as np


#Creating 1-D array using numpy
a=np.array([5,6,7])
print(a[0])

#to find the dimensions of the array it is a property not a function
b=np.array([[1,2,3],[4,3,1]])

print(b.ndim)

c=np.array([[1,2],[3,4]], dtype=np.float64)
print(c.itemsize)

print(b.shape) 

#can reshape the array the dimensions must be compitable so that reshape can be done 
reShapeB=b.reshape(3,2)

print(reShapeB)

#print the whole array with 0 
d=np.zeros((2,3))
print(d)

#same for ones
e=np.ones((2,3))
print(e)


#follows all the property of list 
f=range(10)
print(f) # this is an list from 0 to 9 inclusive

g=np.arange(10)
print(g)

#prints the number with the step counter which is the third parameter
h=np.arange(1,6,2)
print(h)

#this will generate the array of  20 numbers linearly spaced between 1 to 5 inclusive its take three parameters start point,end point, total numbers you want to generate
i=np.linspace(1,5,20)
print(i)


# to flaten any array dimension to 1-D using ravel function
#ravel function does not modify the array it always returns a new array
flattenReShapeB=reShapeB.ravel()
print(flattenReShapeB)


#-----------------------------------MATHEMATICAL FUNCTIONS---------------------------

#finding min and max in the array
minofB=flattenReShapeB.min()
print(minofB)

#summation of all the numbers using sum function
sumOfB=flattenReShapeB.sum()
print(sumOfB)


#can print the sum according to the axis wise like 0 as y x as 1 and z as 2

j=np.array([[1,2,3],[4,5,6],[7,8,9]])
#summation of values that are present at x axis

SumOfJXaxis=j.sum(axis=0)
print(SumOfJXaxis) #gives the sum of all the 3 rows which are present at x axis in 2-D array

# SumOfJZaxis=j.sum(axis=2)
# print(SumOfJZaxis) # gives an error if not z axis exit in the matrix


#find the sqrt of each element using generic np.sqrt function on any array

SqrtOfJ=np.sqrt(j) #does not alter the values of j instead create a new array
print(SqrtOfJ)

#similary find the standard deviation of any array, using np.std method and it also returns the new array
StandardDeviatioOfJ=np.std(j)
print(StandardDeviatioOfJ)

#can add/subtract/multiplication/division two array of same dimension


#can do a matrix product i.e scalar product or dot product
k=np.array([[3,4],[5,6]])
l=np.array([[7,8],[9,10]])

KDotProductL=k.dot(l)
print(KDotProductL)
 