def calculateArea(sides):
    return sides*sides

if __name__=="__main__": #used as entry point for the python program
    a=calculateArea(20)
    print("Area", a)

#Handling Exception
x=int(input("Enter number1: "))
y=int(input("Enter number1: "))
try:
    z=x/y
    print("Divison is", z)
except Exception as e:
    print("Exception occured",type(e).__name__)
    z='None'
    print(z)