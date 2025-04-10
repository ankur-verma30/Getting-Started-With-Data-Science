print('Hello World')

items=['Bread','Pasta','Fruits','Veggies']
items.insert(1,'Butter') #can be done at any position
print(items)

indian=['samosa','daal','naan']
chinese=['egg role','pot stickers','fried rice']
italian=['pizza','pasta','risotto']

'''dish=input('Enter the dish name :')

#conditional if-else condition
if dish in indian:
    print('indian')
elif dish in chinese:
    print('chinese')
else:
    print('italian')  ''' 


#Loop or Iterators
for dishes in indian:
    print(dishes)         

expanse=[1250,2500,2100,3100,2980]

sum=0
for money in expanse:
    sum+=money

print('The total sum of expanse is:',sum)

#range based looping 
total=0
n=len(expanse)
for i in range(0,n-1): #last index is excluded 
    total+=expanse[i] #in range it is used as a index coming out of range

print(total)  

