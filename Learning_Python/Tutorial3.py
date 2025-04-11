import math

print(math.sqrt(16))
print(dir(math))


#importing calender
import calendar
cal=calendar.month(2016,1)
print(cal)

print("Is 2025 is a Leap Year",calendar.isleap(2025))

#Importing the custom  module
#if you want to import from another folder then folderName.moduleName
import Module as m
areaOfSquare=m.area_of_square(25)
print(areaOfSquare)

#Working with JSON
 