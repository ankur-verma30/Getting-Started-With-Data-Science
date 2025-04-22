#----------------Numpy:Slicing/Stacking  and indexing with Boolean arrays-----------

import numpy as np

a=np.array([6,7,8])
print(a[0:2])

#accessing the last element of the array
print(a[-1])

b=np.array([[6,7,8],[1,2,3],[9,3,2]])
print(b[1][2])
print(b[1,2]) #both gives the same result

#slicing in 2-D array
SlicedB=b[0:2,2]
print(SlicedB) #goes to the first 0th row and first row and print the 2nd column of the selected rows 
#Here 2nd column of 0th and 1st row is selected

#to fetch the last row of the array
lastRowofB=b[-1]
print(lastRowofB)

#in last row if we have to do slicing based on columns
lastCoumnOfLastRow=b[-1,0:2]
print(lastCoumnOfLastRow) # gets first two element 0 and 1

LastTwoColumnOfB=b[:,1:]
print(LastTwoColumnOfB)

#printing the array


for row in b:
    for element in row:
        print(element, end=' ')
    print()


#flat the whole array
for cell in b.flat:
    print(cell)


#Stacking two arrays together

c=np.arange(6).reshape(3,2)
d=np.arange(6,12).reshape(3,2)

print(c)
print(d)


#column should be same
VerticalStackingCandD=np.vstack((c,d))
print(VerticalStackingCandD)

#horizontal stacking row should be same
horizontalStackCandD=np.hstack((c,d))
print(horizontalStackCandD) 


print("\n Splitting the array")
e=np.arange(30).reshape(2,15)
result=np.hsplit(e,3)

for splitArray in result:
    print(splitArray)

print("\n Indexing in boolean array")    

f=np.arange(12).reshape(3,4)
booleanArray=f>4
print(booleanArray)

#Extracting element that satisfies any conditions
print(f[booleanArray]) # this will return the numbers which hold the value true such as [5,6,7,8,9,10,11]

#can be replaced with any value if it holds true
f[booleanArray]=-1 # for true condition
print(f) # all the numbers that satisfies the condition are changed to -1