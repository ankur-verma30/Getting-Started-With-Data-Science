class Human():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    def walking(self):
        print('The ',self.name," is walking") 

human1=Human('Ankur',23,'Male');

print(human1.name)
print(human1.age)
print(human1.gender)
        