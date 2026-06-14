#Classes are user defined blueprint or prototype
#Class will have methods, class variables, instance variables, constructors etc
#Self keywords are mandatory for calling variables into methos
#Constructor name should be init
#New keyword is not required when you create object

class Calculator:
    num = 100#class variables and it will be constant no matter how many obj created
    num1 = 50
    #default constructor

    def __init__(self, a, b):
        self.firstnumber = a #instance variable declared under constructor. here firstnumber etc is instance variable and self is obj
        self.secondnumber = b

        print("I am called automatically when object is created")

    def getdata(self):
        print("I am now executing as method in class Calculator")
    def summation(self):
        return self.firstnumber + self.secondnumber + self.num + self.num1


obj = Calculator(2, 3)#syntax to create objects in python
obj.getdata()
print(obj.num)
print(obj.summation())

obj1 = Calculator(5, 6)
obj1.getdata()
print(obj1.num)
print(obj1.num1)
print(obj1.summation())