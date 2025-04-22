import numpy as np
a=np.arange(12).reshape(3,4)

for cell in a.flatten():
    print(cell)
    

#---------------Iterate Numpy array using nditer------------------------
print("\n using C order")
for x in np.nditer(a,order='C'):
    print(x)

#printing fortran order i.e column order
print("\n using F order")
for x in np.nditer(a,order='F',flags=["external_loop"]):
    print(x)

print("\n using A order")
for x in np.nditer(a,order='A'):
    print(x)  

print("\n using K order")
for x in np.nditer(a,order='K'):
    print(x)      

#should follow the general broadcasting rules for iteration simultaneously
b=np.arange(3).reshape(3,1)
for x,y in np.nditer([a,b]):
    print(x,y)