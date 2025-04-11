book={}
 
book['tom']={
    'name':'Tom',
    'address':'1 street, NY',
    'phone':34567890,
} 

book['Joe']={
    'name':'Joe',
    'address':'2 street, NY',
    'phone':56789023,
}

import json
s=json.dumps(book)

print(s)
with open('data.txt','w') as f:
    f.write(s)

print("\nI am going to read the files now\n")
readingFiles=0
with open('data.txt','r') as f:
    readingFiles=f.read()

print(readingFiles) #this gives the string    

newBook=json.loads(readingFiles)
print(newBook) #this gives the dictionary when we loads the string using json method

#nested indexing
print(book['Joe']['phone'])


