def sum(a,b):
    """
    Sum of two numbers Documentation String
    """
    print('a' ,a)
    print('b' ,b)
    total=a+b
    print('Total inside function ',total)
    return total

n=sum(b=5,a=6) #known as named argument after naming they do not follow the order 
print('Total outside the function', n)

d={1:1,2:4,3:9,4:16}

#Method 1
for key in d:
    print("The key is ",key,"and the value is",d[key])

print("This is the method 2 for iterating on dictionaries")
#Method 2
for key,value in d.items():
    print("The key is ",key,"and the value is",value)


#Searching in dictionary

if 1 in d:
    print("The value is", d[1])

#Tuples in python they are immutable
point=(3,7)    

