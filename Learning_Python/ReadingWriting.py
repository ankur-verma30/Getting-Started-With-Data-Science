# '''
# f=open('ReadingWriting.txt','a') #to prevent from overwriting
# f.write('Hello World')
# f.write('\tThis is a developer')
# f.close()
# '''
f=open("ReadingWriting.txt","r") #there are so many modes
for line in f:
    count=0
    for ch in line:
        count+=1
    line+=str(count)    
    print(line)
f.close()


#use with statement helps to automatically automatically closed after the work is done 
#to check it is closed can be done is 
print(f.closed) #if closed gives true
